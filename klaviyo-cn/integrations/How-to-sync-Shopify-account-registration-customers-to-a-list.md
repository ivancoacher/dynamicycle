---
id: "4403349019163"
title: "如何将 Shopify 帐户注册客户同步到列表"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4403349019163-How-to-sync-Shopify-account-registration-customers-to-a-list"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: "zh"
---
## 你将会学到

了解如何将通过 Shopify 帐户注册表单收集的订阅者同步到 Klaviyo 列表。如果您想改用 Klaviyo 表单，请阅读[注册表单入门](https://klaviyo.zendesk.com/hc/en-us/articles/360026474752)。

为了实现这一目标，您需要在注册表中添加 **接受营销** 复选框。

## 开始之前

如果您尚未阅读我们的文章[Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify)，了解有关集成的分步说明，然后再继续阅读本文。

确保您已在 Shopify 集成设置中选择要添加到的电子邮件订阅者列表（在 Klaviyo 中，可以通过选择****集成****选项卡，然后在列表中找到 Shopify 并选择它来找到此列表）。该设置可以在 **来自 Shopify** 选项卡上的 **同步设置** 下找到。将复选框添加到表单后，帐户注册客户将添加到该列表中。

![](https://klaviyo.zendesk.com/hc/article_attachments/32924412323739)

## 在您的 Shopify 注册表上启用“接受营销”

为了将在您的 Shopify 网站上注册帐户的客户添加到 Klaviyo 内的列表中，您需要在注册表中添加一些额外的代码，这些代码可以在registration.liquid 文件（或类似文件）中找到。

1. 将以下代码添加到您的注册表中，以添加 **接受营销** 复选框：

   ````
    <div id="accepts_marketing_checkbox">
     <input type="checkbox" name="customer[accepts_marketing]"checked="checked" value="true" id="marketing">
     <label for="营销">是的！注册我以接收有关所有最新儿童的电子邮件。</label>
     </div>
   ````
2. 您需要使用您想要在表单上使用的标签来自定义标签文本。

客户必须选中此框才能添加到您的列表中。

请注意，如果您在 Shopify 中启用了双重选择加入，则客户首先需要通过 Shopify 的双重选择加入电子邮件确认其订阅，然后才能添加到列表中。如果您在 Klaviyo 中为指定列表启用了双重选择加入，则客户需要通过 Klaviyo 的双重选择加入电子邮件确认其订阅，然后才能将其添加到列表中。

您可以通过填写注册表、选中**接受营销**，然后查看您的测试配置文件是否已添加到您选择的列表中来测试此过程是否有效。

## 故障排除

如果您对编辑和添加代码感到不舒服，并且需要开发人员帮助，我们建议您联系 [Klaviyo 合作伙伴机构](https://klaviyo.partnerpage.io/)。

## 结果

您现在正在将 Shopify 帐户注册客户同步到 Klaviyo 列表。