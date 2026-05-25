"""Shared utilities: retry, API clients, HTML/Markdown conversion."""

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

PROJECT_ROOT = Path(__file__).resolve().parent.parent
KLAVIYO_EN_DIR = PROJECT_ROOT / "klaviyo-en"
KLAVIYO_CN_DIR = PROJECT_ROOT / "klaviyo-cn"
BATTERDOCS_DIR = PROJECT_ROOT / "batterDocs"
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)

WP_SITE_URL = os.getenv("WP_SITE_URL", "").rstrip("/")
WP_USERNAME = os.getenv("WP_USERNAME", "")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD", "")
WP_API_BASE = os.getenv("WP_API_BASE", "/wp-json/wp/v2")

ZENDESK_API = "https://help.klaviyo.com/api/v2/help_center/en-us"

WP_PARENT_CAT = 775425988  # "Kalaviyo 官方文档"

# Klaviyo slug -> WP sub-category ID (under 775425988)
# Loaded dynamically from .category_map.json
CATEGORY_MAP_FILE = KLAVIYO_EN_DIR / ".category_map.json"

def load_category_map():
    if CATEGORY_MAP_FILE.exists():
        return json.loads(CATEGORY_MAP_FILE.read_text("utf-8"))
    return {}

def save_category_map(cat_map):
    CATEGORY_MAP_FILE.write_text(
        json.dumps(cat_map, indent=2, ensure_ascii=False), "utf-8"
    )

# Klaviyo category ID -> batterDocs slug
KLAVIYO_CATEGORY_MAP = {
    115000867647: "account-billing",
    18073014919195: "advanced-kdp-marketing-analytics",
    115000874048: "analytics",
    115000867867: "audience",
    49375106949275: "campaigns",
    4414879524891: "content",
    14234163769755: "conversations",
    48274996158235: "customer-agent",
    34141283979931: "customer-hub",
    45954023294747: "helpdesk",
    115000873988: "deliverability-compliance",
    115000312411: "flows",
    115000032731: "integrations",
    49375133274139: "reviews",
    360000190711: "sign-up-forms",
    29173800271259: "sms",
    49375107982619: "whatsapp",
    50128030093211: "social-marketing",
    50026805374363: "push-notifications",
}

KLAVIYO_CATEGORY_NAMES = {
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


# --- Retry decorator ---

def with_retry(fn, max_retries=5, base_delay=2, description=""):
    """Execute fn with exponential backoff retry on network errors."""
    for attempt in range(1, max_retries + 1):
        delay = base_delay * (2 ** (attempt - 1))
        try:
            return fn()
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.ProxyError) as e:
            desc = f" ({description})" if description else ""
            print(f"  RETRY {attempt}/{max_retries}{desc}: {type(e).__name__}, waiting {delay}s...")
            if attempt == max_retries:
                raise
            time.sleep(delay)
        except requests.exceptions.HTTPError as e:
            if e.response is not None and e.response.status_code == 429:
                retry_after = int(e.response.headers.get("Retry-After", delay))
                print(f"  RATE LIMITED, waiting {retry_after}s...")
                time.sleep(retry_after)
                continue
            raise


# --- API Clients ---

class WordPressClient:
    def __init__(self):
        self.auth = (WP_USERNAME, WP_APP_PASSWORD)
        self.base = f"{WP_SITE_URL}{WP_API_BASE}"

    def _url(self, endpoint):
        return f"{self.base}{endpoint}"

    def get_docs(self, page=1, per_page=100):
        def _do():
            resp = requests.get(
                self._url("/docs"),
                params={"per_page": per_page, "page": page},
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json(), int(resp.headers.get("X-WP-TotalPages", 1))
        return with_retry(_do, description=f"GET docs page {page}")

    def get_all_docs(self):
        all_docs = []
        page = 1
        while True:
            docs, total_pages = self.get_docs(page=page)
            if not docs:
                break
            all_docs.extend(docs)
            if page >= total_pages:
                break
            page += 1
        return all_docs

    def get_categories(self):
        def _do():
            resp = requests.get(
                self._url("/doc_category"),
                params={"per_page": 100},
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description="GET categories")

    def find_category_by_slug(self, slug):
        def _do():
            resp = requests.get(
                self._url("/doc_category"),
                params={"slug": slug, "per_page": 100},
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        cats = with_retry(_do, description=f"SEARCH category slug: {slug}")
        return cats[0] if cats else None

    def create_category(self, name, slug, parent=WP_PARENT_CAT):
        payload = {"name": name, "slug": slug, "parent": parent}

        def _do():
            resp = requests.post(
                self._url("/doc_category"),
                json=payload,
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"CREATE category: {name[:40]}")

    def update_category(self, cat_id, name=None, slug=None, parent=None):
        payload = {}
        if name is not None:
            payload["name"] = name
        if slug is not None:
            payload["slug"] = slug
        if parent is not None:
            payload["parent"] = parent

        def _do():
            resp = requests.post(
                self._url(f"/doc_category/{cat_id}"),
                json=payload,
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"UPDATE category #{cat_id}")

    def find_doc_by_title(self, title):
        def _do():
            resp = requests.get(
                self._url("/docs"),
                params={"search": title, "per_page": 20},
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()

        docs = with_retry(_do, description=f"SEARCH: {title[:40]}")
        clean = re.compile(r"<[^>]+>")
        for doc in docs:
            rendered = doc.get("title", {}).get("rendered", "")
            if clean.sub("", rendered).strip() == title:
                return doc
        return None

    def find_doc_by_slug(self, slug):
        def _do():
            resp = requests.get(
                self._url("/docs"),
                params={"slug": slug, "per_page": 20},
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()

        docs = with_retry(_do, description=f"SEARCH slug: {slug[:40]}")
        for doc in docs:
            if doc.get("slug") == slug:
                return doc
        return docs[0] if docs else None

    def create_doc(self, title, content, category_slug=None, status="publish", slug=None):
        cat_map = load_category_map()
        cat_id = cat_map.get(category_slug) if category_slug else None

        payload = {
            "title": title,
            "content": content,
            "status": status,
            "doc_category": [cat_id] if cat_id else [WP_PARENT_CAT],
        }
        if slug:
            payload["slug"] = slug

        def _do():
            resp = requests.post(
                self._url("/docs"),
                json=payload,
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"CREATE: {title[:40]}")

    def update_doc(self, doc_id, title=None, content=None, category_slug=None, slug=None):
        payload = {"status": "publish"}
        if title:
            payload["title"] = title
        if content is not None:
            payload["content"] = content
        if slug:
            payload["slug"] = slug
        if category_slug:
            cat_map = load_category_map()
            cat_id = cat_map.get(category_slug)
            if cat_id:
                payload["doc_category"] = [cat_id]

        def _do():
            resp = requests.post(
                self._url(f"/docs/{doc_id}"),
                json=payload,
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"UPDATE: doc #{doc_id}")

    def update_doc_categories(self, doc_id, category_ids):
        payload = {"doc_category": category_ids}

        def _do():
            resp = requests.post(
                self._url(f"/docs/{doc_id}"),
                json=payload,
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"UPDATE categories: doc #{doc_id}")


class ZendeskClient:
    def get_categories(self):
        all_categories = {}
        page = 1
        while True:
            def _do(p=page):
                resp = requests.get(
                    f"{ZENDESK_API}/categories.json",
                    params={"per_page": 100, "page": p}, timeout=30,
                )
                resp.raise_for_status()
                return resp.json()
            data = with_retry(_do, description=f"GET categories page {page}")
            categories = data.get("categories", [])
            for c in categories:
                all_categories[c["id"]] = {
                    "id": c["id"],
                    "name": c["name"],
                    "description": c.get("description", ""),
                    "source_url": c.get("html_url", ""),
                    "position": c.get("position", 0),
                    "updated_at": c.get("updated_at", ""),
                }
            if len(categories) < 100:
                break
            page += 1
        return all_categories

    def get_article(self, article_id):
        def _do():
            resp = requests.get(
                f"{ZENDESK_API}/articles/{article_id}.json", timeout=30,
            )
            resp.raise_for_status()
            return resp.json().get("article", {})
        return with_retry(_do, description=f"GET article {article_id}")

    def get_sections(self):
        all_sections = {}
        page = 1
        while True:
            def _do(p=page):
                resp = requests.get(
                    f"{ZENDESK_API}/sections.json",
                    params={"per_page": 100, "page": p}, timeout=30,
                )
                resp.raise_for_status()
                return resp.json()
            data = with_retry(_do, description=f"GET sections page {page}")
            for s in data.get("sections", []):
                all_sections[s["id"]] = {
                    "id": s["id"],
                    "name": s["name"],
                    "category_id": s.get("category_id"),
                    "source_url": s.get("html_url", ""),
                    "position": s.get("position", 0),
                    "parent_section_id": s.get("parent_section_id"),
                    "updated_at": s.get("updated_at", ""),
                }
            if len(data.get("sections", [])) < 100:
                break
            page += 1
        return all_sections

    def get_all_articles(self):
        all_articles = []
        page = 1
        while True:
            def _do(p=page):
                resp = requests.get(
                    f"{ZENDESK_API}/articles.json",
                    params={"per_page": 100, "page": p}, timeout=30,
                )
                resp.raise_for_status()
                return resp.json()
            data = with_retry(_do, description=f"GET articles page {page}")
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


# --- Conversion ---

def html_to_markdown(html: str) -> str:
    class CleanConverter(MarkdownConverter):
        def convert_img(self, el, text, **kwargs):
            src = el.get("src", "")
            alt = el.get("alt", "")
            return f"![{alt}]({src})" if src else ""

        def convert_iframe(self, el, text, **kwargs):
            src = el.get("src", "")
            return f"[{el.get('title', 'Embed')}]({src})" if src else ""

    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["script", "style"]):
        tag.decompose()

    md = CleanConverter(heading_style="atx", bullets="-", strong_em_symbol="**").convert_soup(soup)
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    return "\n".join(line.rstrip() for line in md.split("\n")).strip()


def markdown_to_wp_html(md: str) -> str:
    """Convert markdown back to HTML for WordPress."""
    # WordPress accepts HTML content, so we need to convert back
    # For now, wrap in paragraphs and handle basic formatting
    import re
    lines = md.split("\n")
    html_parts = []
    for line in lines:
        if line.startswith("## "):
            html_parts.append(f"<h2>{line[3:]}</h2>")
        elif line.startswith("### "):
            html_parts.append(f"<h3>{line[4:]}</h3>")
        elif line.startswith("# "):
            html_parts.append(f"<h1>{line[2:]}</h1>")
        elif line.startswith("!["):
            m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", line)
            if m:
                html_parts.append(f'<img src="{m.group(2)}" alt="{m.group(1)}" />')
        elif line.strip():
            html_parts.append(f"<p>{line}</p>")
    return "\n".join(html_parts)


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', "", name)
    name = re.sub(r"\s+", "-", name.strip())
    return name[:120]


# --- Frontmatter ---

def parse_frontmatter(content: str) -> tuple[dict, str]:
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
            meta[key.strip()] = val.strip().strip('"').strip("'")
    return meta, body


def build_frontmatter(fields: dict) -> str:
    lines = ["---"]
    for k, v in fields.items():
        lines.append(f'{k}: "{v}"')
    lines.append("---\n")
    return "\n".join(lines)


# --- Meta files ---

def load_json(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text("utf-8"))
    return {}


def save_json(path: Path, data: dict):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), "utf-8")


# --- Logging ---

class SyncLogger:
    def __init__(self, name: str):
        self.name = name
        self.results = {"success": 0, "skipped": 0, "failed": 0, "errors": []}

    def ok(self, msg):
        self.results["success"] += 1
        print(f"  [OK] {msg}")

    def skip(self, msg):
        self.results["skipped"] += 1

    def fail(self, msg):
        self.results["failed"] += 1
        self.results["errors"].append(msg)
        print(f"  [FAIL] {msg}")

    def summary(self):
        r = self.results
        total = r["success"] + r["skipped"] + r["failed"]
        print(f"\n{'='*50}")
        print(f"  {self.name} Complete")
        print(f"  Total: {total} | OK: {r['success']} | Skip: {r['skipped']} | Fail: {r['failed']}")
        if r["errors"]:
            print(f"  Errors:")
            for e in r["errors"][:5]:
                print(f"    - {e}")
        print(f"{'='*50}")
        return r
