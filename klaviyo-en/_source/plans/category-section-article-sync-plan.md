# Category / Section / Article Sync Plan

Created: 2026-05-24

This plan defines the recommended data synchronization flow for Klaviyo Help Center content into Dynamicycle BetterDocs, including translation boundaries and internal link handling.

## Goal

Build a stable local-first pipeline for:

1. Category pages
2. Section pages
3. Article pages

The pipeline must allow all later translation and upload work to run from local source data without re-fetching Klaviyo unless the source content changes.

## Core Principle

Do not generate final links opportunistically during crawl or translation.

Instead:

1. Crawl and cache source data.
2. Build stable local IDs and slugs.
3. Create or update WordPress shells to obtain `wp_id` and final URLs.
4. Translate content while preserving all IDs, URLs, anchors, and media references.
5. Render final HTML.
6. Resolve all internal Klaviyo links to local BetterDocs URLs.
7. Upload final content.
8. Verify unresolved links and 404 risks.

## Data Layers

### Source Layer

Saved under `klaviyo-en/_source/`.

Required data:

- Homepage category menu: `homepage-menu/category-menu.json`
- Category to section relation: `relations/category-sections.json`
- Section to article relation: `relations/sections-articles.json`
- Category to article relation: `relations/category-articles.json`
- Article source snapshots: `_source/articles/{article_id}.json`
- Article body HTML: `_source/articles/{article_id}.body.html`
- Rendered page HTML when available: `_source/rendered/{article_id}.html`

The source layer is the authority for IDs, hierarchy, source URLs, original text, images, and raw HTML.

### Translation Layer

Saved under `klaviyo-cn/`.

Translation should only modify user-visible text.

Translation must not modify:

- `category_id`
- `section_id`
- `article_id`
- `source_url`
- `slug`
- `wp_id`
- `wp_url`
- `href`
- `src`
- `id`
- `class`
- HTML attributes
- anchors

### Upload Mapping Layer

Required mapping files:

- Category upload map: `klaviyo-en/_source/homepage-menu/category-doc-uploads.json`
- Section upload map: `klaviyo-en/_source/section_preview_uploads.json` or future `section_upload_meta.json`
- Article upload map: `klaviyo-cn/.upload_meta.json`

Recommended final maps:

- `klaviyo-en/_source/url-map/category-url-map.json`
- `klaviyo-en/_source/url-map/section-url-map.json`
- `klaviyo-en/_source/url-map/article-url-map.json`
- `klaviyo-en/_source/url-map/unresolved-links-report.json`

## Stable Slug Rules

Use English slugs only.

```text
Category: categories-{category-slug}
Section:  sections-{category-slug}-{section-slug}
Article:  articles-{english-title-slug}
```

Examples:

```text
categories-customer-agent
sections-customer-agent-guidance
articles-understanding-unique-vs-total-opens-and-clicks
```

When source IDs are available, keep them in metadata even if they are not included in the public slug.

## Recommended Execution Plan

### Phase 1: Crawl Source Data

Commands:

```bash
python3 sync/pipeline.py crawl
python3 sync/pipeline.py crawl-homepage-categories
python3 sync/pipeline.py relationships
```

Outputs:

- Full source article cache
- Homepage 20-category menu
- Category/section/article relationship indexes

Rules:

- This phase may access Klaviyo.
- It should not translate.
- It should not upload content.
- It should be changed-only where possible.

### Phase 2: Prepare Slugs And Expected URLs

Generate expected URLs for every known category, section, and article before translation.

Expected output:

```json
{
  "type": "section",
  "source_id": "49191914194587",
  "source_url": "https://help.klaviyo.com/hc/en-us/sections/49191914194587-Guidance",
  "slug": "sections-customer-agent-guidance",
  "expected_url": "https://dynamicycle.com/docs/sections-customer-agent-guidance/"
}
```

Rules:

- This phase must be local-only.
- It should not depend on translation.
- It should not depend on upload completion.

### Phase 3: Create WordPress Shells

Create or update placeholder pages in this order:

1. Categories
2. Sections
3. Articles, optional if article URLs can be predicted reliably

Purpose:

- Obtain stable `wp_id`
- Confirm final WordPress URL
- Prevent internal links from pointing to missing pages during final render

Shell content can be minimal but should be recognizable.

Example shell content:

```html
<p>Content is being prepared from the local Klaviyo source snapshot.</p>
```

Rules:

- Use stable English slug.
- Save `wp_id`, `slug`, and `link` immediately.
- If a shell exists, update it instead of creating duplicates.
- Never delete remote docs during this phase.

### Phase 4: Translate Content

Translate only after source structure and expected URL maps exist.

Category translation:

- Translate display category name.
- Keep category ID and source URL unchanged.

Section translation:

- Translate section title if the final site should use Chinese section titles.
- Keep section ID, category ID, and source URL unchanged.

Article translation:

- Translate visible text.
- Preserve HTML structure and attributes.
- Preserve images and links exactly until link resolution.

Translation must not translate URL-bearing fields.

Recommended approach:

1. Parse HTML into DOM.
2. Translate text nodes only.
3. Preserve attributes.
4. Rebuild HTML.
5. Run link resolver after translation.

### Phase 5: Render Final HTML

Render each mode differently.

Category pages:

- Use BetterDocs native breadcrumb/title/navigation where appropriate.
- Body should show section cards.
- Cards link to section pages.
- Do not show article lists as the primary category layout.

Section pages:

- Use list format, matching Klaviyo section pages.
- Do not use cards for articles.
- Do not duplicate custom section title if BetterDocs already shows title.
- Body should start directly with article list.
- Article rows link to article pages.
- Include article excerpts when available from source snapshot.

Article pages:

- Hide BetterDocs category sidebar.
- Use article TOC behavior previously approved.
- Remove duplicate TOC, reactions, and social share.
- Preserve source semantics: lists stay lists, resources stay lists unless source is card-based.

### Phase 6: Resolve Links

All internal Klaviyo links must be resolved after translation and before final upload.

Resolver behavior:

```text
Klaviyo category URL -> local category URL
Klaviyo section URL  -> local section URL
Klaviyo article URL  -> local article URL
External URL         -> keep original
Same-page anchor     -> keep or normalize
Unknown URL          -> keep original and log warning
```

Examples:

```text
https://help.klaviyo.com/hc/en-us/categories/48274996158235
=> https://dynamicycle.com/docs/categories-customer-agent/

https://help.klaviyo.com/hc/en-us/sections/49191914194587-Guidance
=> https://dynamicycle.com/docs/sections-customer-agent-guidance/

https://help.klaviyo.com/hc/en-us/articles/115005085427
=> https://dynamicycle.com/docs/articles-understanding-unique-vs-total-opens-and-clicks/
```

Resolver input should include:

- `category-menu.json`
- `category-doc-uploads.json`
- `sections-articles.json`
- `section_upload_meta.json`
- `.crawl_meta.json`
- `.upload_meta.json`

Resolver output should include:

- Updated HTML content
- `unresolved-links-report.json`

### Phase 7: Upload Final Content

Recommended final upload order:

1. Upload/update categories.
2. Upload/update sections.
3. Upload/update articles.
4. Run link resolver again with complete upload maps.
5. Update categories, sections, and articles one more time with final links.

This second update pass prevents category and section pages from keeping stale source links.

### Phase 8: Verify

Verify after upload:

- Every category page links to local section pages.
- Every section page links to local article pages.
- Every article internal Klaviyo category/section/article URL has been replaced.
- External links remain external.
- No unexpected Chinese slugs.
- No duplicated WordPress docs from slug mismatch.
- No unresolved internal Klaviyo links except known unsupported pages.

Suggested reports:

- `unresolved-links-report.json`
- `internal-link-resolution-summary.json`
- `upload-summary.json`
- `duplicate-slug-report.json`

## Link Direction Rules

### Category Page Links

Primary link target:

```text
category -> section
```

Category pages should not primarily jump directly to articles unless a section has no meaningful grouping.

### Section Page Links

Primary link target:

```text
section -> article
```

Section page layout should use a vertical list of article links, not cards.

### Article Page Links

Article pages may link to:

```text
article -> article
article -> section
article -> category
article -> external
```

All Klaviyo internal links should be converted to local BetterDocs links.

## Translation Boundary Checklist

Before translation:

- Source snapshots exist.
- Category/section/article relations exist.
- Stable slugs are generated.
- Expected URL map exists.

During translation:

- Translate visible text nodes only.
- Preserve IDs, URLs, slugs, links, images, and attributes.
- Do not translate frontmatter keys or metadata values except display title/category/section names when intended.

After translation:

- Render HTML.
- Resolve links.
- Upload.
- Save `wp_id` and `wp_url`.
- Run verification.

## Implementation Milestones

1. Add local URL map generator.
2. Add WordPress shell creation for categories, sections, and optionally articles.
3. Add DOM-based translation wrapper that preserves attributes.
4. Add internal Klaviyo link resolver.
5. Add final two-pass upload.
6. Add verification reports.
7. Archive design rules for each mode:
   - Category
   - Section
   - Article

