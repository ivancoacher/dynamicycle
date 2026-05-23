---
id: "115005248128"
title: "了解消息转化跟踪"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005248128-Understanding-message-conversion-tracking"
section: "Data explanations and attribution"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:22Z"
language: "zh"
---
## 你将会学到

了解转化跟踪如何适用于电子邮件、短信和移动推送消息以及如何编辑这些设置。对于发送的每个营销活动和流程，Klaviyo 都会自动跟踪转化情况。这使您可以分析营销渠道的绩效及其各自的成功。 ## 什么是转化跟踪？当收件人打开您的消息，然后在转换期间或[归因窗口](https://help.klaviyo.com/hc/en-us/articles/1260804504250) 内采取其他操作（例如下订单）时，就会发生转换。 Klaviyo 定义涉及订单的转化事件（例如**已下订单**、**已履行订单**、**已订购产品**等）。但是，这不包括订阅者只是打开您的电子邮件或开始结帐。虽然大多数其他平台仅跟踪收入转化，但 Klaviyo 会自动计算帐户中所有指标的转化分析。对于 2024 年 10 月 9 日之后的新客户，电子邮件和短信的默认窗口为 5 天，推送的默认窗口为 24 小时，但您可以在帐户的[电子邮件、短信和推送设置页面](https://help.klaviyo.com/hc/en-us/articles/11118357030555) 中进行调整。请注意，默认的 Klaviyo 电子邮件、短信和推送消息归因窗口可能与其他平台和供应商略有不同。 ## 转化跟踪如何运作？关于转化跟踪有一些重要注意事项：

- ****多渠道或合作归因****
  如果您使用多个营销渠道，Klaviyo 会查看每个单独渠道（短信或电子邮件）的归因窗口。从这里开始，确定这些渠道中的任何一个是否应该在购买时获得收入归属。例如，如果短信归因窗口已关闭，但电子邮件归因窗口仍然打开，并且客户在该时间段内与电子邮件进行了交互，则归因将转到电子邮件。 - ****转化打开并点击跟踪****
  如果有人打开或点击电子邮件，或者 Apple Mail Privacy Protection (MPP) 自动打开电子邮件，则会跟踪转化情况。但是，如果您想从转化指标中排除 MPP 打开，您可以[调整此设置](https://help.klaviyo.com/hc/en-us/articles/4416803987739)。仅当有人打开或点击消息时才会跟踪转化，不包括他们刚刚收到消息但未采取进一步操作的情况。 - ****转换期跟踪****
  当订阅者收到消息时，转换期开始。仅在转化期或归因窗口内发生的后续操作才会计入。 - ****转换期计时****
  对于电子邮件和短信，Klaviyo 每天都会查看消息归属。因此，无论您发送消息的哪一天，都会计算归因率和转化次数。例如，如果您在周五向所有收件人发送电子邮件，而他们在周五和周六都打开了这封电子邮件，则这些打开次数将归因于周五。 - ****转化报告****
  在查看任何[使用消息归因的分析报告](https://help.klaviyo.com/hc/en-us/articles/1260804504250-Understanding-Klaviyo-message-attribution#klaviyo-message-attribution-in-analytics-reports7)时，记住上述内容也很重要。如果您仅查看某一天的分析，Klaviyo 不会归因于与另一天发生的消息关联的转化。换句话说，查询个别日期意味着您为营销活动提供的产生收入的时间更少，并且您的分析将无法提供更大的情况。相反，请选择一个更广泛的时间范围来考虑您的转化窗口。 ### 为什么 Klaviyo 以这种方式跟踪转化？依赖像素的转化跟踪可能不可靠。例如，如果有人在手机上阅读电子邮件，但后来通过笔记本电脑进行购买，则依赖像素跟踪的跟踪将错过该转化。 Klaviyo 不使用像素，因此转化分析更加准确。相反，Klaviyo 根据直接来自内置集成或我们的 API 的数据来计算转化。您无需提前决定要关注哪个指标来进行转化跟踪。虽然大多数其他平台仅跟踪收入转化，但 Klaviyo 会自动计算帐户中所有指标的转化分析。例如，电子商务企业希望了解因电子邮件而发生的购买数量。 但是，如果他们对有多少人查看了至少一个产品页面或在收到电子邮件后开始结帐感兴趣，他们也可以查看此转化数据。这使他们能够比较不同绩效标准下不同活动的影响。 ## 电子邮件转化跟踪

与转化不同，Klaviyo 通过在每封电子邮件的底部放置一个微小的、不可见的像素图像来跟踪打开事件。这种开放跟踪方法是行业标准，不太可能导致垃圾邮件拦截器或邮箱提供商 (MBP) 出现问题。每当收件人打开或单击您的电子邮件时，我们都会将此不可见像素（网络信标）记录为“已查看”，并将电子邮件标记为已打开。无论您选择何种转化时间范围，我们都将继续跟踪您的打开次数和点击次数。了解如何在帐户设置中[编辑跟踪像素的位置](https://help.klaviyo.com/hc/en-us/articles/360049695831)。 ### 潜在的公开差异

收件人可以单击电子邮件而不打开它。例如，如果他们在电子邮件完全加载之前单击链接，则可能会发生这种情况。 Apple Mail Privacy (MPP) 还可能会考虑到非订阅者本人发起的打开。为了帮助从数据中删除 MPP 打开，请始终包含打开和点击过滤器，如下面的示例片段所示。这可确保您捕获所有被跟踪为单击但未打开消息的用户。您还可以调整帐户中的[电子邮件转换设置](https://help.klaviyo.com/hc/en-us/articles/360004059711)，以跟踪默认情况下 MPP 的打开情况。 ![非打开部分的示例，其中用户至少收到 1 封电子邮件，并且打开或点击它们的次数为零](https://klaviyo.zendesk.com/hc/article_attachments/28720770670363)

Klaviyo 通过向每个 URL 添加唯一的跟踪信息来跟踪点击活动。因此，当将鼠标悬停在 Klaviyo 电子邮件中的链接上时，您可能会看到以下示例开头的 URL。请注意，这可能看起来略有不同，具体取决于您的帐户是否具有[专用点击跟踪](https://help.klaviyo.com/hc/en-us/articles/360001550572-Setting-Up-Dedicated-Click-Tracking) 设置。 `[唯一帐户标识符].trk.klaviyomail.com`

## 短信转化跟踪

默认情况下，Klaviyo 设置 5 天的短信转换窗口，您可以在[帐户设置](https://help.klaviyo.com/hc/en-us/articles/11118357030555# adjustment-the-sms-attribution-window3)中编辑该窗口。当 SMS 在转化之前发送给收件人时，或者当收件人单击文本然后在归因窗口内执行其他操作（例如下订单）时，就会发生 SMS 归因。因此，转化窗口是指在发送或点击 SMS 消息后进行任何购买的小时数。请注意，为了跟踪个人资料的 SMS 点击转化，您需要发送一条带有链接的 SMS 消息，并且链接必须使用 Klaviyo 链接缩短程序。设置短信时，务必选中“****自动缩短链接****”选项，以确保您使用默认跟踪。请记住，Klaviyo 将归因与客户在购买或采取行动时与两个渠道的互动联系起来。详细了解[多渠道归因](https://www.klaviyo.com/blog/cooperative-multi-channel-attribution) 以及电子邮件和短信归因如何协同工作。如果您看到大量未归因的转化，请延长短信转化时间范围。 ## 推送转化跟踪

默认情况下，Klaviyo 为推送通知设置 24 小时归因（也称为转化）窗口。但是，您可以在设置中编辑此窗口。当收件人点击通知（即打开推送），然后在归因窗口内执行另一个操作（例如下订单）时，就会发生推送归因。因此，归因窗口是推送通知打开后的小时数，在此期间 Klaviyo 会将转化归因于该消息。请记住，Klaviyo 将归因与客户与每个渠道（推送、短信和电子邮件）的交互联系起来。此外，Klaviyo 将转化归因于客户与之交互的最后一条消息，该消息仍在归因窗口内。 ## 多渠道转换

当您通过多个渠道发送消息时会发生什么？转化将归因于哪条消息？ Klaviyo 使用“最后接触”模型和每个频道的归因窗口的组合。它将转化归因于最近单击或打开的任何消息，只要该转化也在消息的归因窗口内。例如，假设：

- 客户在第 1 天打开电子邮件。 - 同一客户在第 2 天打开推送通知。如果客户在第 3 天购买产品，则转化将归因于推送通知。推送是“最后一次接触”，只要购买发生在 24 小时内，收入就会记入该通知。但是，假设客户在第 4 天购买了产品。在这种情况下，转化将归因于电子邮件。由于购买是在推送转化窗口之外，因此不能归因于推送。但是，购买确实发生在电子邮件窗口内，因此 Klaviyo 会将转化归因于电子邮件。 ## 电子邮件和短信网站跟踪

当您将 Klaviyo 网络跟踪代码段添加到您的网站时，它只能跟踪“已知浏览器”的事件。

Klaviyo 有几种不同的方式来识别网站访问者以进行网络跟踪：

- ****网站跟踪已启用****
  当您启用电子邮件到网站跟踪并在您的网站上安装 Klaviyo 的主要网络跟踪代码段时，Klaviyo 将识别并 [cookie](https://klaviyo.zendesk.com/hc/en-us/articles/360034666712) 点击 Klaviyo 电子邮件或短信并最终浏览您网站的个人。 - ****订阅者选择加入****
  当某人在某个时候通过 Klaviyo 表单订阅/选择加入时，网络跟踪代码将在选择加入时对此人进行 cookie。您可以在[帐户的电子邮件设置](https://help.klaviyo.com/hc/en-us/articles/11118357030555-How-to-change-your-email-and-SMS-message-attribution-settings# adjustment-the-email-attribution-window2)中打开和关闭 Klaviyo 跟踪电子邮件到网站活动的功能。请注意，Klaviyo 会向您的电子邮件或短信中的所有 URL 添加一个称为“_kx”参数的参数，以跟踪活动。然后，Klaviyo 的网络跟踪会对这一独特的编码参数进行解码，并提供识别点击 URL 的用户的能力。此参数会自动附加，不会影响 URL 的加载时间，也不会根据其位置破坏任何 URL。请参阅下面的示例链接，了解其在 URL 中的外观：

`http://example.com/?_kx=J8fjcn003Wy6b-3ILNlOyZXabW6dcFwTyeuxrowMers%3D.McN66`

### Klaviyo 和 Google Analytics 之间的潜在差异

由于 Google Analytics 使用链接点击来跟踪转化，而 Klaviyo 直接使用数据库中的数据，因此两种服务之间的分析可能不会完全一致。因此，在某些情况下，Google Analytics（分析）可能不会在实际发生时记录转化。例如，如果订阅者收到电子邮件、阅读该电子邮件、未点击链接而是访问您的商店，则 Google Analytics（分析）不会记录转化。或者在另一种情况下，客户收到一条短信，打开它，但最终从他们的桌面上进行购买； Google Analytics 也不会记录此转化。然而，在这两种情况下，Klaviyo 都能识别这些转换并将它们缝合在一起。在第一个示例中，Klaviyo 识别出订阅者首先打开了电子邮件，而在第二个示例中，识别出 SMS 消息触发了最终的购买。请记住，Klaviyo 只会在打开的[消息归因窗口](https://help.klaviyo.com/hc/en-us/articles/1260804504250-Understanding-Klaviyo-message-attribution#klaviyo-attribution-timing-for-email-vs--sms3) 中识别这些内容。由于这种根本差异，我们建议尽可能采用 Klaviyo 的转化分析。 ## 将 UTM 跟踪附加到电子邮件

在 Klaviyo 中创建流程、电子邮件或 SMS 营销活动时，您可以将 UTM 参数添加到电子邮件中。您可以[在帐户级别自定义这些 UTM 跟踪参数](https://help.klaviyo.com/hc/en-us/articles/115005247808-Klaviyo-and-Google-Analytics-Tracking)，也可以在电子邮件级别配置这些参数。 默认情况下，Klaviyo 将跟踪：

****电子邮件****

- ****来源****
  列表或段名称
- ****中****
  电子邮件
- ****活动****
  活动名称，包括活动 ID

****短信****

- ****来源****
  列表或段名称
- ****中****
  短信
- ****活动****
  活动名称，包括活动 ID

****流量****

- ****来源****
  流程名称
- ****中****
  电子邮件（请注意，这是默认设置，但您也可以更新设置以反映短信或活动）
- ****活动****
  流消息名称，包括流id

例如，如果您有一个[欢迎系列流程](https://klaviyo.zendesk.com/hc/en-us/articles/115002775172)，第一封电子邮件名为“我们的品牌简介”，流程电子邮件 ID 为 A12bc3，则以下 UTM 参数将附加到您的链接中：

- ****中****
  电子邮件
- ****来源****
  **欢迎系列**
- ****活动****
  “我们的品牌简介 (A12bc3)”

请记住，在 Google Analytics 中，5 个默认 UTM 参数（即 utm\_medium、utm\_source、utm\_campaign、utm\_content 和 utm\_term[Klaviyo 配置文件ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6)) 将自动小写。 ### 附加参数

除了上述默认参数外，您还可以选择在帐户级别设置中打开以下字段：

****电子邮件****

- ****身份证号码****
  您可以选择添加营销活动 ID、带有营销活动 ID 的营销活动名称、[外部 ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5)、[Klaviyo 个人资料ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6)，或链接文本或替代文本。 - ****期限****
  您可以选择包含[外部 ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5)、[Klaviyo 配置文件ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6)，或链接文本或替代文本。 ****短信****

- ****身份证号码****
  您可以选择添加营销活动 ID、带有营销活动 ID 的营销活动名称、[外部 ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5)、[Klaviyo 个人资料ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6)，或链接文本或替代文本。 - ****期限****
  您可以选择包含外部 ID、Klaviyo 个人资料 ID、链接文本或替代文本。 ****流量****

- ****身份证号码****
  您可以选择包含流 ID、带有流 ID 的流消息名称、[外部 ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5)、[Klaviyo 配置文件ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6)，或链接文本或替代文本。 - ****期限****
  您可以选择包含[外部 ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#i5)、[Klaviyo 配置文件ID](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary#k6)，或链接文本或替代文本。 ## 其他资源

- [如何更改消息归属和转换设置](https://help.klaviyo.com/hc/en-us/articles/11118357030555)
- [了解消息归属](https://help.klaviyo.com/hc/en-us/articles/1260804504250)
- [Klaviyo现场跟踪入门](https://help.klaviyo.com/hc/en-us/articles/115005076767)
- [了解 Klaviyo 中的 UTM 跟踪](https://help.klaviyo.com/hc/en-us/articles/115005247808)