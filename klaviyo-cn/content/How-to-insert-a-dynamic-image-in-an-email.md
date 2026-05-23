---
id: "4408810769307"
title: "如何在电子邮件中插入动态图像"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4408810769307-How-to-insert-a-dynamic-image-in-an-email"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:55:00Z"
language: "zh"
---
## 你将会学到

了解电子邮件图像块中的 **动态图像** 选项，包括如何找到要使用的正确个性化标签并将其添加到电子邮件模板中。动态图像允许您根据 Klaviyo 个人资料或事件数据中存储的数据自定义每个收件人的消息。例如，您可以使用此功能在“添加到购物车”指标触发的流程中显示他们最近添加到购物车的商品。或者，通过在订阅者的个人资料中存储唯一的图像 URL，您可以在向他们发送的营销活动中显示该自定义图像。 ## 将您的图像存储在个人资料或活动中

您可以在指标触发的流电子邮件中显示事件数据的动态图像（例如，废弃购物车流的开始结账事件）。事件数据中存储的图像无法在营销活动或非指标触发流中显示，这些流只能使用收件人个人资料中存储的图像作为个人资料属性。 ### 存储活动图像和非指标触发流

要在活动或非指标触发流（即由列表、细分或日期触发的流）中显示动态图像，图像 URL（例如 <https://www.klaviyo.com/static/klaviyo-social-share-image.jpg>）必须存储在每个收件人的个人资料属性中。您可以通过以下方式将图像 URL 添加到其个人资料属性中：

- [上传 CSV 个人资料数据](https://klaviyo.zendesk.com/hc/en-us/articles/1260806293150)
- [使用第三方集成](https://klaviyo.zendesk.com/hc/en-us/articles/360049626051)
- [使用 Klaviyo 的 API](https://developers.klaviyo.com/en/reference/api_overview)

### 存储指标触发流的图像

要在指标触发的流（例如，由“添加到购物车”事件触发的流）中显示动态图像，您可以使用使用上述方法存储的配置文件数据，也可以使用触发该流的指标中的事件数据。请注意，事件数据只能在该事件触发的流程中使用。您可以通过以下方式将事件数据添加到 Klaviyo：

- [通过默认的 Klaviyo 集成](https://klaviyo.zendesk.com/hc/en-us/articles/115000256472)
- [通过第三方集成](https://klaviyo.zendesk.com/hc/en-us/articles/360049626051)
- [使用 Klaviyo 的 API](https://developers.klaviyo.com/en/reference/api_overview)

## 在电子邮件中添加动态图像

将动态图像信息存储在 Klaviyo 中后，请确定用于将其包含在电子邮件中的正确标签。 1. 打开您要添加动态图像的电子邮件模板。 2. 单击****预览和测试****。 3. 滚动浏览****所有属性****下的示例事件和配置文件数据，直到找到图像变量。然后，单击变量名称进行复制。 4. 复制标签后，将图像块拖到消息中。 5. 单击****选择图像> 动态图像****。 6. 将标签粘贴到**动态变量或动态 URL** 字段中。 7. 最后，预览您的电子邮件以确保标签正常工作。如果您没有看到图像，请仔细检查您是否选择了包含您使用的变量的事件或配置文件。 ## 添加备份图片

如果您不确定每个电子邮件收件人的个人资料或事件数据中都会有可用的图像，请考虑使用备份图像，以便该区域不会显示为空白。有 2 种方法可以添加备份图像：

### 使用缺失的产品过滤器

将缺少的产品过滤器添加到动态图像变量的末尾以使用 Klaviyo 的默认备份图像。要添加此过滤器，请在动态图像变量后面添加 |missing\_product\_image，如下所示：

`{{ event.image_url|missing_product_image }}`

如果收到电子邮件的任何人缺少图像，他们将看到缺少的产品图像：

![丢失的图像占位符](https://klaviyo.zendesk.com/hc/article_attachments/28704485792155)

### 设置您自己的备份映像

要选择您自己的备份图像，请应用带有您选择的图像 URL 的默认过滤器。如果收件人没有设置图像，这将显示您的自定义备份图像。 要添加此过滤器，请将 |default:'' 添加到图像变量的末尾，并在单引号之间添加自定义图像 URL，如下所示：

`{{ event.image_url|默认:'www.example.com/custom_image_url.jpg' }}`

## 其他资源

- [如何在文本块中添加个性化](https://help.klaviyo.com/hc/en-us/articles/4408810654235)
- [如何在流电子邮件中构建动态块](https://help.klaviyo.com/hc/en-us/articles/4408802597659)
- [如何创建指标触发流](https://klaviyo.zendesk.com/hc/en-us/articles/360003057151)
- [如何将资源直接嵌入到电子邮件中](https://klaviyo.zendesk.com/hc/en-us/articles/115005256968)