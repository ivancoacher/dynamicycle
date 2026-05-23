---
id: 5350
title: "Deliverability入门"
slug: "start-with-deliverability"
category: "投递与合规（Deliverability &amp; Compliance）"
category_slug: "deliverability-compliance"
wp_url: "https://dynamicycle.com/docs/start-with-deliverability/"
wp_modified: "2025-12-24T06:17:44"
---

##### 什么是邮件[Deliverability](https://www.klaviyo.com/analytics/deliverability/email/score)？

邮件送达率是一个非常微妙的概念，有多个因素会影响一封邮件能否被成功递送。要让一封邮件成功出现在收件人的收件箱中，主要由两个部分组成：邮件Delivery) 和 邮件Deliverability。

###### 邮件Delivery

邮件递送是指邮件成功送达收件人邮件服务器的过程。如果邮件未能成功送达或被收件人的邮件服务商拒绝，就会发生Bounce。

影响递送的因素包括：

- 收件人邮箱地址的有效性： 尝试向不存在的地址发送邮件会导致系统拒绝接收。
- 接收端服务器的临时问题： 例如收件人的收件箱已满，或者他们的邮件服务器暂时宕机。
- 邮件身份验证： 邮件服务器使用 SPF、DKIM 和 DMARC 等验证协议来核实邮件是否来自合法发送者，并会拒绝验证失败的邮件。
- 速率限制： 在极短的时间内向同一个邮件服务器发送过多邮件，可能会导致邮件被拦截或拒绝。

###### ****邮件[Deliverability](https://www.klaviyo.com/analytics/deliverability/email/score)****

邮件送达率是指邮件在成功进入收件人邮件服务器后的落点位置。

- 落点： 良好的送达率能确保你的邮件进入收件人的主收件箱（包括标签式收件箱，如 Google 的 Promotions 推广标签页）。
- 衡量标准： 送达率主要通过反映“真实人为参与”的指标来衡量，例如：Opens、Clicks、回复 、转发 或 转化。

注意： 你可能会拥有很高的“递送率”，但“Deliverability”却很差。这意味着虽然邮件都发出去了且对方服务器也收到了，但大部分邮件都进了垃圾邮件箱，而不是主收件箱。

##### 影响 Deliverability 以及你作为发件人信誉的 4 个核心要素：

1. 发送对象及其互动情况

指的是你发送的 profiles 以及他们对你邮件的参与度。

2. 发送习惯

每次发送邮件的数量以及发送的频率。

3. 邮件内容

收件箱服务商会使用垃圾邮件过滤器，根据图片、链接和邮件主题等内容来判断你的邮件是否能进入收件箱。

4. 发送基础设施

你发送邮件时所使用的基础架构，例如 sending domain、点击追踪域名以及 IP address。

##### ****Deliverability 最佳实践****

通过遵循以下 Deliverability 最佳实践，你可以为你的品牌打下成功的基础，并确保更多邮件能够进入收件人的主收件箱。

###### 预热

所有使用全新专用基础设施（如：新的 Dedicated IP 或新注册的 Root domain）的 Klaviyo 客户，都必须完成相应的 IP 或域名预热。

什么是“冷（Cold）”基础设施： 指过去 30 天内未用于发送邮件的 IP 地址，或是在过去 30 天内新注册（或从未用于发送邮件）的根域名。

Warming 的本质： 这是一个建立过程，目的是在邮件服务商心中树立你作为一个合法、且“表现优秀”的发件人的信誉。

###### Ramping

无论你使用的是 Dedicated IP 还是 Shared IP，Ramping 都是辅助整体预热过程、帮助你成为信誉良好发件人的关键手段。

- Dedicated IP： 此时 Ramping 是针对新基础设施整体预热过程的一部分。
- Shared IP： 新客户需要通过 Ramping 来针对其与 Klaviyo IP 的新合作关系建立信誉。
- Ramping 的操作逻辑： 从极小规模的邮件发送量开始，然后随着时间的推移逐渐增加发送量。

###### 时间线与预期管理

根据你的邮件发送总量，整个 Warming 过程可能会在你完成 Ramping（即达到全量发送）之后仍在继续：

- 量级提升速度： 例如，将发送量提升到 10 万封可能仅需 10 天。
- 初步评定周期： 邮件服务提供商（ESP）或邮箱提供商（MBP）通常需要长达 30 天 的时间才能对你的发件人信誉做出初步判定。
- 波动期： 在信誉验证期间，你可能会注意到邮件表现（如打开率和点击率）在长达约 120 天 的时间内存在波动，这属于正常现象。

###### ****导入洁净的名单****

如果你打算将现有的邮件名单同步或手动导入 Klaviyo，若不事先进行清洗，你的 Deliverability 将面临巨大风险。

- 数据利用： 你之前的邮件服务商（ESP）通常会提供分析主名单互动情况的方法，例如：打开率、退信率（Bounce rates）等。

- 清理无效数据： 在迁移到 Klaviyo 之前，强烈建议利用所有可用数据来隔离并剔除无效或不活跃的邮箱。 导入这些“垃圾”邮箱只会让你的发送量虚增，并严重拖累你的 Deliverability。

- 时间节点： 这一步必须在你在 Klaviyo 进行首次发送之前完成。
- 仅向已订阅的收件人发送邮件：确保你的主邮件名单中仅包含那些明确表示加入订阅的个人，不要有意（或无意）地去联系那些从未订阅的人。

###### 区分“客户”与“订阅者”

我们强烈建议将“客户”与“已授权订阅者”分开管理：

- 相互转换： 客户可以随时成为订阅者，订阅者也可以随时成为客户。
- 授权差异： 客户可能下过订单，但这并不代表他们同意接收常规的营销邮件。
- 负面影响： 如果你不分青红皂白地向账户里所有人发送 Campaign，而不考虑他们是否订阅了营销内容，你会发现退订率飙升且互动率下降——这两者都会对你的 Deliverability 产生负面影响。

###### ****使用双重订阅验证****

最佳实践是让新订阅者在首次加入时确认其邮箱地址。

Double Opt-in 的优势： 帮助你在增加名单人数的同时，减少恶意滥用，防止无效或拼写错误的邮箱进入系统，并能获得一个互动意愿更高的名单。 如果你针对一个或多个名单关闭了 Double Opt-in，你必须非常勤勉地每月进行一次名单清洗。

###### ****定期进行名单清洗****

不要给邮件服务商任何将你标记为垃圾邮件的借口。

操作建议： 利用 Deliverability Hub 提供的逻辑创建一个 segment，用来 suppress（抑制/退订）那些从未与你的邮件互动的订阅者。

为何重要： 大多数主流邮件服务商（如 Gmail 和 Yahoo）会严密追踪收件人如何与你的域名进行互动（例如：多少邮件被标记为垃圾邮件、打开率是多少、bounce 率是多少等）。因此，持续向这些零互动的 profiles 发送邮件会严重蚕食你的发件人信誉。

后果： Mailbox Providers 会根据这些数据决定你邮件的落点——是进入收件箱还是垃圾邮件文件夹。如果你的名单中包含大量不感兴趣的人或高比例的无效邮箱，只会阻碍你触达那些真正想要接收你邮件的客户。定期清洗名单以排除这些人至关重要。

###### ****创建[Engaged segment](https://www.klaviyo.com/lists)****

你不仅应该只向已订阅的联系人发送邮件，还应致力于向“高互动”的订阅者发送；否则，你将面临损害 deliverability 表现的风险。

操作方法： 为了隔离出高互动的订阅者，请创建一个 Engaged Segment。

应用场景： 在发送 campaigns 时，将此分群作为你的核心目标受众。

###### 配置邮件发送基础设施

在 Klaviyo 中，你可以选择使用共享基础设施或自己的专用基础设施。

Klaviyo 建议设置专用发件域名。

- 优势： 使用品牌自己的域名发送邮件而非 Klaviyo 的域名，从而在自己的域名上积累发件人信誉。
- 安全性： 启用 DKIM 和 SPF 身份验证，帮助接收端服务器核实发件人身份。
- 关键配置步骤：
- DMARC 政策： 确定品牌是否正在使用 DMARC 政策并确保其有效。
- 域名对齐： 确保发件人邮箱地址的根域名与专用发件域名的根域名一致。
- 专用点击追踪域名： 连接专用域名以提升链接的可信度。
- 设置 BIMI： 通过 DNS 设置在收件箱中展示品牌 Logo。这能增强品牌辨识度，建立信任，并通过提高互动率来提升 Deliverability。

###### 管理邮件偏好

- 多选项订阅： 在表单和偏好设置页面添加字段，让订阅者选择接收邮件的频率。
- 基于偏好的分群： 根据这些偏好进行 segment，确保发送频率符合受众预期。
- 数据支持： eMarketer 研究显示，进行名单分群的邮件营销人员中，39% 获得了更高的打开率，28% 降低了退订率，24% 提升了 Deliverability、销售线索和收入。

###### 让退订变得简单

如果退订流程复杂，用户更有可能将你的邮件标记为垃圾邮件。

垃圾邮件投诉的严重性： 投诉率一旦达到 0.05%，邮箱提供商（如 Gmail、Yahoo）就会将你视为“不良发件人”，并可能对所有收件人屏蔽你的邮件。

最佳实践： 在邮件的顶部和底部都放置退订链接。一次退订的负面影响远小于一次垃圾邮件投诉。

###### 创建高互动内容

- 避免垃圾邮件特征的标题：

避免全部大写（85% 的人更喜欢全小写或正常大小写）。

避免过多的感叹号（!!!!!）或符号（\*\*\*\*\*）。

避免使用煽动性词汇，如 “100% FREE!”, “ACT NOW!”。

- 图片与文字的平衡：

纯图片邮件易触发垃圾邮件过滤器。

建议： 邮件应包含至少 500 个文本字符。为图片添加 ALT text（替代文本），这不仅有助于避开过滤器，还能提升无障碍体验。

- 限制 URL 数量：

避免在正文中放入过多的超链接，特别是指向非自有域名的链接。

- 个性化 ：

使用 Klaviyo 的功能在主题和正文中插入收件人姓名。

鼓励联系人将你添加到联系人。

在不确定时，使用 Mail Tester 等工具运行 Spam 过滤测试。

###### 发送计划与 [Sunset Flow](https://www.klaviyo.com/flows)

发送计划： 建立基于客户互动程度的发送节奏。过度发送给不活跃的 profiles 会损害信誉，而对活跃客户发送过少则会错失收入。

Sunset Flows： 专门用于逐步淘汰不再互动的客户。这是赢回客户的最后尝试，如果对方仍无反应，则应将其删除或抑制。这能保持名单洁净，保护 Deliverability。

##### 监控 Deliverability

定期监控以下核心指标，以便在问题扩大前及时采取措施：

- 打开率
- 点击率
- 退订率
- 垃圾邮件投诉

[Klaviyo Deliverability Hub](https://www.klaviyo.com/analytics/deliverability/email/score)： 这是一个集中化的空间，允许你在账户层面分析并诊断邮件的 Deliverability 健康状况。

![A screenshot of a Deliverability Hub showing a deliverability score of 84, metrics including open rate, click rate, bounce rate, unsubscribe rate, and spam complaint rate, along with a section for creating a sunset flow.](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_621355_YhliRGNMQPVv9Ik8_1766026894?w=2416&h=1244&type=image/png)

在 Deliverability Hub 中，你会看到一个代表你整体 Deliverability 表现和发件人信誉的分数，以及各项关键指标的具体表现。此外，该中心还提供了一个操作中心，为你列出推荐的后续优化步骤，并提供各种报表，让你深入了解自己在不同邮箱提供商或邮件域名下的表现。

##### ****Gmail 与 Yahoo 发件人新规 (2024年2月起强制执行)****

Google 和 Yahoo 已于 2024 年 2 月开始实施新的发件人要求。如果你发现邮件进入了垃圾邮件箱，请务必核实你是否满足以下要求：

1. 严禁在发件地址中使用 Gmail 或 Yahoo 域名

要求： 不要在“发件人地址（Friendly from-address）”中使用 @gmail.com 或 @yahoo.com。

对策： 请将发件地址切换为你自己拥有的网站域名（例如 @yourbrand.com）。

2. 设置品牌发件域名 (Branded Sending Domain)

作用： 品牌发件域名（也称为专用发件域名）能让你更好地控制发件人信誉。同时，它会移除收件箱中显示的“由 klaviyomail.com 代发（via klaviyomail.com）”的免责声明。

注意： 对于经常向 Google 和 Yahoo 用户发送邮件的大批量发件人，这已成为一项强制要求。

3. 在根域名上设置 DMARC 政策

作用： DMARC 是一种验证协议，服务器通过它确保邮件来自合法发件人，防止品牌域名被恶意冒用。

操作： 你需要在你的 DNS 供应商（如 GoDaddy 或 Cloudflare）后台进行 DMARC 配置。

4. 确保发件地址与发件域名对齐 (Domain Alignment)

要求： 为了符合 DMARC 合规性，你“发件人地址”中的域名必须与你“品牌发件域名”中的根域名保持一致（对齐）。

5. 提供便捷的退订方式

要求： 审计你的 campaign 模板和 flow 邮件，确保邮件正文（通常在页脚）中有清晰的退订链接。

6. 保持极低的垃圾邮件投诉率 (Spam Complaints)

重要性： 维持低投诉率是向邮箱提供商证明你是一个遵循 Deliverability 最佳实践的合法发件人的关键。

工具推荐： 除了查看 Klaviyo 的 Deliverability Hub，建议同时使用 Google Postmaster Tools 来监控你的发送策略是否符合 Google 的官方要求。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)