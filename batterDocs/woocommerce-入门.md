<h1>WooCommerce 入门</h1>

<h2>你将会学到</h2>
<p>了解如何安装 Klaviyo WooCommerce 扩展并在您的 Klaviyo 帐户中启用 WooCommerce 集成。与 WooCommerce 集成的主要步骤是：</p>
<ul>
<li>在 WooCommerce 中安装 Klaviyo 扩展（也称为 Klaviyo 插件）。 - 在 Klaviyo 中启用 WooCommerce 集成。本文还指导您测试 WooCommerce 集成。 WooCommerce 集成将数据实时同步到 Klaviyo。 ![](https://fast.wistia.com/embed/medias/bsnk4fwstw/swatch)</li>
</ul>
<h2>开始之前</h2>
<p>如果您在 WordPress 中有活动的缓存插件或重定向插件，这些插件可能会干扰 Klaviyo 的集成并导致连接问题。我们建议在集成设置过程中禁用这些插件。还有其他设置问题吗？查看 [WooCommerce 集成问题排查](https://help.klaviyo.com/hc/en-us/articles/4515829067803)。强烈建议将 Klaviyo IP 添加到防火墙提供商的允许列表中，以最大程度地减少身份验证和配置问题。更多详情请查看【如何将Klaviyo集成流量IP地址列入白名单】(https://help.klaviyo.com/hc/en-us/articles/19143781289115)。 ## 在 WooCommerce 中安装 Klaviyo 扩展</p>
<p>Klaviyo 的 WooCommerce 扩展允许您向网站添加时事通讯注册表单、启用网站活动跟踪并获取有关人们何时开始结帐和查看产品的数据，以便您可以发送废弃的购物车电子邮件。我们的扩展还与高性能订单存储 (HPOS) 兼容。在开始之前，我们建议您登录您的 Klaviyo 和 WooCommerce 帐户。如果您有多个 Klaviyo 帐户，请注销您不希望与 WooCommerce 集成的任何帐户。 1. 在 WooCommerce 中，单击左侧导航栏中的 <strong><em>*WooCommerce</strong><strong> 选项卡，然后选择 </strong><strong>扩展</strong><strong>。 2. 搜索 </strong>Klaviyo<strong>，然后选择 </strong>Klaviyo for WooCommerce</em>* 以进入 WooCommerce Marketplace 中的 Klaviyo 扩展页面。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720771148059)</p>
<p>3. 单击<strong><em>*添加到购物车</strong><strong>。 4. 确保您已登录 WooCommerce Marketplace 帐户，然后查看。 5. 继续结账，进入订单确认页面，然后单击</strong><strong>添加到站点</strong><strong>。 6. 如果您的 WooCommerce Marketplace 帐户未连接到您的 WooCommerce 网站，请将您的商店 URL 复制粘贴到框中。如果已连接，请从下拉列表中选择您的站点。然后，单击</strong><strong>添加到站点</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720771150235)</p>
<p>7. 导航回您的 WooCommerce 管理员，然后选择 <strong><em>*插件</strong><strong>。滚动浏览已安装插件列表以找到 Klaviyo，然后单击</strong><strong>激活</strong><strong>。 8. 从左侧导航栏中选择</strong><strong>营销</strong><strong>，然后单击</strong><strong>Klaviyo</strong><strong>。 9. 单击</strong><strong>连接帐户</strong></em>*开始，然后继续下一部分。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33640943535515)</p>
<p>设置有问题吗？查看 [WooCommerce 集成问题排查](https://help.klaviyo.com/hc/en-us/articles/4515829067803)。 ## 在 Klaviyo 中启用 WooCommerce 集成</p>
<p>1. 如果出现提示，请登录 Klaviyo。您可以通过打开新选项卡、导航到 [Klaviyo 仪表板](https://www.klaviyo.com/dashboard/performance) 并检查帐户名称来确保登录到正确的 Klaviyo 帐户。如果您需要切换帐户，请单击<strong><em>*注销</strong><strong>，然后登录到正确的帐户后再继续。 2. 检查权限，然后单击</strong><strong>批准</strong></em>*授予权限。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33641463439899)</p>
<p>3. 在集成设置页面，确认帐户名是否正确。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33640943542555)</p>
<p>4. 选中<strong><em>*将电子邮件营销同意复选框添加到您的结帐页面</strong><strong>旁边的框，以轻松将此选项添加到您的 WooCommerce 网站。 - 从</strong><strong>将电子邮件订阅者添加到此列表</strong><strong>下的下拉列表中选择一个列表。如果下拉列表中没有可用的列表，请转到[列表和细分选项卡](https://www.klaviyo.com/lists) 创建一个新列表。任何在结账时通过复选框订阅的人都将被添加到此列表中。客户在结账时点击 </strong>提交订单<strong> 按钮后，同意书将发送至 Klaviyo。 - 在</strong><strong>电子邮件营销同意标签</strong><strong>下，输入您希望在结帐页面上的复选框旁边显示的同意语言。默认语言是 </strong>注册我以接收电子邮件更新和新闻</em>*。！[](https://klaviyo.zendesk.com/hc/article_attachments/28720759277979)</p>
<p>5. 如果您想将此选项添加到您的 WooCommerce 网站，请选中<strong><em>*将短信营销同意复选框添加到您的结账页面</strong><strong>旁边的框。请注意，如果[您的公司有年龄限制](https://help.klaviyo.com/hc/en-us/articles/17252552814875)，短信同意将不会同步到 Klaviyo。 - 从</strong><strong>将 SMS 订阅者添加到此列表中的下拉列表中选择一个列表。</strong><strong> 通过此复选框同意 SMS 营销的用户将订阅您选择的列表。客户在结帐期间单击 </strong>提交订单<strong> 按钮并在 WooCommerce 中创建订单后，同意书将发送至 Klaviyo。 - 在</strong><strong>短信营销同意标签</strong><strong>下，添加您希望在结帐页面上的复选框旁边显示的文本。 - 接下来，添加</strong><strong>短信同意披露文本</strong><strong>，这是 TCPA 合规性所必需的。使用默认的 Klaviyo 同意语言或添加您自己的同意语言。 6. 如果您希望使用处理时的汇率将所有未来的 </strong>已下订单<strong> 和 </strong>已订购产品<strong> 事件转换为选定货币，请选中</strong><strong>将所有货币转换为一种标准</strong><strong> </strong><strong>货币</strong><strong> 框，然后选择一种货币。更改此设置不会影响之前集成的数据。此设置不会更改您帐户上的默认货币。 7. 当您对这些设置感到满意时，单击</strong><strong>完成设置。</strong><strong> 您可以随时返回并编辑这些设置，方法是导航到</strong><strong>集成</strong><strong>选项卡并选择</strong><strong>WooCommerce</strong></em>*。恭喜！您的 WooCommerce 帐户现已连接到 Klaviyo。 ### 故障排除</p>
<p>如果您收到错误消息“无法通过获取订单计数来测试 API。计数无效”，这意味着当 Klaviyo 尝试验证 WooCommerce 集成并获取订单计数时，其 API 不会返回 Klaviyo 期望的值，或者根本不返回任何内容。由于集成尚未正式连接到 Klaviyo，这意味着它需要在 WooCommerce 内解决。要获取有关此错误的更多信息，请使用 Postman 等应用程序对订单计数端点进行 API 调用，这将更深入地了解传递给 Klaviyo 的内容。您需要的端点是：<strong>{customers-url}/wc-api/v1/orders/count</strong>将 {customers-url} 更改为您的 WooCommerce 商店 URL。 ## 测试您的 WooCommerce 集成</p>
<p>要测试您的集成，请访问您的网站并按照以下说明操作：</p>
<p>1. 将商品添加到您的购物车。 2. 进入结账页面。 3. 在结账页面填写您的电子邮件地址和电话号码。如果启用，请选中复选框以订阅电子邮件和短信营销。 4. 提交您的测试订单。 5. 检查以下内容（这些内容可能需要一两分钟才能更新）：</p>
<ul>
<li>**开始结账** 事件记录在 **最近数据**** 下。 - 在您为电子邮件和短信营销选择的列表中创建的个人资料。 - **下订单**事件记录在****最近数据****下。 ### 最近数据</li>
</ul>
<p>最近数据部分显示事件的最新实例。 ### 历史数据</p>
<p>处理历史同步时，历史数据进度栏会实时更新。 ## 后续步骤</p>
<p>恭喜您完成设置！设置并集成帐户后，就可以开始使用 Klaviyo 的核心功能了。完成此类别中的项目后，您就可以充分利用 Klaviyo 的功能了。请查看我们的 [Klaviyo 入门课程](https://academy.klaviyo.com/getting-started-with-klaviyo/1405979)，以确保您能够充分利用您的 Klaviyo 帐户。 ### 从废弃的购物车流程中重建购物车</p>
<p>您可以使用 WooCommerce 数据从废弃的购物车流程重建购物车。我们将在“开始结帐”事件中生成一个密钥，允许您创建一个链接，以便在客户通过此事件在另一台设备上触发的电子邮件返回购物车时重建客户的购物车。 您可以在由开始结账触发的“放弃购物车”流程电子邮件中使用以下 url 参数创建此链接：</p>
<p>````</p>
<p>/cart?wck_rebuild_cart={{ event.extra.CartRebuildKey }}</p>
<p>````</p>
<p>组装完成后，URL 应如下所示：</p>
<p>````</p>
<p>{{organization.url|trim_slash}}/cart?wck_rebuild_cart={{event.extra.CartRebuildKey}}</p>
<p>````</p>
<p>动态生成的产品标题链接直接从您在帐户设置中插入的 URL 中提取。如果需要，可以在电子邮件模板编辑器中更新此 URL。 ![Klaviyo 电子邮件模板编辑器中的按钮块显示按钮文本、购物车重建 URL、以灰色背景取消、以蓝色背景保存](https://klaviyo.zendesk.com/hc/article_attachments/28720759259675)</p>
<p>如果您使用 {{organization.url}} 链接到非安全 HTTP URL，则需要使用 HTTPS 手动添加 URL，以便正确重建购物车。 ## 扩展参考信息</p>
<h3>启用自动更新</h3>
<p>要启用自动更新：</p>
<p>1. 单击<strong><em>*插件</strong><strong>选项卡。向下滚动找到 </strong>Klaviyo<strong> 插件。 2. 单击</strong><strong>启用自动更新</strong></em>*。如果您愿意，您仍然可以从 WooCommerce Marketplace 手动[下载 Klaviyo WooCommerce 扩展](https://woocommerce.com/products/klaviyo-for-woocommerce/)。 ### 查找变更日志</p>
<p>每个新扩展更新的变更日志中都包含发行说明。您可以在 [Wordpress 插件目录](https://wordpress.org/plugins/klaviyo/#developers) 上查看我们的扩展的变更日志。 ### 如果我使用旧版 API 进行集成，如何将 WooCommerce 集成升级为实时？首先，请按照上述扩展安装步骤安装最新的 WooCommerce 扩展。接下来，为具有读/写权限的 v3 集成创建 REST API 密钥。这与您首次安装扩展时创建的旧版 API 密钥不同。通过在 WooCommerce 集成设置页面上选择<strong><em>*保存设置</strong></em>*来更新 Klaviyo 中的集成。请注意，为了使用 WooCommerce 的 API v3，您必须使用 WC 版本 3.5x 或更高版本以及 WP 版本 4.4 或更高版本。</p>
