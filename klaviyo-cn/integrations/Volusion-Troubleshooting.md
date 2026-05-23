---
id: "115005083487"
title: "体积故障排除"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005083487-Volusion-Troubleshooting"
section: "Volusion"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:21Z"
language: "zh"
---
## Volusion 下订单数据未在 Klaviyo 中报告

这可能是您允许导出数据的 Volusion API 设置的问题。要解决此问题，请导航至 Volusion 管理面板的 **库存** 选项卡。从下拉菜单中选择**导入/导出**。

![647863](https://klaviyo.zendesk.com/hc/article_attachments/28716301437851)

单击 **Volusion API** 访问 API 主页面。在 **通用** 部分中，您将找到用于运行商店通用/订单导出的选项。导出运行后，页面将刷新。

![647864](https://klaviyo.zendesk.com/hc/article_attachments/28716301441691)
![647865](https://klaviyo.zendesk.com/hc/article_attachments/28716328819611)

单击“运行”导出通用订单后，页面顶部会生成一个 API URL。例如，URL 将显示为： https://storename.com/net/WebService.aspx?Login=user@storename.com&EncryptedPassword=****ABC123...****&EDI\_Name=GenericOrders

“EncryptedPassword=”和“&EDI\_Name=GenericOrders”之间显示的值（上面粗体显示）将用作您的 API 密钥。使用它可以从 Klaviyo 仪表板的“集成”选项卡重新建立集成设置。

完成后，单击 Klaviyo 帐户的 **Metrics** 选项卡进行测试。查看 Volusion 已下订单指标的近期活动，看看是否有任何新数据已在 Klaviyo 中同步。

如果您看到“已下订单”指标的新数据，请[联系我们的成功团队](https://help.klaviyo.com/hc/en-us/requests/new)，以对 Klaviyo 中缺失的订单进行缺口填补或寻求任何进一步帮助。

有关使用 Volusion API 导出数据的更多信息，请参阅 [Volusion 支持](https://support.volusion.com/hc/en-us/articles/208837888-Exports-Orders-Export-Developer-)。

## 人们在点击我的电子邮件链接时看到“无效输入”错误

Klaviyo 中的“电子邮件到网络跟踪”功能使用点击跟踪将活动与通过 Klaviyo 电子邮件到达您网站的用户联系起来，然后我们最初能够识别他/她的身份（例如当他们进行购买或订阅您的时事通讯时）。

|  |
| --- |
| Volusion 不支持我们的点击跟踪使用的 URL 格式，并且当用户尝试通过这些链接之一访问您的商店时会产生错误，因此必须在 Klaviyo 中禁用此功能，以确保电子邮件中的链接正确到达您的 Volusion 商店。 |

如果您不禁用此跟踪，您的客户在点击电子邮件中指向您网站的任何链接时可能会看到以下错误：

![647866](https://klaviyo.zendesk.com/hc/article_attachments/28716301452059)

您可以在您的帐户设置 (<https://www.klaviyo.com/account>) 下的**电子邮件设置******>******电子邮件到网站跟踪**下禁用此跟踪。

![647867](https://klaviyo.zendesk.com/hc/article_attachments/28716301454491)

禁用此功能后唯一丢失的功能是通过他们点击的电子邮件跟踪您网站上的新个人资料的能力。然而，只要您的网站上有 Klaviyo 网络跟踪分析，只要我们通过在您的商店中购买或注册新闻通讯获得用户的电子邮件地址，我们仍然能够跟踪用户。