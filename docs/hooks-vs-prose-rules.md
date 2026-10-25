# Hooks vs prose rules for agent compliance

When an agent keeps breaking an instruction, adding more prose usually helps less than moving the rule into a mechanical check.

## The pattern

A **prose rule** lives in an instruction file (`CLAUDE.md`, a system prompt, a skill). The model has to remember it and weigh it against everything else in context.

A **hook** is code that runs at a fixed point in the agent's loop (before a tool call, after a tool call, when the prompt is submitted, when the agent tries to stop). It does not depend on the model remembering anything. It allows, blocks, or annotates.

## What one local evaluation showed

This comes from an informal, single-operator setup with a locally hosted 30B-class model and a small number of test runs. It is an anecdote, not a benchmark, so treat the numbers as directional:

- Rules written as prose were followed roughly 80% of the time.
- The same rules enforced by hooks were followed in effectively every run.
- The failures were not random. The model followed recently added instruction sections and ignored older ones. As the instruction file grew, rule density and recency weighting became the problem.

## Guidance

1. **Start with prose.** It is cheap, and many rules never need more.
2. **Promote a rule to a hook when it has been broken twice** and the cost of breaking it is real (data loss, writing to the wrong place, leaking a secret, claiming success without checking).
3. **Keep hooks small and single-purpose.** One hook, one rule, easy to test.
4. **Make hooks fail loudly with a reason the agent can act on.** A block message that says what rule fired and what to do instead lets the agent recover without a human.
5. **Chain, don't merge.** When adding a hook to an existing configuration, append it. Check that the tool or installer you used did not rewrite existing entries, and diff the configuration after.
6. **Test the hook against the failure that motivated it.** A hook you have not seen block the bad case is only a hope.

## Typical hook points and uses

| Point | Example uses |
|---|---|
| Before a tool call | Block writes outside an approved directory; require a dry run first; cap the number of actions per task |
| After a tool call | Append to an audit log; detect output that looks wrong |
| Prompt submitted | Block prompts containing credentials (see `examples/secret-gate/`) |
| Agent stops | Reject a "done" claim that lacks verification evidence |

## Limits

- Hooks guard what you thought to check. They do not replace judgment.
- A hook that blocks too often trains people to disable it. Track false blocks.
- Hook behavior depends on your agent's version and configuration format. Check its current documentation.
