#!/usr/bin/env python3
"""Klaviyo Docs Sync Pipeline v2.

Architecture:
  klaviyo-en/   ← English source (crawled from Klaviyo, local backup only)
  klaviyo-cn/   ← Chinese translations (translated from EN)
  WordPress     ← Only Chinese HTML content gets uploaded

Pipeline:
  crawl     → Fetch from Klaviyo → save EN markdown to klaviyo-en/
  translate → Read EN → translate → save ZH to klaviyo-cn/
  upload    → Read ZH markdown → convert to HTML → upload to WP
  status    → Show sync progress

Usage:
    python3 pipeline.py crawl
    python3 pipeline.py translate
    python3 pipeline.py upload
    python3 pipeline.py full
    python3 pipeline.py status
"""

import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from core import (
    KLAVIYO_EN_DIR, KLAVIYO_CN_DIR, PROJECT_ROOT,
    KLAVIYO_CATEGORY_MAP, KLAVIYO_CATEGORY_NAMES,
    load_category_map,
    ZendeskClient, WordPressClient,
    html_to_markdown, sanitize_filename, parse_frontmatter, build_frontmatter,
    load_json, save_json, SyncLogger,
)

CRAWL_META = KLAVIYO_EN_DIR / ".crawl_meta.json"
TRANSLATE_META = KLAVIYO_CN_DIR / ".translate_meta.json"
UPLOAD_META = KLAVIYO_CN_DIR / ".upload_meta.json"


# ============================================================
# Step 1: Crawl (EN → local only)
# ============================================================

def cmd_crawl():
    """Crawl all articles from Klaviyo Help Center → klaviyo-en/."""
    logger = SyncLogger("Crawl EN")
    KLAVIYO_EN_DIR.mkdir(parents=True, exist_ok=True)

    print("[1/3] Fetching sections...")
    zendesk = ZendeskClient()
    sections = zendesk.get_sections()

    print("[1/3] Fetching articles...")
    articles = zendesk.get_all_articles()
    print(f"  Found {len(articles)} articles")

    meta = load_json(CRAWL_META)
    if "articles" not in meta:
        meta["articles"] = {}

    print("[1/3] Saving to klaviyo-en/...")
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

        cat_dir = KLAVIYO_EN_DIR / cat_slug
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

        (cat_dir / filename).write_text(frontmatter + md_content, "utf-8")

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


# ============================================================
# Step 2: Translate (EN → ZH, local only)
# ============================================================

def translate_text(text: str, target_lang: str = "zh-CN") -> str:
    from deep_translator import GoogleTranslator

    if len(text) <= 4500:
        return GoogleTranslator(source="en", target=target_lang).translate(text) or text

    chunks, chunk = [], ""
    for s in re.split(r'(?<=[.!?])\s+', text):
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


def cmd_translate():
    """Translate EN articles to ZH → klaviyo-cn/."""
    logger = SyncLogger("Translate EN→ZH")
    KLAVIYO_CN_DIR.mkdir(parents=True, exist_ok=True)

    crawl_meta = load_json(CRAWL_META)
    translate_meta = load_json(TRANSLATE_META)
    articles = crawl_meta.get("articles", {})
    translated = translate_meta.get("translated", {})

    to_translate = [
        (aid, info) for aid, info in articles.items()
        if aid not in translated
    ]
    print(f"[2/3] {len(to_translate)} articles to translate")

    for aid, info in to_translate:
        src = KLAVIYO_EN_DIR / info["filename"]
        if not src.exists():
            logger.fail(f"Missing: {info['filename']}")
            continue

        content = src.read_text("utf-8")
        fm, body = parse_frontmatter(content)
        if not body.strip():
            logger.skip(f"Empty: {info['title'][:50]}")
            continue

        try:
            zh_title = translate_text(info["title"])
            zh_body = translate_text(body)

            fm["language"] = "zh"
            fm["title"] = zh_title.replace('"', '\\"')

            cat_slug = info["category_slug"]
            dst_dir = KLAVIYO_CN_DIR / cat_slug
            dst_dir.mkdir(parents=True, exist_ok=True)
            dst = dst_dir / src.name

            dst.write_text(build_frontmatter(fm) + zh_body, "utf-8")

            translated[aid] = {
                "title": zh_title,
                "en_title": info["title"],
                "filename": f"{cat_slug}/{src.name}",
                "category_slug": cat_slug,
                "translated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            logger.ok(f"[{cat_slug}] {info['title'][:40]} → {zh_title[:30]}")

            if logger.results["success"] % 20 == 0:
                save_json(TRANSLATE_META, {"translated": translated})
        except Exception as e:
            logger.fail(f"{info['title'][:40]}: {e}")
            save_json(TRANSLATE_META, {"translated": translated})

        time.sleep(0.3)

    save_json(TRANSLATE_META, {"translated": translated})
    logger.summary()


# ============================================================
# Step 3: Upload ZH (to WordPress BetterDocs as HTML)
# ============================================================

def markdown_to_html(md: str) -> str:
    """Convert markdown to clean HTML for WordPress/BetterDocs."""
    lines = md.split("\n")
    html_parts = []
    in_list = False

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            continue

        # Headings
        if stripped.startswith("#### "):
            html_parts.append(f"<h4>{stripped[5:]}</h4>")
        elif stripped.startswith("### "):
            html_parts.append(f"<h3>{stripped[4:]}</h3>")
        elif stripped.startswith("## "):
            html_parts.append(f"<h2>{stripped[3:]}</h2>")
        elif stripped.startswith("# "):
            html_parts.append(f"<h1>{stripped[2:]}</h1>")

        # Images
        elif stripped.startswith("!["):
            m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', stripped)
            if m:
                html_parts.append(f'<img src="{m.group(2)}" alt="{m.group(1)}" />')

        # List items
        elif stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            html_parts.append(f"<li>{stripped[2:]}</li>")

        # Links
        elif stripped.startswith("[") and "](" in stripped:
            m = re.match(r'\[([^\]]+)\]\(([^)]+)\)', stripped)
            if m:
                html_parts.append(f'<p><a href="{m.group(2)}">{m.group(1)}</a></p>')
            else:
                html_parts.append(f"<p>{stripped}</p>")

        # Regular text
        else:
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            # Handle bold/italic
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', stripped)
            text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
            html_parts.append(f"<p>{text}</p>")

    if in_list:
        html_parts.append("</ul>")

    return "\n".join(html_parts)


def cmd_upload():
    """Upload translated ZH articles to WP BetterDocs as HTML."""
    logger = SyncLogger("Upload ZH")
    wp = WordPressClient()

    translate_meta = load_json(TRANSLATE_META)
    upload_meta = load_json(UPLOAD_META)
    translated = translate_meta.get("translated", {})
    uploaded = upload_meta.get("uploaded", {})

    to_upload = [
        (aid, info) for aid, info in translated.items()
        if aid not in uploaded
    ]
    print(f"[3/3] {len(to_upload)} articles to upload")

    cat_map = load_category_map()

    for aid, info in to_upload:
        filepath = KLAVIYO_CN_DIR / info["filename"]
        if not filepath.exists():
            logger.fail(f"Missing: {info['filename']}")
            continue

        content = filepath.read_text("utf-8")
        fm, body = parse_frontmatter(content)
        title = fm.get("title", info["title"])
        cat_slug = info.get("category_slug", "")
        cat_id = cat_map.get(cat_slug)

        if not cat_id:
            logger.fail(f"No WP category for '{cat_slug}': {title[:40]}")
            continue

        # Convert markdown body to HTML
        html_content = markdown_to_html(body)

        try:
            result = wp.create_doc(title=title, content=html_content, category_slug=cat_slug)
            if result:
                uploaded[aid] = {
                    "wp_id": result["id"],
                    "title": title,
                    "filename": info["filename"],
                    "category_slug": cat_slug,
                    "uploaded_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                }
                logger.ok(f"[{cat_slug}] {title[:50]} → WP #{result['id']}")

                if logger.results["success"] % 50 == 0:
                    save_json(UPLOAD_META, {"uploaded": uploaded})
        except Exception as e:
            logger.fail(f"{title[:40]}: {e}")
            save_json(UPLOAD_META, {"uploaded": uploaded})

        time.sleep(0.5)

    save_json(UPLOAD_META, {"uploaded": uploaded})
    logger.summary()


# ============================================================
# Status
# ============================================================

def cmd_status():
    """Show sync progress."""
    crawl_meta = load_json(CRAWL_META)
    translate_meta = load_json(TRANSLATE_META)
    upload_meta = load_json(UPLOAD_META)

    crawled = len(crawl_meta.get("articles", {}))
    translated_count = len(translate_meta.get("translated", {}))
    uploaded_count = len(upload_meta.get("uploaded", {}))

    # Remote count
    try:
        wp = WordPressClient()
        all_docs = wp.get_all_docs()
        remote_total = len(all_docs)
    except Exception:
        remote_total = "?"

    bar = lambda pct: "█" * int(pct // 5) + "░" * (20 - int(pct // 5))

    pct_tr = (translated_count / crawled * 100) if crawled else 0
    pct_up = (uploaded_count / crawled * 100) if crawled else 0

    print()
    print("╔════════════════════════════════════════════════╗")
    print("║     Klaviyo Docs Sync Status v2               ║")
    print("╠════════════════════════════════════════════════╣")
    print(f"║  [1] Crawled (klaviyo-en/): {crawled:>5} articles   ║")
    print(f"║  [2] Translated (klaviyo-cn/): {translated_count:>4} articles   ║")
    print(f"║  [3] Uploaded ZH to WP:  {uploaded_count:>5} articles   ║")
    print(f"║  Remote total:           {remote_total:>5} articles   ║")
    print("╠════════════════════════════════════════════════╣")
    print(f"║  Translate:[{bar(pct_tr)}] {pct_tr:>5.1f}%          ║")
    print(f"║  Upload:   [{bar(pct_up)}] {pct_up:>5.1f}%          ║")
    print("╚════════════════════════════════════════════════╝")
    print()


# ============================================================
# Full pipeline
# ============================================================

def cmd_full():
    print("=" * 50)
    print("  Klaviyo Docs Sync Pipeline v2")
    print("  EN: crawl only | ZH: translate + upload")
    print("=" * 50)

    print("\n>>> Step 1: Crawl EN (local only)")
    cmd_crawl()

    print("\n>>> Step 2: Translate EN → ZH (local)")
    cmd_translate()

    print("\n>>> Step 3: Upload ZH to WordPress (HTML)")
    cmd_upload()

    print("\n>>> Final Status")
    cmd_status()


COMMANDS = {
    "crawl": cmd_crawl,
    "translate": cmd_translate,
    "upload": cmd_upload,
    "full": cmd_full,
    "status": cmd_status,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd not in COMMANDS:
        print(f"Unknown: {cmd}. Available: {', '.join(COMMANDS.keys())}")
        sys.exit(1)

    COMMANDS[cmd]()
