---
id: "19143781289115"
title: "如何将 Klaviyo 集成流量 IP 地址列入白名单"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19143781289115-How-to-allowlist-Klaviyo-integration-traffic-IP-addresses"
section: "All integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: "zh"
---
## 你将会学到

了解如何将出站 Klaviyo 集成流量的 IP 地址列入白名单，以确保您的防火墙不会阻止 Klaviyo 的请求。所有出站 Klaviyo 集成流量都位于一组可预测的静态 IP 地址后面，因此您可以高度确信该流量来自 Klaviyo。这尤其适用于使用 Magento 2 和 WooCommerce 等自托管电子商务集成的客户。

请注意，集成流量不包括流触发的 Webhook 流量，该流量使用不同的 IP 地址。

## Klaviyo 使用哪些 IP 地址进行集成流量？

Klaviyo 用于集成流量的 IP 地址范围是 207.211.192.0 - 207.211.207.255。这是您应该列入允许名单的范围。该范围可以表示为 CIDR 地址“207.211.192.0/20”。

如果您被限制列入白名单 /20 个范围，我们的范围可以表示为 16 /24 个范围。因此，您需要将以下内容列入许可名单：

`207.211.192.0/24`

`207.211.193.0/24`

`207.211.194.0/24`

`207.211.195.0/24`

`207.211.196.0/24`

`207.211.197.0/24`

`207.211.198.0/24`

`207.211.199.0/24`

`207.211.200.0/24`

`207.211.201.0/24`

`207.211.202.0/24`

`207.211.203.0/24`

`207.211.204.0/24`

`207.211.205.0/24`

`207.211.206.0/24`

`207.211.207.0/24`

## 操作方法示例

### 如何在 Cloudflare 中列入白名单

Cloudflare 不接受将 /20 范围列入白名单，因此您需要将上面给出的所有 16 个 /24 范围列入白名单。

1. 登录您的 [Cloudflare 仪表板](https://dash.cloudflare.com/) 并选择您的帐户和域名。
2. 转到****安全 > WAF > 工具****。
3. 在 **IP 访问规则**下，输入以下详细信息：
   1. 对于**值**，输入第一个范围：`207.211.192.0/24`。
   2. 选择****允许****操作。
   3. 对于**区域**，选择规则是仅应用于当前网站还是帐户中的所有网站。
   4. 输入规则的注释（可选）。
4. 选择****添加****。
5. 对上一节中给出的每个 16 /24 范围重复此过程。

您可以在 [Cloudflare 文档](https://developers.cloudflare.com/waf/tools/ip-access-rules/) 中了解有关 IP 访问规则的更多信息。

### 如何在 Akamai 中列入许可名单

1. 在 [控制台](https://console.janrain.com/#/login) 的编辑页面中，单击****添加新 IP 地址****。
2. 在**将 IP 网络列入白名单**字段中，输入“207.211.192.0/20”。
3. 完成后，单击 **保存更改** 图标。

您可以在 [Akamai 文档](https://techdocs.akamai.com/identity-cloud/docs/manage-property-ip-allow-lists) 中了解有关管理 IP 允许列表的更多信息。

## 结果

您已成功将 Klaviyo 的静态 IP 地址列入出站集成流量的允许名单。您的防火墙或安全提供商现在将安全地允许该流量通过，因为知道该流量源自 Klaviyo。