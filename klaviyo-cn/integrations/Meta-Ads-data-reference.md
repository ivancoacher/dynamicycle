---
id: "360039002832"
title: "元广告数据参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360039002832-Meta-Ads-data-reference"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-17T00:33:08Z"
language: "zh"
---
## 你将会学到

了解通过 Klaviyo 的 Meta Ads 集成从 Meta Ads 同步到 Klaviyo 以及从 Klaviyo 同步到 Meta 的数据。

## 开始之前

在数据流入您的 Klaviyo 帐户之前，您必须首先[与元广告集成](https://klaviyo.zendesk.com/hc/en-us/articles/115005082127)，其中包括将 Klaviyo 列表或细分与元受众同步，和/或同步线索广告。

## 与元受众同步的数据

您可以将 Klaviyo 列表和细分与元受众同步。 Klaviyo 以单向同步方式将电子邮件地址推送给元受众。由于 Meta 限制，自定义受众可能需要 24-48 小时才能在 Meta 中更新。

这是 Klaviyo 和 Meta 受众之间数据同步的方式：

- Klaviyo 将电子邮件地址推送给元受众。
- 只有与 Facebook 登录关联的电子邮件地址才会同步，因此您的受众规模可能与您的列表/细分受众群的规模不完全匹配。
- 当配置文件从列表或细分中添加或删除时，它们也将从元受众中添加或删除。

## 从潜在客户广告表单同步的数据

当您将潜在客户广告表单连接到 Klaviyo 列表时，个人资料信息将添加到您选择的列表中。只有列表（而不是分段）可以与潜在客户广告表单同步。潜在客户广告表单可以放置在 Facebook 或 Instagram 上，因此可以从任一社交媒体来源提取个人资料信息。来自线索广告的数据实时同步到 Klaviyo。

### 个人资料信息

潜在客户广告表单的设计决定了将哪些信息提取到 Klaviyo 中。例如，包含**电子邮件地址**和**名字**字段的线索广告将提取该信息。如果您在潜在客户广告表单中添加 **电话号码** 字段，系统也会提取电话号码。

### 填写的潜在客户广告指标

当一个人通过潜在客户广告表单注册时，该人的个人资料信息将与**填写的潜在客户广告**指标同步到 Klaviyo。

在 Klaviyo 中，您可以导航到帐户的****指标****选项卡（在****分析****下拉列表中）以查看帐户中的所有指标； **填写的潜在客户广告**指标与元图标相关联。您可以使用过滤器选择器过滤此视图以仅查看元广告指标。

当用户通过 Facebook 或 Instagram 上的潜在客户广告表单进行订阅时，就会触发 **填写的潜在客户广告** 指标。该指标与称为元数据的附加属性相关联。

这是与 **Filled Out Lead Ad** 指标相关的元数据列表：

- ****广告ID****
  广告表单 ID；这可以位于您的 Facebook 广告帐户中
- ****广告名称****
  广告名称
- ****广告名称****
  父广告集的名称
- ****活动名称****
  包含广告的营销活动的名称
- ****表格名称****
  潜在客户广告同步标签
- ****页面名称****
  广告展示的页面
- ****平台****
  广告出现的平台：Facebook (fb) 或 Instagram (ig)

Klaviyo 使您能够根据提取到您帐户中的所有指标和元数据进行过滤和细分，以便您可以在粒度级别上自定义您的客户旅程。

## 其他资源

- [如何与元广告集成](https://help.klaviyo.com/hc/en-us/articles/115005082127-How-to-Integrate-with-Facebook-Advertising)
- [Facebook 和 Instagram 上的高级定位入门](https://help.klaviyo.com/hc/en-us/articles/360039769672-Guide-to-Advanced-Targeting-on-Facebook-and-Instagram)