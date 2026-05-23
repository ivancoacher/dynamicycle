---
id: 6666
title: "如何管理账户的 API 密钥"
slug: "accountsapikeys"
category: "账户与计费（Account &amp; Billing）"
category_slug: "account-billing"
wp_url: "https://dynamicycle.com/docs/accountsapikeys/"
wp_modified: "2026-01-28T08:07:15"
---

##### ****公共与私有 API 密钥的区别****

你的公共 API 密钥也被称为 ****Site ID****。这是一个简短的字母数字值。这个公共密钥是你 Klaviyo 账户的唯一标识符，每个账户只有一个。公开你的公共 API 密钥是安全的，因为这个密钥无法用于访问你 Klaviyo 账户中的数据。

私有 API 密钥用于从 Klaviyo 读取数据以及操作一些敏感对象，如列表。私有 API 密钥应像密码一样保管：放在安全的地方，且绝不暴露给公众。一个 Klaviyo 账户可以根据需要生成任意数量的私有 API 密钥。

##### ****如果你的 API 密钥被暴露，该怎么做****

由于公共 API 密钥通常只是一个标识符，因此如果公共 API 密钥被暴露是没有风险的。

但是，私有 API 密钥则不同。私有 API 密钥可以让某人获得不应拥有的访问权限或权限，例如允许他们查看或编辑客户数据。

如果私有 API 密钥被暴露，你应立即创建一个新的私有 API 密钥，并停用旧的密钥。此外，考虑该私有 API 密钥应该具备的权限，并为每个应用程序使用不同的私有 API 密钥。

##### 查找你的 API 密钥

1.点击左下角的 Account 名称。
2.点击 Settings。

![软件界面的菜单，包含"观众"、"内容"、"分析"、"对话"和"设置"选项，显示"Round Pieces"账户信息。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-147.png?resize=902%2C674&ssl=1)

3.选择 API Keys 标签。
4.查看你的公共 API 密钥（即站点 ID）。

- 你可以看到私有 API 密钥的名称，但无法查看密钥本身。

![API密钥管理界面，显示公共API密钥和私有API密钥的相关信息，包括公司名称、创建日期和访问级别。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-148.png?resize=1024%2C611&ssl=1)

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)