---
id: "360048730411"
title: "Magento 集成系统要求参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360048730411-Magento-integration-system-requirements-reference"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:49Z"
language: "zh"
---
## 你将会学到

了解与 Magento 1 或 2 实现最佳同步的系统要求。Magento 商店的管理员负责系统规格和配置。确保您的系统配置为与 Klaviyo 配合使用将实现流畅的集成体验。 ## 配置API用户权限

在将 Magento 商店与 Klaviyo 集成的过程中，您将创建一个新的 [SOAP](https://help.klaviyo.com/hc/en-us/articles/115005082187#set-up-magento-api-credentials1)（对于 Magento 1）或[REST](https://help.klaviyo.com/hc/en-us/articles/115005254348-Integrate-with-Magento-2-x-CE-and-EE-%23setup-your-magento-api-credentials2)（对于 Magento 2）具有完全资源访问权限的角色，并将新用户分配给该角色。确保**资源访问**设置为**全部**。如果没有此 API 用户的必要权限，Klaviyo 将无法与您的 Magento 商店的 API 正确交互，这将阻止集成从您的商店检索数据。 ## 启用对所需 API 端点的访问

Klaviyo 从特定端点请求数据。您的系统配置必须允许访问这些端点；考虑安全控制或 URL 重定向逻辑对这些端点对 Klaviyo 的可访问性的影响。如果 Klaviyo 无法访问预期的 API 端点，部分或全部 Magento 数据将无法同步，您将在应用程序中看到错误报告。所有出站 Klaviyo 集成流量都位于一组可预测的静态 IP 地址后面，因此您可以高度确信该流量来自 Klaviyo；我们建议[将这些地址列入白名单](https://help.klaviyo.com/hc/en-us/articles/19143781289115)。 ## 历史数据同步API请求的系统容量

当您激活集成时，Klaviyo 会自动将 API 请求排队以同步历史数据，包括客户记录、订单记录和产品目录。我们试图快速做到这一点，以使营销人员能够尽快在他们的帐户中使用这些数据。我们还尝试通过限制并发性和优雅地处理重试来负责任地做到这一点。如果您的商店具有大量历史数据、有限的资源容量或其他发出大量 API 请求的应用程序，我们建议咨询您的 Magento 管理员，以确保您的基础设施能够支持历史数据同步。您的管理员可能需要考虑暂时增加资源或应用自动扩展。如果您担心历史数据量或服务器处理临时增加的 API 请求以获取此数据的能力，请考虑临时扩展服务器资源，应用自动扩展。 ## 验证SSL证书有效性

SSL 证书以数字方式验证网站的身份，并在 Web 浏览器和 Web 服务器之间实现加密连接。您网站的 SSL 证书由网站的原始服务器托管。有效的 SSL 证书对于安全接受付款、保护密码登录和保护 Web 表单至关重要。 [此工具](https://www.ssllabs.com/ssltest/analyze.html?viaform=on&d=)可用于验证网站的SSL证书。如果您网站的 SSL 认证过期，Magento 集成可能会被禁用。在这种情况下，必须在托管提供商上更新域和中间认证。如果您不确定您的认证的位置，请联系您的托管提供商寻求帮助

## 足够的服务器内存分配

电子商务网站所需的磁盘空间量取决于多种因素，包括产品数量、每个产品的图像数量、图像质量、服务器上存储的电子邮件数量以及静态内容页面。我们建议为您的 Klaviyo 集成分配超过 1 GB 的内存，但最低要求为 512 MB。如果您的服务器无法分配足够的资源来响应 Klaviyo 的请求，则会发生集成错误。 Klaviyo-Magento 集成从同步历史数据开始，因此建议您在激活集成之前验证 Magento 和服务器中的内存设置。默认 Magento PHP 内存设置为 128 MB。通过将“memory\_limit”变量的值更改为建议的 1024 兆字节，可以在 php.ini 文件中更新此设置。 ## 将时区设置为 UTC

自 20 世纪 60 年代以来，协调世界时 (UTC) 一直是世界主要时间标准。 Klaviyo 依靠 UTC 来安排最新数据的同步。如果您的 Magento 实例使用不同的时区，Klaviyo 会更难以确定哪些数据是最新的并且应该同步。您的 Magento 后端和 app/Mage.php 以及 app/code/local/Mage/Core/Model/Locale.php 文件中的时区应该[更新为 UTC](https://www.simicart.com/blog/set-configure-timezone-magento/)。 ## 其他资源

- [如何与 Magento 1.x（CE 和 EE）集成](https://klaviyo.zendesk.com/hc/en-us/articles/115005082187)
- [如何与 Magento 2.x（CE 和 EE）集成](https://klaviyo.zendesk.com/hc/en-us/articles/115005254348)