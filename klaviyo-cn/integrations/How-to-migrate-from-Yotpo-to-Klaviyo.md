---
id: "39598076123547"
title: "如何从 Yotpo 迁移到 Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/39598076123547-How-to-migrate-from-Yotpo-to-Klaviyo"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: "zh"
---
了解如何通过 Klaviyo 的 Yotpo 电子邮件和短信迁移集成从 Yotpo 电子邮件和短信迁移到 Klaviyo。此集成可同步 Yotpo 的配置文件以及电子邮件和短信订阅。此外，了解迁移时的最佳实践和后续步骤。 ![](https://fast.wistia.com/embed/medias/akui1d7vqk/swatch)

## 开始之前

1. 您必须是 Yotpo 的帐户管理员才能集成。 2. 您必须是 Klaviyo 的管理员或所有者才能集成。 3. 如果您计划从 Yotpo 迁移短信联系人，您必须首先：

- [在 Klaviyo 中设置短信](https://help.klaviyo.com/hc/en-us/articles/4404274419355)。要同步短信同意，您必须在要收集和同步同意的每个区域配置发送号码。 - 在开始从新号码发送之前，[通知订阅者](https://help.klaviyo.com/hc/en-us/articles/4403980438555)。 ### 重新创建表单、电子邮件模板和流程

首先，在 Klaviyo 中重新创建最重要的客户收集方法（在 Klaviyo 中称为“表单”）、电子邮件模板和流程。一旦准备好这些，您就不必担心维护 2 个不同的订户列表或客户沟通中存在差距。有关这些产品领域的信息，请查看这些入门指南：

- [表格](https://help.klaviyo.com/hc/en-us/articles/360026474752)
- [电子邮件模板](https://help.klaviyo.com/hc/en-us/articles/115000102752#h_01HNG9WJTANZBQ3QZRJ4EHD43F)
- [流程](https://help.klaviyo.com/hc/en-us/articles/115002774932)

  由于集成是一次性同步，因此准备好消息和表单意味着您可以立即开始使用 Klaviyo。特别是对于短信，您不应该在两个不同的平台上保持同意。如果您在安装集成后仍从 Yotpo 发送，则订阅或取消订阅的任何人都不会自动转移。这可能意味着您不合规或无法向订阅者发送消息。这也是回顾哪些方面运作良好的好时机：
- 一种形式是否优于其他形式？ - 哪些流量产生的收入最多？ - 哪种电子邮件模板点击次数最高？这不仅告诉您在迁移到 Klaviyo 时要优先考虑什么，而且还表明您应该在哪里花时间进行试验和优化。 ## 将 Yotpo 与 Klaviyo 集成

要将 Yotpo 与 Klaviyo 集成，您需要从 Yotpo 获取应用程序密钥和密钥，然后在 Klaviyo 中设置集成：

1. 在 Yotpo 短信和电子邮件管理中，单击您的帐户图标并选择****帐户设置****。 2. 滚动到 **API 凭证** 部分，然后复制您的 **应用程序密钥**。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39742508136859)
3. 在新选项卡中，登录 Klaviyo 并选择 ****Integrations**** 选项卡。 4. 单击****探索应用程序****。 5. 在 Klaviyo 应用市场上搜索 **Yotpo** 并选择该卡。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39742508140059)
6. 单击****安装****。 7. 将复制的 Yotpo 应用程序密钥粘贴到相应的框中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39749638021275)
8. 切换回 Yotpo 选项卡。 9. 在**API 凭证**下，单击****获取密钥****。 10. 复制发送到您的电子邮件的代码并将其粘贴到框中，然后单击****提交****。 11. 您的密钥将出现在弹出窗口中。单击****复制到剪贴板****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39749664634523)
12. 切换回 Klaviyo 选项卡。 13. 将您的密钥粘贴到相应的框中，然后单击****连接****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39749664635803)
14. 检查权限并单击****允许****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39742508146459)
15. 选中 **将您的 Yotpo 电子邮件和 SMS 迁移电子邮件订阅者同步到 Klaviyo**。如果您不选中该框，Klaviyo 将不会同步来自 Yotpo 的电子邮件同意。 1. 从下拉列表中选择要添加电子邮件订阅者的列表。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499603355)
16. 选中 **将您的 Yotpo 电子邮件和 SMS 迁移 SMS 订阅者同步到 Klaviyo**。如果您不选中该框，Klaviyo 将不会同步来自 Yotpo 的短信同意。 1. 从下拉列表中选择要添加 SMS 订阅者的列表。 17. 单击****完成设置****。 18. 您将收到一条成功消息，确认您的 Yotpo 集成已连接。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39742508149403)

## 数据从 Yotpo 同步到 Klaviyo

将 Yotpo 与 Klaviyo 集成后，Klaviyo 将对 Yotpo 中的所有配置文件执行一次性同步。此集成旨在用于迁移，并且没有持续同步。数据仅从 Yotpo 同步到 Klaviyo。以下数据从 Yotpo 同步到 Klaviyo：

- 个人资料
- 电子邮件订阅（如果您选中设置框并选择了 Klaviyo 列表）
- 短信订阅（如果您选中设置框并选择了 Klaviyo 列表）

  电子邮件和短信订阅根据 Yotpo 中的订阅状态同步；如果个人资料在 Yotpo 中订阅了电子邮件或短信，则它们将在 Klaviyo 中订阅，如果它们在 Yotpo 中取消订阅，则它们将在 Klaviyo 中取消订阅。如果尚未在 Klaviyo 中订阅，订阅的配置文件将被添加到集成设置中定义的列表中。如果您选择不同步订阅，所有配置文件都将同步，状态为**从未订阅**。以下配置文件属性从 Yotpo 同步到 Klaviyo：
- 电子邮件
- 电话号码
- 名字
- 姓氏
- 地址1
- 地址2
- 城市
- 地区
- 邮政编码
- 国家
- Yotpo 性别
- Yotpo默认语言
- Yotpo 默认货币
- Yotpo标签
- Yotpo 电子邮件上次打开
- Yotpo 电子邮件上次发送
- Yotpo 电子邮件上次参与
- Yotpo 短信上次发送
- Yotpo SMS 最后参与

## 迁移数据后

### 关闭 Yotpo 中的所有订阅者收集方法

导入后，您应立即停止在 Yotpo 中收集新订阅者。在两个不同平台上维护订阅者列表不仅很困难，而且是一个有风险的合规举措（特别是对于 SMS）。 1. 在 Yotpo 中，导航至****Audience****。 2. 在**订户收集工具**页面上，向下滚动到**我的工具**。 3. 单击实时工具旁边的 3 个水平点。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499609499)
4. 从菜单中，单击“****编辑****”以查看此工具。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499611035)
5. 在顶部，打开 **状态** 下拉列表。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39663829287451)
6. 选择****草稿****。 7. 现在单击****另存为草稿****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499612699)
8. 对任何其他实时订户收集工具重复此操作。此外，编辑或删除链接到这些选择加入页面的任何位置，例如社交媒体页面、二维码等。 ### 记下 Yotpo 帐户中的关键设置

当您迁移到新的服务提供商时，无法保证他们使用相同的设置。一旦更改平台，这可能会导致数据出现显着差异，因此迁移的关键部分是记下当前设置。特别要注意以下几点：

- 转换窗口，以及[Klaviyo 中归因的工作原理](https://help.klaviyo.com/hc/en-us/articles/1260804504250)
- UTM追踪
- 智能发送

要在 Yotpo 中查找这些设置：

1. 在左侧边栏中，打开****设置****下拉列表，然后单击****常规设置****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39742499614107)
2. 导航至：
   1.****您的转换和 UTM 设置的归属****。 2. ****智能发送的合规性****。 ### SMS 特定注意事项

如果您还将 SMS 计划转移到 Klaviyo，请：

- 在您想要收集和同步同意的每个区域配置发送号码。 - 写下您的订阅关键字。 - 检查安静时间。 ## 后续步骤

完成上述步骤后，恭喜您！您现在将在 Klaviyo 中获得所有关键信息。下一步，我们建议：

1. [取消 Yotpo 中的电子邮件套餐](https://support.yotpo.com/docs/configuring-billing-and- payments)。 2. [在 Klaviyo 中添加您的用户](https://help.klaviyo.com/hc/en-us/articles/360053547071)。 3. 重新创建您的[段](https://help.klaviyo.com/hc/en-us/articles/360035312491)。