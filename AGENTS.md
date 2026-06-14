# Dynamicycle Docs Agent Rules

This repository synchronizes Klaviyo documentation, Chinese translations, and
WordPress/BetterDocs output.

## Mandatory Startup

Before acting on any user request in this repository:

1. Read this file.
2. Read `PROJECT_STATE.md` for the latest execution result and next action.
3. Read the latest entries in `PROJECT_HISTORY.md` when more context is needed.
4. Check `git status --short --branch` and the latest commit.
5. Continue from the recorded state instead of reconstructing project history
   from chat memory.

`PROJECT_STATE.md` is the canonical current-state document. `HANDOFF.md` is a
historical snapshot and must not override newer state.

## Mandatory Operation Recording

Record only user-entered modification requests and explicit local operation
history submissions. Read-only inspection, preview retrieval, demo file output,
and other non-mutating review tasks do not need a `PROJECT_HISTORY.md` entry
unless the user explicitly asks to record them.

In this repository, the user's Chinese word `提交` means submit to the local
operation history (`PROJECT_STATE.md` / `PROJECT_HISTORY.md`) by default. It
does not mean `git commit`, `git push`, or any remote synchronization unless the
user explicitly says Git, commit, push, branch, PR, or remote.

When a user-entered modification operation is written to local operation
history, stage the scoped changed files and create a local Git commit for that
record. Do not run `git push` unless the user explicitly requests a push or
remote synchronization.

When a task should be recorded:

1. At task start, update the state to `in_progress`.
2. After each material milestone, keep the result and next action current.
3. Before the final response, set the task to `completed` or `blocked`.
4. Append the outcome to `PROJECT_HISTORY.md`; never rewrite old history.
5. Record commands or checks that materially prove the result.
6. Never record passwords, API keys, tokens, cookies, or `.env` contents.

Use:

```bash
python3 .agents/skills/project-continuity/scripts/record_step.py \
  --status completed \
  --task "Short task description" \
  --result "What changed or what was learned" \
  --verification "Verification command or result" \
  --changed "path/to/file" \
  --next "Exact next action"
```

## Checkpoint And Device Continuity

For recorded user-entered modification operations, create a local Git checkpoint
after updating `PROJECT_STATE.md` and `PROJECT_HISTORY.md`. Only stage files
belonging to the task plus the continuity documents. Do not push to a remote as
part of routine operation recording.

When creating a local checkpoint:

1. Stage only files belonging to the task plus `PROJECT_STATE.md` and
   `PROJECT_HISTORY.md`.
2. Do not include unrelated user changes.
3. Create a descriptive Git commit.
4. Do not push the current branch unless the user explicitly asks.
5. Record commit results in the state/history documents.
6. If commit or explicitly requested push cannot complete, record the exact blocker and leave a
   precise recovery command.

## "落库" Trigger

When the user says `落库`:

1. Treat the latest instructions as durable project rules.
2. Update `AGENTS.md` for repository-wide mandatory behavior.
3. Update an existing project skill or create a concise skill under
   `.agents/skills/` when the workflow is reusable.
4. Put detailed project facts in an appropriate tracked document instead of
   bloating the skill.
5. Validate any changed skill with `quick_validate.py`.
6. Update state/history, commit the scoped changes, and push the branch.

## Toolchain And System Upgrades

1. Read `TOOLCHAIN.md` before running project scripts.
2. Use the documented project version instead of whichever `python3`, Node, or
   other executable happens to appear first on `PATH`.
3. Do not upgrade or replace system-level software without telling the user.
4. When an upgrade is required, report:
   - Tool name
   - Current version
   - Required or recommended version
   - Why the upgrade is needed
   - How the user can verify the upgrade
5. Wait for the user to perform the system upgrade, then verify it before
   continuing.
6. When a required tool or version changes, update `TOOLCHAIN.md` and any
   relevant version file as part of the same checkpoint.
7. Temporary project-local virtual environments and dependency installs are
   allowed when they do not replace system software or expose credentials.

## Documentation Pipeline Rules

- `klaviyo-en/_source/` is authoritative for source IDs, hierarchy, URLs,
  original HTML, and media.
- Translation changes user-visible text only. Preserve IDs, slugs, URLs,
  anchors, links, media references, and HTML attributes.
- Use stable slugs and update existing remote documents instead of creating
  duplicates.
- Resolve internal Klaviyo links to local documentation links before final
  upload.
- Generate and inspect local previews or dry-run output before batch writes.
- Keep shared category, section, and article presentation in
  `sync/deploy-shared.css`; do not duplicate shared layout, sidebar, typography,
  list, or responsive rules inside individual page generators.
- When giving local preview links to the user, use the local preview server URL
  format `http://127.0.0.1:8765/<filename>.html`; do not provide `file://`
  preview links.
- Do not delete remote documents or force-push unless the user explicitly
  requests it.
- Never commit `.env` or credentials.

## Important Paths

- `PROJECT_STATE.md`: latest resumable execution state
- `PROJECT_HISTORY.md`: append-only task history
- `TOOLCHAIN.md`: required tools, versions, and upgrade policy
- `.agents/skills/project-continuity/`: continuity workflow and recorder
- `batterDocs/`: existing BetterDocs-managed content
- `klaviyo-en/`: English source and relationship data
- `klaviyo-cn/`: translated Chinese content
- `sync/pipeline.py`: BetterDocs synchronization pipeline
- `sync/deploy.py`: WordPress Pages `/docs/v2/` deployment path
- `sync/deploy-shared.css`: shared category/section/article visual rules
- `sync/DEPLOY_STYLES.md`: style ownership and regeneration guide
