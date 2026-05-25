#!/usr/bin/env python3
"""Build local docs/section structure previews and styled article HTML.

This tool is intentionally local-first. It does not upload content to
WordPress. Use it to review the directory model, section model, and article
rendering before enabling any remote upload workflow.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import requests

from core import (
    KLAVIYO_CATEGORY_MAP,
    KLAVIYO_CN_DIR,
    KLAVIYO_EN_DIR,
    PROJECT_ROOT,
    ZENDESK_API,
    load_json,
    parse_frontmatter,
    save_json,
    sanitize_filename,
)


BUILD_DIR = PROJECT_ROOT / "build" / "previews"
BATTERDOCS_META = PROJECT_ROOT / "batterDocs" / ".sync_meta.json"
SECTIONS_META = KLAVIYO_EN_DIR / ".sections_meta.json"
SECTION_INDEX = KLAVIYO_CN_DIR / ".sections_index.json"

ZH_CATEGORY_NAMES = {
    "account-billing": "账户与计费",
    "advanced-kdp-marketing-analytics": "核心数据与分析",
    "analytics-audience": "数据与受众",
    "campaigns": "活动与营销",
    "content": "内容与创意",
    "conversations": "会话与沟通",
    "customer-agent": "客户 Agent",
    "customer-hub": "自助客户中心",
    "deliverability-compliance": "投递与合规",
    "flows": "自动化与生命周期",
    "helpdesk": "帮助台",
    "integrations": "集成",
    "reviews": "评论与评价",
    "sign-up-forms": "注册表单与渠道",
    "sms-whatsapp": "短信与 WhatsApp",
}


@dataclass
class Article:
    article_id: str
    title: str
    filename: str
    category_slug: str
    section: str
    source_url: str
    body: str


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[\s_]+", "-", value)
    return value.strip("-") or "section"


def escape_attr(value: str) -> str:
    return html.escape(value, quote=True)


def inline_md(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{escape_attr(m.group(2))}">{m.group(1)}</a>', text)
    return text


def table_to_html(rows: list[str]) -> str:
    parsed = []
    for row in rows:
        cells = [inline_md(c.strip()) for c in row.strip().strip("|").split("|")]
        parsed.append(cells)
    if len(parsed) < 2:
        return "\n".join(f"<p>{inline_md(r)}</p>" for r in rows)
    head = parsed[0]
    body = parsed[2:] if re.match(r"^\s*\|?\s*:?-{3,}", rows[1]) else parsed[1:]
    thead = "".join(f"<th>{c}</th>" for c in head)
    tbody = "\n".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in body)
    return f'<div class="dc-table-wrap"><table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table></div>'


def article_to_html(md: str, *, include_wrapper: bool = True) -> str:
    """Convert existing translated markdown into a styled BetterDocs body."""
    if md.lstrip().startswith("<"):
        return md.strip()

    lines = md.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None
    in_code = False
    code_lines: list[str] = []
    table_lines: list[str] = []

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{inline_md(' '.join(x.strip() for x in paragraph))}</p>")
            paragraph = []

    def flush_list():
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    def flush_table():
        nonlocal table_lines
        if table_lines:
            out.append(table_to_html(table_lines))
            table_lines = []

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if stripped.startswith("```") or stripped.startswith("````"):
            flush_paragraph()
            flush_list()
            flush_table()
            if in_code:
                out.append(f'<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>')
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue

        if not stripped:
            flush_paragraph()
            flush_list()
            flush_table()
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph()
            flush_list()
            table_lines.append(stripped)
            continue
        flush_table()

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            flush_list()
            level = min(len(heading.group(1)), 4)
            title = re.sub(r"\*+", "", heading.group(2)).strip()
            anchor = slugify(title)
            out.append(f'<h{level} id="{anchor}">{inline_md(title)}</h{level}>')
            continue

        image = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if image:
            flush_paragraph()
            flush_list()
            alt, src = image.groups()
            caption = alt or "Klaviyo help center screenshot"
            out.append(
                '<figure class="dc-doc-figure">'
                f'<img src="{escape_attr(src)}" alt="{escape_attr(caption)}" loading="lazy">'
                f"<figcaption>{html.escape(caption)}</figcaption>"
                "</figure>"
            )
            continue

        bullet = re.match(r"^[-*]\s+(.+)$", stripped)
        ordered = re.match(r"^\d+\.\s+(.+)$", stripped)
        if bullet or ordered:
            flush_paragraph()
            wanted = "ul" if bullet else "ol"
            if list_type != wanted:
                flush_list()
                out.append(f"<{wanted}>")
                list_type = wanted
            item = (bullet or ordered).group(1)
            out.append(f"<li>{inline_md(item)}</li>")
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            flush_list()
            out.append(f'<aside class="dc-note">{inline_md(stripped.lstrip("> "))}</aside>')
            continue

        paragraph.append(stripped)

    flush_paragraph()
    flush_list()
    flush_table()
    if in_code:
        out.append(f'<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>')

    body = "\n".join(out)
    if not include_wrapper:
        return body

    return f'<article class="dc-help-article">\n{body}\n</article>'


def preview_css() -> str:
    return """
body{margin:0;background:#f8fafc;color:#172033;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
a{color:#111827;text-decoration:underline;text-underline-offset:3px}
.dc-shell{max-width:1240px;margin:0 auto;padding:36px 24px}
.dc-layout{display:grid;grid-template-columns:280px minmax(0,1fr);gap:32px;align-items:start}
.dc-sidebar{position:sticky;top:24px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:16px}
.dc-sidebar a{display:block;padding:9px 10px;border-radius:8px;color:#475569;text-decoration:none}
.dc-sidebar a:hover{background:#f1f5f9;color:#0f172a}
.dc-panel{background:#fff;border:1px solid #e5e7eb;border-radius:14px;padding:26px}
.dc-category{padding:24px 0;border-top:1px solid #e5e7eb}
.dc-category:first-child{border-top:0;padding-top:0}
.dc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
.dc-card{border:1px solid #e5e7eb;border-radius:10px;padding:15px 16px;background:#fff}
.dc-muted{color:#64748b;font-size:14px}
.dc-help-article{max-width:820px;font-size:16px;line-height:1.75}
.dc-help-article h1,.dc-help-article h2,.dc-help-article h3,.dc-help-article h4{color:#111827;line-height:1.35}
.dc-help-article h2{font-size:24px;margin:32px 0 14px;padding-bottom:8px;border-bottom:1px solid #e5e7eb}
.dc-help-article h3{font-size:19px;margin:24px 0 10px}
.dc-help-article p{margin:0 0 16px}
.dc-help-article ul,.dc-help-article ol{padding-left:24px;margin:0 0 18px}
.dc-help-article li{margin:6px 0}
.dc-doc-figure{margin:22px 0;border:1px solid #e5e7eb;border-radius:12px;overflow:hidden;background:#fff}
.dc-doc-figure img{display:block;width:100%;height:auto}
.dc-doc-figure figcaption{font-size:14px;color:#64748b;background:#f8fafc;border-top:1px solid #e5e7eb;padding:11px 14px}
.dc-note{border-left:4px solid #334155;background:#f8fafc;border-radius:8px;padding:14px 16px;margin:18px 0}
.dc-table-wrap{overflow-x:auto;margin:20px 0;border:1px solid #e5e7eb;border-radius:10px}
table{width:100%;border-collapse:collapse;background:#fff}
th,td{padding:10px 12px;border-bottom:1px solid #e5e7eb;text-align:left;vertical-align:top}
th{background:#f8fafc;color:#111827}
pre{background:#111827;color:#f8fafc;border-radius:10px;padding:16px;overflow:auto}
code{background:#f1f5f9;border-radius:4px;padding:2px 5px}
pre code{background:transparent;padding:0}
@media(max-width:860px){.dc-layout{grid-template-columns:1fr}.dc-sidebar{position:static}}
"""


def read_articles(base: Path) -> list[Article]:
    articles: list[Article] = []
    for path in sorted(base.glob("*/*.md")):
        content = path.read_text("utf-8", errors="ignore")
        fm, body = parse_frontmatter(content)
        if not fm:
            continue
        articles.append(
            Article(
                article_id=str(fm.get("id", "")),
                title=fm.get("title", path.stem),
                filename=str(path.relative_to(base)),
                category_slug=fm.get("category_slug", path.parent.name),
                section=fm.get("section", "Other") or "Other",
                source_url=fm.get("source_url", ""),
                body=body,
            )
        )
    return articles


def sync_sections() -> dict:
    sections: dict[str, dict] = {}
    page = 1
    while True:
        resp = requests.get(
            f"{ZENDESK_API}/sections.json",
            params={"per_page": 100, "page": page},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        batch = data.get("sections", [])
        for section in batch:
            cat_slug = KLAVIYO_CATEGORY_MAP.get(section.get("category_id"), "uncategorized")
            sections[str(section["id"])] = {
                "id": section["id"],
                "name": section.get("name", ""),
                "slug": slugify(section.get("name", "")),
                "category_id": section.get("category_id"),
                "category_slug": cat_slug,
                "source_url": section.get("html_url", ""),
                "position": section.get("position", 0),
                "parent_section_id": section.get("parent_section_id"),
                "updated_at": section.get("updated_at", ""),
            }
        if len(batch) < 100:
            break
        page += 1
        time.sleep(0.2)

    save_json(SECTIONS_META, {"sections": sections, "synced_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    return sections


def build_section_index() -> dict:
    sections_meta = load_json(SECTIONS_META).get("sections", {})
    cn_articles = read_articles(KLAVIYO_CN_DIR)
    by_name = {(s["category_slug"], s["name"]): s for s in sections_meta.values()}
    index: dict[str, dict] = {}
    for article in cn_articles:
        section = by_name.get((article.category_slug, article.section), {})
        key = f"{article.category_slug}/{slugify(article.section)}"
        item = index.setdefault(
            key,
            {
                "section_id": section.get("id"),
                "section": article.section,
                "section_slug": slugify(article.section),
                "category_slug": article.category_slug,
                "category_name": ZH_CATEGORY_NAMES.get(article.category_slug, article.category_slug),
                "source_url": section.get("source_url", ""),
                "articles": [],
            },
        )
        item["articles"].append(
            {
                "id": article.article_id,
                "title": article.title,
                "filename": article.filename,
                "source_url": article.source_url,
            }
        )
    for item in index.values():
        item["articles"].sort(key=lambda x: x["title"].lower())
    save_json(SECTION_INDEX, {"sections": index, "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    return index


def html_page(title: str, body: str) -> str:
    return f"<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{html.escape(title)}</title><style>{preview_css()}</style></head><body><main class='dc-shell'>{body}</main></body></html>"


def write_batterdocs_preview() -> Path:
    meta = load_json(BATTERDOCS_META)
    docs = list(meta.get("docs", {}).values())
    categories = meta.get("categories", {})
    by_cat: dict[str, list[dict]] = {}
    cat_names: dict[str, str] = {}
    for cat in categories.values():
        cat_names[cat["slug"]] = cat["name"]
    for doc in docs:
        slug = doc["filename"].split("/", 1)[0]
        by_cat.setdefault(slug, []).append(doc)
    for items in by_cat.values():
        items.sort(key=lambda x: x["title"].lower())

    links = "\n".join(f'<a href="#{slugify(slug)}">{html.escape(cat_names.get(slug, slug))} <span class="dc-muted">({len(items)})</span></a>' for slug, items in sorted(by_cat.items()))
    sections = []
    for slug, items in sorted(by_cat.items()):
        cards = "\n".join(f'<div class="dc-card">{html.escape(item["title"])}</div>' for item in items)
        sections.append(f'<section class="dc-category" id="{slugify(slug)}"><h2>{html.escape(cat_names.get(slug, slug))}</h2><div class="dc-grid">{cards}</div></section>')
    body = f"<h1>batterDocs 分类索引预览</h1><div class='dc-layout'><nav class='dc-sidebar'>{links}</nav><div class='dc-panel'>{''.join(sections)}</div></div>"
    out = BUILD_DIR / "batterdocs-index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_page("batterDocs 分类索引预览", body), "utf-8")
    return out


def write_sections_previews(index: dict) -> list[Path]:
    by_cat: dict[str, list[dict]] = {}
    for item in index.values():
        by_cat.setdefault(item["category_slug"], []).append(item)
    for items in by_cat.values():
        items.sort(key=lambda x: x["section"].lower())

    links = "\n".join(f'<a href="#{slugify(cat)}">{html.escape(ZH_CATEGORY_NAMES.get(cat, cat))} <span class="dc-muted">({len(items)})</span></a>' for cat, items in sorted(by_cat.items()))
    blocks = []
    for cat, items in sorted(by_cat.items()):
        cards = []
        for item in items:
            href = f"sections/{item['category_slug']}--{item['section_slug']}.html"
            source = f"<div class='dc-muted'>Klaviyo: {html.escape(item['source_url'])}</div>" if item.get("source_url") else ""
            cards.append(f'<a class="dc-card" href="{href}"><strong>{html.escape(item["section"])}</strong><div class="dc-muted">{len(item["articles"])} articles</div>{source}</a>')
        blocks.append(f'<section class="dc-category" id="{slugify(cat)}"><h2>{html.escape(ZH_CATEGORY_NAMES.get(cat, cat))}</h2><div class="dc-grid">{"".join(cards)}</div></section>')
    body = f"<h1>Klaviyo Sections 索引预览</h1><p class='dc-muted'>按 Klaviyo section 组织中文文档；section 来源同步自 Klaviyo Help Center API。</p><div class='dc-layout'><nav class='dc-sidebar'>{links}</nav><div class='dc-panel'>{''.join(blocks)}</div></div>"
    out = BUILD_DIR / "sections-index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_page("Klaviyo Sections 索引预览", body), "utf-8")

    detail_dir = BUILD_DIR / "sections"
    detail_dir.mkdir(parents=True, exist_ok=True)
    paths = [out]
    for item in sorted(index.values(), key=lambda x: (x["category_slug"], x["section_slug"])):
        anchors = "\n".join(f'<a href="#article-{quote(a["id"] or slugify(a["title"]))}">{html.escape(a["title"])}</a>' for a in item["articles"])
        article_cards = "\n".join(
            f'<section class="dc-category" id="article-{quote(a["id"] or slugify(a["title"]))}"><h2>{html.escape(a["title"])}</h2><p class="dc-muted">{html.escape(a["filename"])}</p></section>'
            for a in item["articles"]
        )
        source = f'<p><a href="{escape_attr(item["source_url"])}">查看 Klaviyo 原 section</a></p>' if item.get("source_url") else ""
        body = f"<h1>{html.escape(item['section'])}</h1><p class='dc-muted'>{html.escape(item['category_name'])} / {len(item['articles'])} articles</p>{source}<div class='dc-layout'><nav class='dc-sidebar'>{anchors}</nav><div class='dc-panel'>{article_cards}</div></div>"
        detail = detail_dir / f"{item['category_slug']}--{item['section_slug']}.html"
        detail.write_text(html_page(item["section"], body), "utf-8")
        paths.append(detail)
    return paths


def write_article_sample(sample: str | None = None) -> Path:
    articles = read_articles(KLAVIYO_CN_DIR)
    article = None
    if sample:
        for candidate in articles:
            if sample in candidate.filename or sample == candidate.article_id:
                article = candidate
                break
    article = article or next((a for a in articles if a.body.strip()), articles[0])
    body = f"<h1>{html.escape(article.title)}</h1>{article_to_html(article.body)}"
    out = BUILD_DIR / "article-sample.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_page(f"Article Sample - {article.title}", body), "utf-8")
    return out


def analyze_articles(limit: int = 20) -> dict:
    articles = read_articles(KLAVIYO_CN_DIR)
    report = {
        "total": len(articles),
        "tables": 0,
        "code_blocks": 0,
        "images": 0,
        "collapsed_numbered_steps": 0,
        "samples": [],
    }
    for article in articles:
        body = article.body
        flags = []
        if re.search(r"^\|.*\|$", body, re.M):
            report["tables"] += 1
            flags.append("table")
        if "```" in body or "````" in body:
            report["code_blocks"] += 1
            flags.append("code")
        if re.search(r"!\[[^\]]*\]\([^)]+\)", body):
            report["images"] += 1
            flags.append("image")
        if re.search(r"\d+\.\s+.+\s+\d+\.\s+", body):
            report["collapsed_numbered_steps"] += 1
            flags.append("collapsed-numbered-steps")
        if flags and len(report["samples"]) < limit:
            report["samples"].append({"filename": article.filename, "title": article.title, "flags": flags})
    return report


def cmd_build(args: argparse.Namespace) -> None:
    if args.sync_sections:
        sections = sync_sections()
        print(f"Synced sections: {len(sections)}")
    index = build_section_index()
    paths = [write_batterdocs_preview(), *write_sections_previews(index), write_article_sample(args.sample)]
    report = analyze_articles()
    report_path = BUILD_DIR / "style-report.json"
    save_json(report_path, report)
    print(f"Sections: {len(index)}")
    print(f"Article style report: {report_path}")
    print("Preview files:")
    for path in paths[:10]:
        print(f"  {path}")
    if len(paths) > 10:
        print(f"  ... {len(paths) - 10} more section detail files")


def cmd_analyze(args: argparse.Namespace) -> None:
    report = analyze_articles(limit=args.limit)
    print(json.dumps(report, indent=2, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build-preview", help="Build local category/section/article previews")
    build.add_argument("--sync-sections", action="store_true", help="Refresh section metadata from Klaviyo API first")
    build.add_argument("--sample", help="Article id or filename substring for article-sample.html")
    build.set_defaults(func=cmd_build)

    analyze = sub.add_parser("analyze-style", help="Report translated markdown structures that need styling")
    analyze.add_argument("--limit", type=int, default=20)
    analyze.set_defaults(func=cmd_analyze)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
