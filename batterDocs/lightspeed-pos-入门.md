<h1>Lightspeed POS 入门</h1>

<h2>你将会学到</h2>
<p>了解如何将 Lightspeed Point of Sale 与 Klaviyo 集成，以及通过集成同步哪些数据。集成后，您将能够根据每个客户的线下购买和活动来个性化和定位电子邮件。 Lightspeed 集成每小时与 Klaviyo 同步一次。从Lightspeed同步的数据包括：</p>
<ul>
<li>销售和订单数据，包括购买了哪些产品、所属类别以及应用的任何折扣</li>
<li>客户信息，包括名字、姓氏和位置信息</li>
<li>已发货和退款的订单数据</li>
</ul>
<h2>开始之前</h2>
<p>此集成仅适用于 Lightspeed POS R 系列。使用 Lightspeed Retail X 系列？请参阅[将 Klaviyo 连接到 Retail POS](https://x-series-support.lightspeedhq.com/hc/en-us/articles/40831009276187-Connecting-Klaviyo-to-Retail-POS-X-Series) X 系列。 。 ## 目录</p>
<ul>
<li>如何与Lightspeed POS集成</li>
<li>验证您的同步数据</li>
<li>从 Lightspeed 同步的数据类型</li>
<li>结果</li>
<li>额外资源</li>
</ul>
<h2>如何与 Lightspeed POS 集成</h2>
<p>1. 在 Klaviyo 中，选择<strong><em>*集成</strong><strong>选项卡，然后单击</strong><strong>探索应用程序</strong><strong>。 2. 搜索 </strong>Lightspeed<strong> 并单击该卡，然后单击</strong><strong>安装</strong><strong>。 3. 单击</strong><strong>连接到 Lightspeed</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28705662705563)</p>
<p>4. 如果需要，登录 Lightspeed，然后单击<strong><em>*授权应用程序</strong></em>*。 5. 返回 Klaviyo，确认您的帐户 ID 正确。 6. 选择是否要将新的 Lightspeed 客户添加到 Klaviyo 列表，然后从下拉列表中选择一个列表。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28705662707739)</p>
<p>7. 完成后，单击<strong><em>*完成设置</strong></em>*。您应该会收到一条成功消息。 ## 验证您的同步数据</p>
<p>要检查您的 Lightspeed 集成：</p>
<p>1. 单击 Klaviyo 中的<strong><em>*分析</strong><strong>下拉列表，然后选择</strong><strong>指标</strong><strong>。 2. 按 Lightspeed 过滤并查找 </strong>已下订单<strong> 指标以验证是否已填充该指标的数据。初始集成数据同步最多可能需要几个小时，具体取决于您帐户中的数据量。 3. Klaviyo 将导入您所有的历史 Lightspeed 数据。为了验证这一点，您可以将 Klaviyo 中特定日期下的订单数量与 Lightspeed 界面中的订单数量进行比较，并确认它们匹配。例如，在探索 </strong>已下订单</em>* 指标时，您可以将鼠标悬停在昨天的数据点上或查看图表下方的数据表，以了解昨天报告了多少订单。将该数字与昨天存储在 Lightspeed 中的数字进行比较，您应该会看到它们完全匹配。 - 如果没有，问题很可能是您的 Klaviyo 帐户的时区与您的 Lightspeed 帐户的时区不匹配。要检查您在克拉维约的时区设置：</p>
<ul>
<li>单击左下角您的帐户名。 - 选择然后单击****设置 > 组织****。 - 向下滚动到**时区**。 ## 从 Lightspeed 同步的数据类型</li>
</ul>
<p>导航至<strong><em>*分析>指标</strong></em>*。带有 Lightspeed 图标的指标是从 Lightspeed 集成同步的。您可以使用右上角的过滤器功能来过滤所有 Lightspeed 指标。 Lightspeed 中的指标和配置文件属性是实时同步的，在 Lightspeed 中记录事件后的几秒钟内，您应该会看到它们出现在 Klaviyo 中。以下是从 Lightspeed 同步的所有指标的列表以及每个同步指标所包含数据的说明。 ![Klaviyo 中的指标页面由 Lightspeed 过滤，显示包含订购产品、已下订单、退款订单和已发货订单指标的列表](https://klaviyo.zendesk.com/hc/article_attachments/28705662703899)</p>
<p>请注意订单事件同步的以下例外情况：</p>
<ul>
<li>价值为 0 美元的订单将不会同步到 Klaviyo。 - 没有电子邮件地址的订单将不会同步到 Klaviyo。 ### 已下订单</li>
</ul>
<p>当客户完成结账流程并在您的实体店创建订单时，系统会跟踪此事件。 Klaviyo 跟踪的事件包括有关订单中所含商品的关键产品信息（例如产品名称和图像），以便您可以[在购买后续电子邮件中使用该信息](http://learn.klaviyo.com/14835-email-templates-advanced-use-cases/how-to-build-a-dynamic-table)。 您可以根据以下条件过滤和定位 <strong>已下订单</strong> 事件：</p>
<ul>
<li>****类别****</li>
</ul>
<p>每个产品所属的所有类别的名称，例如 <strong>T 恤、男装、裤子</strong> 和 <strong>促销</strong></p>
<ul>
<li>****折扣代码****</li>
</ul>
<p>有人在订单中使用的任何折扣或优惠券代码，例如 <strong>SPRING2015</strong></p>
<ul>
<li>****电子邮件域****</li>
</ul>
<p>下订单者的电子邮件域名，例如<strong>gmail.com</strong> 或 <strong>yahoo.com</strong></p>
<ul>
<li>****有折扣****</li>
</ul>
<p>这是正确还是错误</p>
<ul>
<li>****物品****</li>
</ul>
<p>某人订单中的产品名称，例如 <strong>T 恤</strong>或 <strong>裤子</strong></p>
<ul>
<li>****物品数量****</li>
</ul>
<p>订单中的商品总数，例如 <strong>2</strong></p>
<ul>
<li>****商店****</li>
</ul>
<p>下订单的商店名称，例如<strong>Klaviyo-波士顿</strong>或 <strong>Klaviyo-纽约</strong></p>
<ul>
<li>****商店ID****</li>
</ul>
<p>下单的店铺ID</p>
<ul>
<li>****总折扣****</li>
</ul>
<p>任何已应用的优惠券或折扣的总金额，例如 <strong>10.00</strong></p>
<h3>订购的产品</h3>
<p>当客户下订单时，系统会跟踪此事件 - 与 <strong>已下订单</strong> 事件不同，系统会针对某人在单个订单中购买的每件商品跟踪一个 <strong>订购产品</strong> 事件。例如，如果有人购买一件 T 恤和一条裤子，则会跟踪一个 <strong>下订单</strong> 事件和两个 <strong>订购产品</strong> 事件 - 一个 T 恤事件和一个裤子事件。 Klaviyo 跟踪的 <strong>订购产品</strong> 事件包括有关每件购买商品的详细信息。此详细的商品数据可用于根据产品变体选项和 <strong>已下订单</strong> 事件中不可用的其他信息创建行为细分。您可以根据以下条件过滤和定位<strong>订购的产品</strong>事件：</p>
<ul>
<li>****类别****</li>
</ul>
<p>产品所属类别的名称，例如<strong>销售</strong></p>
<ul>
<li>****电子邮件域****</li>
</ul>
<p>下订单者的电子邮件域名，例如<strong>gmail.com</strong> 或 <strong>yahoo.com</strong></p>
<ul>
<li>****姓名****</li>
</ul>
<p>产品的名称或标题，例如 <strong>The Jungle Book DVD</strong></p>
<ul>
<li>****产品 ID****</li>
</ul>
<p>商品的产品 ID，例如 <strong>2222</strong></p>
<ul>
<li>****数量****</li>
</ul>
<p>购买的数量，例如 <strong>2</strong></p>
<h3>订单退款</h3>
<p>当客户完成结账流程并进行付款，但客户要求退回付款时，系统会跟踪此事件。 Klaviyo 跟踪的事件包括有关所购买商品的所有关键产品信息，包括产品名称、图像和折扣信息。您可以根据以下条件过滤和定位<strong>退款订单</strong>事件：</p>
<ul>
<li>****类别****</li>
</ul>
<p>每个产品所属的所有类别的名称，例如 <strong>T 恤、男装、裤子</strong> 和 <strong>促销</strong></p>
<ul>
<li>****折扣代码****</li>
</ul>
<p>有人在订单中使用的任何折扣或优惠券代码，例如 <strong>SPRING2015</strong></p>
<ul>
<li>****电子邮件域****</li>
</ul>
<p>下订单者的电子邮件域名，例如<strong>gmail.com</strong> 或 <strong>yahoo.com</strong></p>
<ul>
<li>****有折扣****</li>
</ul>
<p>这是正确还是错误</p>
<ul>
<li>****物品****</li>
</ul>
<p>某人订单中的产品名称，例如 <strong>T 恤</strong>或 <strong>裤子</strong></p>
<ul>
<li>****物品数量****</li>
</ul>
<p>订单中的商品总数，例如 <strong>2</strong></p>
<ul>
<li>****总折扣****</li>
</ul>
<p>任何已应用的优惠券或折扣的总金额，例如 <strong>10.00</strong></p>
<h3>已发货订单</h3>
<p>当客户订单完成并正在发货时，系统会跟踪此事件。 Klaviyo 跟踪的事件包括有关所购买商品的所有关键产品信息，包括产品名称、图像和折扣信息。您可以根据以下条件过滤和定位 <strong>已发货订单</strong> 事件：</p>
<ul>
<li>****物品****</li>
</ul>
<p>某人订单中所有产品的名称，例如 <strong>T 恤、</strong> <strong>裤子</strong></p>
<ul>
<li>****收藏****</li>
</ul>
<p>某人订单中的全套产品系列，例如<strong>T 恤、男装、裤子</strong>和<strong>促销</strong></p>
<ul>
<li>****折扣代码****</li>
</ul>
<p>有人在订单中使用的任何折扣或优惠券代码，例如 <strong>SPRING2015</strong></p>
<ul>
<li>****总折扣****</li>
</ul>
<p>如果有人使用代码，则任何优惠券或折扣的总金额，例如 <strong>10.00</strong></p>
<p>对于 <strong>已发货订单</strong> 指标，只有当订单状态更改为“已发货”= true 时，我们才会将订单同步为已发货。默认情况下，只能通过在 Lightspeed 中手动单击按钮来设置此发货状态。此外，与客户无关的发货将不会同步。当销售中未指定客户时，可能会发生这种情况。 ### 客户数据</p>
<p>除了上述指标之外，每个 Klaviyo 配置文件中还添加了来自 Lightspeed 的属性。您可以在段和流中使用这些属性。 以下是从 Lightspeed 自动同步的 Klaviyo 属性：</p>
<ul>
<li>电子邮件</li>
<li>名字和姓氏</li>
<li>公司和头衔</li>
<li>城市</li>
<li>州/地区</li>
<li>邮政编码</li>
<li>国家</li>
</ul>
<p>默认情况下，通过 Lightspeed 集成在 Klaviyo 中创建的新配置文件不会触发欢迎系列流程。这是为了防止回头客可能会像首次客户一样通过 Klaviyo 收到欢迎电子邮件。如果您希望更改此功能，请[联系 Klaviyo 支持](https://klaviyo.zendesk.com/hc/en-us/articles/115001002272)。 ## 结果</p>
<p>您已与 Lightspeed POS 集成并查看了同步数据。您现在可以根据每个客户的线下购买和活动来个性化和定位电子邮件。 ## 其他资源</p>
<ul>
<li>[如何在没有预构建 Klaviyo 集成的情况下集成平台](https://developers.klaviyo.com/en/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration)</li>
<li>[集成常见问题解答](https://help.klaviyo.com/hc/en-us/articles/115005081007)</li>
</ul>
