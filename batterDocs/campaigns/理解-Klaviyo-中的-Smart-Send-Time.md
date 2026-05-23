---
id: 7058
title: "理解 Klaviyo 中的 Smart Send Time"
slug: "smartsendtime"
category: "活动与营销（Campaigns）"
category_slug: "campaigns"
wp_url: "https://dynamicycle.com/docs/smartsendtime/"
wp_modified: "2026-02-26T06:36:22"
---

##### Klaviyo 发送时间优化模型的独特之处

虽然许多公司都具备发送时间优化功能，但 Klaviyo 的模型与众不同。Klaviyo 不通过隐藏的公式来确定您业务的发送时间，而是使用一个强大的测试框架来收集客户数据，从而弄清楚他们最有可能在何时打开您的邮件。为了保证透明度，您的测试结果将始终对您可见。

##### 何时应使用 Smart Send Time

虽然了解最佳发送时间很重要，但战略性地使用此功能至关重要。由于我们是根据 ****Recipient****（收件人）的当地时间进行发送，因此请****避免****发送具有强时效性的内容，例如闪购活动或即将到期的截止日期通知。相应地，您不应在重大节日或对您品牌具有重要意义的日期前后进行 Smart Send Time 测试。

##### 如何利用 Smart Send Time

您可以从 ****Campaign**** 向导或 Smart Send Time 报告页面创建测试。您也可以创建多个 Smart Send Time 测试；但请注意，Smart Send Time 仅适用于 Email。

Klaviyo 的 Smart Send Time 测试是根据 ****Recipient**** 的时区进行发送的。如果 Klaviyo 无法确定某个 ****Recipient**** 的时区，邮件将根据您在账户层级（Account Level）选择的时区进行发送。

##### 探索阶段发送 (Exploratory send)

在此阶段，Klaviyo 将在 24 小时内发送邮件。客户会被随机分配到该时段内的某个时间点。所有邮件都将按 ****Recipient****（收件人）的当地时间发送。例如，如果您处于东部标准时间（EST），而一名处于中部标准时间（CST）的订阅者被分配在上午 10 点接收邮件，那么该用户将在 CST 时间上午 10 点收到邮件。

![电子邮件发送设置界面，包含发送选项和日期选择。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-41.png?resize=1024%2C684&ssl=1)

如果您计划在今天进行探索阶段发送，它将在下一个小时整点开始发送（例如，如果您在下午 2:45 计划了任务，第一批邮件将在下午 3:00 开始发送）。如果您计划在未来的某个日期进行探索阶段发送，第一批邮件将在您账户本地时区的凌晨 12:00 开始发送。

您发送的邮件应当是受众覆盖面广且非时效性的邮件（例如：每周通讯）。此外，建议考虑关闭 ****Smart Sending****（智能发送过滤），以确保名单上的所有人都有机会打开您的邮件。如果您在相近的时间窗内还发送了其他 ****Campaign****，请考虑对那些非 Smart Send Time 的邮件开启智能发送过滤，或安排在不同日期发送。

为了缩短并锁定最有效的时间窗，该模型需要大量数据。根据您平时的 ****Recipient****（收件人）数量大小，您可能需要多次执行 Smart Send Time 的这一部分操作。

| ****Recipients（收件人数量）**** | ****所需 Exploratory Sends（探索发送）次数**** |
| --- | --- |
| < 12,000 | 不符合资格 (Not eligible) |
| 12,000 – 17,999 | 4 – 5 次 |
| 18,000 – 23,999 | 3 – 4 次 |
| 24,000 – 47,999 | 2 – 3 次 |
| 48,000 – 71,999 | 1 – 2 次 |
| > 72,000 | 1 次 |

如果您运行了探索阶段发送（Exploratory send），但结果出现偏差（可能是由于节假日或纯粹的时机不佳），您可以申请删除历史 Smart Send Time 数据。

##### 聚焦发送 (Focused send)

在探索发送阶段结束后，Klaviyo 会确定一个聚焦发送时间（即参与度最高的时间点）。

在第二个阶段，Klaviyo 会持续验证从探索发送结果中确定的时间，并根据客户行为的任何变化进行优化。

![一个电子邮件营销工具的界面，用户可以选择安排或立即发送营销活动。界面包含日期、发送类型和测试名称的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-42.png?resize=1024%2C689&ssl=1)

在进行聚焦发送（Focused send）时，1 封邮件会在最佳发送时间发送，另外 2 封邮件则在最佳发送时间的 2 小时窗口内发送；所有邮件均按 ****Recipient****（收件人）的当地时间发送。

例如，如果模型认为上午 7 点是您的最佳发送时间，您的 ****Recipients**** 将被分为 3 组。A 组在当地时间上午 5 点收到邮件，B 组在上午 7 点收到，C 组在上午 9 点收到。

##### 最佳发送 (Optimal send)

一旦确定了最佳发送时间，您就可以开始将其用于发送 ****Campaign****。最佳发送时间适用于任何规模的 ****Audience****（受众）。

选择此选项后，Klaviyo 会在 ****Recipient**** 当地时区的特定时间发送您的 ****Campaign****。

因此，****Campaign**** 的发送过程最长可能持续 24 小时。请注意，此时产生的表现数据不会影响您的最佳发送时间，因为邮件在每个时区仅在一个特定的时间点发送。由于所有 ****Recipients**** 都在同一时间（例如晚上 10:00）收到消息，Klaviyo 没有其他时间点可以用来进行表现对比。因此，Klaviyo 无法学习到任何新数据来更新 Smart Send Time 模型或最佳发送时间。

![调度或发送选项图示，包括选择未来日期和立即发送的相关信息](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-43.png?resize=1024%2C689&ssl=1)

##### Smart Send Time 报告

Smart Send Time 报告允许您查看实验的详细信息，例如实验当前所处的阶段以及上一次发送 ****Campaign**** 的时间。您还可以查看结果概览。图表显示了与该实验相关的所有 ****Campaign**** 在每小时内的打开率。

![每小时的打开率统计图，显示各个时间段的邮件打开率变化，最高值达到24.54%。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-44.png?resize=1024%2C369&ssl=1)

您还可以查看单个 ****Campaign**** 的表现，并了解其在测试过程中的表现情况。

##### Smart Send Time 常见问题 (FAQs)

###### ****为什么我看不到使用 Smart Send Time 的选项？****

Smart Send Time 的探索阶段（Exploratory）和聚焦阶段（Focused）发送仅适用于收件人数量超过 12,000 人的 ****Campaign****。

###### ****我已经向 12,000 名收件人发送了 5 次探索邮件，但仍然看不到聚焦发送的选项。这是为什么？****

对于发送的每封邮件，Klaviyo 会自动跟踪转化情况，即收件人打开邮件并在转化期内采取了进一步行动（如下单）。发送时间模型会等到转化期结束后，才记录会影响理想发送时间的结果。默认情况下，转化期为 5 天，但您可以在账户设置中更改此窗口。

###### ****我每次进行探索发送时都必须使用同一个列表吗？****

不需要，您可以使用不同的列表。如果您想为特定群体（例如仅限美国客户）找到最佳发送时间，则不应加入其他群体，否则会使结果产生偏差。但是，如果您想了解整个客户群的最佳发送时间，可以包含所有的列表（Lists）和 ****Segment****。

###### ****我可以同时发送多封使用 Smart Send Time 的邮件吗？****

可以，您可以根据需要发送任意数量的邮件。但您仍应按照正常的发送频率进行。例如，如果您通常每周发送一次邮件，不要为了让模型运行得更快而增加发送频率，这会使您的结果产生偏差。

###### ****在使用 Smart Send Time 时可以进行 A/B 测试吗？****

您一次只能测试一个变量。因此，您无法对 Smart Send Time 邮件进行 A/B 测试。

###### ****在确定真正的最佳发送时间之前，我需要进行多少次聚焦发送？****

一旦模型拥有足够的数据允许您发送聚焦邮件，就可以确定所建议的时间就是您的最佳发送时间。聚焦发送的作用是：如果您的客户行为发生变化，模型将持续验证并微调该时间。

###### ****Smart Send Time 与 Smart Sending（智能发送过滤）有何不同？****

Smart Send Time 是一系列测试，旨在让您了解发送给客户的最佳时间。而 Smart Sending 则是为了防止您在短时间内向客户发送过多的邮件。

###### ****为什么某个 Campaign 无法用于更新发送时间？****

作为分析过程的一部分，Klaviyo 会检查使用 Smart Send Time 发送的每个 ****Campaign**** 是否具有有效数据。例如，如果在发送时，聚焦发送的目标 ****Segment**** 仅包含两名收件人，系统将仅发送两个版本而非三个，该 ****Campaign**** 将从分析中移除。这可以确保排除异常值对 Smart Send Time 的干扰。您无需采取任何行动，Klaviyo 会自动将后续有效的 ****Campaign**** 纳入分析，以便您继续使用 Smart Send Time 进行发送。

****Campaign 被排除的常见原因包括：**** 由于 ****Smart Sending**** 导致的收件人数量不均、分析数据延迟、发送时收件人 ****Segment**** 规模非常小。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)