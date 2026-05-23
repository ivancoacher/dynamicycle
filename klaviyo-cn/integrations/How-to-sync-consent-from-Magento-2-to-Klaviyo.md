---
id: "5510558435739"
title: "如何将同意从 Magento 2 同步到 Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/5510558435739-How-to-sync-consent-from-Magento-2-to-Klaviyo"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: "zh"
---
## 概述

当您将 Magento 2 商店与 Klaviyo 集成时，有许多选项可以将 Magento 中捕获的同意同步到 Klaviyo。

在集成过程中配置您的同意同步选项非常重要，因为它们不能追溯。

下表概述了每个同步选项

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|设置|报名地点 |速度|双重选择加入 |历史数据| $源值|添加到事件列表 |
| Klaviyo 集成复选框 |帐户注册和 Magento 新闻通讯表格 |作为定期同步的一部分进行订阅（每 30 分钟一次）|即使启用也不会被触发 |如果在历史同步开始之前启用，将同步历史客户 |无 |未触发 |
| Klaviyo Magento 扩展时事通讯设置 | Magento 时事通讯表格 |实时 |如果启用则可以触发（可定制）|未同步 |应用程序接口 |触发 |
| Klaviyo Magento 扩展结帐设置 |结帐时的复选框 |实时 |如果启用将触发 |未同步 |玛根托 |触发 |

## 获取帐户注册用户的同意

如果您为客户提供注册帐户并同时注册您的新闻通讯的选项，他们的同意状态可以同步到 Klaviyo。

您需要在您的 Klaviyo 帐户中启用“向 Klaviyo 列表订阅新客户”设置****（****不是 Magento 扩展）。它位于集成 -> Magento 2

即使您为所选列表配置了双重选择加入，客户也不会收到双重选择加入电子邮件。

选择此设置会将所有新客户同步到 Klaviyo，作为定期同步（大约每 30 分钟）的一部分，包括新闻通讯表中的所有客户。如果您为新闻通讯表单同步指定不同的 Klaviyo 列表（请参阅[通过 Magento 新闻通讯表单获取同意](https://docs.google.com/document/d/1rlWkN0Y03eINGtJiM3W-hfqWipVsDQjMxYnTDe7_zC8/edit#heading=h.99a19ljrnvpv)），那么您将看到这些客户同步到两个列表。

请务必在设置集成时检查此设置，以便 Klaviyo 将所有历史简讯订阅者同步到指定的 Klaviyo 列表。

## 通过 Magento 时事通讯表格获取同意

如果您通过本机 Magento 时事通讯表单获取同意，则需要在 Klaviyo 的 Magento 扩展上启用一项设置，以将该订阅同步到 Klaviyo。

该信息实时同步到 Klaviyo。

使用此功能时，您可以选择遵守或覆盖列表的双重选择加入设置。

****注意：**** **此设置仅适用于启用该设置后订阅的客户。它不会同步先前订阅客户的同意**

## 在结账时获取同意

您可以使用 Klaviyo 扩展程序在结账时获取同意。启用此选项后，结帐时将添加一个复选框，客户在完成购买后将实时订阅所选列表。

您可以通过调整“排序顺序”来调整此复选框在页面上的位置。数字越大，结账页面越靠下。

如果您为所选列表启用了双重选择加入，客户将收到一封双重选择加入确认电子邮件。