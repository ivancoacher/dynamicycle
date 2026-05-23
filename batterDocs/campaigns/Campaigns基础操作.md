---
id: 4835
title: "Campaigns基础操作"
slug: "campaigns%e5%85%a5%e9%97%a8"
category: "活动与营销（Campaigns）"
category_slug: "campaigns"
wp_url: "https://dynamicycle.com/docs/campaigns%e5%85%a5%e9%97%a8/"
wp_modified: "2025-12-22T06:38:38"
---

![AI Doc Summarizer](https://dynamicycle.com/wp-content/plugins/betterdocs/assets/images/ai-summary-icon.svg?v=4.5.0)
Doc Summary

![AI Doc Summarizer Thinking](https://i0.wp.com/dynamicycle.com/wp-content/plugins/betterdocs/assets/images/thinking-spinner.gif?ssl=1)

Thinking

了解一下邮件 Campaign 的基础知识，包括它是什么，以及如何在 Klaviyo 里发送。

邮件 campaign 就是一次性发给一个特定联系人群组的邮件——比如定期的 Newsletter、促销公告，或者其他推广邮件。单个 Campaign 可以创建后立即发送，也可以先准备好，然后 Schedule 在之后的时间发送。

### ****Campaigns vs. Flows****

在 Klaviyo 里，区分 Flows 和 Campaigns 很重要。

| ****Campaign**** | ****Flow**** |
| --- | --- |
| 发送给你提前建好的 Target List | 发送一条或多条 Automated Messages，根据特定的 Triggers 和 filters 来设定 |
| 手动创建和 Schedule | 每当某个特定行为发生时被 Trigger |
| 例子：发给 Newsletter list 的月度邮件，或通过短信发给老客的闪购通知 | 例子：新用户注册后，自动发送的 Welcome email 或 SMS |

### ****创建一个新的 email campaign****

Klaviyo 的 Campaign 会一步步指导你完成创建。

1. 前往 Campaigns 标签页
2. 选择以下任一选项：
   - Create：从头开始定义所有 campaign 细节。
   - Library：用为你量身定制的预制草稿，快速启动一个 campaign。
3. 选择 Email。
4. 点击 Continue。

### ****设置你的 campaign****

当你点击 Create campaign 后，侧边栏会让你进行以下设置：

- Campaign name
  - Campaign 的日期会自动填入作为名称，但你可以改成任何你想要的名字。Campaign name 是必填项。
- Type
  - 根据你的账户情况，选择 Email、SMS 或 Push。
- Tags
  - 可选的 Tags，能帮你更好地管理创建的 Campaigns。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_437000_ZoKHWhg0OnevBcJj_1765436178?w=600&h=1256&type=image/png)

在侧边栏选好选项后，点击 Continue 前往 Recipients 界面，或点击 Save draft 返回 Campaigns 标签页。

### ****添加收件人****

下一个界面是设置你要发给谁，以及发送的细节。一个 Campaign 至少需要 1 个收件人才能发送，否则会被自动取消。

1.选择一个已有的 List 或 Segment 来作为目标。Klaviyo 建议主要发给 Engaged Subscribers（也就是最近有打开或点击邮件的用户）。如果你已经在 Klaviyo 里用过 Flows，那你的账户里就有足够的数据来创建一个 engaged segment。

2.如果想发给多个 Lists/Segments，选择你要 Include 或 Exclude 的 lists/segments。单个 campaign 最多可以发给 15 个 Segments/Lists。了解更多关于 Klaviyo 的 Multi-list sending 功能。

3.注意一下预期的收件人数量——这个估算值已经剔除了重复的资料、被排除的资料和 Suppressions。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_82440_SuckBO3KPYzwViQQ_1765436397?w=1000&h=384&type=image/png)

4.可选操作：

- 要避免发给某些群组，在 Don’t send to 下面添加一个 segment。
- 要避免收件人一下子收到太多邮件，可以开启 Smart Sending，这样会跳过那些最近已经收到过你账户邮件的 Profiles。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_445735_Tk7zSoT9QWPmBHC__1765436574?w=1260&h=614&type=image/png)

5.选择是否要跳过那些最近通过此渠道收到过其他消息的收件人。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_680382_j12FJHz9DegvtNcx_1765436594?w=1000&h=166&type=image/png)

6.如果需要，可以点击齿轮图标来编辑 Campaign 的名称和 Tags。

7.在侧边栏，点击 Tracking 标签页来启用或禁用 Tracking 参数（比如 UTM tracking）。记得点击 Save 保存你的更改。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_621427_Ug2drs3aISN6DQ_6_1765436673?w=600&h=494&type=image/png)

### ****创建邮件内容****

下一个界面就是你构建邮件模板的地方。你可以新建一个模板，或者从模板库里选一个。在这一步，你还可以选择给你的邮件添加一个 Variation，用来做 A/B test。

![一个包含已保存电子邮件模板的界面，左侧展示两个模板，右侧为电子邮件消息设置，包括主题行、预览文本、发件人姓名和发件人邮箱等选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-17.png?resize=930%2C515&ssl=1)

1.仔细检查 Subject line、Sender name 和 Sender email address；如果你希望回复发到另一个邮箱，可以添加一个不同的 Reply-to email address（比如，你希望 Klaviyo 邮件来自个人邮箱，但回复发到客服邮箱）。

2.选择你想要如何创建 Campaign 内容：

- Saved templates

从右边选择一个你之前创建并保存过的模板。

- Email library

浏览模板库，寻找不同的拖拽式模板选项。

- Text Only

点击操作按钮并选择 Switch to text only editor。如果你想发一封纯文本邮件，就是这个选项。这是一个不错的选择，能让邮件看起来像是直接来自你个人，而不是你的组织。

- HTML

点击操作按钮并选择 Switch to HTML editor。如果你有自己的 HTML 邮件模板要导入，或者想从头开始写一个 HTML 模板，就选这个。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_862852_UZr9TvEabYr7O2A6_1765436764?w=526&h=304&type=image/png)

- Create a blank email

使用拖拽式编辑器修改你的设计，然后点击 Next。

### ****Schedule 和发送你的 campaign****

第三个也是最后一个界面，让你可以 Review、Schedule 和发送你的 Campaign。在这一步，你也可以选择给你的邮件添加一个 variation 来做 A/B test。

1.编辑完 Campaign 内容后，点击 Next。

2.Review 所有部分，并修正侧边栏中指示的任何问题。如果一切就绪，点击页面顶部的 Schedule or send。

![Klaviyo 界面展示了一个电子邮件营销活动的审核阶段，包括目标观众数量、电子邮件内容及相关设置。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-18.png?resize=930%2C503&ssl=1)

3.Schedule 或发送你的 Campaign。

选择你希望何时发送你的Campaign，它会在你设定的时间点之后几分钟内排队并发送。你可以选择立即发送，或在以后的日期和时间发送。了解更多关于 Campaign Schedule 和 Send 的选项。

当你 Schedule 一个 Campaign 邮件时，Klaviyo 会开始添加收件人，根据任何被排除的 lists 和你选择的设置来确定发送对象。对于目标为成百上千收件人的 Campaigns，在高流量发送期间，这个过程可能需要几分钟。了解如何取消或重新 Schedule 一个 Campaign。

### ****邮件 campaign 示例****

- 新品或精选

突出展示新品或当季产品，或者介绍你的公司或组织有什么新动态。

- Storytelling

你的企业或组织只是众多之一。解释是什么让它独一无二，并展示品牌“背后的人”，可以通过帮助你的 Subscribers 感觉与你的业务和你本人更有联系，从而建立品牌忠诚度和社区感。

- Highlight interesting content

为最近的 Blog post 或你创建的其他内容提供一个简短的导语，然后给 subscribers 发一个链接阅读更多。将你公司的声音打造成行业内相关的新颖有趣内容的首选来源，这是让 Subscribers 和客户持续回访的好方法。

- Promotions

宣布你的企业正在提供的特别促销或折扣。如果这个优惠是 Email subscribers 专享的就更好了——营造紧迫感和独家感能有效促进行动。

### ****Review 你的结果****

你的前几个 Campaigns 对于建立健康的邮件 Deliverability 至关重要。使用 Klaviyo 的 Campaign reporting 工具来查看你的 Campaign 表现如何，并找出可以改进的地方。了解 Deliverability 以及发送给 Engaged subscribers 的重要性，以便长期最大化你的收入。