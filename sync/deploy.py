#!/usr/bin/env python3
"""Deploy help center as WordPress Pages (bypassing BetterDocs).

Reads translated content from klaviyo-cn/ and relationship data from
klaviyo-en/_source/ to generate professional HTML pages, then deploys
them as native WordPress Pages under /docs/v2/.

Usage:
    python3 sync/deploy.py init          # Create /docs/v2/ parent page
    python3 sync/deploy.py categories    # Deploy category pages
    python3 sync/deploy.py sections      # Deploy section pages
    python3 sync/deploy.py articles      # Deploy article pages
    python3 sync/deploy.py all           # Full deploy: init + categories + sections + articles
    python3 sync/deploy.py preview       # Generate local HTML previews
    python3 sync/deploy.py status        # Show deployment status
"""

import argparse
import html
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))

from core import (
    KLAVIYO_CN_DIR,
    KLAVIYO_EN_DIR,
    PROJECT_ROOT,
    WP_SITE_URL,
    WP_USERNAME,
    WP_APP_PASSWORD,
    WP_API_BASE,
    load_json,
    save_json,
    parse_frontmatter,
    SyncLogger,
    with_retry,
)
from structure import article_to_html, slugify, escape_attr

# --- Paths ---

SOURCE_DIR = KLAVIYO_EN_DIR / "_source"
RELATIONS_DIR = SOURCE_DIR / "relations"
CATEGORY_ARTICLES_JSON = RELATIONS_DIR / "category-articles.json"
HOMEPAGE_MENU_DIR = SOURCE_DIR / "homepage-menu"
HOMEPAGE_CATEGORY_MENU = HOMEPAGE_MENU_DIR / "category-menu.json"
SECTIONS_ARTICLES_JSON = RELATIONS_DIR / "sections-articles.json"
PREVIEW_DIR = PROJECT_ROOT / "build" / "deploy-previews"
DEPLOY_META = Path(__file__).resolve().parent / ".deploy_meta.json"

# --- Category names (ZH) ---

ZH_CATEGORY_NAMES = {
    "account-billing": "账户与计费",
    "advanced-kdp-marketing-analytics": "核心数据与分析",
    "analytics": "数据与受众",
    "audience": "受众",
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
    "sms": "短信",
    "whatsapp": "WhatsApp",
    "push-notifications": "推送通知",
    "social-marketing": "社交营销",
}

ZH_SECTION_NAMES = {
    "Security": "安全",
    "Account": "账户",
    "API keys": "API 密钥",
    "Billing": "账单",
    "Users": "用户",
    "Getting started": "入门指南",
    "Getting started with analytics": "数据分析入门",
    "Getting started with Klaviyo reporting": "Klaviyo 报告入门",
    "Getting started with flows": "自动化流程入门",
    "Getting started with campaigns": "营销活动入门",
    "Templates": "模板",
    "Build and use templates": "构建和使用模板",
    "Getting started with templates": "模板入门",
    "Design best practices": "设计最佳实践",
    "Advanced template design": "高级模板设计",
    "Template troubleshooting": "模板故障排查",
    "Use variable syntax and tags": "使用变量语法和标签",
    "Coupons": "优惠券",
    "Objects": "对象",
    "Products": "产品",
    "Troubleshooting": "故障排查",
    "Troubleshooting flows": "自动化流程故障排查",
}

CATEGORY_DESCRIPTIONS = {
    "account-billing": "了解账户设置、用户权限、账单、安全验证和组织管理。",
    "advanced-kdp-marketing-analytics": "了解核心数据平台、营销分析和更高级的数据能力。",
    "analytics": "了解报表、指标、归因和受众数据分析。",
    "audience": "了解如何管理客户资料、列表、细分和受众数据。",
    "campaigns": "了解如何创建、发送和优化电子邮件、短信和推送活动。",
    "content": "了解如何创建、管理和优化模板、优惠券、产品和个性化内容。",
    "conversations": "了解如何管理客户会话、消息和沟通工作流。",
    "customer-agent": "了解如何设置和使用客户 Agent 提升客户支持效率。",
    "customer-hub": "了解如何配置自助客户中心和客户账户体验。",
    "deliverability-compliance": "了解投递率、发件人信誉、合规和隐私相关设置。",
    "flows": "了解如何构建自动化流程、触发器、条件和生命周期营销。",
    "helpdesk": "了解如何设置帮助台并管理客户支持请求。",
    "integrations": "了解如何连接电商、支付、广告和第三方工具。",
    "reviews": "了解如何收集、管理和展示客户评论与评分。",
    "sign-up-forms": "了解如何创建注册表单、弹窗和订阅增长渠道。",
    "sms": "了解短信订阅、发送、合规和短信营销设置。",
    "whatsapp": "了解 WhatsApp 消息、订阅和客户沟通设置。",
    "push-notifications": "了解如何配置和发送移动推送通知。",
    "social-marketing": "了解社交营销相关设置和增长工具。",
}

# Ordered category slugs for homepage grid display
CATEGORY_ORDER = [
    "featured-resources",
    "account-billing",
    "campaigns",
    "flows",
    "integrations",
    "content",
    "sign-up-forms",
    "sms",
    "deliverability-compliance",
    "analytics",
    "audience",
    "conversations",
    "customer-agent",
    "customer-hub",
    "helpdesk",
    "reviews",
    "advanced-kdp-marketing-analytics",
    "whatsapp",
    "push-notifications",
    "social-marketing",
]


# ============================================================
# WordPress Pages API Client
# ============================================================

class PagesClient:
    """WordPress REST API client for Pages (not BetterDocs docs)."""

    def __init__(self):
        self.auth = (WP_USERNAME, WP_APP_PASSWORD)
        self.base = f"{WP_SITE_URL}{WP_API_BASE}"

    def _url(self, endpoint):
        return f"{self.base}{endpoint}"

    def create_page(self, title, content, slug=None, parent=0, status="publish"):
        payload = {"title": title, "content": content, "status": status, "parent": parent}
        if slug:
            payload["slug"] = slug

        def _do():
            resp = requests.post(self._url("/pages"), json=payload, auth=self.auth, timeout=60)
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"CREATE page: {title[:40]}")

    def update_page(self, page_id, title=None, content=None, slug=None, parent=None):
        payload = {"status": "publish"}
        if title is not None:
            payload["title"] = title
        if content is not None:
            payload["content"] = content
        if slug is not None:
            payload["slug"] = slug
        if parent is not None:
            payload["parent"] = parent

        def _do():
            resp = requests.post(self._url(f"/pages/{page_id}"), json=payload, auth=self.auth, timeout=60)
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"UPDATE page #{page_id}")

    def find_page_by_slug(self, slug, parent=None):
        params = {"slug": slug, "per_page": 20}
        if parent is not None:
            params["parent"] = parent

        def _do():
            resp = requests.get(
                self._url("/pages"),
                params=params,
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        pages = with_retry(_do, description=f"SEARCH page slug: {slug}")
        for page in pages:
            if page.get("slug") == slug and (parent is None or page.get("parent") == parent):
                return page
        return pages[0] if pages else None

    def get_page(self, page_id):
        def _do():
            resp = requests.get(self._url(f"/pages/{page_id}"), auth=self.auth, timeout=30)
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"GET page #{page_id}")

    def get_child_pages(self, parent_id):
        def _do():
            resp = requests.get(
                self._url("/pages"),
                params={"parent": parent_id, "per_page": 100},
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"GET child pages of #{parent_id}")


# ============================================================
# Meta helpers
# ============================================================

def load_deploy_meta():
    meta = load_json(DEPLOY_META)
    meta.setdefault("categories", {})
    meta.setdefault("sections", {})
    meta.setdefault("articles", {})
    return meta

def save_deploy_meta(meta):
    save_json(DEPLOY_META, meta)


def article_slug(title: str, article_id: str = "") -> str:
    slug = slugify(title)
    if article_id and (not slug or len(slug) > 72):
        return f"articles-{slug[:72].strip('-')}-{article_id}"
    return f"articles-{slug}"


def section_slug(section_id: str) -> str:
    return f"section-{section_id}"


def clean_category_name(category_slug: str, fallback: str = "") -> str:
    return ZH_CATEGORY_NAMES.get(category_slug) or fallback or category_slug


def clean_section_name(section_name: str) -> str:
    section_name = (section_name or "").strip()
    return ZH_SECTION_NAMES.get(section_name, section_name)


def meta_page_url(meta: dict, kind: str, key: str, fallback_slug: str) -> str:
    info = meta.get(kind, {}).get(key, {})
    return info.get("url") or docs_url(fallback_slug)


def reading_minutes_from_html(body_html: str) -> int:
    text = BeautifulSoup(body_html or "", "html.parser").get_text(" ", strip=True)
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    latin_words = len(re.findall(r"[A-Za-z0-9]+", text))
    minutes = round((chinese_chars / 450) + (latin_words / 220))
    return max(1, minutes)


def markdown_excerpt(markdown_body: str, max_chars: int = 118) -> str:
    lines = []
    for raw in (markdown_body or "").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("!["):
            continue
        line = re.split(r"\s+#{1,6}\s+", line, maxsplit=1)[0]
        line = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", line)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        line = re.sub(r"`([^`]+)`", r"\1", line)
        line = re.sub(r"\*{1,4}([^*]+)\*{1,4}", r"\1", line)
        line = re.sub(r"#{1,6}\s*", "", line)
        line = re.sub(r"^\s*[-*]\s+", "", line)
        line = re.sub(r"^\s*\d+\.\s+", "", line)
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            lines.append(line)
        if len(" ".join(lines)) >= max_chars:
            break
    excerpt = " ".join(lines).strip()
    if len(excerpt) > max_chars:
        excerpt = excerpt[:max_chars].rstrip(" ，。、；;,.") + "..."
    return excerpt


def format_updated_at(value: str) -> str:
    if not value:
        return ""
    raw = value.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(raw)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=ZoneInfo("UTC"))
        eastern = dt.astimezone(ZoneInfo("America/New_York"))
        hour = eastern.strftime("%I").lstrip("0") or "0"
        return f"{eastern.year}年{eastern.month}月{eastern.day}日 {hour}:{eastern.strftime('%M')} {eastern.strftime('%p')} EST"
    except Exception:
        return value


# ============================================================
# HTML Templates
# ============================================================

SITE_BASE = (WP_SITE_URL or "https://dynamicycle.com").rstrip("/")
DOCS_BASE_PATH = "/docs/v2"
BRAND_LOGO_URL = "https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/02/logo02.png?fit=600%2C126&ssl=1"
BRAND_MARK_URL = "https://dynamicycle.com/wp-content/uploads/2025/03/e59bbee78987-1.png?w=125"


def docs_url(slug: str = "") -> str:
    slug = slug.strip("/")
    if not slug:
        return f"{SITE_BASE}{DOCS_BASE_PATH}/"
    return f"{SITE_BASE}{DOCS_BASE_PATH}/{slug}/"


def local_preview_href(filename: str) -> str:
    return filename


def brand_css() -> str:
    return """
/* --- Dynamicycle brand shell --- */
.hc-brand-shell{min-height:100vh;background:#fafafa;color:#18181b}
.hc-brand-header{position:sticky;top:0;z-index:80;background:rgba(255,255,255,.92);backdrop-filter:saturate(180%) blur(18px);border-bottom:1px solid #ececf0}
.hc-brand-header-inner{max-width:1200px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.hc-brand-logo{display:flex;align-items:center;gap:12px;min-width:0}
.hc-brand-logo img{display:block;width:169px;height:auto}
.hc-brand-doc-badge{font-size:12px;font-weight:600;color:#4f46e5;background:#eef2ff;border:1px solid #e0e7ff;border-radius:999px;padding:4px 9px;white-space:nowrap}
.hc-brand-nav{display:flex;align-items:center;gap:22px;font-size:14px;font-weight:500;color:#3f3f46}
.hc-brand-nav a{color:#3f3f46;text-decoration:none;white-space:nowrap}
.hc-brand-nav a:hover{color:#111827;text-decoration:none}
.hc-brand-cta{display:inline-flex;align-items:center;justify-content:center;border-radius:999px;background:#111827;color:#fff!important;padding:9px 16px;font-size:13px;font-weight:700;box-shadow:0 8px 20px rgba(17,24,39,.14)}
.hc-brand-cta:hover{background:#312e81;color:#fff!important}
.hc-brand-footer{background:#0f172a;color:#e5e7eb;margin-top:0}
.hc-brand-footer-inner{max-width:1200px;margin:0 auto;padding:48px 24px;display:grid;grid-template-columns:minmax(220px,1.2fr) repeat(3,minmax(140px,.7fr));gap:36px}
.hc-brand-footer-logo{display:flex;align-items:center;gap:12px;margin-bottom:14px}
.hc-brand-footer-logo img{width:48px;height:auto;border-radius:10px}
.hc-brand-footer-title{font-size:18px;font-weight:700;color:#fff;line-height:1.35}
.hc-brand-footer-copy{font-size:14px;color:#a1a1aa;max-width:330px;line-height:1.7}
.hc-brand-footer h3{font-size:12px;font-weight:700;color:#fff;text-transform:uppercase;letter-spacing:.08em;margin:0 0 14px}
.hc-brand-footer a{display:block;color:#cbd5e1;text-decoration:none;font-size:14px;margin:9px 0}
.hc-brand-footer a:hover{color:#fff;text-decoration:none}
.hc-brand-footer-bottom{max-width:1200px;margin:0 auto;padding:18px 24px 28px;border-top:1px solid rgba(148,163,184,.18);font-size:12px;color:#94a3b8;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
@media(max-width:980px){
.hc-brand-nav{gap:14px}
.hc-brand-nav a:nth-child(n+4){display:none}
.hc-brand-footer-inner{grid-template-columns:1fr 1fr}
}
@media(max-width:768px){
.hc-brand-header-inner{padding:12px 20px}
.hc-brand-logo img{width:142px}
.hc-brand-doc-badge{display:none}
.hc-brand-nav a:not(.hc-brand-cta){display:none}
.hc-brand-footer-inner{grid-template-columns:1fr;padding:38px 20px}
.hc-brand-footer-bottom{padding-left:20px;padding-right:20px}
}
"""


def brand_header_html() -> str:
    return f"""
<header class="hc-brand-header">
  <div class="hc-brand-header-inner">
    <a class="hc-brand-logo" href="{SITE_BASE}/" aria-label="Dynamicycle home">
      <img src="{BRAND_LOGO_URL}" alt="DYNAMIC CYCLE" loading="eager">
      <span class="hc-brand-doc-badge">Docs v2</span>
    </a>
    <nav class="hc-brand-nav" aria-label="Dynamicycle">
      <a href="{SITE_BASE}/">Home</a>
      <a href="{SITE_BASE}/optimization-engine/">Optimization Engine</a>
      <a href="https://connect.klaviyo.com/dynamic-cycle">Klaviyo Agency</a>
      <a href="{SITE_BASE}/partner/">Partners</a>
      <a href="{SITE_BASE}/blog/">Blog</a>
      <a href="{SITE_BASE}/contact/">Contact</a>
      <a class="hc-brand-cta" href="https://connect.klaviyo.com/dynamic-cycle">GET START</a>
    </nav>
  </div>
</header>"""


def brand_footer_html() -> str:
    return f"""
<footer class="hc-brand-footer">
  <div class="hc-brand-footer-inner">
    <div>
      <div class="hc-brand-footer-logo">
        <img src="{BRAND_MARK_URL}" alt="" loading="lazy">
        <div class="hc-brand-footer-title">AI-Powered<br>Customer Journey Agency</div>
      </div>
      <p class="hc-brand-footer-copy">Dynamic Cycle helps global ecommerce brands design governed AI decision systems on top of Klaviyo.</p>
    </div>
    <div>
      <h3>Solutions</h3>
      <a href="https://mp.weixin.qq.com/s/pYUMbwNYtKkRqKEC5FvtNA?version=4.1.31.70466&platform=mac&from=industrynews">Grow</a>
      <a href="https://mp.weixin.qq.com/s/FBsBl04PMsdfuIC6lMpdlA">Retain</a>
      <a href="https://mp.weixin.qq.com/s/i2W1IbL7BifSc6QZMzPXmg">Discover</a>
      <a href="https://mp.weixin.qq.com/s/kRyW95A9L0JVTQ5Eunv81A">Site Search</a>
    </div>
    <div>
      <h3>Services</h3>
      <a href="https://connect.klaviyo.com/dynamic-cycle">Klaviyo Agency</a>
      <a href="https://mp.weixin.qq.com/s/M-JDhtS4C1S-u2rXTZ-xxw">Email Marketing</a>
      <a href="https://mp.weixin.qq.com/s/jBZ9BpD95O6Cb2k38kyC9g">SMS Marketing</a>
      <a href="{SITE_BASE}/optimization-engine/">Optimization Engine</a>
    </div>
    <div>
      <h3>Contact</h3>
      <a href="mailto:dc@dynamicycle.com">dc@dynamicycle.com</a>
      <a href="{SITE_BASE}/contact/">Contact US</a>
      <a href="{SITE_BASE}/docs/">Docs</a>
      <a href="{docs_url()}">Docs v2</a>
    </div>
  </div>
  <div class="hc-brand-footer-bottom">
    <span>© Dynamic Cycle</span>
    <span>China's Leading Professional Klaviyo Agency</span>
  </div>
</footer>"""


def with_brand_shell(page_html: str) -> str:
    return f'<div class="hc-brand-shell">{brand_header_html()}{page_html}{brand_footer_html()}</div>'


def sidebar_html(active_slug="", meta=None, preview=False):
    """Generate a left sidebar with all category links."""
    items = []
    for slug in CATEGORY_ORDER:
        if slug == "featured-resources":
            continue
        name = ZH_CATEGORY_NAMES.get(slug)
        if not name:
            continue
        active_cls = " hc-sb-item--active" if slug == active_slug else ""
        href = local_preview_href(f"category-{slug}.html") if preview else meta_page_url(meta or {}, "categories", slug, slug)
        items.append(
            f'<a class="hc-sb-item{active_cls}" href="{escape_attr(href)}">'
            f'{html.escape(name)}</a>'
        )
    return f'<nav class="hc-sidebar">{"".join(items)}</nav>'


def topic_sidebar_html(active_slug="", meta=None, preview=False):
    """Generate Klaviyo-style topic/category navigation for section pages."""
    items = []
    for slug in CATEGORY_ORDER:
        if slug == "featured-resources":
            continue
        name = ZH_CATEGORY_NAMES.get(slug)
        if not name:
            continue
        icon = CATEGORY_ICONS.get(slug, """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/></svg>""")
        active_cls = " hc-topic-item--active" if slug == active_slug else ""
        href = local_preview_href(f"category-{slug}.html") if preview else meta_page_url(meta or {}, "categories", slug, slug)
        items.append(
            f'<a class="hc-topic-item{active_cls}" href="{escape_attr(href)}">'
            f'<span class="hc-topic-icon">{icon}</span>'
            f'<span class="hc-topic-label">{html.escape(name)}</span>'
            f'</a>'
        )
    return (
        '<aside class="hc-topic-sidebar">'
        '<h1 class="hc-topic-heading">按主题浏览</h1>'
        f'{"".join(items)}'
        '</aside>'
    )


def extract_toc(body_html):
    """Extract h2/h3 headings from HTML body and return TOC items."""
    toc = []
    for m in re.finditer(r'<h([23])\s+[^>]*id=["\']([^"\']*)["\'][^>]*>(.*?)</h[23]>', body_html):
        level = int(m.group(1))
        anchor = m.group(2)
        title = re.sub(r'<[^>]+>', '', m.group(3)).strip()
        if title and anchor:
            toc.append({"level": level, "anchor": anchor, "title": title})
    return toc


def toc_sidebar_html(toc_items):
    """Generate a TOC sidebar from extracted headings."""
    if not toc_items:
        return ""
    items = []
    for t in toc_items:
        indent = " hc-toc-h3" if t["level"] == 3 else ""
        items.append(
            f'<a class="hc-toc-item{indent}" href="#{t["anchor"]}">'
            f'{html.escape(t["title"])}</a>'
        )
    return (
        '<nav class="hc-toc">'
        '<div class="hc-toc-title">目录</div>'
        f'{"".join(items)}'
        '</nav>'
    )


def layout_css(extra=""):
    """Shared CSS for 2-column layout pages."""
    extra = (extra or "").replace("{{", "{").replace("}}", "}")
    return f"""
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap');
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,"Noto Sans SC",sans-serif;color:#18181b;background:#fafafa;line-height:1.6;-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration:none}}
{brand_css()}

/* --- Layout --- */
.hc-layout{{display:grid;grid-template-columns:260px 1fr;max-width:1200px;margin:0 auto;min-height:80vh}}

/* --- Left sidebar --- */
.hc-sidebar{{position:sticky;top:24px;padding:24px 20px 24px 24px;align-self:start;max-height:calc(100vh - 48px);overflow-y:auto}}
.hc-sb-item{{display:block;font-size:14px;font-weight:500;color:#71717a;padding:8px 12px;border-radius:8px;margin-bottom:2px;transition:all .15s ease;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.hc-sb-item:hover{{background:#f4f4f5;color:#18181b}}
.hc-sb-item--active{{background:#eef2ff;color:#4f46e5;font-weight:600}}

/* --- Topic/category sidebar --- */
.hc-topic-sidebar{{position:sticky;top:104px;align-self:start;max-height:calc(100vh - 128px);overflow-y:auto;padding-right:24px}}
.hc-topic-heading{{font-family:'Instrument Sans',-apple-system,BlinkMacSystemFont,"Noto Sans SC",sans-serif;font-size:28px;font-weight:500;line-height:1.2;color:rgb(29,30,32);margin:0 0 24px}}
.hc-topic-item{{display:flex;align-items:center;gap:14px;padding:17px 20px 17px 0;border-radius:8px;color:rgb(29,30,32);text-decoration:none;transition:background .15s ease,color .15s ease}}
.hc-topic-item:hover{{background:#f4f4f5;color:rgb(29,30,32)}}
.hc-topic-item--active{{background:rgb(29,30,32);color:#fff}}
.hc-topic-item--active:hover{{background:rgb(29,30,32);color:#fff}}
.hc-topic-icon{{width:28px;height:28px;min-width:28px;max-width:28px;display:flex;align-items:center;justify-content:center;flex:0 0 28px;overflow:hidden}}
.hc-topic-icon svg{{display:block;width:26px!important;height:26px!important;min-width:26px;max-width:26px!important;max-height:26px!important;flex:0 0 26px}}
.hc-topic-label{{font-family:'Instrument Sans',-apple-system,BlinkMacSystemFont,"Noto Sans SC",sans-serif;font-size:20px;font-weight:400;line-height:1.25}}

/* --- TOC sidebar (article pages) --- */
.hc-toc{{padding:24px 20px 24px 24px;position:sticky;top:24px;align-self:start;max-height:calc(100vh - 48px);overflow-y:auto}}
.hc-toc-title{{font-size:20px;font-weight:600;color:#1a1a2e;margin:36px 0 28px;padding:0 12px;letter-spacing:0}}
.hc-toc-item{{display:block;font-size:16px;font-weight:400;color:#1a1a2e;padding:10px 12px;border-radius:6px;margin-bottom:24px;transition:all .15s ease;line-height:1.45}}
.hc-toc-item:hover{{color:#18181b;background:#f4f4f5}}
.hc-toc-h3{{padding-left:24px}}

/* --- Main content area --- */
.hc-main{{padding:24px 32px 80px 24px;border-left:1px solid #e4e4e7;min-width:0}}

/* --- Breadcrumb --- */
.hc-crumb{{font-size:14px;color:#71717a;margin-bottom:24px}}
.hc-crumb a{{color:#71717a;transition:color .15s ease}}
.hc-crumb a:hover{{color:#18181b}}
.hc-crumb-sep{{margin:0 8px;color:#d4d4d8}}

{extra}

/* --- Responsive --- */
@media(max-width:1024px){{
.hc-layout{{grid-template-columns:220px 1fr}}
}}
@media(max-width:768px){{
.hc-layout{{grid-template-columns:1fr}}
.hc-sidebar,.hc-toc{{display:none}}
.hc-main{{padding:16px 20px 60px;border-left:none}}
}}
"""


def shared_css():
    return """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans SC",sans-serif;color:#1f2937;background:#fff;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:#1a1a2e;text-decoration:none;transition:color .15s ease}
a:hover{color:#4a4a6a}
img{max-width:100%;height:auto}
.dc-wrap{max-width:1200px;margin:0 auto;padding:0 24px}
"""


def search_js(docs_page_id=None):
    parent_param = f"&parent={int(docs_page_id)}" if docs_page_id else ""
    return f"""
(function(){{
var input=document.getElementById('dc-search-input');
var results=document.getElementById('dc-search-results');
var timer=null;
if(!input)return;
function escapeHtml(s){{return (s||'').replace(/[&<>"']/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c];}});}}
input.addEventListener('input',function(){{
clearTimeout(timer);
var q=this.value.trim();
if(q.length<2){{results.innerHTML='';results.style.display='none';return;}}
timer=setTimeout(function(){{
var base='{SITE_BASE}/wp-json/wp/v2/pages?search='+encodeURIComponent(q)+'&per_page=8&_fields=id,title,link,excerpt,parent';
var urls=[base+'{parent_param}',base];
Promise.all(urls.map(function(u){{return fetch(u).then(function(r){{return r.json();}}).catch(function(){{return [];}});}}))
.then(function(groups){{
var seen={{}};
var pages=[];
groups.forEach(function(group){{(group||[]).forEach(function(p){{
if(!p.id||seen[p.id])return;
seen[p.id]=true;
pages.push(p);
}});}});
pages=pages.filter(function(p){{return p.link&&p.link.indexOf('{DOCS_BASE_PATH}/')!==-1;}});
if(!pages.length){{results.innerHTML='<div class="hc-results-empty">未找到相关内容</div>';results.style.display='block';return;}}
results.innerHTML=pages.map(function(p){{
var t=p.title.rendered||'';
var e=p.excerpt&&p.excerpt.rendered?p.excerpt.rendered.replace(/<[^>]+>/g,'').slice(0,120):'';
return '<a class="hc-results-item" href="'+p.link+'"><span class="hc-results-title">'+escapeHtml(t)+'</span><span class="hc-results-excerpt">'+escapeHtml(e)+'</span></a>';
}}).join('');
results.style.display='block';
}});
}},300);
}});
document.addEventListener('click',function(e){{
if(!e.target.closest('.hc-search')){{
var r=document.getElementById('dc-search-results');
if(r)r.style.display='none';
}}
}});
// Press "/" to focus search
document.addEventListener('keydown',function(e){{
if(e.key==='/'&&!e.ctrlKey&&!e.metaKey&&document.activeElement.tagName!=='INPUT'&&document.activeElement.tagName!=='TEXTAREA'){{
e.preventDefault();
input.focus();
}}
}});
}})();
"""


CATEGORY_COLORS = {
    "account-billing": "#6366f1",
    "advanced-kdp-marketing-analytics": "#8b5cf6",
    "analytics": "#a855f7",
    "campaigns": "#f43f5e",
    "content": "#f97316",
    "conversations": "#14b8a6",
    "customer-agent": "#06b6d4",
    "customer-hub": "#0ea5e9",
    "deliverability-compliance": "#22c55e",
    "flows": "#3b82f6",
    "helpdesk": "#eab308",
    "integrations": "#ec4899",
    "reviews": "#f59e0b",
    "sign-up-forms": "#10b981",
    "sms": "#ef4444",
    "whatsapp": "#25d366",
    "push-notifications": "#818cf8",
    "social-marketing": "#fb923c",
}

CATEGORY_ICONS = {
    "account-billing": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M20 21a8 8 0 10-16 0"/></svg>""",
    "campaigns": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>""",
    "flows": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>""",
    "integrations": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>""",
    "content": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 4h16a1 1 0 011 1v14a1 1 0 01-1 1H4a1 1 0 01-1-1V5a1 1 0 011-1z"/><path d="M8 8h8M8 12h5"/></svg>""",
    "sign-up-forms": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18"/></svg>""",
    "sms": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg>""",
    "deliverability-compliance": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>""",
    "analytics": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>""",
    "audience": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><rect x="14" y="14" width="6" height="6" rx="1"/></svg>""",
    "conversations": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>""",
    "customer-agent": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2a5 5 0 015 5v3a5 5 0 01-10 0V7a5 5 0 015-5z"/><path d="M2 12h2m16 0h2M12 2v2m0 16v2"/><circle cx="12" cy="12" r="3"/></svg>""",
    "customer-hub": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>""",
    "helpdesk": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/><path d="M8 10h.01M12 10h.01M16 10h.01"/></svg>""",
    "reviews": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>""",
    "advanced-kdp-marketing-analytics": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/><polyline points="7.5 4.21 12 6.81 16.5 4.21"/><polyline points="7.5 19.79 7.5 14.6 3 12"/><polyline points="21 12 16.5 14.6 16.5 19.79"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>""",
    "whatsapp": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/><path d="M8 10l2 2 4-4"/></svg>""",
    "push-notifications": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 01-3.46 0"/></svg>""",
    "social-marketing": """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>""",
}


def homepage_html(menu_items, relation_data, docs_page_id=None, preview=False, meta=None):
    """Generate a modern help center homepage — Stripe/Linear/Notion inspired."""
    categories = []
    for slug in CATEGORY_ORDER:
        name_zh = ZH_CATEGORY_NAMES.get(slug)
        if not name_zh:
            continue
        relation = next((r for r in relation_data if r.get("category_slug") == slug), {})
        article_count = relation.get("article_count", 0) if relation else 0
        if article_count == 0:
            continue
        categories.append({"slug": slug, "name": name_zh, "count": article_count})

    cards_html = []
    for cat in categories:
        cat_slug = cat["slug"]
        color = CATEGORY_COLORS.get(cat_slug, "#6366f1")
        icon = CATEGORY_ICONS.get(cat_slug, """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>""")
        href = local_preview_href(f"category-{cat_slug}.html") if preview else meta_page_url(meta or {}, "categories", cat_slug, cat_slug)
        cards_html.append(
            f'<a class="hc-card" href="{escape_attr(href)}">'
            f'<div class="hc-card-icon" style="background:{color}0f;color:{color}">{icon}</div>'
            f'<div class="hc-card-body">'
            f'<span class="hc-card-title">{html.escape(cat["name"])}</span>'
            f'<span class="hc-card-desc">{cat["count"]} 篇文章</span>'
            f'</div>'
            f'<svg class="hc-card-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg>'
            f'</a>'
        )

    # Split into featured (top 4) and rest
    featured = cards_html[:4]
    rest = cards_html[4:]

    featured_html = "\n".join(featured)
    rest_html = "\n".join(rest)

    page = f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',-apple-system,BlinkMacSystemFont,"Noto Sans SC",sans-serif;color:#18181b;background:#fafafa;line-height:1.6;-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration:none}}
{brand_css()}

/* --- Hero --- */
.hc-hero{{background:linear-gradient(135deg,#0f172a 0%,#1e1b4b 50%,#312e81 100%);padding:72px 24px 80px;text-align:center;position:relative;overflow:hidden}}
.hc-hero::before{{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle,rgba(99,102,241,.15) 0%,transparent 60%);animation:hc-pulse 8s ease-in-out infinite}}
@keyframes hc-pulse{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.1)}}}}
.hc-hero-inner{{position:relative;z-index:1;max-width:720px;margin:0 auto}}
.hc-hero h1{{font-size:42px;font-weight:700;color:#fff;margin-bottom:12px;letter-spacing:-.02em}}
.hc-hero p{{font-size:18px;color:#a5b4fc;margin-bottom:40px;font-weight:400}}

/* --- Search --- */
.hc-search{{position:relative;max-width:580px;margin:0 auto}}
.hc-search input{{width:100%;height:56px;border:none;border-radius:16px;padding:0 20px 0 52px;font-size:16px;font-family:inherit;background:rgba(255,255,255,.1);backdrop-filter:blur(12px);color:#fff;outline:none;transition:all .25s ease;box-shadow:0 0 0 1px rgba(255,255,255,.12)}}
.hc-search input::placeholder{{color:rgba(255,255,255,.5)}}
.hc-search input:focus{{background:rgba(255,255,255,.15);box-shadow:0 0 0 2px rgba(129,140,248,.5),0 8px 32px rgba(0,0,0,.2)}}
.hc-search svg{{position:absolute;left:18px;top:50%;transform:translateY(-50%);width:20px;height:20px;color:rgba(255,255,255,.5);pointer-events:none}}
.hc-search-kbd{{position:absolute;right:16px;top:50%;transform:translateY(-50%);background:rgba(255,255,255,.1);border-radius:6px;padding:2px 8px;font-size:12px;color:rgba(255,255,255,.4);font-family:inherit;pointer-events:none}}
.hc-results{{position:absolute;top:64px;left:0;right:0;background:#fff;border-radius:16px;box-shadow:0 20px 60px rgba(0,0,0,.25);display:none;z-index:100;overflow:hidden}}
.hc-results-item{{display:flex;flex-direction:column;padding:14px 20px;border-bottom:1px solid #f4f4f5;cursor:pointer;transition:background .1s ease}}
.hc-results-item:hover{{background:#f9fafb}}
.hc-results-title{{font-size:14px;font-weight:500;color:#18181b}}
.hc-results-excerpt{{font-size:13px;color:#a1a1aa;margin-top:3px}}
.hc-results-empty{{padding:24px;text-align:center;color:#a1a1aa;font-size:14px}}

/* --- Content area --- */
.hc-content{{max-width:1120px;margin:0 auto;padding:48px 24px 80px}}

/* --- Section titles --- */
.hc-section-title{{font-size:14px;font-weight:600;color:#71717a;text-transform:uppercase;letter-spacing:.08em;margin-bottom:20px}}

/* --- Featured grid (2x2) --- */
.hc-featured{{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:48px}}

/* --- All categories grid --- */
.hc-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}

/* --- Category card --- */
.hc-card{{display:flex;align-items:center;gap:16px;padding:20px;background:#fff;border:1px solid #e4e4e7;border-radius:14px;transition:all .2s ease;cursor:pointer}}
.hc-card:hover{{border-color:#c7d2fe;background:#fff;box-shadow:0 8px 30px rgba(99,102,241,.08);transform:translateY(-1px)}}
.hc-card-icon{{width:44px;height:44px;min-width:44px;border-radius:12px;display:flex;align-items:center;justify-content:center}}
.hc-card-icon svg{{width:22px;height:22px}}
.hc-card-body{{flex:1;min-width:0}}
.hc-card-title{{display:block;font-size:15px;font-weight:600;color:#18181b;margin-bottom:2px}}
.hc-card-desc{{font-size:13px;color:#a1a1aa}}
.hc-card-arrow{{width:18px;height:18px;color:#d4d4d8;flex-shrink:0;transition:color .15s ease,transform .15s ease}}
.hc-card:hover .hc-card-arrow{{color:#818cf8;transform:translateX(2px)}}

/* --- Responsive --- */
@media(max-width:1024px){{.hc-grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:768px){{
.hc-hero{{padding:48px 20px 56px}}
.hc-hero h1{{font-size:28px}}
.hc-hero p{{font-size:16px;margin-bottom:28px}}
.hc-featured{{grid-template-columns:1fr}}
.hc-grid{{grid-template-columns:1fr}}
.hc-search-kbd{{display:none}}
}}
</style>

<!-- Hero -->
<div class="hc-hero">
  <div class="hc-hero-inner">
    <h1>DC 中文知识库</h1>
    <p>Klaviyo 营销自动化全中文文档，帮你快速上手和排障</p>
    <div class="hc-search">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
      <input id="dc-search-input" type="search" placeholder="搜索问题，如 如何设置 SMS" autocomplete="off">
      <span class="hc-search-kbd">/</span>
      <div id="dc-search-results" class="hc-results"></div>
    </div>
  </div>
</div>

<!-- Categories -->
<div class="hc-content">
  <div class="hc-section-title">热门分类</div>
  <div class="hc-featured">
    {featured_html}
  </div>
  <div class="hc-section-title">全部分类</div>
  <div class="hc-grid">
    {rest_html}
  </div>
</div>

<script>{search_js(docs_page_id)}</script>"""
    return with_brand_shell(page)


def category_page_html(category_name, category_slug, sections_data, articles_data, meta=None, preview=False):
    """Generate a Klaviyo-style category page with topic sidebar, section cards, and top articles."""
    translated_map = {a["article_id"]: a for a in load_translated_articles()}
    category_sections = [s for s in sections_data if s.get("category_slug") == category_slug]
    sections_by_parent = {}
    for section in category_sections:
        parent_id = str(section.get("parent_section_id") or "")
        sections_by_parent.setdefault(parent_id, []).append(section)

    root_sections = [s for s in category_sections if not s.get("parent_section_id")]
    if not root_sections:
        root_sections = [s for s in category_sections if s.get("articles")]

    def section_article_count(section):
        sid = str(section.get("section_id", ""))
        total = len(section.get("articles", []))
        for child in sections_by_parent.get(sid, []):
            total += len(child.get("articles", []))
        return total

    sections = sorted(root_sections, key=lambda s: (s.get("position", 0), s.get("section_name", "").lower()))

    cards_html = []
    for sec in sections:
        sid = str(sec.get("section_id", ""))
        count = section_article_count(sec)
        if count <= 0:
            continue
        sec_slug = section_slug(sid)
        href = local_preview_href(f"section-{sid}.html") if preview else meta_page_url(meta or {}, "sections", sid, sec_slug)
        cards_html.append(
            f'<a class="hc-cat-section-card" href="{escape_attr(href)}">'
            f'<span class="hc-cat-section-card-name">{html.escape(clean_section_name(sec.get("section_name", "")))}</span>'
            f'<span class="hc-cat-section-card-count">{count} 篇文章</span>'
            f'</a>'
        )

    top_articles_html = []
    for art in articles_data[:8]:
        aid = str(art.get("article_id", ""))
        translated = translated_map.get(aid, {})
        title = translated.get("title") or art.get("title", "")
        excerpt = markdown_excerpt(translated.get("body", "")) if translated else ""
        art_slug = article_slug(title, aid)
        href = local_preview_href("article-sample.html") if preview else meta_page_url(meta or {}, "articles", aid, art_slug)
        top_articles_html.append(
            f'<article class="hc-cat-article">'
            f'<a class="hc-cat-article-title" href="{escape_attr(href)}">{html.escape(title)}</a>'
            f'{f"<p>{html.escape(excerpt)}</p>" if excerpt else ""}'
            f'</article>'
        )

    sidebar = topic_sidebar_html(category_slug, meta=meta, preview=preview)
    description = CATEGORY_DESCRIPTIONS.get(category_slug, f"浏览 {category_name} 相关的指南、设置说明和最佳实践。")

    page_css = """
.hc-category-page{{background:#fafafa}}
.hc-category-layout{{display:grid;grid-template-columns:360px 1fr;max-width:1200px;margin:0 auto;padding:46px 24px 90px;align-items:start}}
.hc-category-main{{position:relative;min-width:0;padding-left:44px;font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif}}
.hc-category-main::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:1px;background:#e4e4e7}}
.hc-category-header{{max-width:820px;margin:0 0 34px}}
.hc-category-title{{font-size:28px;font-weight:600;line-height:36px;color:rgb(29,30,32);letter-spacing:.01em;margin:0 0 12px}}
.hc-category-desc{{font-size:18px;font-weight:400;line-height:30px;color:#52525b;letter-spacing:.012em;margin:0}}
.hc-cat-section-grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;max-width:820px;margin:0 0 62px}}
.hc-cat-section-card{{min-height:128px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:22px 18px;background:#fff;border:1px solid #f0efec;border-radius:8px;box-shadow:0 8px 18px rgba(29,30,32,.05);transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease}}
.hc-cat-section-card:hover{{transform:translateY(-2px);border-color:#e4e4e7;box-shadow:0 12px 24px rgba(29,30,32,.08)}}
.hc-cat-section-card-name{{font-size:20px;font-weight:500;line-height:28px;color:rgb(29,30,32);letter-spacing:.01em;margin:0 0 12px}}
.hc-cat-section-card-count{{font-size:16px;font-weight:400;line-height:24px;color:#52525b;letter-spacing:.012em}}
.hc-cat-top-title{{font-size:21px;font-weight:600;line-height:28px;color:rgb(29,30,32);letter-spacing:.01em;margin:0 0 24px}}
.hc-cat-articles{{display:flex;flex-direction:column;gap:34px;max-width:780px}}
.hc-cat-article-title{{display:inline;color:rgb(29,30,32);font-size:19px;font-weight:500;line-height:30px;letter-spacing:.01em;text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:1px}}
.hc-cat-article p{{font-size:16px;font-weight:400;line-height:27px;color:#52525b;letter-spacing:.012em;margin:7px 0 0;max-width:760px}}
@media(max-width:1024px){{.hc-category-layout{{grid-template-columns:300px 1fr}}.hc-cat-section-grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media(max-width:768px){{.hc-category-layout{{grid-template-columns:1fr;padding:28px 20px 70px}}.hc-category-main{{padding-left:0}}.hc-category-main::before{{display:none}}.hc-topic-sidebar{{position:static;max-height:none;padding:0 0 28px}}.hc-cat-section-grid{{grid-template-columns:1fr}}.hc-category-title{{font-size:24px;line-height:32px}}}}
"""

    page = f"""<style>{layout_css(page_css)}</style>
<div class="hc-category-page">
  <div class="hc-category-layout">
    {sidebar}
    <main class="hc-category-main">
      <header class="hc-category-header">
        <h1 class="hc-category-title">{html.escape(category_name)}</h1>
        <p class="hc-category-desc">{html.escape(description)}</p>
      </header>
      <div class="hc-cat-section-grid">{"".join(cards_html)}</div>
      <section class="hc-cat-top">
        <h2 class="hc-cat-top-title">热门文章</h2>
        <div class="hc-cat-articles">{"".join(top_articles_html)}</div>
      </section>
    </main>
  </div>
</div>"""
    return with_brand_shell(page)


def section_page_html(section_name, section_id, category_name, category_slug, articles_data, meta=None, preview=False, all_sections=None):
    """Generate a Klaviyo-style section/topic page."""
    all_sections = all_sections or {}
    current = all_sections.get(str(section_id), {}) if isinstance(all_sections, dict) else {}
    root_section_name = current.get("parent_section_name") or current.get("section_name") or section_name
    root_section_label = clean_section_name(root_section_name)

    groups = []
    if isinstance(all_sections, dict):
        for sid, sec in all_sections.items():
            if sec.get("category_slug") != category_slug:
                continue
            sec_name = sec.get("section_name", "")
            parent_name = sec.get("parent_section_name", "")
            if sec_name == root_section_name or parent_name == root_section_name:
                if sec.get("articles"):
                    groups.append(sec)
    if not groups:
        groups = [{
            "section_name": section_name,
            "section_id": section_id,
            "category_slug": category_slug,
            "position": 0,
            "articles": articles_data,
        }]
    groups = sorted(groups, key=lambda s: (s.get("position", 0), s.get("section_name", "")))

    group_blocks = []
    total = 0
    for group in groups:
        articles = group.get("articles", [])
        if not articles:
            continue
        total += len(articles)
        article_items = []
        for art in articles:
            title = art.get("zh_title") or art.get("title", "")
            aid = str(art.get("article_id", ""))
            art_slug = art.get("article_slug") or article_slug(title, aid)
            href = local_preview_href("article-sample.html") if preview else meta_page_url(meta or {}, "articles", aid, art_slug)
            excerpt = art.get("excerpt", "")
            article_items.append(
                f'<article class="hc-sec-article">'
                f'<a class="hc-sec-article-title" href="{escape_attr(href)}">{html.escape(title)}</a>'
                f'{f"<p>{html.escape(excerpt)}</p>" if excerpt else ""}'
                f'</article>'
            )
        group_blocks.append(
            f'<section class="hc-sec-group">'
            f'<h2>{html.escape(clean_section_name(group.get("section_name", "")))}</h2>'
            f'<div class="hc-sec-list">{"".join(article_items)}</div>'
            f'</section>'
        )

    sidebar = topic_sidebar_html(category_slug, meta=meta, preview=preview)
    category_href = local_preview_href(f"category-{category_slug}.html") if preview else meta_page_url(meta or {}, "categories", category_slug, category_slug)

    page_css = """
.hc-section-page{{background:#fafafa}}
.hc-section-layout{{display:grid;grid-template-columns:360px 1fr;max-width:1200px;margin:0 auto;padding:46px 24px 90px;align-items:start}}
.hc-section-main{{position:relative;min-width:0;padding-left:44px;font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif}}
.hc-section-main::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:1px;background:#e4e4e7}}
.hc-section-path{{display:flex;align-items:center;gap:10px;margin:0 0 36px;font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;font-size:24px;font-weight:500;line-height:31px;color:rgb(29,30,32);letter-spacing:.01em}}
.hc-section-path a{{color:rgb(29,30,32);text-decoration:underline;text-underline-offset:3px}}
.hc-section-path .hc-back{{font-size:26px;font-weight:400;line-height:31px;text-decoration:none;letter-spacing:0}}
.hc-section-count{{display:none}}
.hc-sec-group{{margin:0 0 70px;max-width:780px}}
.hc-sec-group h2{{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;font-size:21px;font-weight:600;line-height:28px;color:rgb(29,30,32);letter-spacing:.01em;margin:0 0 22px;scroll-margin-top:120px}}
.hc-sec-list{{display:flex;flex-direction:column;gap:34px}}
.hc-sec-article{{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;color:rgb(29,30,32);font-size:16px;line-height:27px;letter-spacing:.012em}}
.hc-sec-article-title{{display:inline;color:rgb(29,30,32);font-size:19px;font-weight:500;line-height:30px;letter-spacing:.01em;text-decoration:underline;text-underline-offset:4px;text-decoration-thickness:1px}}
.hc-sec-article-title:hover{{color:rgb(29,30,32)}}
.hc-sec-article p{{font-size:16px;font-weight:400;line-height:27px;color:#52525b;letter-spacing:.012em;margin:7px 0 0;max-width:760px}}
.hc-sec-article p:last-child{{margin-bottom:0}}
@media(max-width:1024px){{.hc-section-layout{{grid-template-columns:300px 1fr}}.hc-topic-label{{font-size:18px}}}}
@media(max-width:768px){{.hc-section-layout{{grid-template-columns:1fr;padding:28px 20px 70px}}.hc-topic-sidebar{{position:static;max-height:none;padding:0 0 28px}}.hc-section-main{{padding-left:0}}.hc-section-main::before{{display:none}}.hc-section-path{{font-size:20px}}}}
"""

    page = f"""<style>{layout_css(page_css)}</style>
<div class="hc-section-page">
  <div class="hc-section-layout">
    {sidebar}
    <main class="hc-section-main">
      <div class="hc-section-path">
        <a class="hc-back" href="{escape_attr(category_href)}">←</a>
        <span><a href="{escape_attr(category_href)}">{html.escape(category_name)}</a> / {html.escape(root_section_label)}</span>
      </div>
      <div class="hc-section-count">共 {total} 篇文章</div>
      {"".join(group_blocks)}
    </main>
  </div>
</div>"""
    return with_brand_shell(page)


def article_page_html(title, category_name, category_slug, body_html, section_name="", section_id="", meta=None, preview=False, updated_at=""):
    """Generate an article page — exact Klaviyo article layout."""
    # Build breadcrumb
    display_section_name = clean_section_name(section_name)
    crumb_parts = [f'<a href="{escape_attr(local_preview_href("homepage.html") if preview else docs_url())}">帮助中心</a>']
    category_href = local_preview_href(f"category-{category_slug}.html") if preview else meta_page_url(meta or {}, "categories", category_slug, category_slug)
    if section_name and section_id:
        section_href = local_preview_href(f"section-{section_id}.html") if preview else meta_page_url(meta or {}, "sections", str(section_id), section_slug(str(section_id)))
        crumb_parts.append(f'<a href="{escape_attr(category_href)}">{html.escape(category_name)}</a>')
        crumb_parts.append(f'<a href="{escape_attr(section_href)}">{html.escape(display_section_name)}</a>')
    else:
        crumb_parts.append(f'<a href="{escape_attr(category_href)}">{html.escape(category_name)}</a>')
    crumb_html = '<span class="hc-crumb-sep">/</span>'.join(crumb_parts)
    updated_text = format_updated_at(updated_at)
    read_minutes = reading_minutes_from_html(body_html)
    meta_parts = [f"预计阅读 {read_minutes} 分钟"]
    if updated_text:
        meta_parts.append(f"更新于 {updated_text}")
    article_meta_html = ' <span class="hc-art-meta-sep">|</span> '.join(
        f"<em>{html.escape(part)}</em>" if part.startswith("更新于 ") else html.escape(part)
        for part in meta_parts
    )
    category_icon = CATEGORY_ICONS.get(category_slug, """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 8v4l3 3"/></svg>""")

    # Extract TOC — only h2 headings, matching Klaviyo's TOC behavior
    toc = [t for t in extract_toc(body_html) if t["level"] == 2]
    if toc:
        toc_items = []
        for t in toc:
            toc_items.append(
                f'<a class="hc-toc-item" href="#{t["anchor"]}">{html.escape(t["title"])}</a>'
            )
        toc_sidebar = (
            '<nav class="hc-toc">'
            '<div class="hc-toc-title">目录</div>'
            f'{"".join(toc_items)}'
            '</nav>'
        )
    else:
        toc_sidebar = sidebar_html(category_slug, meta=meta, preview=preview)

    page_css = """
/* --- Article header --- */
.hc-article-page{{background:#fafafa}}
.hc-art-context{{width:100%;background:#fffcf9;border-bottom:none}}
.hc-art-context-inner{{width:min(1200px,calc(100% - 48px));margin:0 auto;padding:42px 0 40px}}
.hc-art-context .hc-crumb{{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;font-size:14px;line-height:22px;letter-spacing:.01em;color:#1a1a2e;margin:0 0 28px}}
.hc-art-context .hc-crumb a{{color:#1a1a2e;text-decoration:underline;text-underline-offset:3px}}
.hc-art-context .hc-crumb a:hover{{color:#4a4a6a}}
.hc-art-context .hc-crumb-sep{{color:#1a1a2e;margin:0 10px}}
.hc-art-header{{display:flex;align-items:center;gap:14px;margin-bottom:22px}}
.hc-art-title-icon{{width:32px;height:32px;display:flex;align-items:center;justify-content:center;color:#1a1a2e;flex:0 0 auto}}
.hc-art-title-icon svg{{width:30px;height:30px}}
.hc-art-title{{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;font-size:30px;font-weight:600;color:#1a1a2e;letter-spacing:.01em;line-height:40px;margin:0}}
.hc-art-meta{{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;font-size:16px;line-height:27px;letter-spacing:.012em;color:#1a1a2e}}
.hc-art-meta em{{font-style:italic}}
.hc-art-meta-sep{{color:#71717a}}
.hc-article-layout{{align-items:start;background:#fafafa;position:relative}}
.hc-article-layout::before{{content:"";position:absolute;left:260px;top:28px;bottom:0;width:1px;background:#e4e4e7}}
.hc-article-layout .hc-toc{{top:104px;max-height:calc(100vh - 128px);padding-top:36px}}
.hc-article-layout .hc-toc-title{{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;margin:0 0 28px;letter-spacing:.01em}}
.hc-article-layout .hc-toc-item{{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;line-height:1.6;letter-spacing:.012em}}
.hc-article-main{{padding-top:36px;background:#fafafa;border-left:none}}

/* --- Article body — Chinese reading optimized, based on Klaviyo structure --- */
.hc-art-body{{max-width:780px;font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;font-size:16px;line-height:27px;color:#52525b;letter-spacing:.012em}}
.hc-art-body p,.hc-art-body ul,.hc-art-body ol,.hc-art-body li{{font-size:16px;line-height:27px;letter-spacing:.012em}}
.hc-art-body p,.hc-art-body h2,.hc-art-body h3,.hc-art-body h4,.hc-art-body h5,.hc-art-body h6,.hc-art-body ul,.hc-art-body ol,.hc-art-body blockquote,.hc-art-body pre,.hc-art-body table{{margin-top:0;margin-bottom:18px}}
.hc-art-body h1,.hc-art-body h2,.hc-art-body h3,.hc-art-body h4,.hc-art-body h5,.hc-art-body h6{{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",'Instrument Sans',-apple-system,BlinkMacSystemFont,sans-serif;font-weight:500;color:rgb(29,30,32);letter-spacing:.01em;scroll-margin-top:120px}}
.hc-art-body h2{{font-size:21px;font-weight:600;line-height:28px;padding:0;margin-top:34px;margin-bottom:22px}}
.hc-art-body h3{{font-size:19px;font-weight:500;line-height:30px;margin-top:28px;margin-bottom:18px}}
.hc-art-body h4,.hc-art-body h5,.hc-art-body h6{{font-size:16px;line-height:27px;margin-top:20px}}
.hc-art-body > h2:first-child,.hc-art-body > h3:first-child,.hc-art-body > h4:first-child{{margin-top:0}}
.hc-art-body ul{{padding-left:40px;list-style-type:disc}}
.hc-art-body ol{{padding-left:40px;list-style-type:decimal}}
.hc-art-body li{{margin:18px 0;display:list-item}}
.hc-art-body li:empty{{display:none;margin:0}}
.hc-art-body li>ul{{list-style-type:circle;margin-bottom:0}}
.hc-art-body li>ol{{margin-bottom:0}}
.hc-art-body a{{font-size:16px;line-height:27px;color:rgb(29,30,32);text-decoration:underline;text-underline-offset:3px;transition:color .15s ease}}
.hc-art-body a:hover{{color:rgb(29,30,32)}}
.hc-art-body strong,.hc-art-body b{{font-weight:500;color:rgb(29,30,32)}}
.hc-art-body img{{display:block;height:auto;margin:0 auto 16px;max-width:100%}}
.hc-art-body figure{{margin:40px auto 16px;max-width:100%}}
.hc-art-body table{{width:100%;margin-top:16px;border-collapse:separate;border-spacing:2px}}
.hc-art-body td,.hc-art-body th{{padding:8px;border:1px solid rgb(233,220,198);vertical-align:middle}}
.hc-art-body th{{font-weight:500;background:#f8f8f8}}
.hc-art-body code{{background:#f4f4f5;padding:2px 6px;border-radius:4px;font-size:14px;color:rgb(29,30,32);font-family:'SF Mono',SFMono-Regular,Menlo,monospace}}
.hc-art-body pre{{background:#1a1a2e;color:#e5e7eb;padding:20px;border-radius:8px;overflow-x:auto;font-size:14px;line-height:1.6}}
.hc-art-body pre code{{background:none;padding:0;color:inherit;font-size:inherit}}
.hc-art-body blockquote{{border-left:4px solid #d0d0d0;background:#f8f8f8;padding:14px 18px;color:rgb(29,30,32)}}
.hc-art-body hr{{border:none;border-top:1px solid #e0e0e0;margin:32px 0}}
.hc-art-body > *:last-child{{margin-bottom:0}}
.hc-art-body h2:last-of-type~ul,.hc-art-body h2:last-of-type~div>ul{{list-style-type:none;padding:0}}
.hc-art-body h2:last-of-type~ul>li,.hc-art-body h2:last-of-type~div>ul>li{{margin:4px 0}}

/* --- Legacy classes from structure.py --- */
.dc-note{{border-left:4px solid #d0d0d0;background:#f8f8f8;padding:14px 18px;margin:16px 0;color:#1a1a2e}}
.dc-doc-figure{{margin:40px 0 16px;max-width:100%}}
.dc-doc-figure img{{display:block;width:100%;height:auto;margin:0}}
.dc-doc-figure figcaption{{font-size:14px;color:#6b7280;margin-top:8px}}
.dc-table-wrap{{overflow-x:auto;margin:16px 0}}

@media(max-width:1024px){{.hc-article-layout::before{{left:220px}}}}
@media(max-width:768px){{.hc-article-layout::before{{display:none}}.hc-art-context-inner{{width:auto;padding:28px 20px 30px}}.hc-article-main{{padding-top:28px;background:#fafafa}}.hc-art-title{{font-size:22px}}.hc-art-meta{{font-size:14px}}.hc-art-body{{max-width:none}}}}
"""

    page = f"""<style>{layout_css(page_css)}</style>
<div class="hc-article-page">
  <section class="hc-art-context">
    <div class="hc-art-context-inner">
      <nav class="hc-crumb">{crumb_html}</nav>
      <div class="hc-art-header">
        <div class="hc-art-title-icon">{category_icon}</div>
        <h1 class="hc-art-title">{html.escape(title)}</h1>
      </div>
      <div class="hc-art-meta">{article_meta_html}</div>
    </div>
  </section>
  <div class="hc-layout hc-article-layout">
    {toc_sidebar}
    <div class="hc-main hc-article-main">
      <div class="hc-art-body">
        {body_html}
      </div>
    </div>
  </div>
</div>"""
    return with_brand_shell(page)


# ============================================================
# Data loading
# ============================================================

def load_relation_data():
    data = load_json(CATEGORY_ARTICLES_JSON)
    return data if isinstance(data, list) else []


def load_sections_data():
    """Load sections-articles.json for section page generation."""
    data = load_json(SECTIONS_ARTICLES_JSON)
    return data if isinstance(data, list) else []


def load_homepage_menu():
    data = load_json(HOMEPAGE_CATEGORY_MENU)
    return data.get("categories", [])


def load_translated_articles():
    """Load all translated articles from klaviyo-cn/."""
    articles = []
    for path in sorted(KLAVIYO_CN_DIR.glob("*/*.md")):
        content = path.read_text("utf-8", errors="ignore")
        fm, body = parse_frontmatter(content)
        if not fm or not body.strip():
            continue
        articles.append({
            "article_id": str(fm.get("id", "")),
            "title": fm.get("title", path.stem),
            "category_slug": fm.get("category_slug", path.parent.name),
            "section_name": fm.get("section", ""),
            "section_id": "",
            "body": body,
            "filename": str(path.relative_to(KLAVIYO_CN_DIR)),
            "updated_at": fm.get("klaviyo_updated", ""),
            "source_url": fm.get("source_url", ""),
        })
    return articles


def build_article_context_map(relations):
    """Return article_id -> source relationship row."""
    article_map = {}
    for category in relations:
        for article in category.get("articles", []):
            aid = str(article.get("article_id", ""))
            if aid:
                article_map[aid] = article
    return article_map


def build_section_article_map(sections_data, translated_articles):
    """Build a lookup: section_id -> list of translated article data with section info."""
    # Build article_id -> translated article lookup
    translated_map = {}
    for art in translated_articles:
        translated_map[art["article_id"]] = art
    parent_section_ids = {
        str(sec.get("parent_section_id", ""))
        for sec in sections_data
        if sec.get("parent_section_id")
    }

    # For each section, collect its articles with translation data
    section_map = {}
    for sec in sections_data:
        sid = sec.get("section_id", "")
        articles = sec.get("articles", [])
        if not articles and str(sid) not in parent_section_ids:
            continue
        enriched = []
        for art in articles:
            aid = str(art.get("article_id", ""))
            t = translated_map.get(aid)
            enriched.append({
                "article_id": aid,
                "title": t["title"] if t else art.get("title", ""),
                "zh_title": t["title"] if t else "",
                "article_slug": article_slug(t["title"] if t else art.get("title", ""), aid),
                "category_slug": art.get("category_slug", ""),
                "section_name": art.get("section_name", ""),
                "section_id": art.get("section_id", ""),
                "excerpt": markdown_excerpt(t.get("body", "") if t else ""),
            })
        section_map[sid] = {
            "section_name": sec.get("section_name", ""),
            "section_id": sid,
            "parent_section_id": sec.get("parent_section_id", ""),
            "parent_section_name": sec.get("parent_section_name", ""),
            "category_slug": sec.get("category_slug", ""),
            "category_name": sec.get("category_name", ""),
            "position": sec.get("position", 0),
            "articles": enriched,
        }
    return section_map


def build_deploy_url_lookup(meta, relations, sections_data, translated_articles):
    """Build source/legacy URL -> v2 URL lookup for internal link rewriting."""
    lookup = {}
    translated_map = {a["article_id"]: a for a in translated_articles}

    for rel in relations:
        cat_slug = rel.get("category_slug", "")
        cat_url = meta_page_url(meta, "categories", cat_slug, cat_slug)
        if rel.get("source_url"):
            lookup[normalize_lookup_url(rel["source_url"])] = cat_url

    for sec in sections_data:
        sid = str(sec.get("section_id", ""))
        if not sid:
            continue
        sec_url = meta_page_url(meta, "sections", sid, section_slug(sid))
        if sec.get("source_url"):
            lookup[normalize_lookup_url(sec["source_url"])] = sec_url

    for rel in relations:
        for article in rel.get("articles", []):
            aid = str(article.get("article_id", ""))
            if not aid:
                continue
            title = translated_map.get(aid, {}).get("title") or article.get("title", "")
            art_url = meta_page_url(meta, "articles", aid, article_slug(title, aid))
            for key in (article.get("source_url"), article.get("wp_link")):
                if key:
                    lookup[normalize_lookup_url(key)] = art_url
            lookup[f"article:{aid}"] = art_url
    return lookup


def normalize_lookup_url(url: str) -> str:
    parsed = urlparse(url or "")
    if not parsed.netloc:
        return (url or "").strip()
    path = parsed.path.rstrip("/")
    return f"{parsed.netloc.lower()}{path}"


def resolve_link_href(href: str, lookup: dict) -> str:
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
        return href

    normalized = normalize_lookup_url(href)
    if normalized in lookup:
        return lookup[normalized]

    match = re.search(r"/hc/en-us/(articles|sections|categories)/(\d+)", href)
    if match:
        kind, source_id = match.groups()
        if kind == "articles":
            return lookup.get(f"article:{source_id}", href)
        key_prefix = "sections" if kind == "sections" else "categories"
        for key, value in lookup.items():
            if f"/hc/en-us/{key_prefix}/{source_id}" in key:
                return value

    match = re.search(r"/docs/articles-[^/#?]+", href)
    if match:
        normalized_legacy = normalize_lookup_url(f"{SITE_BASE}{match.group(0)}")
        return lookup.get(normalized_legacy, href)

    return href


def normalize_article_markdown(markdown_body: str) -> str:
    """Clean translation artifacts before the lightweight markdown renderer runs."""
    lines = markdown_body.splitlines()
    normalized = []

    def next_content_line(start_index: int) -> str:
        for candidate in lines[start_index + 1:]:
            stripped_candidate = candidate.strip()
            if stripped_candidate:
                return stripped_candidate
        return ""

    for index, raw in enumerate(lines):
        line = raw.rstrip()
        stripped = line.strip()

        # Some translated files contain "****Important****"; the local renderer
        # interprets that as nested emphasis and leaves stray literal stars.
        line = re.sub(r"\*{3,}([^*\n]+?)\*{3,}", r"**\1**", line)

        numbered = re.match(r"^\s*(\d+)\.\s*(\S.*)$", line)
        if numbered:
            number, text = numbered.groups()
            next_line = next_content_line(index)
            looks_like_section_heading = (
                len(text) <= 90
                and not re.match(r"^\d+\.\s+", next_line)
                and (
                    next_line.startswith(("- ", "* "))
                    or next_line.startswith("  - ")
                    or next_line.startswith("  * ")
                    or next_line.startswith("**")
                    or next_line.startswith("****")
                    or not next_line
                )
            )
            if looks_like_section_heading:
                line = f"### {number}. {text.strip()}"
            else:
                line = f"{number}. {text.strip()}"

        normalized.append(line)

    return "\n".join(normalized)


def prepare_article_body_html(markdown_body: str, lookup: dict | None = None) -> str:
    body_html = article_to_html(normalize_article_markdown(markdown_body), include_wrapper=False)
    soup = BeautifulSoup(body_html, "html.parser")

    for text_node in soup.find_all(string=True):
        if text_node.strip() == "*":
            text_node.extract()

    seen_ids = set()
    for heading in soup.find_all(["h2", "h3"]):
        text = heading.get_text(" ", strip=True)
        base = heading.get("id") or slugify(text)
        anchor = base
        suffix = 2
        while anchor in seen_ids:
            anchor = f"{base}-{suffix}"
            suffix += 1
        heading["id"] = anchor
        seen_ids.add(anchor)

    for img in soup.find_all("img"):
        if not img.get("loading"):
            img["loading"] = "lazy"
        if not img.get("decoding"):
            img["decoding"] = "async"

    if lookup:
        for link in soup.find_all("a", href=True):
            link["href"] = resolve_link_href(link["href"], lookup)

    return str(soup)


# ============================================================
# Commands
# ============================================================

def cmd_init(args):
    """Create the /docs/v2/ parent page."""
    logger = SyncLogger("Init docs/v2")
    wp = PagesClient()
    meta = load_deploy_meta()

    slug = "v2"
    docs_parent = wp.find_page_by_slug("docs", parent=0)
    parent_id = docs_parent["id"] if docs_parent else 0
    existing = None
    if meta.get("docs_page_id"):
        try:
            existing = wp.get_page(meta["docs_page_id"])
        except Exception:
            existing = None
    if not existing:
        existing = wp.find_page_by_slug(slug, parent=parent_id)

    relations = load_relation_data()
    menu_items = load_homepage_menu()

    if existing:
        meta["docs_page_id"] = existing["id"]
        meta["docs_page_url"] = existing.get("link", "")
        content = homepage_html(menu_items, relations, docs_page_id=existing["id"], meta=meta)
        result = wp.update_page(existing["id"], title="Klaviyo 中文知识库 v2", content=content, slug=slug, parent=parent_id)
        meta["docs_page_url"] = result.get("link", meta["docs_page_url"])
        save_deploy_meta(meta)
        logger.ok(f"Parent page updated: #{existing['id']} {meta.get('docs_page_url', '')}")
    else:
        result = wp.create_page(
            title="Klaviyo 中文知识库 v2",
            content=homepage_html(menu_items, relations, meta=meta),
            slug=slug,
            parent=parent_id,
        )
        meta["docs_page_id"] = result["id"]
        meta["docs_page_url"] = result.get("link", "")
        content = homepage_html(menu_items, relations, docs_page_id=result["id"], meta=meta)
        result = wp.update_page(result["id"], content=content, slug=slug, parent=parent_id)
        meta["docs_page_url"] = result.get("link", meta["docs_page_url"])
        save_deploy_meta(meta)
        logger.ok(f"Created parent page: #{result['id']} {result.get('link', '')}")

    if not docs_parent:
        logger.skip("No top-level WordPress page with slug 'docs' was found; real URL may be /v2/ unless the site has a custom rewrite.")
    logger.summary()


def cmd_categories(args):
    """Deploy category pages."""
    logger = SyncLogger("Deploy categories")
    wp = PagesClient()
    meta = load_deploy_meta()

    parent_id = meta.get("docs_page_id")
    if not parent_id:
        print("Error: run 'init' first to create parent page.")
        return

    relations = load_relation_data()
    sections_data = load_sections_data()
    only = args.only

    targets = []
    for rel in relations:
        cat_slug = rel.get("category_slug", "")
        cat_name = clean_category_name(cat_slug, rel.get("category_name", ""))
        if only and cat_slug != only:
            continue
        targets.append({"slug": cat_slug, "name": cat_name, "data": rel})

    meta.setdefault("categories", {})

    for target in targets:
        cat_slug = target["slug"]
        cat_name = target["name"]
        rel_data = target["data"]
        articles = rel_data.get("articles", [])

        content = category_page_html(cat_name, cat_slug, sections_data, articles, meta=meta)

        slug = cat_slug
        existing = None
        if meta["categories"].get(cat_slug, {}).get("page_id"):
            try:
                existing = wp.get_page(meta["categories"][cat_slug]["page_id"])
            except Exception:
                existing = None
        if not existing:
            existing = wp.find_page_by_slug(slug, parent=parent_id)

        try:
            if existing:
                result = wp.update_page(existing["id"], title=cat_name, content=content, slug=slug, parent=parent_id)
                action = "updated"
            else:
                result = wp.create_page(title=cat_name, content=content, slug=slug, parent=parent_id)
                action = "created"

            meta["categories"][cat_slug] = {
                "page_id": result["id"],
                "slug": slug,
                "name": cat_name,
                "url": result.get("link", ""),
                "action": action,
                "article_count": len(articles),
            }
            save_deploy_meta(meta)
            logger.ok(f"[{cat_slug}] {cat_name} -> {action} #{result['id']}")
        except Exception as exc:
            logger.fail(f"[{cat_slug}] {cat_name}: {exc}")

        time.sleep(0.2)

    if not only and meta.get("docs_page_id"):
        homepage = homepage_html(load_homepage_menu(), relations, docs_page_id=meta["docs_page_id"], meta=meta)
        try:
            wp.update_page(meta["docs_page_id"], content=homepage)
            logger.ok("Homepage links refreshed")
        except Exception as exc:
            logger.fail(f"Homepage refresh failed: {exc}")

    logger.summary()


def cmd_sections(args):
    """Deploy section pages."""
    logger = SyncLogger("Deploy sections")
    wp = PagesClient()
    meta = load_deploy_meta()

    if not meta.get("categories"):
        print("Error: run 'categories' first.")
        return

    sections_data = load_sections_data()
    translated = load_translated_articles()
    section_map = build_section_article_map(sections_data, translated)
    only = args.only

    meta.setdefault("sections", {})

    for sid, sec in sorted(section_map.items(), key=lambda x: x[1].get("position", 0)):
        cat_slug = sec["category_slug"]
        if only and cat_slug != only:
            continue

        cat_info = meta["categories"].get(cat_slug, {})
        parent_id = cat_info.get("page_id")
        cat_name = cat_info.get("name", clean_category_name(cat_slug))

        if not parent_id:
            logger.skip(f"[{sid}] no category page for section: {sec['section_name']}")
            continue

        content = section_page_html(
            sec["section_name"], sid, cat_name, cat_slug, sec["articles"], meta=meta, all_sections=section_map
        )
        slug = f"section-{sid}"

        try:
            existing = None
            if meta["sections"].get(sid, {}).get("page_id"):
                try:
                    existing = wp.get_page(meta["sections"][sid]["page_id"])
                except Exception:
                    existing = None
            if not existing:
                existing = wp.find_page_by_slug(slug, parent=parent_id)
            if existing:
                result = wp.update_page(existing["id"], title=sec["section_name"], content=content, slug=slug, parent=parent_id)
                action = "updated"
            else:
                result = wp.create_page(title=sec["section_name"], content=content, slug=slug, parent=parent_id)
                action = "created"

            meta["sections"][sid] = {
                "page_id": result["id"],
                "slug": slug,
                "name": sec["section_name"],
                "category_slug": cat_slug,
                "url": result.get("link", ""),
                "action": action,
            }
            save_deploy_meta(meta)
            logger.ok(f"[{sid}] {sec['section_name']} -> {action} #{result['id']}")
        except Exception as exc:
            logger.fail(f"[{sid}] {sec['section_name']}: {exc}")

        time.sleep(0.2)

    # Refresh category pages so their section-card links use the newly stored WP URLs.
    relations = load_relation_data()
    for rel in relations:
        cat_slug = rel.get("category_slug", "")
        if only and cat_slug != only:
            continue
        cat_info = meta.get("categories", {}).get(cat_slug, {})
        if not cat_info.get("page_id"):
            continue
        cat_name = cat_info.get("name", clean_category_name(cat_slug, rel.get("category_name", "")))
        try:
            content = category_page_html(cat_name, cat_slug, sections_data, rel.get("articles", []), meta=meta)
            wp.update_page(cat_info["page_id"], title=cat_name, content=content, slug=cat_slug, parent=meta.get("docs_page_id"))
            logger.ok(f"[{cat_slug}] category links refreshed")
        except Exception as exc:
            logger.fail(f"[{cat_slug}] category refresh failed: {exc}")

    logger.summary()


def cmd_articles(args):
    """Deploy article pages."""
    logger = SyncLogger("Deploy articles")
    wp = PagesClient()
    meta = load_deploy_meta()

    if not meta.get("categories"):
        print("Error: run 'categories' first.")
        return

    relations = load_relation_data()
    sections_data = load_sections_data()
    article_context = build_article_context_map(relations)
    translated = load_translated_articles()
    translated_map = {a["article_id"]: a for a in translated}
    section_map = build_section_article_map(sections_data, translated)
    url_lookup = build_deploy_url_lookup(meta, relations, sections_data, translated)
    only = args.only
    force = args.force

    if only:
        only_set = {o.strip() for o in only.split(",") if o.strip()}
        translated = [a for a in translated if a["article_id"] in only_set]

    meta.setdefault("articles", {})
    deployed = meta["articles"]

    total = len(translated)
    touched_categories = set()
    touched_sections = set()
    for idx, article in enumerate(translated, 1):
        aid = article["article_id"]
        title = article["title"]
        context = article_context.get(aid, {})
        cat_slug = context.get("category_slug") or article["category_slug"]
        sec_id = str(context.get("section_id") or "")
        sec_name = context.get("section_name") or article.get("section_name") or ""

        cat_info = meta["categories"].get(cat_slug, {})
        parent_id = cat_info.get("page_id")
        cat_name = cat_info.get("name", clean_category_name(cat_slug))

        if not parent_id:
            logger.skip(f"[{cat_slug}] no category page for: {title[:40]}")
            continue

        if not force and aid in deployed:
            logger.skip(f"[{aid}] already deployed: {title[:40]}")
            continue

        body_html = prepare_article_body_html(article["body"], url_lookup)
        content = article_page_html(
            title,
            cat_name,
            cat_slug,
            body_html,
            section_name=sec_name,
            section_id=sec_id,
            meta=meta,
            updated_at=article.get("updated_at", "") or context.get("klaviyo_updated", ""),
        )
        slug = article_slug(title, aid)

        try:
            existing = None
            if deployed.get(aid, {}).get("page_id"):
                try:
                    existing = wp.get_page(deployed[aid]["page_id"])
                except Exception:
                    existing = None
            if not existing:
                existing = wp.find_page_by_slug(slug, parent=parent_id)
            if existing:
                result = wp.update_page(existing["id"], title=title, content=content, slug=slug, parent=parent_id)
                action = "updated"
            else:
                result = wp.create_page(title=title, content=content, slug=slug, parent=parent_id)
                action = "created"

            deployed[aid] = {
                "page_id": result["id"],
                "slug": slug,
                "title": title,
                "category_slug": cat_slug,
                "url": result.get("link", ""),
                "action": action,
            }
            touched_categories.add(cat_slug)
            if sec_id:
                touched_sections.add(sec_id)
            logger.ok(f"[{idx}/{total}] {title[:50]} -> {action}")
            if idx % 50 == 0:
                save_deploy_meta(meta)
        except Exception as exc:
            logger.fail(f"[{aid}] {title[:40]}: {exc}")
            save_deploy_meta(meta)

        time.sleep(0.3)

    save_deploy_meta(meta)

    # Refresh section/category navigation links after article URLs are known.
    url_lookup = build_deploy_url_lookup(meta, relations, sections_data, list(translated_map.values()))
    for sid in sorted(touched_sections):
        sec = section_map.get(sid)
        if not sec or not meta.get("sections", {}).get(sid, {}).get("page_id"):
            continue
        cat_slug = sec["category_slug"]
        cat_info = meta["categories"].get(cat_slug, {})
        try:
            content = section_page_html(
                sec["section_name"],
                sid,
                cat_info.get("name", clean_category_name(cat_slug)),
                cat_slug,
                sec["articles"],
                meta=meta,
                all_sections=section_map,
            )
            wp.update_page(meta["sections"][sid]["page_id"], title=sec["section_name"], content=content, slug=section_slug(sid), parent=cat_info.get("page_id"))
            logger.ok(f"[{sid}] section links refreshed")
        except Exception as exc:
            logger.fail(f"[{sid}] section refresh failed: {exc}")

    for rel in relations:
        cat_slug = rel.get("category_slug", "")
        if cat_slug not in touched_categories or not meta.get("categories", {}).get(cat_slug, {}).get("page_id"):
            continue
        cat_info = meta["categories"][cat_slug]
        try:
            content = category_page_html(cat_info.get("name", clean_category_name(cat_slug)), cat_slug, sections_data, rel.get("articles", []), meta=meta)
            wp.update_page(cat_info["page_id"], content=content, slug=cat_slug, parent=meta.get("docs_page_id"))
            logger.ok(f"[{cat_slug}] category article links refreshed")
        except Exception as exc:
            logger.fail(f"[{cat_slug}] category refresh failed: {exc}")

    logger.summary()


def cmd_preview(args):
    """Generate local HTML previews without uploading."""
    logger = SyncLogger("Generate previews")
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    relations = load_relation_data()
    sections_data = load_sections_data()
    menu_items = load_homepage_menu()
    translated = load_translated_articles()
    meta = load_deploy_meta()
    article_context = build_article_context_map(relations)

    def wrap(title, body_html):
        return f"<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{html.escape(title)}</title></head><body>{body_html}</body></html>"

    # Homepage preview
    hp_html = homepage_html(menu_items, relations, preview=True, meta=meta)
    (PREVIEW_DIR / "homepage.html").write_text(wrap("DC 中文知识库 v2", hp_html), "utf-8")
    logger.ok(f"Homepage: homepage.html")

    # Category previews
    for cat_sample in relations:
        if not cat_sample.get("articles"):
            continue
        cat_slug = cat_sample["category_slug"]
        cat_name = clean_category_name(cat_slug, cat_sample.get("category_name", ""))
        cp_html = category_page_html(cat_name, cat_slug, sections_data, cat_sample["articles"], meta=meta, preview=True)
        (PREVIEW_DIR / f"category-{cat_slug}.html").write_text(wrap(cat_name, cp_html), "utf-8")
        logger.ok(f"Category: category-{cat_slug}.html")

    # Section previews
    section_map = build_section_article_map(sections_data, translated)
    for sid, sec_sample in section_map.items():
        has_child_sections = any(
            child.get("parent_section_id") == sid
            for child in section_map.values()
        )
        if not sec_sample["articles"] and not has_child_sections:
            continue
        cat_slug = sec_sample["category_slug"]
        cat_name = clean_category_name(cat_slug)
        sp_html = section_page_html(
            sec_sample["section_name"], sec_sample["section_id"],
            cat_name, cat_slug, sec_sample["articles"], meta=meta, preview=True, all_sections=section_map
        )
        (PREVIEW_DIR / f"section-{sec_sample['section_id']}.html").write_text(
            wrap(sec_sample["section_name"], sp_html), "utf-8"
        )
        logger.ok(f"Section: section-{sec_sample['section_id']}.html")

    # Article preview — pick one with headings for TOC demo
    sample = None
    for a in translated:
        if not a["body"].strip():
            continue
        h = prepare_article_body_html(a["body"])
        toc = [item for item in extract_toc(h) if item["level"] == 2 and 0 < len(item["title"]) <= 120]
        if len(toc) >= 2:
            sample = a
            break
    if not sample:
        sample = next((a for a in translated if a["body"].strip()), None)
    if sample:
        body_html = prepare_article_body_html(sample["body"])
        context = article_context.get(sample["article_id"], {})
        cat_slug = context.get("category_slug") or sample["category_slug"]
        cat_name = clean_category_name(cat_slug)
        ap_html = article_page_html(
            sample["title"],
            cat_name,
            cat_slug,
            body_html,
            section_name=context.get("section_name") or sample.get("section_name", ""),
            section_id=str(context.get("section_id") or ""),
            meta=meta,
            preview=True,
            updated_at=sample.get("updated_at", "") or context.get("klaviyo_updated", ""),
        )
        (PREVIEW_DIR / "article-sample.html").write_text(wrap(sample["title"], ap_html), "utf-8")
        logger.ok(f"Article: article-sample.html")

    # Article image preview — pick one with rendered images for figure/image QA
    image_sample = None
    image_sample_score = (-1, -1)
    for a in translated:
        if "![" not in a["body"] and "<img" not in a["body"]:
            continue
        body_html = prepare_article_body_html(a["body"])
        image_count = body_html.count("<img")
        if not image_count:
            continue
        toc_count = len([item for item in extract_toc(body_html) if item["level"] == 2 and 0 < len(item["title"]) <= 120])
        score = (toc_count, image_count)
        if score > image_sample_score:
            image_sample = a
            image_sample_score = score
    if image_sample:
        body_html = prepare_article_body_html(image_sample["body"])
        context = article_context.get(image_sample["article_id"], {})
        cat_slug = context.get("category_slug") or image_sample["category_slug"]
        cat_name = clean_category_name(cat_slug)
        ap_html = article_page_html(
            image_sample["title"],
            cat_name,
            cat_slug,
            body_html,
            section_name=context.get("section_name") or image_sample.get("section_name", ""),
            section_id=str(context.get("section_id") or ""),
            meta=meta,
            preview=True,
            updated_at=image_sample.get("updated_at", "") or context.get("klaviyo_updated", ""),
        )
        (PREVIEW_DIR / "article-image-sample.html").write_text(wrap(image_sample["title"], ap_html), "utf-8")
        logger.ok(f"Article image: article-image-sample.html")

    logger.summary()
    print(f"\nPreview directory: {PREVIEW_DIR}")
    print("Open HTML files in browser to review.")


def cmd_status(args):
    """Show deployment status."""
    meta = load_deploy_meta()
    relations = load_relation_data()
    translated = load_translated_articles()

    docs_id = meta.get("docs_page_id", "N/A")
    docs_url = meta.get("docs_page_url", "N/A")
    categories = meta.get("categories", {})
    sections = meta.get("sections", {})
    articles = meta.get("articles", {})
    sections_data = [s for s in load_sections_data() if s.get("articles")]

    cat_slugs_with_articles = set()
    for rel in relations:
        for art in rel.get("articles", []):
            cat_slugs_with_articles.add(art.get("category_slug", ""))

    print()
    print("=" * 50)
    print("  Deploy Status (WordPress Pages)")
    print("=" * 50)
    print(f"  Parent page:    #{docs_id} {docs_url}")
    print(f"  Category pages: {len(categories)}")
    print(f"  Section pages:  {len(sections)}")
    print(f"  Article pages:  {len(articles)}")
    print(f"  Available categories: {len(relations)}")
    print(f"  Available sections: {len(sections_data)}")
    print(f"  Available articles: {len(translated)}")
    print(f"  Missing categories: {max(len(relations) - len(categories), 0)}")
    print(f"  Missing sections:   {max(len(sections_data) - len(sections), 0)}")
    print(f"  Missing articles:   {max(len(translated) - len(articles), 0)}")
    if categories:
        print()
        print("  Categories:")
        for slug, info in sorted(categories.items()):
            print(f"    - {slug}: #{info.get('page_id', '?')} ({info.get('article_count', 0)} articles) {info.get('url', '')}")
    print()


def cmd_all(args):
    """Full deployment: init + categories + sections + articles."""
    print("=" * 50)
    print("  Full Deploy: init -> categories -> sections -> articles")
    print("=" * 50)

    args_init = argparse.Namespace()
    cmd_init(args_init)

    args_cats = argparse.Namespace(only=None)
    cmd_categories(args_cats)

    args_secs = argparse.Namespace(only=None)
    cmd_sections(args_secs)

    args_arts = argparse.Namespace(only=None, force=args.force)
    cmd_articles(args_arts)

    cmd_status(argparse.Namespace())


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="Create /docs/v2/ parent page").set_defaults(func=cmd_init)

    cats = sub.add_parser("categories", help="Deploy category pages")
    cats.add_argument("--only", help="Deploy only this category slug")
    cats.set_defaults(func=cmd_categories)

    secs = sub.add_parser("sections", help="Deploy section pages")
    secs.add_argument("--only", help="Deploy sections for this category slug only")
    secs.set_defaults(func=cmd_sections)

    arts = sub.add_parser("articles", help="Deploy article pages")
    arts.add_argument("--only", help="Comma-separated article IDs to deploy")
    arts.add_argument("--force", action="store_true", help="Redeploy already-deployed articles")
    arts.set_defaults(func=cmd_articles)

    sub.add_parser("preview", help="Generate local HTML previews").set_defaults(func=cmd_preview)
    sub.add_parser("status", help="Show deployment status").set_defaults(func=cmd_status)

    all_cmd = sub.add_parser("all", help="Full deploy: init + categories + sections + articles")
    all_cmd.add_argument("--force", action="store_true", help="Force redeploy everything")
    all_cmd.set_defaults(func=cmd_all)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
