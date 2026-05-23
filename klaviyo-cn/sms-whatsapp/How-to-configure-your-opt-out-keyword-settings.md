---
id: "29109965092251"
title: "如何配置您的选择退出关键字设置"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/29109965092251-How-to-configure-your-opt-out-keyword-settings"
section: "Understanding SMS compliance settings"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: "zh"
---
您必须是所有者、管理员或经理才能使用此功能。

## 你将会学到

了解如何控制选择退出关键字何时导致取消订阅。

选择退出关键字是一种合规关键字，需要操作和响应（即删除同意，然后确认选择退出）。借助此功能，当订阅者发送选择退出关键字时，您可以选择删除同意：

- Anywhere in an SMS (contains word)
  或
- 作为短信中的唯一单词（完全匹配）

此信息仅用于教育和信息目的，****不****应被解释为法律建议。所提供的内容本质上是一般性的，可能不反映最新的信息。 Klaviyo 强烈建议您咨询合格的法律顾问，以确保您遵守与使用我们的服务相关的适用法律和法规。

## 开始之前

请注意以下事项：

- 对于美国的任何订阅者，您无法将 STOP 关键字设置为**完全匹配**。
  - 每当美国号码在短信中包含“停止”一词时，Klaviyo 就会自动立即删除短信同意。
  - 这是为了保护您免受潜在的合规问题的影响，因为美国有关 STOP 关键字的法律更为严格。
- 无论使用哪个选择退出关键字，选择退出关键字的自动响应始终使用“停止”一词。
- 您无法编辑选择退出关键字的自动响应。

有关更多信息，请参阅这篇[有关合规性关键字如何工作的文章。](https://help.klaviyo.com/hc/en-us/articles/29928896469531)

## How each option for opt-out keywords works

当消息包含选择退出关键字时，Klaviyo 提供 2 个选项：

1.****包含单词****（默认）

   - 如果选择退出关键字出现在短信中的任何位置，或者该词完全匹配，则订阅者将选择退出（例如，如果有人发短信“取消订阅”，则会删除短信同意）。
   - 推荐给：那些想要严格遵守规定的人。

   |  |  |
   | --- | --- |
   | ![](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/12157e7bbe0b8db639bf5a505e8d9ef517a1b71f-668x538.png) | ![](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/08f204d50cf4df31445de63147d52e01031852ce-668x538.png) |
2.****完全匹配****

- 当消息仅包含选择退出关键字而没有其他内容时，订阅者将选择退出（例如，某人必须发短信“取消”（不区分大小写）才能同意删除）。
- 推荐用于：使用“取消”、“取消订阅”、“结束”和“退出”等词语的订阅业务。 （客户可以在讨论订阅本身时发送这些内容，而不是在短信同意时发送。）

![](https://klaviyo.zendesk.com/hc/article_attachments/29154296049435)

请注意，无论订阅者实际发送的文本选择退出关键字如何，网络消息始终包含“停止”一词。

## Change your opt-out keyword settings

对于美国订阅者，您无法配置 STOP 关键字的设置。

1. 在左下角选择您的帐户名。
2. 导航至****设置 > 短信 > 关键字响应****。
3. 单击选择退出关键字旁边的****编辑****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/29154311168027)
4. 选择您要配置的退出关键字旁边的下拉列表（例如，**取消**）。

   - 此功能不适用于美国的 STOP 关键字。！[](https://klaviyo.zendesk.com/hc/article_attachments/29158591823131)
5. 选择：

   - ****Contains word**** (default)
     The opt-out keyword appears anywhere in an SMS.
   - ****完全匹配****
     The opt-out keyword is the only word in the SMS.
6. 在保存之前查看有关更改选择退出关键字设置的警告消息。
7. 选择****保存**** 将此设置用于 opt 关键字。