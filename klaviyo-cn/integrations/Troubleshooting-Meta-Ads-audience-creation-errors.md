---
id: "33304725419931"
title: "排除元广告受众群体创建错误"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/33304725419931-Troubleshooting-Meta-Ads-audience-creation-errors"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-16T22:55:27Z"
language: "zh"
---
## 你将会学到

了解如何解决 Klaviyo 中的元广告自定义受众群体创建错误。

当您尝试在 Klaviyo 的元广告集成中创建新的自定义受众群体时，您是否收到以下错误之一？

- **无法创建受众。检查您的 Facebook 广告权限并重新进行身份验证。
  ![](https://klaviyo.zendesk.com/hc/article_attachments/33304909206043)**
- **要创建元广告自定义受众，请在此处同意自定义受众条款。****！[](https://klaviyo.zendesk.com/hc/article_attachments/35583895080091)**

这些错误可能表明您尚未接受 Meta 的广告帐户服务条款。继续阅读以了解如何接受这些权限，以及解决此错误可以采取的其他步骤。

## 开始之前

您必须是元广告帐户的管理员才能完成以下步骤。

## 故障排除步骤

要接受 Meta 的服务条款：

1. 将以下 URL 复制并粘贴到浏览器中，但不要按 Enter 键：

   ````
    https://business.facebook.com/ads/manage/customaudiences/tos/?act=AdAccountID
   ````

   ![](https://klaviyo.zendesk.com/hc/article_attachments/33304903139355)
2. 您需要更新上面的链接，将 **AdAccountID** 更改为 Meta 中您的特定广告帐户 ID。要查找此 ID：

1. 打开一个新选项卡并导航至[Meta 业务设置中的广告帐户](https://business.facebook.com/settings/ad-accounts)。
2. 在左侧选择您的广告帐户。
3. 在右侧帐户名称下找到帐户 ID。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33304903145499)
4. 复制 ID。

3. 在原始选项卡中，将 **AdAccountID** 替换为您从 Meta 复制的 ID，然后按 Enter 键。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33304909224987)
4. 查看并接受服务条款。

如果您首次将 Klaviyo 与元广告集成时收到原始错误，则应重新开始[集成设置过程](https://help.klaviyo.com/hc/en-us/articles/115005082127#h_01HDRXKYW8JVHVNCPZ7KGEK82A)。

如果您在编辑现有集成时收到原始错误，您应该检查 Klaviyo 中的错误是否已解决：

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 从列表中选择****元广告****，进入集成设置页面。
3. 尝试创建新的自定义受众。如果它有效 - 你就准备好了！如果您仍然收到错误，我们建议您重新验证集成：

1. 在同一页面上，单击****管理集成****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33304909230491)
2. 选择****重新验证****。

您现在应该能够在元广告集成中创建自定义受众群体。

如果您仍然遇到此错误，请尝试按照我们的[授权错误故障排除步骤](https://help.klaviyo.com/hc/en-us/articles/26909356614299)操作。您还可以联系[社区](https://community.klaviyo.com/got-a-question-1)或我们的[支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。

## 其他资源

[元广告入门](https://help.klaviyo.com/hc/en-us/articles/115005082127)