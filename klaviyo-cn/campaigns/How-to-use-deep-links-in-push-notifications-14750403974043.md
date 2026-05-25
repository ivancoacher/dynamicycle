---
id: "14750403974043"
title: "如何在推送通知中使用深层链接"
source_url: "https://help.klaviyo.com/hc/en-us/articles/14750403974043-How-to-use-deep-links-in-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:48:40Z"
language: "zh"
translation_strategy: "google_html_text_nodes_preserve_attributes"
---
<h2 id="h_01HBRFEX1CAN3TTVB543M8WJ36">你会学到</h2>
<p>了解如何在 Klaviyo 推送通知中使用深度链接，以便您可以将客户引导至特定的应用内屏幕。深层链接使您的个人资料只需轻轻一按即可轻松访问他们想要的内容。</p>
<p>你可以 <a href="https://help.klaviyo.com/hc/en-us/articles/41701832186523">来自电子邮件和短信的深层链接</a> 通过将您的点击跟踪域链接到您的应用程序。 </p>
<div class="accordion accordion--default">
<div class="accordion__item">
<div class="accordion__item-title"><strong>什么是深层链接？</strong></div>
<div class="accordion__item-content">
<p>A deep link is a custom URI that opens your mobile app to a certain page. It’s a common feature for push notifications, allowing marketers to link to, for example, a specific product page rather than the app’s home page. This way, recipients don’t need to search your app or navigate through menus to find the page they are interested in. </p>
</div>
</div>
<div class="accordion__item">
<div class="accordion__item-title"><strong>什么是 URI？</strong></div>
<div class="accordion__item-content">
<p>URI 代表统一资源标识符。 URI 与 URL 类似：URL 是网站的地址，而 URI 是应用程序（或其他资源）的地址（或“标识符”）。 </p>
</div>
</div>
</div>
<h2 id="h_01HBRFEX1CD047SMGSRCDXYM9D">开始之前</h2>
<p>要在推送通知中使用深层链接，您必须将 Klaviyo 连接到您的 <a href="https://help.klaviyo.com/hc/en-us/articles/360023213971">iOS系统</a> 或者 <a href="https://help.klaviyo.com/hc/en-us/articles/14750928993307">安卓</a> 移动应用程序。 </p>
<p>您还必须为您的应用程序设置深层链接。如果您不确定您的应用程序是否具有深层链接，请与您的开发人员联系。</p>
<p>设置深层链接后，您可以在推送通知之外的其他渠道（包括电子邮件和短信）中使用这些链接。 </p>
<p>请注意，深层链接可能为未经授权的用户提供访问您的应用程序的潜在途径。您应该始终验证您的 URI 及其参数，确保测试并删除任​​何格式不正确的内容。此外，对任何操作添加限制，以便其他应用程序无法影响用户的数据（例如删除内容）。 </p>
<div class="bs-callout bs-callout-default">
<p>想要请求 Klaviyo 推送通知功能吗？填写这个 <a href="https://forms.gle/7iPm6JQ4eKB6H2C4A">谷歌表格</a> 告诉我们吧！ </p>
</div>
<h2 id="h_01HBRFEX1CFTTP5DYR94X41YXZ">关于深度链接</h2>
<p>深层链接是指向应用程序特定部分的自定义 URI。 </p>
<p>深层链接分为 3 个部分： </p>
<ol>
<li>识别您的应用程序 </li>
<li>告诉应用程序要采取什么操作</li>
<li>包括有关该操作的任何附加数据</li>
</ol>
<p>这些部分构成了 URI 的外观。 </p>
<p>请注意，深层链接可能为未经授权的用户提供访问您的应用程序的潜在途径。您应该始终验证您的 URI 及其参数，确保测试并删除任​​何格式不正确的内容。此外，对任何操作添加限制，以便其他应用程序无法影响用户的数据（例如删除内容）。 </p>
<h3 id="h_01HBRFEX1D11QMHQDG4JWRMEPM">深层链接示例</h3>
<p>URI 方案如下所示：scheme:[//authority]path[?query][#fragment]</p>
<p>让我们用一个例子来分解它： </p>
<p>myapp://产品/123abc </p>
<ul>
<li>我的应用程序://<br/>
这是指向您的移动应用程序的方案。虽然此方案可以是任何内容（字母、数字、符号），但我们建议使用您的域名。例如，如果这是 Klaviyo 的应用程序，它看起来像：<em> klaviyo:// </em>
</li>
<li>产品/<br/>
这是 URL 中的路径，告诉应用程序在哪个页面打开产品页面（即操作）。</li>
<li>123abc<br/>
这为应用程序提供了附加信息；在本例中，打开产品 123abc 的页面。 </li>
</ul>
<p><strong>我可以在深层链接中包含 UTM 参数吗？</strong></p>
<p>是的，您可以在营销活动和流量推送通知中使用 UTM 参数。这样，您就可以在 Google Analytics 或其他软件中监控推送通知的性能。</p>
<p>目前，您需要手动添加 UTM 参数。 </p>
<p><strong>我可以在深层链接中包含动态变量和个性化标签吗？ </strong></p>
<p>是的，您可以同时包含动态变量和 <a href="https://help.klaviyo.com/hc/en-us/articles/4408802648731">个性化标签</a> 在深层链接中。因此，您可以个性化链接，以便将某人定向到他们的个人资料、购物车或收藏夹。 </p>
<h2 id="h_01HBRFEX1D1JZR9TFZA440G08K">将深层链接添加到推送通知</h2>
<p>您可以在为推送通知创建消息文本时添加深层链接。 </p>
<p>请注意，您会看到不同的选项，具体取决于您是否为 iOS、Android 或两者设置推送。如果您在 Klaviyo 中仅设置了 iOS，则无法选择添加 Android 深层链接（反之亦然）。 </p>
<ol>
<li>在 Klaviyo 中，导航到您想要深层链接的营销活动或流消息。</li>
<li>进入消息编辑器。 </li>
<li>输入您的推送通知内容。</li>
<li>在左侧菜单上，单击 <strong>行为</strong> 选项卡。</li>
<li>单击下面的下拉菜单 <em>开放行动</em>.</li>
<li>选择 <strong>深层链接</strong>.<br/>
请注意，对于下面的示例，该帐户仅启用了 iOS 推送通知。<br/>
<img alt="Option to send a deep link in a push notification." height="483" src="https://klaviyo.zendesk.com/hc/article_attachments/34417696684955" width="522"/>
</li>
<li>添加您的深层链接。<br/>
注意：如果 Android 和 iOS 的链接相同，则必须将其添加到两个字段。 </li>
<li>点击 <strong>下一个</strong> 以保存包含深层链接的消息并继续发送消息。 </li>
</ol>
<h2 id="h_01HBRFEX1D8CKV5DAX30K5XQP1">结果</h2>
<p>在推送通知中包含深层链接后，任何点击该消息的人都会自动定向到您指定的页面。 </p>
<p>这使您可以轻松推广新产品、鼓励收件人填写个人资料等等。 </p>
<p>如果您的深层链接遇到问题（例如，如果无法打开正确的页面），我们鼓励您与您的开发人员联系，因为 Klaviyo 无法帮助您解决这些问题。 </p>