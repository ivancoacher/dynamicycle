---
id: "115005252988"
title: "如何与Segment集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005252988-How-to-integrate-with-Segment"
section: "Segment"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:23Z"
language: "zh"
---
## 你将会学到

了解如何将 Segment 与 Klaviyo 集成，以便能够触发和过滤流，并使用从 Segment 项目同步到 Klaviyo 的事件定义分段。 Klaviyo 能够将您从 Segment 发出的任何“track”和“identify”调用同步到 Klaviyo。这个集成需要两个步骤：在Segment端启用集成，以及在Klaviyo端启用集成。请务必探索 Segment 的[与 Klaviyo 集成的综合指南](https://segment.com/docs/connections/destinations/catalog/actions-klaviyo/)。 ## 开始之前

此集成现在支持 Segment 和 Klaviyo 之间的双向信息流，但您需要选择 Klaviyo 或 Segment 作为配置文件创建的主要事实来源。如果您选择 Klaviyo 作为主要来源，请注意以下事项：在分段中生成的配置文件包含一个唯一的 ID，Klaviyo 会跟踪该 ID 以记录这些配置文件的来源。 Klaviyo 无法轻松协调来自不同来源的重复配置文件，因此有可能将重复的配置文件推送到分段。有关详细信息，请参阅下面的**在 Klaviyo 中启用集成**部分。 ## 连接 Segment 和 Klaviyo

### 将 Klaviyo 目的地添加到航段

1. 在您的分段项目页面中，单击左侧导航栏中的****连接****，然后单击页面右侧的****添加目标****。 ![网段中的“连接”选项卡，带有蓝色背景的“添加目的地”按钮](https://klaviyo.zendesk.com/hc/article_attachments/28723518315803)
2. 在段目录中搜索 **Klaviyo**。出现后，单击 Klaviyo 磁贴，然后单击下一页上的****配置 Klaviyo****。 ![搜索栏中包含 Klaviyo 的细分目录，结果中包含 Klaviyo 卡](https://klaviyo.zendesk.com/hc/article_attachments/28723518312987)
3. 从您的分段项目中选择并确认源。在下一页上，输入以下所有内容：
   - 您的公共 Klaviyo API 密钥。了解[如何在 Klaviyo 中查找您的公共和私有 API 密钥](https://help.klaviyo.com/hc/en-us/articles/115005062267)。 - 您想要同步的默认 Klaviyo 列表的列表 ID。了解[如何在 Klaviyo 中查找您的列表 ID](https://help.klaviyo.com/hc/en-us/articles/115005078647)。 - 私人 Klaviyo API 密钥。将私有 API 密钥视为保存在安全位置且绝不向公众公开的密码。 ![分段中的 Klaviyo 设置页面，包含 API 密钥、列表 ID 和输入您的私有 API 密钥字段](https://klaviyo.zendesk.com/hc/article_attachments/28723506665883)
4. 最后，向下滚动到“**其他设置**”以验证“**强制电子邮件作为主要标识符**”是否设置为“****开****”。默认情况下应将其打开。如果没有，请单击进入设置并将其设置为****开****。 ![“分段其他设置”部分中的 Klaviyo 设置页面，其中“确认选项”设置为“开”，并将“强制电子邮件作为主要标识符”设置为“开”](https://klaviyo.zendesk.com/hc/article_attachments/28723506671643)
5. 要启用 Klaviyo 端的集成，您首先需要从 Segment 获取写入密钥。在“分段”中，导航至****连接 > 来源****，然后单击您想要与 Klaviyo 连接的站点。 ![分段中的“连接”选项卡中的源列表在列表中显示测试网站](https://klaviyo.zendesk.com/hc/article_attachments/28723518319771)
6. 单击顶部的****设置****选项卡，然后选择****API密钥****。 ![在选择“设置”选项卡的“段”中测试网站源页面，源 ID 和写入密钥已模糊](https://klaviyo.zendesk.com/hc/article_attachments/28723506684059)
7. 复制您的**写入密钥**。您的写入密钥是另一个私有 API 密钥。将其视为密码；将其保存在安全的地方，切勿将其暴露给公众。 ### 在 Klaviyo 中启用集成

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 选择****探索应用程序****，搜索**细分**，然后单击该卡。然后，单击****安装****。 3. 将您之前复制的写入密钥粘贴到框中，然后单击****连接到段****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723506700315)
4. 在下一页上，您将能够通过选中 **不同步未由 Klaviyo 目标更新的配置文件**旁边的框来限制传回分段的数据。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28723518331035)
   - 如概述中所述，此集成现在支持在 Segment 和 Klaviyo 之间来回传递信息的功能，使用唯一的 ID 来跟踪哪些配置文件最初来自 Segment。如果您在 Klaviyo 中启用了多个集成，则同一客户可能会从两个不同的来源与您进行交互，因此，该客户最终将在 Klaviyo 中获得重复的配置文件。 - 为了帮助避免跨多个服务的配置文件重复，您可以选中上面的框，这将限制 Klaviyo 与 Segment 同步的配置文件仅限于最初在 Segment 中创建的配置文件。 5. 完成后，单击****完成设置****。 ## 细分指标

我们建议将最重要的事件同步到 Klaviyo，例如：

- 当客户注册时
- 当顾客开始结账或表示有兴趣付款时
- 顾客购买了什么（包括商品图片和商品描述）

对于您通过 Segment 发送的每个事件，客户均通过其电子邮件地址进行识别。有关如何格式化这些事件的详细信息，请参阅[Segment 的 Klaviyo 集成](https://segment.com/docs/connections/destinations/catalog/actions-klaviyo/) 指南。对于交易网络业务和电子商务平台，我们建议遵循我们的[集成自定义电子商务购物车或平台指南](https://developers.klaviyo.com/en/v1-2/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration)指南，了解有关应通过 Segment 发送到 Klaviyo 的事件的详细信息。 ## 监控 Klaviyo 同步

一旦您激活 Segment 内部的 Klaviyo 集成，您的“identify”和“track”调用将在 5-10 分钟内开始向 Klaviyo 发送数据。要验证 Segment 是否正在向 Klaviyo 发送数据，请单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****选项卡。当事件在 Segment 中触发时，它们会将数据发送到 Klaviyo，其中来自 Segment“track”调用的事件名称用于创建指标名称。 Klaviyo 将分段指标视为第三方 API 指标，因此每个指标在 Klaviyo 中其名称旁边都会有一个齿轮图标。要查看流入 Klaviyo 的数据，请导航至每个指标的 **活动源**。 ![segment9.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28723506691995)

## 结果

现在，您已将 Segment 与 Klaviyo 集成，可以开始使用 Segment 数据来触发和过滤流，并使用从 Segment 项目同步到 Klaviyo 的事件定义段。 ## 其他资源

- [流程入门](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [分段入门](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [如何向流程添加条件拆分](https://help.klaviyo.com/hc/en-us/articles/115003872171)