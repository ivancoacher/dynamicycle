---
id: "9674090873883"
title: "解决 SSO 和 SCIM 错误"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/9674090873883-Troubleshoot-SSO-and-SCIM-errors"
section: "Security"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:55:06Z"
language: "zh"
---
## 你将会学到

了解如何使用 Klaviyo 解决单点登录 (SSO) 错误。本文适用于熟悉 SSO 的人员，例如 IT 专业人员。有关更多信息，请参阅这篇关于[如何设置单点登录](https://help.klaviyo.com/hc/en-us/articles/9353860331035)的文章。 ## 错误列表以及如何修复它们

我们详细分析了您在设置 SSO 时可能遇到的所有潜在错误。当信息缺失或不正确时，往往会发生错误。下表显示了所有潜在错误、修复位置以及修复方法。 |  |  |
| --- | --- |
| ****错误**** | ****如何修复它**** |
|缺少 {email} ({company\_id}) 的 SSO 配置 |确保 SSO 配置设置保存在 Klaviyo 中。 |
|已禁用 {email} ({company\_id}) 的 SSO |在 Klaviyo 的 SSO 配置面板中启用 SSO。 |
|缺少 ({company\_id}) 的 SSO 配置 |确保保存 SSO 配置设置。 |
|已为 ({company\_id}) 禁用 SSO |在 Klaviyo 的 SSO 配置面板中启用 SSO。 |
|无法为账户 ({company\_id}) 中的 {email} 配置新的 SSO 用户（未启用即时配置） |如果您想要使用即时用户配置，请在 IdP SSO 提供商的 SSO 配置面板中将其打开。 |
|已对 {email} ({company\_id}) 禁用 IdP 发起的 SSO |如果您想使用 IdP 发起的 SSO，可以在 SSO 配置面板中启用它。 |
| **缺少（{company\_id}）的 SSO 配置** |确保您的 SSO 配置已设置并保存。 |
|该用户隶属于 Klaviyo 超过 1 家公司。他们在 Klaviyo 中的名字或姓氏与您提供的值不同。请联系该用户并更新他们在您的 IdP 中的姓名，以匹配 Klaviyo | 中的值。如果用户的姓名与 IdP 中的姓名不匹配，管理员应要求用户更新姓名。 |

### SSO 配置错误

|  |  |  |  |
| --- | --- | --- | --- |
| ****错误**** | ****如何修复它**** | |  |
|不受支持的 SAML 版本 |转到您的 IdP SSO 提供商并更新到 SAML 2.0。 | |  |
| SAML 响应中缺少 ID 属性 |检查您的 IdP 设置中的 ID 是否正确且格式正确。 | |  |
|缺少角色属性 |导航到您的 SSO 提供商并确保在 SAML 断言中包含角色属性。角色值必须是以下之一。 | |  |
| [帐户用户角色](https://help.klaviyo.com/hc/en-us/articles/115005231648)： - 所有者 - 管理员 - 经理 - 分析师 - 活动\_协调员 - 内容\_creator - 支持 | [投资组合用户角色](https://help.klaviyo.com/hc/en-us/articles/25181702319643)： - 投资组合\_owner - 投资组合\_admin - 投资组合\_manager - 投资组合\_analyst |  |
| SAML 响应必须包含 1 个断言 |导航到您的 SSO 提供商并确保在 SAML 断言中包含角色属性。 | |  |
| SAML 响应无效。与 saml-schema-protocol-2.0.xsd 不匹配 |确保您的 SAML 响应遵循 SAML 2.0 的架构协议。 | |  |
|响应的断言未加密，SP 需要它 | Klaviyo 要求对断言进行加密。确保您使用的是加密的断言。 | |  |
|断言必须包含条件元素 |确保 IdP 的 SAML 响应断言包含条件元素。 | |  |
|断言必须包含 AuthnStatement 元素 |确保 IdP 的 SAML 响应断言包含 AuthnStatement 元素。 | |  |
|响应中没有 AttributeStatement |确保 IdP 的 SAML 响应断言包含 AttributeStatement 元素。 | |  |
|响应中有一个 EncryptedAttribute，但此 SP 不支持它们 | Klaviyo 不支持属性加密。检查 IdP 的设置并确保没有加密属性。 | |  |
|响应的目标值为空 |转至您的 IdP 并填写目的地。请注意，该值的名称可能不是“目标”，因为它有所不同。如果您没有看到“目标”，请查找该值的其他常用名称：“回复 URL”、“ACS URL”、“断言消费者服务 URL”、“受信任的 URL”和“端点 URL”。 | |  |
| %s 不是此回复的有效受众 |确保 IdP 中的受众 ID 与 SSO 配置面板中提供的受众 URI（服务提供商实体 ID）完全匹配，包括 https:// 前缀。 | |  |
|断言/响应中的颁发者无效（预期为 %(idpEntityId)s，得到 %(issuer)s）|确保 SSO 管理面板中的 IdP SSO URL 字段与您的身份提供商提供的 SSO URL 匹配 | |  |
|根据此响应的 AttributeStatement 的 SessionNotOnOrAfter，属性已过期 |重试登录。如果这不起作用，请延长 IdP 中 SAML 响应的过期窗口，因为它可能太短。 | |  |
|在此响应中未找到有效的主题确认 |检查 IdP 的设置并查找主题确认方法。确保其格式正确。 | |  |
|响应的断言未签名，SP 需要它 | - 转到工作区的 SSO 页面并取消选中已签名的断言框，或者 - 转到 IdP 设置并打开响应的签名断言 如果需要帮助，请联系您的 IdP。 | |  |
|响应消息未签名，SP 需要它 |可以： - 转到工作区的 SSO 页面，取消选中“已签名的响应”框 或者 - 转到 IdP 设置并打开签名响应 如果需要帮助，请联系您的 IdP。 | |  |
|未找到签名。 SAML 响应被拒绝 |检查来自 IdP 的 SAML 消息是否已正确签名。 | |  |
|签名验证失败。 SAML 响应被拒绝 |转到工作区的 SSO 页面并确保证书与从 IdP 发送的证书匹配。 | |  |
|未找到 SAML 响应，仅支持 HTTP\_POST 绑定 |检查您的 IdP 是否正在发送 HTTP\_POST 请求。 | |  |

## 其他故障排除提示

打开与您遇到的问题最匹配的下拉列表，以获取有关如何解决该问题的信息。 ****我无法在 Klaviyo 中编辑用户角色****

最可能的原因是您使用的是即时 (JIT) 配置。当 JIT 打开时，您无法在 Klaviyo 中编辑用户的角色。为此，最好的选择是：

1. 暂时关闭 JIT 配置。 2. 更新用户在 Klaviyo 中的角色。 3. 重新打开 JIT。 ****我无法查看豁免列表****

您需要设置 SSO 才能查看豁免列表。有关说明，请参阅我们的[有关如何在 Klaviyo 中启用 SSO 的文章](https://help.klaviyo.com/hc/en-us/articles/9353860331035)。