# Project State

Last updated: 2026-06-14T21:58:53+08:00

## Current Execution

- Status: `completed`
- Task: Fix /v2/ stale links and push-notifications 404 in docs v2; redeploy categories + sections
- Branch: `codex/klaviyo-docs-sync-state`
- Commit: `cd4e4deb`

## Latest Result

Patched sync/deploy.py: (1) meta_page_url ignores stale URLs not under current DOCS_BASE_PATH and falls back to deterministic URL; (2) topic_sidebar_html filters to active_category_slugs() so categories with no crawled content (push-notifications) are hidden. Redeployed categories (18/18) and sections (204/204). Articles (1205) intentionally NOT deployed per user.

## Verification

- All 18 category pages: http=200, }</p>=0, <p>/*=0, push-notifications=0, stale /v2/ (excl REST)=0. Sampled 3 section pages: http=200, wpautop-clean.

## Changed Files

- `sync/deploy.py, sync/.deploy_meta.json`

## Next Action

When ready, deploy 1205 article pages: .venv/bin/python sync/deploy.py articles

## Notes

- None.

## Resume

```bash
git fetch origin
git checkout codex/klaviyo-docs-sync-state
git pull --ff-only
cat PROJECT_STATE.md
```
