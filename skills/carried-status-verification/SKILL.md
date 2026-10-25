---
name: carried-status-verification
description: Use before repeating any status claim that came from memory, a prior summary, a handoff note, or earlier in the conversation (ticket state, open issues, counter values, "still blocked by X"). Re-check it against its real source first.
---

# Carried-Status Verification

A status claim you did not check this session is unverified, however confidently it was stated and however many times it has been repeated.

## Core rule

Before the first time you repeat a carried status claim to the person, check it against its live source. Do not wait for a later review step to catch it.

Claims this covers:
- the state of a ticket, task or incident
- a counter, checkpoint or progress value
- "X is still blocked by Y"
- "that was already deployed / fixed / decided"
- anything taken from a memory file, a summary of a previous chat, or a handoff document

## Why

Handoffs and summaries are snapshots, not live feeds. A session can spend hours repeating three confident statements that were all out of date when the session began, and only discover it when a final sync reads the real source. Being present in context, being stated firmly, and being repeated earlier in the same conversation are not evidence of being current.

## Steps

1. List the status claims you are about to rely on or repeat.
2. For each, find its real source (the tracker, the file, the system itself).
3. Read that source now.
4. If it matches, proceed. If not, correct the claim and say what changed.
5. If you cannot check it, say the claim is unverified when you pass it on.

## Cheap checks

- Read the newest handoff note, then verify any "still open" item in it before treating it as open.
- Ask the system, not the notes: query the real state where you can.

## Verify before returning

Final answers should mark each status as checked this session (with the source) or unverified. Do not blend the two.
