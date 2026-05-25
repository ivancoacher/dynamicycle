# Dynamicycle Docs Handoff

Last updated: 2026-05-25 09:10 Asia/Shanghai

## Current Git State

- Working branch: `codex/klaviyo-docs-sync-state`
- Remote branch: `origin/codex/klaviyo-docs-sync-state`
- Latest commit before this handoff: `4cf30e9 sync all Klaviyo docs to BetterDocs`
- `main` on remote has many BetterDocs auto-generated commits, so this work was pushed to a separate branch instead of forcing `main`.

To continue on another machine:

```bash
git fetch origin
git checkout codex/klaviyo-docs-sync-state
```

## Sync Status

The current "create documents first" phase is complete.

- Missing translations: `0`
- Translated but not uploaded: `0`
- Full category chain sync report: `19 OK / 0 failed`
- URL map verification: passed
- BetterDocs category cleanup: passed, no remaining parent-only docs detected
- WordPress / BetterDocs now has the current local set of category, section, and article documents.

Primary report:

```text
klaviyo-en/_source/plans/all-category-chain-sync-report.json
```

Important metadata:

```text
klaviyo-cn/.translate_meta.json
klaviyo-cn/.upload_meta.json
klaviyo-en/_source/homepage-menu/category-doc-uploads.json
klaviyo-en/_source/section_preview_uploads.json
klaviyo-en/_source/url-map/source-to-local-url-map.json
```

## Current Strategy

The working priority is:

1. Create all docs first.
2. Optimize layout and structure across all docs.
3. Optimize Chinese content quality.
4. Push updates using the existing update path, not duplicate creation.

For now, translation defaults to Google because the OpenAI API key returned rate-limit errors during this session. The script still keeps the OpenAI path available for later content optimization.

Translation provider behavior:

```bash
TRANSLATION_PROVIDER=google python3 sync/pipeline.py translate
TRANSLATION_PROVIDER=openai python3 sync/pipeline.py translate
```

Do not commit `.env` or any API keys.

## Layout Rules Already Applied

These rules should continue to be applied globally:

- Category pages:
  - Use card grid for sections.
  - Use list format for Top articles.
  - Do not show the duplicate custom breadcrumb/title block; rely on BetterDocs navigation.
  - Keep spacing compact around `.dc-category-page`.

- Section pages:
  - Use source-site-like list layout, not cards.
  - Do not show custom breadcrumb/title blocks; rely on BetterDocs navigation.

- Article pages:
  - No left category list.
  - Move article Table of Contents to the left side.
  - Remove duplicate top in-content Table of Contents.
  - Remove bottom feedback/share/social elements.
  - Preserve source structure such as unordered lists; do not convert lists into cards unless the source actually uses a card-like structure.
  - Preserve images and visible HTML structure where possible.

## Useful Commands

Check remaining work:

```bash
python3 - <<'PY'
import json
from pathlib import Path
trans=json.loads(Path('klaviyo-cn/.translate_meta.json').read_text()).get('translated',{})
upload=json.loads(Path('klaviyo-cn/.upload_meta.json').read_text()).get('uploaded',{})
rels=json.loads(Path('klaviyo-en/_source/relations/category-articles.json').read_text())
missing_trans=[]; missing_upload=[]
for cat in rels:
    ids=[str(a.get('article_id')) for a in cat.get('articles',[]) if a.get('article_id')]
    missing_trans.extend(i for i in ids if i not in trans)
    missing_upload.extend(i for i in ids if i in trans and i not in upload)
print('missing_translation_articles', len(missing_trans))
print('translated_not_uploaded_articles', len(missing_upload))
PY
```

Verify URL maps:

```bash
python3 sync/pipeline.py verify-url-maps
```

Run the full category -> section -> article chain:

```bash
PYTHONUNBUFFERED=1 python3 sync/pipeline.py sync-all-categories
```

Run one category for testing:

```bash
PYTHONUNBUFFERED=1 python3 sync/pipeline.py sync-category customer-agent
```

## Notes

- The exposed OpenAI API key from the chat should be revoked in the OpenAI dashboard and replaced before future OpenAI usage.
- If pushing to `main` later, first reconcile the large remote `main` history carefully. Avoid force-pushing.
- The current branch is the safest continuation point for the next machine.
