---
id: "115005081607"
title: "如何与 Help Scout 集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005081607-How-to-integrate-with-Help-Scout"
section: "Help Scout"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:19Z"
language: "zh"
---
## 你将会学到

了解如何将 Help Scout 与 Klaviyo 集成，以将有关 Help Scout 对话的导入指标同步到您的 Klaviyo 帐户中，这有助于发送有针对性的消息。 Klaviyo 的内置 Help Scout 集成完全支持 Help Scout 的邮箱 API 2.0。 Help Scout 集成每小时与 Klaviyo 同步一次。

## 启用 Help Scout 集成

1. 登录 Klaviyo 并选择****集成****选项卡。
2. 选择****探索应用程序****，搜索**Help Scout**，然后选择该卡。
3. 然后，单击****安装****。
4. 单击****连接以帮助 Scout****。然后，系统可能会提示您登录 Help Scout 帐户以完成连接。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723505995291)
5. 连接后，您将收到一条成功消息。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28723505992091)

## 如何查看从 Help Scout 同步的数据

要查看正在同步到您的 Klaviyo 帐户的帮助 Scout 指标，请单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****选项卡。从下拉列表中选择 **Help Scout** 以查看所有关联的事件。

![](https://klaviyo.zendesk.com/hc/article_attachments/36559164400155)

您可以单击任何指标来查看事件详细信息。通过选择以下任意选项来更深入地研究数据：

- ****图表****以图表形式显示数据
- ****活动源****向您显示事件的时间线，并允许您通过单击任何时间戳来深入了解元数据
- ****群组****
- ****最好的人****

所有数据均可通过单击****导出为 CSV**** 导出。

## 帮助侦察指标

以下指标会从 Help Scout 同步到您的 Klaviyo 帐户：

- 封闭式对话
- 收到回复
- 已发送消息
- 开始对话

### 封闭式对话

当与客户的对话结束时进行跟踪。 Klaviyo 跟踪的事件将包括电子邮件的主题、电子邮件发送到的邮箱以及 Help Scout 中的对话中存在哪些标签。您可以根据以下内容过滤和定位 **封闭式对话** 事件：

- ****邮箱****本次对话的Help Scout中的邮箱名称
- ****标签****每个对话中列出的 Help Scout 标签

### 收到回复

当客户从您的邮箱收到 Help Scout 票证的回复时进行跟踪。 **收到回复** 事件包括电子邮件的主题和正文。您可以根据某人是否收到回复或他们上次收到回复的时间来触发流和段。

### 已发送消息

每当客户向您的 Help Scout 邮箱发送电子邮件时都会进行跟踪。 **已发送消息** 事件包括电子邮件的主题和正文。您可以根据某人是否发送了消息、发送了多少条消息或上次发送消息的时间来触发流和段。

### 开始对话

当客户开始新对话时进行跟踪。 Klaviyo 跟踪的事件将包括电子邮件的主题、电子邮件发送到的邮箱以及 Help Scout 中的对话中存在哪些标签。您可以根据以下内容过滤和定位 **开始对话** 事件：

- ****邮箱****本次对话的Help Scout中的邮箱名称
- ****标签****每个对话中列出的 Help Scout 标签

## 监控 Help Scout 同步

您可以检查几个地方，以确保您的 Help Scout + Klaviyo 集成已启用。

1. 导航到 [集成选项卡](https://www.klaviyo.com/integrations) 并查找 Help Scout 集成。当您看到 Help Scout 集成周围出现绿色边框时，您就知道您的集成已完全同步。
2. 单击 Klaviyo 中的****分析****下拉列表，然后选择****指标****。找到 Help Scout 的 **已发送消息** 指标，然后点击 ****活动源**** 图标。
   ![已发送消息指标的 Klaviyo 活动源，包含时间戳列表和模糊的识别信息](https://klaviyo.zendesk.com/hc/article_attachments/28723505989403)
   如果您的数据集成同步已开始，您将在活动源中看到消息。这些是通过您的 Help Scout 邮箱发送的消息。

## 其他资源

- [集成同步的频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)
- [Klaviyo 和应用程序之间交换的信息类型](https://help.klaviyo.com/hc/en-us/articles/360030696012)