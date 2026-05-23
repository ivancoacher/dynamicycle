<h1>如何将 Klaviyo 现场跟踪添加到您的预订引擎</h1>

<p>本指南将引导您使用 <strong><em>*Klaviyo Hotels Tag</strong><strong> 将 </strong><strong>Google Tag Manager (GTM)</strong><strong> 与您的物业管理系统（Mews、Cloudbeds 或 Guesty）集成。完成此设置后，您将能够直接在您的 Klaviyo 帐户中跟踪关键网站访问者行为，例如 </strong><strong>活跃现场、</strong><strong> </strong><strong>查看列表、</strong><strong> 和 </strong><strong>开始结账</strong><strong>。这将使您能够轻松设置创收自动化，例如浏览放弃和放弃的购物车流程，并创建高度针对性的细分。 </strong><strong>在开始之前，如果您还没有 Google 跟踪代码管理器帐户，请按照 Google 的</strong><strong> [</strong><strong>指南</strong><strong>](https://support.google.com/tagmanager/answer/14842164?hl=en) </strong><strong>了解如何设置帐户。</strong></em>*</p>
<p>---</p>
<h2>步骤 1：找到您的 GTM 容器 ID</h2>
<p>在开始之前，您需要确定要使用的特定容器。 1. 登录您的 [Google 跟踪代码管理器](https://tagmanager.google.com/) 帐户。 2. 选择与您酒店网站关联的<strong><em>*Container</strong><strong>。 3. 在窗口顶部的“提交”和“预览”按钮旁边，您将看到您的</strong><strong>容器 ID</strong><strong>（看起来像“GTM-XXXXXXX”）。 4.</strong><strong>将此 ID</strong></em>* 复制到剪贴板。 ![0.9.png](https://klaviyo.zendesk.com/hc/article_attachments/46643062813851)</p>
<p>---</p>
<h2>步骤 2：将 GTM 连接到您的物业管理系统 (PMS)</h2>
<p>您需要告诉您的预订引擎“监听”您的 GTM 容器。请按照以下适合您的特定平台的步骤操作：</p>
<h3>对于云床</h3>
<p>1. 登录 Cloudbeds。 2. 单击<strong><em>*帐户图标</strong><strong> > </strong><strong>设置 > 预订引擎</strong><strong>。 3. 选择</strong><strong>分析</strong><strong>选项卡</strong><strong>.</strong></em>*</p>
<p>4. 将您的<strong><em>*容器 ID</strong></em>* 粘贴到 GTM 字段中并保存。 ![2.png](https://klaviyo.zendesk.com/hc/article_attachments/46643062816923)</p>
<p>有关更多说明，请遵循 [Cloudbeds 指南](https://myfrontdesk.cloudbeds.com/hc/en-us/articles/25825202111387-Connect-Google-Analytics-with-Cloudbeds-Booking-Engine)。 ### 对于马厩</p>
<p>1. 登录Mews。 2. 转到<strong><em>*设置 > 服务</strong><strong>。 3. 选择可预订服务。 4. 单击</strong><strong>预订引擎</strong><strong>。 5. 选择您想要使用 Google 跟踪代码管理器跟踪的预订引擎。 6. 在 </strong><strong>Google 标签管理器 ID</strong><strong> 下，粘贴您的 </strong><strong>容器 ID。</strong></em>*</p>
<p>7. 单击<strong><em>*保存</strong></em>*。 ![3.png](https://klaviyo.zendesk.com/hc/article_attachments/46643094244763)</p>
<p>有关更多说明，请遵循 [Mews 指南](https://help.mews.com/s/article/google-tag-manager)。 ### 对于客人</p>
<p>1. 要在您的站点上安装代码：</p>
<p>2. 登录Guesty。 3. 选择顶部的<strong><em>*操作</strong><strong>下拉菜单，然后选择</strong><strong>增长 > 分布</strong></em>*。 5.![](https://klaviyo.zendesk.com/hc/article_attachments/46643062822683)</p>
<p>6. 选择<strong><em>*宾客预订引擎</strong><strong>。 7. 单击预订引擎旁边的三个点，然后选择</strong><strong>编辑预订引擎</strong><strong>。 8. 滚动到 </strong>Web 分析<strong> 部分并经过您的 </strong><strong>容器 ID</strong></em>*。 10. ![4.png](https://klaviyo.zendesk.com/hc/article_attachments/46643062823963)</p>
<p>11. 选择<strong><em>*保存预订引擎。</strong></em>*</p>
<p>如需更多说明，请遵循[宾客指南](https://help.guesty.com/hc/en-gb/articles/16714065345821-Using-analytics-tools-in-your-Guesty-Booking-Engine)。 ---</p>
<h2>步骤 3：在 GTM 中添加 Klaviyo Hotels 模板</h2>
<p>现在 GTM 已连接到您的 PMS，您需要添加 Klaviyo 特定的跟踪逻辑。 1. 返回 Google 跟踪代码管理器，单击左侧边栏上的<strong><em>*模板</strong><strong>。 2. 在</strong><strong>标签模板</strong><strong>部分中，单击</strong><strong>搜索库</strong><strong>。 3. 搜索</strong><strong>“Klaviyo 酒店标签”</strong></em>*。 ![6.png](https://klaviyo.zendesk.com/hc/article_attachments/46643094254363)</p>
<p>4. 选择模板并单击<strong><em>*添加到工作区</strong><strong>。 5. 再次单击</strong><strong>添加</strong></em>*进行确认。 ---</p>
<h2>步骤 4：创建并配置您的标签</h2>
<p>此步骤将模板连接到您的特定 Klaviyo 帐户。 1. 转到左侧边栏的<strong><em>*标签</strong><strong>，然后单击</strong><strong>新建</strong><strong>。 2. </strong><strong>为您的标签命名</strong><strong>（例如“Klaviyo Hotels Tracking”）。 3. 单击</strong><strong>标签配置</strong><strong>并选择您刚刚添加的</strong><strong>Klaviyo Hotels Tag</strong><strong>。 4. </strong><strong>输入您的 Klaviyo 公共 API 密钥：</strong><strong> 这是在您的 Klaviyo 帐户设置中找到的 6 个字符标识符（请参阅我们的[查找公共密钥指南](https://help.klaviyo.com/hc/en-us/articles/115005062267)）。 5. </strong><strong>选择您的 PMS：</strong></em>* 从下拉菜单中选择 Mews、Cloudbeds 或 Guesty。 6.![](https://klaviyo.zendesk.com/hc/article_attachments/46643062833051)</p>
<p>7. <strong><em>*设置触发器：</strong><strong> 将鼠标悬停在 </strong><strong>触发</strong><strong> 部分。 单击右上角出现的铅笔。选择</strong><strong>所有页面</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/46643094261531)</p>
<p>8. 为标签命名（例如 [Cloudbeds/Mews/Guesty] 标签）。单击<strong><em>*保存</strong></em>*。 ---</p>
<h2>步骤 5：发布您的更改</h2>
<p>在您提交这些更改之前，您的跟踪不会生效。 1. 点击GTM右上角的蓝色<strong><em>*提交</strong></em>*按钮。 ![10.png](https://klaviyo.zendesk.com/hc/article_attachments/48511182753179)</p>
<p>2. 为您的版本命名（例如“添加了 Klaviyo 酒店跟踪”）。 3. 单击<strong><em>*发布</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/46643062844187)</p>
<p>---</p>
<h2>接下来会发生什么？发布后，标签将自动开始向 Klaviyo 发送活动数据，以识别预订引擎上已识别的访客。 [了解 Klaviyo 可以在此处追踪的人](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACVVC4BXQ0ES5Y50TC)。您可以通过检查 Klaviyo 帐户中的“指标”选项卡中的以下事件来验证是否正在跟踪事件：</h2>
<ul>
<li>****活跃现场：**** 当有人在网站上活跃时触发。 - ****查看的列表：**** 当旅行者查看特定房间或房产时触发。 - ****开始结帐：**** 当旅客进入预订流程时触发。现在，您可以使用浏览放弃和放弃购物车流程模板，在选择 PMS 集成后可以在[此处](https://www.klaviyo.com/flows/create) 找到这些模板。但这只是开始 - 了解更多有关 Klaviyo 现场跟踪的信息 [此处](https://help.klaviyo.com/hc/en-us/articles/115005076767)！</li>
</ul>
