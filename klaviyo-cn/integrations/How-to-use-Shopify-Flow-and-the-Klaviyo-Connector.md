---
id: "360014410811"
title: "如何使用 Shopify Flow 和 Klaviyo Connector"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360014410811-How-to-use-Shopify-Flow-and-the-Klaviyo-Connector"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:43Z"
language: "zh"
---
了解如何将 Klaviyo 连接器与 Shopify Flow 结合使用来跟踪事件（将数据从工作流程发送到 Klaviyo）。 ## 开始之前

如果您尚未阅读我们的 [Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) 指南，了解有关集成的分步说明，然后再继续阅读本文。 ## 什么是 Shopify Flow？ Shopify Flow 是一个电子商务自动化平台，Shopify 商店可以使用它来自动执行常见任务，例如：

- 标记高价值客户
- 标记和取消高风险订单
- 当您的库存水平变低时发送重新订购请求
- 根据标题或 SKU 识别产品并向其添加标签

Shopify Flow 是 Shopify 在其 App Store 中提供的应用程序，适用于 Shopify 套餐及以上套餐（不适用于基本套餐）。您可以[在 Shopify 的应用商店](https://apps.shopify.com/flow) 访问该应用，并且应在按照本文中的步骤进行安装之前安装它。对于使用 Flow 的 Shopify 商家，有许多资源可用于了解 Flow 的功能，以及您可以下载并导入商店的工作流程：

1. [Shopify 帮助中心文档中的工作流程示例](https://help.shopify.com/en/manual/shopify-plus/flow2/reference/examples)
2. [14 个顶级工作流程博客文章](https://www.shopify.com/enterprise/ecommerce-automation-software-shopify-flow)

## 我可以使用适用于 Shopify Flow 的 Klaviyo 连接器做什么？ Shopify 连接器是一项功能，允许 Shopify 商店创建第三方合作伙伴构建的应用触发器和操作。 Klaviyo 连接器支持跟踪事件操作：

- 此操作将数据从您的工作流程发送到 Klaviyo 以便其跟踪。 - ****示例工作流程****当客户的忠诚度等级发生变化时，您可以在 Klaviyo 中跟踪此变化。 - ****它是如何工作的****
    1. 当客户提升忠诚度等级时，LoyaltyLion 会触发此工作流程。 LoyaltyLion 将等级信息发送到 Shopify Flow。 2. Shopify Flow 将有关客户的数据发送到 Klaviyo 以跟踪事件，并将有关客户的数据发送到 LoyaltyLion 以添加客户忠诚度帐户的奖励积分。 ## 如何使用 Klaviyo 连接器

在 Shopify 流程中，您可以将操作添加到工作流程中。 1. 在****选择操作****菜单中，您可以从 Shopify 开发的 **标准操作** 或第三方应用程序开发的附加操作中进行选择。您可以在此处找到 Klaviyo 连接器（如果已安装）。 2. Klaviyo 连接器中可用的操作是 ****跟踪事件********.********![屏幕截图 2025-10-16 at 9.17.20AM.png](https://klaviyo.zendesk.com/hc/article_attachments/42182674738075)****

### 跟踪事件

选择****跟踪事件****操作后，您需要填写以下字段：

- ****Klaviyo 公共 API 密钥****了解如何[在 Klaviyo 中查找您的公共 API 密钥](https://help.klaviyo.com/hc/en-us/articles/115005062267-How-to-manage-your-account-s-API-keys#find-your-api-keys2)。 - ****事件名称****您要跟踪的事件的名称。这将显示在客户档案的事件时间线上。 - ****客户电子邮件地址****正在经历流程的人员的电子邮件，其活动将在 Klaviyo 中进行跟踪。 - ****客户名字****正在经历流程的人员的名字，其活动将在 Klaviyo 中进行跟踪。 - ****客户姓氏****正在经历流程的人员的姓氏，其活动将在 Klaviyo 中进行跟踪。 - ****客户属性****客户属性的哈希字典将作为自定义字段包含在其 Klaviyo 配置文件中。 ![包含名字和拥有帐户的客户属性框，以及包含价值、商品数量和总折扣的事件属性框](https://klaviyo.zendesk.com/hc/article_attachments/28717992039707)
- ****事件属性****有关此事件的自定义信息的哈希字典。请务必注意，作为列表发送的任何内容（例如客户或事件属性）都需要格式化为 JSON 列表才能在 Klaviyo 中正确显示。例如，您可以按以下方式格式化客户标签：
`{"tags": [{% fortags_item in customer.tags%}{% if forloop.first != true %},{% endif %}{{tags_item | json}}{% endfor %}]}`

这些事件将在 Klaviyo 中作为 Shopify 事件进行跟踪，如每个事件旁边的 Shopify 图标所示。要查看您的 Shopify Flow 事件数据：

1. 单击 Klaviyo 中的****分析****下拉列表并选择****指标****
2. 从下拉菜单中选择****Shopify****。该选项卡将仅显示从 Shopify 同步的事件。 ![Klaviyo 中的 Shopify 指标时间表，其中包括取消 VIP 状态和检测到信用卡欺诈等指标](https://klaviyo.zendesk.com/hc/article_attachments/28717992047899)

### 创建活动

“创建营销活动”操作已于 2025 年 10 月 16 日停用。#### 我如何复制“创建营销活动”功能？我们建议更新您的工作流程以使用“[跟踪事件](https://help.klaviyo.com/hc/en-us/articles/360014410811#h_01HCFKXSHCSG8M2RN0EESGVTVY)”操作。此操作允许您创建从 Shopify 到 Klaviyo 的数据，然后可以使用这些数据触发流程或为营销活动构建细分。 1. 在您的 Shopify 流程中，删除“创建广告系列”操作。 2. 在其位置添加“跟踪事件”操作以创建 Klaviyo 的相关客户数据。 3. 在 Klaviyo 中，您可以使用此新事件作为流程的触发器，或基于它创建分段，以针对正确的受众创建营销活动。 ## 故障排除

### 您的数据是否未按预期在 Klaviyo 中显示？确保“客户属性”框和“事件属性”框是有效的 JSON。如果输入不是有效的 JSON，“跟踪事件”步骤将不会按预期将数据传递到 Klaviyo。例如，您的数据变量可能包括 for 循环语句。当计算 for 循环语句时，由于变量存在于 for 循环语法中的新行，它们可能会留下尾随空格：

````
“{% for lineItems_item in order.lineItems %}
{{lineItems_item.name}}
{% endfor %}"
````

由于它是无效的 JSON，因此 Klaviyo 不会摄取它。要解决此问题，请删除 for 循环语法之间的换行符，如下所示：

````
“{% for lineItems_item in order.lineItems %}{{lineItems_item.name}}{% endfor %}”
````

## 结果

您现在已经了解了如何将 Klaviyo Connector 与 Shopify Flow 结合使用来跟踪事件。 ## 其他资源

- [Shopify 入门](https://klaviyo.zendesk.com/hc/en-us/articles/115005080407)
- 详细了解 [Shopify 帮助中心上的连接器](https://help.shopify.com/en/manual/shopify-flow/reference/connectors)