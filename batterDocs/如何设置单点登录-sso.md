<h1>如何设置单点登录 (SSO)</h1>

<h2>你将会学到</h2>
<p>了解如何为您的 Klaviyo 帐户或投资组合设置单点登录 (SSO)。目前，Klaviyo 仅支持身份提供 (IdP) 单点登录。 <strong><em>*为什么使用单点登录？</strong></em>*</p>
<p>单点登录 (SSO) 使您的帐户更加安全，从而帮助保护您以及您的客户。如果您为企业设置了 SSO，则可以要求 Klaviyo 用户使用其 SSO 凭据登录。另外，如果您的组织使用 SSO，您和您的用户可以在重新输入凭据之前更长时间地保持登录 Klaviyo 的状态。 ## 开始之前</p>
<p>我们强烈建议您联系您公司的 IT 部门来帮助您进行设置，因为您需要在公司的身份提供商中执行某些步骤。如果需要，您可以暂时[让他们成为您帐户的管理员](https://help.klaviyo.com/hc/en-us/articles/360053547071) 来设置 SSO。请注意：</p>
<ul>
<li>您必须有付费计划才能使用 SSO。 - 您必须是所有者或管理员才能设置此功能。 - Klaviyo 不支持服务提供商 (SP) SSO，仅支持 IdP SSO。如果您使用身份提供 (IdP) 单点登录 (SSO)，则可以使用它登录 Klaviyo。安全断言标记语言 2.0 (SAML 2.0) SSO 允许成员通过您选择的 IdP 访问 Klaviyo。 IdP SSO 提供商的示例包括 Okta、OneLogin、Microsoft Entra ID 等。如果您对所有用户强制执行 SSO，则任何新用户都需要接受邀请，然后使用 SSO 登录。 ****查看和使用豁免列表****</li>
</ul>
<p>当公司强制执行 SSO 时，添加到豁免列表的用户将能够绕过 SSO 并使用用户名和密码登录。如果出现 IdP 中断或您不想向 IdP 实例添加合作伙伴、承包商或机构成员，这一点非常重要。请注意，只有设置 SSO 后，您才能查看豁免列表。 <strong><em>*什么是工作场所 ID？</strong></em>*</p>
<p>工作场所 ID 也称为 SSO 登录标识符，需要在 Klaviyo 中设置 SAML SSO。它通常与您的公司名称相同。您将在 Klaviyo 设置过程的第 3 步中创建此 ID（在下面的本节中讨论）。设置工作场所 ID 后，用户可以直接访问公司的自定义 URL（例如 www.klaviyo.com/sso/workplace/<id>）来登录 Klaviyo。我们建议告诉用户将此 URL 添加为书签以加快登录过程。 - ID 不能超过 63 个字符。 - ID 必须是 URL 安全的，因此只能包含大写或小写字母、连字符 (-)、句点 (.)、下划线 (\_) 和波形符 (~)。 - ID应该简单且易于用户记住（例如您的公司名称）。 - 例如，Klaviyo 的工作场所 ID 是“Klaviyo”。</p>
<h3>关于即时 (JIT) 供应</h3>
<p>设置 SSO 后，您可以选择在 Klaviyo 中启用即时 (JIT) 配置。当用户添加到具有 JIT 配置的帐户时，用户将需要接受电子邮件中的邀请才能开始访问该帐户。请注意，启用 SSO 并打开 JIT 配置后，您只能更新 IdP 内的[用户的 Klaviyo 角色](https://help.klaviyo.com/hc/en-us/articles/115005231648)，而无法再更新 Klaviyo 内的任何角色。要更新角色，您需要在 IdP 内部执行此操作，或者暂时关闭 JIT 和 [SCIM](https://help.klaviyo.com/hc/en-us/articles/10952782535579) 以在 Klaviyo 内部进行更新。 <strong><em>*什么是 JIT？</strong></em>*</p>
<p>启用 JIT 配置后，IT 管理员不再需要为每个应用程序中的每个用户手动创建帐户。相反，只要用户拥有该应用程序的权限，系统就会在用户第一次尝试登录应用程序时创建用户帐户。例如，IT 管理员可以自动向其 IdP 中的所有用户授予 Klaviyo 访问权限，以便这些用户的帐户将在他们第一次通过其 SSO 门户或通过 Klaviyo 发起的登录登录到 Klaviyo 时自动创建。 ## 设置 SAML SSO</p>
<p>1. 在 Klaviyo 中，单击左下角的组织名称。 2. 单击<strong><em>*设置</strong><strong>。 3. 选择</strong><strong>安全</strong><strong>。 4. 单击</strong><strong>设置 SSO</strong></em>*。 （请注意，不需要多重身份验证。）</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28716331657371" alt="Klaviyo 中的安全选项卡" />
<p>5. 复制 <strong>Klaviyo SSO URL</strong> 和 <strong>受众 URI（服务提供商实体 ID）</strong> 以在下一部分中使用。 ![SSO 配置页面顶部，您可以在其中复制 Klaviyo SSO URL 和受众 URI](https://klaviyo.zendesk.com/hc/article_attachments/28716354655515)</p>
<h2>登录到您的 SSO 提供商</h2>
<p>打开下面的下拉菜单以获取特定于 IdP 的说明。一般来说，您需要：</p>
<p>1. 打开一个新选项卡并登录到您的 SSO 提供商。 2. 找到您的提供商的确认设置。 3. 粘贴 Klaviyo SSO URL 并保存。 4. 下载或找到您的 IdP 元数据。 5. 将用户及其角色分配给 Klaviyo 应用程序。 - 为了让您的角色正确传递到 Klaviyo，我们建议使用密钥格式。 （一些 IdP 在其协议中将属性转换为小写，因此不建议使用标签格式）</p>
<p>|  |  |</p>
<p>| --- | --- |</p>
<p>| <strong><em>*帐户用户角色</strong><strong> | </strong><strong>投资组合用户角色</strong></em>* |</p>
<p>|业主|投资组合\_owner |</p>
<p>|管理员 |投资组合\_admin |</p>
<p>|经理 |投资组合\_经理 |</p>
<p>|分析师 |投资组合\_分析师 |</p>
<p>|活动\_协调员|  |</p>
<p>|内容创建者 |  |</p>
<p>|支持|  |</p>
<p>这些角色取决于您设置 SSO 的帐户类型。在普通帐户中，仅[帐户用户角色](https://help.klaviyo.com/hc/en-us/articles/115005231648)适用。在投资组合账户中，仅[投资组合用户角色](https://help.klaviyo.com/hc/en-us/articles/25181702319643)适用</p>
<p><strong><em>*奥克塔</strong></em>*</p>
<p>1. 登录您的 Okta 管理员帐户。 2. 导航至<strong><em>*应用程序 > 应用程序</strong><strong>。 3. 选择</strong><strong>创建应用程序集成</strong></em>*。 ![Okta 中的应用程序页面，您可以在其中创建应用程序集成](https://klaviyo.zendesk.com/hc/article_attachments/28716331667611)</p>
<p>4. 在模式中，选择<strong><em>*SAML 2.0</strong></em>* 选项。 ![选择 SAML 2.0 时的登录选项](https://klaviyo.zendesk.com/hc/article_attachments/28716354670747)</p>
<p>5. 单击<strong><em>*下一步</strong></em>*。 6. 为集成命名（例如“Klaviyo”）。 ![Okta 集成向导的第 1 步，您可以在其中命名应用程序](https://klaviyo.zendesk.com/hc/article_attachments/28716331685403)</p>
<p>7. 单击<strong><em>*下一步</strong><strong>。 8. 在 </strong>单点登录 URL<strong> 字段中，粘贴 Klaviyo SSO 设置屏幕中的 </strong>Klaviyo SSO URL<strong>。 9. 在 </strong>受众 URI（SP 实体 ID）<strong> 字段中，粘贴来自 Klaviyo 的 </strong>受众 URI（服务提供商实体 ID）<strong>。 10. 将 </strong>名称 ID<strong> 格式字段设置为 </strong><strong>电子邮件地址</strong><strong>。 11. 将 </strong>应用程序用户名<strong> 更改为 </strong><strong>电子邮件</strong><strong>。 12. 检查</strong>更新应用程序用户名<strong>设置为</strong><strong>创建并更新</strong></em>*。 ![Klaviyo 集成的 SAML 配置设置](https://klaviyo.zendesk.com/hc/article_attachments/28716354798619)</p>
<p>13. 单击<strong><em>*下一步</strong><strong>。 14. 选择 </strong><strong>我是 Okta</strong><strong> </strong><strong>添加内部应用程序的客户</strong><strong>。 - 您无需检查或填写此页面上的任何其他信息。 15. 滚动到页面底部并单击</strong><strong>完成</strong><strong>。 16. 转到</strong><strong>登录</strong></em>*选项卡。 ![Okta 中应用程序的登录选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28716354685211)</p>
<p>17. 向下滚动到 <strong>SAML 签名证书</strong> 部分。 18. 找到有效证书，然后单击<strong><em>*操作</strong><strong>下拉列表。 19. 单击</strong><strong>查看 IdP 元数据</strong></em>*。 ![选择查看 IdP 元数据时的操作下拉列表](https://klaviyo.zendesk.com/hc/article_attachments/28716354687515)</p>
<p>20. 将打开一个新选项卡，应如下所示。 ![XML 元数据页面示例](https://klaviyo.zendesk.com/hc/article_attachments/28716331703067)</p>
<p>21. 在新选项卡中，右键单击并选择<strong><em>*另存为>保存</strong><strong>，以便稍后可以将此文件上传到Klaviyo。 22. 导航回 Okta。 23. 转到</strong><strong>作业</strong><strong>选项卡。 24. 单击</strong><strong>分配</strong></em>*。 25. 选择是将应用程序分配给个人（即人员）还是组。 ![按人员或组将用户分配到应用程序的选项](https://klaviyo.zendesk.com/hc/article_attachments/28716354673435)</p>
<p>26. 找到您想要为其分配 Klaviyo 的人员或组，然后单击其姓名旁边的<strong><em>*分配</strong></em>*。 ![通过“人员”选项分配用户的示例](https://klaviyo.zendesk.com/hc/article_attachments/28716331705371)</p>
<p>27. 如果您选择个人：</p>
<ul>
<li>为每个人选择用户名；默认是他们在 Okta 中的用户名。 - 单击****保存并返回****。！[将用户名分配给个人的模式](https://klaviyo.zendesk.com/hc/article_attachments/28716331709211)</li>
</ul>
<p>28. 完成后，单击<strong><em>*完成</strong><strong>。 </strong><strong>一次登录</strong></em>*</p>
<p>1. 登录您的 One Login 帐户。 2. 导航至<strong><em>*应用程序 > 应用程序</strong></em>*。 ![突出显示子项应用程序时的应用程序下拉菜单](https://klaviyo.zendesk.com/hc/article_attachments/28716331678363)</p>
<p>3. 点击右上角<strong><em>*添加应用</strong></em>*。 ![选择添加应用程序时一次登录的应用程序页面](https://klaviyo.zendesk.com/hc/article_attachments/28716331682971)</p>
<p>4. 搜索“Klaviyo”，然后选择出现的结果。 ![在一次登录应用程序中搜索 Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28716354700443)</p>
<p>5. 可选：选择显示名称、上传新图标或添加此应用程序的说明。 6. 单击右上角的<strong><em>*保存</strong><strong>。 7. 导航至左侧边栏中的</strong><strong>配置</strong></em>*。 ![没有任何信息的配置页面](https://klaviyo.zendesk.com/hc/article_attachments/28716331718427)</p>
<p>8. 在 <strong>SAML Consumer URL</strong> 字段中，粘贴您的 <strong>Klaviyo SSO URL</strong>。 9. 在 <strong>受众 (SP 实体 ID)</strong> 字段中，粘贴您的 <strong>受众 URI（服务提供商实体 ID）</strong>。 10. 单击<strong><em>*保存</strong><strong>。 11. 单击左侧边栏中的</strong><strong>SSO</strong><strong>。 12. 打开 </strong>SAML 签名算法<strong> 下拉列表。 13. 选择</strong><strong>SHA-256</strong></em>*。 ![突出显示 SHA-256 时的 SAML 签名算法下拉列表](https://klaviyo.zendesk.com/hc/article_attachments/28716354710939)</p>
<p>14. 可选：向下滚动以更改您的登录显示设置。 ![一次登录应用程序的登录显示设置](https://klaviyo.zendesk.com/hc/article_attachments/28716331729179)</p>
<p>15. 单击<strong><em>*保存</strong><strong>。 16. 打开右上角的</strong><strong>更多操作</strong><strong>下拉菜单。 17. 选择</strong><strong>SAML 元数据</strong></em>*。这将下载您需要在下一部分中上传的文件。 ![突出显示 SAML 元数据时的更多操作下拉列表](https://klaviyo.zendesk.com/hc/article_attachments/28716331734939)</p>
<p>在继续下一部分之前，您需要在一次登录中将用户添加到 Klaviyo 应用程序，然后分配他们的角色。 18. 要将用户添加到 Klaviyo 应用程序，请单击左上角的<strong><em>*用户 > 用户</strong></em>*。 ![用户菜单下拉菜单](https://klaviyo.zendesk.com/hc/article_attachments/28716331739163)</p>
<p>19. 选择一个用户来访问 Klaviyo。我们建议指定在 Klaviyo 中设置 SSO 的人员。 20. 在左侧边栏中选择<strong><em>*应用程序</strong><strong>。 21. 单击右侧的加号按钮向该用户添加应用程序。 22. 从下拉列表中选择</strong><strong>Klaviyo</strong></em>*。 ![选择 Klaviyo 作为用户的应用程序](https://klaviyo.zendesk.com/hc/article_attachments/28716354727579)</p>
<p>23. 单击<strong><em>*继续</strong><strong>。 24. 在出现的模式中，向下滚动到 </strong>角色</em>* 下拉列表。 25. 打开此下拉列表并选择应分配给该用户的 [Klaviyo 角色](https://help.klaviyo.com/hc/en-us/articles/115005231648)。 ![为用户选择 Klaviyo 角色](https://klaviyo.zendesk.com/hc/article_attachments/28716331715099)</p>
<p>26. 单击<strong><em>*保存</strong><strong>。 </strong><strong>微软 Entra ID (Azure AD)</strong></em>*</p>
<p>1. 登录 Microsoft Entra ID（以前称为 Azure AD）。 2. 单击<strong><em>*Microsoft Entra ID</strong><strong>。 3. 选择</strong><strong>添加</strong><strong>下拉列表，然后单击</strong><strong>企业应用程序</strong><strong>。 4. 单击</strong><strong>创建您自己的应用程序</strong></em>*。 ![Microsoft Entra ID Gallery，您可以在其中创建应用程序](https://klaviyo.zendesk.com/hc/article_attachments/28716354728219)</p>
<p>5. 将应用程序命名为“Klaviyo”，然后单击<strong><em>*创建</strong><strong>。 6. 单击左侧边栏中的</strong><strong>单点登录</strong></em>*。 ![应用程序的单点登录方法页面，默认禁用](https://klaviyo.zendesk.com/hc/article_attachments/28716331767067)</p>
<p>7. 选择<strong><em>*SAML</strong><strong>。 8. 单击“</strong>基本 SAML 配置<strong>”框中的“</strong><strong>编辑</strong></em>*”。 ![基本 SAML 配置框，单点登录页面中的步骤 1](https://klaviyo.zendesk.com/hc/article_attachments/28716331749787)</p>
<p>9. 在出现的右侧边栏中，单击“<strong>标识符（实体 ID）</strong>”下的“<strong><em>*添加标识符</strong></em>*”。 ![为应用程序的 SSO 配置 SAML 的侧边栏](https://klaviyo.zendesk.com/hc/article_attachments/28716331753115)</p>
<p>10. 在出现的字段中，粘贴来自 Klaviyo 的 <strong>受众 URI</strong><strong>（服务提供商实体 ID）</strong>。 11. 在“<strong>回复 URL（断言消费者服务 URL）</strong>”下，单击“<strong><em>*添加回复 URL</strong><strong>”。 12. 在此处粘贴来自 Klaviyo 的 </strong>Klaviyo SSO URL</em>*。 ![添加标识符和回复 URL 后的 SAML 配置示例](https://klaviyo.zendesk.com/hc/article_attachments/28716331755419)</p>
<p>13. 注意：如果要添加 <strong>登录 URL</strong>，则必须首先创建工作场所 ID，这将在下一节中讨论。 我们建议完成设置过程，然后返回到此步骤。 14. 单击侧边栏左上角的<strong><em>*保存</strong><strong>，然后单击右上角的</strong><strong>X</strong><strong>。 15. 向下滚动到 </strong>SAML 证书<strong> 框（Entra 中 </strong>单点登录页面</em>* 上的步骤 3）。 ![单点登录页面第3步](https://klaviyo.zendesk.com/hc/article_attachments/28716354742555)</p>
<p>16. 在“<strong>联合元数据 XML</strong>”旁边，单击“<strong><em>*下载</strong></em>*”。 ![仅突出显示联合元数据 XML 选项的 SAML 证书框](https://klaviyo.zendesk.com/hc/article_attachments/28716354754203)</p>
<p>17. 仍在 <strong>SAML 证书</strong> 框中，单击右上角的<strong><em>*编辑</strong></em>*。 18. 在右侧显示的侧栏中，检查：</p>
<ul>
<li>**签名选项** 要求对 SAML 断言进行签名（此处，我们将其设置为 ****签署 SAML 断言****）。请注意，签署响应是可选的。 - **签名算法** 设置为 ****SHA-256****。！[编辑 SAML 证书签名选项和算法的侧边栏](https://klaviyo.zendesk.com/hc/article_attachments/28716331761307)</li>
</ul>
<p>19. 向上滚动到 <strong>属性和声明</strong> 框（Entra 中 <strong>单点登录页面</strong> 上的步骤 2），然后单击 <strong><em>*编辑</strong></em>*。 ![单点登录页面的第 2 步，即“属性和声明”框](https://klaviyo.zendesk.com/hc/article_attachments/28716354759579)</p>
<p>20. 单击“<strong>必需的声明</strong>”部分中的<strong><em>*唯一用户标识符（名称 ID）</strong></em>*。 ![管理索赔模式，其中突出显示唯一用户标识符行](https://klaviyo.zendesk.com/hc/article_attachments/28716354763419)</p>
<p>21. 单击<strong><em>*源属性</strong></em>*下拉列表。 ![唯一用户标识符的源属性字段](https://klaviyo.zendesk.com/hc/article_attachments/28716331779995)</p>
<p>22. 搜索“user.mail”，然后选择它。 ![搜索 user.mail 的源属性](https://klaviyo.zendesk.com/hc/article_attachments/28716354776347)</p>
<p>23. 点击左上角<strong><em>*保存</strong><strong>，返回</strong>属性和声明<strong>页面。 24. 选择左上角的</strong><strong>添加新声明</strong></em>*。 ![在属性和声明页面添加新声明](https://klaviyo.zendesk.com/hc/article_attachments/28716354779419)</p>
<p>25. 输入名称“角色”。 26. 将 <strong>源属性</strong> 更改为“user.signedroles”。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28716331810331" alt="Azure 14 新角色声明.png" />
<p>27. 单击<strong><em>*保存</strong><strong>。 28. 点击</strong><strong>Home</strong><strong> 返回目录。 29. 在左侧边栏中，单击</strong><strong>应用程序注册</strong></em>*。 ![左侧边栏中的应用程序注册选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28716354789659)</p>
<p>30. 转到<strong><em>*所有应用程序</strong></em>*选项卡。 ![应用程序注册页面中的所有应用程序选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28716354791707)</p>
<p>31. 单击进入 Klaviyo 应用程序。 32. 选择<strong><em>*应用程序角色 > 创建应用程序角色</strong></em>*。 ![在应用角色页面创建应用角色](https://klaviyo.zendesk.com/hc/article_attachments/28716354783003)</p>
<p>33. 为每个角色创建显示名称。 34. 选择<strong><em>*用户/组</strong><strong>作为</strong>允许的成员类型</em>*。 35. 按照如下所示准确分配这些值之一：</p>
<ul>
<li>管理员</li>
<li>经理</li>
<li>分析师</li>
<li>活动\_协调员</li>
<li>内容创建者</li>
<li>支持！[将用户指定为 Klaviyo 帐户所有者的示例](https://klaviyo.zendesk.com/hc/article_attachments/28716331794459)</li>
</ul>
<p>36. 添加描述，然后单击<strong><em>*应用</strong></em>*。然后，要将用户分配到 Klaviyo 应用程序，请按照以下步骤操作：</p>
<p>37. 导航到<strong><em>*Microsoft Entra ID > 企业应用程序</strong><strong>。 38. 单击</strong><strong>Klaviyo</strong><strong> 应用程序。 39. 导航到</strong><strong>用户和组> 添加用户/组</strong></em>*。 ![示例 Klaviyo 应用程序的用户和组页面](https://klaviyo.zendesk.com/hc/article_attachments/28716331802267)</p>
<p>40. 单击“<strong><em>*用户</strong></em>*”以填充右侧边栏。 ![为应用程序选择用户](https://klaviyo.zendesk.com/hc/article_attachments/28716354796443)</p>
<p>41. 选择您要添加到 Klaviyo 应用程序的用户。 42. 单击<strong><em>*选择</strong><strong>。 43. 单击进入</strong><strong>选择角色</strong></em>*。 ![为所选用户分配角色](https://klaviyo.zendesk.com/hc/article_attachments/28716331796635)</p>
<p>44. 选择该用户在 Klaviyo 中应具有的角色。 45. 单击<strong><em>*选择</strong><strong> 确认角色。 46. 单击左下角的</strong><strong>分配</strong></em>*。 ## 在 Klaviyo 中完成设置</p>
<p>1. 导航回 Klaviyo 选项卡的 <strong>SSO 设置</strong> 页面。 2. 选择：</p>
<ul>
<li>添加您的 IdP 颁发者和 SSO。 或者</li>
<li>上传包含此信息的文件。！[SSO 配置页面的第二步，您可以在其中添加有关 iDP 颁发者的信息](https://klaviyo.zendesk.com/hc/article_attachments/28716354659099)</li>
</ul>
<p>3. 为您的 SSO 登录创建您的 SSO 登录标识符（也称为工作场所 ID）；通常，这与您的公司名称相同。 - ID 不能超过 63 个字符。 - ID 必须是 URL 安全的，因此只能包含大写或小写字母、连字符 (-)、句点 (.)、下划线 (\_) 和波形符 (~)。 - ID应该简单且易于用户记住（例如您的公司名称）。 - 例如，Klaviyo 的工作场所 ID 是“Klaviyo”。！[SSO 配置页面的第三步，添加您的工作场所 ID](https://klaviyo.zendesk.com/hc/article_attachments/28716354664987)</p>
<p>4. 单击<strong><em>*测试 SSO</strong><strong>。 5. 选中</strong><strong>启用 SSO</strong></em>* 框。 6. 可选：选中以下一个或多个框。 - 要求所有用户进行 SSO。 - IdP 发起登录。 - 即时 (JIT) 配置。 ![设置后使用 SSO 的选项](https://klaviyo.zendesk.com/hc/article_attachments/28716354646811)</p>
<h2>结果</h2>
<p>现在您将能够使用 SSO 提供商登录 Klaviyo。</p>
