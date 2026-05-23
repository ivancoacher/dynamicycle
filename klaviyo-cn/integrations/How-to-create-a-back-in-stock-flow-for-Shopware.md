---
id: "13325405718939"
title: "如何为 Shopware 创建库存返还流程"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/13325405718939-How-to-create-a-back-in-stock-flow-for-Shopware"
section: "Shopware"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:28Z"
language: "zh"
---
## 你将会学到

了解如何为 Shopware 6 创建库存补货流程，以提醒客户有关库存的信息。此流程将使用从您的 Shopware 商店同步的 **订阅返回库存** 事件。 ## 开始之前

确保执行以下操作：

- 与 Shopware 6 集成（请参阅 [Shopware 入门](https://help.klaviyo.com/hc/en-us/articles/13001662470939) 了解具体操作方法）。作为集成过程的一部分，请确保：

- 在您的扩展程序设置中打开 **Track Back in Stock**，这会将 **订阅 Back in Stock** 事件同步到 Klaviyo。 ![追踪库存设置切换为蓝色](https://klaviyo.zendesk.com/hc/article_attachments/28715965319451)
- 将您的 Shopware 6 产品目录同步到 Klaviyo。 ## 在 Shopware 中自定义您的“返回库存”按钮和表单

仅当产品缺货并标记为清仓促销时，“库存补货”表单才会出现在产品详细信息页面上。如果您要追踪库存（通过 Shopware 中的扩展设置），您还可以自定义网站上的“库存恢复时通知我”按钮（针对缺货商品显示）和表单。客户必须单击按钮并填写表格才能接收库存补货通知。要自定义这些元素：

1. 登录您的 Shopware 管理员。 2. 导航至****设置 > 扩展 > Klaviyo****。 3. 向下滚动到**返货弹窗样式**，您可以在其中自定义返货弹窗打开按钮、弹窗关闭按钮和订阅按钮的文字颜色和背景。 ![弹出打开按钮设置，颜色设置为白色，背景设置为深蓝色](https://klaviyo.zendesk.com/hc/article_attachments/28715965322267)
4. 单击正方形，然后使用选择器选择颜色，或者，如果您有品牌颜色的十六进制颜色代码，请将其粘贴到相应的框中。 5. 在**代码段名称**下，如果您希望在站点代码中自定义它们，您将找到有关如何在 HTML 中引用不同库存组件的参考。 ![打开按钮、关闭按钮和电子邮件字段标签的片段名称](https://klaviyo.zendesk.com/hc/article_attachments/28715971891739)
6. 完成后，单击****保存****。 ## 在 Klaviyo 中配置您的库存设置

接下来，[在 Klaviyo 中配置您的库存设置](https://help.klaviyo.com/hc/en-us/articles/115003872251-How-to-build-a-back-in-stock-flow#back-in-stock-flow-settings2)：最低库存规则和客户通知规则。 - 最低库存规则是指在您通知订阅者之前需要补充多少商品。 - 客户通知规则允许您选择要通知的客户数量以及通知之间等待的时间。 ## 创建流程

1. 在 Klaviyo 中，选择****流程****选项卡。 2. 单击****创建流程****，然后****从头开始创建****。 3. 为您的流程命名，然后单击****创建流程****。 4. 在流程构建器中，选择触发选项****指标****，然后选择 Klaviyo 指标****订阅返回库存****。不要添加任何触发器或流过滤器，然后单击****保存****。 5. 紧接着触发后，拖入“返回库存延迟”。进入您流程的收件人将在此延迟后等待，直到他们感兴趣的商品重新进货。发生这种情况后，他们将继续流程中的下一步，在本例中是您在延迟后添加的电子邮件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28715965332123)
6. 使用动态变量设计您的库存电子邮件，以提取此通知的产品信息。 [了解如何使用动态事件数据对流进行个性化](https://help.klaviyo.com/hc/en-us/articles/115002779071-Personalize-Flow-Emails-with-Dynamic-Event-Data)。 7. 通常，您在此流程中只需要一条消息作为该项目已返回的通知。 [关闭智能发送](https://help.klaviyo.com/hc/en-us/articles/115002779311-Smart-Sending-for-Flows#how-to-disable-smart-sending) 此消息可确保每个人都收到警报。 8. 您不需要为此系列添加任何额外的时间延迟，因为库存延迟将确保进入您的流程的每个人都会等到他们订阅的商品回到库存后再继续。 9. 要了解流状态以及如何实时设置流，请阅读[流入门](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-started-with-flows)。 有关库存回流的更多指导，请阅读[如何构建库存回流](https://help.klaviyo.com/hc/en-us/articles/115003872251)。 ## 结果

您已经为 Shopware 6 创建了库存流。现在，您可以更好地个性化您的客户沟通并增加收入。 ## 其他资源

- [了解库存流量回流的工作原理](https://help.klaviyo.com/hc/en-us/articles/360051612551-Understanding-how-back-in-stock-flows-work)
- [商店软件数据参考](https://help.klaviyo.com/hc/en-us/articles/13006716790299)
- [如何使用动态事件数据个性化流](https://help.klaviyo.com/hc/en-us/articles/115002779071-Personalize-Flow-Emails-with-Dynamic-Event-Data)