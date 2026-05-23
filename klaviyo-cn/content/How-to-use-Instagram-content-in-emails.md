---
id: "360004384031"
title: "如何在电子邮件中使用 Instagram 内容"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360004384031-How-to-use-Instagram-content-in-emails"
section: "Build and use templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: "zh"
---
## 你将会学到

了解如何使用 RSS feed 生成器通过您的 Instagram 帐户设置自定义 Web feed，以及如何在电子邮件中显示 feed。通过自定义网络源，您可以将 Instagram 内容连接到电子邮件并动态显示最新的 Instagram 照片、标题等。此过程需要设置 XML 源并将自定义代码插入到您的电子邮件模板中。如果您不习惯编辑电子邮件代码，请联系 [Klaviyo 合作伙伴](https://connect.klaviyo.com/) 寻求帮助。 ## 设置 Instagram 网络源

要在没有开发人员或 Klaviyo 合作伙伴帮助的情况下设置 Instagram 网络源，请使用 RSS 源生成器。请注意，此 RSS 提要生成器应用程序需要付费计划才能托管 Instagram RSS 提要。您可以使用任何 RSS 源生成器，但如果您使用不同的应用程序，则可能需要自定义以下部分中的示例代码。 1. 使用[RSS feed生成器工具](https://rss.app/)创建一个帐户。 2. 导航至[我的动态](https://rss.app/myfeeds)。 3. 在右上角，单击****新源****。 4. 在 **输入网页 URL** 字段中，添加您的 Instagram URL，格式为 https://www.instagram.com/YOUR\_USERNAME。 5. 单击****生成****。 6. 单击****保存到我的源****。保存 Feed 后，导航至 Feed 页面并找到 Feed URL。它应遵循以下格式：<https://rss.app/feeds/UNIQUE_FEED_ID.xml>。 ![提要 URL](https://klaviyo.zendesk.com/hc/article_attachments/28720656477851)

作为此方法的替代方法，您可以使用其基本显示 API 或使用第三方应用程序来设置 Instagram 网络源。某些 [Klaviyo 合作伙伴](https://connect.klaviyo.com/) 将此作为服务提供，例如 [FourSixty](https://connect.klaviyo.com/integrations/foursixty)。 ## 在 Klaviyo 中设置您的 feed

设置 RSS 源后：

1. 单击 Klaviyo 左下角您的帐户名称。 2. 选择****设置****。 3. 选择****其他****。 4. 打开****网络源****选项卡。 5. 单击****添加网络源****。 ![添加网络提要](https://klaviyo.zendesk.com/hc/article_attachments/28720668265883)
6. 为您的 feed 命名，并输入您刚刚生成的 RSS feed URL，作为上一节中的 **Feed URL**。 7. 将**请求方法**设置为****GET****，将**内容类型**设置为****XML****。 ![提要设置](https://klaviyo.zendesk.com/hc/article_attachments/28720668267931)
8. 单击****添加网络源****。 ## 将 Instagram 内容放入您的电子邮件中

如果您使用第三方平台或 Instagram 的基本显示 API 来生成 Feed，请按照我们的[向电子邮件添加自定义 Web Feed 的指南](https://help.klaviyo.com/hc/en-us/articles/115005258768-Guide-to-Adding-a-Custom-Web-Feed-in-an-Email) 操作。如果您使用过上面推荐的 RSS feed 应用，请使用下面的代码在电子邮件中显示 Instagram feed 中的 3 个最新项目。 1. 将新的 HTML 块添加到您的模板中。 2. 将以下代码复制到 HTML 块中，并确保将 FEED\_NAME 替换为您的 Feed 名称（例如上例中的 **Instagram\_Feed**）。 ````
<div>{% for feeds.FEED_NAME.rss.channel.item|slice:":3" %}
    <table style="display:inline-block; margin-left:auto; margin-right:auto">
	<正文>
	    <tr>
		<td style="width:150px; text-align: center;"><a href="{{ item.link }}">
		  <img style="max-width: 150px; height: auto;" src="{% if item|lookup:'media:content'|lookup:'0'|lookup:'@url' %}{{ item|lookup:'media:content'|lookup:'0'|lookup:'@url' }}{% else %}{{ item|lookup:'media:content'|lookup:'@url' }}{% endif %}" style="margin: 1px; max-width: 150px;高度：自动；” /></a>
		</td>
	    </tr>
	</tbody>
    </表>
{% endfor %}</div>
````

在 Klaviyo 中预览消息时，您的 Instagram feed 将不会加载。将预览电子邮件发送到您自己的收件箱以确保其正确显示。如果您想显示超过 3 个最近的帖子，请调整过滤器 **|slice:":3"**，以包含您要显示的帖子数（例如 |slice:":6" 显示 6 个帖子）。如果您想向表格添加其他字段（例如标题或图像发布日期），请按照我们的[向电子邮件添加自定义网络源](https://help.klaviyo.com/hc/en-us/articles/115005258768-Guide-to-Adding-a-Custom-Web-Feed-in-an-Email)指南根据需要调整上面的代码。我们仅建议精通技术的营销人员或有权访问开发人员的任何人使用自定义 HTML。 虽然我们的产品确实支持自定义 HTML，但我们的支持团队除了提供本文档中涵盖的一般指导之外，无法帮助您构建自定义模板。为了维护您的数据安全，Klaviyo 的支持团队无法打开您的 HTML 文件。如果您需要开发人员帮助来进行设置，请联系 [Klaviyo 的合作伙伴](https://klaviyo.partnerpage.io/) 之一。