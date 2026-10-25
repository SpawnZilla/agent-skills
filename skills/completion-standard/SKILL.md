---
name: completion-standard
description: Use when reporting that work is done, or when deciding whether to deploy it. Done means carried through to the running state; separate "staged, ready for handoff" from "built and running", and deploy as part of finishing where possible.
---

# Completion Standard

"Done" means the whole path has been carried through to the running or deployed state, unless the person said otherwise. Anything less is a different status and must be named as such.

## Status vocabulary

- **Drafted:** written, not run.
- **Staged:** files in place, ready for handoff, not running.
- **Built and tested:** ran and passed checks in a test setting.
- **Deployed and running:** live, with the live behavior confirmed.

Never use "done" for the first two.

## Deploy when done

If work can be deployed, deploy it as part of finishing rather than leaving it staged for a later session. Where deployment is outside your access, produce a complete, ready-to-run package: exact commands, exact file placements, nothing left to research. State which host or prompt each command runs in.

## Checking completion

Judge completion from everything relevant, never from a subset. Before saying "done":

1. List what the task required.
2. Check each item against the real state (run the check, read the file, query the service).
3. Confirm the running behavior, not just that the files exist.

## Verify before returning

The final report names the status from the vocabulary above, what was checked and how, and anything that is staged but not live.
