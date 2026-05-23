<h1>如何为 Shopify 创建废弃的“添加到购物车”流程</h1>

<p>了解如何创建由 Shopify <strong>添加到购物车</strong> 事件触发的废弃购物车流程。默认的 Klaviyo 放弃购物车流程由 Shopify <strong>结账开始</strong> 事件触发，而 <strong>添加到购物车</strong> 放弃购物车流程针对尚未开始结账的更多休闲购物者。</p>
<h2>开始之前</h2>
<p>为了启用此流程，您需要[启用 Klaviyo 应用嵌入](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZM0NY2336G80MJFM3) 并检查集成设置 <strong>跟踪行为事件</strong>，以便跟踪 Shopify 中的 <strong>添加到购物车</strong> 事件。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/35510459309467" alt="" />
<h2>创建流程</h2>
<p>要启用此流程，我们建议使用 Klaviyo 流程库中提供的预构建流程：</p>
<p>1. 导航到 Klaviyo 的 [流库](https://www.klaviyo.com/library/flows)。</p>
<p>2. 单击进入“防止销售损失”目标部分。</p>
<p>3. 选择<strong><em>*放弃购物车提醒、</strong><strong> </strong><strong>Shopify</strong><strong> </strong><strong>添加到购物车触发器</strong></em>* 流程。有两个选项：仅电子邮件，或电子邮件和短信。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/35545007778843" alt="" />
<img src="https://klaviyo.zendesk.com/hc/article_attachments/35545007792539" alt="" />
<p>4. 如果您启用了行为跟踪，则此流程将准备好使用所有推荐的过滤器和动态电子邮件内容，以支持个性化购物车后续消息传递。</p>
<h2>您是否使用 Klaviyo 的 Amazon Buy 与 Prime 集成？</h2>
<p>如果您使用 Buy with Prime 来支持商店中任何产品的付款和配送，并且您已[集成了 Klaviyo 和 Buy with Prime](https://help.klaviyo.com/hc/en-us/articles/14708088221467)，请确保执行以下操作：</p>
<p>对于已放弃的“添加到购物车”流程，请添加以下流程过滤器，以排除开始结账或通过“Buy with Prime”进行购买的客户接收到错误消息：</p>
<ul>
<li>**开始结账**（使用 Prime 购买）**自开始此流程以来零次**并且</li>
<li>**下订单**（使用 Prime 购买）**自开始此流程以来零次。**</li>
</ul>
<h2>结果</h2>
<p>您现在已为 Shopify 启用了废弃的 <strong>添加到购物车</strong> 流程。</p>
<h2>其他资源</h2>
<p><a href="https://klaviyo.zendesk.com/hc/en-us/articles/115002779411">如何创建废弃的购物车流程</a></p>
<p><a href="https://klaviyo.zendesk.com/hc/en-us/articles/4425956184731">如何为Shopify启用现场跟踪</a></p>
