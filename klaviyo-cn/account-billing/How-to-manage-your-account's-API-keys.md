---
id: "115005062267"
title: "如何管理您帐户的 API 密钥"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005062267-How-to-manage-your-account-s-API-keys"
section: "API keys"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:54:16Z"
language: "zh"
---
只有所有者或管理员才能访问 API 密钥选项卡。

了解如何访问和管理您的 Klaviyo 帐户的 API 密钥。

如果您想了解如何创建或克隆私有 API 密钥，请阅读[如何创建私有 API 密钥](https://help.klaviyo.com/hc/en-us/articles/7423954176283)。

## API 公钥和私钥的区别

您的公共 API 密钥也称为您的 **站点 ID**。这是一个简短的字母数字值。该公钥是您的 Klaviyo 帐户的唯一标识符，每个帐户只有一个。公开您的公共 API 密钥是安全的，因为该密钥无法用于访问您的 Klaviyo 帐户中的数据。

私有 API 密钥用于从 Klaviyo 读取数据并操作一些敏感对象，例如列表。像对待密码一样对待私有 API 密钥：保存在安全的地方并且永远不会向公众公开。 Klaviyo 帐户可以根据需要生成任意数量的私有 API 密钥。

### 如果您的 API 密钥暴露该怎么办

由于公共 API 密钥通常是一个标识符，因此如果公开 API 密钥被公开，则不会有风险。

对于私有 API 密钥而言，情况并非如此。私有 API 密钥可以向某人授予他们不应拥有的访问权限或权限，例如允许他们查看或编辑客户数据。

如果私有 API 密钥暴露，您应立即[创建一个新的私有 API 密钥](https://help.klaviyo.com/hc/en-us/articles/7423954176283) 并停用旧密钥。此外，请考虑私有 API 密钥应具有哪些权限，并为每个应用程序使用不同的私有 API 密钥。

## 找到您的 API 密钥

创建 API 私钥后，您将无法查看任何私钥。相反，您应该将私有 API 密钥视为密码：仅与您信任的各方共享这些密钥，并将它们保存在安全的地方，例如保险库或密码管理器。

1. 单击左下角您的帐户名称。
2. 单击****设置****。
   ![settings.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705662510747)
3. 选择****API 密钥****选项卡。
4. 查看您的公共 API 密钥（即 s**ite ID**）。
   - 您可以看到您的私有 API 密钥的名称，但无法查看密钥本身。
     ![帐户设置中的 API 密钥选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28705662509467)

### 克隆私有 API 密钥

虽然您可以[克隆现有的私有 API 密钥](https://help.klaviyo.com/hc/en-us/articles/7423954176283)，但克隆的密钥将：

- 与原来的键完全不同。
- 使用与原始名称相同的名称。
- 与原版具有相同的范围。

## 其他资源

- [如何创建私有API密钥](https://help.klaviyo.com/hc/en-us/articles/7423954176283)
- [Klaviyo 的 API 参考指南](https://developers.klaviyo.com/en/reference/api_overview)
- [了解 Klaviyo 和应用程序之间如何交换信息](https://klaviyo.zendesk.com/hc/en-us/articles/360030265051)