---
id: "29091293276187"
title: "了解流量警报"
source_url: "https://help.klaviyo.com/hc/en-us/articles/29091293276187-Understanding-flow-alerts"
section: "Troubleshooting flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:37Z"
language: "zh"
translation_strategy: "html_text_nodes_preserve_attributes"
---
<h2 id="h_01J7E4E914GNN84EH159XHBJM3">你会学到</h2><p>了解设置流程时可能会看到的不同警报和警告消息。当设置不完整或功能正在更改且设置不再有效时，会出现这些消息。 </p><p>对于阻止流程运行的问题，警报将显示为红色图标；对于需要解决但仍允许流程运行的问题，警报将显示为黄色图标。任何相关文本都将以相应的颜色突出显示。</p><p>流量警报可以出现在 2 个不同的位置，本文将介绍这些位置：</p><ul>
<li data-list-item-id="eaf9cb89835121fe1fc0211377aecda3f">这 <em>流量</em> 选项卡 - 您可以在其中查看帐户中所有流量的列表。</li>
<li data-list-item-id="ee79713ed6bd2a2c580200943506e9556">流程构建器 - 构建流程时使用的编辑器。</li>
</ul><h2 id="h_01J7E4E914V5YVBYHMQJDPDFX3">流选项卡警报</h2><p>当查看 <em>流量</em> 选项卡有两种类型的警报：</p><ol>
<li data-list-item-id="e67b904da4acf5e1331166808ceec51d7">红色的流名称表示如果没有正确的操作，该流将无法运行。当创建流但尚未设置触发器时会出现此情况。<br/><img height="92" src="https://klaviyo.zendesk.com/hc/article_attachments/29091559904283" width="205"/>
</li>
<li data-list-item-id="efa5c4942bbea77982813af38b6578b0f">中的黄色警告图标 <em>地位</em> 列表示流程仍将运行，但除非采取适当的措施，否则可能会跳过某些元素。将鼠标悬停在该图标上可获取有关该问题的更多信息。这可能包括已添加但尚未设置或具有无效设置的消息或其他操作。<br/><img height="163" src="https://klaviyo.zendesk.com/hc/article_attachments/29091569069595" width="480"/>
</li>
</ol><h2 id="h_01J7E4E914GNZZ4PGQRM313JVS">流程生成器警报</h2><p>流程构建器中尚未设置或设置无效的元素将在操作卡上显示相应的警告消息。警告意味着将跳过该元素，直到正确设置为止。</p><p>要查看所有警报：</p><ol>
<li data-list-item-id="ee509b3b271f9ac3a307f257dc2302b3a">
<p>单击 <strong>警报</strong> 标题栏右侧的图标按钮可打开流程操作中心。该徽章指示流程中活动警报的数量。</p>
<p><img height="506" src="https://klaviyo.zendesk.com/hc/article_attachments/46630158161819" width="1358"/><br/> </p>
</li>
<li data-list-item-id="e065fbead8dd4ecbdbe751852c51ac0bf">
<p>在警报列表中，您有多个选项：</p>
<p><img class="wysiwyg-image-resized" height="1504" src="https://klaviyo.zendesk.com/hc/article_attachments/46630158169371" style="aspect-ratio: 746/1504; width: 32.22%;" width="746"/><br/> </p>
<ul>
<li data-list-item-id="e49081e96ee4a817242f115c56fec5337">点击提示（如 <strong>设置</strong>) 查看受影响的流程元素的设置面板。</li>
<li data-list-item-id="e81ec5654cfeeb7a0f17577b2439947f0">点击 <strong>解雇 </strong>将警报移至 <em>被解雇 </em>选项卡。</li>
<li data-list-item-id="e08a6f944f4a66298027537822321b2b5">单击 <em>被解雇 </em>选项卡可查看之前取消的任何警报，您可以将其移回到 <em>积极的</em> 选项卡。</li>
</ul>
</li>
</ol><p>否则，您可以直接在流程画布上查看未配置的状态和其他警报，这些警报显示在每个操作的卡上。单击流程卡可查看需要进行的更改。</p><p><img class="wysiwyg-image-resized" height="738" src="https://klaviyo.zendesk.com/hc/article_attachments/46630158173083" style="aspect-ratio: 474/738; width: 49.4%;" width="474"/></p><div class="bs-callout bs-callout-default"><p>确保保存对流程元素所做的任何更改。如果您退出设置面板而不保存更改，警告将保留。</p></div><p>单击下面的小节可了解每个流程元素的警报。</p><div class="accordion accordion--default">
<div class="accordion__item">
<div class="accordion__item-title"><h3 id="h_01J7E4E915F5B22JGP84KDNR59">留言</h3></div>
<div class="accordion__item-content">
<p>消息需要满足以下条件才能发送：</p>
<ul>
<li data-list-item-id="e1354f2a6f07c0f259b7b2abb164ee023">主题行（电子邮件）</li>
<li data-list-item-id="e1b627317291cc251bed2bc0a7f5a80d2">使用企业域的有效发件人地址（电子邮件）</li>
<li data-list-item-id="e17acab4683e844bfe57ce41e3399ca6a">模板（电子邮件）或消息内容（短信和推送）</li>
</ul>
<p>对于下面的示例电子邮件，有两个必须解决的设置问题：</p>
<ol>
<li data-list-item-id="e59fd05ffaec4744aba4f9239c1a7fc03">流消息使用的电子邮件的收件箱提供商域 (@gmail.com) 不是有效的发件人地址。发件人地址必须更改为使用您网站域的电子邮件。这也适用于内部警报。</li>
<li data-list-item-id="ee1281a92029f74f2ff7bf32494602a42">流消息尚未选择模板。消息需要模板才能发送。</li>
</ol>
<p><img height="536" src="https://klaviyo.zendesk.com/hc/article_attachments/29091569079195" width="380"/></p>
</div>
</div>
<div class="accordion__item">
<div class="accordion__item-title"><h3 id="h_01J7E4E915XHJ0T455MZCN2ZE4">内部警报</h3></div>
<div class="accordion__item-content">
<p>内部警报需要以下信息才能发送：</p>
<ul>
<li data-list-item-id="eceec0c0a13accedb318258847b586b5f">至少 1 位收件人 <em>发送至 </em>场地</li>
<li data-list-item-id="e4e39f0efe212839316c3c003287c3de4">有效的发件人地址</li>
<li data-list-item-id="e0be53d77d3d98aa9c61d0912ead2c10b">主题</li>
<li data-list-item-id="edb1bd096316e29fd86a9e3792bc6456c">留言内容</li>
</ul>
</div>
</div>
<div class="accordion__item">
<div class="accordion__item-title"><h3 id="h_01J7E4E915Z6MF63KTRJD81H8T">时间延误</h3></div>
<div class="accordion__item-content"><p>时间延迟需要输入一个数字 <em>设置延时时间</em> 场地。</p></div>
</div>
<div class="accordion__item">
<div class="accordion__item-title"><h3 id="h_01J7E4E915GYD8Q7FGEZTKSXJ5">分裂</h3></div>
<div class="accordion__item-content">
<p>拆分需要至少设置 1 个条件才能发挥作用。 </p>
<p>如果条件不再有效，拆分可能会发出警告。例如，如果特定属性在拆分条件下不再可用，则拆分的设置面板中将显示一条警告消息。</p>
</div>
</div>
<div class="accordion__item">
<div class="accordion__item-title"><h3 id="h_01J7E4E9152XBE1159M20MBXEG">过滤器</h3></div>
<div class="accordion__item-content"><p>应用于触发器或单个流消息的过滤器是可选的。如果条件不再有效，他们可能会收到警告。例如，如果特定属性在过滤条件中不再可用，则过滤器的设置面板中将显示一条警告消息。</p></div>
</div>
</div><h2 id="h_01J7E4E9155XMBRV82SPM6439D">其他资源</h2><p>您的流程仍然遇到问题吗？ </p><ul>
<li data-list-item-id="e34cc9dc60c01bc4ab952704f26c87e8b">了解 <a href="https://help.klaviyo.com/hc/en-us/articles/115002779471">对流程进行故障排除</a>.</li>
<li data-list-item-id="e7fe9869a73d46fe74d6045475c4b9658">了解不同的 <a href="https://help.klaviyo.com/hc/en-us/articles/1260805003210">跳过流消息的原因</a>.</li>
</ul>