---
id: "115005254948"
title: "如何从 Mailchimp 迁移"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254948-How-to-migrate-from-Mailchimp"
section: "Migrate from an email service provider"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-11T11:06:38Z"
language: "zh"
---
## 你将会学到

了解如何使用 Klaviyo 的 Mailchimp 集成将 Mailchimp 数据迁移到 Klaviyo。完全过渡到 Klaviyo 后，我们建议您删除 Mailchimp 集成。 Klaviyo 从 Mailchimp 同步以下数据：

- 订阅者信息（包括取消订阅和清理的联系人）
- Mailchimp 受众（同步到 Klaviyo 列表）
- 电子邮件接收、点击和打开
- Mailchimp 评级

## 开始之前

如果您的 Mailchimp 帐户当前已与 Shopify 商店集成，并且您已经[将 Shopify 与 Klaviyo 集成](https://help.klaviyo.com/hc/en-us/articles/115005080407)，请确保在将 Mailchimp 与 Klaviyo 集成之前断开 Mailchimp 与 Shopify 的连接。如果未能断开旧的集成，可能会导致双重选择加入电子邮件发送到您现有的订阅者列表。 ## 清单

从 Mailchimp 迁移到 Klaviyo 需要四个关键步骤：

1. 将您的电子商务平台与 Klaviyo 集成
2. 将 Mailchimp 与 Klaviyo 集成
3. 将电子邮件模板从 Mailchimp 迁移到 Klaviyo
4. 注销您的 Mailchimp 帐户

## 如何与 Mailchimp 集成

将您的 Mailchimp 帐户与 Klaviyo 集成可以获取您的所有联系人数据，包括联系人何时收到、打开和点击电子邮件。 1. 首先，您需要获取 Mailchimp API 密钥。我们建议专门为 Klaviyo 集成创建一个新密钥，但如果您愿意，也可以使用现有密钥。 2. 您可以通过以下方式获取 Mailchimp API 密钥：登录 Mailchimp，单击您的个人资料图标，然后导航至****帐户和账单 > 附加 > API 密钥****。 3. 单击 ****创建密钥****。 4. 为您的密钥命名，然后单击****生成密钥****。 5. 单击****将密钥复制到剪贴板****。然后，安全保存。 6. 从 Mailchimp 获取 API 密钥后，登录 Klaviyo。 7. 选择****集成****选项卡。 8. 单击****探索应用程序****并搜索 Mailchimp。单击 Mailchimp 卡，然后单击****安装****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/31880103276059)
9. 在设置页面上，将 Mailchimp API 密钥粘贴到指定字段中。 10. 单击****连接到 Mailchimp****。 11. 粘贴 API 密钥后，单击查看**高级选项**选项：
    - **收集 Mailchimp 活动的打开和点击数据** - 选中此选项以同步 Mailchimp 参与度。 - **从 Mailchimp 受众创建 Klaviyo 列表** - 选中此选项可同步所有现有的 Mailchimp 受众。 - **仅同步特定受众的联系人** - 选中此选项可仅同步特定 Mailchimp 受众。系统将提示您选择要同步的受众群体。您必须选中上一个选项以从 Mailchimp 受众创建**Klaviyo 列表**，此选项才能发挥作用。 ![Klaviyo 的 Mailchimp 集成设置页面，包含用于同步受众的选项](https://klaviyo.zendesk.com/hc/article_attachments/28723506902811)
12. 如果您在“高级”中选择“仅同步特定受众的联系人”，则您需要指定之前向其发送营销活动的所有受众 ID。即使不同的同步受众群体包含相同的联系人，如果营销活动最初并非发送给该受众群体，您也不会看到该营销活动的完整互动数据。 13. Klaviyo 只会同步状态为“已发送”的营销活动数据。状态为“正在发送”的广告活动的数据将不会同步。请注意，Klaviyo 不会同步整个活动；我们同步打开和点击数据，如果您希望在 Klaviyo 中重新创建 Mailchimp 活动，您可以在下面了解如何导出 Mailchimp 电子邮件模板。 14. 单击****连接到Mailchimp****后，数据将在几分钟内开始同步。 ## 同步频率

当您首次集成 Klaviyo 和 Mailchimp 时，我们将同步您的所有联系人和过去 90 天的活动数据。这称为历史同步，并且仅发生一次。历史同步后，Mailchimp数据同步到Klaviyo，如下：

- 现有观众每 30 分钟同步一次。 - 新受众和/或活动每 6 小时同步一次。 - 发送营销活动后，现有营销活动会同步以捕获收件人数据。 ## 查看您的 Mailchimp 数据

Klaviyo 会自动从 Mailchimp 同步所有联系人以及订阅信息（除非您选择 **仅同步特定受众的联系人**）。 您将看到联系人是否已订阅或取消订阅，并且已标记为“已清除”或已退回的联系人将被添加到您在 Klaviyo 的黑名单中。我们根据联系人是否在 Mailchimp 中订阅来订阅联系人，除非该个人资料已存在于 Klaviyo 中。如果配置文件已存在，我们将根据其时间戳使用更新的同意状态。如果您在与 Klaviyo 集成后删除 Mailchimp 中的联系人，则他们不会在 Klaviyo 中删除。如果在添加 Mailchimp 集成之前，Klaviyo 中已经存在一个配置文件作为活动配置文件，并且它已在 Mailchimp 中清理/退回，则它不会在 Klaviyo 中被抑制。要禁止这些联系人，您可以将它们从 Mailchimp 导出为 CSV 并将其上传到 Klaviyo 中的禁止列表。此外，我们的 Mailchimp 集成：

- 如果您选中了 **收集 Mailchimp 营销活动的打开和点击数据** 设置，则同步 Mailchimp 营销活动的打开和点击数据。 - 如果您选中了 **从 Mailchimp 受众创建 Klaviyo 列表** 设置，则从 Mailchimp 受众创建 Klaviyo 列表。 - 如果您选中了 **从 MailChimp 受众创建 Klaviyo 列表** 设置，则会同步 Mailchimp 评级。如果您仅同步特定受众的联系人，您的 Mailchimp 评级（即使对于那些已同步的联系人）也不会同步到 Klaviyo。 - 同步已完成发送并在过去 90 天内发送的营销活动的以下指标（不包括 A/B 测试一部分的营销活动）：
  - 单击电子邮件
  - 打开电子邮件
  - 收到电子邮件

请务必注意，只有姓名、电子邮件地址、Mailchimp 评级和联系人位置会同步；要迁移可能附加到 Mailchimp 中的联系人个人资料的自定义属性（标签），请参阅以下部分。 ## 将 Mailchimp 标签导入 Klaviyo

如果您使用 Mailchimp 标签来标记和组织联系人，则可以手动将这些标签导出和导入到 Klaviyo 中。 Klaviyo 的内置 Mailchimp 集成不会同步您的任何标签。 1. 首先导航至 Mailchimp 中的****管理联系人 > 标签****，查看要同步的特定标签。 2. 单击 **查看** 旁边的下拉菜单将为您提供“导出为 CSV”选项，以从 Mailchimp 导出您的分段。使用 Mailchimp 的指南了解有关导出具有特定标签的联系人的更多信息。 ![在 Mailchimp 的标签设置中，在 VIP 标签页面右侧选择“查看”菜单，并将鼠标悬停在“导出为 CSV”选项附近](https://klaviyo.zendesk.com/hc/article_attachments/28723506886043)
3. 从 Mailchimp 导出数据后，您可以[将其作为自定义属性导入 Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/1260806293150)。自定义属性附加到您的 Klaviyo 配置文件，您可以根据特定属性创建分段，或使用它们向您的流程添加过滤器或动态显示电子邮件内的数据。 ## 将您的电子邮件模板从 Mailchimp 迁移到 Klaviyo

Klaviyo 具有直观的拖放模板生成器，您可以使用它来重新创建 Mailchimp 模板。我们建议使用此方法来构建您的模板，因为它将确保它们针对移动设备进行了优化、响应灵敏，并且易于编辑和迭代。但是，如果您没有时间专门使用 Klaviyo 的模板生成器重新创建 Mailchimp 模板，则可以从 Mailchimp 导出电子邮件模板并将其导入 Klaviyo。此过程涉及编辑和更新电子邮件模板的原始 HTML。如果您想使用 Klaviyo 的拖放编辑器重新创建模板，请[查看我们的指南](https://klaviyo.zendesk.com/hc/en-us/articles/4407911841435) 以了解使用 Klaviyo 模板编辑器的诀窍。 ### 从 Mailchimp 导出您的模板

1. 在您的 Mailchimp 帐户中，导航到您想要迁移到 Klaviyo 的模板。在模板名称旁边的下拉列表中，选择****导出为 HTML****。 ![在 Mailchimp 的模板中，在页面右侧选择所需模板的“编辑”菜单，将鼠标悬停在“导出为 HTML”选项上](https://klaviyo.zendesk.com/hc/article_attachments/28723518563611)
2. 系统将提示您确认导出，并且 HTML 文件将保存到您的计算机。 ### 替换模板标签

Klaviyo 和 Mailchimp 使用不同的模板标签在电子邮件中插入动态内容。 例如，Mailchimp 中的“名字”标签与 Klaviyo 中的不同，因此将任何 Mailchimp 特定标签替换为相应的 Klaviyo 标签非常重要。最需要换出的标签是取消订阅标签。 1. 在将模板导入 Klaviyo 之前，您必须添加 {% unsubscribe %} 标签，因为 Klaviyo 不允许您上传没有取消订阅标签的 HTML 模板，除非它们用于交易电子邮件。 2. 要编辑模板中的标签，请在文本编辑器（例如 Sublime Text）中打开 HTML 文件。下面是其他常见 Mailchimp 标签及其相应的 Klaviyo 标签的表格。 |  |  |
| --- | --- |
| ****Mailchimp 标签**** | ****克拉维约标签**** |
| `*|UNSUB|*` | `{% 取消订阅 %}` |
| `*|FNAME|*` | `{{ 名字 }}` |
| `*|LNAME|*` | `{{ 姓氏 }}` |
| `*|列表：公司|*` | `{{ 组织名称 }}` |
| `*|电子邮件|*` | `{{ 电子邮件 }}` |
| `*|更新配置文件|*` | `{% manage_preferences %}` |
| `*|MC:主题|*` |这是电子邮件的主题行，在 Klaviyo 模板编辑器中针对每封电子邮件进行设置。 |
| `*|MC_PREVIEW_TEXT|*` |这是电子邮件的预览文本，在 Klaviyo 模板编辑器中针对每封电子邮件进行设置。 |

请参阅下面的**其他资源**，了解有关 Klaviyo 模板标签的更多信息。将标签替换为 Klaviyo 标签后，您可以保存 HTML 文件。 ### 将您的模板导入 Klaviyo

1. 在您的 Klaviyo 帐户中，单击****内容****下拉列表并选择****模板****选项卡，然后选择****导入模板****。 2. 在****导入模板****模式中，从您的计算机中选择 HTML 文件来上传您刚刚保存的文件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33047503255835)
3. 您可以在****预览****选项卡中查看电子邮件模板的预览。 4. 请注意，今后您将必须直接编辑 HTML 才能更改模板。 ## 注销您的 Mailchimp 帐户

如果您在删除集成之前开始清理 Mailchimp 中的联系人，这些联系人将在 Klaviyo 中被抑制。一旦您的 Mailchimp 帐户安全注销，请务必先删除集成，然后再清除 Mailchimp 中您不希望在 Klaviyo 中抑制的联系人。如果您禁用或删除 Mailchimp 集成，从 Mailchimp 同步到 Klaviyo 的受众和个人资料将不会在 Klaviyo 中删除。将所有数据移至 Klaviyo 后，您可以采取三个关键步骤来确保您不再需要 Mailchimp 帐户：

1. 确保您的注册表单和列表增长工具指向 Klaviyo，而不是 Mailchimp
2. 在 Klaviyo 中按照流程重新创建自动化
3.删除Mailchimp集成

### 注册表单和列表增长工具

如果您的 Mailchimp 帐户中有任何注册表单或注册表单活动，您将需要确保在 Klaviyo 中重新创建这些注册表单，以便您的列表在 Klaviyo 而不是 Mailchimp 中继续增长。您将无法将 Mailchimp 中创建的表单重定向到 Klaviyo。相反，您可以：

1. 使用 Klaviyo 注册表单生成器从头开始重新创建您的表单
2.使用与Klaviyo集成的第三方列表增长工具
3. 通过您的电子商务平台集成您的自定义表单

如果您使用第三方列表增长工具而不是 Mailchimp 的内置表单生成器，请确保它同步到 Klaviyo。 Klaviyo 与许多第三方列表增长工具集成。 [扫描我们的集成列表](https://help.klaviyo.com/hc/en-us/categories/115000874028-Other-Data-Integrations) 查找您正在使用的工具。如果您没有看到它列出，请考虑使用 Klaviyo 的[注册表单生成器](https://help.klaviyo.com/hc/en-us/articles/360026474752-Getting-started-with-signup-forms) 创建表单，或切换到其他第三方工具。请注意，默认情况下，所有 Klaviyo 列表都是双重选择加入的。要将列表更改为单一选择加入，请参阅我们的[双重选择加入流程指南](https://klaviyo.zendesk.com/hc/en-us/articles/115005251108)。如果您使用自定义编码表单，则可以确保这些联系人同步到 Klaviyo。为此，请确保您的自定义表单将新订阅者直接同步到您的电子商务平台，并且您的电子商务商店已与您的 Klaviyo 帐户集成。将所有注册表单更改为指向 Klaviyo 后，等待几天并在 Mailchimp 中观察您的受众。 如果您注意到订阅者仍在添加到这些受众中，则可能至少有一种形式仍需要更换。接下来，您需要关闭 Mailchimp 注册表单。为此，请转到安装表单的页面的代码并删除以

`<!-- 开始 Mailchimp 注册表单 -->`

并以

`<!--结束 mc_embed_sign-up-->`

### 电子邮件自动化

Klaviyo 将电子邮件自动化称为流程，并允许更高级和更有针对性的序列。在 Klaviyo 中重新创建这些内容非常重要，这样您就不需要继续使用 Mailchimp 发送触发电子邮件。要了解更多信息，请查看我们的[流程入门]指南(https://help.klaviyo.com/hc/en-us/articles/115002774932)。一旦您的 Klaviyo 流程上线，请关闭 Mailchimp 中的所有自动化功能，以确保您不会向他人重复发送电子邮件。 1. 为此，请单击特定活动旁边的****暂停并编辑****。 2. 然后，在弹出窗口中单击****暂停****。 ![Mailchimp 中的电子邮件活动，以深灰色选择“暂停”和“编辑”](https://klaviyo.zendesk.com/hc/article_attachments/28723518566555)

### 删除 Mailchimp 集成

一旦您将所有列表增长工具指向您的 Klaviyo 帐户、暂停您的 Mailchimp 自动化并启用您的 Klaviyo 流程，您就可以删除 Mailchimp 集成。在删除 Mailchimp 集成之前，请务必仔细检查一切是否按预期运行。在您的注册表单和其他列表增长工具中输入测试电子邮件，放弃购物车，然后注册您的时事通讯以触发欢迎系列。 1. 单击“****受众****”下拉列表，然后选择 Klaviyo 帐户中的“****个人资料****”选项卡，以确保个人资料中的信息反映所有正确的沟通。 2. 如果您注册的列表是双重选择加入的，请务必先确认您的电子邮件。 3. 完成这些步骤并完全迁移到 Klaviyo 后，您可以继续删除 Mailchimp 集成。选择****集成****选项卡。 4. 单击 Mailchimp 集成右侧的操作按钮。 5. 选择****删除集成****以删除集成。 ![为 Mailchimp 集成选择了“删除集成”的“集成”选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28723506904347)

## 结果

您现在已从 Mailchimp 迁移到 Klaviyo 并了解了切换电子邮件发送的最佳实践。 ## 其他资源

### 克拉维约资源

- [如何从其他电子邮件服务提供商迁移到 Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005082767)
- [模板标签和变量语法参考](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731)

### Mailchimp 资源

- [关于联系人评级](https://mailchimp.com/help/about-contact- ratings/)
- [查看或导出您的联系人](https://mailchimp.com/help/view-export-contacts/#View_or_Export_Tagged_Contacts)