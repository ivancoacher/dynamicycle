---
id: "360003124151"
title: "切换电商平台后如何更新Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360003124151-How-to-update-Klaviyo-after-switching-ecommerce-platforms"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:42Z"
language: "zh"
---
## 你将会学到

了解当您从一个电子商务平台切换到另一个电子商务平台时需要更新的 Klaviyo 领域。完全可以在保留相同的 Klaviyo 帐户的情况下切换电子商务平台，但需要记住一些重要步骤，以确保您的注册表单、流程和其他 Klaviyo 功能继续按预期运行。 ## 1.迁移历史数据

### 电子商务平台之间

在将新的电子商务平台与 Klaviyo 集成之前，请确保您已将所有历史购买数据从旧的电子商务平台完全迁移到新的电子商务平台。这将确保您在 Klaviyo 中的报告保持一致，并且您不必在 Klaviyo 细分和流量中引用两个电子商务平台的指标。 ### 从您的电子商务平台到 Klaviyo

如果您需要将历史购买数据直接从以前的电子商务平台添加到 Klaviyo，而 Klaviyo 没有预先构建集成，[您可以按照以下步骤手动将事件数据添加到 Klaviyo。](https://help.klaviyo.com/hc/en-us/articles/115005081247-How-to-Manually-Import-Historical-Event-Data)

## 2. 与您的新平台集成

对于我们的每个内置电子商务集成，我们都有相应的文档。找到适合您的新平台的说明后，您可以进行集成，新的指标将开始填充到您的帐户中。 - [Shift4Shop（以前的 3dcart）](https://help.klaviyo.com/hc/en-us/articles/115005083107-Integrate-with-3dcart)
- [BigCommerce](https://help.klaviyo.com/hc/en-us/sections/115001509808-BigCommerce)
- [Magento 1](https://help.klaviyo.com/hc/en-us/articles/115005082187-Integrate-with-Magento-1-x-CE-and-EE-)
- [Magento 2](https://help.klaviyo.com/hc/en-us/articles/115005254348-Integrate-with-Magento-2-x-CE-and-EE-)
- [Mi9](https://help.klaviyo.com/hc/en-us/articles/360020156011-How-to-Integrate-with-Mi9)
- [OpenCart](https://help.klaviyo.com/hc/en-us/articles/115005255408-Integrate-with-OpenCart)
- [PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492-How-to-Integrate-with-PrestaShop)
- [Salesforce Commerce Cloud](https://help.klaviyo.com/hc/en-us/articles/360033744951-How-to-Integrate-with-Salesforce-Commerce-Cloud)
- [Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-Integrate-with-Shopify)
- [Spree](https://help.klaviyo.com/hc/en-us/articles/115005255448-Integrate-with-Spree)
- [Volusion](https://help.klaviyo.com/hc/en-us/articles/115005083427-Integrate-with-Volusion)
- [Wix](https://klaviyo.zendesk.com/hc/en-us/articles/6202669053723)
- [WooCommerce](https://help.klaviyo.com/hc/en-us/articles/115005255808-Integrate-with-WooCommerce)

如果您在上面没有看到新的电子商务集成，则需要[改用自定义集成](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration)。 ## 3. 确认新数据正在同步到 Klaviyo

集成新平台后，您将能够通过单击****分析****下拉列表并选择****指标****来查看两个不同商店的指标。这包括 **下订单** 和 **结帐开始** 等指标。您可能希望从旧平台[删除旧指标](https://help.klaviyo.com/hc/en-us/articles/115005076787-Managing-Metrics#how-to-delete-a-metric)，但删除指标也会从您的帐户中删除与该指标关联的所有历史数据。仅当您不想利用此历史数据（即之前的**下订单事件**），或者您已将数据从旧电子商务平台迁移到新平台时，才执行此操作。 ## 4. 设置现场跟踪

请务必遵循相应文档中列出的所有集成说明，包括在新网站上启用[现场活动和查看的产品跟踪](https://help.klaviyo.com/hc/en-us/articles/115005076767)（统称为“现场跟踪”）。 ## 5. 更新注册表单

更新您的电子商务平台的注册表单，以确保它们同步到 Klaviyo 列表。对于许多电子商务集成，这是通过启用集成时的设置来完成的。您还可以将平台的注册表单替换为 [Klaviyo 注册表单](https://help.klaviyo.com/hc/en-us/articles/360026474752-Guide-to-Creating-a-Signup-Form)。 ## 6. 克隆和更新流程

您的帐户中可能会有[指标触发的流](https://help.klaviyo.com/hc/en-us/articles/360003057151-Create-a-Metric-Triggered-Flow)，需要连接到新指标。虽然您无法直接更改流触发器，但您可以[克隆流](https://help.klaviyo.com/hc/en-us/articles/115002775032-Clone-a-Flow)并为正确的指标选择新触发器。如果任何流具有过滤器，请务必仔细检查这些过滤器是否正确映射。如果您不克隆指标触发流，则执行触发操作的新联系人将不会排队，因为不会有更多数据从您的旧平台流入 Klaviyo。如果任何电子商务指标触发的流程模板包含动态数据，则也必须更新。例如，平台 A 的废弃购物车流程中使用的模板标签将不同于平台 B 所使用的模板标签。这些流程包括：

- 废弃的购物车
- 购买后
  - 新顾客谢谢你
  - 回头客谢谢
  - 产品评论/交叉销售

使用正确的动态数据更新克隆流的最快方法是：

1. 导航至****流程****选项卡中的****浏览创意****。 ![Klaviyo 中的“流程”选项卡在列表中显示黄色状态的废弃购物车流程](https://klaviyo.zendesk.com/hc/article_attachments/28717380554907)
2. 选择您想要重建的流程。如果您要迁移到平台 B，您将需要选择旁边带有平台 B 徽标的流程。 3. 找到动态代码块或部分并保存。 4. 接下来，导航到新的克隆模板，并将现有动态内容替换为保存的内容。这可以节省您从头开始重新设计现有流程模板的时间。 5. 确保[将克隆的流设置为 **草稿** 或 **手动**](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8RVQANQHGVRJ6V4W63)，以便消息在迁移过程中不会自动开始发送。完成迁移过程后，您可以启用流程。 ## 7. 确认欢迎系列设置

Klaviyo 的电子商务集成并未排除在结帐时订阅的购买者进入欢迎流程。如果您想排除这些配置文件触发您的欢迎系列，请在您的流程中添加过滤器“所有时间下订单零次”。 ## 8. 克隆片段

此外，任何具有基于指标条件的分段都需要重新创建以合并新指标。使用基于指标的条件[克隆所有分段](https://help.klaviyo.com/hc/en-us/articles/24898429283739)，并编辑它们以从新的正确指标中提取信息。 ## 9. 禁用旧的集成

一旦您完全停止使用旧平台，您可以选择“****集成****”选项卡来禁用集成，然后在列表中查找集成。选择集成后，单击****管理集成>禁用集成****。 ## 结果

您现在已在切换电子商务平台后更新了 Klaviyo。 ## 其他资源

- [Klaviyo 入门（学院课程）](https://academy.klaviyo.com/getting-started-with-klaviyo)
- 需要更多与 Klaviyo 集成的帮助吗？查看 [Klaviyo 的代理合作伙伴](https://klaviyo.partnerpage.io/?utm_source=helpcenter&utm_medium=integrations)