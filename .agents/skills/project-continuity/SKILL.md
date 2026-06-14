---
name: project-continuity
description: Maintain a durable, resumable execution record for the Dynamicycle documentation repository. Use for user-entered modification requests, explicit local operation-history submissions, the trigger "落库", explicit Git checkpoints, or preparing work to continue under another account or computer. Do not use for read-only inspection, preview retrieval, or demo file output unless the user explicitly asks to record them.
---

# Project Continuity

## Recording Scope

Record only user-entered modification requests and explicit local operation
history submissions. Read-only inspection, preview retrieval, demo file output,
and other non-mutating review tasks do not need a `PROJECT_HISTORY.md` entry
unless the user explicitly asks to record them.

The user's Chinese word `提交` means submit to the local operation history
(`PROJECT_STATE.md` / `PROJECT_HISTORY.md`) by default. It does not mean
`git commit`, `git push`, or remote synchronization unless the user explicitly
says Git, commit, push, branch, PR, or remote.

When a user-entered modification operation is written to local operation
history, stage the scoped changed files and create a local Git commit for that
record. Do not run `git push` unless the user explicitly requests a push or
remote synchronization.

## Start A Recorded Task

1. Read `AGENTS.md`.
2. Read `PROJECT_STATE.md`.
3. Inspect the latest `PROJECT_HISTORY.md` entries when needed.
4. Check the current branch, worktree, and latest commit.
5. Record the task as `in_progress` before substantial work.

## Record Progress

Run `scripts/record_step.py` from the repository root after a material
milestone. Record facts, verification, changed paths, and one exact next action.
Do not record credentials.

```bash
python3 .agents/skills/project-continuity/scripts/record_step.py \
  --status in_progress \
  --task "Task description" \
  --result "Current result" \
  --verification "Check performed" \
  --changed "path/to/file" \
  --next "Next executable action"
```

## Finish A Recorded Task

1. Verify the task result.
2. Record `completed` or `blocked`.
3. For recorded modification operations, stage only task-owned files plus
   `PROJECT_STATE.md` and `PROJECT_HISTORY.md`, then create a descriptive local
   Git commit.
4. Do not push unless the user explicitly asks for remote synchronization or
   the `落库` trigger applies.

Do not stage unrelated worktree changes. If an explicitly requested push fails,
leave the local commit intact and record the exact recovery command.

## Handle "落库"

Treat `落库` as a persistence command:

1. Convert the latest user rules into concise mandatory instructions.
2. Put repository-wide rules in `AGENTS.md`.
3. Update this or another project skill when the workflow is reusable.
4. Put detailed facts and current results in tracked state/reference documents.
5. Record required tools and versions in `TOOLCHAIN.md`.
6. Validate changed skills.
7. Record, commit, and push the checkpoint.

## Handle Tool Upgrades

Before replacing or upgrading system-level software, tell the user the current
version, target version, reason, and verification command. Wait for the user to
perform the upgrade. Use `TOOLCHAIN.md` as the durable project record.
