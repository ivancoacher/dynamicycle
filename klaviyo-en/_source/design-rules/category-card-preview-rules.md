# Category Card Preview Rules

Archived: 2026-05-24

These rules describe the approved BetterDocs category preview layout tested on:

- `https://dynamicycle.com/docs/categories-customer-agent-2/`
- Local generator: `python3 sync/pipeline.py upload-category-preview customer-agent`

## Scope

Use these rules for category-type preview pages that represent a Klaviyo category and its child sections.

Do not apply these rules to normal Klaviyo article pages. Article pages must continue to follow the article-specific TOC/sidebar rules.

## Approved Category Preview Layout

- Use BetterDocs native breadcrumb, title, and left navigation. Do not recreate the BetterDocs title/navigation inside custom content.
- The custom content body should start directly with the section card grid.
- Do not show a duplicate custom `<h1>` for the category name inside `.dc-category-page`.
- Do not prefix the WordPress document title with `Category:`. Use the plain category name, for example `Customer Agent`.
- Use card mode for category sections, not an article list.
- Each card should represent one section and show:
  - Section name
  - Article count, e.g. `5 articles` or `1 article`
- Keep cards clean and quiet:
  - White background
  - 8px border radius
  - Light border
  - Subtle shadow
  - Centered section name and count
- Do not show the article list on this category preview page.

## Spacing Rules

- `.dc-category-page` should not be centered with large side gaps.
- Use `margin: 0`, not `margin: 0 auto`, so the card grid aligns with the BetterDocs content column.
- Remove top padding above the card grid.
- Keep bottom padding modest.
- The card grid should start close below the BetterDocs title.

Current approved CSS pattern:

```css
.dc-category-page {
  max-width: 980px;
  margin: 0;
  padding: 0 0 28px;
}

.dc-category-hero,
.dc-category-meta {
  display: none;
}

.dc-section-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(220px, 1fr));
  gap: 20px 24px;
  margin-top: 0;
}

.dc-section-grid > br {
  display: none !important;
}
```

## WordPress Auto-Formatting Gotcha

WordPress/BetterDocs may insert `<br>` nodes inside the custom grid. CSS grid treats those `<br>` elements as grid items, which can make the first real card appear missing or shifted.

Always include:

```css
.dc-section-grid > br {
  display: none !important;
}
```

## Upload Behavior

- Category preview uploads should update the stored preview `wp_id` from `klaviyo-en/_source/category_preview_uploads.json` when available.
- Do not accidentally update the formal 20 homepage category documents when the user is reviewing a category preview sample.
- Save preview metadata in `klaviyo-en/_source/category_preview_uploads.json`.

## Verification Checklist

After uploading a category preview:

- BetterDocs title shows the plain category name.
- Custom body has no duplicate category `<h1>`.
- Page does not contain `Category: {Name}`.
- `.dc-section-card` count equals the number of sections.
- `.dc-category-section li` count is `0` for card-mode preview pages.
- The first card is visible in the first grid slot.
