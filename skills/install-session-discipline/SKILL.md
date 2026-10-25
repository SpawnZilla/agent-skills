---
name: install-session-discipline
description: Use before the first install, uninstall or system-level change in a session (package managers, installer scripts, manual builds, anything writing outside a scoped project directory). Confirms where it installs, requires approval and a dry run, and paces the work with explicit pause points.
---

# Install Session Discipline

Two rules for any install work: where things install, and how the session is paced.

Set your own protected locations when you adopt this skill. The defaults below suit a typical Linux machine; edit them to match yours.

- **Protected by default:** boot and EFI partitions, swap, the root filesystem (/), and home directories.
- **Approved install target:** a dedicated data volume or project directory you name (for example `/opt/<project>` or a mounted data drive).

## Rule 1: Install path

Nothing installs to a protected location without explicit approval. Before any install command (package manager, installer script, manual build):

1. State where it installs.
2. State which drive or filesystem that is.
3. Get explicit approval.
4. Run a dry run first.

The four-step check costs seconds. Recovering from a large stack installed to the wrong place by default can cost a full uninstall.

## Rule 2: Session pacing

Every install session uses pause points between phases:

```
PAUSE: [what just happened / what comes next].
Reply GO to proceed or STOP to hold.
```

- Capture a baseline (system state snapshot) before touching anything.
- Use the same format every session, including the ones that look simple. Those are where skipping a pause does the most damage.

## How they fit together

Rule 1's check is itself one of the pause points. A well-run session:

1. PAUSE: baseline captured, ready to start.
2. State target, drive and get approval.
3. PAUSE: dry run about to execute.
4. Run the dry run and show the output.
5. PAUSE: dry run clean, ready for the real install.
6. Run the real install.
7. PAUSE: install complete, verify before the next phase.

Repeat per phase.

## Commands you give the person

State where each command runs (which host or prompt), and say in plain terms what it does to the machine before the command itself.

## Verify before returning

After the install, confirm: files landed in the approved location, nothing was written to protected locations, and the service or tool actually runs. Report those three results.

## Why

A skipped pause or unapproved path usually fails quietly. The cost appears later as a harder problem: a root-owned install that has to be unwound, or an unreviewed change buried in a running system.
