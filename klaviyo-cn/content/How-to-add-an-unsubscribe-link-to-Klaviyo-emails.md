---
id: "115006054267"
title: "如何向 Klaviyo 电子邮件添加取消订阅链接"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115006054267-How-to-add-an-unsubscribe-link-to-Klaviyo-emails"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:26Z"
language: "zh"
---
## 你将会学到

了解如何在您的 Klaviyo 电子邮件活动和流程中包含取消订阅链接。 ## 包含取消订阅链接的重要性

Klaviyo 要求所有电子邮件中都包含取消订阅链接。为什么？一方面，这是法律。 [CAN-SPAM 法案](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) 要求所有商业电子邮件“必须包含清晰且明显的解释，说明收件人将来如何选择不再接收您的电子邮件。”您还必须在 10 个工作日内尊重收件人的选择退出请求。包含取消订阅链接对于保持良好的发件人声誉至关重要。如果您不允许收件人选择退出并决定是否/何时停止接收您的电子邮件，他们更有可能通过收件箱服务将您的电子邮件标记为垃圾邮件。垃圾邮件投诉非常严重，可能会严重损害您的电子邮件送达率。如果您的滥用率甚至达到 0.1%，邮箱提供商（例如 Gmail、Hotmail 和 Yahoo）就会开始将您视为“不良发件人”，并自行处理问题，将您的电子邮件过滤为所有收件人的垃圾邮件。 ### 如果我忘记了怎么办？如果 Klaviyo 在您的一封电子邮件中没有检测到取消订阅标签，它会自动在您的电子邮件底部添加一个取消订阅链接，其中包含基本的取消订阅标签。 ![默认取消订阅页脚](https://klaviyo.zendesk.com/hc/article_attachments/28720656374299)

## 添加取消订阅链接

默认情况下，基本标签将生成带有文本“取消订阅”的链接。

1. 导航至您的电子邮件模板。 2. 选择现有文本块或将新文本块添加到电子邮件中。 3. 双击块打开文本编辑菜单。 4. 单击文本编辑菜单中的个性化图标。 5. 从****所有类型****菜单中，选择****链接和预览****。 6. 选择****取消订阅****。 ![取消订阅菜单选项](https://klaviyo.zendesk.com/hc/article_attachments/28720668168859)

当收件人单击 Klaviyo 取消订阅链接时，他们将进入确认页面以确认取消订阅请求。 ## 取消订阅链接的样式

您可以在文本编辑器中根据需要设置取消订阅文本的样式。请注意，通过 Klaviyo 发送的所有电子邮件（即使用拖放编辑器构建的电子邮件、纯文本电子邮件和自定义 HTML 电子邮件）都支持以下标签。要自定义生成的链接的文本：

1.插入标签：`{% unsubscribe %}`
2. 在 **unsubscribe** 后添加两个单引号以及您想要的文本：`{% unsubscribe 'YOUR UNSUBSCRIBE TEXT' %}`

### 对损坏的取消订阅链接进行故障排除

如果您在按钮中使用默认的“{% unsubscribe %}”标记或作为文本链接的 **URL**，它将中断。这是因为默认取消订阅标记会生成完整的 HTML 链接，而不仅仅是 URL。 ![损坏的取消订阅链接](https://klaviyo.zendesk.com/hc/article_attachments/30007938335387)

如果发生这种情况，请改用以下标签：`{% unsubscribe_link %}`

此标记比默认标记提供更多控制，因为它仅生成取消订阅 URL。使用方法：

- 超链接文本时将其添加到 **URL** 字段。 ![URL 字段](https://klaviyo.zendesk.com/hc/article_attachments/30007938339611)
- 将其添加到按钮块的 **链接地址** 字段。 ![按钮块的链接地址字段](https://klaviyo.zendesk.com/hc/article_attachments/30007938342939)
- 使用自定义 HTML，将取消订阅标签放在 <a href></a> 标签内：`<a href ="{% unsubscribe_link %}" style="color: red;">在此处取消订阅。</a>`

## 添加一键取消订阅以满足 Yahoo 和 Google 发件人要求

您无需采取任何操作即可满足 Google 和 Yahoo 对批量发件人的一键取消订阅要求。 Klaviyo 会自动将代码添加到您发送的每封电子邮件的标题中，以便对受支持的收件箱启用一键取消订阅。详细了解 [Yahoo 和 Google 的电子邮件发件人要求](https://academy.klaviyo.com/2024-new-sender-requirements-checklist/1817230)。 ## 取消订阅链接最佳实践

最佳做法是让您的取消订阅链接可见且易于访问。轻松取消订阅可以减少客户的挫败感，这也是许多收件箱提供商的要求。请遵循以下最佳实践，以确保您的取消订阅链接易于找到：

- 使用[符合辅助功能标准]的颜色(https://help.klaviyo.com/hc/en-us/articles/360034711931)。 确保文本和背景颜色之间有高对比度。 ![在颜色选择方面具有良好和不良可访问性的电子邮件页脚示例](https://klaviyo.zendesk.com/hc/article_attachments/28720668162459)
- 不要使用比周围文本小很多的字体。 - 不要将取消订阅链接隐藏在长句子中，或将超链接的单词更改为难以浏览的内容。 ![带有容易和难以找到的取消订阅按钮的电子邮件页脚示例](https://klaviyo.zendesk.com/hc/article_attachments/28720656365083)
- 使用与文本其余部分不同的链接颜色。不要手动更改链接颜色，以免其混合在一起并且难以阅读。 ![带有易于识别和伪装取消订阅按钮的电子邮件页脚示例](https://klaviyo.zendesk.com/hc/article_attachments/28720656366875)