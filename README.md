# agent-skills

Small, general-purpose skills and notes for AI coding agents, focused on one theme: making agents check their work instead of asserting it.

Each skill is a folder with a `SKILL.md` (YAML frontmatter plus instructions) in the common agent-skill format. Each ends with a "Verify before returning" section that says what evidence the agent must show.

## Skills

| Skill | Use it when |
|---|---|
| [existence-verification-escalation](skills/existence-verification-escalation) | You are about to say something does not exist |
| [syntax-self-check](skills/syntax-self-check) | You are about to write or edit code in a live location |
| [carried-status-verification](skills/carried-status-verification) | You are about to repeat a status from memory, a summary or a handoff |
| [pre-write-verification](skills/pre-write-verification) | You are about to overwrite an existing file or document |
| [reference-existence-check](skills/reference-existence-check) | A drafted script or plan names functions, paths, ports or services |
| [completion-standard](skills/completion-standard) | You are about to say work is done, or deciding whether to deploy it |
| [incident-to-rule](skills/incident-to-rule) | Something failed, or the same correction was needed twice |
| [install-session-discipline](skills/install-session-discipline) | You are about to install or change system-level software |
| [doc-sync](skills/doc-sync) | You are reconciling living documents with what happened in a session |
| [mcp-access-watchdog](skills/mcp-access-watchdog) | An MCP tool or folder access is missing, shrank or errors, or a session depends on MCP servers |
| [session-handoff](skills/session-handoff) | You are ending a session or passing work to another session or agent |

## Docs and examples

- [docs/hooks-vs-prose-rules.md](docs/hooks-vs-prose-rules.md): when to move a rule from prose into a hook.
- [docs/verification-before-return.md](docs/verification-before-return.md): how to add verification to a skill.
- [examples/secret-gate](examples/secret-gate): a tested prompt-submit hook that blocks likely credentials.

## Using a skill

Copy the skill's folder into your agent's skills directory (for Claude Code, a `skills/` folder in your project's `.claude/` directory or your user-level skills folder). Edit anything environment-specific, such as the protected paths in `install-session-discipline`, to match your setup.

## Provenance

These skills were written from experience running a multi-agent homelab workflow and are published in generalized form. See [NOTICE.md](NOTICE.md).

## License

MIT. See [LICENSE](LICENSE).
