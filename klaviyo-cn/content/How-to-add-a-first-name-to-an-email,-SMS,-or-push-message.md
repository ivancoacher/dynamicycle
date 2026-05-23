---
id: "11613154130843"
title: "如何将名字添加到电子邮件、短信或推送消息中"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/11613154130843-How-to-add-a-first-name-to-an-email-SMS-or-push-message"
section: "Use variable syntax and tags"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-11T10:58:12Z"
language: "zh"
---
## 你将会学到

了解如何添加一个变量来动态填充电子邮件、短信或推送消息中收件人的名字。这些在活动和流程、任何消息的正文以及电子邮件的主题行中得到支持。

## 添加名字变量

1. 在 Klaviyo 中打开消息（即电子邮件、短信或推送）。
2. 单击文本字段格式栏中的个性化图标。
3. 从列表中选择****名字****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32002440882971)
4. 可选：在 **默认文本** 字段中，添加要向未设置名字的收件人显示的文本。例如，如果您有一行内容为“Hey FIRST\_NAME”，则可以使用 **there** 作为默认文本。
   - 如果未设置收件人的名字，他们的消息将显示为“嘿那里”，而不是“嘿 FIRST\_NAME”。
5. 可选：从 **大写** 菜单中选择一个可选：
   - ****输入时****
     收件人的姓名将按照其个人资料中的名称显示。
   - ****Ag****（即标题大小写）
     收件人姓名将转换为首字母大写（即第一个字母大写，所有其他字母小写）。
   - ****AG****（即大写）
     收件人姓名将转换为全部大写字母。
   - ****ag****（即小写）
     收件人姓名将转换为全部小写字母。
6. 单击****插入****。
7. 请注意出现的标签：“{{ first_name|title|default:'there' }}”（如果您将 **there** 设置为默认文本并选择 ****Ag****（即标题大小写）。

当您发送消息时，此标签将替换为每个收件人的姓名。

## 自定义你的名字变量

在上面的示例中，“|default:'there'”和“|title”是过滤器。 Klaviyo 提供了多种过滤器来自定义变量的显示方式。 了解有关[在 Klaviyo 中使用过滤器](https://help.klaviyo.com/hc/en-us/articles/360058907911) 的更多信息。

## 其他资源

- 查看消息的更多个性化选项：[消息个性化参考](https://help.klaviyo.com/hc/en-us/articles/4408802648731)
- 了解如何使用预览面板查找个性化标签：[如何使用预览面板进行消息个性化](https://klaviyo.zendesk.com/hc/en-us/articles/27843522951707)
- 了解如何使用电子邮件编辑器：[电子邮件模板编辑器指南](https://help.klaviyo.com/hc/en-us/articles/4407911841435)
- 博客文章：[各个级别的短信营销策略[+12个专业技巧]](https://www.klaviyo.com/blog/sms-marketing-strategies)