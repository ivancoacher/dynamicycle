---
id: "360055336451"
title: "如何为 Magento 2 启用 webhook"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360055336451-How-to-enable-webhooks-for-Magento-2"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:52Z"
language: "zh"
---
## 你将会学到

了解如何启用 Klaviyo webhooks，这将使您的 Magento 2 集成能够实时同步目录产品删除，并在结帐时启用同意。

## 开始之前

如果您尚未启用 Magento 2 集成，则需要完成 [Magento 2 集成指南](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-) 中概述的设置步骤，其中还包括有关启用 Klaviyo webhooks 的说明。

## 启用网络钩子

1. 登录您的 Magento 2 帐户并从管理仪表板导航至****Stores > Configuration****。
2. 单击 ****Klaviyo**** 并选择 ****Webhooks**** 选项卡。！[显示商店配置仪表板的 Webhooks 选项卡的图像。](https://klaviyo.zendesk.com/hc/article_attachments/28720658704411)
3. 创建一个 Webhook Secret 并将其输入到相应的 ****Webhook Secret**** 字段中。 Webhook 密钥是 Klaviyo 将用于验证的密钥。此秘密可以是您选择的任何内容，但我们建议创建一个安全的字母和数字字符串。出于安全目的，Magento 会用星号隐藏您的 webhook 秘密，因此请小心正确输入。
   如果您使用多商店集成，则应在默认配置中输入此字段中的 Webhook 密钥，并且相同的密钥将用作每个商店配置的验证。 Webhook 密钥只能添加到默认配置中，而不应该为每个商店添加。
4. 在 **使用产品删除 Webhook？** 旁边，从下拉选项中选择 ****是****。 **产品删除** Webhook 允许集成从 Klaviyo 的目录中删除您在 Magento 2 中删除的产品。
5. 单击****保存配置****完成设置。您的 Magento 2 集成现在将从目录中实时删除已删除的产品。

## 其他资源

- [如何与 Magento 2.x（CE 和 EE）集成](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348)
- [查看您的 Magento 2 数据](https://klaviyo.zendesk.com/hc/en-us/articles/115003458852)