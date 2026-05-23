---
id: "26909356614299"
title: "元广告同步、凭据和授权错误故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/26909356614299-Troubleshooting-Meta-Ads-sync-credential-and-authorization-errors"
section: "Meta Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-16T22:46:51Z"
language: "zh"
---
## 你将会学到

了解如何解决元广告集成的同步、凭据和授权错误。

您是否收到过以下错误消息或电子邮件之一？

- **您的元广告集成不再按预期同步。 Klaviyo 不再被授权连接到元广告。
  ![](https://klaviyo.zendesk.com/hc/article_attachments/28981090659867)**
- **您的凭据已过期。检查您的 Meta Ad Manager 权限并重新进行身份验证以恢复同步。
  ![](https://klaviyo.zendesk.com/hc/article_attachments/28981077652763)**
- **Klaviyo 不再被授权连接到元广告。请检查元广告并更新您的设置以重新启用同步。
  ![](https://klaviyo.zendesk.com/hc/article_attachments/35587393816859)**

要解决这些错误，我们建议更新您的权限，接受 Meta 的服务条款，然后按照以下步骤重新验证您的 Meta Ads 集成。这些错误的发生可能有多种根本原因。即使您不确定根本原因，以下步骤也可以解决各种问题。

## 故障排除步骤

### 检查您的元帐户和设置

首先，确认您对元业务帐户、Facebook 页面和广告帐户拥有完全控制权。

1. 访问您的[元业务设置](https://business.facebook.com/latest/settings/)。
2. 在链接中，单击“**人员”下的您的用户名。**
3. 如果您使用线索广告：请确保您想要连接到 Klaviyo 的 Facebook 页面具有**完全控制**权限。如果没有，请单击****管理****并调整权限。一旦您完全控制，您就可以继续。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28715966407579)
4. 如果您使用自定义受众：请确保您要连接到 Klaviyo 的广告帐户具有**完全控制**权限。如果没有，请单击****管理****并调整权限。一旦您完全控制，您就可以继续。

### 接受 Meta 的服务条款

要接受 Meta 的服务条款：

1. 将以下 URL 复制并粘贴到浏览器中，但不要按 Enter 键：

   ````
    https://business.facebook.com/ads/manage/customaudiences/tos/?act=AdAccountID
   ````

   ![](https://klaviyo.zendesk.com/hc/article_attachments/35584051538715)
2. 您需要更新上面的链接，将 **AdAccountID** 更改为 Meta 中您的特定广告帐户 ID。要查找此 ID：

1. 打开一个新选项卡并导航至[Meta 业务设置中的广告帐户](https://business.facebook.com/settings/ad-accounts)。
2. 在左侧选择您的广告帐户。
3. 在右侧帐户名称下找到帐户 ID。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35584051541659)
4. 复制 ID。

3. 在原始选项卡中，将 **AdAccountID** 替换为您从 Meta 复制的 ID，然后按 Enter 键。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35584051545755)
4. 查看并接受服务条款。

### 重新验证 Klaviyo 和元广告

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 在列表中找到**元广告**并选择它。
3. 在您的设置页面上，单击右上角的****管理集成>重新验证****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35584028377371)

您的集成现在应该开始正常同步。

如果您仍然遇到问题，请尝试联系[社区](https://community.klaviyo.com/got-a-question-1)或我们的[支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。

## 其他资源

[元广告入门](https://help.klaviyo.com/hc/en-us/articles/115005082127)