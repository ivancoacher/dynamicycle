---
id: "1260805704029"
title: "对 Klaviyo.js 和网站速度报告进行故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/1260805704029-Troubleshooting-Klaviyo-js-and-site-speed-reports"
section: "Troubleshooting sign-up forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:56:42Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 的现场 JavaScript (Klaviyo.js)，这是您粘贴到网站上以启用**网站上活动**跟踪的代码片段，及其对网站速度的影响。需要安装 Klaviyo.js 才能在您的网站上发布 Klaviyo 注册表单。

如需通过集成启用 **Active on Site** 的帮助，请参阅[如何验证注册表单是否已启用](https://help.klaviyo.com/hc/en-us/articles/360002035871)。

## 排除网站速度性能问题

Klaviyo.js 通过我们的许多[电子商务集成](https://help.klaviyo.com/hc/en-us/articles/115000256472-Understanding-integrations#ecommerce-integrations1) 自动注入，您可以为其他平台手动安装它。它可以显示 Klaviyo 注册表单，并且可以让您跟踪客户何时在您的网站上活跃。

- 如果您发现 Klaviyo 的 JavaScript 影响您网站的性能（即 PageSpeed 分数），并且它是通过集成自动安装的，您可以尝试[手动安装](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration#active-on-site-tracking-snippet)。

  对于 Shopify，我们建议您通过 [Klaviyo 的 Shopify 应用嵌入](https://help.klaviyo.com/hc/en-us/articles/4425956184731) 启用**网站上活动**跟踪，而不是手动安装。这会绕过网站的本机标签管理器，并可以加快 Klaviyo 的 JavaScript 加载速度。
- 如果您不使用 Klaviyo 注册表单（意味着您使用其他工具在网站上创建和发布注册表单），请确保****注册表单**** 选项卡中的所有表单均设置为 **草稿**。

  导航至****注册表单****选项卡，查看每个注册表单的**状态**。 **实时**表示您网站上已发布的表单，**编辑**表示具有未发布更改的实时表单，而**草稿**表示尚未在您网站上发布的表单。

  ![注册表单选项卡显示三个实时表单、编辑表单和草稿表单示例的状态列。](https://klaviyo.zendesk.com/hc/article_attachments/28716066373403)

无论您使用哪种安装方法（例如，通过电子商务集成或手动安装），Klaviyo 的 JavaScript 都是异步加载的。这意味着它不会阻止加载网站的其他方面。然而，Google 的 PageSpeed Insights 和其他网站速度报告可能仍将其标记为影响网站加载时间的因素。

网站速度和 SEO 对我们的客户很重要，Klaviyo 致力于最大限度地减少 JavaScript 的影响。了解我们的[工程师如何优化 klaviyo.js](https://klaviyo.tech/improving-forms-performance-c67c98114d49)。当我们发布新的更新以使 Klaviyo.js 性能更高并缩短加载时间时，您将继续看到改进。

## 其他资源

- [Klaviyo现场追踪入门](https://help.klaviyo.com/hc/en-us/articles/115005076767-Guide-to-Klaviyo-Web-Tracking)
- [第三方集成参考](https://help.klaviyo.com/hc/en-us/articles/360049626051-Third-Party-Integrations)