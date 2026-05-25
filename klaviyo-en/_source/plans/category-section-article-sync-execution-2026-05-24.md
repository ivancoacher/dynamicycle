# Category / Section / Article Sync Execution Report

Executed: 2026-05-24

## Commands Run

```bash
python3 -m py_compile sync/pipeline.py
python3 sync/pipeline.py relationships
python3 sync/pipeline.py prepare-url-maps
python3 sync/pipeline.py resolve-redirect-links
python3 sync/pipeline.py verify-url-maps
python3 sync/pipeline.py status
```

## Completed

- Built local category-section relationships.
- Built local section-article relationships.
- Built local category-article relationships.
- Generated local URL maps for categories, sections, and articles.
- Added redirect aliases for old Klaviyo URLs that resolve to known local pages or approved external destinations.
- Added high-confidence manual aliases for old Klaviyo URLs that are no longer available in the source API.
- Updated upload rendering so internal Klaviyo links are resolved after translation and before WordPress upload.
- Updated translation logic so future translations translate visible HTML text nodes while preserving IDs, classes, links, image URLs, and attributes.
- Re-uploaded one controlled article sample to WordPress: `115005085427`.

## Current Counts

- Categories: 20
- Sections: 293
- Articles: 1205
- URL lookup keys: 3172
- Redirect aliases: 76
- Manual aliases: 27
- Remaining unresolved internal doc-link occurrences: 0
- Remaining unique unresolved source URLs: 0

## Generated Files

- `klaviyo-en/_source/relations/category-sections.json`
- `klaviyo-en/_source/relations/sections-articles.json`
- `klaviyo-en/_source/relations/category-articles.json`
- `klaviyo-en/_source/url-map/category-url-map.json`
- `klaviyo-en/_source/url-map/section-url-map.json`
- `klaviyo-en/_source/url-map/article-url-map.json`
- `klaviyo-en/_source/url-map/source-to-local-url-map.json`
- `klaviyo-en/_source/url-map/redirect-url-map.json`
- `klaviyo-en/_source/url-map/manual-url-aliases.json`
- `klaviyo-en/_source/url-map/unresolved-links-report.json`

## Link Exceptions

The previous unresolved old Klaviyo URLs were reviewed and mapped through `manual-url-aliases.json`.

Current result:

- Cached internal Klaviyo docs links resolved: yes
- Remaining unresolved internal docs links: 0

## Upload Boundary

No batch WordPress article upload was executed in this run.

One sample article was updated:

- Source ID: `115005085427`
- WordPress ID: `11475`
- URL: `https://dynamicycle.com/docs/articles-understanding-unique-vs-total-opens-and-clicks/`
- Online check: HTTP 200, Chinese title/body present, `dc-help-article` wrapper present, sample old Klaviyo link no longer present.

The next safe batch sequence is:

```bash
python3 sync/pipeline.py relationships
python3 sync/pipeline.py prepare-url-maps
python3 sync/pipeline.py verify-url-maps
python3 sync/pipeline.py upload --dry-run --force --limit 10
```

Only run the real batch upload after reviewing the dry-run output.
