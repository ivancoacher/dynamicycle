---
id: "14781686592283"
title: "了解推送通知同意"
source_url: "https://help.klaviyo.com/hc/en-us/articles/14781686592283-Understanding-push-notification-consent"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:48:43Z"
language: "zh"
translation_strategy: "google_html_text_nodes_preserve_attributes"
---
<h2 id="h_01HBRFCB4V9K1EXBY1KMSSJT1D">你会学到</h2>
<p>了解 <a href="https://help.klaviyo.com/hc/en-us/articles/360023213971">推送通知</a> 同意和合规最佳实践。这些指南可以帮助您遵守同意收集做法并与客户保持积极的关系。 </p>
<div class="bs-callout bs-callout-default">
<p>此处提供的信息旨在提供教育意义，不应被视为法律建议。 Klaviyo 鼓励我们所有的客户向其律师寻求法律建议，了解他们具体应如何遵守适用的隐私和营销法律。</p>
</div>
<h2 id="h_01HBRFCB4VXYEKNEBGMV324B2X">什么算作推送通知同意</h2>
<p>为了向个人资料发送推送通知，您必须收集他们的信息 <a href="https://help.klaviyo.com/hc/en-us/articles/4404203889947">明确同意</a> 第一的。 </p>
<p>对于推送通知，授予同意会生成存储在 Klaviyo 配置文件中的推送令牌（也称为设备令牌）。一个推送令牌仅对 1 个设备有效，一个配置文件可以有多个推送令牌。如果某人同意在手机和平​​板电脑上推送通知，则该个人资料将有 2 个不同的推送令牌，每个设备一个。</p>
<p>此外，同意在一台设备上推送通知意味着您只能向该设备发送推送通知。这并不意味着您可以将推送通知发送到任何其他设备，即使您知道它适用于同一配置文件。 </p>
<p>推送通知同意也与电子邮件和短信同意分开收集。如果您同意使用其他渠道，这并不意味着您可以向该联系人发送推送通知，直到他们明确选择接收推送通知。 </p>
<h3 id="h_01HEJFNYQPYG04ZJVNCM7ZGKE2">在哪里查看个人资料是否同意推送通知</h3>
<p>要查看个人是否订阅接收推送通知，请转到他们的个人资料页面。然后，检查 <em>渠道 </em>部分。 </p>
<p>如果用户同意接收推送通知，“IOS 应用程序”或“Android 应用程序”部分将出现，旁边带有绿色复选标记。</p>
<p class="wysiwyg-text-align-center"><img alt="Subscribed to mobile push marketing on a profile" src="https://klaviyo.zendesk.com/hc/article_attachments/35811315409435"/></p>
<div class="accordion accordion--default">
<div class="accordion__item">
<div class="accordion__item-title"><strong>当一个配置文件上有多个推送令牌时，这意味着什么？</strong></div>
<div class="accordion__item-content">
<p>如果配置文件具有多个推送令牌，则用户可能已同意在多个设备上接收该应用程序的通知。例如，配置文件可能有 iPhone 和 iPad。</p>
<p>多个令牌也可能用于同一设备，但这只是暂时的。发生的情况是： </p>
<ol>
<li>用户删除应用，导致应用服务站Token失效。 </li>
<li>用户稍后重新下载应用程序，因此应用程序服务站向他们颁发新的令牌。 （此时，新旧令牌都会显示在用户的个人资料上。）</li>
<li>当您尝试向此配置文件发送推送通知时，应用程序服务站会提供有关无效令牌的错误。 </li>
<li>Klaviyo 从配置文件中删除无效令牌。</li>
</ol>
</div>
</div>
</div>
<h2 id="h_01HBRFCB4VJN1H7HRBYPJCAKCV">推送通知的最佳实践</h2>
<h3 id="h_01HBRFCB4VP9RY5EMHWFVSNQKE">许可入门 </h3>
<div class="bs-callout bs-callout-default">
<p>此许可入门（也称为选择加入提示）是应用内消息；它不是您在 Klaviyo 中设计的表单。</p>
</div>
<p>要收集推送同意，您必须提示客户使用本机 iOS 和 Android 提示启用推送通知。</p>
<p>解释为什么要首先向用户发送通知也是最佳实践。此推送“入门”应概述您发送的通知类型以及用户应选择加入的原因：</p>
<ul>
<li>
<strong>您的品牌发送哪些类型的通知</strong><br/>
包括有关您的品牌计划发送的不同推送通知的详细信息（例如，帐户更改、帐户更改、提醒和特别折扣）。 </li>
<li>
<strong>为什么用户应该选择加入</strong><br/>
包含有关客户为何应提供权限的信息（例如，接收重要更新或提前访问销售）。</li>
</ul>
<p class="wysiwyg-text-align-center"><img alt="Example pre-permission prompt to collect push notification consent" height="505" src="https://klaviyo.zendesk.com/hc/article_attachments/28704486353051" width="560"/></p>
<p>Apple 的本机 iOS 权限提示将遵循您自己的权限提示，用户可以为您的应用程序提供向其设备发送推送通知的权限。 </p>
<p class="wysiwyg-text-align-center"><img alt="Natitve IOS permission prompt for push notifications" src="https://klaviyo.zendesk.com/hc/article_attachments/28704478241947"/></p>
<h3 id="h_01HBRFCB4W6GTVHXMGFYW00RMB">选择加入语言示例</h3>
<p>最佳做法是让您的预许可提示包含有关您计划发送的特定推送通知的详细信息。这让应用程序用户确切地知道他们期望收到什么，并与潜在订阅者建立信任。 </p>
<p>这种语言的一个例子是：<br/>
<br/>
“<em>[公司/我们] 希望向您发送有关特别折扣、产品发布和发货更新的通知。你可以随时选择退出。”</em></p>
<p>但是，您还可以选择预许可提示来更广泛地描述您计划发送的通知类型：</p>
<p>"<em>[公司/我们] </em><em>位于XXX</em><em> 希望向您发送包含营销和服务相关消息的通知。您可以随时选择退出。</em>”</p>
<h3 id="h_01HBRFCB4WGHS5QG2Q4ZTRPC04">Notification content </h3>
<p>与短信等具有禁止主题的渠道不同，推送通知没有限制特定类型内容的规定。同样，根据 Apple 和 Android 的条款和条件，对于推送通知不存在明确的限制。确保推送通知的内容符合 Klaviyo 的规定 <a href="https://www.klaviyo.com/legal/acceptable-use-policy">可接受的使用政策</a>. </p>
<h3 id="h_01HBRFCB4WVCC4R03TKWS3P3X6">安静时间</h3>
<p>推送通知通常对安静时间没有任何要求，但在某些国家/地区，安静时间适用于所有营销传播，包括推送通知。因此，最好避免在晚上 8 点到晚上 8 点之间发送通知。以及收件人当地时区上午 8 点。 </p>
<h3 id="h_01HBRFCB4WE5845XN4GB8Y9YZY">通知首选项</h3>
<p>您的应用程序的最佳做法是进一步解释客户在订阅推送通知时可能会收到什么类型的内容。这允许客户参考他们在初始选择披露后预计收到的推送通知类型，并选择在以后的日期推送通知（如果他们在应用程序设置期间没有这样做）。</p>
<p>您可以在应用程序中构建一个通知首选项部分，用于显示客户已选择的通知类型并允许用户控制其首选项。</p>
<p>此外，通过以下方式向客户发送相关通知始终是最佳实践： <a href="https://help.klaviyo.com/hc/en-us/articles/115000250912">围绕他们的兴趣收集信息</a> 并创建有针对性的 <a href="https://help.klaviyo.com/hc/en-us/articles/115005237908">段</a>. </p>
<div class="bs-callout bs-callout-default">
<p>请注意，Klaviyo 不支持创建推送通知首选项中心。 Klaviyo 建议与应用程序的开发团队合作，将此部分构建到您的应用程序中。如果您对使用 Klaviyo 管理客户的推送通知偏好有其他疑问，请联系我们 <a href="https://help.klaviyo.com/hc/en-us/requests/new">支持团队</a> or on our <a href="https://community.klaviyo.com/">社区论坛</a>.</p>
</div>
<h2 id="h_01HBRFCB4WAPZVFWNY3XSB96BQ">其他资源 </h2>
<ul>
<li><a href="https://help.klaviyo.com/hc/en-us/articles/12932500186907">了解您的推送通知设置 </a></li>
<li><a href="https://help.klaviyo.com/hc/en-us/articles/360023213971">如何设置 iOS 推送通知</a></li>
<li><a href="https://help.klaviyo.com/hc/en-us/articles/360006653972">如何发送推送通知活动</a></li>
</ul>
<div class="bs-callout bs-callout-default">
<p>想要请求 Klaviyo 推送通知功能吗？填写这个 <a href="https://forms.gle/7iPm6JQ4eKB6H2C4A">谷歌表格</a> 告诉我们吧！ </p>
</div>