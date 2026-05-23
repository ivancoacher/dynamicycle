---
id: "1260806102230"
title: "如何在短信中添加动态图片"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/1260806102230-How-to-add-a-dynamic-image-to-a-text-message"
section: "Getting started with SMS flows"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:26Z"
language: "zh"
---
## 你将会学到

了解如何在 Klaviyo 中将动态图像添加到彩信中。

包含动态图像可以让您个性化您的短信。例如，您可以向某人展示他们查看、开始结帐或购买的确切产品。

## 开始之前

根据您的使用情况，您可能并不总是能够添加动态图像。

- 只有指标触发的流程才能使用基于事件数据（例如结帐或下订单中的商品）或事件的目录标签的动态图像。
- 仅当图像 URL 作为收件人个人资料中的自定义属性存在时，营销活动以及列表和分段触发的流才能具有动态图像。

另外，关于动态图像，请务必注意以下几点：

- 每条彩信仅允许 1 个动态图像。
- 图片应小于 600 KB；否则运营商会对其进行压缩，这可能会使图像看起来失真。
- 如果您尝试使用不允许彩信的发送号码发送动态图像，则消息将发送，但图像将被删除。
- 您可以对动态图像使用条件语句。
- 移动运营商不支持WebP文件，附加此类图像可能会导致消息失败。

## 如何添加动态图片

1. 选择要包含动态图像的流消息。
2. 在右侧边栏中，单击 ****编辑****。！[流程中新短信的边栏](https://klaviyo.zendesk.com/hc/article_attachments/28720670835355)
3. 单击右上角的****预览和文本****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627732347035)
4. 找到要包含的图像的数据源。
5. 单击图像第一个变量的数据源，该变量通常以 0 结尾。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627695663259)
6. 单击 ****完成****。
7. 单击左侧“消息”框中的“添加图像”图标（图像图标）。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627695670299)
8. 转到****动态图像****选项卡。
9. 粘贴图像的动态变量或动态 URL。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627695672731)
10. 单击 ****保存****。
11. 通过确保动态图像出现在预览屏幕中来检查动态图像是否已正确添加。

****使用目录标签****

您还可以使用[目录标签](https://help.klaviyo.com/hc/en-us/articles/360004785571)在彩信中添加动态图像。为此：

1. 在短信预览模式中，找到第一个列出的产品的产品 ID 或 SKU。
2. 复制该变量。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627732367771)
3. 单击****完成****返回短信编辑器。
4. 单击左侧消息框中的 **添加图像** 图标（图像图标）。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627732370587)
5. 转到****动态图像****选项卡。
6. 粘贴以下目录标签：
   **{% 目录 event.id %} {{catalog\_item.featured\_image.thumbnail.src}} {% endcatalog %}**
7. 将 **{% Catalog event.id %}** 中的 **event.id** 替换为您之前复制的标签中的变量。从变量中删除括号和所有过滤器（因此 **{{ event.extra.line\_items.0.product\_id|default:'' }}** 变为 **event.extra.line\_items.0.product\_id**）。
   示例： **{% Catalog event.extra.line\_items.0.product\_id %} {{catalog\_item.featured\_image.thumbnail.src}} {% endcatalog %}**
8. 单击****保存****。

****使用条件语句的示例****

动态图像可以使用条件语句。

下面是 if/else 语句的示例，表示如果存在变体图像，请将其显示给收件人；否则，使用默认图像：
{% if event.extra.line\_items.0.product.variant.images.0.src %}{{ event.extra.line\_items.0.product.variant.images.0.src }}{% else %}{{ event.extra.line\_items.0.product.images.0.src }}{% endif %}

请注意，这些语句的确切格式取决于您的集成，您不应从电子邮件模板中复制它们。

## 其他资源

- 查找更多[MMS图像和GIF最佳实践](https://help.klaviyo.com/hc/en-us/articles/360041074911)
- 了解有关 Klaviyo 中事件变量的更多信息：
  - [关于使用事件变量个性化流程](https://help.klaviyo.com/hc/en-us/articles/115002779071)
  - [如何在基于事件的流程电子邮件中插入动态图像](https://help.klaviyo.com/hc/en-us/articles/115000104431)