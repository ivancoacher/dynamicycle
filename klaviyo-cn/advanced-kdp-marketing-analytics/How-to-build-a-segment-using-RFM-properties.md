---
id: "18193920339483"
title: "如何使用 RFM 属性构建分段"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18193920339483-How-to-build-a-segment-using-RFM-properties"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: "zh"
---
## 你将会学到

了解如何使用 RFM 值和客户分组作为细分中的属性。在分段中使用 RFM 属性对于在营销内容中创建基于分段的推荐非常有用。例如，您可能希望为当前的一些 **有风险** 或 **不活跃** 客户提供折扣，或者与最近组中的客户使用交叉销售内容。有关如何在营销活动或流程中使用 RFM 分段的信息，请参阅我们的[策略指南](https://help.klaviyo.com/hc/en-us/articles/18194102384539)。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 和 [营销分析](https://help.klaviyo.com/hc/en-us/articles/33789259613595) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。前往我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672) 了解如何购买这些计划。 ## 最近的报告更新（截至 2024 年 5 月 2 日）

自 2024 年 5 月 2 日起，RFM 报告正在推出新的属性和设置。请查看以下有关使用高级 KDP 的[现有](#h_01HWWHY499J0M3QFMVG16Z3ZWY) 和[新](#h_01HWWJ5KRZPD5X16RWRMN70BWQ) 客户的信息。 ### 使用高级 KDP 的现有客户

#### 配置文件属性更改

RFM 报告将具有 3 个新属性。下图中显示的前 2 个属性可以在段中使用。从 2024 年 5 月 2 日开始，Klaviyo 将推出下表所示的新属性。然后在 5 月 21 日，Klaviyo 将自动更新您的分段以使用这些新属性并删除旧属性值。建议您在 21 日之前，使用旧属性手动调整任何项目（例如，在报告、流程、模板、表单等中）。 | ****旧房产**** | ****新房产**** | ****它测量什么？**** | ****其他注意事项**** |
| --- | --- | --- | --- |
| **$当前\_月\_rfm\_group** | **现任 RFM 小组** |配置文件当前所属的 RFM 组。 |  |
| **$前\_月\_rfm\_group** | **前 RFM 小组** |最近的**不同** RFM 组，该配置文件属于其当前 RFM 组之前的组。 |在配置文件的 RFM 组发生更改之前，其**之前的 RFM 组**将显示为 **未知********。**** |
|不适用 | **RFM 组最后更改** |配置文件从 **前一个 RFM 组** 转换到 **当前 RFM 组** 的时间戳。仅当配置文件更改其 RFM 组时才会出现此情况。 |  |

#### 当配置文件属性刷新时

此外，RFM 属性每晚都会刷新，而不是每月 1 号。这意味着 Klaviyo 将每 24 小时检查一次更新，如果配置文件上的这些 RFM 属性已更改，您将看到这些更改得到反映。请记住，RFM 仪表板会立即更新，而配置文件记录的更改每 24 小时更新一次。因此，您可能会在仪表板中看到每个 RFM 组的数字差异，但这些差异尚未反映在您的配置文件中。 ### 使用高级 KDP 的新客户

在 2024 年 5 月 2 日或之后刚刚加入高级 KDP 的新客户无需担心过渡到新的配置文件属性，因为这些属性已经成为标准。此外，请记住，在入职或更新 RFM 模型时，当模型计算 **当前 RFM 组** 并检测先前状态时，您可能会看到 **先前 RFM 组** 的 **未知** 状态。 ## 设置具有 RFM 属性的段

从内部 **RFM 分析**：

1. 如果您是高级 KDP 客户，请导航至****高级 KDP > 智能 > 客户洞察 > RFM 分析****。或者，如果您是 Marketing Analytics 客户，请导航至****Marketing Analytics > 客户洞察 > RFM 分析****。 2. 滚动找到 **RFM 分段** 卡，然后单击 ****创建分段****。 ![分段构建按钮.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705699287579)
3. 进入细分生成器后，为您的细分命名并从 **标签** 下拉列表中添加任何适用的标签。 4. 在 **定义** 下拉列表中，选择 ******关于某人的属性******。 5. 在 **Dimension** 下拉列表中，查找或使用两个 RFM 选项之一：
   ******当前 RFM 组******
   配置文件当前所属的 RFM 组。 ******前 RFM 组******
   最近的**不同** RFM 组，该配置文件属于其当前 RFM 组之前的组。 6. 使用**等于**下拉列表使 RFM 等于或不等于某个组。例如，您可以使用**不等于冠军**来定位除**冠军**之外的所有客户群体。详细了解[分段条件及其使用方法](https://help.klaviyo.com/hc/en-us/articles/115005062847#segment-conditions1)。 7. 使用维度值查找并选择特定客户 RFM 组。默认情况下，数据输出**类型**将为**文本**。将其保留为**文本**，以便该属性正常工作。您还可以选择使用[**和**](https://help.klaviyo.com/hc/en-us/articles/360036534631)[或](https://help.klaviyo.com/hc/en-us/articles/360036534631) [**或**](https://help.klaviyo.com/hc/en-us/articles/360036534631) [连接器](https://help.klaviyo.com/hc/en-us/articles/360036534631) 进一步定制您的细分。例如，您可能只想定位 **不活跃** 和 **有风险** 群体。 8. 分段完成后，单击****创建分段****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28705699290011)