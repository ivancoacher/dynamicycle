<h1>如何通过 Klaviyo 管理和分发 Punchh 优惠</h1>

<h2>你将会学到</h2>
<p>了解如何直接在 Klaviyo 中创建和管理 Punchh 奖励优惠，并将其与您现有的列表和细分绑定。这使您能够在使用 Klaviyo 处理分发、消息传递和归因的同时精心策划复杂的忠诚度体验。</p>
<h2>开始之前</h2>
<p>在 Klaviyo 中创建优惠之前，请确保您的 Punchh 帐户中已配置 Punchh 可兑换物品。</p>
<h2>创建报价</h2>
<p>第一步是在 Klaviyo 中定义 Punchh 活动的活动详细信息。</p>
<p>1. 在 Klaviyo 中，选择<strong><em>*集成</strong></em>*选项卡。</p>
<p>2. 单击您的 <strong><em>*Punchh</strong></em>* 集成。</p>
<p>3. 在<strong>优惠管理</strong>部分中，单击<strong><em>*创建优惠。</strong></em>*</p>
<img src="https://cdn.sanity.io/images/6ct6b26e/help-center-prod/4e973b74ddaacb1191bb086389870128a24d650c-3456x1688.png" alt="Punchh 集成设置页面显示连接详细信息、Webhook 设置、订阅者同步和优惠管理。" />
<p>4. 在 Klaviyo 中创建新的 Punchh 活动，并输入活动的 <strong>名称</strong> 和 <strong>开始日期</strong>。</p>
<ul>
<li>您最多可以选择未来 3 个月后的开始日期。</li>
</ul>
<img src="https://cdn.sanity.io/images/6ct6b26e/help-center-prod/5b2b23ec9dd3c4e3d5289ba079808e7b5eab647a-3456x1662.png" alt="营销平台“创建优惠”页面的屏幕截图，显示活动详细信息、可兑换分配的输入字段以及有关最终更改的警告。" />
<h2>分配可赎回项</h2>
<p>定义可兑换项后，您必须通过将客户映射到您的 Klaviyo 数据来决定哪些客户有资格获得哪种奖励。</p>
<p>1. 导航至优惠构建器的<strong><em>*分配可兑换</strong></em>*部分。</p>
<p>2. 在您的可兑换项和特定<strong><em>*Klaviyo 列表或细分</strong></em>* 之间创建映射。</p>
<p>您可以将单个可兑换项映射到单个 Klaviyo 列表或分段。</p>
<img src="https://cdn.sanity.io/images/6ct6b26e/help-center-prod/d9c301f2e461ce87b5bb2497be259fb3dadf8991-3456x1662.png" alt="Web 应用程序的“创建优惠”页面，显示“Punchh 活动详细信息”，其中包含“搜索可兑换”的打开下拉菜单和一条警告消息。" />
<h2>通过 Klaviyo 消息分发奖励</h2>
<p>创建报价后，Klaviyo 会自动将 Klaviyo 列表或分段中的配置文件同步到 Punchh 分段（如果 Punchh 中已存在）。当根据您的映射向配置文件发放奖励时，Klaviyo 会通过该配置文件的 Punchh 集成记录<strong><em>*获得的奖励</strong><strong>指标和</strong><strong>奖励</strong></em>*对象。</p>
<h3>使用已获奖励指标</h3>
<p>要使用 Klaviyo 分配 Punchh 奖励，您可以使用 <strong>获得的奖励</strong> 指标来触发自动流程，确保客户在符合条件时收到奖励通知。您还可以使用动态块在消息中包含奖励详细信息。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/50585012249755" alt="" />
<h3>使用奖励对象</h3>
<p>要使用 Klaviyo 分配 Punchh 奖励，您还可以使用 <strong>奖励</strong> 对象来触发自动流程并细分您的客户。您还可以使用动态块在消息中包含奖励详细信息。</p>
<p>例如，如果您想在客户的奖励到期之前向其发送提醒，您可以通过引用 <strong>ExpiringAt</strong> 属性，在 <strong>Reward</strong> 对象上设置[日期触发流](https://help.klaviyo.com/hc/en-us/articles/35146374047515#h_01JPTG7J0Q843B5XQGRMB6DVXM)。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/50585012251291" alt="" />
