#!/usr/bin/env python3
"""Klaviyo Docs Sync Pipeline.

Full pipeline: Crawl → Push EN → Translate → Push ZH
Each article is processed individually (stream, not batch).

Usage:
    python3 pipeline.py crawl              # Step 1: Crawl from Klaviyo
    python3 pipeline.py push-en            # Step 2: Push English to WP
    python3 pipeline.py translate          # Step 3: Translate EN → ZH
    python3 pipeline.py push-zh            # Step 4: Push Chinese to WP
    python3 pipeline.py full               # Steps 1-4 in sequence
    python3 pipeline.py status             # Show sync status
"""

import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from core import (
    KLAVIYO_DIR, BATTERDOCS_DIR, PROJECT_ROOT,
    WP_CATEGORY_IDS, KLAVIYO_CATEGORY_MAP, KLAVIYO_CATEGORY_NAMES,
    ZendeskClient, WordPressClient,
    html_to_markdown, sanitize_filename, parse_frontmatter, build_frontmatter,
    load_json, save_json, SyncLogger, with_retry,
)

CRAWL_META = KLAVIYO_DIR / ".crawl_meta.json"
PUSH_EN_META = KLAVIYO_DIR / ".push_en_meta.json"
TRANSLATE_META = KLAVIYO_DIR / ".translate_meta.json"
PUSH_ZH_META = KLAVIYO_DIR / ".push_zh_meta.json"


# ============================================================
# Step 1: Crawl
# ============================================================

def cmd_crawl():
    """Crawl all articles from Klaviyo Help Center."""
    logger = SyncLogger("Crawl")
    KLAVIYO_DIR.mkdir(parents=True, exist_ok=True)

    print("[1/4] Fetching sections...")
    zendesk = ZendeskClient()
    sections = zendesk.get_sections()
    print(f"  Found {len(sections)} sections")

    print("[1/4] Fetching articles...")
    articles = zendesk.get_all_articles()
    print(f"  Found {len(articles)} articles")

    meta = load_json(CRAWL_META)
    if "articles" not in meta:
        meta["articles"] = {}

    print("[1/4] Saving to klaviyo/...")
    for a in articles:
        if a.get("draft"):
            continue

        article_id = str(a["id"])
        title = a.get("title", a.get("name", "Untitled"))
        html_body = a.get("body", "") or ""
        html_url = a.get("html_url", "")
        section_id = a.get("section_id")
        updated_at = a.get("updated_at", "")

        sec = sections.get(section_id, {})
        cat_id = sec.get("category_id", 0)
        cat_slug = KLAVIYO_CATEGORY_MAP.get(cat_id, "uncategorized")
        cat_name = KLAVIYO_CATEGORY_NAMES.get(cat_id, "Uncategorized")

        cat_dir = KLAVIYO_DIR / cat_slug
        cat_dir.mkdir(parents=True, exist_ok=True)

        md_content = html_to_markdown(html_body)
        filename = f"{sanitize_filename(title)}.md"

        frontmatter = build_frontmatter({
            "id": article_id,
            "title": title.replace('"', '\\"'),
            "source_url": html_url,
            "section": sec.get("name", ""),
            "category": cat_name,
            "category_slug": cat_slug,
            "klaviyo_updated": updated_at,
            "language": "en",
        })

        filepath = cat_dir / filename
        filepath.write_text(frontmatter + md_content, "utf-8")

        # Check if new or updated
        existing = meta["articles"].get(article_id, {})
        if existing.get("klaviyo_updated") != updated_at:
            meta["articles"][article_id] = {
                "title": title,
                "filename": f"{cat_slug}/{filename}",
                "source_url": html_url,
                "category_slug": cat_slug,
                "klaviyo_updated": updated_at,
                "status": "new" if not existing else "updated",
            }
            logger.ok(f"[{cat_slug}] {title[:50]}")
        else:
            logger.skip(f"[{cat_slug}] {title[:50]}")

    save_json(CRAWL_META, meta)
    logger.summary()
    return logger.results


# ============================================================
# Step 2: Push English to WP (streaming)
# ============================================================

def cmd_push_en():
    """Push English articles to WordPress BetterDocs. One by one."""
    logger = SyncLogger("Push EN")
    crawl_meta = load_json(CRAWL_META)
    push_meta = load_json(PUSH_EN_META)
    wp = WordPressClient()

    articles = crawl_meta.get("articles", {})
    pushed = push_meta.get("pushed", {})

    print(f"[2/4] {len(articles)} articles in crawl meta, {len(pushed)} already pushed")

    for article_id, info in articles.items():
        if article_id in pushed:
            logger.skip(f"{info['title'][:50]}")
            continue

        filepath = KLAVIYO_DIR / info["filename"]
        if not filepath.exists():
            logger.fail(f"File missing: {info['filename']}")
            continue

        content = filepath.read_text("utf-8")
        _, body = parse_frontmatter(content)

        try:
            result = wp.create_doc(
                title=info["title"],
                content=body,
                category_slug=info["category_slug"],
            )
            pushed[article_id] = {
                "wp_id": result["id"],
                "title": info["title"],
                "filename": info["filename"],
                "category_slug": info["category_slug"],
                "pushed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            logger.ok(f"[{info['category_slug']}] {info['title'][:50]} → WP #{result['id']}")

            # Save meta every 50 articles
            if logger.results["success"] % 50 == 0:
                save_json(PUSH_EN_META, {"pushed": pushed})

        except Exception as e:
            logger.fail(f"{info['title'][:50]}: {e}")
            # Save progress even on failure
            save_json(PUSH_EN_META, {"pushed": pushed})
            continue

        time.sleep(0.5)

    save_json(PUSH_EN_META, {"pushed": pushed})
    logger.summary()
    return logger.results


# ============================================================
# Step 3: Translate EN → ZH
# ============================================================

def translate_text(text: str, target_lang: str = "zh-CN") -> str:
    """Translate text using Google Translate (free, no API key)."""
    from deep_translator import GoogleTranslator

    # Split into chunks of ~4500 chars (Google limit ~5000)
    if len(text) <= 4500:
        result = GoogleTranslator(source="en", target=target_lang).translate(text)
        return result or text

    chunks = []
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunk = ""
    for s in sentences:
        if len(chunk) + len(s) > 4500:
            chunks.append(chunk)
            chunk = s
        else:
            chunk += " " + s
    if chunk:
        chunks.append(chunk)

    translated = []
    for c in chunks:
        t = GoogleTranslator(source="en", target=target_lang).translate(c)
        translated.append(t or c)
        time.sleep(0.2)
    return " ".join(translated)


def translate_article(src_path: Path, dst_path: Path) -> bool:
    """Translate a single article from EN to ZH."""
    content = src_path.read_text("utf-8")
    fm, body = parse_frontmatter(content)

    if not body.strip():
        return False

    try:
        translated_body = translate_text(body)

        # Build Chinese frontmatter
        fm["language"] = "zh"
        fm["translated_from"] = fm.get("id", "")
        fm["title"] = translate_text(fm.get("title", ""))
        frontmatter = build_frontmatter(fm)

        dst_path.parent.mkdir(parents=True, exist_ok=True)
        dst_path.write_text(frontmatter + translated_body, "utf-8")
        return True
    except Exception as e:
        print(f"  TRANSLATE ERROR: {e}")
        return False


def cmd_translate(max_workers: int = 3):
    """Translate all English articles to Chinese."""
    logger = SyncLogger("Translate")
    crawl_meta = load_json(CRAWL_META)
    translate_meta = load_json(TRANSLATE_META)

    articles = crawl_meta.get("articles", {})
    translated = translate_meta.get("translated", {})

    # Find untranslated articles
    to_translate = []
    for aid, info in articles.items():
        if aid in translated:
            logger.skip(f"{info['title'][:50]}")
            continue
        src = KLAVIYO_DIR / info["filename"]
        if not src.exists():
            continue
        dst = BATTERDOCS_DIR / info["category_slug"] / src.name
        to_translate.append((aid, info, src, dst))

    print(f"[3/4] {len(to_translate)} articles to translate")

    for aid, info, src, dst in to_translate:
        ok = translate_article(src, dst)
        if ok:
            translated[aid] = {
                "title": info["title"],
                "filename": f"{info['category_slug']}/{src.name}",
                "translated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            logger.ok(f"[{info['category_slug']}] {info['title'][:50]}")

            if logger.results["success"] % 20 == 0:
                save_json(TRANSLATE_META, {"translated": translated})
        else:
            logger.fail(f"{info['title'][:50]}")

        time.sleep(0.3)

    save_json(TRANSLATE_META, {"translated": translated})
    logger.summary()
    return logger.results


# ============================================================
# Step 4: Push Chinese to WP (streaming)
# ============================================================

def cmd_push_zh():
    """Push translated Chinese articles to WordPress."""
    logger = SyncLogger("Push ZH")
    crawl_meta = load_json(CRAWL_META)
    translate_meta = load_json(TRANSLATE_META)
    push_zh_meta = load_json(PUSH_ZH_META)

    wp = WordPressClient()
    articles = crawl_meta.get("articles", {})
    translated = translate_meta.get("translated", {})
    pushed_zh = push_zh_meta.get("pushed", {})

    print(f"[4/4] {len(translated)} translated, {len(pushed_zh)} already pushed ZH")

    for aid, info in translated.items():
        if aid in pushed_zh:
            logger.skip(f"{info['title'][:50]}")
            continue

        filepath = BATTERDOCS_DIR / info["filename"]
        if not filepath.exists():
            logger.fail(f"File missing: {info['filename']}")
            continue

        content = filepath.read_text("utf-8")
        fm, body = parse_frontmatter(content)
        title = fm.get("title", info["title"])

        try:
            result = wp.create_doc(
                title=title,
                content=body,
                category_slug=info.get("category_slug", crawl_meta["articles"].get(aid, {}).get("category_slug", "")),
            )
            pushed_zh[aid] = {
                "wp_id": result["id"],
                "title": title,
                "filename": info["filename"],
                "pushed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            logger.ok(f"{title[:50]} → WP #{result['id']}")

            if logger.results["success"] % 50 == 0:
                save_json(PUSH_ZH_META, {"pushed": pushed_zh})

        except Exception as e:
            logger.fail(f"{title[:50]}: {e}")
            save_json(PUSH_ZH_META, {"pushed": pushed_zh})
            continue

        time.sleep(0.5)

    save_json(PUSH_ZH_META, {"pushed": pushed_zh})
    logger.summary()
    return logger.results


# ============================================================
# Status
# ============================================================

def cmd_status():
    """Show comprehensive sync status."""
    crawl_meta = load_json(CRAWL_META)
    push_en_meta = load_json(PUSH_EN_META)
    translate_meta = load_json(TRANSLATE_META)
    push_zh_meta = load_json(PUSH_ZH_META)

    crawled = len(crawl_meta.get("articles", {}))
    pushed_en = len(push_en_meta.get("pushed", {}))
    translated_count = len(translate_meta.get("translated", {}))
    pushed_zh = len(push_zh_meta.get("pushed", {}))

    # Remote count
    try:
        wp = WordPressClient()
        docs, _ = wp.get_docs(page=1, per_page=1)
        # Get total from first page
        all_docs = wp.get_all_docs()
        remote_total = len(all_docs)
        remote_cats = {}
        for d in all_docs:
            for cid in d.get("doc_category", []):
                remote_cats[cid] = remote_cats.get(cid, 0) + 1
    except Exception:
        remote_total = "?"
        remote_cats = {}

    print()
    print("╔══════════════════════════════════════════════════╗")
    print("║        Klaviyo Docs Sync Status                 ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║  [1] Crawled (EN local):  {crawled:>5} articles       ║")
    print(f"║  [2] Pushed EN to WP:     {pushed_en:>5} articles       ║")
    print(f"║  [3] Translated EN→ZH:    {translated_count:>5} articles       ║")
    print(f"║  [4] Pushed ZH to WP:     {pushed_zh:>5} articles       ║")
    print(f"║  Remote total:            {remote_total:>5} articles       ║")
    print("╠══════════════════════════════════════════════════╣")

    if crawled > 0:
        pct_en = pushed_en / crawled * 100
        pct_tr = translated_count / crawled * 100
        pct_zh = pushed_zh / crawled * 100
        bar_en = "█" * int(pct_en // 5) + "░" * (20 - int(pct_en // 5))
        bar_tr = "█" * int(pct_tr // 5) + "░" * (20 - int(pct_tr // 5))
        bar_zh = "█" * int(pct_zh // 5) + "░" * (20 - int(pct_zh // 5))
        print(f"║  EN push:  [{bar_en}] {pct_en:>3.0f}%  ║")
        print(f"║  Translate:[{bar_tr}] {pct_tr:>3.0f}%  ║")
        print(f"║  ZH push:  [{bar_zh}] {pct_zh:>3.0f}%  ║")

    print("╚══════════════════════════════════════════════════╝")
    print()


# ============================================================
# Full Pipeline
# ============================================================

def cmd_full():
    """Run the complete pipeline."""
    print("=" * 50)
    print("  Klaviyo Docs Full Sync Pipeline")
    print("=" * 50)
    print()

    print(">>> Step 1: Crawl from Klaviyo")
    cmd_crawl()
    print()

    print(">>> Step 2: Push English to WordPress")
    cmd_push_en()
    print()

    print(">>> Step 3: Translate EN → ZH")
    cmd_translate()
    print()

    print(">>> Step 4: Push Chinese to WordPress")
    cmd_push_zh()
    print()

    print(">>> Final Status")
    cmd_status()


# ============================================================
# Main
# ============================================================

COMMANDS = {
    "crawl": cmd_crawl,
    "push-en": cmd_push_en,
    "translate": cmd_translate,
    "push-zh": cmd_push_zh,
    "full": cmd_full,
    "status": cmd_status,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(COMMANDS.keys())}")
        sys.exit(1)

    COMMANDS[cmd]()
