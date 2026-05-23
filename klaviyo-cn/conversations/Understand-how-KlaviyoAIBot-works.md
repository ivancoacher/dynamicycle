---
id: "40496146232219"
title: "了解 KlaviyoAIBot 的工作原理"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40496146232219-Understand-how-KlaviyoAIBot-works"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-21T13:56:56Z"
language: "zh"
---
了解 KlaviyoAIBot，包括：

- 它是什么以及它爬行什么
- 如何识别真实请求
- 爬行如何尊重网站规则以及如何控制它

本文适用于看到 KlaviyoAIBot 流量并想要确认其是否合法或调整允许其抓取方式的任何人。 ## KlaviyoAIBot 是什么？ KlaviyoAIBot 是 Klaviyo 的网络爬虫，用于其 Kai 客户代理功能。 KlaviyoAIBot 从您已明确连接到您的帐户的域和 URL 中获取公开可用的页面。通过索引这些内容，Klaviyo 可以在您的网站和 Klaviyo 平台内定制 AI 体验。这对于内容生成、人工智能答案和产品推荐非常有用。您可以添加主店面之外的来源，包括帮助中心（例如 Zendesk）、博客和新闻文章。 KlaviyoAIBot 不会绕过身份验证、付费墙或访问控制。 ## 它是如何工作的

- ****同意和范围****
  Klaviyo 会抓取您已明确连接到您的帐户的域和 URL。例如，它会抓取与您的 Klaviyo 帐户集成的任何公共 Shopify 页面，但不会在维基百科中搜索相关内容。 - ****尊重网站规则****
  KlaviyoAIBot 只抓取您想要抓取的内容，遵循 中定义的机器人排除协议 (REP)。 -****礼貌****。如果您的站点发出速率限制信号，Klaviyo 会自动降低其速率。 Klaviyo 遵循标准 HTTP 响应，例如 503 或 503 以及标头。 - ****重访****
  Klaviyo 会定期重新爬行以保持内容新鲜。频率根据变化信号和您的配置而变化。 ## 如何识别KlaviyoAIBot

KlaviyoAIBot 使用 2 个互补信号。如果您看到声称是 KlaviyoAIBot 的请求未通过签名验证（或未被 Cloudflare 标记为经过验证的机器人），请将其视为不可信。 ###

KlaviyoAIBot/1.0 (+https://help.klaviyo.com/hc/en-us/articles/<article\_id>)

### HTTP 消息签名（网络机器人身份验证）

每个请求均使用 [HTTP 消息签名 RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) 和 Cloudflare 的 [Web Bot Auth](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/web-bot-auth/) 进行签名。您可以使用它来验证请求是否真正来自 KlaviyoAIBot，而无需依赖 IP 白名单。 ****提示****：如果您的网站位于 Cloudflare 后面，Cloudflare 将为您验证 Klaviyo 的签名，并将流量标记为已验证的机器人（cf.bot\_management.verified\_bot = true）。您可以在 WAF 规则中使用该字段安全地允许它。 ****我看到流量显示它是 KlaviyoAIBot。我怎么知道它是真的？****
如果您使用 Cloudflare，请确认请求已标记为经过验证的机器人。如果您不使用 Cloudflare，请验证请求是否包含根据 RFC 9421 和 Web Bot Auth 进行验证的 HTTP 消息签名标头。 ## KlaviyoAIBot 爬行的内容

- ****您的电子商务商店****
  连接到 Klaviyo 的电子商务域。 - ****其他来源****
  连接到您网站的任何其他来源，例如帮助中心（例如 Zendesk）、文档门户、知识库、博客和客户连接的新闻文章。 - ****公共内容****
  KlaviyoAIBot 尊重 robots.txt 中的机器人规则，并且不会尝试访问门禁资源。 ### 如何控制或限制爬行

- R****obots.txt****
  添加或更新 KlaviyoAIBot 用户代理的机器人规则以允许或禁止部分。详细了解 [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt) 和 [REP](https://datatracker.ietf.org/doc/html/rfc9309)。 - ****暂时放缓****
  返回标准速率限制响应，例如 [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) 或带有 [Retry-After](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) 的 503，以在不更改机器人规则的情况下降低速率。 - ****选择连接的内容****
  您可以随时添加或删除想要连接的域和 URL。 ****我可以屏蔽网站的特定部分吗？****
是的。在 robots.txt 中使用 KlaviyoAIBot 的机器人规则来禁止这些路径。如果您不知道如何操作，请联系

****机器人是否遵守临时减速信号？****
是的。标准速率限制响应（例如 429 或 503 以及 Retry-After）受到尊重。 ## 数据使用和隐私

KlaviyoAIBot 检索内容以支持 AI 功能，例如内容生成、AI 答案和产品推荐。抓取的内容与您的帐户绑定并遵循您的设置。只要源页面保持公开可用，Klaviyo 就会定期更新索引内容以使其保持最新状态。当某个页面通过 robots.txt 受到限制或从源站点中删除时，Klaviyo 会在几天内删除相应的索引内容。当您断开某个来源与您的帐户的连接时，Klaviyo 会立即删除相关内容。 ****你们公布IP范围吗？****

不会。验证基于加密签名和 Cloudflare 的 Verified bots 程序，而不是静态 IP 白名单。