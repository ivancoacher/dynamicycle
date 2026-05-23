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
KLAVIYO_DIR = PROJECT_ROOT / "klaviyo"
BATTERDOCS_DIR = PROJECT_ROOT / "batterDocs"
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)

WP_SITE_URL = os.getenv("WP_SITE_URL", "").rstrip("/")
WP_USERNAME = os.getenv("WP_USERNAME", "")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD", "")
WP_API_BASE = os.getenv("WP_API_BASE", "/wp-json/wp/v2")

ZENDESK_API = "https://help.klaviyo.com/api/v2/help_center/en-us"

# batterDocs category slug -> WP term ID
WP_CATEGORY_IDS = {
    "account-billing": 775425969,
    "advanced-kdp-marketing-analytics": 775425957,
    "analytics-audience": 775425956,
    "campaigns": 775425959,
    "content": 775425958,
    "conversations": 775425960,
    "customer-agent": 775425976,
    "customer-hub": 775425961,
    "dc-resources": 775425962,
    "deliverability-compliance": 775425963,
    "faq": 775425978,
    "flows": 775425971,
    "helpdesk": 775425977,
    "integrations": 775425972,
    "reviews": 775425973,
    "sign-up-forms": 775425974,
    "sms-whatsapp": 775425975,
}

# Klaviyo category ID -> batterDocs slug
KLAVIYO_CATEGORY_MAP = {
    115000867647: "account-billing",
    18073014919195: "advanced-kdp-marketing-analytics",
    115000874048: "analytics-audience",
    115000867867: "analytics-audience",
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
    29173800271259: "sms-whatsapp",
    49375107982619: "sms-whatsapp",
    50128030093211: "content",
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
        try:
            return fn()
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                requests.exceptions.ProxyError) as e:
            delay = base_delay * (2 ** (attempt - 1))
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

    def create_doc(self, title, content, category_slug, status="publish"):
        cat_id = WP_CATEGORY_IDS.get(category_slug)
        if not cat_id:
            print(f"  WARN: unknown category '{category_slug}'")
            cat_id = 775425978  # fallback to FAQ

        def _do():
            resp = requests.post(
                self._url("/docs"),
                json={
                    "title": title,
                    "content": content,
                    "status": status,
                    "doc_category": [cat_id],
                },
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"CREATE: {title[:40]}")

    def update_doc(self, doc_id, title=None, content=None):
        payload = {"status": "publish"}
        if title:
            payload["title"] = title
        if content is not None:
            payload["content"] = content

        def _do():
            resp = requests.post(
                self._url(f"/docs/{doc_id}"),
                json=payload,
                auth=self.auth, timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        return with_retry(_do, description=f"UPDATE: doc #{doc_id}")


class ZendeskClient:
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
                all_sections[s["id"]] = {"name": s["name"], "category_id": s.get("category_id")}
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
