---
id: 5159
title: "Campaign 设置 A/B Test实操"
slug: "campaign-a-b-test"
category: "活动与营销（Campaigns）"
category_slug: "campaigns"
wp_url: "https://dynamicycle.com/docs/campaign-a-b-test/"
wp_modified: "2025-12-16T07:28:31"
---

了解如何为 Campaign 设置并运行 A/B Test，如何解读测试结果，以及 A/B Testing Campaigns 的一些用例。Klaviyo 的 Campaign A/B Testing 功能允许您轻松测试不同的 Subject Lines、Message Content 和 Send Times，以便您更好地了解什么对您的受众最有效。

##### 为 Campaign 邮件创建 A/B Test

1.导航至 Campaigns > Create campaign。
2.在侧边栏中，为 Campaign 命名。
3.选择 Email，然后点击 Continue。
4.选择您想要发送的 lists 或 segments。
5.点击 Next。
6.输入 subject line，如需要，可编辑 preview text、sender name 和 sender email address。
7.创建您的第一个邮件版本，添加文案、图片和链接。
8.在 subject line 字段上方，点击 Create A/B test。
此操作将自动创建您的第二个完全相同的版本，并进入 Campaign A/B test 页面。

![An email message setup interface displaying fields for subject line, preview text, sender name, and sender email for creating an A/B test.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-47.png?resize=1000%2C658&ssl=1)

9.在每个版本 name 字段中，添加一个描述性的 variation 名称，用以说明正在进行 A/B testing 的内容，例如：“Summer launch email – white buttons.”

![A/B test setup interface for email campaigns, showing options to test content and send times, with a highlighted variation name field labeled 'Summer launch email - white buttons'.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-48.png?resize=1024%2C370&ssl=1)

##### 配置Test Variations

决定要测试 Campaign 中的哪些元素的表现，以便构建不同的 Campaign 版本。

##### 测试内容

您可以测试消息内容，以确定您的受众希望看到什么。点击页面顶部的 Test Content。

为您的 A/B 测试编辑其中一个版本。一次A/B 测试只比较一个因素，这一点很重要，因此如果您编辑了标题，就不要更改任何其他内容。如果需要，您可以通过点击特定版本卡片上的 Clone 按钮来添加更多版本，但我们建议只使用 2 个版本。

##### 测试发送时间

您也可以测试发送时间，以确定您的受众希望在何时收到您的消息。点击页面顶部的 Test Send Times。
测试发送时间时，请确保两个版本的内容和标题完全相同，
建议在晚上发送。或者可以使用Smart Send Time。

##### 选择测试策略

如果账户符合条件，从以下选项中决定测试策略：

- 获胜版本（标准 A/B 测试）
- 为每位收件人提供个性化版本

![Klaviyo A/B测试设置界面，显示两个发送策略选项：获胜变体和为每位收件人提供个性化变体。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-49.png?resize=600%2C272&ssl=1)

##### 获胜版本与个性化版本的区别

两种测试策略选项都会将不同版本发送给由活动总收件人一定百分比组成的测试组，并根据您选择的指标（例如，打开率）来测试消息的成功度。然而，在测试期结束后，每种策略向其余收件人发送消息的方式存在一些关键差异：

- 获胜版本 – A/B 测试的默认选项，它将确定 1 个获胜版本，并在测试期结束后将其发送给活动的其余收件人。
- 个性化版本 – 使用 AI 在与每个版本互动的测试收件人中搜索模式。测试期结束后，Klaviyo 将预测哪个版本对每位收件人的效果更好，并向其余收件人发送他们偏好的版本。

##### 为每位收件人提供个性化版本

如果您想根据每位收件人的具体情况来个性化他们收到的版本，请选择“为每位收件人提供个性化版本”。

Klaviyo 将使用每个档案的信息来确定哪个版本最有可能成功转化该档案。此档案信息包括但不限于：

- 历史互动率
- 客户生命周期价值 (CLV)
- 地理位置

例如，如果您已选择打开率作为获胜指标，并且测试组中 CLV 为 100 或以上的档案更频繁地打开版本 A，而 CLV 低于 100 的档案更频繁地打开版本 B，那么活动的其余收件人将根据其 CLV 收到他们最有可能打开的版本对应的邮件。这是一个简化的示例，因为 Klaviyo 将使用许多数据点来确定个性化版本。

##### 配置 A/B 测试设置

创建内容后，请决定您测试池的大小和测试期的长度。

首先，选择获胜指标，即您希望看到改善的主要指标。可从以下选项中选择：

- 打开率

在测试标题、Preview Text或发件人姓名和电子邮件地址时推荐使用。

- 点击率

在测试邮件内容（如按钮大小或颜色）时推荐使用。

- 下单率

仅适用于拥有“已下单”指标的用户，并且不适用于个性化版本。在测试邮件内容（例如，展示畅销品还是新品能带来更多转化）时推荐使用。

![Klaviyo A/B test内容设置，显示获胜指标和规模分配选项的界面。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-50.png?resize=1024%2C422&ssl=1)

我们会根据您的列表大小推荐测试规模，并根据 A/B 测试指标（即打开、点击或下单）推荐测试时长。如果需要，您可以使用滑块栏更改测试规模。如果测试规模小于 100%，您还可以调整测试时长。

在下面的示例中，20% 的活动收件人将收到版本 A，另外 20% 将收到版本 B。根据这些收件人中打开、点击或下单的人数（取决于您选择的获胜指标），系统将在 6 小时后选出获胜版本，其余的收件人将收到该获胜版本。

![A graphical depiction of A/B test settings for an email campaign, including test size distribution and winning variation metrics.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-51.png?resize=1024%2C328&ssl=1)

##### 调整测试设置后，点击 Continue 进行审核。

如果您正在进行内容 A/B 测试，并希望根据每位收件人的时区发送消息：请将您的测试规模设置为 100%然后，在安排Campaigns时，您将可以选择“Recipient’s Local Timezone”作为您发送的时区。

##### 审核 A/B 测试结果并选择获胜者

导航至您正在测试的活动，以查看其进度并了解哪个版本的表现更佳。如果活动仍在发送中，而您希望结束正在进行的 A/B 测试：

- 导航至正在进行的活动中的“A/B 测试结果”选项。
- 点击您想选择的版本旁边的更多选项菜单。
- 点击“选为获胜者”。

当您手动选择一个获胜者时，任何尚未收到该活动的人都将立即收到获胜版本。如果您的 A/B 测试规模是 100% 的收件人，我们将在整个消息的转化窗口内持续收集数据，因此随着新数据的涌入，获胜者可能会发生变化