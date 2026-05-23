---
id: "18596283143707"
title: "如何将动态图像添加到推送通知"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18596283143707-How-to-add-a-dynamic-image-to-a-push-notification"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:11Z"
language: "zh"
---
## 你将会学到

了解如何将动态图像添加到推送通知。

动态图像是个性化推送通知的好方法。例如，您可以向某人展示他们最喜欢、开始结账或购买的确切产品。

## 开始之前

您可以在以下位置使用动态图像：

- 指标触发的流程，使用事件数据（例如结账或下订单中的商品）或事件的目录标签。
- 营销活动以及列表和分段触发的流，但仅当图像 URL 作为收件人个人资料中的自定义属性存在时。

  另外，关于推送动态图片，还需要注意以下几点：
- 每个推送通知仅允许使用 1 个动态图像。
- 图片必须小于 1 MB。
- 您可以对动态图像使用条件语句。

想要请求 Klaviyo 推送通知功能吗？填写此 [Google 表单](https://forms.gle/7iPm6JQ4eKB6H2C4A) 告诉我们！

## 添加动态图像到推送通知

1. 选择要包含动态图像的消息。
2. 在左侧边栏中，单击****配置内容****或****编辑****。
3. 在流程中添加或选择推送通知。
4. 单击右上角的****查看详细信息****图标。
   ![推送预览窗口中的查看详细信息图标](https://klaviyo.zendesk.com/hc/article_attachments/28717418395291)
5. 找到要包含的图像的数据源。
6. 单击图像第一个变量的数据源，该变量通常以 0 结尾。
   ![图像数据源的示例](https://klaviyo.zendesk.com/hc/article_attachments/28717391149467)
7. 在左侧，单击 **正文** 框中的 **插入媒体** 图标。
   ![将媒体添加到push.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717391154459)
8. 转到****动态图像****选项卡。
9. 粘贴图像的动态变量或动态 URL。
   ![粘贴示例变量后的动态图像选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28717418408731)
10. 单击****保存****。
11. 通过确保动态图像出现在预览屏幕中来检查动态图像是否已正确添加。

****使用目录标签的示例****

您还可以使用目录标签在丰富的推送通知中添加动态图像。为此：

1. 转到****分析 > 指标****。
2. 选择您要使用的指标（例如，**订购的产品**）。
3. 单击特定事件的****详细信息****。
4. 查找 SKU 或产品 ID 标签。
5. 复制标签的标签（括号或冒号除外），以便获得准确的拼写和大小写。
   在下面的示例中，我们复制“ProductID”。
   ![image5.png](https://klaviyo.zendesk.com/hc/article_attachments/28717391147547)
6. 将其粘贴到不会丢失的地方。
7. 导航到由您刚刚选择的同一指标触发的流。
8. 选择要在其中包含动态图像的推送通知。
9. 在左侧边栏中，单击****配置内容****或****编辑****。
10. 在左侧，单击 **正文** 框中的 **插入媒体** 图标。
    ![将媒体添加到push.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717391154459)
11. 转到****动态图像****选项卡。
12. 粘贴以下目录标签：
    {% 目录 event.id %} {{catalog\_item.featured\_image.thumbnail.src}} {% endcatalog %}
13. 将 {% Catalog event.id %} 中的 id 替换为您之前复制的标签。
    示例： {% 目录 event.ProductID %} {{catalog\_item.featured\_image.thumbnail.src}} {% endcatalog %}
14. 单击****保存****。

****动态图像条件语句的使用示例****

动态图像可以使用条件语句。

下面是 if/else 语句的示例，表示如果存在变体图像，请将其显示给收件人；否则，使用默认图像：

**{% if event.extra.line\_items.0.product.variant.images.0.src %}{{ event.extra.line\_items.0.product.variant.images.0.src }}{% else %}{{ event.extra.line\_items.0.product.images.0.src }}{% endif %}**

请注意，这些语句的确切格式取决于您的集成，并且您不应从电子邮件模板中复制它们。