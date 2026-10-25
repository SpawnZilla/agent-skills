---
name: syntax-self-check
description: Use before writing or editing any code file in a live location. Run a real syntax check on the exact new text first, on every edit, including docstring, comment and prose changes inside code files.
---

# Syntax Self-Check

Reading an edit over is not a syntax check. Before the new text goes into a live file, parse the exact text in a scratch location.

## Core rule

Stage the exact new content outside the live file, run the language's parser or compiler on it, and only then write it to the real location.

- Python: `python3 -m py_compile <staged_file>`
- Shell: `bash -n <staged_file>`
- JSON: `python3 -m json.tool <staged_file>`
- Other languages: the equivalent parse-only or lint command.

Also search the new text for backslash sequences that could be misread, such as `\u` or `\x` inside a string that was meant to be plain text.

## Why it applies to "just a docstring"

Prose is more likely than code to collide with escape and quote syntax, because whoever wrote it was not thinking about the language. A placeholder containing a backslash-u sequence inside an ordinary Python docstring is read as a unicode escape and breaks the file. The same mistake can repeat in one session if the first fix is not generalized.

## Steps

1. Write the exact new file content (or the patched result) to a scratch path.
2. Run the parse-only check for that language.
3. Grep the new text for risky escape sequences.
4. Write to the live path only after both are clean.
5. Re-run the check on the live file after writing.

## Verify before returning

Report the exact command you ran and its result. "Looks fine" is not a result.

## What this does not replace

A syntax check shows the file will parse. It does not show the change is correct. Review the logic separately.
