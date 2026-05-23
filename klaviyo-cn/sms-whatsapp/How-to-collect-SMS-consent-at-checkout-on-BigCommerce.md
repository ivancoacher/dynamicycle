---
id: "360058194032"
title: "如何在 BigCommerce 结帐时收集短信同意"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360058194032-How-to-collect-SMS-consent-at-checkout-on-BigCommerce"
section: "Collect SMS consent at checkout"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:53Z"
language: "zh"
---
## 你将会学到

了解如何在 BigCommerce 结账时开始收集短信同意。这总共大约需要 5-10 分钟。为了方便起见，我们建议登录您的 BigCommerce 和 Klaviyo 帐户并保持两者打开。

****为什么要在结账时收集短信同意？****

在结帐页面上收集短信营销的同意是扩大列表的最简单方法。 BigCommerce 商店可以利用 Klaviyo 的这一优势，让您通过短信营销扩大影响范围。当有人输入电话号码、选择短信营销并在结帐页面上的 **送货** 步骤中单击****继续****时，同意将同步到 Klaviyo，从而轻松扩展您的短信列表。

## 开始之前

请注意，您必须：

- [在 Klaviyo 中打开短信](https://klaviyo.zendesk.com/hc/en-us/articles/4404274419355)。
- [创建移动服务条款](https://klaviyo.zendesk.com/hc/en-us/articles/360049177511)
- 更新您的[隐私政策](https://klaviyo.zendesk.com/hc/en-us/articles/4404199571867)

提示：准备好隐私政策和服务条款的链接，因为您在更新 Klaviyo 集成设置时将需要它们。

您只能在 Klaviyo SMS 可用的情况下收集 SMS 同意。请参阅本文，了解有关[在哪里可以使用 Klaviyo SMS](https://help.klaviyo.com/hc/en-us/articles/4402914866843) 的信息。

## 在 Klaviyo 中：更新您的集成设置

1. 单击左下角您的组织名称。
2. 导航至****集成 > BigCommerce****。
3. 选中****将您的 BigCommerce SMS 订阅者同步到 Klaviyo**** 框。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28705664167835)
4. 选择您希望短信订阅者同步的列表。请注意，如果您还收集电子邮件订阅者，则应使用与电子邮件不同的 SMS 列表。为每个渠道分配单独的列表可确保将同意正确应用于正确的渠道。
5. 在列表下方粘贴您的隐私政策和服务条款的链接。
6. 复制代码片段并将其放在手边。
7. 单击 ****保存**** 保存这些更改并转到您的 BigCommerce 商店。

## 在 BigCommerce 中：通过脚本管理器添加脚本

1. 在您的 BigCommerce 商店中，导航至****店面 > 脚本管理器****。
2. 选择****页脚****作为脚本在页面上的位置。
3. 选择 ****Checkout**** 作为脚本的添加位置。
4. 选择最适用的脚本类别。对于结帐时的短信同意，我们建议您选择 **** 定位；广告****。
   ![在 BigCommerce 结账时添加短信同意的选项](https://klaviyo.zendesk.com/hc/article_attachments/28705664161563)
5. 选择****Script**** 作为脚本类型。
6. 将代码片段粘贴到下面的 **脚本内容** 框中。
   ![结账时粘贴短信同意代码片段的字段](https://klaviyo.zendesk.com/hc/article_attachments/28705664162203)
7. 完成选择并粘贴脚本后，单击****保存****。
8. 可选：如果您想调整该字段在结帐页面上的位置
   1. 前往****高级设置 > 帐户注册表****。
      ![BigCommerce 高级设置下的帐户注册表单页面](https://klaviyo.zendesk.com/hc/article_attachments/28705637369499)
   2. 单击进入****地址字段****选项卡。
   3. 将电话号码字段移至列表底部。

## 结果

您的结帐页面现在将类似于下图所示。

![可以收集短信同意的 BigCommerce 结账页面示例](https://klaviyo.zendesk.com/hc/article_attachments/28705664165403)

现在，当有人输入电话号码，选中接受短信营销的复选框，然后点击“送货”部分中的“继续****”时，他们将自动同步到您指定的 Klaviyo 列表，从而更轻松、更快速地扩大您的短信列表。

## 其他资源

- 了解[同时使用短信和电子邮件的基础知识](https://help.klaviyo.com/hc/en-us/articles/360056849631)。
- 了解[如何将嵌入式表单添加到您的网站](https://help.klaviyo.com/hc/en-us/articles/360022594552)。
- 想要停止收集短信订阅者吗？阅读这篇[关于在结帐时禁用短信同意的文章。](https://help.klaviyo.com/hc/en-us/articles/360058194372)