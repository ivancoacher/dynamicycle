#!/usr/bin/env python3
"""Migrate existing English articles to sub-categories under 775425988.

- Creates sub-categories under "Kalaviyo 官方文档" (775425988)
- Updates all pushed EN articles to new sub-categories
- Saves category mapping for future sync
"""

import json
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

WP = os.getenv("WP_SITE_URL", "").rstrip("/")
AUTH = (os.getenv("WP_USERNAME", ""), os.getenv("WP_APP_PASSWORD", ""))
PARENT_CAT_ID = 775425988

CATEGORY_MAP_FILE = PROJECT_ROOT / "klaviyo-en" / ".category_map.json"

# Klaviyo category slug -> display name (Chinese)
KLAVIYO_SLUG_NAMES = {
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

# Old WP category IDs (top-level) that EN articles currently belong to
OLD_WP_CATS = {
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


def api(endpoint, method="GET", json_data=None):
    url = f"{WP}/wp-json/wp/v2{endpoint}"
    for attempt in range(5):
        try:
            if method == "GET":
                resp = requests.get(url, params=json_data, auth=AUTH, timeout=30)
            else:
                resp = requests.post(url, json=json_data, auth=AUTH, timeout=30)
            if resp.status_code == 429:
                time.sleep(int(resp.headers.get("Retry-After", 5)))
                continue
            resp.raise_for_status()
            return resp.json()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            delay = 2 ** attempt
            print(f"  Retry {attempt+1}/5: {e}, waiting {delay}s...")
            time.sleep(delay)
    raise Exception(f"Failed after 5 retries: {endpoint}")


def step1_create_subcategories():
    """Create sub-categories under 775425988."""
    print("=" * 50)
    print("Step 1: Creating sub-categories")
    print("=" * 50)

    cat_map = load_category_map()

    for slug, name in KLAVIYO_SLUG_NAMES.items():
        if slug in cat_map:
            print(f"  EXISTS: {name} → WP cat #{cat_map[slug]}")
            continue

        result = api("/doc_category", method="POST", json_data={
            "name": name,
            "slug": f"klaviyo-{slug}",
            "parent": PARENT_CAT_ID,
        })
        new_id = result["id"]
        cat_map[slug] = new_id
        print(f"  CREATED: {name} → WP cat #{new_id}")
        save_category_map(cat_map)
        time.sleep(0.5)

    print(f"\nCategory map saved to {CATEGORY_MAP_FILE}")
    return cat_map


def step2_update_articles(cat_map):
    """Update all pushed EN articles to new sub-categories."""
    print("\n" + "=" * 50)
    print("Step 2: Updating article categories")
    print("=" * 50)

    push_meta = json.loads(
        (PROJECT_ROOT / "klaviyo-en" / ".push_en_meta.json").read_text("utf-8")
    )
    pushed = push_meta.get("pushed", {})
    print(f"Total articles to update: {len(pushed)}")

    updated = 0
    failed = 0
    for aid, info in pushed.items():
        # Extract category slug from filename
        cat_slug = info["filename"].split("/")[0]
        new_cat_id = cat_map.get(cat_slug)

        if not new_cat_id:
            print(f"  SKIP (no mapping): {cat_slug} - {info['title'][:40]}")
            continue

        try:
            api(f"/docs/{info['wp_id']}", method="POST", json_data={
                "doc_category": [new_cat_id],
            })
            updated += 1
            if updated % 50 == 0:
                print(f"  Progress: {updated}/{len(pushed)}")
        except Exception as e:
            failed += 1
            print(f"  FAIL: WP#{info['wp_id']} {info['title'][:40]}: {e}")
            if failed > 5:
                print("  Too many failures, stopping")
                break

        time.sleep(0.3)

    print(f"\nDone. Updated: {updated}, Failed: {failed}")


def load_category_map():
    if CATEGORY_MAP_FILE.exists():
        return json.loads(CATEGORY_MAP_FILE.read_text("utf-8"))
    return {}


def save_category_map(cat_map):
    CATEGORY_MAP_FILE.write_text(
        json.dumps(cat_map, indent=2, ensure_ascii=False), "utf-8"
    )


if __name__ == "__main__":
    cat_map = load_category_map()
    if not cat_map:
        cat_map = step1_create_subcategories()
    step2_update_articles(cat_map)
