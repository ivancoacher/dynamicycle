---
id: "5510750923035"
title: "Magento 2 集成故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/5510750923035-Troubleshooting-your-Magento-2-integration"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: "zh"
---
## 你将会学到

了解如何按照下述故障排除步骤解决 Magento 2 OAuth 设置问题。如果您在完成这些步骤后仍然遇到问题，请联系我们的[社区](https://community.klaviyo.com/got-a-question-1)或[我们的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。 ## 开始之前

如果您还没有阅读我们的 [Magento 2 入门](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-) 指南，了解设置 Magento 2 集成的分步说明。 Klaviyo 使用 OAuth 协议生成访问令牌并从 Magento 2 商店检索数据。如果您自定义了 Magento 2 安装，可能会导致 Klaviyo 的 OAuth 过程失败。本文将指导您完成一系列故障排除步骤，以确定故障发生的位置。 ## 一般故障排除步骤

### 确保您的网站可以通过有效的 SSL 证书公开访问

Klaviyo 的 OAuth 过程要求您的网站可公开访问，否则生成访问令牌所需的 API 调用将失败。 1. 确保您的商店访问权限不受密码保护或 IP 限制。 2. 确保可以使用有效的 SSL 证书通过 HTTPS 访问您的商店。您可以在[此处](https://www.ssllabs.com/ssltest/analyze.html)测试您的证书。 ### 确保您的防火墙没有阻止 Klaviyo 的请求

所有出站 Klaviyo 集成流量都位于一组可预测的静态 IP 地址后面，因此您可以高度确信该流量来自 Klaviyo。阅读我们的文章以了解[如何将 Klaviyo 集成流量 IP 地址列入白名单](https://help.klaviyo.com/hc/en-us/articles/19143781289115)。 ### 检查您的 Magento 2 和 Klaviyo 扩展版本

1. 如果您使用的是 Magento v2.2.0，则需要[手动启用 OAuth](https://help.klaviyo.com/hc/en-us/articles/4403350880411)。 2. 确保您已安装正确的 Klaviyo 扩展（您可能需要[升级](https://help.klaviyo.com/hc/en-us/articles/115005254348#h_01HNZMK310HQPFJWZ2NB1C6NSC)）。 ### 确保 OAuth 端点可访问

您可能有额外或缺失的重写规则，这可能导致默认的 Magento 2 OAuth 端点无法访问。 Klaviyo 需要访问这些端点来生成授权过程所需的凭据。确保您的商店可以访问以下 URL：

````
https://[存储 URL]/oauth/token/request
````

````
https://[存储 URL]/oauth/token/access
````

1. 您可以通过发出如下 POST 请求来验证它们是否可以访问：

   ````
   curl --location --url 'https://[存储 URL]/oauth/token/request' --request 'POST' -v
   ````

   ````
   curl --location --url 'https://[存储 URL]/oauth/token/access' --request 'POST' -v
   ````
2. 您应该会收到类似于以下内容的响应。以这种方式发出请求时看到错误是正常的，它验证端点是否正确响应。 ![curloauthendpoint.png](https://klaviyo.zendesk.com/hc/article_attachments/28713384135323)
3. 如果您没有收到与 OAuth 相关的响应，则应检查是否存在阻止访问这些 URL 的重定向、无效重写规则或内部服务器错误。这可能是由 URL 中的商店子路径引起的。通过访问以下端点来测试存储子路径问题：

````
https://[存储 URL]/[存储路径]/oauth/token/request
````

````
https://[存储 URL]/[存储路径]/oauth/token/access
````

如果这些端点可以解决，请在 .htaccess 文件中包含以下重写规则来解决问题。 ````
重写引擎开启
RewriteRule /oauth/token/request$ https://%{HTTP_HOST}/[存储路径]/oauth/token/request [L,R=301]
RewriteRule /oauth/token/access$ https://%{HTTP_HOST}/[存储路径]/oauth/token/access [L,R=301]
````

### 删除集成并重新创建它

如果您在上次集成尝试失败后进行了更改，最好删除原始的 OAuth 集成。使用的密钥可能无效，需要重新生成。 1. 在 Magento 中，导航至****系统****
2. 选择****集成****
3. 找到 Klaviyo 集成记录并将其删除

删除集成记录后，请按照我们的[如何与 Magento 2 集成](https://help.klaviyo.com/hc/en-us/articles/115005254348-How-to-Integrate-with-Magento-2-x-CE-and-EE-#setup-oauth7) 指南中的步骤创建新的集成记录并重试。 ## Magento 版本特定的问题

### Magento 2.4.2 特有的故障

如果您使用 Magento 2.4.2，则存在一个 OAuth 激活失败的已知问题。激活集成后，您可能会看到如下所示的错误消息。即使您没有收到错误，OAuth 激活也可能失败。通常，可以在 Magento 日志中找到错误。 ![m2oauthfailed.png](https://klaviyo.zendesk.com/hc/article_attachments/28713384127643)

为了解决此错误，您需要：

- 升级到 Magento 2.4.3。查看 Magento 2 的文档以[升级您的版本](https://devdocs.magento.com/cloud/project/project-upgrade.html)。 - 按照 [Klaviyo 的 github 存储库](https://github.com/klaviyo/magento2-klaviyo/issues/122) 的描述为 Magento 2 应用补丁。 ### Magento 2.4.6 特有的身份验证失败

您是否使用 Magento 2.4.6 并在与 Klaviyo 集成后遇到 401 身份验证错误？这可能是由于影响 Magento 2.4.6 版本的已知 Magento 错误造成的。要解决此问题，您需要启用不记名令牌身份验证，以便 Klaviyo 可以使用它（而不是 OAuth 1.0）发出请求。要启用不记名令牌身份验证：

1. 在您的 Magento 管理员中，导航至 ****Stores > Configuration > Services > OAuth > Consumer Settings****。 2. 对于设置 **允许 OAuth 访问令牌用作独立承载令牌**，选择 **是**。 3. 单击****保存配置****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28713384150683)

进行此更新后，您之前的身份验证错误应该得到解决，并且集成同步将恢复。