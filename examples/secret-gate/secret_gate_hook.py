#!/usr/bin/env python3
"""Prompt-submit hook that blocks prompts containing likely credentials.

Reads a JSON object on stdin with the submitted text under "prompt".
Exit 0 lets the prompt through. Exit 2 blocks it and prints a reason to stderr.

Design choices:
- Fails open on unreadable input, so a malformed payload never locks you out.
- Reports only the kind of secret found and a masked preview, never the value.
- Patterns are deliberately few and high-signal. Extend PATTERNS for your stack.
"""
import json
import re
import sys

PATTERNS = [
    ("AWS access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private key block", re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")),
    ("Slack token", re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b")),
    ("API key (sk- style)", re.compile(r"\bsk-[A-Za-z0-9_-]{24,}\b")),
    (
        "credential assignment",
        re.compile(
            r"(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token)\b\s*[:=]\s*['\"]?[^\s'\"]{8,}"
        ),
    ),
]


def mask(text: str) -> str:
    """Show only the first 3 characters of a match."""
    return text[:3] + "***" if len(text) > 3 else "***"


def scan(prompt: str):
    """Return a list of (label, masked_preview) for each finding."""
    findings = []
    for label, pattern in PATTERNS:
        match = pattern.search(prompt)
        if match:
            findings.append((label, mask(match.group(0))))
    return findings


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        prompt = payload.get("prompt", "") if isinstance(payload, dict) else ""
    except (json.JSONDecodeError, OSError):
        return 0
    if not isinstance(prompt, str):
        return 0

    findings = scan(prompt)
    if not findings:
        return 0

    lines = ["Prompt blocked: it appears to contain credentials."]
    for label, preview in findings:
        lines.append(f"  - {label} (starts with {preview})")
    lines.append("Remove or rotate the secret and resubmit without it.")
    print("\n".join(lines), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
