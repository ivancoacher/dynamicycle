---
id: 6298
title: "Google Ads 入门"
slug: "googleads"
category: "集成（Integrations）"
category_slug: "integrations"
wp_url: "https://dynamicycle.com/docs/googleads/"
wp_modified: "2026-01-08T06:38:30"
---

了解如何将 Google Ads 与 Klaviyo 集成。此集成允许您自动执行以下操作：

- 将 Klaviyo 的List或Segment连接到Google Audience。
- 将 Profile 从 Klaviyo 同步到 Google。
- 借助 Klaviyo 更轻松地推动您的 Google Ads 策略。集成后，您将能够基于购买数据等标准进行现有客户的再营销、优化投放目标，并在广告活动中排除特定 Profile。

##### 如何集成 Google Ads

1.登录您的 Klaviyo 账户。

2.选择 ****[Integrations](https://www.klaviyo.com/integrations)****选项。

3.点击 ****Explore apps****。

4.搜索 ****Google Ads**** 并点击相应卡片，然后点击 ****Install****（安装）。

5.点击 ****Connect to Google****（连接到 Google）。

![A user interface displaying steps to integrate Google Ads with Klaviyo, featuring a 'Connect to Google' button and instructions for authorizing access and configuring settings.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-64.png?resize=1024%2C646&ssl=1)

6.登录您的 Google 账号。请注意，您登录的 Google 账号必须拥有您想要连接的 Google Ads 账号的****直接管理员权限****。不支持通过经理账号/MCC（我的客户中心）账号进行访问。

7.同意相关权限请求，并点击 ****Allow****（允许），随后您将返回到 Klaviyo 界面。

![Google帐户登录确认页面，显示用户允许Klaviyo管理其AdWords广告系列的权限。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-65.png?resize=885%2C1024&ssl=1)

8.从下拉菜单中选择您想要集成的 Google Ads 账户。如果在下拉菜单中没有看到正确的账户，请确认您是否拥有该账户的管理员权限，然后重试。

![Klaviyo与Google Ads集成的设置页面，显示用户需要选择的Google Ads账户、市场区域选项以及连接Klaviyo列表或细分的选择框。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-66.png?resize=1024%2C698&ssl=1)

9.选择您的营销对象是否包含****欧洲经济区****（EEA，目前包括欧盟国家以及冰岛、列支敦士登和挪威）或****英国****（UK）的用户。

10.如果您的营销对象包含 EEA 或英国用户，为了遵守《数字市场法案》（DMA），您必须同意仅将那些****已授权广告投放许可****的受众发送给 Google。

11.在 ****Connections****（连接）部分，选择一个 Klaviyo List或Segment来与 Google Audience 建立关联。

12.如果您需要在 Klaviyo 中创建一个List：

- 导航至 ****Audience**** 下的 ****[Lists & Segments](https://www.klaviyo.com/lists)**** 选项卡。
- 点击 ****Create List/Segment****。
- 为列表命名并分配相关标签。
- 点击 ****Create List****（创建列表）。

13.选择一个 Google 受众来与您的列表或细分进行连接。如果您需要创建一个新的 Google 受众，请在搜索框中输入新名称，然后点击 ****+ Create audience: [Audience Name]****。

![界面展示了创建Google Ads再营销受众的下拉菜单，用户可以选择现有受众或创建新受众。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-67.png?resize=628%2C400&ssl=1)

14.如果您想添加更多连接，请点击 Add Connection。请注意，您可以随时返回此设置页面来添加更多连接。此外，这是一种 1:1 的同步机制：您不能为多个 Klaviyo 列表或细分选择同一个 Google 受众，也不能将同一个 Klaviyo 列表或细分连接到多个 Google 受众。

15.一旦完成连接添加，点击 Complete setup。

16.随后会出现一条成功消息，告知您 Google Ads 账户现已成功连接到 Klaviyo。

![A notification indicating that the Google Ads account is now connected to Klaviyo, with information about syncing times and settings.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-68.png?resize=1024%2C552&ssl=1)

17.集成完成后，您的收件箱会收到一封来`google.integrations@klaviyo.com` 的 Google Ads 经理账号关联请求，Accept该请求。

##### 集成运作原理

在将 Klaviyo 的 List 或 Segment 连接到 Google Audiences 时，您可以：

- 创建 1:1 同步： 在一个 Klaviyo List 或 Segment 与一个 Google Audience 之间建立同步。请注意，您不能为多个 Klaviyo List 或 Segment 选择同一个 Google Audience，也不能将同一个 Klaviyo List 或 Segment 连接到多个 Google Audiences。
- 直接创建受众： 在 Klaviyo 内部直接创建新的 Google Audience，以便连接新的 List 或 Segment。

##### 通过 Lists & Segments 选项管理您的广告集成

您可以直接在 Klaviyo 的 ****Lists & Segments**** 选项卡中创建或更新 Google 受众同步（以及任何其他广告平台的同步）。

****操作步骤如下：****

1.在 Klaviyo 中，点击左侧导航栏中的 [Lists & Segments](https://www.klaviyo.com/lists)。

2.对于已连接到广告集成受众的每个 List 或 Segment，您将在 [Integrations](https://www.klaviyo.com/integrations)列中看到相应的广告平台图标。

3.若要查看特定 List 或 Segment 的更多详细信息，请点击右侧的三个点图标，并选择 Linked integrations。

![Klaviyo 列表和细分管理界面，展示不同的列表和细分信息，包括名称、类型、成员数量和创建日期。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-69.png?resize=1024%2C629&ssl=1)

4.您将被引导至该 List 或 Segment 的 Settings选项卡下的 Integrations 栏目。

![Klaviyo的新闻通讯列表设置界面，显示集成功能选项，包括Facebook和Google广告的受众同步设置。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-70.png?resize=1024%2C483&ssl=1)

5.在此页面，您可以执行以下操作：

- 连接新的广告集成： 关联其他广告平台。
- 激活或取消激活同步： 开启或关闭该 List 或 Segment 的同步状态。
- 添加新的同步： 为该 List 或 Segment 添加新的同步任务，并选择对应的 Google 受众。

6.完成任何更改后，请点击 Save。

##### 集成使用场景

您可以利用此集成，通过多种方式结合 Google Ads 推动您的营销策略。我们将这些使用场景归纳为 4 个主要类别：

- 对现有 Profile 进行再营销 (Retargeting)： 针对已有的客户信息进行再次精准触达。
- 在未来的广告活动中排除特定 Segment： 避免向不相关的群体展示广告，从而节省预算。
- 利用现有 Segment 优化投放目标： 基于已有的高质量数据来寻找类似的新客户。
- 观察并监控特定受众的表现： 跟踪特定群体在广告活动中的实际转化效果。

##### 对现有 Profile 进行再营销

您可以将用于精准邮件和短信营销的同套细分逻辑，直接应用于定向广告。请参考以下 Segment 建议：

- ****Cart abandoners****：针对过去 7 天内开始结账但未下单的客户。投放的广告内容应与您在“放弃购物车流程 (Flow)”中提供的消息或折扣保持一致。
- ****Winback****：针对一段时间未购买的客户，投放展示当下流行趋势单品的广告。
- ****Re-engage****：针对不活跃的订阅者，展示他们曾在您网站上查看过的商品，或提供限时促销活动。
- ****Cross-sell****：针对购买过某种产品的客户，推广另一种不同但具有互补性的产品。
- ****New customer****：针对访问过网站但从未购买的用户，通过广告鼓励他们完成首次下单（例如利用****弹窗****中提到过的首单优惠）。
- ****Cross-channel****：针对您已通过邮件触达的用户，投放相关广告以强化品牌信息，并使用类似的行动号召（CTA）。
- ****Potential brand enthusiasts****：这些客户近期有过购买，但频率不高且客单价较低。通过推广畅销品或相关产品，重点提升他们的购买频率或平均订单价值。
- ****Unengaged VIP****：如果曾经的 VIP 客户近期未与品牌互动，您可以在不同平台（如 Google）定向投放广告，将他们带回您的品牌。

##### 如何在 Google Ads 中应用这些 Segment

按照以下步骤，将上述 ****Segment**** 应用到 Google Ads 的广告组或广告系列中：

1. ****在 Klaviyo 中创建 Segment：****
   - 导航至 ****Audience**** 下的 ****[Lists & Segments](https://www.klaviyo.com/lists)****。
   - 点击 ****Create List/Segment****，然后选择 ****Segment****。
   - 根据您想要定向的目标群体设计过滤条件。
2. ****建立连接：****
   - 按照前文提到的“集成步骤”，将该 ****Segment**** 连接到一个新的 Google Audience。
3. ****在 Google Ads 中设置定向：****
   - 完成集成后，登录 Google Ads 后台。
   - 使用“定位（Targeting）”设置，将您的广告组或广告系列的目标指向从 Klaviyo 同步过来的受众。

****核心技巧：**** 如果一个用户通过****弹窗****加入了您的 ****List****，但一直没有打开您的欢迎邮件，这种“邮件不活跃”的用户是进行 Google 再营销的绝佳目标。

##### 在未来的广告活动中排除现有 Profile

如果您希望在广告中排除某些 ****List**** 或 ****Segment****（例如：排除近期刚购买过、短时间内不太可能再次下单的客户），您可以先在 Klaviyo 中创建该群体，将其同步至 Google Ads 的自定义受众，然后在广告组或广告系列中将其设为****排除项****。

- ****操作流程：**** 这与定向特定受众的过程非常相似，唯一的区别在于您需要在 Google Ads 中执行“排除”操作，而非“定位”。

##### 利用现有 Segment 优化投放目标

您可以利用 Klaviyo 中的 VIP ****List**** 或 ****Segment****，通过 Google 的“优化型投放 (Optimized Targeting)”来触达与您的优质客户特征相似的新潜客。

1. ****设置步骤：**** 在 Klaviyo 中创建或选择一个现有的 VIP ****Segment****，通过集成将其同步到 Google 受众。
2. ****应用信号：**** 在 Google Ads 中，启用“优化型投放”，并将该同步过来的 ****Segment**** 添加为该广告系列的****投放信号 (Targeting Signal)****。

- ****优势：**** 这能帮助您触达那些极有可能转化、且与您现有高价值客户属性类似的新受众。

##### 观察并监控特定受众的表现

您也可以选择仅****监控****广告在特定受众中的表现（即报表功能），而不改变广告系列或广告组的现有触达范围。

- ****决策依据：**** 通过对 Profile 的观察和数据报告，您可以决定是否要为这些群体创建一个全新的广告组/系列进行针对性投放，或者针对他们调整出价（Bid Adjustments）。
- ****场景应用：**** 比如，您可以观察那些通过****弹窗****注册但尚未下单的受众在通用搜索广告中的转化率，如果表现优异，则可以为他们增加出价。

##### EEA（欧洲经济区）合规授权要求

从 2024 年 3 月 6 日起，Google 开始在欧洲经济区（EEA）和英国（UK）强制执行《数字市场法案》(DMA)。因此，Google 更新了其[欧盟地区用户意见征求政策](https://support.google.com/adspolicy/answer/13165480)，要求所有与 Google Ads 集成的平台在向 Google 同步 EEA 或 英国地区的 Profile 时，必须包含广告投放授权（Advertising Consent）信息。

****Klaviyo 的应对方案：**** Klaviyo 的 Google Ads 集成已包含同步所需授权标识（Consent Markers）的选项。在设置集成时，您只需勾选以下选项即可：

****“我同意仅将那些已授权广告投放许可的受众发送给 Google。”**** **(I agree to only send audiences to Google that have granted consent for ad targeting)**

![Screenshot of a form asking if users market to people in the EEA or UK, with options for 'Yes' and 'No', and a consent statement for EEA/UK marketing.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-71.png?resize=1024%2C287&ssl=1)

当您在设置中选择此选项时，Klaviyo 会自动为同步中的 Profile 设置“广告个性化”和“广告用户数据”授权，以便您能够通过 Google Ads 对他们进行营销。这包括自动在 Google Ads 中设置授权状态。因此，如果您向 EEA 或英国地区的 Profile 投放广告，您的品牌必须确实在前端收集了这些授权，以确保符合合规要求。

重要提醒：

- ****授权区分：**** “广告授权（Advertising Consent）”与用于发送通信的“营销授权（Marketing Consent）”是分开的。如果您计划针对 EEA 或英国的 Profile 投放广告，必须在 Klaviyo 之外收集这些授权。
- ****如何收集：**** 通常，这需要通过 \*\*CMP（授权管理平台）\*\*来完成，例如 OneTrust。您的品牌应与 CMP 合作，以深入了解如何更好地管理广告授权数据，以及如何将其导出到其他平台。
- ****生效时间：**** 这一新要求的强制执行始于 2024 年 3 月 6 日，具有前瞻性。在此日期之前通过集成同步的 Profile 不需要追溯更新广告授权数据。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)