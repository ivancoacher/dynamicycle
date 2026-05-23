#!/usr/bin/env python3
"""Push Klaviyo articles to BetterDocs via WordPress REST API.

Usage:
    python3 klaviyo_push.py                     # Push all articles
    python3 klaviyo_push.py --category campaigns # Push specific category
    python3 klaviyo_push.py --dry-run            # Preview without pushing
"""

import json
import os
import re
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
KLAVIYO_DIR = PROJECT_ROOT / "klaviyo"
BATTERDOCS_DIR = PROJECT_ROOT / "batterDocs"
load_dotenv(PROJECT_ROOT / ".env")

WP_SITE_URL = os.getenv("WP_SITE_URL", "").rstrip("/")
WP_USERNAME = os.getenv("WP_USERNAME", "")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD", "")
WP_API_BASE = os.getenv("WP_API_BASE", "/wp-json/wp/v2")

# batterDocs category slug -> WordPress term ID
CATEGORY_IDS = {
    "account-billing": 775425969,
    "advanced-kdp-marketing-analytics": 775425957,
    "analytics-audience": 775425956,
    "campaigns": 775425959,
    "content": 775425958,
    "conversations": 775425960,
    "customer-agent": 775425976,
    "customer-hub": 775425961,
    "deliverability-compliance": 775425963,
    "flows": 775425971,
    "helpdesk": 775425977,
    "integrations": 775425972,
    "reviews": 775425973,
    "sign-up-forms": 775425974,
    "sms-whatsapp": 775425975,
}

PUSH_META = KLAVIYO_DIR / ".push_meta.json"


def api_url(endpoint: str) -> str:
    return f"{WP_SITE_URL}{WP_API_BASE}{endpoint}"


def auth() -> tuple:
    return (WP_USERNAME, WP_APP_PASSWORD)


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()

    meta = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            meta[key] = val

    return meta, body


def load_push_meta() -> dict:
    if PUSH_META.exists():
        return json.loads(PUSH_META.read_text("utf-8"))
    return {"pushed": {}}


def save_push_meta(meta: dict):
    PUSH_META.write_text(json.dumps(meta, indent=2, ensure_ascii=False), "utf-8")


def get_existing_docs() -> set:
    """Get set of titles already on BetterDocs to avoid duplicates."""
    titles = set()
    page = 1
    while True:
        resp = requests.get(
            api_url("/docs"),
            params={"per_page": 100, "page": page},
            auth=auth(),
            timeout=30,
        )
        data = resp.json()
        if not data:
            break
        for d in data:
            titles.add(d["title"]["rendered"])
        total_pages = int(resp.headers.get("X-WP-TotalPages", 1))
        if page >= total_pages:
            break
        page += 1
    return titles


def push_articles(category_filter: str = None, dry_run: bool = False):
    """Push Klaviyo articles to BetterDocs."""
    print("Loading existing docs from BetterDocs...")
    existing_titles = get_existing_docs()
    print(f"Found {len(existing_titles)} existing docs on remote")

    push_meta = load_push_meta()
    pushed = push_meta.get("pushed", {})

    # Collect all articles to push
    articles_to_push = []
    for cat_dir in sorted(KLAVIYO_DIR.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name.startswith("."):
            continue
        if category_filter and cat_dir.name != category_filter:
            continue

        cat_slug = cat_dir.name
        cat_id = CATEGORY_IDS.get(cat_slug)
        if not cat_id:
            print(f"  SKIP unknown category: {cat_slug}")
            continue

        for md_file in sorted(cat_dir.glob("*.md")):
            content = md_file.read_text("utf-8")
            fm, body = parse_frontmatter(content)
            title = fm.get("title", md_file.stem)
            klaviyo_id = fm.get("id", "")

            # Skip if already pushed
            if klaviyo_id in pushed:
                continue

            # Skip if title already exists on remote
            if title in existing_titles:
                continue

            articles_to_push.append({
                "klaviyo_id": klaviyo_id,
                "title": title,
                "body": body,
                "cat_slug": cat_slug,
                "cat_id": cat_id,
                "source_url": fm.get("source_url", ""),
                "filename": f"{cat_slug}/{md_file.name}",
            })

    print(f"\nArticles to push: {len(articles_to_push)}")

    if dry_run:
        for a in articles_to_push[:20]:
            print(f"  [{a['cat_slug']}] {a['title'][:60]}")
        if len(articles_to_push) > 20:
            print(f"  ... and {len(articles_to_push) - 20} more")
        return

    # Push in batches
    success = 0
    failed = 0
    for i, a in enumerate(articles_to_push):
        resp = requests.post(
            api_url("/docs"),
            json={
                "title": a["title"],
                "content": a["body"],
                "status": "publish",
                "doc_category": [a["cat_id"]],
            },
            auth=auth(),
            timeout=30,
        )

        if resp.status_code in (200, 201):
            data = resp.json()
            wp_id = data["id"]
            pushed[a["klaviyo_id"]] = {
                "wp_id": wp_id,
                "title": a["title"],
                "filename": a["filename"],
                "pushed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            success += 1
            if success % 10 == 0:
                save_push_meta({"pushed": pushed})
                print(f"  Progress: {success}/{len(articles_to_push)} pushed")
        else:
            print(f"  FAILED: {a['title'][:50]} — {resp.status_code}")
            failed += 1

        # Rate limit
        time.sleep(0.5)

    save_push_meta({"pushed": pushed})
    print(f"\nDone. Pushed: {success}, Failed: {failed}")

    # Also copy to batterDocs local directory
    print("\nCopying to local batterDocs directory...")
    copied = 0
    for a in articles_to_push:
        if a["klaviyo_id"] not in pushed:
            continue
        src = KLAVIYO_DIR / a["filename"]
        dst = BATTERDOCS_DIR / a["filename"]
        if not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(src.read_text("utf-8"), "utf-8")
            copied += 1
    print(f"Copied {copied} new articles to batterDocs/")


if __name__ == "__main__":
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    cat_filter = None
    if "--category" in args:
        idx = args.index("--category")
        cat_filter = args[idx + 1] if idx + 1 < len(args) else None

    push_articles(category_filter=cat_filter, dry_run=dry_run)
