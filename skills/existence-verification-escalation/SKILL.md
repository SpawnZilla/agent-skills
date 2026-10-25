---
name: existence-verification-escalation
description: Use before stating that any file, directory, path, or piece of content does not exist. A single empty search result is never proof of absence. Trigger whenever a search tool comes back empty and the next instinct is to report "this doesn't exist" or "I couldn't find X".
---

# Existence Verification Escalation

An empty search result means the search found nothing, not that the thing is absent. The pattern may have been wrong, the tool may not look as deep as its description claims, or the name may differ slightly. Escalate before concluding anything.

## Core rule

Never conclude non-existence from a single targeted search. An empty result is a prompt to look wider, not a final answer.

## Escalation tiers

1. **Targeted search.** Search for the exact name or pattern. If empty, that proves nothing yet.
2. **List the parent directly.** List the directory, or walk the tree from a known root. This catches naming variations, case mismatches, and searches that silently stopped at the top level.
3. **Read a nearby confirmed file.** Open a file you know exists in the same area and look for references to the target.

Say "does not exist" only after tier 2 (and tier 3 where relevant) also come up empty.

## Aim the next look with evidence already in hand

Every listing you have already pulled is evidence. Before the next call, read what you have. If a directory name in an earlier listing shares words with the target, check that directory first. Guessing a new, plausible-sounding path while ignoring a matching name in your own output is motion without progress.

## Do not trust a "recursive" search tool at face value

A tool that claims to search recursively can still fail silently, for example by looking only at the first directory level. Treat "no matches" from any such tool as a weak signal until you have verified its behavior, and pair it with a direct directory listing of the plausible parent folders.

## When escalation is incomplete, say so

- Honest: "A direct search didn't find X. I haven't checked every plausible directory yet."
- Not honest: "X does not exist," after an incomplete or misdirected search.

## Verify before returning

Before reporting that something is absent, state which tiers you completed and what each returned. If you cannot list them, the conclusion is not ready.

## Why it matters

A confident false negative sends people the wrong way: recreating a file that exists, assuming a feature is missing, or deciding something was never decided. It is worse than reporting nothing.
