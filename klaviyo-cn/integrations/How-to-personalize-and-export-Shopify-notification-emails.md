---
id: "115005080587"
title: "如何个性化和导出 Shopify 通知电子邮件"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005080587-How-to-personalize-and-export-Shopify-notification-emails"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "zh"
---
## 你将会学到

了解如何使用 Klaviyo 自定义 Shopify 的默认电子邮件模板，以在所有通知中实现品牌一致性。 Shopify 提供了许多默认电子邮件模板，可在 Shopify 中使用这些模板来进行自动通知，例如发货更新和密码重置。虽然这些模板很实用，但 Shopify 中没有内置模板编辑器可用于自定义和设计这些电子邮件的样式。使用 Klaviyo，您可以使用独特的布局和样式完全自定义 Shopify 通知模板，然后将其导出并粘贴到 Shopify 中，以便通过 Shopify（不是 Klaviyo）发送它们。 ## 开始之前

####知识检查

如果您尚未阅读我们的 [Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) 指南，了解有关集成的分步说明，然后再继续阅读本文。 - Klaviyo 保存您所有的电子邮件模板。如果您决定更改徽标或网站主题，可以轻松返回并相应更新您的通知电子邮件。进行任何更改后，您需要将更新后的模板重新导入 Shopify。 - 您可以在此处找到 [Shopify 通知变量](https://help.shopify.com/en/manual/orders/notifications/email-variables) 的完整列表。您可以使用这些变量中的任何一个来自定义您的 Shopify 电子邮件模板。 - Shopify 目前不支持使用 Klaviyo 产品块，该块用于在电子邮件中动态填充您的产品。因此，如果您尝试从具有产品块的 Klaviyo 导出通知模板，您将看到一条错误消息，或者****导出****选项将灰显。如果删除该块，您应该能够成功导出模板。 - 您在这些模板中看到的所有变量都是 Shopify 变量，与 Klaviyo 变量不同。虽然您可以按照自己喜欢的方式编辑内容并自定义这些模板，但使用动态变量编辑块时请务必小心。如果您进行太多更改，可能会影响模板的功能。 - 直接在 Shopify 中预览编辑后的电子邮件模板，以了解客户将收到的内容。您还可以在 Klaviyo 中预览这些模板，但仅限于样式目的 — 除非您在 Shopify 中预览，否则您将无法看到填充有动态内容的变量。 ## 编辑模板

1. 在 Klaviyo 中，单击****内容****下拉列表并选择****模板****。 2. 在****电子邮件模板****选项卡中，单击****模板类型****下拉列表并选择****Shopify****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33747868617883)
3. 此视图显示多个预构建的 Shopify 通知模板，您可以自定义这些模板并将其导出到 Shopify 中。选择您想要使用的模板。在出现的模式中，单击****使用模板****。 4. 编辑模板以匹配您的品牌风格。然后，您的模板将出现在模板库的****电子邮件：已保存****选项卡中。 ## 将模板导出到 Shopify

所有 Shopify 通知电子邮件均通过 Shopify 发送，而不是 Klaviyo。自定义模板后，您需要一次导出一封电子邮件的 HTML 代码并将其粘贴到 Shopify 中。对于每个电子邮件模板：

1. 单击****内容****下拉列表并选择****模板****选项卡。 2. 找到您的模板并单击三个点，然后选择****导出。**** 将出现 **导出模板 HTML** 窗口。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33747822587931)
3. 复制窗口中的 HTML 代码，以便将其粘贴到 Shopify 中。 4. 在您的 Shopify 商店后台中，点击****设置********>**** ****通知。****
5. 在这里找到您想要更新的通知模板并单击它。 6. 您将立即看到一大块标有**电子邮件正文 (HTML)** 的部分。将您在此窗口中看到的现有代码替换为您从 Klaviyo 复制的代码。 7. 单击****预览****。您应该会看到一封示例电子邮件，其中反映了您在 Klaviyo 中设计的自定义模板。 ![Shopify 中的发货确认电子邮件模板显示电子邮件主题、电子邮件正文 HTML，以及预览、发送测试电子邮件和保存选项](https://klaviyo.zendesk.com/hc/article_attachments/28720621942171)
8. 单击****保存。****

## 结果

自定义每个电子邮件模板并将 HTML 添加到 Shopify 后，Shopify 发送的通知电子邮件将进行个性化并反映您的品牌风格。 ## 其他资源

- [Shopify 入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005080407)
- [如何禁用 Shopify 发送的通知电子邮件](https://help.klaviyo.com/hc/en-us/articles/4403589811611-How-to-Disable-Notification-Emails-Sent-by-Shopify)
- [Shopify 数据参考](https://help.klaviyo.com/hc/en-us/articles/115005080447-Reviewing-Your-Shopify-Data)