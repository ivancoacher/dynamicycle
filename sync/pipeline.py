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
    python3 pipeline.py crawl-article https://help.klaviyo.com/hc/en-us/articles/115005085427
    python3 pipeline.py translate
    python3 pipeline.py upload
    python3 pipeline.py full
    python3 pipeline.py status
"""

import json
import os
import re
import signal
import sys
import time
import csv
import html
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup, NavigableString

sys.path.insert(0, str(Path(__file__).resolve().parent))

from core import (
    KLAVIYO_EN_DIR, KLAVIYO_CN_DIR, PROJECT_ROOT,
    WP_SITE_URL, WP_PARENT_CAT,
    KLAVIYO_CATEGORY_MAP, KLAVIYO_CATEGORY_NAMES,
    load_category_map, save_category_map,
    ZendeskClient, WordPressClient,
    html_to_markdown, sanitize_filename, parse_frontmatter, build_frontmatter,
    load_json, save_json, SyncLogger, with_retry,
)
from structure import article_to_html, slugify, escape_attr

CRAWL_META = KLAVIYO_EN_DIR / ".crawl_meta.json"
TRANSLATE_META = KLAVIYO_CN_DIR / ".translate_meta.json"
UPLOAD_META = KLAVIYO_CN_DIR / ".upload_meta.json"
SOURCE_DIR = KLAVIYO_EN_DIR / "_source"
SOURCE_ARTICLES_DIR = SOURCE_DIR / "articles"
SOURCE_RENDERED_DIR = SOURCE_DIR / "rendered"
SOURCE_CATEGORY_PAGES_DIR = SOURCE_DIR / "category-pages"
SOURCE_INDEX = SOURCE_DIR / "source_index.json"
SOURCE_REPORT = SOURCE_DIR / "last_crawl_report.json"
RELATIONS_DIR = SOURCE_DIR / "relations"
CATEGORY_PREVIEW_META = SOURCE_DIR / "category_preview_uploads.json"
SECTION_PREVIEW_META = SOURCE_DIR / "section_preview_uploads.json"
HOMEPAGE_MENU_DIR = SOURCE_DIR / "homepage-menu"
HOMEPAGE_CATEGORY_MENU = HOMEPAGE_MENU_DIR / "category-menu.json"
HOMEPAGE_CATEGORY_MENU_CSV = HOMEPAGE_MENU_DIR / "category-menu.csv"
HOMEPAGE_CATEGORY_UPLOAD_META = HOMEPAGE_MENU_DIR / "category-doc-uploads.json"
URL_MAP_DIR = SOURCE_DIR / "url-map"
CATEGORY_URL_MAP = URL_MAP_DIR / "category-url-map.json"
SECTION_URL_MAP = URL_MAP_DIR / "section-url-map.json"
ARTICLE_URL_MAP = URL_MAP_DIR / "article-url-map.json"
SOURCE_TO_LOCAL_URL_MAP = URL_MAP_DIR / "source-to-local-url-map.json"
UNRESOLVED_LINKS_REPORT = URL_MAP_DIR / "unresolved-links-report.json"
REDIRECT_URL_MAP = URL_MAP_DIR / "redirect-url-map.json"
MANUAL_URL_ALIASES = URL_MAP_DIR / "manual-url-aliases.json"

MENU_CATEGORY_ZH = {
    "featured-resources": "精选资源",
    "account-billing": "账户与计费",
    "advanced-kdp-marketing-analytics": "高级 KDP 与营销分析",
    "analytics": "分析",
    "audience": "受众",
    "campaigns": "营销活动",
    "content": "内容",
    "conversations": "会话",
    "customer-agent": "客户 Agent",
    "customer-hub": "客户中心",
    "deliverability-compliance": "投递与合规",
    "flows": "自动化流程",
    "helpdesk": "帮助台",
    "integrations": "集成",
    "push-notifications": "推送通知",
    "reviews": "评论",
    "sign-up-forms": "注册表单",
    "sms": "短信",
    "social-marketing": "社交营销",
    "whatsapp": "WhatsApp",
}

LEGACY_CATEGORY_SLUG_REUSE = {
    "analytics": "klaviyo-analytics-audience",
    "sms": "klaviyo-sms-whatsapp",
}


# ============================================================
# Step 1: Crawl (EN → local only)
# ============================================================

def article_id_from_arg(value: str) -> str:
    match = re.search(r"/articles/(\d+)", value) or re.search(r"^\s*(\d+)\s*$", value)
    if not match:
        raise ValueError(f"Cannot find Klaviyo article id in: {value}")
    return match.group(1)


def canonical_help_url(url: str) -> str:
    return url.replace("https://klaviyo.zendesk.com", "https://help.klaviyo.com")


def article_markdown_filename(title: str, article_id: str) -> str:
    return f"{sanitize_filename(title)}-{article_id}.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def extract_html_assets(html: str, base_url: str) -> dict:
    """Capture source structure needed for later styling without re-fetching Klaviyo."""
    soup = BeautifulSoup(html or "", "html.parser")

    def clean_text(value: str, limit: int = 240) -> str:
        return re.sub(r"\s+", " ", value or "").strip()[:limit]

    images, image_seen = [], set()
    for img in soup.find_all("img"):
        src = (img.get("src") or "").strip()
        if not src:
            continue
        src = urljoin(base_url, src)
        if src in image_seen:
            continue
        image_seen.add(src)
        images.append({
            "src": src,
            "alt": img.get("alt", ""),
            "width": img.get("width", ""),
            "height": img.get("height", ""),
        })

    links, link_seen = [], set()
    for a in soup.find_all("a"):
        href = (a.get("href") or "").strip()
        if not href:
            continue
        href = urljoin(base_url, href)
        key = (href, clean_text(a.get_text(" ", strip=True)))
        if key in link_seen:
            continue
        link_seen.add(key)
        links.append({"href": href, "text": key[1]})

    headings = []
    for tag in soup.find_all(re.compile(r"^h[1-6]$")):
        headings.append({
            "level": int(tag.name[1]),
            "id": tag.get("id", ""),
            "text": clean_text(tag.get_text(" ", strip=True)),
        })

    return {
        "images": images,
        "links": links,
        "headings": headings,
    }


def fetch_rendered_article_page(url: str) -> str:
    url = canonical_help_url(url)

    def _do():
        resp = requests.get(
            url,
            headers={"User-Agent": "DynamicycleDocsSync/1.0 (+https://dynamicycle.com)"},
            timeout=45,
        )
        resp.raise_for_status()
        return resp.text

    return with_retry(_do, description=f"GET rendered article {url}")


def source_file_paths(article_id: str) -> dict:
    return {
        "snapshot": SOURCE_ARTICLES_DIR / f"{article_id}.json",
        "body_html": SOURCE_ARTICLES_DIR / f"{article_id}.body.html",
        "rendered_html": SOURCE_RENDERED_DIR / f"{article_id}.html",
    }


def save_source_snapshot(
    article: dict,
    sections: dict,
    categories: dict,
    *,
    fetch_rendered: bool,
    refresh_rendered: bool,
) -> dict:
    article_id = str(article["id"])
    section_id = article.get("section_id")
    section = sections.get(section_id, {})
    category_id = section.get("category_id")
    category = categories.get(category_id, {})
    html_url = canonical_help_url(article.get("html_url", ""))
    body_html = article.get("body", "") or ""

    SOURCE_ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    SOURCE_RENDERED_DIR.mkdir(parents=True, exist_ok=True)
    paths = source_file_paths(article_id)

    paths["body_html"].write_text(body_html, "utf-8")
    api_assets = extract_html_assets(body_html, html_url)

    rendered_status = "not_requested"
    rendered_error = ""
    rendered_assets = {}
    if fetch_rendered:
        if refresh_rendered or not paths["rendered_html"].exists():
            try:
                rendered_html = fetch_rendered_article_page(html_url)
                paths["rendered_html"].write_text(rendered_html, "utf-8")
                rendered_assets = extract_html_assets(rendered_html, html_url)
                rendered_status = "fetched"
            except Exception as exc:
                rendered_status = "failed"
                rendered_error = str(exc)
        else:
            rendered_status = "cached"
            rendered_html = paths["rendered_html"].read_text("utf-8")
            rendered_assets = extract_html_assets(rendered_html, html_url)

    snapshot = {
        "captured_at": utc_now(),
        "article": article,
        "normalized": {
            "id": article_id,
            "title": article.get("title", article.get("name", "Untitled")),
            "source_url": html_url,
            "section_id": section_id,
            "section": section.get("name", ""),
            "category_id": category_id,
            "category": category.get("name") or KLAVIYO_CATEGORY_NAMES.get(category_id, "Uncategorized"),
            "category_slug": KLAVIYO_CATEGORY_MAP.get(category_id, "uncategorized"),
            "klaviyo_updated": article.get("updated_at", ""),
            "created_at": article.get("created_at", ""),
            "draft": article.get("draft", False),
            "promoted": article.get("promoted", False),
            "position": article.get("position", 0),
            "label_names": article.get("label_names", []),
        },
        "files": {
            "body_html": str(paths["body_html"].relative_to(KLAVIYO_EN_DIR)),
            "rendered_html": str(paths["rendered_html"].relative_to(KLAVIYO_EN_DIR)) if paths["rendered_html"].exists() else "",
        },
        "assets": {
            "api_body": api_assets,
            "rendered_page": rendered_assets,
        },
        "rendered_page": {
            "status": rendered_status,
            "error": rendered_error,
        },
    }
    save_json(paths["snapshot"], snapshot)
    return {
        "snapshot": str(paths["snapshot"].relative_to(KLAVIYO_EN_DIR)),
        "body_html": str(paths["body_html"].relative_to(KLAVIYO_EN_DIR)),
        "rendered_html": str(paths["rendered_html"].relative_to(KLAVIYO_EN_DIR)) if paths["rendered_html"].exists() else "",
        "rendered_status": rendered_status,
        "rendered_error": rendered_error,
    }


def save_crawled_article(article: dict, sections: dict, meta: dict, logger: SyncLogger, *, write_markdown: bool = True, snapshot_files: dict | None = None) -> None:
    article_id = str(article["id"])
    title = article.get("title", article.get("name", "Untitled"))
    html_body = article.get("body", "") or ""
    html_url = canonical_help_url(article.get("html_url", ""))
    section_id = article.get("section_id")
    updated_at = article.get("updated_at", "")

    sec = sections.get(section_id, {})
    cat_id = sec.get("category_id", 0)
    cat_slug = KLAVIYO_CATEGORY_MAP.get(cat_id, "uncategorized")
    cat_name = KLAVIYO_CATEGORY_NAMES.get(cat_id, "Uncategorized")

    cat_dir = KLAVIYO_EN_DIR / cat_slug
    cat_dir.mkdir(parents=True, exist_ok=True)

    filename = article_markdown_filename(title, article_id)

    if write_markdown:
        md_content = html_to_markdown(html_body)
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
    meta["articles"][article_id] = {
        "title": title,
        "filename": f"{cat_slug}/{filename}",
        "source_url": html_url,
        "category_slug": cat_slug,
        "section_id": section_id,
        "section": sec.get("name", ""),
        "klaviyo_updated": updated_at,
        "status": "new" if not existing else ("updated" if write_markdown else "snapshot"),
    }
    if snapshot_files:
        meta["articles"][article_id]["source_snapshot"] = snapshot_files.get("snapshot", "")
        meta["articles"][article_id]["body_html"] = snapshot_files.get("body_html", "")
        meta["articles"][article_id]["rendered_html"] = snapshot_files.get("rendered_html", "")
    logger.ok(f"[{cat_slug}] {title[:50]}")


def save_source_index(categories: dict, sections: dict, articles_meta: dict, report: dict) -> None:
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    index = {
        "captured_at": utc_now(),
        "source_root": "https://help.klaviyo.com/hc/en-us",
        "counts": {
            "categories": len(categories),
            "sections": len(sections),
            "articles": len(articles_meta),
        },
        "categories": {str(k): v for k, v in categories.items()},
        "sections": {str(k): v for k, v in sections.items()},
        "articles": articles_meta,
        "last_report": report,
    }
    save_json(SOURCE_INDEX, index)
    save_json(SOURCE_REPORT, report)


def cmd_crawl():
    """Crawl all articles from Klaviyo Help Center → klaviyo-en/ and _source/."""
    logger = SyncLogger("Crawl EN")
    KLAVIYO_EN_DIR.mkdir(parents=True, exist_ok=True)

    print("[1/4] Fetching categories...")
    zendesk = ZendeskClient()
    categories = zendesk.get_categories()

    print("[2/4] Fetching sections...")
    sections = zendesk.get_sections()
    categories = {
        k: {**v, "source_url": canonical_help_url(v.get("source_url", ""))}
        for k, v in categories.items()
    }
    sections = {
        k: {**v, "source_url": canonical_help_url(v.get("source_url", ""))}
        for k, v in sections.items()
    }

    print("[3/4] Fetching article index...")
    articles = zendesk.get_all_articles()
    print(f"  Found {len(articles)} articles")

    meta = load_json(CRAWL_META)
    if "articles" not in meta:
        meta["articles"] = {}
    meta["categories"] = {str(k): v for k, v in categories.items()}
    meta["sections"] = {str(k): v for k, v in sections.items()}

    report = {
        "started_at": utc_now(),
        "finished_at": "",
        "mode": "english_source_snapshot",
        "source_root": "https://help.klaviyo.com/hc/en-us",
        "articles_found": len(articles),
        "articles_skipped_draft": 0,
        "markdown_written": 0,
        "source_snapshots_written": 0,
        "rendered_pages_fetched": 0,
        "rendered_pages_cached": 0,
        "unchanged_skipped": 0,
        "failed": 0,
    }

    print("[4/4] Saving changed source files and missing snapshots...")
    jobs = []
    for a in articles:
        if a.get("draft"):
            report["articles_skipped_draft"] += 1
            continue
        article_id = str(a["id"])
        updated_at = a.get("updated_at", "")
        existing = meta["articles"].get(article_id, {})
        paths = source_file_paths(article_id)
        existing_file = existing.get("filename", "")
        md_exists = bool(existing_file) and (KLAVIYO_EN_DIR / existing_file).exists()
        changed = existing.get("klaviyo_updated") != updated_at
        missing_snapshot = not paths["snapshot"].exists()
        missing_rendered = not paths["rendered_html"].exists()

        if changed or not md_exists or missing_snapshot or missing_rendered:
            jobs.append({
                "article": a,
                "article_id": article_id,
                "write_markdown": changed or not md_exists,
                "refresh_rendered": changed or missing_rendered,
            })
        else:
            sec = sections.get(a.get("section_id"), {})
            cat_id = sec.get("category_id", 0)
            cat_slug = KLAVIYO_CATEGORY_MAP.get(cat_id, "uncategorized")
            title = a.get("title", a.get("name", "Untitled"))
            report["unchanged_skipped"] += 1
            logger.skip(f"[{cat_slug}] {title[:50]}")

    print(f"  To process: {len(jobs)} | unchanged: {report['unchanged_skipped']} | drafts: {report['articles_skipped_draft']}")

    def process_job(job: dict) -> dict:
        article = zendesk.get_article(job["article_id"]) or job["article"]
        snapshot_files = save_source_snapshot(
            article,
            sections,
            categories,
            fetch_rendered=True,
            refresh_rendered=job["refresh_rendered"],
        )
        return {
            "article_id": job["article_id"],
            "article": article,
            "snapshot_files": snapshot_files,
            "write_markdown": job["write_markdown"],
        }

    workers = 8
    completed = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(process_job, job) for job in jobs]
        for future in as_completed(futures):
            completed += 1
            try:
                result = future.result()
                article_id = result["article_id"]
                snapshot_files = result["snapshot_files"]
                save_crawled_article(
                    result["article"],
                    sections,
                    meta,
                    logger,
                    write_markdown=result["write_markdown"],
                    snapshot_files=snapshot_files,
                )
                report["source_snapshots_written"] += 1
                if result["write_markdown"]:
                    report["markdown_written"] += 1
                if snapshot_files.get("rendered_status") == "fetched":
                    report["rendered_pages_fetched"] += 1
                elif snapshot_files.get("rendered_status") == "cached":
                    report["rendered_pages_cached"] += 1
                elif snapshot_files.get("rendered_status") == "failed":
                    report["failed"] += 1
                    logger.fail(f"Rendered page failed for {article_id}: {snapshot_files.get('rendered_error', '')[:120]}")
            except Exception as exc:
                report["failed"] += 1
                logger.fail(str(exc))

            if completed % 25 == 0:
                print(f"  Progress: {completed}/{len(jobs)}")
                save_json(CRAWL_META, meta)

    save_json(CRAWL_META, meta)
    report["finished_at"] = utc_now()
    save_source_index(categories, sections, meta.get("articles", {}), report)
    logger.summary()
    print(f"  Source index: {SOURCE_INDEX}")
    print(f"  Crawl report: {SOURCE_REPORT}")


def cmd_crawl_article(source: str):
    """Crawl one Klaviyo article by original URL or numeric id."""
    logger = SyncLogger("Crawl single EN")
    KLAVIYO_EN_DIR.mkdir(parents=True, exist_ok=True)

    article_id = article_id_from_arg(source)
    zendesk = ZendeskClient()

    print("[1/1] Fetching sections...")
    categories = zendesk.get_categories()
    sections = zendesk.get_sections()
    categories = {
        k: {**v, "source_url": canonical_help_url(v.get("source_url", ""))}
        for k, v in categories.items()
    }
    sections = {
        k: {**v, "source_url": canonical_help_url(v.get("source_url", ""))}
        for k, v in sections.items()
    }

    print(f"[1/1] Fetching article {article_id}...")
    article = zendesk.get_article(article_id)
    if not article:
        raise RuntimeError(f"Article not found: {article_id}")

    meta = load_json(CRAWL_META)
    meta.setdefault("articles", {})
    meta["categories"] = {str(k): v for k, v in categories.items()}
    meta["sections"] = {str(k): v for k, v in sections.items()}

    snapshot_files = save_source_snapshot(
        article,
        sections,
        categories,
        fetch_rendered=True,
        refresh_rendered=True,
    )
    save_crawled_article(article, sections, meta, logger, snapshot_files=snapshot_files)
    save_json(CRAWL_META, meta)
    save_source_index(categories, sections, meta.get("articles", {}), {
        "started_at": utc_now(),
        "finished_at": utc_now(),
        "mode": "single_english_source_snapshot",
        "source_root": "https://help.klaviyo.com/hc/en-us",
        "article_id": article_id,
        "rendered_status": snapshot_files.get("rendered_status", ""),
    })
    logger.summary()


# ============================================================
# Step 2: Translate (EN → ZH, local only)
# ============================================================

TRANSLATION_PROVIDER = (os.getenv("TRANSLATION_PROVIDER") or "google").strip().lower()
OPENAI_TRANSLATION_MODEL = os.getenv("OPENAI_TRANSLATION_MODEL") or os.getenv("OPENAI_MODEL") or "gpt-5-mini"
GOOGLE_TRANSLATE_TIMEOUT = int(os.getenv("GOOGLE_TRANSLATE_TIMEOUT", "20"))


def openai_response_create(payload: dict) -> dict:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set. Add it to .env before running ChatGPT translation.")
    resp = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()


def openai_response_text(response) -> str:
    if isinstance(response, dict):
        text = response.get("output_text")
        if text:
            return text.strip()
        chunks = []
        for item in response.get("output", []) or []:
            for content in item.get("content", []) or []:
                value = content.get("text")
                if value:
                    chunks.append(value)
        return "\n".join(chunks).strip()

    text = getattr(response, "output_text", None)
    if text:
        return text.strip()
    chunks = []
    for item in getattr(response, "output", []) or []:
        for content in getattr(item, "content", []) or []:
            value = getattr(content, "text", None)
            if value:
                chunks.append(value)
    return "\n".join(chunks).strip()


def split_for_translation(text: str, max_chars: int = 4200) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    chunks = []
    remaining = text
    while remaining:
        if len(remaining) <= max_chars:
            chunks.append(remaining)
            break
        cut = max(
            remaining.rfind("\n", 0, max_chars),
            remaining.rfind(". ", 0, max_chars),
            remaining.rfind("; ", 0, max_chars),
            remaining.rfind(", ", 0, max_chars),
            remaining.rfind(" ", 0, max_chars),
        )
        if cut < max_chars // 2:
            cut = max_chars
        chunks.append(remaining[:cut].strip())
        remaining = remaining[cut:].strip()
    return [chunk for chunk in chunks if chunk]


def google_translate_chunk(text: str, target_lang: str = "zh-CN") -> str:
    resp = requests.get(
        "https://translate.googleapis.com/translate_a/single",
        params={
            "client": "gtx",
            "sl": "auto",
            "tl": target_lang,
            "dt": "t",
            "q": text,
        },
        timeout=GOOGLE_TRANSLATE_TIMEOUT,
    )
    resp.raise_for_status()
    data = resp.json()
    return "".join(part[0] for part in data[0] if part and part[0])


def google_translate_text(text: str, target_lang: str = "zh-CN") -> str:
    if not text or not text.strip():
        return text
    translated = []
    for chunk in split_for_translation(text):
        translated.append(google_translate_chunk(chunk, target_lang=target_lang))
        time.sleep(0.05)
    return "".join(translated) or text


def google_translate_text_items(items: list[str], target_lang: str = "zh-CN") -> list[str]:
    if not items:
        return []
    translated = []
    for value in items:
        if not value or not value.strip():
            translated.append(value)
            continue
        try:
            translated.append(google_translate_text(value, target_lang=target_lang))
        except Exception:
            translated.append(value)
        time.sleep(0.05)
    return translated


def openai_translate_text(text: str, target_lang: str = "zh-CN") -> str:
    if not text or not text.strip():
        return text
    response = openai_response_create({
        "model": OPENAI_TRANSLATION_MODEL,
        "input": [
            {
                "role": "system",
                "content": (
                    "You are a professional localization translator for Klaviyo help-center documentation. "
                    "Translate English into Simplified Chinese. Preserve product names, URLs, markdown syntax, "
                    "HTML entities, placeholders, inline code, and variable names. Keep the meaning precise, "
                    "natural, and concise for Chinese SaaS documentation. Return only the translation."
                ),
            },
            {
                "role": "user",
                "content": f"Target language: {target_lang}\n\n{text}",
            },
        ],
    })
    return openai_response_text(response) or text


def openai_translate_text_items(items: list[str], target_lang: str = "zh-CN") -> list[str]:
    if not items:
        return []
    payload = [{"id": i, "text": value} for i, value in enumerate(items)]
    response = openai_response_create({
        "model": OPENAI_TRANSLATION_MODEL,
        "input": [
            {
                "role": "system",
                "content": (
                    "You are a professional localization translator for Klaviyo help-center documentation. "
                    "Translate English into Simplified Chinese. Preserve product names, URLs, placeholders, "
                    "inline code, variables, numbers, and markup-sensitive punctuation. "
                    "Return strict JSON only: an array of objects with id and text, preserving every id."
                ),
            },
            {
                "role": "user",
                "content": json.dumps(
                    {"target_language": target_lang, "items": payload},
                    ensure_ascii=False,
                ),
            },
        ],
    })
    raw = openai_response_text(response)
    try:
        if raw.startswith("```"):
            raw = re.sub(r"^```(?:json)?\s*", "", raw).strip()
            raw = re.sub(r"\s*```$", "", raw).strip()
        parsed = json.loads(raw)
        by_id = {int(item["id"]): item.get("text", "") for item in parsed}
        return [by_id.get(i, items[i]) or items[i] for i in range(len(items))]
    except Exception:
        return [translate_text(value, target_lang=target_lang) for value in items]


def translate_text(text: str, target_lang: str = "zh-CN") -> str:
    if TRANSLATION_PROVIDER == "openai":
        return openai_translate_text(text, target_lang=target_lang)
    return google_translate_text(text, target_lang=target_lang)


def translate_text_items(items: list[str], target_lang: str = "zh-CN") -> list[str]:
    if TRANSLATION_PROVIDER == "openai":
        return openai_translate_text_items(items, target_lang=target_lang)
    return google_translate_text_items(items, target_lang=target_lang)


def translate_html_visible_text(html_content: str, target_lang: str = "zh-CN") -> str:
    """Translate visible HTML text while preserving attributes, links, images, IDs, and classes."""
    soup = BeautifulSoup(html_content or "", "html.parser")
    skip_parents = {"script", "style", "code", "pre", "svg", "noscript"}
    text_nodes = []
    for node in soup.find_all(string=True):
        if not isinstance(node, NavigableString):
            continue
        if node.parent and node.parent.name in skip_parents:
            continue
        text = str(node)
        if not text or not text.strip():
            continue
        if re.fullmatch(r"[\W_]+", text.strip()):
            continue
        original = str(node)
        leading = original[:len(original) - len(original.lstrip())]
        trailing = original[len(original.rstrip()):]
        core = original.strip()
        text_nodes.append((node, leading, core, trailing))

    batch_size = 24
    for i in range(0, len(text_nodes), batch_size):
        batch = text_nodes[i:i + batch_size]
        try:
            translated = translate_text_items([item[2] for item in batch], target_lang=target_lang)
            for (node, leading, _core, trailing), value in zip(batch, translated):
                node.replace_with(NavigableString(f"{leading}{value}{trailing}"))
        except Exception:
            for node, _leading, _core, _trailing in batch:
                node.replace_with(node)
        time.sleep(0.1)
    return str(soup)


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

    class TranslationTimeout(Exception):
        pass

    def _timeout_handler(signum, frame):
        raise TranslationTimeout("translation timed out")

    previous_handler = signal.signal(signal.SIGALRM, _timeout_handler)

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
            signal.alarm(180)
            zh_title = translate_text(info["title"])
            body_html_rel = info.get("body_html", "")
            body_html_path = KLAVIYO_EN_DIR / body_html_rel if body_html_rel else None
            if body_html_path and body_html_path.exists():
                zh_body = translate_html_visible_text(body_html_path.read_text("utf-8"))
            else:
                zh_body = translate_text(body)

            fm["language"] = "zh"
            fm["title"] = zh_title.replace('"', '\\"')
            fm["translation_strategy"] = f"{TRANSLATION_PROVIDER}_html_text_nodes_preserve_attributes"

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
                "translation_provider": TRANSLATION_PROVIDER,
                "translated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            logger.ok(f"[{cat_slug}] {info['title'][:40]} → {zh_title[:30]}")
            save_json(TRANSLATE_META, {"translated": translated})
        except TranslationTimeout as e:
            logger.fail(f"{info['title'][:40]}: {e}")
            save_json(TRANSLATE_META, {"translated": translated})
        except Exception as e:
            logger.fail(f"{info['title'][:40]}: {e}")
            save_json(TRANSLATE_META, {"translated": translated})
        finally:
            signal.alarm(0)

        time.sleep(0.3)

    signal.signal(signal.SIGALRM, previous_handler)
    save_json(TRANSLATE_META, {"translated": translated})
    logger.summary()


# ============================================================
# Step 3: Upload ZH (to WordPress BetterDocs as HTML)
# ============================================================

def markdown_to_html(md: str) -> str:
    """Convert markdown to clean HTML for WordPress/BetterDocs."""
    return article_to_html(md)


def article_base_slug(info: dict, fm: dict | None = None) -> str:
    """Build the English-title slug before duplicate disambiguation."""
    fm = fm or {}
    prefix = "articles"
    if fm.get("slug"):
        value = slugify(fm["slug"])
        return value if value.startswith(f"{prefix}-") else f"{prefix}-{value}"
    source_url = fm.get("source_url") or info.get("source_url", "")
    match = re.search(r"/articles/\d+-(.+)$", source_url)
    if match:
        return f"{prefix}-{slugify(match.group(1))}"
    filename = Path(info.get("filename", "")).stem
    return f"{prefix}-{slugify(filename)}"


def article_slug_base_counts() -> dict:
    crawl_meta = load_json(CRAWL_META).get("articles", {})
    counts: dict[str, int] = {}
    for info in crawl_meta.values():
        base = article_base_slug(info, {})
        counts[base] = counts.get(base, 0) + 1
    return counts


def article_slug(info: dict, fm: dict, article_id: str = "") -> str:
    """Use stable English slugs, never translated Chinese titles; append ID for duplicate titles."""
    base = article_base_slug(info, fm)
    if article_id and article_slug_base_counts().get(base, 0) > 1 and not base.endswith(f"-{article_id}"):
        return f"{base}-{article_id}"
    return base


def has_duplicate_article_slug(info: dict, fm: dict) -> bool:
    return article_slug_base_counts().get(article_base_slug(info, fm), 0) > 1


def wp_doc_url(slug: str) -> str:
    base = (WP_SITE_URL or "https://dynamicycle.com").rstrip("/")
    return f"{base}/docs/{slug.strip('/')}/"


def strip_url_fragment(url: str) -> tuple[str, str]:
    parsed = urlparse(canonical_help_url(url or ""))
    fragment = parsed.fragment
    parsed = parsed._replace(query="", fragment="")
    clean = urlunparse(parsed).rstrip("/")
    return clean, fragment


def source_lookup_key(url: str) -> str:
    clean, _fragment = strip_url_fragment(url)
    match = re.search(r"/hc/en-us/(categories|sections|articles)/(\d+)", clean)
    if match:
        singular = {"categories": "category", "sections": "section", "articles": "article"}[match.group(1)]
        return f"{singular}:{match.group(2)}"
    return clean


def add_source_aliases(lookup: dict, source_url: str, local_url: str) -> None:
    clean, _fragment = strip_url_fragment(source_url)
    if not clean or not local_url:
        return
    lookup[source_lookup_key(clean)] = local_url
    lookup[clean] = local_url


def local_url_for_source(source_url: str, lookup: dict | None = None) -> str:
    if not source_url:
        return ""
    if lookup is None:
        lookup = load_json(SOURCE_TO_LOCAL_URL_MAP).get("lookup", {})
    clean, fragment = strip_url_fragment(source_url)
    local = lookup.get(source_lookup_key(clean)) or lookup.get(clean)
    if not local:
        return ""
    return f"{local}#{fragment}" if fragment else local


def article_expected_slug_from_source(article: dict) -> str:
    source_url = article.get("source_url", "")
    match = re.search(r"/articles/\d+-(.+)$", strip_url_fragment(source_url)[0])
    if match:
        base = f"articles-{slugify(match.group(1))}"
    else:
        base = f"articles-{slugify(article.get('title', '') or article.get('article_id', 'article'))}"
    article_id = id_text(article.get("article_id"))
    if article_id and article_slug_base_counts().get(base, 0) > 1 and not base.endswith(f"-{article_id}"):
        return f"{base}-{article_id}"
    return base


def cmd_prepare_url_maps():
    """Generate local source URL -> BetterDocs URL maps without fetching remote content."""
    logger = SyncLogger("Prepare local URL maps")
    URL_MAP_DIR.mkdir(parents=True, exist_ok=True)

    if not (RELATIONS_DIR / "category-sections.json").exists():
        cmd_relationships()

    menu_items = load_homepage_category_menu()
    category_uploads = load_json(HOMEPAGE_CATEGORY_UPLOAD_META)
    section_uploads = load_json(SECTION_PREVIEW_META)
    article_uploads = load_json(UPLOAD_META).get("uploaded", {})
    category_sections = load_json(RELATIONS_DIR / "category-sections.json")
    sections_articles = load_json(RELATIONS_DIR / "sections-articles.json")
    category_articles = load_json(RELATIONS_DIR / "category-articles.json")

    lookup: dict[str, str] = {}
    category_map = []
    for item in menu_items:
        slug = item.get("wp_doc_slug") or menu_doc_slug(item)
        uploaded = category_uploads.get(item.get("menu_slug", ""), {})
        local_url = uploaded.get("wp_link") or item.get("wp_doc_url") or wp_doc_url(slug)
        row = {
            "type": "category",
            "source_id": id_text(item.get("source_category_id")),
            "source_url": canonical_help_url(item.get("source_url", "")),
            "source_name": item.get("menu_name", ""),
            "title": item.get("menu_name_zh") or item.get("menu_name", ""),
            "slug": slug,
            "expected_url": wp_doc_url(slug),
            "wp_id": uploaded.get("wp_id", ""),
            "wp_url": local_url,
        }
        category_map.append(row)
        add_source_aliases(lookup, row["source_url"], local_url)

    existing_category_ids = {row["source_id"] for row in category_map if row.get("source_id")}
    for cat in category_sections:
        if id_text(cat.get("category_id")) in existing_category_ids:
            continue
        slug = category_doc_slug(cat)
        local_url = wp_doc_url(slug)
        row = {
            "type": "category",
            "source_id": id_text(cat.get("category_id")),
            "source_url": canonical_help_url(cat.get("source_url", "")),
            "source_name": cat.get("category_name", ""),
            "title": cat.get("category_name", ""),
            "slug": slug,
            "expected_url": local_url,
            "wp_id": "",
            "wp_url": local_url,
        }
        category_map.append(row)
        add_source_aliases(lookup, row["source_url"], local_url)

    section_map = []
    seen_section_slugs = set()
    duplicate_section_slugs = []
    for section in sections_articles:
        slug = section_doc_slug(section)
        if slug in seen_section_slugs:
            duplicate_section_slugs.append(slug)
            slug = f"{slug}-{id_text(section.get('section_id'))}"
        seen_section_slugs.add(slug)
        uploaded = section_uploads.get(id_text(section.get("section_id")), {})
        local_url = uploaded.get("link") or wp_doc_url(slug)
        row = {
            "type": "section",
            "source_id": id_text(section.get("section_id")),
            "source_url": canonical_help_url(section.get("source_url", "")),
            "source_name": section.get("section_name", ""),
            "category_id": id_text(section.get("category_id")),
            "category_slug": section.get("category_slug", ""),
            "slug": slug,
            "expected_url": wp_doc_url(slug),
            "wp_id": uploaded.get("wp_id", ""),
            "wp_url": local_url,
            "article_count": len(section.get("articles", [])),
        }
        section_map.append(row)
        add_source_aliases(lookup, row["source_url"], local_url)

    article_map = []
    article_rows = []
    for category in category_articles:
        article_rows.extend(category.get("articles", []))
    seen_article_ids = set()
    for article in article_rows:
        aid = id_text(article.get("article_id"))
        if aid in seen_article_ids:
            continue
        seen_article_ids.add(aid)
        uploaded = article_uploads.get(aid, {})
        slug = uploaded.get("slug") or article_expected_slug_from_source(article)
        local_url = uploaded.get("link") or wp_doc_url(slug)
        row = {
            "type": "article",
            "source_id": aid,
            "source_url": canonical_help_url(article.get("source_url", "")),
            "source_name": article.get("title", ""),
            "category_id": id_text(article.get("category_id")),
            "category_slug": article.get("category_slug", ""),
            "section_id": id_text(article.get("section_id")),
            "slug": slug,
            "expected_url": wp_doc_url(slug),
            "wp_id": uploaded.get("wp_id", ""),
            "wp_url": local_url,
        }
        article_map.append(row)
        add_source_aliases(lookup, row["source_url"], local_url)

    merged = {
        "generated_at": utc_now(),
        "lookup": lookup,
        "counts": {
            "categories": len(category_map),
            "sections": len(section_map),
            "articles": len(article_map),
            "lookup_keys": len(lookup),
            "duplicate_section_slugs": len(duplicate_section_slugs),
        },
        "duplicate_section_slugs": duplicate_section_slugs,
        "files": {
            "category_url_map": str(CATEGORY_URL_MAP.relative_to(PROJECT_ROOT)),
            "section_url_map": str(SECTION_URL_MAP.relative_to(PROJECT_ROOT)),
            "article_url_map": str(ARTICLE_URL_MAP.relative_to(PROJECT_ROOT)),
        },
    }

    redirect_map = load_json(REDIRECT_URL_MAP)
    for item in redirect_map.get("resolved", []):
        add_source_aliases(lookup, item.get("source_url", ""), item.get("local_url", ""))
    manual_aliases = load_json(MANUAL_URL_ALIASES)
    for item in manual_aliases.get("aliases", []):
        add_source_aliases(lookup, item.get("source_url", ""), item.get("local_url", ""))
    merged["lookup"] = lookup
    merged["counts"]["lookup_keys"] = len(lookup)
    merged["counts"]["redirect_aliases"] = len(redirect_map.get("resolved", []))
    merged["counts"]["manual_aliases"] = len(manual_aliases.get("aliases", []))

    save_json(CATEGORY_URL_MAP, {"generated_at": utc_now(), "items": category_map})
    save_json(SECTION_URL_MAP, {"generated_at": utc_now(), "items": section_map})
    save_json(ARTICLE_URL_MAP, {"generated_at": utc_now(), "items": article_map})
    save_json(SOURCE_TO_LOCAL_URL_MAP, merged)

    logger.ok(f"categories: {len(category_map)}")
    logger.ok(f"sections: {len(section_map)}")
    logger.ok(f"articles: {len(article_map)}")
    if duplicate_section_slugs:
        logger.fail(f"Duplicate section slugs detected: {len(duplicate_section_slugs)}")
    logger.summary()
    print(f"  URL map: {SOURCE_TO_LOCAL_URL_MAP}")


def resolve_internal_links_in_html(html_content: str, lookup: dict | None = None, *, report_context: str = "") -> tuple[str, list[dict]]:
    if not html_content:
        return html_content, []
    if lookup is None:
        lookup = load_json(SOURCE_TO_LOCAL_URL_MAP).get("lookup", {})
    soup = BeautifulSoup(html_content, "html.parser")
    unresolved = []
    for a in soup.find_all("a"):
        href = (a.get("href") or "").strip()
        if not href or href.startswith(("#", "mailto:", "tel:")):
            continue
        absolute = urljoin("https://help.klaviyo.com", href)
        parsed = urlparse(absolute)
        if parsed.netloc not in {"help.klaviyo.com", "klaviyo.zendesk.com"}:
            continue
        if not re.search(r"/hc/en-us/(articles|sections|categories)/\d+", parsed.path):
            continue
        local = local_url_for_source(absolute, lookup)
        if local:
            a["href"] = local
        else:
            unresolved.append({
                "context": report_context,
                "href": canonical_help_url(absolute),
                "text": re.sub(r"\s+", " ", a.get_text(" ", strip=True)).strip()[:160],
            })
    return str(soup), unresolved


def cmd_verify_url_maps():
    """Scan cached source HTML for unresolved internal Klaviyo links."""
    logger = SyncLogger("Verify local URL maps")
    if not SOURCE_TO_LOCAL_URL_MAP.exists():
        cmd_prepare_url_maps()
    lookup = load_json(SOURCE_TO_LOCAL_URL_MAP).get("lookup", {})
    unresolved = []
    scanned = 0
    for path in sorted(SOURCE_ARTICLES_DIR.glob("*.body.html")):
        article_id = path.stem.replace(".body", "")
        html_content = path.read_text("utf-8")
        _resolved, misses = resolve_internal_links_in_html(
            html_content,
            lookup,
            report_context=f"article:{article_id}",
        )
        scanned += 1
        unresolved.extend(misses)

    report = {
        "generated_at": utc_now(),
        "scanned_articles": scanned,
        "unresolved_count": len(unresolved),
        "unresolved": unresolved,
    }
    URL_MAP_DIR.mkdir(parents=True, exist_ok=True)
    save_json(UNRESOLVED_LINKS_REPORT, report)
    if unresolved:
        logger.fail(f"unresolved internal links: {len(unresolved)}")
    else:
        logger.ok("all cached internal links resolved")
    logger.summary()
    print(f"  Report: {UNRESOLVED_LINKS_REPORT}")


def cmd_resolve_redirect_links():
    """Resolve old Klaviyo help URLs and add aliases when they redirect to known local docs."""
    logger = SyncLogger("Resolve redirected Klaviyo links")
    if not UNRESOLVED_LINKS_REPORT.exists():
        cmd_verify_url_maps()
    if not SOURCE_TO_LOCAL_URL_MAP.exists():
        cmd_prepare_url_maps()

    previous_redirects = load_json(REDIRECT_URL_MAP)
    url_map = load_json(SOURCE_TO_LOCAL_URL_MAP)
    lookup = url_map.get("lookup", {})
    report = load_json(UNRESOLVED_LINKS_REPORT)
    unresolved = report.get("unresolved", [])
    unique_urls = sorted({strip_url_fragment(item.get("href", ""))[0] for item in unresolved if item.get("href")})

    resolved_aliases = []
    still_unresolved = []
    skipped = []
    session = requests.Session()
    session.headers.update({"User-Agent": "DynamicycleDocsSync/1.0 (+https://dynamicycle.com)"})

    for source_url in unique_urls:
        parsed = urlparse(source_url)
        path = parsed.path
        if not re.search(r"/hc/en-us/(articles|sections|categories)/", path):
            skipped.append({"source_url": source_url, "reason": "not a docs category/section/article URL"})
            continue
        try:
            resp = session.get(source_url, allow_redirects=True, timeout=25)
            final_url = canonical_help_url(resp.url)
            local = local_url_for_source(final_url, lookup)
            final_host = urlparse(final_url).netloc
            is_external_final = final_host and "help.klaviyo.com" not in final_host and "klaviyo.zendesk.com" not in final_host
            if resp.status_code < 400 and not local and is_external_final:
                local = final_url
            if resp.status_code < 400 and local:
                add_source_aliases(lookup, source_url, local)
                resolved_aliases.append({
                    "source_url": source_url,
                    "final_url": strip_url_fragment(final_url)[0],
                    "local_url": local,
                    "status_code": resp.status_code,
                })
                logger.ok(f"{source_url} -> {local}")
            else:
                still_unresolved.append({
                    "source_url": source_url,
                    "final_url": strip_url_fragment(final_url)[0],
                    "status_code": resp.status_code,
                    "reason": "final URL is not in local map",
                })
        except Exception as exc:
            still_unresolved.append({
                "source_url": source_url,
                "reason": str(exc),
            })
        time.sleep(0.12)

    url_map["lookup"] = lookup
    url_map["generated_at"] = utc_now()
    url_map.setdefault("counts", {})["lookup_keys"] = len(lookup)
    url_map.setdefault("counts", {})["redirect_aliases"] = len(resolved_aliases)
    save_json(SOURCE_TO_LOCAL_URL_MAP, url_map)
    resolved_by_source = {
        item.get("source_url", ""): item
        for item in previous_redirects.get("resolved", [])
        if item.get("source_url")
    }
    for item in resolved_aliases:
        resolved_by_source[item.get("source_url", "")] = item
    skipped_by_source = {
        item.get("source_url", ""): item
        for item in previous_redirects.get("skipped", [])
        if item.get("source_url")
    }
    for item in skipped:
        skipped_by_source[item.get("source_url", "")] = item

    save_json(REDIRECT_URL_MAP, {
        "generated_at": utc_now(),
        "resolved_count": len(resolved_by_source),
        "still_unresolved_count": len(still_unresolved),
        "skipped_count": len(skipped_by_source),
        "resolved": sorted(resolved_by_source.values(), key=lambda item: item.get("source_url", "")),
        "still_unresolved": still_unresolved,
        "skipped": sorted(skipped_by_source.values(), key=lambda item: item.get("source_url", "")),
    })
    if still_unresolved:
        logger.fail(f"still unresolved docs URLs: {len(still_unresolved)}")
    if skipped:
        logger.skip(f"skipped non-doc URLs: {len(skipped)}")
    logger.summary()
    print(f"  Redirect map: {REDIRECT_URL_MAP}")


def cmd_upload(dry_run=False, limit=None, force=False, only_ids=None):
    """Upload translated ZH articles to WP BetterDocs as HTML."""
    logger = SyncLogger("Upload ZH")
    wp = WordPressClient()

    translate_meta = load_json(TRANSLATE_META)
    upload_meta = load_json(UPLOAD_META)
    translated = translate_meta.get("translated", {})
    uploaded = upload_meta.get("uploaded", {})

    only_ids = {id_text(value) for value in (only_ids or []) if id_text(value)}
    to_upload = []
    for aid, info in translated.items():
        if only_ids and id_text(aid) not in only_ids:
            continue
        if force or aid not in uploaded:
            to_upload.append((aid, info))
    if limit:
        to_upload = to_upload[:limit]
    print(f"[3/3] {len(to_upload)} articles to upload")

    if dry_run:
        for aid, info in to_upload:
            action = "update/create" if force else "create-if-missing"
            print(f"  DRY-RUN [{action}] [{info.get('category_slug', '')}] {aid} {info.get('title', '')[:80]}")
        return

    cat_map = load_category_map()
    if not SOURCE_TO_LOCAL_URL_MAP.exists():
        cmd_prepare_url_maps()
    url_lookup = load_json(SOURCE_TO_LOCAL_URL_MAP).get("lookup", {})
    unresolved_links = []

    for aid, info in to_upload:
        filepath = KLAVIYO_CN_DIR / info["filename"]
        if not filepath.exists():
            logger.fail(f"Missing: {info['filename']}")
            continue

        content = filepath.read_text("utf-8")
        fm, body = parse_frontmatter(content)
        title = fm.get("title", info["title"])
        cat_slug = expected_category_slug_for_article(aid, info.get("category_slug", ""))
        slug = article_slug(info, fm, aid)
        duplicate_slug = has_duplicate_article_slug(info, fm)
        cat_id = cat_map.get(cat_slug)

        if not cat_id:
            logger.fail(f"No WP category for '{cat_slug}': {title[:40]}")
            continue

        # Convert markdown body to HTML
        html_content = markdown_to_html(body)
        html_content, misses = resolve_internal_links_in_html(
            html_content,
            url_lookup,
            report_context=f"article:{aid}",
        )
        unresolved_links.extend(misses)

        try:
            uploaded_record = uploaded.get(aid, {})
            existing = None
            if uploaded_record.get("wp_id") and not duplicate_slug:
                existing = {"id": uploaded_record["wp_id"]}
            if existing:
                try:
                    result = wp.update_doc(existing["id"], title=title, content=html_content, category_slug=cat_slug, slug=slug)
                    action = "updated"
                except requests.exceptions.HTTPError as exc:
                    if exc.response is None or exc.response.status_code != 404:
                        raise
                    existing = None
                    result = None
                    logger.skip(f"Stale WP id for {aid}; falling back to slug lookup")
            if not existing:
                existing = wp.find_doc_by_slug(slug)
                if not existing and not duplicate_slug:
                    existing = wp.find_doc_by_title(title)
                if existing:
                    result = wp.update_doc(existing["id"], title=title, content=html_content, category_slug=cat_slug, slug=slug)
                    action = "updated"
                else:
                    result = wp.create_doc(title=title, content=html_content, category_slug=cat_slug, slug=slug)
                    action = "created"
            if result:
                uploaded[aid] = {
                    "wp_id": result["id"],
                    "title": title,
                    "filename": info["filename"],
                    "category_slug": cat_slug,
                    "uploaded_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "action": action,
                    "slug": slug,
                    "link": result.get("link", ""),
                }
                logger.ok(f"[{cat_slug}] {title[:50]} → {action} WP #{result['id']}")

                if logger.results["success"] % 50 == 0:
                    save_json(UPLOAD_META, {"uploaded": uploaded})
        except Exception as e:
            logger.fail(f"{title[:40]}: {e}")
            save_json(UPLOAD_META, {"uploaded": uploaded})

        time.sleep(0.5)

    save_json(UPLOAD_META, {"uploaded": uploaded})
    if unresolved_links:
        URL_MAP_DIR.mkdir(parents=True, exist_ok=True)
        save_json(UNRESOLVED_LINKS_REPORT, {
            "generated_at": utc_now(),
            "source": "upload",
            "unresolved_count": len(unresolved_links),
            "unresolved": unresolved_links,
        })
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
# Local relationships (no remote fetch)
# ============================================================

def id_text(value) -> str:
    return "" if value is None else str(value)


def source_menu_slug_by_category_id(category_id: str) -> str:
    menu = load_json(HOMEPAGE_CATEGORY_MENU).get("categories", [])
    for item in menu:
        if id_text(item.get("source_category_id")) == id_text(category_id):
            return item.get("menu_slug", "")
    numeric_id = int(category_id) if id_text(category_id).isdigit() else 0
    return KLAVIYO_CATEGORY_MAP.get(numeric_id, "uncategorized")


def section_path(section_id: str, sections: dict) -> list[dict]:
    path = []
    seen = set()
    current = id_text(section_id)
    while current and current not in seen and current in sections:
        seen.add(current)
        sec = sections[current]
        path.append({
            "section_id": current,
            "name": sec.get("name", ""),
            "source_url": canonical_help_url(sec.get("source_url", "")),
        })
        current = id_text(sec.get("parent_section_id"))
    path.reverse()
    return path


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def cmd_relationships():
    """Build local category/section/article relationship indexes from cached metadata only."""
    logger = SyncLogger("Build local relationships")
    RELATIONS_DIR.mkdir(parents=True, exist_ok=True)

    crawl_meta = load_json(CRAWL_META)
    source_index = load_json(SOURCE_INDEX)
    translate_meta = load_json(TRANSLATE_META).get("translated", {})
    upload_meta = load_json(UPLOAD_META).get("uploaded", {})
    wp_category_map = load_category_map()

    raw_categories = crawl_meta.get("categories") or source_index.get("categories", {})
    raw_sections = crawl_meta.get("sections") or source_index.get("sections", {})
    raw_articles = crawl_meta.get("articles") or source_index.get("articles", {})

    categories = {id_text(k): v for k, v in raw_categories.items()}
    sections = {id_text(k): v for k, v in raw_sections.items()}
    articles = {id_text(k): v for k, v in raw_articles.items()}

    def category_record(category_id: str) -> dict:
        cat = categories.get(category_id, {})
        numeric_id = int(category_id) if category_id.isdigit() else 0
        slug = source_menu_slug_by_category_id(category_id)
        return {
            "category_id": category_id,
            "category_name": cat.get("name") or KLAVIYO_CATEGORY_NAMES.get(numeric_id, "Uncategorized"),
            "category_slug": slug,
            "wp_category_id": wp_category_map.get(slug, ""),
            "source_url": canonical_help_url(cat.get("source_url", "")),
            "position": cat.get("position", 0),
            "updated_at": cat.get("updated_at", ""),
        }

    def section_record(section_id: str) -> dict:
        sec = sections.get(section_id, {})
        category_id = id_text(sec.get("category_id"))
        parent_id = id_text(sec.get("parent_section_id"))
        path = section_path(section_id, sections)
        return {
            "section_id": section_id,
            "section_name": sec.get("name", ""),
            "source_url": canonical_help_url(sec.get("source_url", "")),
            "position": sec.get("position", 0),
            "parent_section_id": parent_id,
            "parent_section_name": sections.get(parent_id, {}).get("name", ""),
            "category_id": category_id,
            "category_name": category_record(category_id)["category_name"],
            "category_slug": category_record(category_id)["category_slug"],
            "wp_category_id": category_record(category_id)["wp_category_id"],
            "path": path,
            "path_text": " > ".join(item["name"] for item in path),
            "updated_at": sec.get("updated_at", ""),
        }

    def article_record(article_id: str, article: dict) -> dict:
        section_id = id_text(article.get("section_id"))
        sec = sections.get(section_id, {})
        category_id = id_text(sec.get("category_id"))
        translated = translate_meta.get(article_id, {})
        uploaded = upload_meta.get(article_id, {})
        path = section_path(section_id, sections)
        return {
            "article_id": article_id,
            "title": article.get("title", ""),
            "source_url": canonical_help_url(article.get("source_url", "")),
            "category_id": category_id,
            "category_name": category_record(category_id)["category_name"],
            "category_slug": category_record(category_id)["category_slug"],
            "wp_category_id": category_record(category_id)["wp_category_id"],
            "section_id": section_id,
            "section_name": article.get("section") or sec.get("name", ""),
            "section_path": path,
            "section_path_text": " > ".join(item["name"] for item in path),
            "en_file": article.get("filename", ""),
            "source_snapshot": article.get("source_snapshot", ""),
            "body_html": article.get("body_html", ""),
            "rendered_html": article.get("rendered_html", ""),
            "klaviyo_updated": article.get("klaviyo_updated", ""),
            "translated": bool(translated),
            "zh_file": translated.get("filename", ""),
            "uploaded": bool(uploaded),
            "wp_id": uploaded.get("wp_id", ""),
            "wp_link": uploaded.get("link", ""),
        }

    section_article_map = {sid: [] for sid in sections}
    category_article_map = {cid: [] for cid in categories}
    category_section_map = {cid: [] for cid in categories}

    section_records = {sid: section_record(sid) for sid in sections}
    article_records = {
        aid: article_record(aid, article)
        for aid, article in articles.items()
    }

    for sid, sec in section_records.items():
        category_section_map.setdefault(sec["category_id"], []).append(sec)

    for aid, article in article_records.items():
        section_article_map.setdefault(article["section_id"], []).append(article)
        category_article_map.setdefault(article["category_id"], []).append(article)

    for items in category_section_map.values():
        items.sort(key=lambda item: (item.get("position", 0), item.get("section_name", "")))
    for items in section_article_map.values():
        items.sort(key=lambda item: (item.get("title", ""), item.get("article_id", "")))
    for items in category_article_map.values():
        items.sort(key=lambda item: (item.get("section_path_text", ""), item.get("title", "")))

    category_sections = []
    for category_id in sorted(category_section_map, key=lambda cid: (category_record(cid)["position"], category_record(cid)["category_name"])):
        cat = category_record(category_id)
        sections_for_cat = category_section_map.get(category_id, [])
        category_sections.append({
            **cat,
            "section_count": len(sections_for_cat),
            "article_count": len(category_article_map.get(category_id, [])),
            "sections": sections_for_cat,
        })

    sections_articles = []
    for sid in sorted(section_records, key=lambda sid: (section_records[sid]["category_name"], section_records[sid]["path_text"])):
        sec = section_records[sid]
        articles_for_section = section_article_map.get(sid, [])
        sections_articles.append({
            **sec,
            "article_count": len(articles_for_section),
            "articles": articles_for_section,
        })

    category_articles = []
    for category_id in sorted(category_article_map, key=lambda cid: (category_record(cid)["position"], category_record(cid)["category_name"])):
        cat = category_record(category_id)
        articles_for_cat = category_article_map.get(category_id, [])
        category_articles.append({
            **cat,
            "article_count": len(articles_for_cat),
            "articles": articles_for_cat,
        })

    files = {
        "category_sections_json": RELATIONS_DIR / "category-sections.json",
        "sections_articles_json": RELATIONS_DIR / "sections-articles.json",
        "category_articles_json": RELATIONS_DIR / "category-articles.json",
        "relationships_index_json": RELATIONS_DIR / "relationships-index.json",
        "category_sections_csv": RELATIONS_DIR / "category-sections.csv",
        "sections_articles_csv": RELATIONS_DIR / "sections-articles.csv",
        "category_articles_csv": RELATIONS_DIR / "category-articles.csv",
    }

    save_json(files["category_sections_json"], category_sections)
    save_json(files["sections_articles_json"], sections_articles)
    save_json(files["category_articles_json"], category_articles)

    category_section_rows = []
    for cat in category_sections:
        for sec in cat["sections"]:
            category_section_rows.append({
                "category_id": cat["category_id"],
                "category_name": cat["category_name"],
                "category_slug": cat["category_slug"],
                "wp_category_id": cat["wp_category_id"],
                "section_id": sec["section_id"],
                "section_name": sec["section_name"],
                "parent_section_id": sec["parent_section_id"],
                "parent_section_name": sec["parent_section_name"],
                "section_path": sec["path_text"],
                "section_source_url": sec["source_url"],
            })

    section_article_rows = []
    for sec in sections_articles:
        for article in sec["articles"]:
            section_article_rows.append({
                "section_id": sec["section_id"],
                "section_name": sec["section_name"],
                "section_path": sec["path_text"],
                "category_id": sec["category_id"],
                "category_name": sec["category_name"],
                "category_slug": sec["category_slug"],
                "article_id": article["article_id"],
                "title": article["title"],
                "source_url": article["source_url"],
                "en_file": article["en_file"],
                "translated": article["translated"],
                "uploaded": article["uploaded"],
                "wp_id": article["wp_id"],
                "wp_link": article["wp_link"],
            })

    category_article_rows = []
    for cat in category_articles:
        for article in cat["articles"]:
            category_article_rows.append({
                "category_id": cat["category_id"],
                "category_name": cat["category_name"],
                "category_slug": cat["category_slug"],
                "wp_category_id": cat["wp_category_id"],
                "article_id": article["article_id"],
                "title": article["title"],
                "section_id": article["section_id"],
                "section_name": article["section_name"],
                "section_path": article["section_path_text"],
                "source_url": article["source_url"],
                "en_file": article["en_file"],
                "translated": article["translated"],
                "uploaded": article["uploaded"],
                "wp_id": article["wp_id"],
                "wp_link": article["wp_link"],
            })

    write_csv(files["category_sections_csv"], category_section_rows, list(category_section_rows[0].keys()) if category_section_rows else [])
    write_csv(files["sections_articles_csv"], section_article_rows, list(section_article_rows[0].keys()) if section_article_rows else [])
    write_csv(files["category_articles_csv"], category_article_rows, list(category_article_rows[0].keys()) if category_article_rows else [])

    summary = {
        "generated_at": utc_now(),
        "source": "local klaviyo-en/.crawl_meta.json and klaviyo-en/_source only",
        "counts": {
            "categories": len(categories),
            "sections": len(sections),
            "articles": len(articles),
            "category_section_rows": len(category_section_rows),
            "section_article_rows": len(section_article_rows),
            "category_article_rows": len(category_article_rows),
            "translated_articles": sum(1 for article in article_records.values() if article["translated"]),
            "uploaded_articles": sum(1 for article in article_records.values() if article["uploaded"]),
        },
        "files": {key: str(path.relative_to(PROJECT_ROOT)) for key, path in files.items()},
    }
    save_json(files["relationships_index_json"], summary)

    if SOURCE_INDEX.exists():
        source_index["relationships"] = summary
        save_json(SOURCE_INDEX, source_index)

    logger.ok(f"category-sections: {len(category_section_rows)} rows")
    logger.ok(f"sections-articles: {len(section_article_rows)} rows")
    logger.ok(f"category-articles: {len(category_article_rows)} rows")
    logger.summary()
    print(f"  Relationships index: {files['relationships_index_json']}")


# ============================================================
# Homepage category menu (20 source directory entries)
# ============================================================

def menu_category_slug(name: str) -> str:
    return slugify(name.replace("&", " "))


def menu_doc_slug(item: dict) -> str:
    return f"categories-{item['menu_slug']}"


def menu_doc_link(item: dict) -> str:
    return f"https://dynamicycle.com/docs/{menu_doc_slug(item)}/"


def relationship_by_category_id() -> dict:
    items = load_json(RELATIONS_DIR / "category-articles.json")
    return {id_text(item.get("category_id")): item for item in items}


def fallback_category_slug(menu_slug: str, relation: dict | None = None) -> str:
    if relation:
        return relation.get("category_slug", "")
    if menu_slug == "push-notifications":
        return "campaigns"
    if menu_slug == "featured-resources":
        return ""
    return menu_slug


def crawl_homepage_category_menu() -> list[dict]:
    HOMEPAGE_MENU_DIR.mkdir(parents=True, exist_ok=True)
    url = "https://help.klaviyo.com/hc/en-us"

    def _do():
        resp = requests.get(
            url,
            headers={"User-Agent": "DynamicycleDocsSync/1.0 (+https://dynamicycle.com)"},
            timeout=45,
        )
        resp.raise_for_status()
        return resp.text

    page_html = with_retry(_do, description="GET Klaviyo help center home")
    soup = BeautifulSoup(page_html, "html.parser")
    links = soup.select("a[class*='topicsMenuItem']")
    if not links:
        links = [a for a in soup.find_all("a") if "/hc/en-us/categories/" in (a.get("href") or "")]

    seen = set()
    rows = []
    relations = relationship_by_category_id()
    for position, a in enumerate(links, start=1):
        name = re.sub(r"\s+", " ", a.get_text(" ", strip=True)).strip()
        href = a.get("href") or ""
        if not name:
            continue
        menu_slug = menu_category_slug(name)
        if menu_slug in seen:
            continue
        seen.add(menu_slug)
        source_url = urljoin(url, href)
        match = re.search(r"/categories/(\d+)", href)
        category_id = match.group(1) if match else ""
        relation = relations.get(category_id)
        category_slug = fallback_category_slug(menu_slug, relation)
        rows.append({
            "position": len(rows) + 1,
            "menu_name": name,
            "menu_name_zh": MENU_CATEGORY_ZH.get(menu_slug, name),
            "menu_slug": menu_slug,
            "source_url": source_url,
            "source_category_id": category_id,
            "local_category_slug": category_slug,
            "article_count": len(relation.get("articles", [])) if relation else 0,
            "section_count": len({id_text(article.get("section_id")) for article in relation.get("articles", [])}) if relation else 0,
            "wp_doc_slug": f"categories-{menu_slug}",
            "wp_doc_url": f"https://dynamicycle.com/docs/categories-{menu_slug}/",
            "has_local_relation": bool(relation),
        })

    menu = {
        "source_url": url,
        "captured_at": utc_now(),
        "count": len(rows),
        "categories": rows,
    }
    save_json(HOMEPAGE_CATEGORY_MENU, menu)
    write_csv(HOMEPAGE_CATEGORY_MENU_CSV, rows, list(rows[0].keys()) if rows else [])
    return rows


def cmd_crawl_homepage_categories():
    logger = SyncLogger("Crawl homepage category menu")
    rows = crawl_homepage_category_menu()
    logger.ok(f"{len(rows)} category menu entries saved")
    logger.summary()
    print(f"  Menu JSON: {HOMEPAGE_CATEGORY_MENU}")
    print(f"  Menu CSV: {HOMEPAGE_CATEGORY_MENU_CSV}")


def category_tree_targets() -> list[dict]:
    rows = load_homepage_category_menu()
    targets = []
    for item in rows:
        targets.append({
            "position": item.get("position", 0),
            "menu_slug": item["menu_slug"],
            "wp_slug": f'klaviyo-{item["menu_slug"]}',
            "reuse_slug": LEGACY_CATEGORY_SLUG_REUSE.get(item["menu_slug"], f'klaviyo-{item["menu_slug"]}'),
            "name": item.get("menu_name_zh") or item.get("menu_name") or item["menu_slug"],
            "source_name": item.get("menu_name", ""),
            "source_category_id": id_text(item.get("source_category_id")),
            "source_url": item.get("source_url", ""),
            "article_count": item.get("article_count", 0),
            "section_count": item.get("section_count", 0),
        })
    return targets


def cmd_ensure_category_tree():
    """Ensure Kalaviyo parent has exactly the 20 source homepage categories as child terms."""
    logger = SyncLogger("Ensure BetterDocs category tree")
    wp = WordPressClient()
    existing = wp.get_categories()
    by_slug = {item.get("slug"): item for item in existing}
    cat_map = {}
    report = {
        "generated_at": utc_now(),
        "parent_category_id": WP_PARENT_CAT,
        "parent_name": "Kalaviyo 官方文档",
        "items": [],
        "legacy_top_level": [],
    }

    for target in category_tree_targets():
        current = by_slug.get(target["wp_slug"]) or by_slug.get(target["reuse_slug"])
        if current:
            result = wp.update_category(
                current["id"],
                name=target["name"],
                slug=target["wp_slug"],
                parent=WP_PARENT_CAT,
            )
            action = "updated"
        else:
            result = wp.create_category(
                target["name"],
                target["wp_slug"],
                parent=WP_PARENT_CAT,
            )
            action = "created"
        cat_map[target["menu_slug"]] = result["id"]
        report["items"].append({
            **target,
            "wp_category_id": result["id"],
            "wp_slug": result.get("slug", target["wp_slug"]),
            "parent": result.get("parent"),
            "action": action,
        })
        logger.ok(f"{target['menu_slug']} -> {action} #{result['id']}")
        time.sleep(0.2)

    legacy_source_slugs = {
        "account-billing",
        "advanced-kdp-marketing-analytics",
        "analytics-audience",
        "campaigns",
        "content",
        "conversations",
        "customer-agent",
        "customer-hub",
        "deliverability-compliance",
        "flows",
        "helpdesk",
        "integrations",
        "reviews",
        "sign-up-forms",
        "sms-whatsapp",
    }
    for item in existing:
        if item.get("parent") == 0 and item.get("slug") in legacy_source_slugs:
            report["legacy_top_level"].append({
                "id": item.get("id"),
                "slug": item.get("slug"),
                "name": item.get("name"),
                "count": item.get("count"),
            })

    save_category_map(cat_map)
    report_path = SOURCE_DIR / "category-tree-report.json"
    save_json(report_path, report)
    logger.summary()
    print(f"  Category map: {KLAVIYO_EN_DIR / '.category_map.json'}")
    print(f"  Tree report: {report_path}")


def expected_wp_category_for_article(article_id: str, fallback_slug: str = "") -> int | None:
    cat_map = load_category_map()
    snapshot = SOURCE_ARTICLES_DIR / f"{article_id}.json"
    if snapshot.exists():
        data = load_json(snapshot)
        normalized = data.get("normalized", {})
        menu_slug = source_menu_slug_by_category_id(id_text(normalized.get("category_id")))
        if menu_slug in cat_map:
            return cat_map[menu_slug]
    if fallback_slug in cat_map:
        return cat_map[fallback_slug]
    return None


def expected_category_slug_for_article(article_id: str, fallback_slug: str = "") -> str:
    snapshot = SOURCE_ARTICLES_DIR / f"{article_id}.json"
    if snapshot.exists():
        data = load_json(snapshot)
        normalized = data.get("normalized", {})
        menu_slug = source_menu_slug_by_category_id(id_text(normalized.get("category_id")))
        if menu_slug and menu_slug != "uncategorized":
            return menu_slug
    return fallback_slug


def build_expected_doc_category_assignments() -> dict[int, dict]:
    """Return expected single child BetterDocs category per known Klaviyo-derived doc."""
    cat_map = load_category_map()
    expected: dict[int, dict] = {}

    def add(wp_id, category_slug: str, source: str, source_id: str = ""):
        if not wp_id or category_slug not in cat_map:
            return
        expected[int(wp_id)] = {
            "categories": [cat_map[category_slug]],
            "category_slug": category_slug,
            "source": source,
            "source_id": source_id,
        }

    for menu_slug, item in load_json(HOMEPAGE_CATEGORY_UPLOAD_META).items():
        add(item.get("wp_id"), menu_slug, "homepage-category", id_text(item.get("source_category_id")))

    for category_slug, item in load_json(CATEGORY_PREVIEW_META).items():
        add(item.get("wp_id"), category_slug, "category-preview", id_text(item.get("category_id")))

    for section_id, item in load_json(SECTION_PREVIEW_META).items():
        add(item.get("wp_id"), item.get("category_slug", ""), "section-preview", id_text(section_id))

    for meta_path, key in [
        (UPLOAD_META, "uploaded"),
        (KLAVIYO_EN_DIR / ".push_meta.json", "pushed"),
    ]:
        for article_id, item in load_json(meta_path).get(key, {}).items():
            wp_cat_id = expected_wp_category_for_article(article_id, item.get("category_slug", ""))
            if not item.get("wp_id") or not wp_cat_id:
                continue
            expected[int(item["wp_id"])] = {
                "categories": [wp_cat_id],
                "category_slug": next((slug for slug, cid in cat_map.items() if cid == wp_cat_id), ""),
                "source": key,
                "source_id": id_text(article_id),
            }

    return expected


def infer_expected_category_from_slug(doc_slug: str) -> dict | None:
    cat_map = load_category_map()
    menu_slugs = sorted(cat_map.keys(), key=len, reverse=True)
    for menu_slug in menu_slugs:
        if doc_slug == f"categories-{menu_slug}" or doc_slug.startswith(f"categories-{menu_slug}-"):
            return {
                "categories": [cat_map[menu_slug]],
                "category_slug": menu_slug,
                "source": "slug-category-page",
                "source_id": "",
            }
        if doc_slug.startswith(f"sections-{menu_slug}-"):
            return {
                "categories": [cat_map[menu_slug]],
                "category_slug": menu_slug,
                "source": "slug-section-page",
                "source_id": "",
            }
    return None


def cmd_clean_parent_category(dry_run: bool = True, limit: int | None = None):
    """Normalize Klaviyo docs so each doc belongs only to its correct child category."""
    logger = SyncLogger("Clean parent category assignments")
    wp = WordPressClient()
    docs = wp.get_all_docs()
    expected_by_doc_id = build_expected_doc_category_assignments()
    candidates = []
    parent_only = []
    already_ok = 0
    unknown_parent_child = []
    for doc in docs:
        cats = doc.get("doc_category") or []
        doc_id = int(doc.get("id"))
        doc_slug = doc.get("slug", "")
        expected = expected_by_doc_id.get(doc_id) or infer_expected_category_from_slug(doc_slug)
        if expected:
            new_cats = expected["categories"]
            if cats == new_cats:
                already_ok += 1
                continue
            candidates.append({
                "id": doc_id,
                "slug": doc_slug,
                "title": BeautifulSoup(doc.get("title", {}).get("rendered", ""), "html.parser").get_text(" ", strip=True),
                "old_categories": cats,
                "new_categories": new_cats,
                "category_slug": expected.get("category_slug", ""),
                "source": expected.get("source", ""),
                "source_id": expected.get("source_id", ""),
                "link": doc.get("link", ""),
            })
        elif WP_PARENT_CAT in cats and len(cats) > 1:
            new_cats = [cat for cat in cats if cat != WP_PARENT_CAT]
            unknown_parent_child.append({
                "id": doc_id,
                "slug": doc_slug,
                "title": BeautifulSoup(doc.get("title", {}).get("rendered", ""), "html.parser").get_text(" ", strip=True),
                "old_categories": cats,
                "new_categories": new_cats,
                "link": doc.get("link", ""),
            })
        elif cats == [WP_PARENT_CAT]:
            parent_only.append({
                "id": doc_id,
                "slug": doc_slug,
                "title": BeautifulSoup(doc.get("title", {}).get("rendered", ""), "html.parser").get_text(" ", strip=True),
                "categories": cats,
                "link": doc.get("link", ""),
            })

    candidates.extend(unknown_parent_child)
    if limit:
        candidates_to_update = candidates[:limit]
    else:
        candidates_to_update = candidates

    report = {
        "generated_at": utc_now(),
        "dry_run": dry_run,
        "total_docs": len(docs),
        "known_expected_count": len(expected_by_doc_id),
        "already_ok_count": already_ok,
        "will_update_count": len(candidates_to_update),
        "candidate_count": len(candidates),
        "unknown_parent_child_count": len(unknown_parent_child),
        "parent_only_count": len(parent_only),
        "parent_only": parent_only,
        "items": candidates_to_update,
    }
    report_path = SOURCE_DIR / "parent-category-cleanup-report.json"
    save_json(report_path, report)

    print(f"Total docs: {len(docs)}")
    print(f"Known expected docs: {len(expected_by_doc_id)}")
    print(f"Already correct: {already_ok}")
    print(f"Docs to normalize: {len(candidates)}")
    print(f"Fallback parent+child only: {len(unknown_parent_child)}")
    print(f"Docs parent only: {len(parent_only)}")
    print(f"Will update this run: {len(candidates_to_update)}")
    if dry_run:
        print("DRY-RUN only. No WordPress writes will be made.")
        for item in candidates_to_update[:20]:
            print(f"  DRY {item['id']} {item['slug']} {item['old_categories']} -> {item['new_categories']} ({item.get('category_slug') or 'fallback'})")
        if len(candidates_to_update) > 20:
            print(f"  ... {len(candidates_to_update) - 20} more")
        logger.ok("dry-run completed")
        logger.summary()
        print(f"  Report: {report_path}")
        return

    for item in candidates_to_update:
        try:
            result = wp.update_doc_categories(item["id"], item["new_categories"])
            logger.ok(f"{item['id']} {item['slug']} -> {result.get('doc_category')}")
            time.sleep(0.15)
        except Exception as exc:
            logger.fail(f"{item['id']} {item['slug']}: {exc}")
            save_json(report_path, {**report, "logger": logger.results})

    report["completed_at"] = utc_now()
    report["logger"] = logger.results
    save_json(report_path, report)
    logger.summary()
    print(f"  Report: {report_path}")


def load_homepage_category_menu() -> list[dict]:
    data = load_json(HOMEPAGE_CATEGORY_MENU)
    rows = data.get("categories", [])
    if rows:
        return rows
    return crawl_homepage_category_menu()


def zh_article_title(article: dict, upload_meta: dict) -> str:
    uploaded = upload_meta.get(id_text(article.get("article_id")), {})
    return uploaded.get("title") or article.get("title", "")


def category_source_reference(item: dict, refresh: bool = False) -> dict:
    """Capture source category layout elements used by Klaviyo category pages."""
    SOURCE_CATEGORY_PAGES_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = SOURCE_CATEGORY_PAGES_DIR / f"{item['menu_slug']}.json"
    if cache_path.exists() and not refresh:
        return load_json(cache_path)

    source_url = item.get("source_url", "")
    reference = {
        "source_url": source_url,
        "captured_at": utc_now(),
        "title": item.get("menu_name", ""),
        "description": "",
        "section_cards": [],
        "top_articles": [],
    }
    if not source_url:
        save_json(cache_path, reference)
        return reference

    def _do():
        resp = requests.get(source_url, timeout=30)
        resp.raise_for_status()
        return resp.text

    page_html = with_retry(_do, description=f"GET category page: {item['menu_slug']}")
    soup = BeautifulSoup(page_html, "html.parser")
    h1 = soup.find("h1")
    if h1:
        reference["title"] = h1.get_text(" ", strip=True) or reference["title"]
        meta = h1.find_parent()
        desc = meta.find("p") if meta else None
        if not desc and meta:
            for sibling in h1.find_next_siblings():
                if sibling.get_text(" ", strip=True):
                    desc = sibling
                    break
        if not desc:
            desc = h1.find_next("p")
        if desc:
            reference["description"] = desc.get_text(" ", strip=True)

    for link in soup.find_all("a", href=True):
        href = link.get("href", "")
        text = link.get_text(" ", strip=True)
        if "/sections/" not in href or "article" not in text:
            continue
        match = re.match(r"(.+?)\s+(\d+)\s+articles?$", text, re.I)
        if not match:
            continue
        reference["section_cards"].append({
            "title": match.group(1).strip(),
            "article_count": int(match.group(2)),
            "source_url": canonical_help_url(urljoin(source_url, href)),
        })

    seen_articles = set()
    for link in soup.select('a[class*="topArticle"]'):
        href = link.get("href", "")
        if "/articles/" not in href or href in seen_articles:
            continue
        seen_articles.add(href)
        li = link.find_parent("li")
        desc = ""
        if li:
            paragraph = li.find("p")
            if paragraph:
                desc = paragraph.get_text(" ", strip=True)
        reference["top_articles"].append({
            "title": link.get_text(" ", strip=True),
            "description": desc,
            "source_url": canonical_help_url(urljoin(source_url, href)),
        })

    save_json(cache_path, reference)
    return reference


def first_paragraph_from_article_snapshot(article_id: str) -> str:
    snapshot = SOURCE_ARTICLES_DIR / f"{article_id}.json"
    if not snapshot.exists():
        return ""
    data = load_json(snapshot)
    body = data.get("article", {}).get("body", "")
    soup = BeautifulSoup(body, "html.parser")
    for tag in soup.find_all(["p", "li"]):
        text = tag.get_text(" ", strip=True)
        if text:
            return text
    return ""


def article_id_from_source_url(source_url: str) -> str:
    match = re.search(r"/articles/(\d+)", source_url or "")
    return match.group(1) if match else ""


def homepage_category_doc_html(item: dict, menu_items: list[dict], relation: dict | None, upload_meta: dict) -> str:
    lookup = load_json(SOURCE_TO_LOCAL_URL_MAP).get("lookup", {})
    source_ref = category_source_reference(item)
    articles = relation.get("articles", []) if relation else []
    article_by_id = {id_text(article.get("article_id")): article for article in articles}

    top_sections: dict[str, dict] = {}
    for article in articles:
        path = article.get("section_path") or []
        top = path[0] if path else {}
        key = id_text(top.get("section_id")) or id_text(article.get("section_id")) or article.get("section_name") or "other"
        if key not in top_sections:
            top_sections[key] = {
                "section_name": top.get("name") or article.get("section_name") or "Other",
                "source_url": top.get("source_url") or "",
                "articles": [],
            }
        top_sections[key]["articles"].append(article)

    section_cards = source_ref.get("section_cards") or [
        {
            "title": group["section_name"],
            "article_count": len(group["articles"]),
            "source_url": group.get("source_url", ""),
        }
        for group in sorted(top_sections.values(), key=lambda value: value["section_name"])
    ]
    card_html = []
    for card in section_cards:
        count = int(card.get("article_count") or 0)
        noun = "article" if count == 1 else "articles"
        link = local_url_for_source(card.get("source_url", ""), lookup) or card.get("source_url") or "#"
        card_html.append(
            f'<a class="dc-category-card" href="{escape_attr(link)}">'
            f'<span class="dc-card-title">{html.escape(card.get("title", ""))}</span>'
            f'<span class="dc-card-count">{count} {noun}</span>'
            '</a>'
        )

    top_articles = source_ref.get("top_articles") or []
    if not top_articles:
        top_articles = [
            {
                "title": article.get("title", ""),
                "description": first_paragraph_from_article_snapshot(id_text(article.get("article_id"))),
                "source_url": article.get("source_url", ""),
            }
            for article in articles[:6]
        ]

    if not card_html and item.get("menu_slug") == "featured-resources":
        for entry in menu_items:
            if entry.get("menu_slug") == item.get("menu_slug"):
                continue
            count = int(entry.get("article_count") or 0)
            noun = "article" if count == 1 else "articles"
            card_html.append(
                f'<a class="dc-category-card" href="{escape_attr(menu_doc_link(entry))}">'
                f'<span class="dc-card-title">{html.escape(entry.get("menu_name", ""))}</span>'
                f'<span class="dc-card-count">{count} {noun}</span>'
                '</a>'
            )

    top_article_html = []
    for top_article in top_articles:
        article_id = article_id_from_source_url(top_article.get("source_url", ""))
        local_article = article_by_id.get(article_id, {})
        link = (
            local_url_for_source(top_article.get("source_url", ""), lookup)
            or article_preview_link(local_article)
            or top_article.get("source_url")
            or "#"
        )
        description = top_article.get("description") or first_paragraph_from_article_snapshot(article_id)
        top_article_html.append(
            '<li>'
            f'<a href="{escape_attr(link)}">{html.escape(top_article.get("title", ""))}</a>'
            f'<p>{html.escape(description)}</p>'
            '</li>'
        )

    top_articles_section = (
        f'<section class="dc-top-articles" aria-label="Top articles">'
        f'<h2>Top articles</h2>'
        f'<ul>{"".join(top_article_html)}</ul>'
        f'</section>'
        if top_article_html else ""
    )

    title = source_ref.get("title") or item.get("menu_name") or item.get("menu_name_zh", "")
    description = source_ref.get("description") or ""

    return f"""
<style>
.wp-block-post-title,.betterdocs-social-share,.betterdocs-article-reactions,.betterdocs-entry-footer,.betterdocs-feedback-form,.betterdocs-article-reactions-heading,.betterdocs-toc,.betterdocs-toc-wrapper,.batterdocs-anchor{{display:none!important}}
.dc-source-category{{max-width:980px;margin:0;padding:0 0 36px;color:#242424;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.dc-source-category h1{{font-size:26px;line-height:1.25;font-weight:400;margin:0 0 14px;color:#242424;letter-spacing:0}}
.dc-source-category .dc-description{{font-size:20px;line-height:1.45;margin:0 0 30px;color:#242424}}
.dc-category-grid{{display:grid;grid-template-columns:repeat(3,minmax(200px,1fr));gap:24px;margin:0 0 70px}}
.dc-category-grid>br,.dc-top-articles>br{{display:none!important}}
.dc-category-card{{min-height:110px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;padding:20px 18px;background:#fff;border:1px solid #f2f2ef;border-radius:8px;box-shadow:0 8px 18px rgba(15,23,42,.08);text-decoration:none;color:#242424;transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease}}
.dc-category-card:hover{{transform:translateY(-2px);box-shadow:0 12px 24px rgba(15,23,42,.11);border-color:#deded8;color:#111827}}
.dc-card-title{{font-size:19px;line-height:1.3;text-align:center;font-weight:400;max-width:210px}}
.dc-card-count{{font-size:16px;line-height:1.3;text-align:center;color:#242424}}
.dc-top-articles h2{{font-size:22px;line-height:1.3;font-weight:400;margin:0 0 24px;color:#242424;letter-spacing:0}}
.dc-top-articles ul{{list-style:none;margin:0;padding:0}}
.dc-top-articles li{{margin:0 0 32px;padding:0}}
.dc-top-articles a{{display:inline;color:#242424;font-size:20px;line-height:1.35;text-decoration:underline;text-underline-offset:3px}}
.dc-top-articles a:hover{{color:#0f766e}}
.dc-top-articles p{{max-width:900px;margin:5px 0 0;color:#2f2f2f;font-size:15px;line-height:1.5}}
@media(max-width:900px){{.dc-category-grid{{grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-bottom:50px}}}}
@media(max-width:560px){{.dc-source-category{{padding:4px 0 30px}}.dc-source-category .dc-description{{font-size:18px;margin-bottom:24px}}.dc-category-grid{{grid-template-columns:1fr;gap:14px;margin-bottom:42px}}.dc-category-card{{min-height:104px}}.dc-top-articles li{{margin-bottom:26px}}}}
</style>
<div class="dc-source-category">
  <h1>{html.escape(title)}</h1>
  <p class="dc-description">{html.escape(description)}</p>
  <div class="dc-category-grid" aria-label="Category sections">
    {"".join(card_html)}
  </div>
  {top_articles_section}
</div>
""".strip()


def cmd_upload_homepage_categories(category_slug: str = ""):
    logger = SyncLogger("Upload 20 category docs")
    all_menu_items = load_homepage_category_menu()
    menu_items = all_menu_items
    if category_slug:
        menu_items = [item for item in all_menu_items if item.get("menu_slug") == category_slug]
        if not menu_items:
            raise RuntimeError(f"Homepage category not found: {category_slug}")
    if len(menu_items) != 20:
        logger.skip(f"Uploading selected homepage categories: {len(menu_items)}")
    relations = relationship_by_category_id()
    upload_meta = load_json(UPLOAD_META).get("uploaded", {})
    wp = WordPressClient()
    preview_dir = PROJECT_ROOT / "build" / "previews" / "homepage-categories"
    preview_dir.mkdir(parents=True, exist_ok=True)
    result_meta = load_json(HOMEPAGE_CATEGORY_UPLOAD_META)

    for item in menu_items:
        relation = relations.get(id_text(item.get("source_category_id")))
        title = f"分类：{item['menu_name_zh']}"
        slug = menu_doc_slug(item)
        content = homepage_category_doc_html(item, all_menu_items, relation, upload_meta)
        (preview_dir / f"{slug}.html").write_text(content, "utf-8")
        category_slug = fallback_category_slug(item["menu_slug"], relation)

        try:
            existing = wp.find_doc_by_slug(slug) or wp.find_doc_by_title(title)
            if existing:
                result = wp.update_doc(
                    existing["id"],
                    title=title,
                    content=content,
                    category_slug=category_slug,
                    slug=slug,
                )
                action = "updated"
            else:
                result = wp.create_doc(
                    title=title,
                    content=content,
                    category_slug=category_slug,
                    slug=slug,
                )
                action = "created"
            result_meta[item["menu_slug"]] = {
                **item,
                "title": title,
                "wp_id": result.get("id"),
                "wp_link": result.get("link", menu_doc_link(item)),
                "action": action,
                "uploaded_at": utc_now(),
                "local_preview": str((preview_dir / f"{slug}.html").relative_to(PROJECT_ROOT)),
            }
            logger.ok(f"{item['menu_name']} -> {action} {result.get('link', '')}")
            time.sleep(0.2)
        except Exception as exc:
            logger.fail(f"{item['menu_name']}: {exc}")
        save_json(HOMEPAGE_CATEGORY_UPLOAD_META, result_meta)

    menu_data = load_json(HOMEPAGE_CATEGORY_MENU)
    menu_data["uploaded_at"] = utc_now()
    menu_data["uploads"] = result_meta
    save_json(HOMEPAGE_CATEGORY_MENU, menu_data)
    logger.summary()
    print(f"  Upload meta: {HOMEPAGE_CATEGORY_UPLOAD_META}")


# ============================================================
# Category preview upload
# ============================================================

def category_doc_slug(category: dict) -> str:
    value = category.get("category_slug") or slugify(category.get("category_name", "category"))
    return f"categories-{slugify(value)}"


def article_preview_link(article: dict) -> str:
    if article.get("wp_link"):
        return article["wp_link"]
    if article.get("wp_id"):
        return f"https://dynamicycle.com/?p={article['wp_id']}"
    return article.get("source_url", "#")


def category_page_html(category: dict) -> str:
    lookup = load_json(SOURCE_TO_LOCAL_URL_MAP).get("lookup", {})
    sections: dict[str, dict] = {}
    for article in category.get("articles", []):
        sid = id_text(article.get("section_id")) or "uncategorized"
        section_source_url = ""
        for path_item in article.get("section_path", []):
            if id_text(path_item.get("section_id")) == sid:
                section_source_url = path_item.get("source_url", "")
                break
        if sid not in sections:
            sections[sid] = {
                "section_id": sid,
                "section_name": article.get("section_name") or "Other",
                "section_path": article.get("section_path_text") or article.get("section_name") or "Other",
                "section_source_url": section_source_url,
                "articles": [],
            }
        if section_source_url and not sections[sid].get("section_source_url"):
            sections[sid]["section_source_url"] = section_source_url
        sections[sid]["articles"].append(article)

    ordered_sections = sorted(
        sections.values(),
        key=lambda item: (item.get("section_path", ""), item.get("section_name", "")),
    )
    section_count = len(ordered_sections)
    article_count = sum(len(item["articles"]) for item in ordered_sections)

    cards = []
    for sec in ordered_sections:
        count = len(sec["articles"])
        noun = "article" if count == 1 else "articles"
        link = local_url_for_source(sec.get("section_source_url", ""), lookup) or wp_doc_url(
            f"sections-{slugify(category.get('category_slug', 'category'))}-{slugify(sec['section_name'])}"
        )
        cards.append(
            f'<a class="dc-section-card" href="{escape_attr(link)}">'
            f'<span class="dc-card-title">{html.escape(sec["section_name"])}</span>'
            f'<span class="dc-card-count">{count} {noun}</span>'
            '</a>'
        )

    source = category.get("source_url", "")
    source_link = (
        f'<a href="{escape_attr(source)}" target="_blank" rel="noopener">Klaviyo source category</a>'
        if source else ""
    )

    return f"""
<style>
.wp-block-post-title,.betterdocs-social-share,.betterdocs-article-reactions,.betterdocs-entry-footer,.betterdocs-feedback-form,.betterdocs-article-reactions-heading,.betterdocs-toc,.betterdocs-toc-wrapper,.batterdocs-anchor{{display:none!important}}
.dc-category-page{{max-width:980px;margin:0;padding:0 0 28px;color:#1f2933;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.dc-category-hero{{display:none}}
.dc-category-meta{{display:none}}
.dc-section-grid{{display:grid;grid-template-columns:repeat(3,minmax(220px,1fr));gap:20px 24px;margin-top:0}}
.dc-section-grid>br{{display:none!important}}
.dc-section-card{{min-height:118px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:20px 18px;background:#fff;border:1px solid #f0f0ee;border-radius:8px;box-shadow:0 10px 22px rgba(15,23,42,.08);text-decoration:none;color:#202124;transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease}}
.dc-section-card:hover{{transform:translateY(-2px);box-shadow:0 14px 28px rgba(15,23,42,.11);border-color:#deded8;color:#111827}}
.dc-card-title{{font-size:20px;line-height:1.25;text-align:center;font-weight:400}}
.dc-card-count{{font-size:16px;line-height:1.35;text-align:center;color:#202124}}
@media(max-width:900px){{.dc-section-grid{{grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}}}}
@media(max-width:560px){{.dc-category-page{{padding:4px 0 28px}}.dc-section-grid{{grid-template-columns:1fr;gap:14px}}.dc-section-card{{min-height:104px}}}}
</style>
<div class="dc-category-page">
  <main class="dc-section-grid" aria-label="Category sections">
    {"".join(cards)}
  </main>
</div>
""".strip()


def cmd_upload_category_preview(category_slug: str = "customer-agent"):
    logger = SyncLogger("Upload category preview")
    relationships = load_json(RELATIONS_DIR / "category-articles.json")
    if not relationships:
        print("  Missing relationships. Building from local cache first...")
        cmd_relationships()
        relationships = load_json(RELATIONS_DIR / "category-articles.json")

    category = next((item for item in relationships if item.get("category_slug") == category_slug), None)
    if not category:
        available = ", ".join(item.get("category_slug", "") for item in relationships)
        raise RuntimeError(f"Category slug not found: {category_slug}. Available: {available}")
    if not SOURCE_TO_LOCAL_URL_MAP.exists():
        cmd_prepare_url_maps()

    title = category["category_name"]
    slug = category_doc_slug(category)
    html_content = category_page_html(category)
    preview_dir = PROJECT_ROOT / "build" / "previews"
    preview_dir.mkdir(parents=True, exist_ok=True)
    (preview_dir / f"{slug}.html").write_text(html_content, "utf-8")

    wp = WordPressClient()
    meta = load_json(CATEGORY_PREVIEW_META)
    homepage_uploads = load_json(HOMEPAGE_CATEGORY_UPLOAD_META)
    homepage_match = next(
        (
            item for item in homepage_uploads.values()
            if id_text(item.get("source_category_id")) == id_text(category.get("category_id"))
            or item.get("local_category_slug") == category.get("category_slug")
        ),
        {},
    )
    stored = meta.get(category["category_slug"], {})
    stored_wp_id = homepage_match.get("wp_id") or stored.get("wp_id")
    if stored_wp_id:
        result = wp.update_doc(
            stored_wp_id,
            title=title,
            content=html_content,
            category_slug=category["category_slug"],
            slug=slug,
        )
        action = "updated"
    else:
        existing = wp.find_doc_by_title(title)
        if existing:
            result = wp.update_doc(
                existing["id"],
                title=title,
                content=html_content,
                category_slug=category["category_slug"],
            )
            action = "updated"
        else:
            result = wp.create_doc(
                title=title,
                content=html_content,
                category_slug=category["category_slug"],
                slug=slug,
            )
            action = "created"

    if not result:
        raise RuntimeError(f"Failed to upload category preview: {category['category_name']}")

    meta[category["category_slug"]] = {
        "category_id": category.get("category_id", ""),
        "category_name": category.get("category_name", ""),
        "category_slug": category.get("category_slug", ""),
        "wp_id": result.get("id"),
        "slug": result.get("slug", slug),
        "link": result.get("link", ""),
        "action": action,
        "uploaded_at": utc_now(),
        "section_count": len({id_text(a.get("section_id")) for a in category.get("articles", [])}),
        "article_count": len(category.get("articles", [])),
        "local_preview": str((preview_dir / f"{slug}.html").relative_to(PROJECT_ROOT)),
    }
    save_json(CATEGORY_PREVIEW_META, meta)
    logger.ok(f"{title} -> {action} WP #{result.get('id')} {result.get('link', '')}")
    logger.summary()
    print(f"  Preview URL: {result.get('link', '')}")
    print(f"  Local HTML: {preview_dir / f'{slug}.html'}")


# ============================================================
# Section preview upload
# ============================================================

def section_doc_slug(section: dict) -> str:
    category = slugify(section.get("category_slug", "category"))
    name = slugify(section.get("section_name", "section"))
    return f"sections-{category}-{name}"


def find_section_preview(source: str, sections: list[dict]) -> dict | None:
    source = (source or "").strip()
    if not source:
        source = "customer-agent/guidance"
    if source.isdigit():
        return next((item for item in sections if id_text(item.get("section_id")) == source), None)
    normalized = slugify(source.replace("/", " "))
    for item in sections:
        candidates = {
            slugify(item.get("section_name", "")),
            f'{slugify(item.get("category_slug", ""))}-{slugify(item.get("section_name", ""))}',
            f'{slugify(item.get("category_slug", ""))}-{slugify(item.get("section_path", ""))}',
        }
        if normalized in candidates:
            return item
    return None


def section_articles_with_descendants(section: dict, all_sections: list[dict]) -> list[dict]:
    section_id = id_text(section.get("section_id"))
    articles = []
    seen = set()
    for item in all_sections:
        path_ids = {id_text(path.get("section_id")) for path in item.get("path", [])}
        if id_text(item.get("section_id")) == section_id or section_id in path_ids:
            for article in item.get("articles", []):
                article_id = id_text(article.get("article_id"))
                if article_id and article_id not in seen:
                    seen.add(article_id)
                    articles.append(article)
    if not articles:
        return section.get("articles", [])
    return articles


def section_page_html(section: dict, all_sections: list[dict] | None = None) -> str:
    lookup = load_json(SOURCE_TO_LOCAL_URL_MAP).get("lookup", {})
    article_source = (
        section_articles_with_descendants(section, all_sections)
        if all_sections is not None else section.get("articles", [])
    )
    articles = sorted(article_source, key=lambda item: item.get("title", ""))
    items = []

    def article_excerpt(article: dict) -> str:
        snapshot = article.get("source_snapshot", "")
        if not snapshot:
            return ""
        path = KLAVIYO_EN_DIR / snapshot
        if not path.exists():
            return ""
        try:
            data = load_json(path)
            body = data.get("article", {}).get("body", "") or ""
            soup = BeautifulSoup(body, "html.parser")
            for tag in soup.find_all(["script", "style", "img", "iframe"]):
                tag.decompose()
            for p in soup.find_all(["p", "div"]):
                text = re.sub(r"\s+", " ", p.get_text(" ", strip=True)).strip()
                if len(text) >= 80:
                    return text[:360]
        except Exception:
            return ""
        return ""

    for article in articles:
        link = local_url_for_source(article.get("source_url", ""), lookup) or article_preview_link(article)
        excerpt = article_excerpt(article)
        excerpt_html = f'<p>{html.escape(excerpt)}</p>' if excerpt else ""
        items.append(
            '<li>'
            f'<a href="{escape_attr(link)}">{html.escape(article.get("title", ""))}</a>'
            f'{excerpt_html}'
            '</li>'
        )

    title_text = section.get("section_name", "")

    return f"""
<style>
.betterdocs-social-share,.betterdocs-article-reactions,.betterdocs-entry-footer,.betterdocs-feedback-form,.betterdocs-article-reactions-heading,.betterdocs-toc,.betterdocs-toc-wrapper,.batterdocs-anchor{{display:none!important}}
.dc-section-page{{max-width:860px;margin:0;padding:0 0 34px;color:#242424;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.dc-section-list{{list-style:none;margin:0;padding:0}}
.dc-section-list>br{{display:none!important}}
.dc-section-list li{{margin:0 0 32px;padding:0}}
.dc-section-list li:last-child{{margin-bottom:0}}
.dc-section-list a{{display:inline;color:#242424;font-size:18px;line-height:1.45;text-decoration:underline;text-underline-offset:3px}}
.dc-section-list a:hover{{color:#0f766e}}
.dc-section-list p{{max-width:820px;margin:6px 0 0;color:#343434;font-size:14px;line-height:1.55}}
@media(max-width:760px){{.dc-section-list li{{margin-bottom:24px}}}}
</style>
<div class="dc-section-page">
  <ul class="dc-section-list" aria-label="{escape_attr(title_text)} articles">
    {"".join(items)}
  </ul>
</div>
""".strip()


def cmd_upload_section_preview(section_source: str = "customer-agent/guidance"):
    logger = SyncLogger("Upload section preview")
    sections = load_json(RELATIONS_DIR / "sections-articles.json")
    if not sections:
        print("  Missing relationships. Building from local cache first...")
        cmd_relationships()
        sections = load_json(RELATIONS_DIR / "sections-articles.json")

    section = find_section_preview(section_source, sections)
    if not section:
        raise RuntimeError(f"Section not found: {section_source}")
    if not SOURCE_TO_LOCAL_URL_MAP.exists():
        cmd_prepare_url_maps()

    title = section["section_name"]
    slug = section_doc_slug(section)
    html_content = section_page_html(section, sections)
    preview_dir = PROJECT_ROOT / "build" / "previews" / "sections"
    preview_dir.mkdir(parents=True, exist_ok=True)
    (preview_dir / f"{slug}.html").write_text(html_content, "utf-8")

    wp = WordPressClient()
    meta = load_json(SECTION_PREVIEW_META)
    stored = meta.get(id_text(section.get("section_id")), {})
    stored_wp_id = stored.get("wp_id")
    if stored_wp_id:
        result = wp.update_doc(
            stored_wp_id,
            title=title,
            content=html_content,
            category_slug=section.get("category_slug", ""),
        )
        action = "updated"
    else:
        existing = wp.find_doc_by_slug(slug) or wp.find_doc_by_title(title)
        if existing:
            result = wp.update_doc(
                existing["id"],
                title=title,
                content=html_content,
                category_slug=section.get("category_slug", ""),
            )
            action = "updated"
        else:
            result = wp.create_doc(
                title=title,
                content=html_content,
                category_slug=section.get("category_slug", ""),
                slug=slug,
            )
            action = "created"

    if not result:
        raise RuntimeError(f"Failed to upload section preview: {title}")

    meta[id_text(section.get("section_id"))] = {
        "section_id": id_text(section.get("section_id")),
        "section_name": section.get("section_name", ""),
        "category_slug": section.get("category_slug", ""),
        "category_name": section.get("category_name", ""),
        "wp_id": result.get("id"),
        "slug": result.get("slug", slug),
        "link": result.get("link", ""),
        "action": action,
        "uploaded_at": utc_now(),
        "article_count": len(section_articles_with_descendants(section, sections)),
        "local_preview": str((preview_dir / f"{slug}.html").relative_to(PROJECT_ROOT)),
    }
    save_json(SECTION_PREVIEW_META, meta)
    logger.ok(f"{title} -> {action} WP #{result.get('id')} {result.get('link', '')}")
    logger.summary()
    print(f"  Preview URL: {result.get('link', '')}")
    print(f"  Local HTML: {preview_dir / f'{slug}.html'}")


def cmd_upload_all_section_previews(limit: int | None = None):
    logger = SyncLogger("Upload all section previews")
    sections = load_json(RELATIONS_DIR / "sections-articles.json")
    if not sections:
        print("  Missing relationships. Building from local cache first...")
        cmd_relationships()
        sections = load_json(RELATIONS_DIR / "sections-articles.json")
    if not SOURCE_TO_LOCAL_URL_MAP.exists():
        cmd_prepare_url_maps()

    preview_dir = PROJECT_ROOT / "build" / "previews" / "sections"
    preview_dir.mkdir(parents=True, exist_ok=True)
    wp = WordPressClient()
    meta = load_json(SECTION_PREVIEW_META)
    selected = sections[:limit] if limit else sections

    for section in selected:
        article_count = len(section_articles_with_descendants(section, sections))
        if article_count == 0:
            logger.skip(f"{section.get('section_name', '')}: no articles")
            continue

        title = section["section_name"]
        slug = section_doc_slug(section)
        html_content = section_page_html(section, sections)
        (preview_dir / f"{slug}.html").write_text(html_content, "utf-8")
        stored = meta.get(id_text(section.get("section_id")), {})
        try:
            if stored.get("wp_id"):
                result = wp.update_doc(
                    stored["wp_id"],
                    title=title,
                    content=html_content,
                    category_slug=section.get("category_slug", ""),
                    slug=slug,
                )
                action = "updated"
            else:
                existing = wp.find_doc_by_slug(slug)
                if existing:
                    result = wp.update_doc(
                        existing["id"],
                        title=title,
                        content=html_content,
                        category_slug=section.get("category_slug", ""),
                        slug=slug,
                    )
                    action = "updated"
                else:
                    result = wp.create_doc(
                        title=title,
                        content=html_content,
                        category_slug=section.get("category_slug", ""),
                        slug=slug,
                    )
                    action = "created"

            meta[id_text(section.get("section_id"))] = {
                "section_id": id_text(section.get("section_id")),
                "section_name": section.get("section_name", ""),
                "category_slug": section.get("category_slug", ""),
                "category_name": section.get("category_name", ""),
                "wp_id": result.get("id"),
                "slug": result.get("slug", slug),
                "link": result.get("link", ""),
                "action": action,
                "uploaded_at": utc_now(),
                "article_count": article_count,
                "local_preview": str((preview_dir / f"{slug}.html").relative_to(PROJECT_ROOT)),
            }
            save_json(SECTION_PREVIEW_META, meta)
            logger.ok(f"{section.get('category_slug', '')}/{title} -> {action} {result.get('link', '')}")
            time.sleep(0.12)
        except Exception as exc:
            logger.fail(f"{section.get('category_slug', '')}/{title}: {exc}")
            save_json(SECTION_PREVIEW_META, meta)

    logger.summary()
    print(f"  Upload meta: {SECTION_PREVIEW_META}")


# ============================================================
# Single category sync orchestration
# ============================================================

def find_category_sync_target(source: str) -> tuple[dict, dict, list[dict]]:
    source = (source or "customer-agent").strip()
    menu_items = load_homepage_category_menu()
    category_relations = load_json(RELATIONS_DIR / "category-articles.json")
    section_relations = load_json(RELATIONS_DIR / "sections-articles.json")
    if not category_relations:
        cmd_relationships()
        category_relations = load_json(RELATIONS_DIR / "category-articles.json")
        section_relations = load_json(RELATIONS_DIR / "sections-articles.json")

    category_id = ""
    match = re.search(r"/categories/(\d+)", source)
    if match:
        category_id = match.group(1)

    normalized = slugify(source)
    menu_item = None
    for item in menu_items:
        candidates = {
            id_text(item.get("source_category_id")),
            item.get("menu_slug", ""),
            item.get("local_category_slug", ""),
            slugify(item.get("menu_name", "")),
            slugify(item.get("menu_name_zh", "")),
        }
        if category_id and id_text(item.get("source_category_id")) == category_id:
            menu_item = item
            break
        if normalized in {slugify(value) for value in candidates if value}:
            menu_item = item
            break

    relation = None
    if menu_item:
        category_id = id_text(menu_item.get("source_category_id"))
    for item in category_relations:
        if category_id and id_text(item.get("category_id")) == category_id:
            relation = item
            break
        if normalized in {slugify(item.get("category_slug", "")), slugify(item.get("category_name", ""))}:
            relation = item
            break

    if not relation and menu_item:
        relation = {
            "category_id": id_text(menu_item.get("source_category_id")),
            "category_name": menu_item.get("menu_name", ""),
            "category_slug": menu_item.get("menu_slug", ""),
            "wp_category_id": load_category_map().get(menu_item.get("menu_slug", "")),
            "source_url": menu_item.get("source_url", ""),
            "position": menu_item.get("position"),
            "article_count": 0,
            "articles": [],
        }

    if not relation:
        available = ", ".join(item.get("menu_slug", "") for item in menu_items)
        raise RuntimeError(f"Category not found: {source}. Available menu slugs: {available}")

    if not menu_item:
        menu_item = {
            "menu_slug": relation.get("category_slug", ""),
            "menu_name": relation.get("category_name", ""),
            "menu_name_zh": MENU_CATEGORY_ZH.get(relation.get("category_slug", ""), relation.get("category_name", "")),
            "source_category_id": relation.get("category_id", ""),
            "source_url": relation.get("source_url", ""),
            "wp_doc_slug": category_doc_slug(relation),
            "wp_doc_url": wp_doc_url(category_doc_slug(relation)),
        }

    sections = [
        section for section in section_relations
        if id_text(section.get("category_id")) == id_text(relation.get("category_id"))
    ]
    sections.sort(key=lambda item: (item.get("path_text", ""), item.get("section_name", "")))
    return menu_item, relation, sections


def category_sync_report_path(category_slug: str) -> Path:
    path = SOURCE_DIR / "plans"
    path.mkdir(parents=True, exist_ok=True)
    return path / f"{category_slug}-chain-sync-report.json"


def cmd_sync_category(source: str = "customer-agent", dry_run: bool = True, force: bool = False, prepared: bool = False):
    """Sync one Klaviyo category as a closed category -> sections -> articles workflow."""
    logger = SyncLogger("Sync single category")
    if not prepared:
        cmd_ensure_category_tree()
        cmd_relationships()

    menu_item, category, sections = find_category_sync_target(source)
    translate_meta = load_json(TRANSLATE_META).get("translated", {})
    upload_meta = load_json(UPLOAD_META).get("uploaded", {})
    section_uploads = load_json(SECTION_PREVIEW_META)
    category_uploads = load_json(CATEGORY_PREVIEW_META)
    homepage_category_uploads = load_json(HOMEPAGE_CATEGORY_UPLOAD_META)

    articles = category.get("articles", [])
    article_ids = [id_text(article.get("article_id")) for article in articles if id_text(article.get("article_id"))]
    missing_translations = [aid for aid in article_ids if aid not in translate_meta]
    missing_uploads = [aid for aid in article_ids if aid not in upload_meta]
    uploaded_sections = [
        section for section in sections
        if id_text(section.get("section_id")) in section_uploads
    ]
    report_path = category_sync_report_path(category.get("category_slug", "category"))

    print("=" * 72)
    print("Single Category Chain Sync")
    print("=" * 72)
    print(f"Source:       {source}")
    print(f"Category:     {category.get('category_name')} ({category.get('category_slug')})")
    print(f"Source URL:   {menu_item.get('source_url') or category.get('source_url')}")
    print(f"WP URL:       {homepage_category_uploads.get(menu_item.get('menu_slug', ''), {}).get('wp_link') or category_uploads.get(category.get('category_slug', ''), {}).get('link') or wp_doc_url(menu_item.get('wp_doc_slug') or category_doc_slug(category))}")
    print(f"Sections:     {len(sections)}")
    print(f"Articles:     {len(article_ids)}")
    print(f"Translated:   {len(article_ids) - len(missing_translations)}/{len(article_ids)}")
    print(f"Uploaded:     {len(article_ids) - len(missing_uploads)}/{len(article_ids)}")
    print(f"Section docs: {len(uploaded_sections)}/{len(sections)}")
    print(f"Force article upload: {force}")

    if dry_run:
        print("\nDRY-RUN only. No WordPress writes will be made.")
        print("\nExecution order:")
        print("  1. Ensure BetterDocs 20-child category tree")
        print("  2. Upload/update translated articles in this category")
        print("  3. Upload/update every section page in this category, including parent sections")
        print("  4. Refresh URL maps and verify cached internal links")
        print("  5. Upload/update category page again so cards point to section pages")
        print("  6. Normalize parent category assignments")
        print("\nSections:")
        for section in sections:
            sid = id_text(section.get("section_id"))
            status = "uploaded" if sid in section_uploads else "will create/update"
            article_count = len(section_articles_with_descendants(section, sections))
            print(f"  - {sid} | {section.get('path_text') or section.get('section_name')} | {article_count} articles incl. descendants | {status}")
        print("\nArticle sample:")
        for article in articles[:10]:
            aid = id_text(article.get("article_id"))
            tr = "translated" if aid in translate_meta else "missing-translation"
            up = "uploaded" if aid in upload_meta else "missing-upload"
            print(f"  - {aid} | {article.get('title')} | {tr} | {up}")
        if len(articles) > 10:
            print(f"  ... {len(articles) - 10} more articles")
        save_json(report_path, {
            "generated_at": utc_now(),
            "dry_run": True,
            "source": source,
            "category": {
                "category_id": category.get("category_id"),
                "category_name": category.get("category_name"),
                "category_slug": category.get("category_slug"),
                "source_url": menu_item.get("source_url") or category.get("source_url"),
            },
            "section_count": len(sections),
            "article_count": len(article_ids),
            "translated_count": len(article_ids) - len(missing_translations),
            "uploaded_count": len(article_ids) - len(missing_uploads),
            "missing_translations": missing_translations,
            "missing_uploads": missing_uploads,
        })
        logger.ok("dry-run completed")
        logger.summary()
        print(f"  Report: {report_path}")
        return

    if missing_translations:
        raise RuntimeError(
            f"Missing translations for {len(missing_translations)} articles. "
            "Run translation first or add category-scoped translation before real upload."
        )

    # First ensure article docs exist or refresh them; section pages link to article pages.
    cmd_upload(force=force, only_ids=article_ids)

    # Refresh article URL maps before section pages, then sync category-scoped sections.
    cmd_prepare_url_maps()
    for section in sections:
        cmd_upload_section_preview(id_text(section.get("section_id")))

    # Refresh section URL maps before the category page, then sync the category page.
    cmd_prepare_url_maps()
    cmd_upload_homepage_categories(menu_item.get("menu_slug") or category.get("category_slug", ""))
    cmd_prepare_url_maps()
    cmd_verify_url_maps()
    cmd_clean_parent_category(dry_run=False)

    final_section_uploads = load_json(SECTION_PREVIEW_META)
    final_upload_meta = load_json(UPLOAD_META).get("uploaded", {})
    category_uploads = load_json(HOMEPAGE_CATEGORY_UPLOAD_META)
    save_json(report_path, {
        "generated_at": utc_now(),
        "dry_run": False,
        "source": source,
        "category": {
            "category_id": category.get("category_id"),
            "category_name": category.get("category_name"),
            "category_slug": category.get("category_slug"),
            "source_url": menu_item.get("source_url") or category.get("source_url"),
            "wp_url": category_uploads.get(menu_item.get("menu_slug", ""), {}).get("wp_link", ""),
        },
        "section_count": len(sections),
        "section_uploaded_count": sum(1 for section in sections if id_text(section.get("section_id")) in final_section_uploads),
        "article_count": len(article_ids),
        "article_uploaded_count": sum(1 for aid in article_ids if aid in final_upload_meta),
        "missing_translations": missing_translations,
    })
    logger.ok("category sync completed")
    logger.summary()
    print(f"  Report: {report_path}")


def cmd_sync_all_categories(dry_run: bool = True, force: bool = False, continue_on_missing: bool = False):
    """Run the closed sync workflow category by category."""
    logger = SyncLogger("Sync all categories")
    cmd_ensure_category_tree()
    cmd_relationships()
    menu_items = [item for item in load_homepage_category_menu() if item.get("source_category_id")]
    reports = []
    for item in menu_items:
        slug = item.get("menu_slug", "")
        print("\n" + "#" * 72)
        print(f"# Sync category: {slug}")
        print("#" * 72)
        try:
            cmd_sync_category(slug, dry_run=dry_run, force=force, prepared=True)
            reports.append({
                "category_slug": slug,
                "status": "ok",
                "report": str(category_sync_report_path(slug)),
            })
            logger.ok(slug)
        except RuntimeError as exc:
            message = str(exc)
            if "Missing translations" in message and continue_on_missing:
                reports.append({
                    "category_slug": slug,
                    "status": "skipped_missing_translations",
                    "error": message,
                })
                logger.skip(f"{slug}: {message}")
                print(f"  [SKIP] {slug}: {message}")
                continue
            reports.append({
                "category_slug": slug,
                "status": "failed",
                "error": message,
            })
            logger.fail(f"{slug}: {message}")
            if not continue_on_missing:
                break
        except Exception as exc:
            message = str(exc)
            reports.append({
                "category_slug": slug,
                "status": "failed",
                "error": message,
            })
            logger.fail(f"{slug}: {message}")
            if not continue_on_missing:
                break

    report_path = SOURCE_DIR / "plans" / "all-category-chain-sync-report.json"
    save_json(report_path, {
        "generated_at": utc_now(),
        "dry_run": dry_run,
        "force": force,
        "continue_on_missing": continue_on_missing,
        "items": reports,
        "logger": logger.results,
    })
    logger.summary()
    print(f"  Report: {report_path}")


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
    "crawl-article": cmd_crawl_article,
    "translate": cmd_translate,
    "upload": cmd_upload,
    "full": cmd_full,
    "status": cmd_status,
    "relationships": cmd_relationships,
    "ensure-category-tree": cmd_ensure_category_tree,
    "clean-parent-category": cmd_clean_parent_category,
    "prepare-url-maps": cmd_prepare_url_maps,
    "verify-url-maps": cmd_verify_url_maps,
    "resolve-redirect-links": cmd_resolve_redirect_links,
    "crawl-homepage-categories": cmd_crawl_homepage_categories,
    "upload-homepage-categories": cmd_upload_homepage_categories,
    "upload-category-preview": cmd_upload_category_preview,
    "upload-section-preview": cmd_upload_section_preview,
    "upload-all-section-previews": cmd_upload_all_section_previews,
    "sync-category": cmd_sync_category,
    "sync-all-categories": cmd_sync_all_categories,
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1].lower()
    if cmd not in COMMANDS:
        print(f"Unknown: {cmd}. Available: {', '.join(COMMANDS.keys())}")
        sys.exit(1)

    if cmd == "crawl-article":
        if len(sys.argv) < 3:
            print("Usage: python3 sync/pipeline.py crawl-article <klaviyo_article_url_or_id>")
            sys.exit(1)
        COMMANDS[cmd](sys.argv[2])
    elif cmd == "upload":
        dry_run = "--dry-run" in sys.argv[2:]
        force = "--force" in sys.argv[2:]
        limit = None
        only_ids = []
        if "--limit" in sys.argv[2:]:
            i = sys.argv.index("--limit")
            if i + 1 < len(sys.argv):
                limit = int(sys.argv[i + 1])
        if "--ids" in sys.argv[2:]:
            i = sys.argv.index("--ids")
            if i + 1 < len(sys.argv):
                only_ids = [value.strip() for value in sys.argv[i + 1].split(",") if value.strip()]
        COMMANDS[cmd](dry_run=dry_run, limit=limit, force=force, only_ids=only_ids)
    elif cmd == "upload-category-preview":
        category_slug = sys.argv[2] if len(sys.argv) > 2 else "customer-agent"
        COMMANDS[cmd](category_slug)
    elif cmd == "upload-section-preview":
        section_source = sys.argv[2] if len(sys.argv) > 2 else "customer-agent/guidance"
        COMMANDS[cmd](section_source)
    elif cmd == "upload-homepage-categories":
        category_slug = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else ""
        COMMANDS[cmd](category_slug)
    elif cmd == "upload-all-section-previews":
        limit = None
        if "--limit" in sys.argv[2:]:
            i = sys.argv.index("--limit")
            if i + 1 < len(sys.argv):
                limit = int(sys.argv[i + 1])
        COMMANDS[cmd](limit=limit)
    elif cmd == "sync-category":
        source = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else "customer-agent"
        dry_run = "--dry-run" in sys.argv[2:]
        force = "--force" in sys.argv[2:]
        COMMANDS[cmd](source, dry_run=dry_run, force=force)
    elif cmd == "sync-all-categories":
        dry_run = "--dry-run" in sys.argv[2:]
        force = "--force" in sys.argv[2:]
        continue_on_missing = "--continue-on-missing" in sys.argv[2:]
        COMMANDS[cmd](dry_run=dry_run, force=force, continue_on_missing=continue_on_missing)
    elif cmd == "clean-parent-category":
        dry_run = "--dry-run" in sys.argv[2:]
        limit = None
        if "--limit" in sys.argv[2:]:
            i = sys.argv.index("--limit")
            if i + 1 < len(sys.argv):
                limit = int(sys.argv[i + 1])
        COMMANDS[cmd](dry_run=dry_run, limit=limit)
    else:
        COMMANDS[cmd]()
