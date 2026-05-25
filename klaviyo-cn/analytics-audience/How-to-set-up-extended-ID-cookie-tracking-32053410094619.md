---
id: "32053410094619"
title: "如何设置扩展 ID cookie 跟踪"
source_url: "https://help.klaviyo.com/hc/en-us/articles/32053410094619-How-to-set-up-extended-ID-cookie-tracking"
section: "About cookies in Klaviyo"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:38Z"
language: "zh"
translation_strategy: "html_text_nodes_preserve_attributes"
---
<h2 id="h_01JFG23R9T1NBR5WHK2YSBTQ21">你会学到</h2>
<p>了解如何设置扩展 ID，以便更长时间地合规地捕获和跟踪订阅者与您的品牌的互动。扩展 ID 是一项第一方身份图功能，允许您跟踪并保留 cookie 长达 1 年。因此，您可以更长时间地识别这些交互和行为，以定位、细分和自动化营销信息。</p>
<h2 id="h_01JFG23R9TXVZHWKCET29WK9VD">开始之前</h2>
<p>请注意以下与扩展 ID 相关的事项：</p>
<ul>
<li>所有 Klaviyo 付费计划均提供扩展 ID。</li>
<li>扩展 ID 不提供与转换 API (CAPI) 的集成以及对概率标识符（即 IP 地址、设备数据、点击 ID、位置或用户代理等标识符）的支持。</li>
<li>不支持跨公司、设备和浏览器的重新识别跟踪</li>
<li>扩展ID不使用指纹技术。</li>
</ul>
<div class="bs-callout bs-callout-default">
<p>如果您选择开启扩展 ID，强烈建议您向客户重新发出 Cookie 通知，并告知他们 Klaviyo 将使用第一方 Cookie 来重新发出 Klaviyo cookie。这将允许 Klaviyo 和您的企业在用户的浏览器 cookie 过期后重新识别用户。此外，建议您更新隐私声明，以确保您的客户了解此重新识别过程。</p>
</div>
<h2 id="h_01JFG23R9T94KPB8FSBM133RWH">扩展 ID 如何工作？</h2>
<p>扩展 ID 通过利用通用确定性标识符（即精确的唯一标识符）来工作。对于其他平台或解决方案，您将需要设置自定义标识符。</p>
<div class="bs-callout bs-callout-default">
<p>扩展 ID 无法根据其他网站的购物者信息自动创建新的配置文件。购物者需要已经拥有 Klaviyo 配置文件以获取扩展 ID，以便重新识别他们并更新他们的 Klaviyo 身份 cookie。</p>
</div>
<h2 id="h_01JFG23R9T1NA3PC8GWNPYGMZ3">开启扩展ID</h2>
<ol>
<li>单击帐户左下角的帐户菜单。</li>
<li>选择 <strong>设置</strong> 从菜单中。<br/>
<img alt="Settings page in account menu" src="https://klaviyo.zendesk.com/hc/article_attachments/32053902569883"/>
</li>
<li>导航至 <strong>数据</strong> 选项卡。</li>
<li>在 <em>扩展ID</em> 部分，单击 <strong>使能够</strong>。一旦你点击 <strong>使能够</strong>，您的帐户将开始扩展 cookie 的跟踪。<br/>
<img alt="" height="668" src="https://klaviyo.zendesk.com/hc/article_attachments/45139567095707" width="1156"/>
<div class="bs-callout bs-callout-default">
<p>启用后，Klaviyo 将开始使用您品牌网站上的其他第一方标识符重新识别用户。  默认情况下，我们尝试使用以下通用标识符</p>
<table>
<tbody>
<tr>
<td><strong>类型</strong></td>
<td><strong>平台</strong></td>
<td><strong>标识符</strong></td>
</tr>
<tr>
<td>电商平台（如适用）</td>
<td>购物</td>
<td>_shopify_y</td>
</tr>
<tr>
<td>电商平台（如适用）</td>
<td>销售人员</td>
<td>__cq_uuid</td>
</tr>
<tr>
<td>分析工具</td>
<td>谷歌分析</td>
<td>_ga</td>
</tr>
<tr>
<td>广告网络</td>
<td>微软清晰度</td>
<td>_clck</td>
</tr>
<tr>
<td>广告网络</td>
<td>微软必应</td>
<td>_uetvid</td>
</tr>
<tr>
<td>广告网络</td>
<td>快照</td>
<td>_scid</td>
</tr>
<tr>
<td>广告网络</td>
<td>抖音</td>
<td>_ttp</td>
</tr>
<tr>
<td>广告网络</td>
<td>红迪网</td>
<td>_rdt_uuid</td>
</tr>
</tbody>
</table>
</div>
</li>
<li>可选：在 <em>添加自定义标识符</em>，在中填写您的自定义标识符的名称 <em>输入自定义标识符</em> 场地。在中添加您的 cookie 值 <em>钥匙</em> 场地。请记住，此信息通常存储为键值对。例如，在 cookie user_id=12345 中，“user_id”是您的密钥，“12345”是值。然后，打开 <em>地点/来源</em> 下拉菜单查找并选择您的工具。</li>
<li>可选：单击 <strong>+ 添加</strong> 按钮可根据需要添加更多自定义标识符。<br/>
<img alt="" height="525" src="https://klaviyo.zendesk.com/hc/article_attachments/45139588163867" width="743"/>
</li>
<li>可选：单击右上角 <strong>节省</strong>。保存自定义标识符后，您将进入初始设置屏幕，显示其状态为 <em>正在验证</em>。请注意，验证标识符最多可能需要 2 周的时间。</li>
</ol>
<p>验证您的自定义标识符后，设置页面上的状态将更改为 <em>积极的</em>。现在这意味着该解决方案的任何后续跟踪都已扩展。但是，如果您的状态是 <em>失败的</em>，扩展 ID 系统发现您提供的标识符不够唯一，不足以用于扩展 ID。为了避免 Klaviyo 中配置文件之间的数据重叠，该标识符已被阻止，并且不会用于扩展 ID 识别。</p>
<h2 id="h_01JFG23R9T2SC2N1AN61TCWY3Q">禁用扩展 ID 或特定标识符</h2>
<p>如果您连接了某个解决方案或工具，但您不再希望对其进行扩展跟踪，则可以禁用它们。此外，如果您希望在所有工具中完全关闭扩展 ID，您也可以这样做。</p>
<div class="bs-callout bs-callout-default">
<p>通过禁用一个或所有扩展 ID 标识符，您将立即恢复到 Klaviyo <a href="https://help.klaviyo.com/hc/en-us/articles/360034666712">默认跟踪设置</a>.</p>
</div>
<ol>
<li>单击帐户左下角的帐户菜单。</li>
<li>选择 <strong>设置</strong> 从菜单中。<br/>
<img alt="Setings page in account menu" src="https://klaviyo.zendesk.com/hc/article_attachments/32053902569883"/>
</li>
<li>导航至 <strong>数据</strong> 选项卡。</li>
<li>可选：在 <em>扩展ID</em> 部分，单击左上角的三点菜单。选择 <strong>禁用扩展 ID</strong> 然后单击 <strong>禁用</strong> 确认。<br/>
</li>
</ol>
<h2 id="h_01JS4JW6RGK7NP82A9M60ZXWGP">衡量扩展 ID 的影响 </h2>
<p>要查看扩展 ID 对您的品牌识别访问者的能力的影响，您可以利用 <em>现场活跃</em> 事件。</p>
<ol>
<li>导航至 <strong>分析</strong> &gt; <strong>Metrics</strong> &gt; <strong>现场活跃</strong>.</li>
<li>添加过滤器 <strong>通过 &gt; 扩展_id</strong>. </li>
</ol>
<p>这表明与 Klaviyo 的标准客户端 cookie 相比，由于扩展 ID 捕获的额外活动现场事件的数量。扩展 ID 事件的值为 <em>1.0</em> （即 true），而使用 Klaviyo 的标准 cookie 跟踪捕获的事件的值为 <em>0.0</em> （即假）。 </p>
<p><img alt="" src="https://klaviyo.zendesk.com/hc/article_attachments/36116155646619"/></p>