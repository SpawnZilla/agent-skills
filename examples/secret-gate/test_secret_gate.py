import json
import subprocess
import sys
import unittest
from pathlib import Path

HOOK = str(Path(__file__).with_name("secret_gate_hook.py"))


def run(payload):
    data = payload if isinstance(payload, str) else json.dumps(payload)
    return subprocess.run(
        [sys.executable, "-I", HOOK],
        input=data,
        capture_output=True,
        text=True,
    )


class SecretGateTests(unittest.TestCase):
    def test_clean_prompt_passes(self):
        r = run({"prompt": "Please refactor the parser and add tests."})
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stderr, "")

    def test_aws_key_blocked(self):
        fake = "AKIA" + "ABCDEFGHIJKLMNOP"
        r = run({"prompt": f"use key {fake} for the upload"})
        self.assertEqual(r.returncode, 2)
        self.assertIn("AWS access key id", r.stderr)
        self.assertNotIn(fake, r.stderr)

    def test_private_key_blocked(self):
        r = run({"prompt": "-----BEGIN " + "RSA PRIVATE KEY-----\nabc"})
        self.assertEqual(r.returncode, 2)

    def test_github_token_blocked(self):
        fake = "ghp_" + "a" * 36
        r = run({"prompt": f"token {fake}"})
        self.assertEqual(r.returncode, 2)
        self.assertNotIn(fake, r.stderr)

    def test_password_assignment_blocked(self):
        r = run({"prompt": "password = hunter2hunter2"})
        self.assertEqual(r.returncode, 2)

    def test_short_password_word_not_blocked(self):
        r = run({"prompt": "reset the password field label"})
        self.assertEqual(r.returncode, 0)

    def test_malformed_input_fails_open(self):
        self.assertEqual(run("not json").returncode, 0)

    def test_missing_prompt_passes(self):
        self.assertEqual(run({"other": 1}).returncode, 0)


if __name__ == "__main__":
    unittest.main()
