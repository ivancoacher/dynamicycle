---
id: 6257
title: "如何从 Mailchimp 迁移"
slug: "migratemailchimp"
category: "集成（Integrations）"
category_slug: "integrations"
wp_url: "https://dynamicycle.com/docs/migratemailchimp/"
wp_modified: "2026-01-08T03:01:31"
---

****Klaviyo 会从 Mailchimp 同步以下数据：****

- 订阅者信息（包括取消订阅者和已清理的联系人）
- Mailchimp 受众（Mailchimp Audiences，将同步为 Klaviyo 列表）
- 邮件的接收、点击和打开记录
- Mailchimp 评分（Mailchimp Ratings）

##### 在开始之前

如果您的 Mailchimp 账户当前已与 Shopify 店铺集成，并且您已经[将 Shopify 与 Klaviyo 集成](https://www.klaviyo.com)，请务必在将 Mailchimp 与 Klaviyo 集成之前，****先断开 Mailchimp 与 Shopify 的连接****。未能断开旧集成可能会导致向您现有的订阅者列表重复发送双重加入（Double Opt-in）确认邮件。

##### 迁移清单

从 Mailchimp 迁移到 Klaviyo 需要四个关键步骤：

1. 将您的电商平台与 Klaviyo 集成。
2. 将 Mailchimp 与 Klaviyo 集成。
3. 将您的邮件模板从 Mailchimp 迁移到 Klaviyo。
4. 关停您的 Mailchimp 账户。

##### 如何集成 Mailchimp

将您的 Mailchimp 账户与 Klaviyo 集成会同步您所有的联系人数据，包括联系人接收、打开和点击邮件的时间记录。

首先，您需要获取一个 ****Mailchimp API 密钥****。我们建议专门为 Klaviyo 集成创建一个新密钥，但如果您愿意，也可以使用现有密钥。

1.登录 Mailchimp，点击您的头像图标。

2.导航至 ****Account & billing > Extras > API keys****。

3.点击 ****Create a Key****（创建密钥）。

4.为您的密钥命名，然后点击 ****Generate Key****（生成密钥）。

5.点击 ****Copy Key to Clipboard****（复制密钥到剪贴板），然后妥善保存。

6.****获取 API 密钥后，登录 Klaviyo：****

7.选择 [****Integrations****](https://www.klaviyo.com/integrations)选项。

8.点击 ****Explore apps****并搜索 Mailchimp。

9.点击 Mailchimp 卡片，然后点击 ****Install****。

![Klaviyo与Mailchimp集成的步骤，包含添加Mailchimp API密钥的输入框以及相关设置说明。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-55.png?resize=1024%2C738&ssl=1)

10.在设置页面上，将 Mailchimp API 密钥粘贴到指定字段中。

11.点击 ****Connect to Mailchimp****（连接到 Mailchimp）。

12.粘贴密钥后，点击查看 ****Advanced options****（高级选项）：

- ****Collect open and click data for Mailchimp campaigns（收集 Mailchimp 活动的打开和点击数据）：**** 勾选此项以同步 Mailchimp 的互动数据。
- ****Create Klaviyo lists from Mailchimp audiences（从 Mailchimp 受众创建 Klaviyo 列表）：**** 勾选此项以同步您所有现有的 Mailchimp 受众。
- ****Only sync contacts from specific audiences（仅同步特定受众中的联系人）：**** 勾选此项可以仅同步指定的 Mailchimp 受众。随后系统会提示您选择要同步哪些受众。****注意：**** 您必须先勾选前一个“从 Mailchimp 受众创建 Klaviyo 列表”的选项，此功能才能生效。

![邮件营销平台 Mailchimp 的集成设置界面，展示 API 密钥选项和高级设置，包括收集打开和点击数据的功能。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-56.png?resize=1024%2C593&ssl=1)

13.如果您在高级设置（Advanced）中选择了仅同步特定受众中的联系人（Only sync contacts from specific audiences），您需要指定之前发送过 Campaign 的所有受众 ID（Audience IDs）。即使另一个同步的受众中包含相同的联系人，如果最初的 Campaign 不是发送给该受众的，您将无法看到该 Campaign 完整的互动数据。

14.Klaviyo 仅同步状态为“已发送（Sent）”的 Campaign 数据。状态为“正在发送（Sending）”的 Campaign 数据将不会被同步。请注意，Klaviyo 不会同步整个 Campaign 活动的内容；我们仅同步打开和点击数据。如果您希望在 Klaviyo 中重新创建 Mailchimp 的 Campaign，可以参考下文了解如何导出您的 Mailchimp 邮件模板。

15.在您点击 Connect to Mailchimp 后，数据将在几分钟内开始同步。

##### 同步频率

当您首次集成 Klaviyo 和 Mailchimp 时，我们将同步您所有的联系人以及过去 90 天的 Campaign 数据。这被称为“历史同步”，且仅执行一次。

历史同步完成后，Mailchimp 数据将按以下频率同步至 Klaviyo：

- ****现有受众（Existing audiences）：**** 每 30 分钟同步一次。
- ****新受众和/或新 Campaign：**** 每 6 小时同步一次。
- ****现有 Campaign 活动：**** 在邮件发送后进行同步，以捕获收件人数据。

##### 查看您的 Mailchimp 数据

Klaviyo 会自动从 Mailchimp 同步所有联系人及其订阅信息（除非您选择了“仅同步特定受众中的联系人”）。您可以看到联系人是处于“已订阅”还是“已取消订阅”状态；此外，在 Mailchimp 中被标记为“已清理（Cleaned）”或发生退信（Bounced）的联系人将被添加至 Klaviyo 的Suppression List中。

我们根据联系人在 Mailchimp 中的订阅状态来决定其在 Klaviyo 的订阅情况，除非该 Profile 已存在于 Klaviyo 中。如果 Profile 已存在，我们将根据时间戳使用最新的授权状态（Consent Status）。

- ****关于删除：**** 如果您在集成 Klaviyo 后在 Mailchimp 中删除了某个联系人，该联系人不会在 Klaviyo 中被删除。
- ****关于抑制：**** 如果某个 Profile 在添加 Mailchimp 集成之前已作为活跃 Profile 存在于 Klaviyo 中，但在 Mailchimp 中是被清理/退信的状态，它不会在 Klaviyo 中被自动抑制。要抑制这些联系人，您可以从 Mailchimp 导出为 CSV 文件，然后上传到 Klaviyo 的抑制列表中。

###### ****此外，我们的 Mailchimp 集成还包括：****

- ****同步打开和点击数据：**** 如果您勾选了“收集 Mailchimp 活动的打开和点击数据”设置。
- ****创建列表：**** 如果您勾选了“从 Mailchimp 受众创建 Klaviyo 列表”设置。
- ****同步评分：**** 如果您勾选了“从 Mailchimp 受众创建 Klaviyo 列表”设置，则会同步 Mailchimp 评分。如果您仅同步特定受众，那么即使是这些同步的联系人，其评分也不会同步到 Klaviyo。
- ****同步指标：**** 同步过去 90 天内已完成发送的 Campaign 的以下指标（不包括 A/B 测试中的 Campaign）：
  - Clicked Email（点击邮件）
  - Opened Email（打开邮件）
  - Received Email（收到邮件）

****重要提示：**** 系统仅同步联系人的姓名、邮箱地址、Mailchimp 评分和地理位置。

##### 将 Mailchimp 标签（Tags）导入 Klaviyo

如果您使用 Mailchimp 标签来标记和组织联系人，则需要手动将这些标签导出并导入到 Klaviyo。Klaviyo 内置的 Mailchimp 集成****不会****自动同步您的任何标签。

1. 首先，在 Mailchimp 中导航至 ****Manage contacts > Tags****，查看您想要同步的具体标签。
2. 点击 ****View**** 旁边的下拉菜单，选择 ****Export as CSV****（导出为 CSV），即可从 Mailchimp 导出相应的细分群体。

![Mailchimp 标签管理界面的截图，显示标签排序选项和导出为 CSV 的下拉菜单。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-57.png?resize=1024%2C294&ssl=1)

一旦您从 Mailchimp 导出了数据，就可以将其作为Custom properties导入 Klaviyo。自定义属性会附加在您的 Klaviyo Profile 上，您可以根据特定属性创建Segments，或者利用它们为Flows添加筛选条件，以及在邮件中动态显示数据。

##### 将您的邮件模板从 Mailchimp 迁移到 Klaviyo

Klaviyo 拥有直观的拖拽式模板编辑器，您可以用来重新制作您的 Mailchimp 模板。我们****推荐****使用这种方法构建模板，因为它可以确保模板在移动端经过优化、具备响应式布局，并且在未来易于编辑和迭代。

但是，如果您没有时间专门使用 Klaviyo 的模板编辑器重新制作模板，也可以从 Mailchimp 导出邮件模板并将其导入 Klaviyo。

###### 从 Mailchimp 导出模板

1.在您的 Mailchimp 账户中，导航到您想要迁移到 Klaviyo 的模板。

2.在模板名称旁边的下拉菜单中，选择 ****Export as HTML****（导出为 HTML）。

![Mailchimp 模板导出选项界面，包含模板列表及导出为 HTML 的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-58.png?resize=1024%2C456&ssl=1)

3.系统会提示您确认导出，随后一个 HTML 文件将保存到您的电脑中。

##### 更换模板标签

Klaviyo 和 Mailchimp 使用不同的模板标签来在邮件中插入动态内容。例如，“名（First Name）”标签在 Mailchimp 和 Klaviyo 中是不一样的，因此务必将任何 Mailchimp 特有的标签替换为对应的 Klaviyo 标签。

****最重要的替换项是“取消订阅（Unsubscribe）”标签。****

- 在将模板导入 Klaviyo 之前，您必须添加一个 `{% unsubscribe %}` 标签。这是因为 Klaviyo 不允许上传不包含取消订阅标签的 HTML 模板（除非该模板被标记为交易类邮件）。
- 要编辑模板中的标签，请使用文本编辑器（如 Sublime Text）打开该 HTML 文件。下表列出了常用的 Mailchimp 标签及其对应的 Klaviyo 标签。

![An image displaying a comparison chart of Mailchimp and Klaviyo template tags, highlighting the differences in syntax for common tags such as unsubscribe, first name, last name, and email.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-59.png?resize=1024%2C694&ssl=1)

在您将标签更换为 Klaviyo 标签后，即可保存您的 HTML 文件。

##### 将模板导入 Klaviyo

1.在您的 Klaviyo 账户中，点击 [****Content****下](https://www.klaviyo.com/templates/list)拉菜单，选择 [****Templates****](https://www.klaviyo.com/templates/list)选项卡。

![Klaviyo 用户界面的一部分，显示导航栏，其中突出显示了 'Content' 选项，包含多个子选项，如 Templates。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-60.png?resize=342%2C936&ssl=1)

2.点击 ****Import Template****。

3.在弹出的\*\*导入模板弹窗（Import template modal）\*\*中，选择您刚才保存在电脑上的 HTML 文件进行上传。

![Klaviyo导入模板界面，包含文件上传选项、模板名称输入框和HTML文件选择区域。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-61.png?resize=920%2C684&ssl=1)

4.您可以在Preview选项中查看邮件模板的外观效果。

5.请注意，从现在起，您必须直接编辑 HTML 代码才能对该模板进行任何更改。

##### 关停您的 Mailchimp 账户

如果您在移除集成之前开始在 Mailchimp 中删除或清理联系人，这些联系人在 Klaviyo 中也会被设为“已抑制”。当您的 Mailchimp 账户安全关停后，在删除或清理那些您不希望在 Klaviyo 中被抑制的联系人之前，请务必先移除集成。即使您禁用或移除 Mailchimp 集成，从 Mailchimp 同步到 Klaviyo 的受众和 Profile 也****不会****被删除。

将所有数据迁移至 Klaviyo 后，您需要执行以下三个关键步骤来确保可以彻底停用 Mailchimp 账户：

1. 确保您的注册****弹窗****和列表增长工具指向 Klaviyo，而非 Mailchimp。
2. 在 Klaviyo 中将您的自动化（Automations）重新创建为流程（Flows）。
3. 移除 Mailchimp 集成。

##### 注册弹窗与列表增长工具

如果您在 Mailchimp 账户中有任何注册****弹窗****或注册表单营销活动，您需要确保在 Klaviyo 中重新创建它们，以便您的列表在 Klaviyo（而非 Mailchimp）中持续增长。您无法将 Mailchimp 创建的****弹窗****重定向到 Klaviyo。相反，您可以：

- 使用 Klaviyo 的注册****弹窗****构建器从头开始重新创建您的****弹窗****。
- 使用与 Klaviyo 集成的第三方列表增长工具。
- 通过您的电子商务平台集成您的自定义表单。

如果您使用的是第三方列表增长工具而非 Mailchimp 内置的表单构建器，请确保该工具能够同步到 Klaviyo。Klaviyo 与许多第三方列表增长工具都有集成。您可以浏览我们的集成列表来查找您正在使用的工具。如果未在列表中看到它，请考虑使用 Klaviyo 的****注册弹窗构建器****来创建您的****弹窗****，或更换为其他第三方工具。

****请注意：**** 所有 Klaviyo 列表默认均为“双重加入（Double Opt-in）”。

如果您使用的是自定义代码表单，可以确保这些联系人同步到 Klaviyo。为此，请确保您的自定义表单将新订阅者直接同步到您的电商平台，并且该平台已与您的 Klaviyo 账户集成。

在将所有注册****弹窗****切换为指向 Klaviyo 后，请等待几天并观察 Mailchimp 中的受众。如果您发现仍有订阅者被添加到这些受众中，说明可能至少还有一个****弹窗****尚未更换。

##### 邮件自动化 (Email Automations)

Klaviyo 将邮件自动化称为 ****Flows****，它支持更高级、更具针对性的序列。在 Klaviyo 中重新创建这些流程非常重要，这样您就无需继续使用 Mailchimp 来发送触发式邮件了。

一旦您的 Klaviyo 流程上线，请务必关闭 Mailchimp 中所有的自动化设置，以确保不会向用户重复发送邮件。

****操作步骤如下：****

1. 在 Mailchimp 中，点击特定 Campaign 旁的 ****Pause and Edit****（暂停并编辑）。
2. 在弹出的Pop-up中，点击 ****Pause****（暂停）。

![A screenshot showing an email campaign status in a marketing platform, indicating a scheduled email campaign for the Math Department with options to 'Pause and Edit'.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-62.png?resize=620%2C91&ssl=1)

##### 移除 Mailchimp 集成

在您将所有的列表增长工具都指向 Klaviyo 账户、暂停了 Mailchimp 自动化，并正式上线了 Klaviyo Flows之后，您就可以移除 Mailchimp 集成了。在移除之前，请务必再次检查一切是否运行正常。您可以使用测试邮箱在注册****弹窗****及其他增长工具中进行订阅，尝试“放弃购物车”，或订阅您的Newsletter以触发“欢迎系列”Flow。

1. 点击 Klaviyo 账户中的 ****Audience**** 下拉菜单，选择 [****Profiles****](https://www.klaviyo.com/people) 选项卡，确保 Profile 中的信息准确反映了所有的沟通记录。
2. 如果您订阅的列表是“双重加入（Double Opt-in）”，请务必先去邮箱点击确认。

****一旦完成这些步骤并确认完全迁移到 Klaviyo，您就可以移除集成：****

1. 选择 ****[Integrations](https://www.klaviyo.com/integrations)****选项。
2. 点击 Mailchimp 集成右侧的操作按钮。
3. 选择 ****Remove integration****（移除集成）以彻底移除。

![Klaviyo集成界面，显示Mailchimp和Shopify的链接状态，提供禁用和移除集成选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-63.png?resize=1024%2C257&ssl=1)

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)