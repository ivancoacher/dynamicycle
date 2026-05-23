---
id: "10952782535579"
title: "如何设置 SCIM 用户配置"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/10952782535579-How-to-set-up-SCIM-user-provisioning"
section: "Security"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:56:35Z"
language: "zh"
---
## 你将会学到

了解如何在账户或投资组合中设置跨域身份管理 (SCIM) 用户配置系统。您必须拥有付费计划并且是管理员或所有者才能设置此功能。 ## 开始之前

在设置 SCIM 之前，您还需要[在 Klaviyo 中打开 SSO](https://help.klaviyo.com/hc/en-us/articles/9353860331035)。请注意，SCIM 配置通常是身份提供商 (IdP) 的附加组件。例如，除了 SSO 计划之外，IdP 通常还需要单独的 SCIM 计划。如果您在 IdP 中没有看到以下步骤，请确认您的计划正确。 ## 打开 SCIM 用户配置

1. 单击左下角您的组织名称。 2. 单击****设置> 安全****。 ![帐户设置中的安全选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28704477982875)
3. 选中**SCIM 配置**框。 4. 复制或下载访问密钥，包括前缀“Klaviyo-API-Key”。请注意，此密钥仅显示一次，因此请确保您可以访问它。如果复制，请立即将其粘贴到安全的地方。 ![访问密钥示例](https://klaviyo.zendesk.com/hc/article_attachments/28704486111131)
5. 单击****完成****。 6. 复制基本 URL 并将其粘贴到某个位置，最好是存储访问密钥的位置。接下来，您必须联系 SSO 提供商来完成该过程。此过程因提供商而异。下面，我们提供了有关 OKTA、One Login 和 Azure 的说明，尽管您可以使用任何其他提供商进行设置。 ****奥克塔****

1. 导航至****应用程序 > 应用程序****。 2. 选择 Klaviyo 应用程序。 3. 转到****登录****选项卡。 ![具有 SSO 的应用程序的四个选项卡：常规、登录、导入和分配](https://klaviyo.zendesk.com/hc/article_attachments/28704477997723)
4. 在 **凭证详细信息** 下，检查：

   - **应用程序用户名格式**设置为****电子邮件****。 - **更新应用程序用户名**设置为****创建和更新****。！[“登录”选项卡中的“凭据详细信息”部分](https://klaviyo.zendesk.com/hc/article_attachments/28704486118683)
5. 单击进入****常规****选项卡。 ![应用程序的常规选项卡，当没有配置时](https://klaviyo.zendesk.com/hc/article_attachments/28704477985051)
6. 选择****编辑****。 7. 在**配置**下，选择 SCIM。 ![选择 SCIM 进行配置](https://klaviyo.zendesk.com/hc/article_attachments/28704486124827)
8. 单击****保存****。 9. 单击进入****配置****选项卡。 10. 选择****编辑**** 打开**SCIM 连接** 页面（如下所示）。 ![无信息的 SCIM 连接页面](https://klaviyo.zendesk.com/hc/article_attachments/28704477991963)
11. 在 **SCIM 连接器基本 URL** 中，粘贴来自 Klaviyo 的基本 URL。 12. 对于**用户的唯一标识符字段**，输入“userName”。
13. 在**支持的配置操作**下，选中以下复选框：

    - 导入新用户和配置文件更新
    - 推送新用户
    - 推送个人资料更新
14. 将 **身份验证模式** 选项更改为 HTTP 标头。 15. 将访问密钥粘贴到**授权**下。 ![填写完毕后 SCIM 连接的外观](https://klaviyo.zendesk.com/hc/article_attachments/28704486119195)
16. 单击****测试连接器配置****。 17. 单击****保存****。 18. 在“**配置到应用程序**”旁边，单击“****编辑****”。 19. 勾选****启用****以下功能：

    - **创建用户**。 - **更新用户属性**。 - **停用用户。**！[在“配置到应用程序”页面中启用功能](https://klaviyo.zendesk.com/hc/article_attachments/28704486120731)
20. 单击****保存****。 21. 向下滚动到应用程序的属性映射部分。 22. 单击****转到配置文件编辑器****。 23. 单击****添加属性****。 ![Okta 中的配置文件编辑器页面顶部，显示添加属性的按钮](https://klaviyo.zendesk.com/hc/article_attachments/28704477999899)
24. 为 **显示名称**、**变量名称** 和 **外部名称** 键入“角色”。 25. 在**外部命名空间**中，输入以下内容：
    瓮：ietf：参数：scim：模式：核心：2.0：用户
26. 选中****定义枚举值列表****复选框。 ![角色属性的第一个必需设置](https://klaviyo.zendesk.com/hc/article_attachments/28704486132763)
27. 添加角色和价值观；有效的角色值如下：

    - 管理员
    - 经理
    - 分析师
    - 活动\_协调员
    - 内容创建者
    - 支持！[角色属性具有正确值的所有角色](https://klaviyo.zendesk.com/hc/article_attachments/28704486134171)
28. 向下滚动到**需要属性**并选中****是****。 29. 选择属性类型（个人或团体）。 30. 建议：将**用户权限**保留为****只读****。 ![角色属性的其余必需设置](https://klaviyo.zendesk.com/hc/article_attachments/28704478000539)
31. 单击****保存****。 32. 导航至****应用程序 > 应用程序****，然后选择您的应用程序。 33. 单击****分配****。 34. 选择是将应用程序分配给个人（即人员）还是组。 ![显示“分配”下拉列表的“分配”选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28704486135323)
35. 找到您想要为其分配 Klaviyo 的人员或组，然后单击其姓名旁边的****分配****。 ![搜索分配给应用程序的用户的示例](https://klaviyo.zendesk.com/hc/article_attachments/28704478005915)
36. 向下滚动到 **角色** 字段并为他们分配正确的角色。 ![角色下拉列表，显示 Klaviyo 中角色的所有值](https://klaviyo.zendesk.com/hc/article_attachments/28704486114843)
37. 单击****保存并返回****。 ****一次登录****

1. 在管理门户中，单击****应用程序****。 2. 单击****添加应用程序****。 3. 搜索“Klaviyo”。
4. 单击****Klaviyo**** 添加它。 5. 可选：重命名连接。 6. 单击****配置。****
7. 在 **SCIM 承载令牌** 字段中，粘贴您的 SCIM 访问密钥。 8. 单击“**API 连接**”下的“****启用****”。 9. 单击****保存。****
10. 转到左侧边栏中的****配置****。 11. 选中****启用配置****框。 12. 不要取消选中**创建用户**、**删除用户**或**更新用户**框。 ![具有正确设置的凭据详细信息部分](https://klaviyo.zendesk.com/hc/article_attachments/28704477975451)
13. 建议：在 **当在 OneLogin 中删除用户或删除用户的应用程序访问权限时，请执行以下操作** 的下拉列表中选择 ****删除****。 14. 单击****保存****。 ****Microsoft Entra ID（以前称为 Azure AD）****

1. 登录[Microsoft Entra ID](https://portal.azure.com/#home.)。 2. 单击****Microsoft Entra ID****（以前称为“Azure Active Directory”）
3. 单击左侧的****企业应用程序****。 ![左侧边栏中的企业应用程序选项](https://klaviyo.zendesk.com/hc/article_attachments/28704486140699)
4. 选择您的应用程序。 - 如果您尚未创建应用程序，请按照 [SSO 指南](https://help.klaviyo.com/hc/en-us/articles/9353860331035) 中的步骤操作。 5. 单击左侧的****配置****，然后选择****开始****。 ![突出显示“配置”时应用程序的左侧边栏](https://klaviyo.zendesk.com/hc/article_attachments/28704478008731)
6. 在名为 **配置模式** 的字段中，选择 ****自动****。 ![将配置模式更改为自动](https://klaviyo.zendesk.com/hc/article_attachments/28704478010011)
7. 转至 **管理员凭据**。 8. 将 Klaviyo 中的 SCIM 基本 URL 粘贴到 **租户 URL** 字段中。 9. 将 SCIM API 密钥粘贴到 **秘密令牌** 字段中。请注意，粘贴此令牌时应不带任何前缀（例如，不包含“Bearer”或“Klaviyo-API-Key”）。 10. 测试连接。 11.连接成功后，点击左上角的****保存****。 12. 在同一页面中，向下滚动并打开 ****Mappings**** 下拉列表。 ![映射下拉列表以配置（按顺序）Azure AD 组或用户](https://klaviyo.zendesk.com/hc/article_attachments/28704486146459)
13. 选择****配置 Azure Active Directory 用户****。 14. 可选：删除不支持的属性。请注意，Klaviyo 仅支持 SCIM 的 c**ustomappsso Attribute** 列中的以下属性：

    - “用户名”
    - “活跃”
    - 电子邮件[类型 eq“工作”].value'
    - “名字.givenName”
    - “姓名.家庭名称”
    - emails[primary eq "True"].value'
    - 角色[primary eq "True"].value'
    - SingleAppRoleAssignment([appRoleAssignments])
      - 不支持appRoleAssignments
15. 单击****保存****，然后单击****主页****。 16. 导航回****Microsoft Entra ID > 企业应用程序 > Klaviyo > 配置****。 17. 选择****开始配置****。 ![配置选项卡，显示开始配置按钮](https://klaviyo.zendesk.com/hc/article_attachments/28704478011931)