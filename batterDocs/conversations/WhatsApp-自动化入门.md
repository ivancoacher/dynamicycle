---
id: 5827
title: "WhatsApp 自动化入门"
slug: "createwhatsapp"
category: "会话与沟通（Conversations）"
category_slug: "conversations"
wp_url: "https://dynamicycle.com/docs/createwhatsapp/"
wp_modified: "2025-12-25T09:16:40"
---

了解如何构建 WhatsApp 自动化，它可以让您提出问题并发送个性化建议。这不仅是与受众互动的一种快速简便的方法，也是收集更多数据并为您营销策略提供参考的绝佳方式。

##### 开始之前

请注意以下事项：

- 您必须已经设置好 WhatsApp。
- 您的出站消息属于“服务”消息，且是免费的。

每个自动化必须至少包含：

- 1 条消息。每条消息包含 2 个选项。
- 1 个推荐。

自动化要求入站渠道匹配。如果客户通过自动化向品牌发送消息，其消息必须通过同一渠道发送，自动化才能生效。

- 例如，配置了一个通过 WhatsApp 发送消息的自动化。客户必须在 WhatsApp 中回复该自动化才能使其运行，而不能通过 SMS 回复。

##### 构建自动化

###### 设置自动化及其触发关键词

1.导航至 Automations。

2.点击 Create automation。

3.进入新自动化后，点击 Trigger。

4.在右侧栏中选择一种触发类型：

- Always on
- Message response

![界面显示两个选项：'Always on'（始终开启）和'Message response'（消息回复），用于触发WhatsApp自动化消息的设置。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-148.png?resize=618%2C256&ssl=1)

5.输入您想要作为触发关键词的单词或短语。请注意：

触发关键词的运作方式因类型而异：

- 始终开启 (Always on)：通过检查入站短信是否与这些单词完全匹配来运行。

例如：如果您使用“Pets”作为触发关键词，该自动化仅会对“Pets”触发，而不会对“pet”或“petsitter”触发。

- 消息回复 (Message response)：通过检查入站短信是否包含这些单词来运行。

例如：如果您使用“Outdoor furniture”作为触发关键词，该自动化将对包含“Outdoor”和“Furniture”的内容触发。

触发关键词必须满足：

- 3 个或更多字符，最多 20 个字符。唯一性（即不能用于任何其他自动化）。可以包含空格并组成短语，例如：”I love pets”。不区分大小写。”PETS” 仍会触发 “pets”。不能包含特殊字符（如：+、-、&）。
- 不能与订阅或合规关键词（如：STOP、JOIN）关联。

6.点击 Save。

7.要添加更多触发关键词：

- 再次点击触发器。
- 选择 Add keyword。

8.若要根据关键词触发器设置个人资料属性，请开启 Assign responses as a profile property选项。

在下面的示例中，这将创建一个新的自定义个人资料属性“Favorite scent”（最喜欢的香型），其值可以为“Linen”、“Apple Cider”或“Pumpkin”。

![设置触发器的界面，包含关键词选项，如'linen'、'apple cider'和'pumpkin'，以及将响应分配为个人资料属性的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-149.png?resize=438%2C655&ssl=1)

##### 创建您的消息并添加选项

1.点击 Add message。

![自动化设置界面，包含触发器配置和添加消息选项](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-150.png?resize=518%2C267&ssl=1)

2.在 Message（消息）框中输入您的消息文本。

3.为该消息添加至少 2 个选项。请注意：

- 选项按顺序编号。
- 订阅者可以回复选项文本或对应的数字。

选项识别采用“包含”逻辑：

- 选项可以出现在消息中的任何位置（包括作为另一个单词的一部分）。
- 缩写或拼写错误的单词可能会被识别。

选项设置的最佳实践：

- 使用单个数字或字母作为选项（例如数字“21”或仅使用字母“A”）。
- 不使用拼写困难的单词。
- 不使用长短语。

![界面显示用于 WhatsApp 自动化设置的消息部分，包含问题和选择选项，包括猫、狗和其他选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-151.png?resize=708%2C1024&ssl=1)

4.要添加更多选项，请选择 Add Choice。

5.可选：在 Settings（设置）下的 Internal name（内部名称）字段中为您的消息命名。为消息命名可以方便日后参考。

6.若要根据选项设置个人资料属性，请开启 Settings下的 Assign response to a profile property选项。

- 在下面的示例中，这将设置一个名为“Pet”的自定义个人资料属性，其值可以为“Cat”、“Dog”或“Other”。

![显示 WhatsApp 自动化设置界面，内部名称设置为 'Pet'，包含响应分配为个人资料属性的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-152.png?resize=626%2C516&ssl=1)

7.选择Save。

8.点击加号 (+) 按钮并选择 Add message来增加更多消息。

- 建议将每个自动化的消息数量限制在 2-3 条以内。

##### 添加推荐

假设您经营一家纸杯蛋糕店，您的自动化流程正试图引导客户找到他们喜爱的产品。您的推荐可以充分利用用户对类似“香草还是巧克力？”或“您最喜欢的水果是什么？”等问题的回答。

1.在您的消息之后，点击加号 (+) 按钮，然后点击 Add recommendation。

![界面显示添加消息和添加推荐的选项，展示了WhatsApp自动化的设置步骤。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-153.png?resize=772%2C432&ssl=1)

2.为您的推荐起一个描述性的名称（例如：“巧克力草莓爱好者”）。

3.添加您的消息。

- 示例：“我们也喜欢巧克力和草莓的搭配。试试这些我们最受欢迎的产品吧。”

4.选择您希望此推荐适用的选项组合（例如：同时选择了“草莓”和“巧克力”的人）。

- 您可以为一个推荐选择多个选项组合。

![A screenshot of a WhatsApp automation setup interface, showing fields for internal name, recommendation message, and required responses for a chocolate and strawberry lovers theme.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-154.png?resize=626%2C976&ssl=1)

5.选择 Save。

6.点击 Default recommendation旁边的箭头。

7.为该推荐命名。

8.输入您的默认推荐消息，作为所有推荐的兜底方案（Fallback）。通常，人们会使用畅销产品或新品作为默认选项。

- 示例：“经典搭配！点击此处查看我们的产品：[www.cupcakes123.com/products](https://www.google.com/search?q=https://www.cupcakes123.com/products)”

![用户界面截图，显示添加默认推荐选项的设置，包括内部名称和推荐信息框。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-155.png?resize=638%2C640&ssl=1)


9.点击 Save。

10.为您设置的每种选项组合添加对应的推荐，或者使用默认推荐发送给所有其他的选项组合。

##### 调整您的设置

为您当前的自动化调整任何Session settings。操作步骤如下：

1.点击右上角的齿轮图标。

2.选择 Session settings。

![An interface displaying options to edit settings for session management in a WhatsApp automation tool, with a gear icon and menu options.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-156.png?resize=926%2C338&ssl=1)

3.您可以更新以下设置：

- 频道范围 (Channel Scoping)
- 重新提示回复 (Reprompt response)
- 回退回复 (Fallback response)
- 最大重新提示次数 (Maximum number of reprompts)
- 最大超时时间（以小时为单位） (Maximum timeout)

##### 预览并开启自动化

一旦您对自动化配置感到满意：

1. 点击右上角的“播放”按钮预览自动化 预览效果与实际体验略有不同。它无法识别拼写错误，也不会显示链接缩短。了解更多关于预览自动化的信息。
2. 仔细检查您的触发关键词、消息、选项以及推荐内容。 一旦自动化开启，您必须先将其关闭才能进行编辑。关闭操作会导致当前处于该自动化流程中的所有人立即退出。
3. 点击右上角的 Turn on。

一旦您开启了自动化，它将发送给任何发送了触发关键词的 WhatsApp 订阅者。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)