---
id: 7294
title: "如何管理 email suppressions 以及 bulk delete profiles"
slug: "emailsuppressionsbulkdeleteprofiles"
category: "数据与受众（Analytics &amp; Audience）"
category_slug: "analytics-audience"
wp_url: "https://dynamicycle.com/docs/emailsuppressionsbulkdeleteprofiles/"
wp_modified: "2026-03-31T02:21:02"
---

##### 删除与抑制 Profiles

Klaviyo 为你提供了两种选项：你可以选择将 profiles 从账户中彻底删除，或者对其执行 suppress。如果选择 suppress，这些 profiles 仍会保留在你的账户中，但无法接收营销信息。具体选择哪种方式，取决于你的业务需求。

##### Deleting（删除）

当你在 Klaviyo 中删除 profiles 时，它们连同其数据会被彻底从你的账户中移除。你将无法再查看这些 profiles 及其与你的品牌或消息的互动情况。已删除的数据无法恢复。

请注意，由于被删除 profile 的数据也已丢失，如果他们在被移除后与你的网站进行了互动（例如提交了注册表单），他们可能会作为新的 profile 再次进入你的 Klaviyo 账户。

当你确定不再需要某 profile 的数据，或者该 profile 请求删除其数据时，你应该在你的账户中删除这些 profiles。

##### Suppressing（抑制）

当你在 Klaviyo 中 suppress profiles 时，它们会保留在你的账户中，但不再被视为活跃状态。在被 suppress 的状态下，profiles 无法接收营销邮件，并且不会计入你账户的配额限制。即使 suppress 的 profile 已经提供了同意并表示希望接收邮件，他们也无法收到营销信息。

当你不再希望某些 profiles 接收任何营销邮件，但仍希望使用其数据进行分析和维护客户群的完整视图时，你应该在你的账户中 suppress 这些 profiles。

批量抑制 Profiles

在 Klaviyo 中，你可以批量 suppress 列表或细分中的 profiles。要批量 suppress 一组 profiles：

一旦手动 suppress 了某个 profile，如果该 profile 随后被取消 suppress，则在 90 天内无法再次手动对其进行 suppress。此规则在创建新账户后的前 30 天内不生效。

- 进入 Klaviyo 中“受众”标签下的“Lists & segments”页面。
- 在你要 suppress 的列表或细分旁边，打开操作菜单。
- 选择“Suppress 当前成员”以 suppress 该组的所有成员。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_898791_UBRq-Yjeyn-zdNSq_1774879086?w=1860&h=1074&type=image/png)

如果该组包含符合以下条件的 profiles，Klaviyo 会在执行操作前显示一个包含两个选项的弹窗。该弹窗会汇总将要被 suppress 的 profiles 数量，并允许你查看一组符合弹窗中“近期活跃”标准的 profiles，以便考虑将其保持活跃状态。你可以选择：

- 仅 suppress 非活跃 profiles（此选项不会 suppress 近期活跃的 profiles）
- Suppress 所有人（当前默认行为）

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_760918_FVGBg4VMH_tom_Yf_1774879105?w=1484&h=818&type=image/png)

在弹窗中，你可以下载一份 CSV 文件，其中包含将保持活跃的 profiles 信息，包括姓名、邮箱、profile ID、电话号码和最后活跃日期，以便于审计或重新导入的Flow。

此操作仅适用于执行 suppress 时列表或细分中的所有 profiles，不会影响之后加入的 profiles。如果组中的某个 profile 已经被 suppress，其状态不会受到影响。

##### ****当没有需要保持活跃的 Profiles 时****

如果列表或细分中没有 Profiles 满足近期活跃规则（即在过去约 6 个月内没有经过验证的点击或订单），弹窗将只显示一个“Suppress 所有人”的选项。在这种情况下：

- 不存在单独的“保持活跃”组，并且
- 其行为等同于现有的批量抑制流程，没有任何建议排除的项。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_269959_R4DfMnow4-WqBBBL_1774879147?w=739&h=203&type=image/png)

##### 查看可以保持活跃的 Profiles

批量抑制弹窗使用了与细分构建器相同的逻辑。当你抑制一个列表或细分时，Klaviyo 会将“活跃”的 Profiles 识别为符合以下条件的用户：

位于你正在抑制的列表或细分中，并且：

- Profile 已订阅接收邮件营销
- 并且该 Profile 没有将你的任何邮件标记为垃圾邮件
- 并且该 Profile 在最近 6 个月内有真人验证的邮件点击（非机器人）或有购买行为

要重现弹窗建议保持活跃的 Profiles 集合，你可以构建一个细分，例如：

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_588798_CSB5xRsErDFxxvWN_1774879168?w=1600&h=663&type=image/png)

##### 通过上传 CSV 文件进行抑制

如果你想保留账户中的一组联系人，并通过抑制他们来停止向其发送邮件，你也可以将他们上传到你账户的抑制列表中。

- 创建一个包含你想要抑制对象的列表或细分。
- 将此列表或细分导出为 CSV 文件。
- 删除电子表格中除标题为“Email”的列之外的所有列。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_530644_8jJ9g4MTYuXS4PcF_1774879187?w=650&h=568&type=image/png)

- 进入“Profiles”标签页。
- 点击该页面右上角的“查看被抑制的 Profiles”按钮。
- 选择“导入”。

##### ****抑制建议****

除了从“列表与细分”进行批量抑制外，Klaviyo 还会在“被抑制的 Profiles”页面突出显示长期不活跃的 Profiles，以供你考虑进行抑制。

这些建议基于现有的类似“sunset”的不活跃定义，旨在帮助你在不抑制近期购买者或点击者的情况下减少活跃 Profile 的数量。

##### ****抑制建议的工作原理****

当你的账户中存在符合“日落”细分条件的 Profiles 时，你将在“被抑制的 Profiles”页面顶部看到一个横幅，其中汇总了建议抑制的 Profiles 数量。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_303580_xyFbZVaSb_EZP6vz_1774879226?w=1684&h=253&type=image/png)

- 建议的 Profiles 必须满足以下标准：
- 创建于至少 180 天前
- 在过去约 72 周内收到过 5 封或更多邮件
- 从未打开或点击过你的邮件
- 从未访问过你的网站或进行过购买。

那些仍显示近期经过验证的互动（如过去约 6 个月内的真人点击或订单）的 Profiles 不会包含在这些建议中，并且会继续受到你现有防护机制的保护。

##### 查看并抑制建议的 Profiles

要执行抑制建议：

- 进入“受众” → “Profiles”，然后点击“查看被抑制的 Profiles”。
- 如果有可用的抑制建议，请查看横幅文本，其中汇总了建议抑制的 Profiles 数量。
- 点击“查看并抑制”Profiles 以查看建议的 Profiles 并对其进行抑制。
- 在你确认后，Klaviyo 只会抑制建议弹窗中包含的 Profiles。你账户中的其他活跃 Profiles 不会受到影响。

##### ****批量取消抑制 Profiles****

你也可以批量取消抑制列表或细分中的 Profiles。要批量取消抑制一组 Profiles：

- 进入“受众”标签下的“Lists & segments”页面。
- 在你要取消抑制的列表或细分旁边，打开操作菜单。
- 选择“取消抑制当前成员”以取消抑制该组的所有成员。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_746614_lww_iC21Kc1qQzxk_1774879256?w=1848&h=1074&type=image/png)

只有非送达相关的抑制可以被移除。如果一个 Profile 由于硬退信或连续 7 次软退信而被抑制，为了保护你的送达率，该抑制无法被移除。

此操作仅适用于取消抑制时列表或细分中的所有 Profiles，不会影响之后加入的 Profiles。如果组中的某个 Profile 已经被取消抑制，其状态不会受到影响。

##### ****批量删除 Profiles****

当你删除用户时，这些 Profiles 会被彻底擦除，且不会保留任何历史记录。通常，你应该尽量抑制而不是删除 Profiles。

要永久从你的账户中移除一组用户：

- 创建一个包含这些联系人的Lists & segments。
- 点击屏幕左下角的“你的账户”下拉菜单，然后选择“设置”。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_571918_YXqy-Vgm2QLdeyvN_1774879293?w=482&h=450&type=image/png)

- 进入“其他” > “Profile 维护”。
- 在“移除 Profiles”部分，从下拉菜单中选择你希望删除的列表或细分。
- 点击“删除用户”。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_328642_Fw8Ge_oAvsEfCTax_1774879310?w=1268&h=598&type=image/png)

在出现的确认弹窗中，在字段中输入数值以确认你想要删除的 Profiles 数量。

![](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_736205_bKw52RLjpLEFRgZq_1774879326?w=2484&h=1146&type=image/png)

##### ****结果****

一旦你抑制了一个Lists & segments，该组中的所有 Profiles 都将处于被抑制状态。

- 如果你在“Lists & segments”页面使用了批量抑制选项并选择了“仅抑制不活跃的 Profiles”，那么只有不符合近期活跃标准的 Profiles 才会被抑制。
- 如果你使用了“被抑制的 Profiles”页面中的抑制建议横幅，那么只有你在该建议中确认的 Profiles 才会被抑制。

- 你账户中的其他 Profiles 保持不变，并且仍然可以根据其同意状态接收邮件。被抑制的 Profiles 无法通过电子邮件联系，也不会计入你的 Klaviyo 计费方案。即使被抑制的 Profile 已提供同意并表示希望接收邮件，他们也无法接收营销信息。
- 当你取消抑制一个列表或细分时，该组中的所有 Profiles 将能够接收邮件，除非他们之前已选择退出。取消抑制 Profile 不会影响其同意状态，因此如果 Profile 之前已取消订阅，他们仍然无法接收邮件，因为他们已选择退出。
- 如果你删除 Profiles，它们将被彻底擦除，且不会保留任何历史记录。这是一个永久性操作，无法撤销。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)