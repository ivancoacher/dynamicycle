---
id: "115002779491"
title: "排查为何在流程中多次安排配置文件的原因"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002779491-Troubleshooting-why-a-profile-is-scheduled-in-a-flow-multiple-times"
section: "Troubleshooting flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:38Z"
language: "zh"
---
## 你将会学到

了解如何对同一个人多次排队接收流的情况进行故障排除。这些配置文件可能已多次采取触发操作。例如，某人可能连续多次购买或在同一浏览会话中查看了多个产品。

## 使用智能发送来限制消息频率

[智能发送](https://help.klaviyo.com/hc/en-us/articles/115002779311-Smart-Sending-for-Flows-VFB-)，如果启用，将确保没有人在既定的智能发送期间（默认情况下分别为 16 小时和 24 小时）收到超过一封电子邮件或短信。当您的流程是由常见的重复行为（例如查看产品或在网站上活跃）触发时，我们强烈建议您保持启用智能发送。

## 使用额外的过滤器来限制消息频率

如果您想禁用某个流的智能发送，并且担心在短时间内向某人发送多封电子邮件或文本，您还可以[对您的消息使用附加过滤器](https://help.klaviyo.com/hc/en-us/articles/115002779091-Add-an-Additional-Filter-to-a-Single-Flow-Email-VFB-)，以限制某人从该流接收消息的频率流动。这个过滤器应该是：

**某人做过或没做过的事情 > 收到的电子邮件 > 地点 > 主题 > 等于 > INSERT\_EMAIL'S\_SUBJECT > 零次 > 在过去 > X 天**

确保将 INSERT\_EMAIL'S\_SUBJECT 替换为电子邮件的实际主题行，将 X 替换为您要使用的天数。

![](https://klaviyo.zendesk.com/hc/article_attachments/34263477109019)

## 使用配置文件过滤器来限制消息频率

或者，您可以向整个流程添加过滤器，以限制某人进入该流程的频率。为此，请添加以下配置文件过滤器：

**未曾在此流程中 > 跳过过去 X 天内曾在此流程中的任何人**

![](https://klaviyo.zendesk.com/hc/article_attachments/34263477113115)

确保将 X 替换为您要使用的天数。

此选项不适用于基于列表和分段的流，因为它们仅针对每个收件人触发一次。

## 其他资源

了解有关流程的更多信息：

- [如何预览流量触发设置](https://help.klaviyo.com/hc/en-us/articles/360028374111)
- [理解流分支](https://help.klaviyo.com/hc/en-us/articles/115003883992)

了解[流程故障排除](https://klaviyo.zendesk.com/hc/en-us/articles/115002779471)。

了解更多关于[Klaviyo中的智能发送](https://help.klaviyo.com/hc/en-us/articles/115002779311)。