---
id: "360051127672"
title: "了解绝对流程时间线和重新加入拆分"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360051127672-Understanding-the-absolute-flow-timeline-and-rejoining-splits"
section: "Add steps or actions to flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:50Z"
language: "zh"
---
## 你将会学到

通过示例了解为什么在重新连接拆分时时间线可能不会出现。

流程的时间线是指一个人完成该流程需要多长时间。例如，如果您的流程延迟了两天，然后发送了一封电子邮件，则绝对时间线提示将显示两天，因为这是流程完成所需的时间。但是，此时间线可能并不总是出现，特别是当流包含重新加入的拆分时。

## 计时和重新加入拆分

可能存在分离路径具有不同时间延迟的情况。在这种情况下，当您重新加入拆分时，来自“是”和“否”路径的收件人将经历与触发器不同的绝对时间线。

在下面的示例中，有 3 条路径在重新加入后汇集在一起​​。对于以绿色突出显示的两个人，他们将在两天后重新加入后收到最终的折扣电子邮件，而来自黄色突出显示路径的人将在四天后收到相同的电子邮件，因为在此路径上设置了额外的时间延迟。

![示例流程显示如何将条件拆分重新连接到流程的单个路径。](https://klaviyo.zendesk.com/hc/article_attachments/28704477341467)

由于黄色路径的时间线不同，因此您不会在电子邮件卡右下角下方看到[绝对时间线提示](https://help.klaviyo.com/hc/en-us/articles/115003885212)。

## 其他资源

- [如何重新加入和断开流拆分](https://help.klaviyo.com/hc/en-us/articles/360002419512)
- [了解分裂附近的时间延迟](https://help.klaviyo.com/hc/en-us/articles/360050334651)