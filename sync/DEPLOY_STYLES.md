# Deploy Preview Style Ownership

The generated category, section, and article pages inline their CSS, but their
shared source is `sync/deploy-shared.css`.

## Shared Decisions

- Category and section pages use the same 360px topic column, 44px content
  inset, divider, background, Chinese font stack, and mobile collapse rules.
- Topic-menu icons use a fixed 28x28px container and a 26x26px SVG.
- Topic-menu items keep an 8px left inset so icons do not touch the item edge.
- Category and section article lists share title, excerpt, spacing, color, and
  link styles.
- Article pages share the same page background, font tokens, divider color,
  sidebar foundations, and responsive breakpoints.

## Where To Edit

- Change cross-page colors, fonts, widths, sidebars, list presentation, or
  responsive behavior in `sync/deploy-shared.css`.
- Keep only page-specific components in `sync/deploy.py`:
  category cards and header, section path and groups, article header and body.
- Do not edit generated files under `build/deploy-previews/` manually.

After a style change, regenerate and inspect all page types:

```bash
.venv/bin/python sync/deploy.py preview
```
