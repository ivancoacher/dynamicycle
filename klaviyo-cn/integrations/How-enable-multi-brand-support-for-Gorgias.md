---
id: "33997568400539"
title: "如何为 Gorgias 启用多品牌支持"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/33997568400539-How-enable-multi-brand-support-for-Gorgias"
section: "Gorgias"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:49Z"
language: "zh"
---
如果您在 Klaviyo 引入对多个 Gorgias 品牌的支持之前集成了 Klaviyo 和 Gorgias，请了解如何为 Klaviyo 的 Gorgias 集成启用多品牌支持。门票、短信、WhatsApp 消息和评论现在可以按品牌同步。如果您在一个 Gorgias 帐户中管理多个品牌，则每个 Klaviyo 帐户同步一个 Gorgias 品牌可以轻松使用您的票证数据并组织您的短信和 WhatsApp 对话。启用多品牌支持需要 4 个步骤：

1.（可选）从 Klaviyo 中删除现有的“不正确”Gorgias 配置文件
2. 在 Gorgias 中创建规则以按品牌标记门票
3.（可选）根据品牌标签在 Gorgias 中创建视图
4. 更新您的 Gorgias 集成设置

第一次想要整合？前往 [Gorgias 入门](https://help.klaviyo.com/hc/en-us/articles/4408023789083)。 ## 开始之前

请注意，当您更新 Gorgias 集成以启用多品牌支持时，之前通过集成同步的历史数据将保留在您的帐户中，除非您选择手动删除 Klaviyo 配置文件。 ##（可选）从 Klaviyo 中删除 Gorgias 配置文件

如果您现在想要将您的 Klaviyo 帐户与特定 Gorgias 品牌关联，您可能需要删除之前通过集成同步的 Gorgias 配置文件。由于没有与这些旧配置文件关联的品牌，因此无法精确删除特定品牌的配置文件。相反，我们建议删除通过 Gorgias 集成同步但与您的 Klaviyo 帐户关联的电子商务网站没有任何交互的配置文件。这些配置文件可能是从“错误”的品牌同步的。为此，我们建议创建这些配置文件的一部分，然后将其删除。这应该在更新 Gorgias 集成之前完成。创建段：

1. 某人做过或没做过的事情 > 已开票 (Gorgias) > 至少一次 > 一直以来并且
2.某人做过或没做过的事情 > 查看产品 > 零次 > 一直以来并且
3.某人做过或没做过的事情 > 已开始结账 > 零次 > 全部时间并且
4.某人做过或没做过的事情 > 已下订单 > 零次 > 一直以来 AND
5.某人做过或没做过的事情 > 订阅列表 (Klaviyo) > 零次 > 全部时间

1. 在 Klaviyo 中，导航至****受众 > 列表和细分****。 2. 选择****新建 > 创建段****。 3. 为您的分段命名并选择任意标签。 4. 使用从电子商务平台同步的事件添加以下细分条件：
5. 您还可以为帐户中的任何其他适用事件添加条件，指定配置文件未跟踪这些事件。 6. 单击****创建分段****。 7. 然后，按照我们的[批量删除说明](https://help.klaviyo.com/hc/en-us/articles/24312135764251#h_01HT5F82SYT68E2X2Z68DC78RR)删除您在上面创建的分段。 ## 在 Gorgias 中创建规则以按品牌标记门票

在 Gorgias 中，对于每个品牌，您需要创建一条规则来查看用户写入的电子邮件，然后用适当的品牌标记票证：

1. 何时 > 工单创建 > 然后
2. IF > 消息集成 > IS > [品牌专用电子邮件地址]
3. 然后 > 添加标签 > [品牌特定标签]
   ![](https://klaviyo.zendesk.com/hc/article_attachments/37720714482587)

1. 在您的 Gorgias 设置中，选择 ****规则****（可在 **生产力**下找到）。 2. 添加新规则。 3. 为您的规则命名具有描述性的名称。 4. 添加以下规则条件：
5. 确保**启用规则**设置为****开****。 6. 单击****创建规则****。对您想要与单独的 Klaviyo 帐户集成的每个品牌重复此过程。 ## （可选）根据品牌标签在 Gorgias 中创建视图

设置自动标记门票的规则后，我们建议在 Gorgias 中为每个品牌创建一个视图，其中包含标有该品牌名称的所有门票：

1. 在 Gorgias 中，创建一个新视图。 2. 添加以下过滤器：标签 > 包含全部 > [品牌标签]

![](https://klaviyo.zendesk.com/hc/article_attachments/37720796406427)

对您想要与单独的 Klaviyo 帐户集成的每个品牌重复此过程。 ## 更新您的 Gorgias 集成设置

要更新您的 Gorgias 集成设置并在给定的 Klaviyo 帐户中启用多品牌支持：

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 从启用的集成列表中选择 **Gorgias**。 3. 我们建议每个 Klaviyo 帐户连接一个 Gorgias 品牌。在 **门票** 下，选择您想要与此 Klaviyo 帐户一起使用的 Gorgias 品牌对应的标签，并将新门票同步到 Klaviyo。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37720914786459)
4. 如果您使用 SMS 对话：在 **对话** 下，我们建议添加与您想要与此 Klaviyo 帐户一起使用的 Gorgias 品牌相对应的标签。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37720900025883)
5. 选中**同步 WhatsApp 对话**复选框以使用 WhatsApp 集成功能。 1. 支持代理还可以使用[扩展 WhatsApp 对话的模板](https://help.klaviyo.com/hc/en-us/articles/40116778911259)，确保他们可以在 24 小时服务窗口之外继续与收件人互动。 ![显示同步 WhatsApp 对话选项的对话框](https://klaviyo.zendesk.com/hc/article_attachments/41259966180635)
6. 如果您使用评论：在**评论**下，我们建议添加与您想要与此 Klaviyo 帐户一起使用的 Gorgias 品牌相对应的标签。 ![](https://klaviyo.zendesk.com/hc/article_attachments/37720900027291)
7. 完成后，单击****更新设置****。您需要与 Gorgias 集成，并为要与 Gorgias 品牌连接的每个 Klaviyo 帐户配置上述品牌相关设置。