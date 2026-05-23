---
id: "115005073907"
title: "了解 Klaviyo 何时以及如何设置配置文件的位置"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005073907-Understanding-when-and-how-Klaviyo-sets-a-profile-s-location"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-18T18:44:56Z"
language: "zh"
---
## 你将会学到

了解在哪里可以找到个人资料的位置信息、如何使用和更新个人资料等等。同步或创建新配置文件时，Klaviyo 根据配置文件的帐单地址确定位置和时区信息。如果尚未购买配置文件，则位置和时区将根据 IP 地理位置确定。 ## 在个人资料中查找位置信息

您可以通过导航到 Klaviyo 中的个人资料页面来找到个人资料的位置，该位置与任何联系信息一起显示在标题中。 ![个人资料页面顶部](https://klaviyo.zendesk.com/hc/article_attachments/33101716556571)

## Klaviyo 中的位置如何使用和更新

[根据收件人的时区发送](https://help.klaviyo.com/hc/en-us/articles/115005054847#schedule-and-send-your-campaign6)、[创建基于位置的段](https://help.klaviyo.com/hc/en-us/articles/115005065887)，或向流添加特定于位置或时区的过滤器。以下是如何设置和更新个人资料的位置和时区信息的示例概述：

1. ****个人资料访问您的网站或提交表单。**** 该请求包括他们的 IP 地址，但没有地址数据，因此 Klaviyo 根据 IP 估计他们的位置和时区。 2. ****个人资料通过 Shopify 下订单。**** Klaviyo 的 Shopify 集成从订单中提取帐单地址并更新个人资料的位置和时区。因为这个
   地址数据比基于 IP 的估计更权威，因此具有优先权。 3. ****个人资料继续浏览您的网站。**** 尽管这些交互包括 IP 地址，但个人资料的位置现在受到保护 — 基于 IP 的估计不会覆盖地址
   数据由 Shopify 设置。 4. ****客户更新从 Shopify 同步。**** 如果客户在 Shopify 中的默认地址与其上次订单的帐单地址不同，则配置文件的位置将更新以反映客户记录。两个来源具有相同的权限，因此最近同步的数据显示在配置文件上。请注意，电子邮件打开和单击不会更新个人资料的位置或时区，即使该个人资料没有其他位置数据也是如此。 ![配置文件中显示位置和时区的示例](https://klaviyo.zendesk.com/hc/article_attachments/33101716559387)

如果您使用自定义集成，则帐单地址不会用于确定位置。您需要使用配置文件 API 中的位置对象来设置配置文件的位置。了解有关[自定义集成](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration)和Klaviyo的[Profiles API](https://developers.klaviyo.com/en/reference/create_profile)的更多信息。收集电话号码时，号码的区号不会影响配置文件中保存的位置。但是，区号可用于确定收件人的[安静时间](https://help.klaviyo.com/hc/en-us/articles/22711363273627)。 ## IP 地理位置

当未收到帐单地址时，Klaviyo 使用 IP 地理定位来设置配置文件的位置。 Klaviyo 可以通过 IP 识别一个人，并在该个人资料满足以下条件时设置位置：

- 单击消息
- 通过 Klaviyo 注册表单订阅
- 被 Klaviyo 的网络跟踪片段捕获

  尽管 IP 地理定位被用作行业标准，但它有时可能不准确。以下是您可能会发现配置文件的 IP 地理位置与其实际位置之间存在差异的几个原因：
- 每当某人打开电子邮件或通过网络跟踪捕获时，Klaviyo 就会检查他们的 IP。例如，如果有人在去中国旅行时打开电子邮件，他们的 IP 就会反映出来，即使他们的典型位置是在加利福尼亚州。 - IP不是静态的，IP所属的位置也不是静态的；这使得 IP 地理定位不完善。如果用户的互联网服务提供商为其连接分配了 IPv6 地址，则可能无法正确捕获其位置。当您想要安排发送给每个收件人所在时区的活动时，这是最相关的。根据收件人上次打开电子邮件或通过注册表单选择加入的位置，Klaviyo 在发送时为收件人记录的时区可能与收件人收到您的下一个营销活动时所在的时区不同。 Klaviyo 无法从电子邮件打开事件获取准确 IP 数据的其他情况：
- 如果**打开电子邮件**事件在跟踪时通过代理；在 Gmail 中打开的电子邮件也是如此。 - 如果 **打开电子邮件** 事件通过集成（如 Mailchimp）同步到 Klaviyo。在这种情况下，我们评估的 IP 将是 Mailchimp 服务器 IP，而不是实际电子邮件收件人的 IP。 ## 自己更新位置信息

如果您想要更新一个或多个配置文件的任何位置相关属性（通过[手动导入](https://help.klaviyo.com/hc/en-us/articles/115005074627#add-a-custom-property-yourself2)此位置数据或[使用 API](https://developers.klaviyo.com/en/reference/update_profile)），您需要引用相关的 Klaviyo物业名称：

- ****城市：**** 他们居住的城市
- ****州/地区：**** 他们居住的州/地区
- ****国家：**** 他们居住的国家
- ****邮政编码：**** 他们居住的邮政编码

有关属性以及如何管理和更新属性的更多信息，请参阅我们的[属性指南](https://klaviyo.zendesk.com/hc/en-us/articles/115005074627)。