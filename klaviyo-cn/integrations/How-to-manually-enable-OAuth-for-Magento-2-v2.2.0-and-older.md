---
id: "4403350880411"
title: "如何为 Magento 2 v2.2.0 及更早版本手动启用 OAuth"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4403350880411-How-to-manually-enable-OAuth-for-Magento-2-v2-2-0-and-older"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:57Z"
language: "zh"
---
## 概述

Magento 2 版本 2.2.0 需要旧版本的 Klaviyo 扩展，该扩展不允许在扩展设置中进行 OAuth 设置。对于当前使用 v2.2.0 的客户（不支持 2.2.0 之前的版本），我们建议您手动将 OAuth 添加到集成中。我们还建议更新到 Magento 2 的最新版本，以利用所有新的和即将推出的 Klaviyo 集成功能。本指南介绍了在安装扩展并配置 Webhooks 后如何设置 OAuth。如果您需要安装 Magento 2 的 Klaviyo 扩展，请查看[我们的安装说明](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348)。

## 设置 OAuth

首先，确保您已登录 Magento 2 帐户。在这里，我们将启用 OAuth 将您的 Klaviyo 帐户安全地连接到您刚刚安装的 Magento 2 扩展。

从左侧导航窗格导航至****系统****，然后选择****集成****。单击右上角的****添加新集成****，手动设置与 OAuth 身份验证的集成。在 **名称** 字段中为新集成命名，并在 **您的密码** 字段中输入您的安全密码。

![manualoauth.png](https://klaviyo.zendesk.com/hc/article_attachments/28723544125339)

使用以下 URL 填写 **Callback URL** 字段，并将 <**Company ID>** 更新为您的 Klaviyo 公共 API 密钥。请务必删除 URL 中可能自动添加的任何多余空格。

````
https://www.klaviyo.com/integration-oauth-one/magento-two/auth/confirm?c=<公司 ID>
````

然后，使用以下 URL 更新 **Identity Link URL**：

````
https://www.klaviyo.com/integration-oauth-one/magento-two/auth/handle
````

选择左侧的****API**** 选项卡并导航到****资源访问**** 下拉菜单。我们建议您选择 ****All**** 以授予 Klaviyo 所需的所有 API 访问规则。

如果您希望仅允许特定选择，请确保选中以下各项。

- “目录>库存>类别”
- “购物车 > 管理购物车”
- “客户 > 客户群体”
- “客户 > 所有客户”
- “销售 > 运营 > 订单 > 操作 > 查看”
- “商店 > 属性 > 产品”
- “目录>库存>产品”
- “销售 > 运营 > 发货”
- “商店 > 设置 > 所有商店”
- “营销 > 通讯 > 时事通讯订阅者”

完成选择后，单击****保存。****

然后找到您在上面使用的名称的集成，然后单击****激活****。

![activateoauth.png](https://klaviyo.zendesk.com/hc/article_attachments/28723522207899)

激活集成将打开一个窗口，请求您批准访问。单击****允许****重定向到 Klaviyo 以完成集成设置。

![oauthperms.png](https://klaviyo.zendesk.com/hc/article_attachments/28723522209691)

如果您尚未登录，请登录，或者确认您的帐户名和 ID 正确，然后单击 ****集成 Magento 2。**** 这会将 Magento 2 集成添加到与您用于设置的 API 密钥关联的 Klaviyo 帐户。如果您登录了多个 Klaviyo 帐户并且未显示正确的帐户，请注销任何其他会话。

![m2authorize.png](https://klaviyo.zendesk.com/hc/article_attachments/28723544135451)

如果窗口自动关闭，则连接成功。

如果您收到以下错误，请确保第一步中使用的 API 密钥与您当前登录的帐户相对应。

![apierror.png](https://klaviyo.zendesk.com/hc/article_attachments/287235222214811)

在 Magento 和 Klaviyo 之间建立连接时，如果您收到错误列表，则可以单击每个错误以了解有关原因的更多信息。

![oauthgenerror.png](https://klaviyo.zendesk.com/hc/article_attachments/28723522217627)

## 后续步骤

现在您已启用 OAuth，请继续[在 Klaviyo 中启用 Magento 2 集成](https://help.klaviyo.com/hc/en-us/articles/115005254348#enable-the-magento-2-integration-in-klaviyo8)。