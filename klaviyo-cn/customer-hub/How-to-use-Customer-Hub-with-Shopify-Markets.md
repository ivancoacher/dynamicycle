---
id: "44768355991195"
title: "如何将客户中心与 Shopify Markets 结合使用"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/44768355991195-How-to-use-Customer-Hub-with-Shopify-Markets"
section: "Build and use Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:55:01Z"
language: "zh"
---
## 你将会学到

了解如何将 Shopify Markets 与客户中心集成，以确保您的产品信息、货币和定价与客户正在浏览的本地“市场”环境相匹配。

## 要求

- 您必须拥有配置了 [****Shopify Markets****](https://help.shopify.com/en/manual/international/managing) 的 Shopify 商店。
- 您必须安装并激活****Klaviyo Customer Hub****。

## 概述

如果您使用 Shopify Markets 在多个区域进行销售，客户中心可以自动适应客户的位置并向他们显示适合该市场的产品信息。

通过与 Shopify Markets 集成，客户中心可确保门户中显示的产品信息、货币和定价与本地环境相匹配。

## 它是如何工作的

当客户访问您的网站时，Shopify 会检测他们的国家/地区和区域设置（通常基于 IP 地址或货币选择器）。客户中心支持此检测。

当在 Klaviyo 中启用 Shopify Markets 支持时，客户中心将：

- ****本地化产品目录：**** 产品名称、描述和可用性将与 Shopify 中的特定市场设置相匹配。
- ****显示本地货币：**** 订单、最近购买和产品推荐将显示该特定市场的正确货币和价格。
- ****与现场语言保持一致：**** 中心中显示的语言将尝试与您的 Shopify 店面当前使用的语言相匹配。

> ****注意：**** 虽然客户中心支持本地化，但 ****AI Agent**** 和 ****Inbox**** 功能目前仅支持英语。

##

## 如何设置 Shopify Markets 支持

Shopify Markets 支持在客户中心自动无缝运行，无需任何设置。对于使用旧版 Shopify 集成的现有客户，您可能需要确认您已为 Klaviyo 提供了正确的范围。确认方法如下：

- 在 Klaviyo 中，导航至****服务 -********客户中心****
- 在仪表板上，如果您看到此警告，请单击“修复 Shopify”并按照说明进行操作
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44768361282075)
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44768355990171)
- 如果您没有看到警告，则表明您的 Shopify 集成已经是最新的，并且 Shopify Markets 支持正常工作。

如果您的 Shopify 集成已过时，客户中心的大部分功能仍可与 Shopify Markets 配合使用（例如显示正确翻译的产品名称、货币符号、价格），但产品可能会显示在客户中心内不可用的市场中，例如在推荐、最近查看和收藏的产品中。

## 故障排除

****为什么显示错误的货币？**** 客户中心依赖于您的主题检测到的“window.Shopify.country”和市场背景。确保您的 Shopify 主题在用户更改其区域时正确切换上下文。

****为什么中心中缺少某些产品？**** 如果产品未在您的 Shopify 设置中发布到特定市场，则该产品不会出现在该地区客户的客户中心中。

##