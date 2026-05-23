---
id: "35094079400219"
title: "客户中心中电子邮件和短信同意收集指南"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/35094079400219-Guide-to-email-and-SMS-consent-collection-in-the-Customer-Hub"
section: "Getting started with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:40Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 如何通过客户中心现场体验从个人资料中收集电子邮件和短信同意。 Shopify 客户中心目前支持标准店面和 Shopify Headless。对于 WooCommerce，请导航至 https://help.klaviyo.com/hc/en-us/articles/47792369863451

有关客户中心功能的反馈，请发送电子邮件至 customerhub@klaviyo.com。 ## 开始之前

要在客户中心界面中收集电子邮件或短信同意，请首先确保您已在 Klaviyo 帐户中完成以下步骤：

- [在 Klaviyo 中启用客户中心](https://help.klaviyo.com/hc/en-us/articles/33660324811675)
- 如果您打算收集短信同意
  - [在 Klaviyo 中打开短信](https://help.klaviyo.com/hc/en-us/articles/4404274419355)
  - 设置您的披露语言，包括：
    - 创建[移动服务条款](https://help.klaviyo.com/hc/en-us/articles/360049177511)
    - 更新您的[隐私政策](https://help.klaviyo.com/hc/en-us/articles/360049177511)

请注意，客户中心中的 SMS 同意收集仅适用于 Klaviyo SMS 计划的用户。如果您使用其他短信提供商，请[禁用短信同意收集设置](https://help.klaviyo.com/hc/en-us/articles/35094079400219#h_01JWAE1A2R3S6SXFA7XAC0KK83)。此外，短信同意收集目前不适用于 [需要年龄限制的 Klaviyo 品牌](https://help.klaviyo.com/hc/en-us/articles/17252552814875#h_01H9NZT3W40TBKBXGFQHKCEYRZ)。 ## Customer Hub 如何连接到 Shopify 帐户

要了解 Klaviyo 如何通过客户中心收集同意，首先了解它如何与 Shopify 账户集成会很有帮助。当您的网站启用客户中心功能时：

- 客户中心抽屉体验取代了默认的 Shopify 帐户登录页面。上线后，单击帐户图标或访问网站上的任何 /account 页面都会自动打开客户中心界面，并提示登录。 - 客户数据从 Shopify 帐户同步到 Klaviyo，允许配置文件使用其现有的 Shopify 凭据登录。如果配置文件没有 Klaviyo 配置文件，则会在登录时创建一个。 - Klaviyo 使用此数据来识别哪些个人资料已经订阅了短信营销，并在客户中心抽屉的 **个人资料** 选项卡上准确显示他们的个人信息。 ## 在客户中心收集同意

在 Klaviyo 中，您可以控制是否在客户中心界面中要求个人资料获得电子邮件和短信营销同意。对于短信同意收集：

- ****如果您在 Klaviyo 中有有效的短信计划****：默认情况下启用客户中心界面中的短信同意收集。 - ****如果您没有 Klaviyo SMS 计划****：短信同意收集将自动禁用，因此不会要求网站访问者在客户中心订阅短信。 ### 需要同意的地方

有 2 个地方可能会要求个人资料同意：

1.****客户中心登录****：使用电子邮件登录后，当前还不是电子邮件或短信订阅者的访问者会被提示提供电子邮件和/或电话号码并同意电子邮件和/或短信营销（下表中的左图）。 2. ****在“客户中心”抽屉中编辑个人资料信息页面****：登录的个人资料可以直接在“客户中心”的个人资料选项卡中的“编辑个人资料”页面中管理其渠道同意。 |  |  |
| --- | --- |
|客户中心登录同意请求插页式 |编辑个人资料页面-营销同意管理|
| ![](https://klaviyo.zendesk.com/hc/article_attachments/44083736752667) | ![](https://klaviyo.zendesk.com/hc/article_attachments/44083755248667) |

默认情况下包含您帐户的披露语言。请注意，客户中心界面不支持智能选择加入和点击文本，并且这些页面上的文本和按钮标签也无法自定义。 Klaviyo 仅向尚未订阅短信营销的访客索要电话号码。如果网站访问者在登录期间跳过短信同意提示，他们在 30 天内不会在登录时看到其他提示。 ### 在客户中心双重选择短信同意

Klaviyo 通过客户中心界面对所有 SMS 注册使用双重选择加入流程。此两步验证流程可确保客户明确同意接收 SMS 营销消息。这个过程如下：

1. 访问者提供他们的电话号码，选中 **注册短信营销** 复选框，然后单击 ****继续****。 2. 客户中心界面中的加载屏幕告诉他们检查消息。 ![客户中心界面中的加载屏幕指示某人回复“是”以确认短信同意订阅。](https://klaviyo.zendesk.com/hc/article_attachments/37621292472731)
3. 他们会收到一条自动短信，要求他们确认订阅（例如，回复“是”）。 4. 一旦他们确认，他们的 Klaviyo 个人资料就会更新为 **订阅** SMS 状态，并且 **订阅 SMS 营销** 指标会记录在他们的活动中。如果网站访问者输入电话号码但未通过短信确认订阅，则他们不会被标记为已订阅，并且以后在客户中心登录时也不会再次收到短信同意提示。不过，他们仍然可以在 **编辑个人资料** 页面上订阅短信营销。同样，如果访问者在之前订阅后取消订阅短信营销，他们在登录时将不会再次看到短信同意请求，但他们可以选择从客户中心界面中的 **编辑个人资料** 页面重新订阅。 ## 在客户中心配置同意收集

要在客户中心界面中选择要请求同意的渠道：

1. 在 Klaviyo 的主导航中，选择****服务 - 客户中心****。 2. 单击 ****设置****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/40773879688091)
3. 滚动到 **营销同意** 部分，然后取消选中复选框以禁用
   ![](https://klaviyo.zendesk.com/hc/article_attachments/44083736758939)
4. 单击 ****保存****。 ## 常见问题解答

#### 我已经可以在没有获得明确电子邮件同意的情况下向我的客户发送电子邮件。收集他们的电子邮件同意有什么价值？电子邮件同意是一个微妙的话题。虽然在发送任何营销信息之前明确需要短信同意，但并不总是需要电子邮件同意。要了解什么最适合您的品牌，请参阅：

- [了解显式同意与隐式同意](https://klaviyo.zendesk.com/hc/en-us/articles/4404203889947)
- [了解个人资料中的同意](https://klaviyo.zendesk.com/hc/en-us/articles/360037101072)
- [电子邮件送达最佳实践参考](https://klaviyo.zendesk.com/hc/en-us/articles/25620771311643)

## 其他资源

- [客户中心入门](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675)
- [短信选择加入方法参考](https://klaviyo.zendesk.com/hc/en-us/articles/27902671291419)
- [了解客户中心仪表板](https://klaviyo.zendesk.com/hc/en-us/articles/33660382797595)