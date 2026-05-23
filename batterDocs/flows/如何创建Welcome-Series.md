---
id: 6111
title: "如何创建Welcome Series"
slug: "welcome"
category: "自动化与生命周期（Flows）"
category_slug: "flows"
wp_url: "https://dynamicycle.com/docs/welcome/"
wp_modified: "2026-01-05T07:48:25"
---

您的邮件Welcome Series flow应当与 SMS Welcome Series flow分开，因为订阅者可能会在不同时间分别订阅邮件和短信，且每个订阅者只能进入一次特定的欢迎流程。此外，为了使用虚拟名片（Virtual Contact Cards）和短信专用优惠券等功能，我们也建议您创建一个专门的 SMS 欢迎系列。

Welcome Series 是一项至关重要的自动化功能，因此 Klaviyo 提供了一个开箱即用的预设 Welcome Series。您可以在账户的 [Flows](https://www.klaviyo.com/flows) 标签页中找到 Welcome Series flow 的示例。如果您需要更高级的 Welcome flow，也可以在我们的 [flow](https://www.klaviyo.com/flows/create) 库中浏览不同的创意。

##### 了解联系人是如何被添加到List中的

在设置 Welcome Series 之前，您必须将其连接到您选择的List。创建账户后，您的 List & segments 标签页中会预先生成一个名为 Email List 的空列表。您可以将此列表用于您的 Welcome Series flow，或者创建一个新列表。

无论您选择哪个列表，都应该是新订阅者在注册时被添加到的那个列表。新联系人可以通过以下四种主要方式被添加到列表中，从而触发 Welcome Series：

- 通过填写弹窗注册
- 通过订阅页面注册
- 通过手动添加到列表
- 通过 Lists API 或 Subscribe API

****如果您正在导入列表，请暂停您的 Welcome Series****

如果您已经将 Welcome Series 设置为 Live 状态并想要导入列表，您必须先将该系列设置为 Manual。否则，每个被导入的人都会被安排发送该系列的第一条消息，即使他们是几个月前订阅的。

请按照以下步骤进行导入：

1. 打开与您的主列表关联的 Welcome Series flow。
2. 在 flow 构建器的右上角，点击 Update Action Statuses。
3. 在下拉菜单中选择 Manual。
4. 点击 Update Statuses。
5. 按照我们的指南了解如何将联系人导入列表。
6. 重复步骤 1-2，然后将您的 flow 重新设置回 Live。

****导入完成后，您可以手动向导入的旧联系人发送欢迎消息：****

- 打开您的 Welcome flow 。
- 点击第一条消息。

![Klaviyo Welcome Series flow interface showing email details and actions for a marketing automation setup.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-15.png?resize=1024%2C568&ssl=1)

- 在侧边栏的 Performance 部分，点击 View details。
- 进入 Recipient Activity 标签页。
- 点击 Needs Review。

![Email recipient activity dashboard showing 'Needs review' section and conversion metrics.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-16.png?resize=1024%2C532&ssl=1)

- 对于任何您想发送欢迎邮件的导入联系人，点击 Needs Review 列表中邮件旁边的 Send。
- 或者，您可以点击 Cancel All 以防止这些联系人收到该消息。
- 对 flow 中的任何其他消息重复此步骤。

****您可能需要确保通过电商集成订阅的联系人已被添加到正确的列表中。****

例如，许多 Shopify 主题在页脚都有一个默认的通讯注册弹窗。虽然这不属于 Klaviyo 弹窗，但使用此表单注册的联系人仍然可以被添加到 Klaviyo 的列表中。

要验证通过集成订阅的联系人是否被添加到列表中，以及他们被添加到了哪个列表，请按照以下步骤操作：

- 在 Klaviyo 主导航栏的左下角，点击您的账户名称。
- 点击 [Integrations](https://www.klaviyo.com/integrations)。
- 点击您的电商集成的名称。
- 在集成设置中，如果您的集成能够将联系人同步到特定列表，请确保选择与您的 Welcome Series 所使用的相同的列表。请参阅以下 Shopify 示例：

![Screenshot showing the option to sync Shopify email subscribers to Klaviyo, with a dropdown menu to select a list.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-17.png?resize=1024%2C457&ssl=1)

- 此外，如果您有任何正在运行的 Klaviyo 弹窗，请确保这些弹窗也指向同一个列表。

###### 了解双重确认与单一确认 list

默认情况下，Klaviyo 中的每个 list 都是双重确认（double opt-in）。这是为了保护您的邮件送达率，并确保添加到您的 list 中的联系人拥有有效的电子邮件地址或电话号码。我们建议您的主 list 保留此设置。

双重确认 list 的工作流程如下：

1. 联系人注册。
2. 联系人收到确认短信或邮件。
3. 一旦他们确认订阅，就会被引导至确认订阅页面。
4. 联系人被添加到 list。
5. 联系人触发 Welcome Series。
6. 如果第一条欢迎消息设置为立即发送，他们将收到该消息。

##### 使用 Klaviyo 的标准 welcome flow

当您创建 Klaviyo 账户时，可以轻松地在账户中添加一个预设的名为“Welcome Series”的 welcome flow。

要设置此 flow：

1.导航至 Klaviyo 账户中的 [Flows](https://www.klaviyo.com/flows) 标签。

2.在 Welcome Series 的卡片上，点击 Get Started。

![A graphic displaying the 'Welcome Series' feature, introducing subscribers through a three-email series, with a flag icon and text highlighting its benefits and potential revenue generation for Klaviyo users.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-18.png?resize=524%2C658&ssl=1)

如果您账户中没有任何 flow，当您查看 Flows 标签页时，这将是左侧的第一张卡片。如果您账户中已经有了 flow，您可以在 flow 列表下方查看预设 flow 的不同卡片。

![Klaviyo界面中显示的Flows选项卡，主页左侧有导航菜单，顶部有创建流程的按钮。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-19.png?resize=1024%2C572&ssl=1)

3.在 Welcome Series Setup 弹窗中，选择您希望 Welcome Series 关联的 list。这应该是新联系人在注册订阅您的品牌消息后被添加到的主 list。

![欢迎系列设置界面，包含三个电子邮件的自动化流程，用于欢迎新订阅者并促进转化。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-21.png?resize=1024%2C1005&ssl=1)

4.点击Use template

在将预设 Welcome Series 中的邮件设置为 Live 状态之前，请使用您自己的内容和品牌形象对邮件模板进行个性化定制。

1.在 flow 构建器中点击一条消息。

2.在详情面板中，根据需要编辑邮件subject line和发件人信息（sender details）。

![Klaviyo Welcome Series flow interface displaying email actions, subject line, and sender details.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-22.png?resize=1024%2C567&ssl=1)

3.在 Template 部分，点击 Edit 来编辑邮件模板。

4.使用邮件模板编辑器修改消息内容，使其符合您的品牌形象。

![Klaviyo welcome series flow setup interface with email actions and editing options displayed.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-23.png?resize=1024%2C568&ssl=1)

5.对 flow 中的其他消息重复上述步骤。

Welcome Series flow 是在有人订阅您的 email list 后介绍自己的绝佳方式。上面提到的 Welcome Series 包含三封邮件：

- 邮件 #1，立即发送 向新订阅者介绍您的品牌并收集他们的邮件偏好。若要在用户确认订阅后立即发送邮件，请在 flow 触发器后直接添加邮件，不要设置时间延迟。
- 邮件 #2，3天后 在用户注册三天后，鼓励订阅者在社交媒体上关注您。
- 邮件 #3，4天后 在用户注册四天后，展示您的畅销产品。

您可以根据具体的应用场景自定义或更改其中任何邮件的目标。您还可以向此 flow 中添加更多内容，例如分支（splits）和 SMS 消息。

##### 创建进阶 Welcome Series flow

如果您想要一个更高级的Welcome Series flow：

1.导航至 [Flows](https://www.klaviyo.com/flows) 标签页。

2.点击右上角的 Create Flow 以查看 flow 库。

3.在搜索栏中输入 “welcome series”，即可查看预设 Welcome Series flow 的不同版本。

![A screenshot of the Klaviyo 'Create Flow' interface, displaying various Welcome Series templates for nurturing subscribers, including options for SMS and email campaigns.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-24.png?resize=1024%2C623&ssl=1)

##### 从头开始构建 welcome flow

您也可以按照以下步骤构建自己的 Welcome Series：

1.导航至 [Flows](https://www.klaviyo.com/flows) 标签页。

2.点击右上角的 Create Flow。

![A user interface display showing various automated flow options in a marketing platform, including 'Welcome Series', 'Customer Thank You', and 'Post-Purchase Followup'. A prominent button labeled 'Build your own' is highlighted in the upper right corner.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-25.png?resize=1024%2C625&ssl=1)

3.点击右上角的 Build your own。

4.为您的 flow 命名。

![界面显示一个创建流程的窗口，包含输入框用于命名流程和选择标签，同时提供两种创建流程的选项：使用人工智能创建或手动创建。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-26.png?resize=517%2C1024&ssl=1)

5.点击 Create Flow。

6.在 flow 构建器中，从 Recommended 或 All triggers 标签页中选择 Added to list。

7.选择您的 list。

8.点击 Done。

9.将 email 动作拖入您的 flow 中。

![Klaviyo的流构建器界面，显示触发条件为‘当某人被添加到Email List时’，并包含一封待设置的电子邮件。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-27.png?resize=1024%2C569&ssl=1)

10.点击该消息并点击 Configure Content 开始编辑。

11.完成符合品牌风格的消息编辑后，根据需要拖入 time delay（时间延迟）和额外的消息。

每个 flow 都需要一个触发事件（trigger event），并支持可选的 flow 过滤器（flow filters），用于对谁能接收 flow 邮件添加额外限制。

请注意，一个人只能接收一次由 list 触发的 flow 中的消息。这意味着如果某人订阅后完成了您的欢迎流程，随后退订，即使他们之后重新订阅，也不会再次收到这些消息。

##### 如何安排 Welcome Series 的时间以及包含多少封邮件

在构建 Welcome Series 时，您可能会想知道应该包含多少封邮件，以及邮件之间应配置多长时间。对于标准的 Welcome Series，我们建议在一周内发送 3 封邮件，并采用我们预设 flow 中的以下节奏：

- 邮件 #1，立即发送
- 邮件 #2，3 天后
- 邮件 #3，4 天后

##### Welcome Series 中应包含的内容

Welcome Series 是新订阅者与您品牌的首次互动，因此展示出您最好的一面非常重要。Welcome Series 可以有几种不同类型的目标。在为 Welcome Series flow 创作内容时，请始终牢记您的目标。

以下是一些示例：

- 分享品牌故事和使命 您可以创建一个以故事为核心的 Welcome Series，旨在向新订阅者介绍品牌的使命，而不是急于推销首笔交易。在这种情况下，最佳实践是建立一个较长的 Welcome Series，由品牌创始人分享个人轶事，讨论他们为什么要创立公司以及您想要实现的目标。
- 提供促销和优惠券 如果您在注册弹窗中提供了奖励，请务必将其包含在 Welcome Series 的第一封邮件中。
- 推销您的内容 如果 Welcome Series 的主要目标是将订阅者转化为客户，请展示最引人注目的产品。使用产品模块（product blocks）来展示趋势产品或畅销产品，以最大限度地增加用户看到心仪商品并使用折扣进行首次购买的机会。
- 推广社交媒体 您可以利用 Welcome Series 推广品牌的社交媒体渠道，以建立客户关系并提升品牌知名度。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)