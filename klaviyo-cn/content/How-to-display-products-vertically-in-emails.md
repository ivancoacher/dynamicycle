---
id: "19462923466651"
title: "如何在电子邮件中垂直显示产品"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19462923466651-How-to-display-products-vertically-in-emails"
section: "Advanced template design"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: "zh"
---
## 你将会学到

了解如何在废弃的购物车中显示产品，并垂直地进行订单确认流程（即在产品信息上方而不是旁边显示图像）。

## 创建垂直产品块

以下说明将帮助您将现有的水平产品块转换为垂直产品块。如果您还没有包含动态内容块的流电子邮件，请[在流库中查找​​](https://help.klaviyo.com/hc/en-us/articles/115002779411)。

1. 在 Klaviyo 侧栏中选择 ****Flows****。
2. 导航至您废弃的购物车或订单确认流程。
3. 单击右上角的****更新操作状态****，在编辑时将流程设置为****手动****。
4. 在包含动态内容块（即显示某人购物车中的产品的表格块）的流程中打开一封电子邮件。
5. 在动态表块的正下方添加一个新部分。
   ![节块](https://klaviyo.zendesk.com/hc/article_attachments/28720660124699)
6. 将图像块和表格块添加到新部分。
7. 从 ****表设置 > 行集合**** 和 ****表设置 > 行别名**** 复制值。
8. 导航至****显示选项****，然后单击****创建重复规则****。
   ![创建重复规则](https://klaviyo.zendesk.com/hc/article_attachments/28720671860123)
9. 将表块中的值分别粘贴到 **Repeat For** 和 **Item alias** 字段中。
   ![新旧重复](https://klaviyo.zendesk.com/hc/article_attachments/28720671874203)
10. 在表格块中，单击 **动态图像** 下的****替换****。
    ![替换动态图片按钮](https://klaviyo.zendesk.com/hc/article_attachments/28720671868699)
11. 在出现的模式中，复制 **动态变量或动态 URL** 字段中的所有内容。
    ![动态图像字段](https://klaviyo.zendesk.com/hc/article_attachments/28720660071067)
12. 单击新部分中的图像块。
13. 单击****浏览图像库****。
14. 选择****动态图像****并粘贴动态 URL。
15. 单击****保存****。
16. 复制表块的 **链接地址** 字段中显示的标签。
    ![图片链接地址](https://klaviyo.zendesk.com/hc/article_attachments/28720660051867)
17. 将此标签粘贴到新图像块的 **链接地址** 字段中。
18. 复制原始表块中的文本内容。
    ![文字内容](https://klaviyo.zendesk.com/hc/article_attachments/28720660130459)
19. 将文本粘贴到新文本块中。
20. 预览电子邮件以确保所有产品信息都显示在新部分中。如果出现错误，请检查所有元素（即行集合、行别名、动态图像 URL 和文本内容）是否已正确传输。
21. 一旦您对新部分感到满意​​，请删除原始表块。
22. （可选）将新部分保存为[通用内容](https://help.klaviyo.com/hc/en-us/articles/115005413888)，以便在流中的其他消息中使用。

## 结果

执行这些步骤后，您的电子邮件将包含垂直产品块（产品信息上方带有图像），而不是水平显示的产品图像和信息。

![垂直产品块](https://klaviyo.zendesk.com/hc/article_attachments/28720671837979)

## 其他资源

- [深色模式电子邮件设计最佳实践](https://klaviyo.zendesk.com/hc/en-us/articles/360049181631)
- [如何在 Klaviyo 中更新您的品牌风格](https://klaviyo.zendesk.com/hc/en-us/articles/4403537778331)