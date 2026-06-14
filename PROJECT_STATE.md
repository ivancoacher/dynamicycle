# Project State

Last updated: 2026-06-14T22:01:12+08:00

## Current Execution

- Status: `completed`
- Task: 落库 docs v2 deploy rules + push branch
- Branch: `codex/klaviyo-docs-sync-state`
- Commit: `509bf70b`

## Latest Result

Persisted docs-v2 deploy rules (wp:html wrap, stale-/v2/ meta fallback, sidebar filtering, deploy order) in AGENTS.md and CLAUDE.md. Committed 509bf70b and pushed to origin/codex/klaviyo-docs-sync-state (ff25476e..509bf70b). First push attempt hit the known GitHub SSH reset; retry succeeded.

## Verification

- git push origin codex/klaviyo-docs-sync-state -> ff25476e..509bf70b (success)

## Changed Files

- `AGENTS.md, CLAUDE.md`

## Next Action

When ready: .venv/bin/python sync/deploy.py articles  (1205 article pages; large run, background it)

## Notes

- None.

## Resume

```bash
git fetch origin
git checkout codex/klaviyo-docs-sync-state
git pull --ff-only
cat PROJECT_STATE.md
```
