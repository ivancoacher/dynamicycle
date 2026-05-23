---
id: 6833
title: "如何使用 Smart Translations 创建多语言 Email Campaign"
slug: "smarttranslations"
category: "活动与营销（Campaigns）"
category_slug: "campaigns"
wp_url: "https://dynamicycle.com/docs/smarttranslations/"
wp_modified: "2026-02-24T01:45:02"
---

了解如何根据 Audience 的语言偏好，创建并发送多种语言的 Email Campaign。Klaviyo 支持将 Campaign 内容翻译成 60 多种语言。

如果您已经拥有或计划扩展国际客户群，实现 Campaign 本地化将大有裨益。使用每位订阅者首选的语言发送邮件，能助您触达更广泛的 Audience，从而提升整体的 Engagement（参与度）。

这一部分是核心操作指南，我进行了排版优化，确保步骤清晰且口吻专业：

##### 翻译 Campaign

在开始翻译之前，请确保您的邮件内容已在原始语言状态下完成最终润色并准备就绪。否则，如果您后续对原始内容进行了修改，则需要重新执行一遍翻译流程。

1. 创建 Campaign 或编辑现有的 Campaign 草稿。
2. 在 Campaign 向导的 Recipients（收件人）步骤中，确保为您的 Campaign Audience 添加了已知具有多种语言偏好的列表或 Segment（分众）。
3. 如果您尚未添加邮件模板，请为您的 Campaign 添加一个。
4. 在 Message（消息）步骤，点击 Edit（编辑）进入模板编辑器。
5. 点击右上角的 Translate（翻译）。
6. 选择编写内容时所使用的原始语言（Original language）。
7. 勾选各个语言对应的复选框，选择您想要将 Campaign 翻译成的语种。系统会根据该 Campaign Audience 的首选语言为您提供“推荐语言”。此栏目也会包含您在翻译设置中预设的任何语言。
8. 如有需要，点击 Additional languages（更多语言）下方的下拉菜单，查看并选择推荐列表之外的语言。
9. 根据需要，选择一个 Fallback language（回退语言），以便在无法获取客户的首选语言时使用。此语言可以与原始语言不同。

![语言选择界面，显示原始语言为德语，以及推荐的英语和法语选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-15.png?resize=700%2C515&ssl=1)

10.点击 Translate。

11.在接下来的步骤中，预览所有将被翻译的邮件元素。如有需要，您可以手动编辑其中任何一项。您还可以点击所列图片旁边的编辑按钮，将其更换为适合目标语言的图片。

![展示三瓶葡萄酒的图片，背景为木制酒桶。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-16.png?resize=900%2C563&ssl=1)

12.点击所列 Text Block 旁边的编辑按钮，即可查看并编辑完整的文本内容。

![展示2020年玫瑰酒的界面，包含精选好酒汁和部分在选定酒桶中熟成的信息。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-17.png?resize=900%2C563&ssl=1)

13.如果您选择了多种目标语言，点击顶部的箭头或使用下拉菜单在不同语言之间进行切换。

14.如果您想添加更多语言或移除当前选择的语言，请点击该语言的名称。

15.完成后点击SAVE

![界面显示了一个酒类产品发布页面，包括选择语言的下拉菜单和酒桶的图片，右侧介绍了2020年玫瑰酒的相关信息。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-18.png?resize=900%2C563&ssl=1)

##### 产品内容区域化 (Regionalizing)

实现产品内容的区域化，可以让您的客户看到与其偏好相匹配的产品信息、币种以及价格。

###### 动态产品 Block (Dynamic Product Blocks)

1. 产品内容的区域化功能适用于已启用 Shopify Markets 的 Shopify 集成。
2. 在 Smart Translations 中使用的 Dynamic Product Blocks，会自动根据客户的语言和国家/地区，匹配相应的产品信息、币种及价格。当某款产品在特定国家/地区不销售时，系统将不会向该地区的客户推荐该产品。
3. 在 Smart Translations 编辑器中，请选择一个 Fallback catalog locale（回退目录区域设置）。当无法识别客户所属国家/地区时，系统将使用此设置。您可以在账户设置中为每种语言配置默认的 Fallback catalog locale。
4. 如果您选择了多种翻译语言，点击顶部的箭头或使用下拉菜单即可在不同语言之间切换。

![编辑界面显示产品块设置，包括语言和购买按钮文本](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-19.png?resize=1024%2C169&ssl=1)

###### 静态产品 Block (Static Product Blocks)

1. 在 Smart Translations 中使用的 Static Product Blocks，可以根据 Feed（数据源）的内容，按照“翻译 Campaign”部分的指令为每种语言进行手动配置。

![展示几瓶玫瑰色的葡萄酒，背景为绿色植物，界面中包含关于酒庄的信息和菜单选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-20.png?resize=800%2C496&ssl=1)

为了纠正可能出现的翻译错误：

- 点击警告信息旁边的 Review translations（检查翻译）。
- 点击 Update translation，即可更新所有以黄色高亮显示的、未同步的 Block。

![显示内容更新提示的界面，包含图像和文本元素。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-21.png?resize=700%2C504&ssl=1)

若要单独编辑某个元素，请点击铅笔图标，并从以下选项中进行选择：

- Re-translate（重新翻译）：翻译任何已更改的文本。
- Match source（匹配源内容）：使图片或 URL 与原始源内容保持一致。
- Edit（编辑）：手动修改该元素。
- Ignore（忽略）：保持元素现状，不作更改。

##### 克隆消息与 A/B 测试的翻译

- 如果您克隆一个带有翻译的 Campaign，新生成的 Campaign 会保留原件中的所有翻译，您可以根据需要自由编辑。
- 当您创建 A/B 测试时，新的 Variation将保留原始邮件中的翻译内容。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)