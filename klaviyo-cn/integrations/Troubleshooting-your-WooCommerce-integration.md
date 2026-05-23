---
id: "4515829067803"
title: "对 WooCommerce 集成进行故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4515829067803-Troubleshooting-your-WooCommerce-integration"
section: "WooCommerce troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:58Z"
language: "zh"
---
## 你将会学到

了解如何按照下述相关故障排除方案解决 WooCommerce 集成设置的问题。如果您遇到的问题不在此列表中，请通过[社区](https://community.klaviyo.com/got-a-question-1)或我们的[支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)联系。 ## 开始之前

如果您还没有阅读我们的[WooCommerce 入门](https://help.klaviyo.com/hc/en-us/articles/115005255808) 指南，了解有关集成的分步说明。如果您想升级插件，请查看我们关于[如何升级 WooCommerce 插件](https://help.klaviyo.com/hc/en-us/articles/4418005597723) 的文章。 ## 故障排除场景

根据应用内收到的错误消息，参考以下方案来解决您的问题。请注意，如果您选择删除集成然后重新集成，您的 WooCommerce 数据将不会从 Klaviyo 中删除。 ###“为了避免功能中断，您可能需要禁用以下插件：**插件名称**”

如果您在 WordPress 中有活动的缓存插件或重定向插件，这些插件可能会干扰 Klaviyo 的集成并导致连接问题。我们建议在集成设置过程中禁用这些插件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28716055944091)

###“我们无法完成您的设置”

![](https://klaviyo.zendesk.com/hc/article_attachments/28716066411035)

此消息意味着您的防火墙阻止了 Klaviyo 的请求，或者您在 Cloudflare 中启用了 Bot Fight 模式，或者两者兼而有之。要解决此问题，我们建议将 Klaviyo 集成流量列入白名单并禁用 Bot Fight 模式（如果您已启用）。 1. 了解如何[将 Klaviyo 集成流量 IP 地址列入白名单](https://help.klaviyo.com/hc/en-us/articles/19143781289115)。 2. 要在 Cloudflare 中禁用 Bot Fight 模式：
   1.登录[Cloudflare仪表板](https://dash.cloudflare.com/login)。 2. 选择您的帐户和域。 3. 转到****安全 > 机器人****。 4. 对于机器人战斗模式，选择 **关闭**。 ### “确保您的 WooCommerce 商店启用了 https 和 SSL”

![](https://klaviyo.zendesk.com/hc/article_attachments/28716055952027)

Klaviyo 希望您的商店 URL 遵守 HTTPS 协议，这意味着该网站具有有效的 SSL 证书。如果您的网站使用 HTTP 而不是 HTTPS，您可能会遇到问题。您可以在[SSL服务器测试（由Qualys SSL Labs提供支持）](https://www.ssllabs.com/ssltest/analyze.html)检查您的SSL证书是否有效。 Klaviyo 要求测试以 A 级通过。 ### “无法使用提供的凭据访问 API”

如果您进行了自定义以阻止非登录用户访问 API，则可能会收到此错误。通常，这是 **functions.php** WordPress 文件中的一个函数，它会触发 401 状态代码响应。如果您有这样的自定义，请将其删除或注释掉以消除错误。有关此错误的更多信息，请查看 [WooCommerce REST API 常见问题解答](https://developer.wordpress.org/rest-api/frequently-asked-questions/#require-authentication-for-all-requests)。 ###“无法访问订单 API，请检查连接设置并重试”

此错误意味着当 Klaviyo 尝试验证 WooCommerce 集成并获取订单计数时，他们的 API 不会返回 Klaviyo 期望的值，或者根本不返回任何内容。由于集成尚未正式连接到 Klaviyo，这意味着它需要在 WooCommerce 内解决。要获取有关此错误的更多信息，您需要对订单计数端点进行 API 调用，这将更深入地了解传递给 Klaviyo 的内容。下面是一个 cURL 请求示例。要使用它，请填写您的商店 URL、消费者密钥和消费者秘密：

````
卷曲 https://STORE_URL/wp-json/wc/v3/orders \
-u CONSUMER_KEY:CONSUMER_SECRET
````

### “您的 Klaviyo 插件已过时”

![](https://klaviyo.zendesk.com/hc/article_attachments/33638394936859)

有时，Webhook 到达 Klaviyo 时会出现延迟，导致您暂时看到旧的设置页面。几分钟后此问题应该会自行解决。 ### 从 WordPress 连接到 Klaviyo 时出现 404

要解决此问题，您应该确认您已为 WordPress 网站启用了永久链接。除非启用永久链接，否则 WooCommerce 身份验证将无法工作。 1. 导航到您的 WordPress 网站并转到 ****设置**** > ****永久链接****。 2. 在 **通用设置** 下，选择除 **普通** 之外的任何链接结构。 3. 单击****保存更改****进行确认。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28716055953819)
4. 完成后，重新与 Klaviyo 集成。 ### 安装失败 - 我们无法安装您的扩展

尝试通过 [WooCommerce 安装集成] 时，您可能会遇到“安装失败”错误市场](https://woocommerce.com/products/klaviyo-for-woocommerce/?utm_source=extensionsscreen&utm_medium=product&utm_campaign=wcaddons&in_app_label=promoted&wccom-site=https%3A%2F%2Fvoluntory-plat ypus.jurassic.ninja&wccom-back=%252Fwp-admin%252Fadmin.php%253Fpage%253Dwc-admin%2526path%253D%25252F扩展&wccom-woo-version=10.3.5&wccom-connect-nonce=48111ee6ce&utm_group=发现我们的最爱）。 ![图片 (1).png](https://klaviyo.zendesk.com/hc/article_attachments/43279509814939)

如果您无法从 WooCommerce Marketplace 成功安装，您还可以从 Wordpress 插件管理员安装该插件。 1. 导航到您的 WordPress 管理员并转到****插件****。 2. 选择****添加插件****。 3. 在****搜索插件****中搜索**Klaviyo**。 4. 选择****立即安装****。 5. 选择****激活。****
6. 从左侧导航中选择****营销****，然后单击****Klaviyo****。 7. 单击 ****连接帐户**** 开始，然后继续在 [入门] 中的 [启用 WooCommerce 集成](https://help.klaviyo.com/hc/en-us/articles/115005255808#h_01FV97DEKASQ117J7HBFCVHBKA) WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808) 文章。