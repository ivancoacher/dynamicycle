#!/usr/bin/env python3
"""BetterDocs Git Sync Tool.

Syncs documentation between WordPress BetterDocs and local markdown files.

Usage:
    python sync.py pull     — Download all docs from BetterDocs → markdown files
    python sync.py push     — Upload local markdown files → BetterDocs
    python sync.py status   — Show diff between local and remote
"""

import json
import os
import re
import sys
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from markdownify import MarkdownConverter

# Load .env from project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

WP_SITE_URL = os.getenv("WP_SITE_URL", "").rstrip("/")
WP_USERNAME = os.getenv("WP_USERNAME", "")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD", "")
WP_API_BASE = os.getenv("WP_API_BASE", "/wp-json/wp/v2")

BATTERDOCS_DIR = PROJECT_ROOT / "batterDocs"
META_FILE = BATTERDOCS_DIR / ".sync_meta.json"

# --- Helpers ---

def api_url(endpoint: str) -> str:
    return f"{WP_SITE_URL}{WP_API_BASE}{endpoint}"


def auth() -> tuple:
    return (WP_USERNAME, WP_APP_PASSWORD)


def get_all_docs() -> list[dict]:
    """Fetch all docs from BetterDocs API (paginated)."""
    all_docs = []
    page = 1
    while True:
        resp = requests.get(
            api_url("/docs"),
            params={"per_page": 100, "page": page},
            auth=auth(),
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        all_docs.extend(data)
        total_pages = int(resp.headers.get("X-WP-TotalPages", 1))
        if page >= total_pages:
            break
        page += 1
        time.sleep(0.5)
    return all_docs


def get_all_categories() -> dict:
    """Fetch all doc categories, return {id: name_slug} mapping."""
    resp = requests.get(
        api_url("/doc_category"),
        params={"per_page": 100},
        auth=auth(),
        timeout=30,
    )
    resp.raise_for_status()
    cats = {}
    for c in resp.json():
        cats[c["id"]] = {
            "name": c["name"],
            "slug": c["slug"],
            "count": c.get("count", 0),
        }
    return cats


def html_to_markdown(html: str) -> str:
    """Convert HTML content to clean Markdown."""

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

    # Pre-process: clean up WP-specific markup
    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style tags
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()

    # Convert buttons/links that are just wrappers
    for a in soup.find_all("a"):
        if not a.get_text(strip=True) and a.find("img"):
            continue

    cleaned_html = str(soup)

    md = CleanConverter(
        heading_style="atx",
        bullets="-",
        strong_em_symbol="**",
        strip=["script", "style"],
    ).convert_soup(soup)

    # Post-process cleanup
    # Remove excessive blank lines
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    # Clean up trailing whitespace per line
    md = "\n".join(line.rstrip() for line in md.split("\n"))
    # Remove zero-width characters
    md = md.replace("​", "").replace("‌", "").replace("﻿", "")

    return md.strip()


def sanitize_filename(name: str) -> str:
    """Convert title to safe filename."""
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = re.sub(r"\s+", "-", name.strip())
    name = name[:100]
    return name


def load_meta() -> dict:
    if META_FILE.exists():
        return json.loads(META_FILE.read_text("utf-8"))
    return {"docs": {}, "categories": {}}


def save_meta(meta: dict):
    META_FILE.write_text(json.dumps(meta, indent=2, ensure_ascii=False), "utf-8")


# --- Commands ---

def cmd_pull():
    """Download all docs from BetterDocs to local markdown files."""
    print("Fetching categories...")
    categories = get_all_categories()
    print(f"Found {len(categories)} categories")

    print("Fetching all docs...")
    docs = get_all_docs()
    print(f"Found {len(docs)} docs")

    meta = {"docs": {}, "categories": {}}

    # Save category mapping
    for cat_id, cat_info in categories.items():
        meta["categories"][str(cat_id)] = cat_info
        cat_dir = BATTERDOCS_DIR / cat_info["slug"]
        cat_dir.mkdir(parents=True, exist_ok=True)

    # Process each doc
    for doc in docs:
        doc_id = doc["id"]
        title = doc["title"]["rendered"]
        html_content = doc["content"]["rendered"]
        slug = doc["slug"]
        modified = doc.get("modified_gmt", "")
        cat_ids = doc.get("doc_category", [])

        # Determine category directory
        cat_slug = "uncategorized"
        cat_name = "未分类"
        if cat_ids:
            cat_info = categories.get(cat_ids[0])
            if cat_info:
                cat_slug = cat_info["slug"]
                cat_name = cat_info["name"]

        cat_dir = BATTERDOCS_DIR / cat_slug
        cat_dir.mkdir(parents=True, exist_ok=True)

        # Convert to markdown
        md_content = html_to_markdown(html_content)

        # Build file with frontmatter
        filename = f"{sanitize_filename(title)}.md"
        filepath = cat_dir / filename

        frontmatter = f"""---
id: {doc_id}
title: "{title.replace('"', '\\"')}"
slug: "{slug}"
category: "{cat_name}"
category_slug: "{cat_slug}"
wp_url: "{doc.get('link', '')}"
wp_modified: "{modified}"
---

"""
        filepath.write_text(frontmatter + md_content, "utf-8")

        # Update meta
        meta["docs"][str(doc_id)] = {
            "title": title,
            "slug": slug,
            "filename": f"{cat_slug}/{filename}",
            "wp_modified": modified,
            "category": cat_name,
        }

        print(f"  [{cat_slug}] {title[:50]}")

    save_meta(meta)
    print(f"\nDone. {len(docs)} docs synced to {BATTERDOCS_DIR}")


def cmd_push():
    """Upload local markdown changes back to BetterDocs."""
    if not WP_USERNAME or not WP_APP_PASSWORD:
        print("Error: WP credentials not configured. Check .env file.")
        sys.exit(1)

    meta = load_meta()
    if not meta.get("docs"):
        print("No sync metadata found. Run 'pull' first.")
        sys.exit(1)

    pushed = 0
    skipped = 0

    for doc_id, doc_meta in meta["docs"].items():
        filepath = BATTERDOCS_DIR / doc_meta["filename"]
        if not filepath.exists():
            print(f"  SKIP (file missing): {doc_meta['filename']}")
            skipped += 1
            continue

        content = filepath.read_text("utf-8")

        # Strip frontmatter
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                content = content[end + 3:].strip()

        # Update via API
        resp = requests.post(
            api_url(f"/docs/{doc_id}"),
            json={
                "content": content,
                "status": "publish",
            },
            auth=auth(),
            timeout=30,
        )

        if resp.status_code == 200:
            print(f"  PUSHED: {doc_meta['title'][:50]}")
            pushed += 1
        else:
            print(f"  FAILED: {doc_meta['title'][:50]} — {resp.status_code}: {resp.text[:100]}")

        time.sleep(0.5)

    print(f"\nDone. Pushed: {pushed}, Skipped: {skipped}")


def cmd_status():
    """Compare local files with remote docs."""
    meta = load_meta()
    if not meta.get("docs"):
        print("No sync metadata found. Run 'pull' first.")
        return

    print("Fetching remote docs for comparison...")
    remote_docs = {str(d["id"]): d for d in get_all_docs()}

    local_ids = set(meta["docs"].keys())
    remote_ids = set(remote_docs.keys())

    new_remote = remote_ids - local_ids
    new_local = local_ids - remote_ids
    common = local_ids & remote_ids

    updated = []
    for doc_id in common:
        remote_modified = remote_docs[doc_id].get("modified_gmt", "")
        local_modified = meta["docs"][doc_id].get("wp_modified", "")
        if remote_modified != local_modified:
            updated.append(doc_id)

    print(f"\nStatus:")
    print(f"  Local docs:  {len(local_ids)}")
    print(f"  Remote docs: {len(remote_ids)}")
    print(f"  New remote:  {len(new_remote)}")
    print(f"  New local:   {len(new_local)}")
    print(f"  Updated:     {len(updated)}")

    if new_remote:
        print(f"\n  New on remote:")
        for doc_id in new_remote:
            title = remote_docs[doc_id]["title"]["rendered"]
            print(f"    + {title}")

    if updated:
        print(f"\n  Modified on remote:")
        for doc_id in updated:
            title = remote_docs[doc_id]["title"]["rendered"]
            print(f"    ~ {title}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    command = sys.argv[1].lower()
    commands = {"pull": cmd_pull, "push": cmd_push, "status": cmd_status}

    if command not in commands:
        print(f"Unknown command: {command}")
        print(f"Available: {', '.join(commands.keys())}")
        sys.exit(1)

    commands[command]()
