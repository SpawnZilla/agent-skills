---
name: doc-sync
description: Use when reconciling a set of living documents (status files, trackers, logs, runbooks) with what happened in the current session, at the end of a session or on a schedule. Read full content and cross-reference before deciding nothing needs updating; never judge by date alone.
---

# Doc Sync

A reconciliation pass between your living documents and what actually happened. The goal is that the next session starts from accurate documents.

## Core principle: content rule

Read the full content of each living document the session touched or could have touched, and cross-reference it against what happened. A recent date is not evidence of completeness: a file updated yesterday can still be missing today's change.

For documents split into an index plus category files, "full content" means the index plus every category file the index says the session touched or could have touched. It does not mean every category file, and it never means a stub that only points elsewhere.

## Steps

1. **Read the living documents, index first.**
2. **Cross-reference with the session.** What was built, fixed, decided, discovered or explicitly deferred?
3. **Update current-state documents** with current state only. Keep pending items out of them.
4. **Update the pending list.** Mark done items, add new ones. Nothing goes on the list unless the owner adds it or approves a suggestion.
5. **Record incidents**, one entry per real incident (see incident-to-rule).
6. **Size check.** Compare every touched file with its size limits. Warn at the warning threshold; at the cap, propose a split and wait for approval.
7. **Lint, then commit.** Run the project's linter. Commit only when it is clean.
8. **Give the push command** and say which machine and directory it runs in.

## Standing rules during a sync

- **Persist mid-session events.** When something significant happens, flag it right away: update now or save for sync?
- **No loose ends.** Before syncing, scan the pending list for items under five minutes of work and flag them. Items with no movement for 30 days get promoted.
- **Check before overwriting.** Read a document's live content before replacing it. Never write from a remembered version.
- **Disclose own mistakes.** When you confirm one, stop and say what happened, the impact and the proposed fix.

## Before concluding "nothing needs updating"

Be able to say what you checked in each document and why it needed no change. "It was not obviously stale" is not an answer.

## Verify before returning

Report: files updated, files read and left alone (with the reason), size warnings, lint result, and the commit id. Re-read your own diff before committing.

## Failure mode

Treating "the date looks recent" or "I already know what is in it" as a replacement for reading. Read first, every time, even when confident.
