<h1>如何通过店面向 BigCommerce 客户发送消息</h1>

<h2>你将会学到</h2>
<p>了解如何通过店面向 BigCommerce 客户发送消息。如果您使用的是 BigCommerce 多店面 (MSF)，Klaviyo 会将名为“渠道 ID”的属性与每个订单事件同步，该事件告诉您客户与哪个店面进行了交互。此信息将添加到 Klaviyo 个人资料中，可用于对 Klaviyo 中的客户进行细分并向他们发送有针对性的消息。 ## 开始之前</p>
<p>在继续阅读本文之前，请确保您已[将 BigCommerce 商店与 Klaviyo 集成](https://help.klaviyo.com/hc/en-us/articles/115005082547)。请注意，并非 Klaviyo BigCommerce 集成的所有方面都与 BigCommerce Multi-Storefront 原生兼容，包括现场跟踪和注册表单。 Klaviyo 的店面特定消息传递功能仅限于使用通道 ID 记录事件的配置文件，如下所列。 ## 从 BigCommerce 同步的数据</p>
<p>渠道 ID 属性指示客户与哪个 BigCommerce 店面进行交互。 Klaviyo 会针对以下事件从 BigCommerce 同步渠道 ID 属性：</p>
<ul>
<li>开始结账</li>
<li>已下订单</li>
<li>订购的产品</li>
<li>已履行的订单</li>
<li>取消订单</li>
<li>已退款的订单</li>
</ul>
<p>任何跟踪上述事件之一的客户都将在其 Klaviyo 个人资料中添加 2 个与频道 ID 相关的属性：</p>
<ul>
<li>****BigCommerce 原始频道 ID****</li>
</ul>
<p>此属性列出配置文件访问的第一个店面的 ID。 - <strong><em>*BigCommerce 频道 ID</strong></em>*</p>
<p>ID 数组，其中包含配置文件访问的每个店面的 ID。要确定哪个店面对应于哪个渠道 ID：</p>
<p>1. 在每个店面下测试订单。 2. 在 Klaviyo 中，导航至<strong><em>*分析 > 指标</strong><strong>。 3. 按 </strong>BigCommerce<strong> 过滤。 4. 选择</strong><strong>已下订单</strong><strong> 事件，然后选择</strong><strong>活动源</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30880829241499)</p>
<p>5. 对于每个测试订单，单击三点菜单并选择<strong><em>*活动详细信息</strong></em>*。您将能够看到订单的渠道 ID。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30880829243419)</p>
<p>6. 记下哪个测试订单/店面对应于哪个渠道 ID。 ## 按店面细分客户</p>
<p>您可以通过执行以下操作为每个店面创建一个细分：</p>
<p>1. 在 Klaviyo 中，导航至<strong><em>*受众 ></strong><strong></em></strong><em>列表和细分<strong></em><em>。 2. 选择</strong><strong>新建 > 创建分段</strong><strong>。 3. 为您的细分命名具有描述性的名称（例如“[店面名称]客户”）。 4. 对于第一个分段条件，选择</strong><strong>有关某人的属性 > BigCommerce 原始渠道名称 > 等于 > [店面的渠道 ID]</strong><strong>。 </strong>类型<strong>应设置为</strong>数字<strong>。 5. 使用 </strong>AND<strong> 添加第二个分段条件。如果您希望向这些客户发送电子邮件，则此条件应该是</strong><strong>如果某人可以或不能接收营销>可以接收>电子邮件营销</strong></em>*。这可确保您所在细分市场中的客户可以收到营销电子邮件。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30880829246875)</p>
<p>6. 完成后，单击<strong><em>*创建分段</strong></em>*。请注意，此细分查看客户访问的第一个店面。 ### 未跟踪渠道 ID 的客户</p>
<p>您还可以为尚未跟踪渠道 ID 的 BigCommerce 客户创建另一个细分。如果有人在您的 BigCommerce 网站上填写了 Klaviyo 表单，但尚未开始结帐、下订单等，则可能会发生这种情况。您的细分条件将为<strong><em>*有关某人的属性> BigCommerce 原始渠道>未设置</strong><strong></em></strong><em>和<strong></em></strong><strong><em>如果某人可以或不能接收营销>可以接收>电子邮件营销</strong><strong>。确保将第一个条件的 </strong>Type<strong> 设置为 </strong>Text</em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30880785555227)</p>
<h2>通过店面向客户发送消息</h2>
<p>如果您只想向特定店面的订阅者发送消息，您可以为上面创建的其中一个细分创建[细分触发流](https://help.klaviyo.com/hc/en-us/articles/360003040052)，或[发送营销活动](https://help.klaviyo.com/hc/en-us/articles/115005054847)到该流程段。您还可以向所有订阅者发送消息，并按店面自定义该消息。下面，了解如何按店面创建一组欢迎消息，以及如何创建按店面个性化的废弃购物车流程。 ### 店面欢迎系列</p>
<p>要按店面创建欢迎系列流程，您需要改编[传统欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172)。首先，您需要创建单独的[细分触发流](https://help.klaviyo.com/hc/en-us/articles/360003040052)欢迎客户，每个流程均由上面的店面细分之一触发。然后，您可以将每条流消息个性化到特定的店面。对于已订阅营销但尚未跟踪频道 ID 的客户，请确保创建不特定于任何店面的额外欢迎系列流程。如果有人在您的 BigCommerce 网站上填写了 Klaviyo 表单，但尚未开始结帐、下订单等，则可能会发生这种情况。 ### 店面放弃购物车</p>
<p>您可以根据客户的关联店面向客户发送个性化的废弃购物车提醒。 1. 要创建流程，请从[废弃购物车提醒模板](https://www.klaviyo.com/library/flows?object_id=JmMG2t)开始。您将编辑此模板，并为每个店面进行条件分割。 2. 4 小时分割后，为第一个店面添加条件分割。将条件设置为 <strong><em>*BigCommerce 原始通道 > 等于 > [第一个通道 ID]</strong><strong>。将</strong>类型<strong>设置为</strong>数字</em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30880785557787)</p>
<p>3. 此分割的<strong>是</strong>路径应该是原始模板中的其余块。自定义此路径中通往您的第一个店面的流消息。对于<strong>否</strong>路径，您应该添加另一个具有相同条件的条件分割，但它应该设置为您的第二个店面。 4. 第二个 <strong>是</strong> 路径应该是第一个 <strong>是</strong> 路径内容的副本，但您应该自定义第二个店面的消息内容。 5. 继续以这种方式为每个店面添加条件分割。当您到达最后一个时，<strong>No</strong> 路径应该结束流程，不再有任何内容。这是因为跟踪 <strong>Started Checkout</strong> 事件的每个配置文件都应该有一个通道 ID，并被定向到 <strong>Yes</strong> 路径之一。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30882230895387)</p>
<h2>结果</h2>
<p>您现在已经了解了如何按店面细分 BigCommerce 客户并向他们发送有针对性的消息。</p>
