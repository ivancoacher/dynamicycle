<h1>如何与 Chargebee 集成</h1>

<h2>你将会学到</h2>
<p>了解如何将 Chargebee 与 Klaviyo 集成，以便根据客户的发票和付款数据个性化和定位消息传递。以下数据从 Chargebee 同步到 Klaviyo：</p>
<ul>
<li>开具发票时，以及每张发票中包含的项目</li>
<li>用户支付失败、退款、支付成功时的支付信息</li>
</ul>
<h2>添加 Chargebee 集成</h2>
<p>1. 在 Klaviyo 中，选择<strong><em>*集成</strong><strong>选项卡。 2. 选择</strong><strong>探索应用程序</strong><strong>，搜索</strong>Chargebee<strong>，然后单击该卡。然后，单击</strong><strong>安装</strong></em>*。 3. 在下一页上，输入您的 Chargebee URL 的子域。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720758388507)</p>
<p>4. 输入您的 Chargebee API 密钥。 5. 单击<strong><em>*连接到 Chargebee</strong></em>*。 ## 监控 Klaviyo 同步并验证数据</p>
<p>要检查从集成同步的数据：</p>
<p>1. 单击 Klaviyo 中的<strong><em>*分析</strong><strong>下拉列表，然后选择</strong><strong>指标</strong><strong>。 2. 按 Chargebee 过滤。 3. 查找 Chargebee 的 </strong>已签发发票<strong> 指标，然后单击 </strong><strong>活动源</strong></em>* 图标。 ![Klaviyo 中 Chargebee 开具发票指标的活动源，显示指标示例](https://klaviyo.zendesk.com/hc/article_attachments/28720770263707)</p>
<p>4. 如果您的集成已开始同步数据，您将看到添加到此活动源的 <strong>已签发发票</strong> 事件。 Klaviyo 导入您的所有 Chargebee 数据。要验证这一点，您可以将特定日期的成功付款数量与 Chargebee 界面中的数量进行比较，并确认它们匹配。 1. 在 Klaviyo 中，导航至 <strong><em>*Analytics</strong><strong> </strong><strong>></strong><strong> </strong><strong>Metrics</strong><strong>。 2. 找到并单击“</strong><strong>成功支付</strong></em>*”指标，将进入指标图表页面，您可以在其中查看最近 30 天的数据。 3. 将鼠标悬停在前一天的数据点上或查看图表下方的数据表，了解您昨天有多少笔付款。 4. 将该数字与 Chargebee 中存储的数据进行比较，您应该看到它们匹配。 ![Klaviyo 中的 Chargebee 开具发票指标图表，显示一段时间内的发票数量](https://klaviyo.zendesk.com/hc/article_attachments/28720758383899)</p>
<h2>从 Chargebee 同步的数据</h2>
<h3>Chargebee 指标</h3>
<p>以下指标从 Chargebee 同步到 Klaviyo：</p>
<ul>
<li>****激活订阅****</li>
</ul>
<p>此指标记录订阅从“试用”状态转变为“活动”状态的时间。 - <strong><em>*取消订阅</strong></em>*</p>
<p>该指标记录取消订阅的时间。如果由于未付款或卡详细信息不存在而取消订阅，则订阅的可能原因为“cancel\_reason”。 - <strong><em>*创建订阅</strong></em>*</p>
<p>此指标记录新创建订阅的时间。 - <strong><em>*付款失败</strong></em>*</p>
<p>此指标记录 Chargebee 中付款被标记为失败时的事件。通过此指标，您可以定位未能付款的客户，并让他们知道他们有逾期余额。 - <strong><em>*开具发票</strong></em>*</p>
<p>每次通过 Chargebee 向客户开具发票时，此指标都会记录一个事件。此指标对于细分已开具发票但尚未付款或付款失败的客户非常有用。它还可用于触发分段以通知客户即将付款。 - <strong><em>*退款</strong></em>*</p>
<p>该指标记录您通过 Chargebee 退款时的事件。 - <strong><em>*支付成功</strong></em>*</p>
<p>每次客户通过 Chargebee 成功支付发票时，该指标都会记录一个事件。这些事件将包括有关您的客户、他们的发票以及发票中的产品的数据。这对于在客户付款后向其发送自动发票，或使用电子邮件流来确定客户何时在您的网站上活跃但尚未为您的产品或服务付款非常有用。您可以向这些用户发送电子邮件，提供在您的网站上购物的折扣。 ### 客户数据</p>
<p>除了 Klaviyo 从 Chargebee 同步的指标之外，如果 Chargebee 中存在电子邮件地址但 Klaviyo 中不存在，我们将为该人创建一个新的 Klaviyo 个人资料。该个人资料将包括以下信息：</p>
<ul>
<li>****一般联系方式****名字、姓氏、公司、电话号码</li>
<li>****自定义属性****Chargebee 卡状态、付款类型、付款状态和 Chargebee 订阅状态\*</li>
</ul>
<p>\*请注意，Chargebee 订阅状态属性可能无法准确反映最新的订阅状态。 ## 结果</p>
<p>您现在已与 Chargebee 集成并查看了从 Chargebee 同步到 Klaviyo 的数据。现在，您可以使用 Chargebee 数据根据客户的发票和付款数据来个性化和定位消息传递。 ## 其他资源</p>
<ul>
<li>[Klaviyo 和应用程序参考之间交换的信息](https://help.klaviyo.com/hc/en-us/articles/360030696012)</li>
</ul>
