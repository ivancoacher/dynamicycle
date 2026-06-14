---
name: project-continuity
description: Maintain a durable, resumable execution record for the Dynamicycle documentation repository. Use for every user-directed task in this project, especially when starting or finishing work, recording milestones or failures, responding to the trigger "落库", creating Git checkpoints, or preparing work to continue under another account or computer.
---

# Project Continuity

## Start A Task

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

## Finish A Task

1. Verify the task result.
2. Record `completed` or `blocked`.
3. Stage only task-owned files and the two continuity documents.
4. Commit with a descriptive message.
5. Push the current branch to its upstream.
6. Record a final checkpoint containing the commit and push result. Amend the
   checkpoint commit when practical so the remote state document names the
   commit that contains it.

Do not stage unrelated worktree changes. If push fails, leave the local commit
intact and record the exact recovery command.

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
