# Dynamicycle Docs

BetterDocs 文档同步仓库。

## 关键路径

- `batterDocs/` — 按分类组织的 markdown 文档（17 个分类，82+ 篇文章）
- `sync/sync.py` — Python 同步工具（pull/push/status）
- `.env` — WP 认证信息（已 gitignore）

## 常用命令

```bash
python3 sync/sync.py pull    # 从 BetterDocs 拉取文档
python3 sync/sync.py status  # 对比本地与远程差异
python3 sync/sync.py push    # 推送本地修改到 BetterDocs
```

## 文档格式

每篇文章包含 YAML frontmatter：

```yaml
---
id: 1234
title: "文章标题"
slug: "article-slug"
category: "分类名称"
category_slug: "category-slug"
wp_url: "https://dynamicycle.com/docs/article-slug/"
wp_modified: "2025-01-01T00:00:00"
---
```

## 数据流

1. `pull`: BetterDocs API → HTML → Markdown → git
2. `push`: git → Markdown → BetterDocs API
3. （待开发）Klaviyo help docs → 翻译/转换 → batterDocs → push
