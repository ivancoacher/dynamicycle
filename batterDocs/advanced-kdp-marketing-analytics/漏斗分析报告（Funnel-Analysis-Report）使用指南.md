---
id: 6364
title: "漏斗分析报告（Funnel Analysis Report）使用指南"
slug: "getting-started-with-the-funnel-analysis-report"
category: "核心数据与分析（Advanced KDP &amp; Marketing Analytics）"
category_slug: "advanced-kdp-marketing-analytics"
wp_url: "https://dynamicycle.com/docs/getting-started-with-the-funnel-analysis-report/"
wp_modified: "2026-01-09T08:38:00"
---

您将学习如何使用 funnel analysis reporting（漏斗分析报告）来回顾客户在您的品牌中的旅程，以及他们在行动或转化前可能在何处流失。了解客户可能流失的位置有助于您判断应在哪些地方优化营销漏斗。

##### 访问仪表板

- 如果将是 Advanced KDP 客户，请前往：Advanced KDP → Intelligence → Customer Insights → Funnel analysis

- 如果将是 Marketing Analytics 客户，请前往：Marketing Analytics → Customer Insights → Funnel analysis

- 如果这是将第一次创建漏斗分析，请点击如下所示的 “Create funnel”。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/create-funnel.jpg?resize=857%2C595&ssl=1)

注：您在每个账户中只能创建 1 个漏斗仪表板，该仪表板最多可包含 10 个漏斗分析卡片。在接下来的步骤中自定义仪表板时，您将不断向这个唯一的仪表板中添加漏斗卡片或图表。

##### 自定义并添加漏斗分析卡片

创建新卡片或漏斗图表时，您可以选择命名卡片（请注意，这将应用于仪表板中的每个单独的卡片或图表），根据需要按特定 segment（细分群组）进行筛选，并添加特定的 metric （指标）步骤或操作。

您还可以选择为每个步骤添加额外的筛选条件，以聚焦更具体的客户子集。这些选项位于点击 “Create funnel” 后屏幕右侧出现的设置菜单中，如下图所示。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/settings-menu-new.jpg?resize=309%2C1024&ssl=1)

###### ****1. 命名你的卡片****

为您的卡片起一个能识别您要查看的客户旅程的名称。例如，“过去 90 天内未购买的新客户”。

###### 2. 按客户segment筛选

接下来，您可以选择 1 个 segment 进行筛选。这在您希望聚焦某一特定客户群体及其行为时非常有用。

打开 “Filter by segment (optional)” 下拉菜单，从按字母顺序排列的列表中选择您的 segment，或者在 Filter 字段中搜索。

****注意****：不需要必须为您的 funnel card 选择特定的 segment。如果您不选 segment，漏斗分析将在您选择的时间范围和漏斗设置下查看所有个人档案（profiles）。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/filter-by-menu.jpg?resize=700%2C418&ssl=1)

###### 3. 设置完成时间窗口

下一步，您可以选择指定正在创建的漏斗的第一步和最后一步之间的最大时间间隔。

打开 “Days” 下拉菜单，选择 Hours（小时）、Days（天）或 Weeks（周），然后在左侧字段中输入一个整数。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/completion-window.jpg?resize=675%2C387&ssl=1)

然后，您将进入配置漏斗步骤或事件的部分，并查看客户可能在旅程的何处流失。

****重要提示****：这些步骤必须按正确的逻辑顺序排列，从第一步开始，以确保您能准确捕捉到客户在漏斗中的移动。例如，将像 Started checkout（开始结账）这样的转化指标放在像 Active on site（活跃在网站上）这样的指标之前，可能会产生不准确的数据，因为您可能没有遵循最合乎逻辑的行动顺序。此外，某些指标组合（例如 Klaviyo 事件与电商事件混合使用）也可能会产生人为的数据下降和不准确的结果。

###### 4. 选择 Metric 事件

打开 “Metric”（指标）下拉菜单，从按字母顺序排列的列表中选择您的 Metric 事件，或者在筛选字段中搜索。此列表将包含所有 Klaviyo 事件以及您电商集成中的任何事件。

###### 5. 添加更多步骤

如果您想添加超过要求的 2 个步骤，请点击 “Add Step”（添加步骤）。

- 创建漏斗至少需要 2 个 Metric 事件
- 最多可添加 5 个 Metric 事件
- 你可以通过点击右上角的垃圾桶图标删除某一步骤

在每个步骤下方，您可以选择添加筛选条件以进一步细化您的客户子集。例如，如果您正在分析复购客户，您可以按 Country（国家）添加筛选条件，查看订单主要来自哪些地区。

###### 6. 为步骤添加筛选条件

打开 “Select an additional filter”（选择额外过滤器）下拉菜单，从列表中选择您的 Metric 事件或进行搜索。

###### 7. 为筛选条件选择具体值

如果您添加了筛选条件，则必须为其指定一个值。

值与您选择的 Metric 和筛选类型相关。例如，如果您选择非转化指标 Active on site，并将筛选条件设为 Attributed Message（归因消息），您将看到用于从值下拉列表中选择特定归因消息的选项。

打开 “Select a value”（选择一个值）下拉菜单，从列表中选择或进行搜索所需值。

###### 8. 创建漏斗

当您对漏斗设置满意后，点击 “Create”（创建）。

###### 排查潜在的卡片错误

若您的漏斗已成功创建，您将看到新卡片出现在仪表板顶部。

- 如果您收到错误消息提示 **“Your funnel could not be saved”**（您的漏斗无法保存），请刷新页面并重试。
- 如果您收到 **“Something went wrong”**（出了点问题）的消息，这意味着数据当前不可用。您需要手动刷新页面，看看数据现在是否加载。
- 此外，您可能会收到卡片错误，指出您使用的是已失效的 segment，或者一个或多个 Metric 事件已被删除。遇到此情况，请刷新整个页面或根据需要调整漏斗，然后点击 “Create” 保存这些更改。

注：在某些情况下，即便漏斗成功创建，某些步骤的数值也可能异常偏低或不准确。这通常与某些指标组合方式有关（例如 Klaviyo 事件与电商事件混合）。有关这些潜在问题的更多说明，请参阅我们的[漏斗分析故障排查指南](https://help.klaviyo.com/hc/en-us/articles/17797984549659)。

##### 查看分析结果

漏斗卡片创建后，将出现在仪表板顶部。如果需要，您随时可以调整卡片的顺序。下面是一个包含 5 个步骤的漏斗卡片示例。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/mceclip1.png?resize=1024%2C440&ssl=1)

根据您添加的步骤数量，每张卡片都会按从左到右的顺序，显示对应步骤的柱状图。

- 最左侧的第一根柱子，表示在当前报告时间范围内，符合第一个 Metric 事件的客户总数（显示为顶部数值和柱形高度）。
- 后续每一根柱子，表示在第一步客户总数的基础上，完成该步骤的客户数量（显示为顶部数值、百分比和柱形高度）。

例如，在上述示例中：

- 有 18,138 位客户收到了邮件
- 其中 14,336 位打开了邮件
- 在这 18,136 人中，有 3,773 人点击了邮件
- 随后有 1,154 个用户将商品加入购物车
- 最终有 662 个用户完成下单

您还可以通过将鼠标悬停在卡片中的任何柱状子上，查看从第一步到该步骤的整体完成率。

##### 编辑卡片

- 如需编辑卡片，找到您想要调整的漏斗卡片或图表，然后点击 “Edit”（编辑）。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/edit-button-on-card-1.jpg?resize=1024%2C459&ssl=1)

- 设置菜单将从右侧出现，根据需要修改您的漏斗步骤或设置。
- 对编辑满意后，点击 “Save”（保存）。

如果您进行了编辑但未点击 “Save”，系统会提示您放弃更改，或者取消操作并返回继续编辑以保存更改。

##### 克隆您的漏斗

您还可以克隆漏斗，以便在无需从头开始重新创建漏斗的情况下快速迭代。要克隆现有漏斗，请点击操作菜单（即 3 个点的菜单），然后选择 “Clone”（克隆）选项。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/mceclip0.png?resize=1024%2C433&ssl=1)

这将复制您的漏斗，以便您在保留原始漏斗的同时进行更改。

##### 自定义主仪表板视图

除了自定义每个单独卡片的设置外，您还可以自定义整个仪表板本身的设置。

##### 调整仪表板时间范围

默认情况下，漏斗仪表板和所有卡片将使用 Last 7 days（过去 7 天）作为时间范围。

但是，您可以将其调整为以下选项：

- Last 7 days（过去 7 天）
- Last 30 Days（过去 30 天）
- Last 90 Days（过去 90 天）
- Last 365 Days（过去 365 天）
- Week-to-date（本周至今）
- Month-to-date（本月至今）
- Year-to-date（年初至今）
- Custom（自定义，选择您自己的开始和结束日期）

调整方法：

1. 点击报告顶部的时间范围下拉菜单。
2. 选择您想要的时间范围。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/timeframe-dropdown.jpg?resize=288%2C128&ssl=1)

您选择的任何时间范围都会更新整个仪表板。请注意，只有同时满足以下条件的用户才会显示在卡片中：

- 符合漏斗第一步事件条件
- 且发生在你所选的时间范围内

##### 调整仪表板顺序

如需调整卡片顺序，请点击并按住卡片顶部的点状图标，然后将卡片拖拽到你希望的位置。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)