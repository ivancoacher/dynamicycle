<h1>如何为 PrestaShop 创建独特的优惠券</h1>

<h2>你将会学到</h2>
<p>了解如何为您的 PrestaShop 商店创建独特的一次性优惠券，并在流程中使用它们来激励订阅者进行购买。为此，您首先需要在 PrestaShop 中创建优惠券，然后在 Klaviyo 中配置链接优惠券的设置。 PrestaShop 的唯一优惠券代码只能在流电子邮件或短信中使用，不能在活动或表单中使用。如果您想在活动中包含优惠券，请考虑上传唯一代码或使用[静态 PrestaShop 优惠券](https://help.klaviyo.com/hc/en-us/articles/19655157461403)。 <strong><em>*流程中独特优惠券的用例</strong></em>*</p>
<ul>
<li>****废弃的购物车****</li>
</ul>
<p>向之前未购买过的购物车放弃者发送仅在有限时间内（例如 2 至 4 天）有效的折扣代码，以营造紧迫感并鼓励休闲浏览者进行转化。 - <strong><em>*赢回</strong></em>*</p>
<p>向最近未购买的买家发送折扣代码，以激励他们再次购买。与废弃购物车优惠券逻辑类似，发送具有设定到期日期的优惠券可以营造紧迫感并促使购买。 - <strong><em>*欢迎系列</strong></em>*</p>
<p>新订阅者加入您的电子邮件列表后，立即向他们发送折扣代码。如果他们在 2 周后仍未购买，您可以发送另一个代码以增加奖励。 ## 开始之前</p>
<h3>Klaviyo 模块版本</h3>
<p>要在 PrestaShop 中使用独特的优惠券，您必须使用 Klaviyo 的 PrestaShop 模块版本 1.5.0。要将模块更新到最新版本：</p>
<p>1. 登录您的 PrestaShop 管理员。 2. 导航至<strong><em>*模块 > 模块管理器</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/35197586800923)</p>
<p>3. 滚动找到 Klaviyo 模块并选择<strong><em>*升级</strong></em>*。 ![PrestaShop中升级Klaviyo模块](https://klaviyo.zendesk.com/hc/article_attachments/28704479194139)</p>
<p>如果您从低于 1.3.0 的版本升级，升级前发送的废弃购物车电子邮件中使用的购物车重建链接将不再有效。但是，升级后发送的所有废弃购物车消息都将正常运行。要了解每个版本中所做的更改，请前往 [PrestaShop 插件市场中的 Klaviyo 模块](https://addons.prestashop.com/en/newsletter-sms/49837-klaviyo.html)，向下滚动到 <strong>新增功能</strong>，然后单击 <strong><em>*显示更改日志历史记录</strong><strong>。 #### </strong>购物车规则限制<strong>设置是什么？在 PrestaShop 的 Klaviyo 模块中，</strong>购物车规则限制<strong>设置允许您限制客户在单个订单上组合购物车规则代码的方式。默认情况下，此设置为 </strong>每个前缀一个购物车规则</em>*。这可以防止客户在结账时添加多个具有相同[前缀](#h_01HYDKX0A91K8ME4MZH60RXMCW)的代码。 ![PrestaShop Klaviyo 模块中的优惠券使用设置](https://klaviyo.zendesk.com/hc/article_attachments/28704479210395)</p>
<h3>整合</h3>
<p>此外，请确保您已将 Klaviyo 与 PrestaShop 集成，并且可以在 Klaviyo 左侧导航中的 <strong>内容</strong> 下查看 <strong>优惠券</strong> 选项卡。如果您已集成但没有看到 <strong>优惠券</strong> 选项卡：</p>
<p>1. 在 Klaviyo 左侧导航的左下角选择您的公司名称，然后选择<strong><em>*集成</strong><strong>。 2. 搜索 PrestaShop 并选择该卡。 3. 单击</strong><strong>更新设置</strong><strong>以更新您的集成设置。您现在应该在左侧导航栏中的 </strong>内容<strong> 下看到 </strong>优惠券</em>* 选项卡。 ## 在 PrestaShop 中创建您的优惠券</p>
<p>PrestaShop 中的优惠券称为 <strong>购物车规则</strong>。要在 PrestaShop 中创建新的购物车规则，请导航至 <strong>购物车规则</strong> 页面并选择 <strong><em>*添加新的购物车规则。</strong></em>*</p>
<p>创建购物车规则时，PrestaShop 有 3 个主要选项卡：</p>
<ul>
<li>****信息****</li>
</ul>
<p>设置购物车规则的标识符（例如名称）和主要设置。 - <strong><em>*条件</strong></em>*</p>
<p>设置优惠券应适用于哪些客户。 - <strong><em>*行动</strong></em>*</p>
<p>设置购物车规则的折扣和促销。 ![在 PrestaShop 中创建购物车规则 UI](https://klaviyo.zendesk.com/hc/article_attachments/28704487263643)</p>
<p>详细了解如何在 [PrestaShop 中创建购物车规则](https://docs.prestashop-project.org/1.7-documentation/user-guide/looking/managing-catalog/managing-discounts/cart-rules) 并查看每个字段的说明。在 PrestaShop 中创建价格规则后，您可以将其链接到 Klaviyo 中的优惠券。 ## 在 Klaviyo 中配置您的优惠券</p>
<p>现在您已经在 PrestaShop 中创建了购物车规则，您需要在 Klaviyo 中进行设置，以便为您的流程生成代码。 1. 在 Klaviyo 的左侧导航中导航至<strong><em>*内容 > 优惠券</strong><strong>。 2. 在顶部的菜单栏中，选择</strong><strong>PrestaShop</strong></em>* 选项卡。 ![Klaviyo 中创建的优惠券列表](https://klaviyo.zendesk.com/hc/article_attachments/28704487262491)</p>
<p>3. 选择<strong><em>*创建优惠券</strong></em>*。 4. 在 Klaviyo 中为优惠券设置以下属性：</p>
<ul>
<li>****姓名****</li>
</ul>
<p>在 Klaviyo 中为 PrestaShop 购物车规则创建一个名称。在消息中指定优惠券时将使用此名称。 - <strong><em>*购物车规则 ID</strong></em>*</p>
<p>输入来自 PrestaShop 的购物车规则 ID。 Klaviyo 在显示其他设置选项之前执行查找以确认购物车规则 ID 存在。这必须与 PrestaShop 中关联的购物车规则 ID 完全匹配。 - <strong><em>*前缀</strong></em>*</p>
<p>输入要应用于 PrestaShop 中生成的每个购物车规则的可选前缀。 Klaviyo 将为每个人生成一个随机代码，但您也可以指定在每 10 位代码之前包含一个前缀（例如，前缀 <strong>WELCOME20</strong> 将生成类似于 <strong>WELCOME20-0123456789</strong> 的代码）。 - <strong><em>*数量</strong></em>*</p>
<p>指定每天应发送的最少代码数。 Klaviyo 将使用该数字（必须介于 0 到 150,000 之间）自动生成每日代码库存。只要领取优惠券的客户数量不超过您设置的最低代码数量，您就无需补充优惠券代码。 - <strong><em>*活跃日期</strong></em>*</p>
<p>选择 PrestaShop 中的购物车规则何时生效。默认情况下，优惠券从创建代码的日期和时间起有效。即使在 PrestaShop 中购物车规则的<strong>条件</strong>选项卡上设置了有效日期，Klaviyo 中的<strong>有效日期</strong>也会覆盖 PrestaShop 设置。对于结束日期，您可以选择：</p>
<ul>
<li>****一定天数后****</li>
</ul>
<p>客户收到优惠券后的有效天数。 - <strong><em>*在特定日期</strong></em>*</p>
<p>优惠券将不再有效的特定日期和时间。 5. 单击<strong><em>*创建优惠券</strong></em>*。一旦您在 PrestaShop 中创建了优惠券并在 Klaviyo 中进行了配置，Klaviyo 将开始自动为您的流消息生成代码。以下是 Klaviyo 中正确配置优惠券的示例：</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28704487270555" alt="在Klaviyo中正确设置PrestaShop优惠券" />
<h2>连续使用您独特的优惠券</h2>
<p>创建并配置优惠券后，将其插入流消息中。 1. 导航至 Klaviyo 左侧导航栏中的<strong><em>*Flows</strong><strong> 选项卡。 2. 打开现有流程或[创建新流程](https://help.klaviyo.com/hc/en-us/articles/115002774932)。 3. 选择流程内的流程消息。 4. 打开所选流消息的消息编辑器。 5. 单击个性化图标。根据您的编辑器，您可能会看到一个人物图标或标有“</strong><strong>个性化</strong></em>*”的按钮。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39892625665947)</p>
<p>6. 从<strong>所有类型</strong>菜单中，选择<strong><em>*优惠券</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/39892625669787)</p>
<p>7. 选择您要添加的优惠券。 8. 可选：选择流程电子邮件上的<strong><em>*3 个点</strong><strong>，然后单击</strong><strong>预览</strong></em>*。请注意，当您直接在 Klaviyo 中预览电子邮件时，您将不会看到填充的唯一代码。相反，您会看到优惠券的名称带有“预览”连字符。 Klaviyo 只会在实际发送时创建和共享唯一代码。 ![预览模式下显示的带有优惠券标签的示例电子邮件。](https://klaviyo.zendesk.com/hc/article_attachments/39892625671195)</p>
<p>发送消息时，由您的前缀和 10 个随机数字组成的唯一折扣代码将动态替换每个收件人的变量。如果您在多条流消息中包含相同的优惠券标签，收件人每次都会收到相同的唯一代码。 ![优惠券前缀末尾添加了独特的10位代码](https://klaviyo.zendesk.com/hc/article_attachments/39892625674395)</p>
<p>实时流电子邮件的唯一优惠券代码会根据您在 <strong>优惠券详细信息</strong> 页面的 <strong>最低库存</strong> 部分中指定的数量自动生成。例如，如果您创建<strong>最低库存</strong>为 100 的优惠券，Klaviyo 会生成一批 100 个唯一代码。这些每天都会自动补充；但是，如果您在充值前使用了全部 100 个代码，则由于可用代码不足，将跳过第 101 次分配优惠券的尝试。 这会自动触发 Klaviyo 生成另外 100 个代码。由于流程的优惠券代码会自动补充，因此您无需通过<strong>添加代码</strong>选项手动添加批量优惠券代码。 ## 测试您的 Flow 电子邮件的优惠券</p>
<p>在将带有优惠券的流程发送给受众之前，我们建议您先进行测试。 1. 在流程构建器中，单击<strong><em>*查看并打开</strong><strong>。 2. 将状态更改为</strong>手动<strong>。 3. 单击</strong><strong>打开</strong><strong>。 4. 通过执行与您的流程相对应的触发操作来触发您的流程（例如，填写注册表单以加入某个列表）。完成触发操作后，您的流程将自动生成 100 张优惠券。优惠券可能需要几分钟才能生成代码。因此，加载缓冲区很短，您可能会在 </strong>跳过：重试生成代码<strong> 下看到您的测试配置文件。一旦优惠券生成完毕，这种情况就会消失。 5. 生成优惠券后，触发流程的测试电子邮件将显示在电子邮件的</strong>需要审核<strong>下。 6. 单击流消息的 </strong>收件人活动<strong> 下的 </strong>需求审核</em><em>*</em> 存储桶。 ![需要在流电子邮件的收件人活动中进行审核组](https://klaviyo.zendesk.com/hc/article_attachments/28704479202971)</p>
<p>7. 选择<strong><em>*立即发送</strong></em>*。 ![流程电子邮件的需求审核组中的个人资料立即发送按钮](https://klaviyo.zendesk.com/hc/article_attachments/28704479202203)</p>
<p>8. 检查您的收件箱中是否有包含唯一代码的电子邮件。 ## 常见优惠券问题故障排除</p>
<p>如果您在 Klaviyo 中为 PrestaShop 创建唯一优惠券时遇到问题，请执行以下建议的故障排除步骤。 #### 检查您的 Klaviyo 插件版本</p>
<p>Klaviyo 的 PrestaShop 独特优惠券功能需要 PrestaShop 的 Klaviyo 附加组件版本 1.5.0 或更高版本。您可以在 PrestaShop 中的 <strong><em>*Modules > Module Manager</strong><strong> 下检查 Klaviyo 插件的版本。如果您需要更新 Klaviyo 附加组件，请选择</strong><strong>升级</strong></em>*。 ![PrestaShop中升级Klaviyo模块](https://klaviyo.zendesk.com/hc/article_attachments/28704479194139)</p>
<h4>检查您的 PrestaShop 集成设置</h4>
<p>如果您与 PrestaShop 的集成未同步，或者您的 PrestaShop 商店无法访问，Klaviyo 将无法生成新的优惠券代码。要查看您的 PrestaShop 集成设置：</p>
<p>1. 在 Klaviyo 左侧导航的左下角选择您的公司名称，然后选择<strong><em>*集成</strong><strong>。 2. 搜索 </strong>PrestaShop<strong>，然后选择该卡。 3. 单击</strong><strong>更新设置</strong></em>*以更新您的集成设置。有关配置 Klaviyo 与 PrestaShop 集成的更多帮助，请参阅 [PrestaShop 入门](https://help.klaviyo.com/hc/en-us/articles/360054551492)。 #### 验证 PrestaShop 中是否存在购物车规则 ID</p>
<p>如果您收到一条错误，表明无法找到 PrestaShop 购物车规则 ID，则 Klaviyo 无法将指定的购物车规则 ID 与您的 PrestaShop 帐户中的规则 ID 进行匹配。要解决此问题，请更新优惠券的购物车规则 ID，确保其与 PrestaShop 商店中的现有购物车规则匹配。</p>
