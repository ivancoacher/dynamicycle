---
id: "33660504643867"
title: "如何在客户中心显示产品推荐"
source_url: "https://help.klaviyo.com/hc/en-us/articles/33660504643867-How-to-display-product-recommendations-in-Customer-Hub"
section: "Build and use Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:56:48Z"
language: "zh"
translation_strategy: "google_html_text_nodes_preserve_attributes"
---
<h2 id="h_01JMFVFEH0D0QFZ16R2KZ1GR33">你会学到</h2>
<p>了解如何在客户中心抽屉中显示个性化产品推荐，为客户定制购物体验并提高转化率。通过展示对客户有吸引力的产品，您可以提高转化率并提供交叉销售机会以提高平均订单价值。</p>
<div class="bs-callout bs-callout-requirements ignore-for-search">
<p>Shopify 客户中心目前支持标准店面和 Shopify Headless。对于 WooCommerce，请导航至 https://help.klaviyo.com/hc/en-us/articles/47792369863451</p>
<p>有关客户中心功能的反馈，请发送电子邮件至 customerhub@klaviyo.com。</p>
</div>
<div class="bs-callout bs-callout-requirements ignore-for-search">
<p> </p>
</div>
<h2 id="h_01JMFVFEH0F67PCJ8CR5RYN3H8">开始之前</h2>
<p>本指南介绍了如何激活产品推荐，以便它们显示在您网站上的客户中心抽屉中。在继续之前，请确保 <a href="https://klaviyo.com/try-service" rel="noopener noreferrer" target="_blank">客户中心功能已启用</a>.</p>
<p><a href="https://help.klaviyo.com/hc/en-us/articles/33660324811675" rel="noopener noreferrer" target="_blank">了解有关客户中心的更多信息</a>.</p>
<h2 id="h_01JMFVFEH01ENKFE6ZRGPVGQJX">关于产品推荐</h2>
<p>启用后，产品推荐会显示在 <em>为你</em> 您网站上客户中心抽屉的选项卡。这些建议是根据购物者在您网站上的行为以及购物者在 Klaviyo 中的历史记录量身定制的，从而增加了他们的购买可能性。</p>
<p><img alt="A Customer Hub drawer open on an example brand's website showing the Recommended products section highlighted." src="https://klaviyo.zendesk.com/hc/article_attachments/34194267469339"/></p>
<p>对于任何登录的购物者，Klaviyo 都会分析他们的浏览历史记录（即查看过的产品）和过去从 Shopify 网站购买的商品，以便显示相关的产品推荐。</p>
<p>最多 5 个推荐产品显示在图像轮播中 <em>推荐产品</em> 其他内容块下方的部分。在产品推荐块中，购物者可以：</p>
<ul>
<li>查看产品详细信息，包括商品名称、价格和尺寸（如果适用）。</li>
<li>将商品添加到他们的购物车。</li>
<li>将项目添加到他们的收藏夹，如果 <a href="https://klaviyo.zendesk.com/hc/en-us/articles/33660543083419"><em>收藏夹</em> 已启用</a>.</li>
</ul>
<p>购物者可以点击旁边的箭头 <em>推荐产品</em> 部分也可以在列表视图中查看这些项目。 </p>
<p class="wysiwyg-text-align-center"><img alt="The list view of the recommended products section in the Customer Hub interface." src="https://klaviyo.zendesk.com/hc/article_attachments/34194267478171"/></p>
<p>这些产品会根据购物者的活动随着时间的推移而更新。请注意，产品推荐模型是 <a href="https://help.klaviyo.com/hc/en-us/articles/115005082787#h_01HA7KGGHEDAPZQZSZJJFMCX5H" rel="noopener noreferrer" target="_blank">一般7天训练一次</a>，取决于用途。推荐模型可能需要几天的时间来考虑全新的事件。 </p>
<p>如果 Klaviyo 没有数据来确定个性化推荐，它会向客户显示过去 90 天内最畅销的产品。 </p>
<h2 id="h_01JMFVFEH0DQHEEWGJYTTE74RK">启用产品推荐</h2>
<ol>
<li>在 Klaviyo 的左侧导航中，选择 <strong>服务 - </strong><strong>客户中心</strong>.</li>
<li>选择 <strong>扩展</strong>.</li>
<li>在下面 <em>产品推荐</em>，选中该框以 <strong>启用产品推荐</strong>.<br/><img src="https://klaviyo.zendesk.com/hc/article_attachments/40774228685979"/>
</li>
<li>点击 <strong>节省</strong>.</li>
</ol>
<p>一旦上线，当有人点击产品推荐时，Klaviyo 会记录一个 <em>客户中心点击推荐产品</em> 事件。您可以根据此指标构建细分，以发送有针对性的、行为驱动的营销活动。</p>
<h2 id="h_01JMFVFEH1362M3CBDA0AXCJ3T">从推荐中排除某些产品</h2>
<p>您可能希望阻止某些项目出现在 <em>产品推荐 </em>在客户中心查看，例如免费礼品、运输保险或缺货商品。</p>
<p>Klaviyo 提供了一个标签， <em>klaviyo_hub_recommendation_exclude</em>，您可以将其应用于 Shopify 中您希望排除的产品。请记住，客户已购买的产品会自动从他们的产品推荐中排除。</p>
<p>要排除特定产品：</p>
<ol>
<li>导航到 Shopify 后台中的产品页面。</li>
<li>在 <em>标签</em> 右侧字段，添加标签 <em>klaviyo_hub_recommendation_exclude</em>.<br/><img alt="The Tags field in Shopify showing the klaviyo_hub_recommendation_exclude tag added." src="https://klaviyo.zendesk.com/hc/article_attachments/34972804300699"/>
</li>
<li>点击 <strong>节省</strong>.</li>
</ol>
<p>保存此更改后，该产品将不再出现在客户中心界面中任何客户的产品推荐中。</p>
<div class="bs-callout bs-callout-default">
<p>从产品推荐中删除产品最多可能需要 30 分钟。</p>
</div>
<h2 id="h_01JMFVFEH1ATGBJ36698FP0FSG">产品推荐的收入归因 </h2>
<p>如果购物者从 <em>产品推荐</em> 部分添加到购物车，然后下订单，Klaviyo 将该商品的收入归因于客户中心。</p>
<p>该数据可以在 <em>产生的收入</em> 的栏目 <a href="https://www.klaviyo.com/customer-hub/dashboard" rel="noopener noreferrer" target="_blank">客户中心仪表板</a>. </p>
<h2 id="h_01JMFVFEH149N1MD9JZDHBKPYK">其他资源</h2>
<ul>
<li><a href="https://help.klaviyo.com/hc/en-us/articles/33660382797595" rel="noopener noreferrer" target="_blank">了解客户中心概览仪表板</a></li>
<li><a href="https://help.klaviyo.com/hc/en-us/articles/33660543083419">如何在客户中心显示收藏的项目</a></li>
<li><a href="https://help.klaviyo.com/hc/en-us/articles/33660517680795">如何将内容块添加到客户中心</a></li>
</ul>