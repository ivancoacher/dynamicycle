---
id: "14477037350299"
title: "如何启用 PrestaShop 价格包含增值税"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/14477037350299-How-to-enable-PrestaShop-price-include-VAT"
section: "PrestaShop"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T11:01:11Z"
language: "zh"
---
## 你将会学到

了解如何在 PrestaShop 商店的列出价格中包含增值税（税）并将含税价格数据同步到 Klaviyo。您的 PrestaShop 价格数据将与您的 Klaviyo 产品目录以及 **查看的产品** 和 **添加到购物车** 事件同步。

要开始同步包含增值税的价格数据，您可以[手动](https://help.klaviyo.com/hc/en-us/articles/14477037350299#manually-update-existing-prestashop-integrations3)或在[Klaviyo]的帮助下更新您的集成支持](https://help.klaviyo.com/hc/en-us/articles/14477037350299#support-assistance-update-existing-prestashop-integrations4)。

## 开始之前

当您重新集成或更新集成时，您必须安装 Klaviyo 模块版本 1.2.10 或更高版本才能同步包含增值税的价格数据。由于[我们的 v1/v2 API 已停用](https://help.klaviyo.com/hc/en-us/articles/360054551492#h_01HD6YRW7VWJQKBXTN7TGA7N88)，我们强烈建议您在 2024 年 6 月 30 日之前将 PrestaShop 模块升级到版本 1.4.1 或更高版本。升级到版本 1.4.1 或更高版本将使您能够利用优惠券生成和实时交易事件同步，这些功能首次在 1.3.0 上发布。

## 启用含增值税价格

### 手动更新现有 PrestaShop 集成

1. 从 Klaviyo 中删除 PrestaShop 集成。
2. 从 PrestaShop 中删除并卸载 Klaviyo 模块。
3. 根据需要更新任何电子邮件模板，例如，应删除对商品价格应用乘数的任何地方。
4. 按照我们的[PrestaShop 入门](https://help.klaviyo.com/hc/en-us/articles/360054551492) 指南，将 PrestaShop 与 Klaviyo 重新集成。确保安装 Klaviyo 模块版本 1.2.10 或更高版本以同步包含增值税的价格数据。

### 支持协助更新现有 PrestaShop 集成

1. 关闭消息引用产品目录中的商品价格数据的所有流程和活动，例如任何产品块。
2. 根据需要更新任何电子邮件模板，例如，应删除对商品价格应用乘数的任何地方。
3. 将 Klaviyo 模块更新至版本 1.2.10 或更高版本。
4. [联系 Klaviyo 支持](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272) 寻求帮助，以含税价格回填您现有的产品目录产品。
5. 当含增值税价格的产品目录回填完成后，您的支持代表将与您联系。
6. 重新启用消息引用产品目录中的商品价格数据的任何流程和活动。

## 含增值税价格数据

### 事件数据

在使用 1.2.10 或更高版本设置或更新集成后，下面的含增值税价格字段将包含在您的“查看产品”和“添加到购物车”事件中。

查看的产品：“含税价格”

添加到购物车：`AddedItemPriceInclTax`

这些附加价格字段仅在未来有效。增值税字段不会回填到现有的“查看产品”和“添加到购物车”事件中。

### 目录数据

2023 年 1 月 25 日之后使用 Klaviyo 模块版本 1.2.10 或更高版本创建的所有 Prestashop 集成都会将 PrestaShop 的**含增值税**价格同步到您的产品目录中。

2023 年 1 月 25 日之前创建的所有 Prestashop 集成都会将增值税**独家**价格同步到您的产品目录中。

## 结果

恭喜！您已成功更新 PrestaShop 集成，以使用产品目录中的含增值税价格数据。您的**添加到购物车**和**查看产品**事件将捕获包含增值税价格的数据。

## 其他资源

- [PrestaShop 入门](https://klaviyo.zendesk.com/hc/en-us/articles/360054551492)
- [PrestaShop数据参考](https://klaviyo.zendesk.com/hc/en-us/articles/360055123191)