# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This file is the **self-contained Claude adaptation of `AGENTS.md`**. `AGENTS.md`
remains the shared canonical rule file for other agents (Codex, etc.); when the two
disagree, treat `AGENTS.md` as the source of truth and surface the drift to the user.
All "Codex" instructions in `AGENTS.md` apply to Claude here.

## What this repo does

Translates Klaviyo Help Center documentation into Chinese and publishes it to the
Dynamicycle WordPress site (`dynamicycle.com/docs/`). There is no application code —
only Python sync/deploy scripts plus crawled and translated content trees.

## Mandatory startup

Before acting on any user request:

1. Read this file.
2. Read `PROJECT_STATE.md` for the latest execution result and next action.
3. Read recent entries in `PROJECT_HISTORY.md` when more context is needed.
4. Check `git status --short --branch` and the latest commit.
5. Continue from the recorded state instead of reconstructing project history from
   chat memory.

`PROJECT_STATE.md` is the canonical current-state document. `HANDOFF.md` is a
historical snapshot and must not override newer state.

## Operation recording & commits

Record **only** user-entered modification requests and explicit local operation
history submissions. Read-only inspection, preview retrieval, demo file output, and
other non-mutating review tasks do **not** need a `PROJECT_HISTORY.md` entry unless
the user explicitly asks.

**The Chinese word `提交` means "submit to the local operation history"
(`PROJECT_STATE.md` / `PROJECT_HISTORY.md`) by default.** It does *not* mean
`git commit`, `git push`, or any remote synchronization unless the user explicitly
says Git, commit, push, branch, PR, or remote.

When a user-entered modification operation is written to local operation history,
stage the scoped changed files and create a **local** Git commit for that record. Do
**not** run `git push` unless the user explicitly requests a push or remote sync.

When a task should be recorded:

1. At task start, update the state to `in_progress`.
2. After each material milestone, keep the result and next action current.
3. Before the final response, set the task to `completed` or `blocked`.
4. Append the outcome to `PROJECT_HISTORY.md`; never rewrite old history.
5. Record commands or checks that materially prove the result.
6. Never record passwords, API keys, tokens, cookies, or `.env` contents.

Use the recorder:

```bash
python3 .agents/skills/project-continuity/scripts/record_step.py \
  --status completed \
  --task "Short task description" \
  --result "What changed or what was learned" \
  --verification "Verification command or result" \
  --changed "path/to/file" \
  --next "Exact next action"
```

## Checkpoint & device continuity

For recorded user-entered modification operations, create a **local** Git checkpoint
after updating `PROJECT_STATE.md` and `PROJECT_HISTORY.md`. Only stage files belonging
to the task plus the continuity documents. Do not push to a remote as part of routine
operation recording.

When creating a local checkpoint:

1. Stage only files belonging to the task plus `PROJECT_STATE.md` and
   `PROJECT_HISTORY.md`.
2. Do not include unrelated user changes.
3. Create a descriptive Git commit.
4. Do not push the current branch unless the user explicitly asks.
5. Record commit results in the state/history documents.
6. If a commit or an explicitly requested push cannot complete, record the exact
   blocker and leave a precise recovery command.

## "落库" trigger

When the user says `落库`:

1. Treat the latest instructions as durable project rules.
2. Update `AGENTS.md` for repository-wide mandatory behavior, and mirror the change
   here if it affects Claude's workflow.
3. Update an existing project skill or create a concise skill under
   `.agents/skills/` when the workflow is reusable.
4. Put detailed project facts in an appropriate tracked document instead of bloating
   the skill.
5. Validate any changed skill. (Note: `AGENTS.md` references a `quick_validate.py`
   validator that is not currently present in the repo — if missing, validate the
   skill's frontmatter and script paths manually.)
6. Update state/history, commit the scoped changes, and push the branch.

## Toolchain & system upgrades (hard constraint)

1. Read `TOOLCHAIN.md` before running project scripts.
2. Use the documented project version, not whichever `python3`, Node, or other
   executable happens to appear first on `PATH`.
3. **Do not upgrade or replace system-level software without telling the user.**
4. When an upgrade is required, report: tool name, current version, required or
   recommended version, why the upgrade is needed, and how the user can verify it.
5. Wait for the user to perform the system upgrade, then verify it before continuing.
6. When a required tool or version changes, update `TOOLCHAIN.md` and any relevant
   version file as part of the same checkpoint.
7. Temporary project-local virtual environments and dependency installs are allowed
   when they do not replace system software or expose credentials.

**Python 3.13.11 is required.** `sync/deploy.py` uses Python 3.10+ type-union
syntax; the macOS system `python3` reports `3.9.6` and is incompatible. Use
`/opt/homebrew/bin/python3.13` or the project `.venv/`:

```bash
/opt/homebrew/bin/python3.13 -m venv .venv
.venv/bin/python -m pip install -r sync/requirements.txt
```

`.venv/` is git-ignored.

## Architecture: data flow & authoritative paths

```
Klaviyo Zendesk API
   │  sync/pipeline.py crawl
   ▼
klaviyo-en/            English source — AUTHORITATIVE for IDs, slugs, URLs, hierarchy, media; NEVER uploaded
   {category}/         source articles
   _source/            relationship + URL-map + homepage-menu JSON
   │  sync/pipeline.py translate   (Google default; TRANSLATION_PROVIDER=openai optional)
   ▼
klaviyo-cn/            Chinese translations — these get uploaded
   .translate_meta.json / .upload_meta.json   resumable per-article progress + Klaviyo-id→WP-id map

batterDocs/            original Dynamicycle Chinese docs (BetterDocs-managed markdown)
build/deploy-previews/ generated local HTML previews
```

Previews are served at `http://127.0.0.1:8765/<file>.html`. When giving the user
local preview links, always use that URL format, never `file://`.

## Two separate deploy paths (do not confuse them)

| | BetterDocs pipeline | WordPress Pages v2 |
|---|---|---|
| Script | `sync/pipeline.py` | `sync/deploy.py` |
| Target | BetterDocs plugin docs under WP parent category `775425988` | Native WP pages under `/klaviyo-cn-docs-v2/` |
| Scope | crawl → translate → upload | generate HTML from `klaviyo-cn/` + `_source/`, deploy via WP Pages REST |

`PROJECT_STATE.md` records which path is in progress. The active work branch is
`codex/klaviyo-docs-sync-state`.

## Common commands

All commands run from repo root (`docs/`). Use `.venv/bin/python`.

```bash
# === BetterDocs pipeline (sync/pipeline.py) ===
.venv/bin/python sync/pipeline.py status                     # progress / what's left
.venv/bin/python sync/pipeline.py crawl                      # crawl EN from Klaviyo
.venv/bin/python sync/pipeline.py crawl-article "<url|id>"   # one source article
.venv/bin/python sync/pipeline.py translate                  # EN → ZH
.venv/bin/python sync/pipeline.py upload                     # ZH → WordPress BetterDocs
.venv/bin/python sync/pipeline.py full                       # all steps in sequence
.venv/bin/python sync/pipeline.py sync-category customer-agent   # one category chain (test)
.venv/bin/python sync/pipeline.py sync-all-categories        # full category→section→article chain
.venv/bin/python sync/pipeline.py verify-url-maps            # validate URL maps
# upload flags: --dry-run --force --limit N --ids a,b,c

# === WordPress Pages v2 (sync/deploy.py) ===
.venv/bin/python sync/deploy.py preview          # regenerate build/deploy-previews/*.html
.venv/bin/python sync/deploy.py status           # deployment status
.venv/bin/python sync/deploy.py init             # create /docs/v2/ parent page
.venv/bin/python sync/deploy.py categories       # category pages
.venv/bin/python sync/deploy.py sections         # section pages
.venv/bin/python sync/deploy.py articles         # article pages
.venv/bin/python sync/deploy.py all              # init + categories + sections + articles
# flags: categories/sections --only <slug>; articles --only <ids> --force; all --force
```

The full list of `pipeline.py` subcommands lives in its `COMMANDS` dict near the
bottom of the file.

## Documentation & content rules

- `klaviyo-en/_source/` is authoritative for source IDs, hierarchy, URLs, original
  HTML, and media.
- Translation changes user-visible text only. Preserve IDs, slugs, URLs, anchors,
  links, media references, and HTML attributes.
- Use English mode-prefixed slugs (e.g. `articles-{english-title-slug}`), never
  Chinese slugs. Use stable slugs and update existing remote documents instead of
  creating duplicates.
- Resolve internal Klaviyo links to local documentation links before final upload.
- Generate and inspect local previews or `--dry-run` output before batch writes.
- Do not delete remote documents or force-push unless the user explicitly requests it.
- Never commit `.env` or credentials.

## Style ownership

Shared visual rules for generated category/section/article pages live in
**`sync/deploy-shared.css`** (`deploy.py` inlines it). Keep shared layout, sidebar,
typography, list, and responsive rules there — do not duplicate them inside
individual page generators, and do not edit generated files under
`build/deploy-previews/` by hand. Keep only page-specific components in `deploy.py`.
After any CSS change, regenerate with `.venv/bin/python sync/deploy.py preview` and
inspect. See `sync/DEPLOY_STYLES.md`.

## Project skills (Klaviyo sync workflows)

- `.claude/skills/` (git-ignored, local only) — three workflows exposed as slash
  commands: `klaviyo-sync` (dispatcher), `klaviyo-global-refresh` (batch refresh of
  changed docs only), `klaviyo-url-refresh` (refresh one URL, upload, return live
  preview).
- `.agents/skills/project-continuity/` — the tracked continuity-workflow skill.

## Important paths

- `PROJECT_STATE.md` — latest resumable execution state
- `PROJECT_HISTORY.md` — append-only task history
- `TOOLCHAIN.md` — required tools, versions, and upgrade policy
- `HANDOFF.md` — historical snapshot (do not let it override `PROJECT_STATE.md`)
- `AGENTS.md` — shared canonical agent rules for all agents
- `.agents/skills/project-continuity/` — continuity workflow and recorder script
- `batterDocs/` — existing BetterDocs-managed content
- `klaviyo-en/` — English source and relationship data
- `klaviyo-cn/` — translated Chinese content
- `sync/pipeline.py` — BetterDocs synchronization pipeline
- `sync/deploy.py` — WordPress Pages `/docs/v2/` deployment path
- `sync/deploy-shared.css` — shared category/section/article visual rules
- `sync/DEPLOY_STYLES.md` — style ownership and regeneration guide
