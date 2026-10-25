---
name: mcp-access-watchdog
description: Use when an MCP tool or folder access you expect is missing, errors, or changed, and at the start of a session that depends on MCP servers. Diagnose from the client log and the server's actual arguments before reporting a tool as lost, and never kill a server process without checking whether it runs inside a container.
---

# MCP Access Watchdog

MCP tools can disappear, shrink or be renamed without any error you would notice: a filesystem server quietly loses allowed directories, a server stops while the client keeps running, tool names change mid-session. This skill covers how to notice that early, diagnose it from evidence, and fix it without causing damage.

## When to use it

- At the start of a session that depends on MCP servers (cheap check, below).
- Whenever a tool call fails or returns "access denied", "outside allowed directories" or "tool not found". Re-check before you report anything as missing.
- When the person says access was lost, or a path that worked earlier no longer does.

## 1. Cheap start-of-session check

Run one small call per server you depend on and compare the results with what you expect:

- **Filesystem server:** list its allowed directories and compare with the directories you expect.
- **Git server:** a cheap read, such as listing branches. Avoid status on a large dirty tree; its output is long.
- **Memory or other servers:** one small search or read.
- **Remote shell, if any:** a trivial echo.

If everything responds, say so in one line. If not, go to step 2. A start-of-session check misses anything lost later, so repeat the relevant check whenever a call fails.

## 2. Do not trust the tool list at a glance

- Tools can be deferred and not visible until you search for them. A tool not being visible is not evidence of no access. Search for the capability first.
- Tool names can change between sessions or mid-session (for example when the client switches the way it exposes servers). Before concluding a tool is gone, search for the same capability under its new name.
- Apply the existence-verification-escalation skill before claiming access is unavailable.

## 3. Diagnose from evidence

1. **Read the client's MCP log for that server.** Look at the latest server start. Two messages matter:
   - A line saying the allowed directories were set from the server's arguments means the configured list is in effect.
   - A line saying the allowed directories were updated from the client's roots, with a count lower than expected, means the client's roots replaced the configured list. This is the signature of directories silently dropping.
2. **Compare the server's actual arguments to the expected set.** Inspect the running process command line, not just the config file. A directory missing from the arguments cannot be served.
3. **Check whether the process exists and who owns it.** A missing server while the client runs, or an unexpected second copy under another user, points to different causes.
4. **Check timing.** Note when access last worked and when it first failed, then list what changed in between (a restart, a folder attached in the client, a new session type). Report the window, not a guess.

Treat the roots-replace-config explanation as a hypothesis until you have tested it: restart cleanly, check the directories in a plain session, then attach a folder in a second session and check again.

## 4. Never kill a root-owned server process on sight

A server process owned by root is not automatically stale. A container can run the same server, and from the host it looks like a root-owned process.

Before treating any server process as stale:

1. Read `/proc/<pid>/cgroup` for the process.
2. If it contains `docker`, `containerd`, `libpod` or `kubepods`, it belongs to a container. Leave it alone.
3. Identify the owner: map the container id to its compose file or runtime, and note what depends on it.
4. Only then decide. Alert first; kill only with approval or a setting that explicitly allows it.

A real incident: an automated check killed three root-owned filesystem-server processes as stale. They were a working container's tool server, and the kill took down every client that depended on it until the container restarted. Save forensics (parent process, cgroup, start time, command line) before any kill, and default automatic kills to off.

## 5. Fix lost access safely

Fix what you can fix without waiting, within these limits, unless the person has set stricter ones:

- Do not delete anything. Do not touch files belonging to the person's projects.
- Back up any config file before you edit it, and say what you changed afterward.
- Safe steps from inside a session: search for the tools again, refresh the tool list, retry once, request folder access.
- Steps that end the session, such as restarting the client, you cannot do yourself. Tell the person immediately, give the exact command, say where it runs, and state what it does to the machine in plain words.
- If a retry fails twice, stop and report; do not loop.

Never restart the client automatically from a watchdog: it ends the person's open chat.

## 6. Optional: a host watchdog

A small timer-driven script can catch this without spending model tokens. Useful checks:

| Check | BAD when |
|---|---|
| Roots override | The latest filesystem-server start in the client log shows a roots update with fewer directories than expected, or the arguments lack an expected directory |
| Process arguments | The client is running and the filesystem server is missing or its arguments lack an expected directory |
| Other servers | The client is running and a server you rely on has no process |
| Root-owned servers | A root-owned server process exists outside container cgroups (alert only) |

Design rules that held up: alert on state change (OK to BAD, BAD to OK) so it does not repeat itself; make the expected directories, user, log path and alert endpoint configuration, not constants; keep credentials in a root-only environment file; default automatic fixes off.

Limits: Linux only; it depends on the wording of the server's log lines, which can change between versions; it cannot catch a failure that never logs a roots line (the process-arguments check still covers part of that); and a process-pattern match can hit unrelated processes whose command line contains the same words.

## Verify before returning

Before you tell the person access is lost, give: which call failed and with what message, what the log's latest server start says, what the running process arguments are, and the cgroup check if a root-owned process was involved. Before you tell them it is fixed, repeat the original failing call and report its result. If you could not check one of these, say so.
