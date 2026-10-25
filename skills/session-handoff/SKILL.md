---
name: session-handoff
description: Use when ending a work session or passing work to a fresh session or another agent. Writes a handoff note that captures state, decisions, open items and how to resume, and defines the opener a receiving session uses to continue from it.
---

# Session Handoff

A handoff note lets a fresh session resume without re-deriving context. It is a snapshot, so the receiving session must verify it before trusting it (see carried-status-verification).

## When to write one

- At the end of a session with unfinished work.
- Before handing a task to another agent or person.
- When a session has run long enough that its context is getting crowded.

## Note structure

Write a short file with these sections, in this order:

1. **Goal.** One or two sentences on what the work is for.
2. **Current state.** What exists now, with paths. What is done, what is staged, what is running (use the completion-standard vocabulary).
3. **Decisions made.** Each decision with a one-line reason, so it is not reopened by accident.
4. **Open items.** What remains, in priority order, with the first concrete next step.
5. **Gotchas.** Things that cost time this session and will again.
6. **How to verify.** Commands or checks the next session should run first to confirm this note is still accurate.

Keep it brief enough to read in a minute. Link to files by path instead of restating their contents.

## Receiving a handoff

Use an opener such as: `Continue from handoff: <path>`

The receiving session should:

1. Read the note.
2. Run its "How to verify" checks before repeating any status from it.
3. Report what matched and what changed since the note was written.
4. Then continue with the first open item.

## Verify before returning

Before you finish writing the note, re-read it as if you were the next session: could you resume from it alone? Check that every path in it exists.

## Provenance note

Written for this repository. Handoff notes are a common practice in agent workflows and this structure is general. The idea of compacting a conversation into a document another agent can continue from is also found in the `handoff` skill of mattpocock/skills (MIT License). See NOTICE.md.
