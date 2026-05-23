---
id: "360049849432"
title: "如何对流程分支进行 A/B 测试"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360049849432-How-to-A-B-test-flow-branches"
section: "Test and optimize flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-22T10:29:57Z"
language: "zh"
---
## 你将会学到

了解如何使用条件拆分组件对流程分支进行 A/B 测试，以测试流程中的时间、折扣和电子邮件数量等内容。在本文中，我们将介绍如何设置和结束流程分支的 A/B 测试。

您还可以对单个流电子邮件进行 A/B 测试。请阅读[如何对电子邮件进行 A/B 测试](https://klaviyo.zendesk.com/hc/en-us/articles/6960371049115) 获取指导。

## 设置测试分支

1. 在 ****Flows**** 选项卡中导航到您想要进行 A/B 测试的流程。
2. 将条件拆分拖动到您想要开始 A/B 测试的位置。
3. 配置分割时，选择****随机样本****作为条件。在这里，系统将提示您选择有多少百分比的受众将走“是”路径，您可以将其视为控件。
4. 对于均匀的 A/B 测试，请选择 50%。否则，单击下拉菜单选择不同的百分比。

拆分将为每个配置文件随机选择一个分支。因为这是完全随机的，所以您可能不会在每个分支中看到完全均匀数量的配置文件（分割比例为 50%），但它会很接近。

例如，您可能想测试向欢迎系列的一个分支发送一封额外的电子邮件。为此，您可以将拆分拖动到流程的末尾，添加时间延迟，然后配置电子邮件内容。

![](https://klaviyo.zendesk.com/hc/article_attachments/46986105243931)

配置好拆分后，您就可以构建测试分支的内容。根据您正在测试的内容，这可能是多封电子邮件或与您控制分支中的时间不同的时间。

运行 A/B 测试时，请记住，一次测试多个变量可能会导致结果出现偏差，并且很难确定如何归因收入、打开率等方面的差异。因此，最佳做法是在确定获胜者后一次测试一个变量。

Apple Mail Privacy Protection (MPP) 随 iOS15 和其他 Apple 设备的更新一起发布，由于我们接收打开率数据的方式发生变化，可能会导致打开率过高。

如果您要触发打开本身的流量，我们建议创建一个[自定义报告](https://help.klaviyo.com/hc/en-us/articles/4416803987739)，其中包含 MPP 属性来查看这些受影响的打开。您还可以在您的个人[订阅者细分](https://help.klaviyo.com/hc/en-us/articles/4416791883163)中识别这些开放。

## 确定最佳分支

要确定最佳时间延迟，请查看每条消息的分析。根据流量，根据打开率、点击率、转化率来决定哪个分支最好。

要快速查看流中消息的流分析：

1. 单击右下角工具栏上的****显示分析****图标按钮
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46986105248155)
2. 查看每个流分支中的消息指标并决定您喜欢哪个分支。
   ![显示不同流路径中并排的两条消息的消息性能指标。](https://klaviyo.zendesk.com/hc/article_attachments/28711678107547)

请阅读我们关于[了解流量分析](https://help.klaviyo.com/hc/en-us/articles/115002779351)的文章了解更多信息。

## 结束 A/B 测试

在决定哪个分支更适合您的受众之后：

1. 单击条件分割。
2. 要让所有收件人都选择“是”路径，请将百分比设置为 100%；如果您希望每个人都走“否”路径，请将其设置为 0%（如下例所示）。这样，那些已经在 **等待** 队列中的人仍然会收到旧消息，而不是像删除分支一样被从流中取出。
3. 在不再使用的分支中，将消息设置为 **草稿**。

![](https://klaviyo.zendesk.com/hc/article_attachments/46986105251227)

## 其他资源

- [如何对流程电子邮件进行 A/B 测试](https://help.klaviyo.com/hc/en-us/articles/6960371049115)
- [了解 A/B 测试的最佳实践](https://help.klaviyo.com/hc/en-us/articles/360045012632)
- [掌握电子邮件 A/B 测试：Klaviyo 经验证的提高收入的提示和技巧](https://www.klaviyo.com/blog/ab-testing-email)