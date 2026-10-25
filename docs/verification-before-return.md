# Adding "verify before returning" to a skill

Most skills say when to trigger and what to check. Fewer say what must be shown before the skill's output counts as final. Adding that closes a common gap: the skill runs, but nothing confirms it worked.

## The section to add

Put a short section near the end of each skill:

```markdown
## Verify before returning

<One of the checks below, stated as something the agent must show.>
```

## Choose a check type

1. **Objective check.** Run something that can fail and report the result.
   - Code skill: re-parse the changed file and report the command and exit status.
   - File skill: confirm the file exists at the stated path and report its size.
   - Install skill: confirm the files landed where approved and the service starts.
2. **Second-pass review.** Re-read your own output against the source of truth before returning it.
   - Sync skill: re-read your diff against the living documents before committing.
   - Research skill: re-check each cited claim against its source.
3. **Reviewer agent.** Where your setup allows it, have a separate agent that did not produce the work check it. It cannot grade its own work.

## Write the requirement as evidence

Weak: "Make sure the file is correct."
Strong: "Report the exact command you ran and its result."

The strong form cannot be satisfied by saying "looks fine."

## Keep it proportionate

A one-line check beats a long checklist nobody follows. Add the cheapest check that would have caught the failure you have actually seen.

## Where this appears in this repository

Every skill under `skills/` ends with a "Verify before returning" section written in this style.
