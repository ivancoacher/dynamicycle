---
id: "7423954176283"
title: "如何创建或克隆私有 API 密钥"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/7423954176283-How-to-create-or-clone-a-private-API-key"
section: "API keys"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: "zh"
---
您必须是所有者或管理员才能创建、克隆或删除私有 API 密钥。 ## 你将会学到

了解如何创建私有 API 密钥（这是用于 API 调用的唯一标识符）以及如何定义范围。私有 API 密钥和范围都可以通过限制第三方可以访问的内容来帮助您保护您和您客户的数据。 ## 关于私有 API 密钥和范围

当您进行 API 调用时，它允许一个软件连接到另一个软件。这种连接允许一个软件向另一个软件请求、编辑或添加信息。私有 API 密钥可确保此请求具有正确的权限（即，它来自授权的用户、帐户或程序）。可以把它想象成一把房子钥匙：它可以让您和您的家人进入，但将其他人拒之门外。包含私有 API 密钥的范围会增加另一层授权，限制第三方可以访问的特定元素。范围类似于酒店钥匙，只允许您访问某些区域（例如您的房间或健身房），而不是整个建筑物。 ### 范围类型

创建私有 API 密钥时，必须选择其范围。换句话说，您必须决定是否希望第三方：

- 无权访问 API 端点。 - 查看 API 端点的所有数据，但无法进行更改（也称为“只读”）。 - 创建、删除与该端点关联的任何内容以及进行其他更改（也称为“完全访问权限”或“写访问权限”）。例如，假设您想从第三方软件[将订阅者添加到 Klaviyo 列表](https://developers.klaviyo.com/en/reference/create_list_relationships)。在这种情况下，您必须对列表、配置文件和批量订阅配置文件的 API 端点具有完全（写入）访问权限。但是，第三方不需要访问任何其他端点。您可以在开发者门户上了解 [Klaviyo 的 API](https://developers.klaviyo.com/en/reference/api_overview) 并查看[每个端点的可用范围](https://developers.klaviyo.com/en/docs/authenticate_)。 ## 开始之前

请注意以下事项：

- 创建私有 API 密钥后，您不能：
  - 再次查看私有API密钥。 - 提示：安全地保存私有 API 密钥并记下您想要使用它们的用途，例如在密码管理器中。 - 添加或编辑其范围。 - 如果您需要更改范围，唯一的选择是删除原始 API 私有密钥，然后创建一个具有正确范围的新密钥。 - 默认情况下，私有 API 密钥具有完全访问权限。如果您不确定需要哪些 API 端点、范围或权限，请联系开发人员或联系 [Klaviyo 合作伙伴](https://connect.klaviyo.com/) 寻求帮助。 ## 创建私有 API 密钥

创建私有 API 密钥后，您将无法查看它。相反，您应该将私有 API 密钥视为密码：仅与您信任的各方共享这些密钥，并将它们保存在安全的地方，例如保险库或密码管理器。 1. 单击左下角的组织名称。 2. 导航至****设置****。 3. 单击****API 密钥****。 ![帐户设置中的 API 密钥选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28723522966299)
4. 单击****创建私有 API 密钥****。 5. 命名 API 密钥。 6. 选择您想要提供 API 密钥的范围：

   - 只读
   - 完整
   - 自定义！[创建具有范围的私有 API 密钥的页面](https://klaviyo.zendesk.com/hc/article_attachments/28723522963355)
7. 选择****创建****。现在，当您共享私有 API 密钥时，第三方将只能访问您在范围中定义的信息。 ## 使用查询

查询用于高级场景。如果您还不熟悉查询或如何使用它们，我们建议您与开发人员合作。 #### 包括

请注意，如果您尝试使用“include”查询，则必须更改上面列出的格式。例如，配置文件端点是 **/api/profiles**。但是，如果您添加包含查询参数 (**/api/profiles?include=list**)，您还需要 **list:read** 或​​ **list:full access**，具体取决于您进行的 API 调用类型。 #### 范围

使用“scopes”参数，您可以创建一个 URL 参数来自动填充您的私有 API 密钥所需的访问范围。在范围查询中，包含要预选的范围的逗号分隔列表。 示例 URL 是：
**https://www.klaviyo.com/create-private-api-key?scopes=campaigns:read,campaigns:write**

导航到我们的开发者门户以查看[您可以在此查询中使用的范围](https://developers.klaviyo.com/en/docs/authenticate_)。 ## 克隆私有 API 密钥

使用私有 API 密钥，克隆允许您创建与原始密钥具有相同范围和权限的新密钥。请注意：

- 克隆不会生成与原始私有 API 密钥相同的密钥。 - 您无法重命名克隆的 API 密钥；它与原始密钥具有相同的名称。克隆私有 API 密钥：

1. 导航至****API 密钥**** 选项卡。 2. 单击要克隆的密钥旁边的三点菜单。 3. 选择****克隆 > 克隆****。 ![用于克隆或删除私有 API 密钥的菜单](https://klaviyo.zendesk.com/hc/article_attachments/28723544939931)
4. 复制或下载新的私有 API 密钥并将其存储在安全的地方。 5. 如果不再需要旧密钥，请务必将其删除。