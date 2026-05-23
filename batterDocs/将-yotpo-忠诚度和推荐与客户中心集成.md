<h1>将 Yotpo 忠诚度和推荐与客户中心集成</h1>

<p>本文概述了客户中心的 Yotpo 忠诚度和推荐集成，它允许您直接在网站上提供本机忠诚度体验。通过将 Yotpo 与客户中心集成，购物者无需离开商店或与第三方小部件交互即可查看自己的积分、跟踪 VIP 状态并兑换奖励。</p>
<h2>集成的好处</h2>
<ul>
<li>****减少摩擦****：购物者可以完全在客户中心内完成忠诚度操作（例如兑换），减少重定向并保持他们在现场的参与度。</li>
<li>****统一的品牌体验****：使用客户中心的基本布局和语音呈现忠诚度信息，创造一个有凝聚力的购买后旅程。</li>
<li>****提高可见性****：向登录会员和非会员展示忠诚度价值，以推动计划注册和保留。</li>
</ul>
<h2>开始之前</h2>
<p>要启用此集成，请确保您拥有：</p>
<p>1. 一个活跃的 Yotpo 忠诚度和推荐帐户。</p>
<p>2. 客户中心位于您的网站上。</p>
<p>3.您的 Yotpo <strong><em>*API 密钥</strong><strong> 和 </strong><strong>GUID</strong></em>*。</p>
<p>4. Yotpo 内管理现有的 Yotpo x Klaviyo 集成，以同步配置文件属性和事件。</p>
<h2>如何启用 Yotpo 集成</h2>
<p>1. 在 Klaviyo 应用程序中，导航至 <strong><em>*KService > 客户中心</strong></em>*。</p>
<p>2. 打开<strong><em>*扩展设置</strong></em>*页面。</p>
<p>3. 从忠诚度提供商列表中选择 <strong><em>*Yotpo</strong></em>*。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/46364536700955" alt="屏幕截图 2026-02-06 1.38.57 PM.png" />
<p>4. 在必填字段中输入您的 Yotpo <strong><em>*API 密钥</strong><strong> 和 </strong><strong>GUID</strong></em>*（这些内容将被安全存储以方便后端 API 调用）。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/46364536706971" alt="屏幕截图 2026-02-06 1.39.04 PM.png" />
<p>5.<strong><em>*保存您的更改</strong></em>*。启用后，忠诚度体验将在中心内对您的客户可见。</p>
<h2>购物体验</h2>
<p>Yotpo 集成向客户中心添加了两个主要视图：</p>
<h3>1.“为你”忠诚总结</h3>
<p>当购物者打开客户中心时，他们将看到一个简洁的奖励摘要块。根据他们的状态，他们将看到：</p>
<ul>
<li>****当前积分余额****：他们的实时积分总数。</li>
<li>****VIP 等级****：他们当前的会员级别（例如铜牌、银牌、金牌）。</li>
<li>****最佳/下一个奖励****：突出显示他们当前有资格获得的最有价值的奖励或他们可以获得的下一个奖励。</li>
</ul>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/46365040867611" alt="屏幕截图 2026-02-06 1.50.30 PM.png" />
<h3>2.奖励页面</h3>
<p>为了更深入地了解，购物者可以导航到中心内的专用奖励页面来访问：</p>
<ul>
<li>****赚取方式****：有关如何累积更多积分的信息。</li>
<li>****可用奖励****：固定或可变兑换选项列表。</li>
<li>****中心内兑换****：购物者可以直接用积分兑换优惠券代码，然后显示该优惠券代码以供立即使用。</li>
<li>****推荐链接****：供购物者与朋友分享的独特链接。</li>
</ul>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/46365049996187" alt="屏幕截图 2026-02-06 1.50.15 PM.png" />
<h2>数据和配置文件属性</h2>
<p>该集成利用从 Yotpo 同步到 Klaviyo 的多个配置文件属性来个性化体验：</p>
<ul>
<li>`swell_point_balance`：显示客户当前的积分。</li>
<li>`swell_vip_tier_name`：表示客户当前的等级。</li>
<li>`swell_referral_link`：提供客户的唯一推荐 URL。</li>
<li>`swell_has_account`：确定购物者是否是您的忠诚度计划的会员。</li>
</ul>
<p>Customer Hub 还实时调用 Yotpo 的 API 以获取最新的计划详细信息，例如主动兑换选项和等级定义，确保购物者始终看到准确的数据。</p>
