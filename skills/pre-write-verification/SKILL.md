---
name: pre-write-verification
description: Use before rewriting, replacing or overwriting any existing file or document you did not just read. Confirms task identity, existence, and current content, and shows a diff when the live copy differs from what you expected.
---

# Pre-Write Verification

Writing from a remembered or earlier-read version can silently destroy newer content. Check before you overwrite.

## Core rule

Fresh appends can proceed directly. Any rewrite, substitution or overwrite needs four checks first.

1. **Task identity.** Is this the file and the task the person actually meant? Confirm the name, location and purpose match the request.
2. **Existence.** Confirm the target exists (or does not) by direct listing, not by a single search. See the existence-verification-escalation skill.
3. **Fresh read at write time.** Read the live content immediately before writing. A read from earlier in the session does not count.
4. **Diff and ask.** If the live content differs from what you based your change on, show the difference and ask before overwriting.

## Steps

1. State what you are about to replace and why.
2. Read the live file now.
3. Compare against your base version.
4. If identical, write. If different, show the diff and wait.
5. After writing, check the result (size, diff against the intended content).

## Verify before returning

Report the diff or the confirmation that the live file matched your base version. If you skipped the fresh read, say so.

## Common failure

Treating "I already know what's in it" as a substitute for reading it. Read first, even when confident.
