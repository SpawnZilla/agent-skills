---
name: incident-to-rule
description: Use after an agent or process fails, or when the person corrects the same mistake twice. Find the root cause, record the incident with evidence, and turn the fix into a durable rule, skill update or automated check rather than a one-off chat correction.
---

# Incident to Rule

A correction that lives only in the chat will be repeated. Turn each real failure into a durable change.

## Core rule

When something fails, do not only fix the output. Find why it happened, record it, and change the process so it is caught next time.

## Steps

1. **Fix the immediate problem.** Stop the damage first.
2. **Find the root cause.** Classify it as one of: process (the steps were wrong), context (the agent lacked or misread information), or code (a defect in a script or tool).
3. **Record one entry per real incident** (not per mention). Include: what happened, the impact, the root cause class, the fix, and an evidence excerpt captured at write time (a log line, session or audit id, the failing output).
4. **Choose the durable form.**
   - A wording fix in an existing skill or instruction file, for process and context causes.
   - An automated check, hook or gate, if the same prose rule has already failed.
   - A code fix, if the cause was a defect.
5. **Update the durable artifact** in the same session, not later.
6. **Check it.** Reproduce the original failure where you can and confirm the new rule or check would have caught it.

## Rules of thumb

- Capture evidence when you write the record. Reconstructed evidence goes stale.
- If a rule has been violated more than once, a prose rule is the wrong tool. Move it into a mechanical check.
- Annotate old entries as superseded instead of rewriting history.
- Disclose your own mistakes the moment you confirm them: what happened, the impact, the proposed fix.

## Verify before returning

Name the incident record, the durable change you made, and how you confirmed it would catch a repeat. If you could not confirm, say so.
