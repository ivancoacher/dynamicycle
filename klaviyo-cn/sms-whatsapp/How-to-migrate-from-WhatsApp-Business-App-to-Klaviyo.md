---
id: "40116568714523"
title: "如何从 WhatsApp Business 应用迁移到 Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40116568714523-How-to-migrate-from-WhatsApp-Business-App-to-Klaviyo"
section: "Migrate to Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-05-11T12:54:21Z"
language: "zh"
---
了解如何从 WhatsApp Business 应用迁移到 Klaviyo。

如果您的 WhatsApp 号码与 WhatsApp Business 应用程序关联，那么迁移到 Klaviyo 意味着您将迁移到 WhatsApp Business API。 Klaviyo 可以迁移您的号码，但您将失去以下两件事：

- 在移动设备上访问 WhatsApp Business 应用程序 UI。
- 应用程序中的聊天记录（除非手动导出）。

****WhatsApp Business API 与 WhatsApp Business 应用程序有何不同？****

****WhatsApp Business 应用程序**** 专为小型企业设计，可在手机上运行，就像常规 WhatsApp 应用程序一样。它最适合一两个人直接管理客户聊天。虽然它使用简单，但它仅提供有限的自动化，并且不支持高级集成。

****WhatsApp Business API****（Klaviyo 使用）是为大中型企业构建的。它不作为移动应用程序运行；相反，它通过 Cloud API 连接到 Klaviyo 等平台。此设置支持自动化、集成以及扩展到更大的支持或营销团队。发送模板消息（例如订单更新、提醒或促销）也需要该 API。

## 开始之前

在开始迁移之前，请确保：

- 您可以访问您的 WhatsApp Business 应用程序。
- 在设置过程中，您可以通过您的电话号码接收短信。
- 如果您想保留聊天记录，您已经导出了它。

聊天记录不会传输到 WhatsApp API，并且在您停用 WhatsApp Business 应用程序后将被删除。聊天历史记录无法导入到 Klaviyo，但建议将其导出以保存记录。

## 从 WhatsApp Business 应用程序迁移

### 停用您的 WhatsApp Business 应用程序

停用您当前的 WhatsApp Business 应用程序，以便您的号码可以免费转移到 WhatsApp API。请参阅[Meta 关于停用帐户的文章](https://faq.whatsapp.com/969230211289837)。

### 禁用双因素身份验证

要迁移到 Klaviyo，您必须在 WhatsApp Business 帐户中禁用电话号码的双因素身份验证 (2FA)。如果您无法或不确定如何执行此操作，请联系您当前的提供商。

如果您有权访问 WhatsApp 管理器，您可以自行禁用此功能。

1. 在 Meta Business Suite 中，导航至****业务设置****。
2. 选择****WhatsApp 帐户****。
3. 选择您要修改的特定 WhatsApp 帐户。
4. 单击帐户设置中的****WhatsApp Manager****。
5. 选择与您的帐户关联的电话号码。
6. 单击所选电话号码的****设置****，然后选择****两步验证****选项卡。
7. 单击****关闭两步验证****。这将触发一封确认电子邮件。
8. 单击发送给您的电子邮件确认中的链接以确认此更改并禁用 2FA。

### 将您的 WhatsApp 帐户连接到 Klaviyo

1. 在 Klaviyo 中，转到****设置**** > ****WhatsApp****。
2. 单击****连接到 WhatsApp****。
3. 按照设置模式中的说明进行操作。
   1. 创建一个新的 WhatsApp 企业帐户。
   2. 使用相同的显示名称。
   3. 添加您要迁移的电话号码。
   4. 使用发送到您的号码的验证码验证您的帐户。

## 后续步骤

恭喜！您已迁移至 Klaviyo。

了解[导入您的 WhatsApp](https://help.klaviyo.com/hc/en-us/articles/40116243735579) 或了解如何[设置流程](https://help.klaviyo.com/hc/en-us/articles/40116763040411)。