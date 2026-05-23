#!/usr/bin/env python3
"""Klaviyo Help Center Crawler.

Crawls all articles from help.klaviyo.com via Zendesk API,
converts to markdown with batterDocs-compatible frontmatter.

Usage:
    python3 klaviyo_crawler.py              # Crawl all articles
    python3 klaviyo_crawler.py --category campaigns  # Crawl specific category
    python3 klaviyo_crawler.py --count-only          # Just count articles
"""

import json
import os
import re
import sys
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
KLAVIYO_DIR = PROJECT_ROOT / "klaviyo"
META_FILE = KLAVIYO_DIR / ".crawl_meta.json"

ZENDESK_API = "https://help.klaviyo.com/api/v2/help_center/en-us"

# Klaviyo category -> batterDocs category slug mapping
CATEGORY_MAP = {
    115000867647: "account-billing",            # Account & billing
    18073014919195: "advanced-kdp-marketing-analytics",  # Advanced KDP & Marketing Analytics
    115000874048: "analytics-audience",          # Analytics
    115000867867: "analytics-audience",          # Audience
    49375106949275: "campaigns",                 # Campaigns
    4414879524891: "content",                    # Content
    14234163769755: "conversations",             # Conversations
    48274996158235: "customer-agent",            # Customer Agent
    34141283979931: "customer-hub",              # Customer Hub
    115000873988: "deliverability-compliance",   # Deliverability & compliance
    115000312411: "flows",                       # Flows
    45954023294747: "helpdesk",                  # Helpdesk
    115000032731: "integrations",                # Integrations
    49375133274139: "reviews",                   # Reviews
    360000190711: "sign-up-forms",              # Sign-up forms
    29173800271259: "sms-whatsapp",             # SMS
    49375107982619: "sms-whatsapp",             # WhatsApp
    50128030093211: "content",                  # Social Marketing -> content
}

# Category names (for display)
CATEGORY_NAMES = {
    115000867647: "Account & billing",
    18073014919195: "Advanced KDP & Marketing Analytics",
    115000874048: "Analytics",
    115000867867: "Audience",
    49375106949275: "Campaigns",
    4414879524891: "Content",
    14234163769755: "Conversations",
    48274996158235: "Customer Agent",
    34141283979931: "Customer Hub",
    45954023294747: "Helpdesk",
    115000873988: "Deliverability & compliance",
    115000312411: "Flows",
    115000032731: "Integrations",
    49375133274139: "Reviews",
    360000190711: "Sign-up forms",
    29173800271259: "SMS",
    49375107982619: "WhatsApp",
    50128030093211: "Social Marketing",
}


def api_get(endpoint: str, params: dict = None) -> dict:
    """Make a Zendesk API request with rate limiting."""
    resp = requests.get(f"{ZENDESK_API}{endpoint}", params=params or {}, timeout=30)
    if resp.status_code == 429:
        retry_after = int(resp.headers.get("Retry-After", 5))
        print(f"  Rate limited, waiting {retry_after}s...")
        time.sleep(retry_after)
        return api_get(endpoint, params)
    resp.raise_for_status()
    return resp.json()


def html_to_markdown(html: str) -> str:
    """Convert HTML to clean Markdown."""

    class CleanConverter(MarkdownConverter):
        def convert_img(self, el, text, **kwargs):
            src = el.get("src", "")
            alt = el.get("alt", "")
            if not src:
                return ""
            return f"![{alt}]({src})"

        def convert_iframe(self, el, text, **kwargs):
            src = el.get("src", "")
            if src:
                title = el.get("title", "Embedded content")
                return f"[{title}]({src})"
            return ""

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()

    md = CleanConverter(
        heading_style="atx",
        bullets="-",
        strong_em_symbol="**",
        strip=["script", "style"],
    ).convert_soup(soup)

    md = re.sub(r"\n{4,}", "\n\n\n", md)
    md = "\n".join(line.rstrip() for line in md.split("\n"))
    return md.strip()


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = re.sub(r"\s+", "-", name.strip())
    return name[:120]


def get_sections() -> dict:
    """Fetch all sections with category mapping."""
    sections = {}
    page = 1
    while True:
        data = api_get("/sections.json", {"per_page": 100, "page": page})
        for s in data.get("sections", []):
            sections[s["id"]] = {
                "name": s["name"],
                "category_id": s.get("category_id"),
            }
        if len(data.get("sections", [])) < 100:
            break
        page += 1
    return sections


def get_all_articles() -> list:
    """Fetch all articles (paginated)."""
    all_articles = []
    page = 1
    while True:
        data = api_get("/articles.json", {"per_page": 100, "page": page})
        articles = data.get("articles", [])
        if not articles:
            break
        all_articles.extend(articles)
        print(f"  Fetched page {page}: {len(articles)} articles (total: {len(all_articles)})")
        if len(articles) < 100:
            break
        page += 1
        time.sleep(0.3)
    return all_articles


def crawl_all(category_filter: str = None):
    """Main crawl function."""
    KLAVIYO_DIR.mkdir(parents=True, exist_ok=True)

    print("Fetching sections...")
    sections = get_sections()
    print(f"Found {len(sections)} sections")

    print("Fetching articles...")
    articles = get_all_articles()
    print(f"Found {len(articles)} articles")

    # Filter by category if specified
    if category_filter:
        filtered = []
        for a in articles:
            sec = sections.get(a.get("section_id"), {})
            cat_id = sec.get("category_id")
            mapped = CATEGORY_MAP.get(cat_id, "uncategorized")
            if mapped == category_filter:
                filtered.append(a)
        print(f"Filtered to {len(filtered)} articles in '{category_filter}'")
        articles = filtered

    meta = {"articles": {}, "sections": {str(k): v for k, v in sections.items()}}

    # Stats
    stats = {}
    for a in articles:
        sec = sections.get(a.get("section_id"), {})
        cat_id = sec.get("category_id", 0)
        cat_slug = CATEGORY_MAP.get(cat_id, "uncategorized")
        stats[cat_slug] = stats.get(cat_slug, 0) + 1

    print("\nCategory distribution:")
    for slug, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {slug}: {count}")

    # Save articles
    print(f"\nSaving {len(articles)} articles...")
    saved = 0
    for a in articles:
        article_id = a["id"]
        title = a.get("title", a.get("name", "Untitled"))
        html_body = a.get("body", "") or ""
        html_url = a.get("html_url", "")
        section_id = a.get("section_id")
        updated_at = a.get("updated_at", "")
        draft = a.get("draft", False)

        if draft:
            continue

        # Map to category
        sec = sections.get(section_id, {})
        cat_id = sec.get("category_id", 0)
        cat_slug = CATEGORY_MAP.get(cat_id, "uncategorized")
        cat_name = CATEGORY_NAMES.get(cat_id, "Uncategorized")

        # Create directory
        cat_dir = KLAVIYO_DIR / cat_slug
        cat_dir.mkdir(parents=True, exist_ok=True)

        # Convert to markdown
        md_content = html_to_markdown(html_body)

        # Build frontmatter
        filename = f"{sanitize_filename(title)}.md"
        filepath = cat_dir / filename

        frontmatter = f"""---
id: {article_id}
title: "{title.replace('"', '\\"')}"
source_url: "{html_url}"
section: "{sec.get('name', '')}"
category: "{cat_name}"
category_slug: "{cat_slug}"
klaviyo_updated: "{updated_at}"
language: en
---

"""
        filepath.write_text(frontmatter + md_content, "utf-8")

        meta["articles"][str(article_id)] = {
            "title": title,
            "filename": f"{cat_slug}/{filename}",
            "source_url": html_url,
            "category_slug": cat_slug,
            "klaviyo_updated": updated_at,
        }
        saved += 1

    # Save metadata
    META_FILE.write_text(json.dumps(meta, indent=2, ensure_ascii=False), "utf-8")
    print(f"\nDone. Saved {saved} articles to {KLAVIYO_DIR}")


def count_only():
    """Just count articles per category."""
    print("Fetching sections...")
    sections = get_sections()

    print("Fetching articles...")
    articles = get_all_articles()

    stats = {}
    for a in articles:
        sec = sections.get(a.get("section_id"), {})
        cat_id = sec.get("category_id", 0)
        cat_slug = CATEGORY_MAP.get(cat_id, "uncategorized")
        cat_name = CATEGORY_NAMES.get(cat_id, "Unknown")
        if cat_slug not in stats:
            stats[cat_slug] = {"name": cat_name, "count": 0}
        stats[cat_slug]["count"] += 1

    print(f"\nTotal: {len(articles)} articles in {len(stats)} categories\n")
    for slug, info in sorted(stats.items(), key=lambda x: -x[1]["count"]):
        print(f"  {slug:40s} ({info['name']:40s}): {info['count']}")


if __name__ == "__main__":
    args = sys.argv[1:]

    if "--count-only" in args:
        count_only()
    elif "--category" in args:
        idx = args.index("--category")
        cat = args[idx + 1] if idx + 1 < len(args) else None
        crawl_all(category_filter=cat)
    else:
        crawl_all()
