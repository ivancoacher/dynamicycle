# Customer Agent Category Sync Report

Executed: 2026-05-24

## Source

- Category source URL: `https://help.klaviyo.com/hc/en-us/categories/48274996158235`
- Category slug: `customer-agent`

## Result

- Category page: `https://dynamicycle.com/docs/categories-customer-agent/`
- Sections: 5/5 uploaded
- Articles: 20/20 translated and uploaded
- Internal Klaviyo doc links: 0 unresolved
- Duplicate article slugs: 0
- Duplicate article WordPress IDs in metadata: 0

## Section Pages

- `https://dynamicycle.com/docs/sections-customer-agent-guidance/`
- `https://dynamicycle.com/docs/sections-customer-agent-launch/`
- `https://dynamicycle.com/docs/sections-customer-agent-skills/`
- `https://dynamicycle.com/docs/sections-customer-agent-tools/`
- `https://dynamicycle.com/docs/sections-customer-agent-training/`

## Notes

- The category page was normalized back to the canonical slug `categories-customer-agent`.
- Duplicate English article titles are now disambiguated by appending the Klaviyo article ID to the slug.
- Stale WordPress IDs in `.upload_meta.json` are handled by falling back to slug lookup or creating a new doc.
- The old `categories-customer-agent-2` page still exists remotely as an earlier preview artifact, but current local metadata and URL maps point to `categories-customer-agent`.

## Commands

```bash
python3 sync/pipeline.py sync-category https://help.klaviyo.com/hc/en-us/categories/48274996158235 --dry-run
python3 sync/pipeline.py sync-category https://help.klaviyo.com/hc/en-us/categories/48274996158235 --force
python3 sync/pipeline.py prepare-url-maps
python3 sync/pipeline.py verify-url-maps
```
