# Project State

Last updated: 2026-06-14T21:07:10+08:00

## Current Execution

- Status: `completed`
- Task: Fix docs v2 homepage styling broken by WordPress wpautop
- Branch: `codex/klaviyo-docs-sync-state`
- Commit: `ff25476e`

## Latest Result

Added idempotent _wrap_block_html() helper in sync/deploy.py; PagesClient.create_page and update_page now wrap content in <!-- wp:html -->...<!-- /wp:html --> Custom HTML block so WordPress renders it verbatim instead of injecting <p>/<br> into <style>/<svg>/<input>. Redeployed homepage via 'deploy.py init' (page #13163).

## Verification

- curl https://dynamicycle.com/klaviyo-cn-docs-v2/ -> wpautop mangle signatures all 0 (}</p>=0, <p>/*=0, <svg><br=0, <input><br=0), </style> intact=14, hc-hero=10 hc-card=118 layout rendered.

## Changed Files

- `sync/deploy.py`

## Next Action

Optional follow-up: run 'deploy.py categories' (or 'all') to apply same wp:html wrap to category/section/article pages and refresh stale /v2 category-card links on the homepage.

## Notes

- None.

## Resume

```bash
git fetch origin
git checkout codex/klaviyo-docs-sync-state
git pull --ff-only
cat PROJECT_STATE.md
```
