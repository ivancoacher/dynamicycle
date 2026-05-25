---
id: "115005085427"
title: "了解独立打开次数与总打开次数和点击次数"
slug: "articles-understanding-unique-vs-total-opens-and-clicks"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005085427-Understanding-unique-vs-total-opens-and-clicks"
section: "Analyze email results"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-11T10:54:40Z"
language: "zh"
---
<style>
.betterdocs-sidebar,
.betterdocs-docs-sidebar,
.betterdocs-single-layout-2 .betterdocs-sidebar,
.betterdocs-single-layout-3 .betterdocs-sidebar,
.betterdocs-single-wraper .betterdocs-sidebar,
.betterdocs-toc,
.betterdocs-table-of-contents,
.betterdocs-toc-wrapper,
.betterdocs-toc-container,
.betterdocs-content-area > .betterdocs-toc,
.betterdocs-doc-content > .betterdocs-toc,
.betterdocs-article-reactions,
.betterdocs-social-share {
  display: none !important;
}
.betterdocs-content-area,
.betterdocs-single-content,
.betterdocs-doc-content {
  max-width: none !important;
}
.dc-article-shell {
  display: grid;
  grid-template-columns: minmax(210px, 260px) minmax(0, 820px);
  gap: 34px;
  align-items: start;
  color: #1f2937;
}
.dc-article-toc {
  position: sticky;
  top: 110px;
  border-right: 1px solid #e5e7eb;
  padding: 4px 20px 16px 0;
}
.dc-article-toc h2 {
  font-size: 20px;
  line-height: 1.25;
  margin: 0 0 12px;
  color: #334155;
}
.dc-article-toc ol {
  list-style: none;
  margin: 0;
  padding: 0;
  counter-reset: toc;
}
.dc-article-toc li {
  counter-increment: toc;
  margin: 0;
}
.dc-article-toc li a {
  display: block;
  padding: 7px 0;
  color: #385579;
  text-decoration: none;
  line-height: 1.45;
}
.dc-article-toc li a::before {
  content: counter(toc) ". ";
}
.dc-article-toc li a:hover {
  color: #111827;
  text-decoration: underline;
  text-underline-offset: 3px;
}
.dc-help-article {
  max-width: 820px;
  color: #1f2937;
  font-size: 16px;
  line-height: 1.75;
}
.dc-learn-list {
  margin: 18px 0 0 22px;
  padding: 0;
}
.dc-learn-list li {
  margin: 0 0 18px;
  padding-left: 2px;
}
.dc-learn-list strong {
  display: block;
  color: #111827;
  font-size: 16px;
  line-height: 1.45;
  margin-bottom: 3px;
}
.dc-learn-list span {
  display: block;
  color: #1f2937;
  line-height: 1.7;
}
.dc-resource-list {
  margin: 0;
  padding: 0;
  list-style: none;
}
.dc-resource-list li {
  margin: 0 0 16px;
}
.dc-resource-list a {
  color: #111827;
  text-decoration: underline;
  text-underline-offset: 3px;
}
.dc-resource-list p {
  margin: 4px 0 0;
  color: #1f2937;
  line-height: 1.7;
}
@media (max-width: 900px) {
  .dc-article-shell {
    display: block;
  }
  .dc-article-toc {
    position: static;
    border-right: 0;
    border-bottom: 1px solid #e5e7eb;
    margin-bottom: 24px;
    padding-bottom: 18px;
  }
}
</style>

<div class="dc-article-shell">
<nav class="dc-article-toc" aria-label="文章目录">
  <h2>Table Of Contents</h2>
  <ol>
    <li><a href="#what-you-will-learn">你将会学到</a></li>
    <li><a href="#campaign-opens-clicks">查看 Campaign 的打开量和点击量</a></li>
    <li><a href="#unique-opens-clicks">独立打开次数和独立点击次数</a></li>
    <li><a href="#total-opens-clicks">总打开次数和总点击次数</a></li>
    <li><a href="#additional-resources">其他资源</a></li>
  </ol>
</nav>

<div class="dc-help-article">

<section id="what-you-will-learn" style="margin-bottom: 32px;">
  <h2 style="font-size: 24px; line-height: 1.35; margin: 0 0 14px; color: #111827;">你将会学到</h2>
  <p style="margin: 0 0 12px;">了解在查看 Campaign 结果时，独立打开/点击与总打开/点击之间的区别。简单来说：</p>
  <ul class="dc-learn-list">
    <li>
      <strong>独立打开次数</strong>
      <span>打开邮件的唯一收件人数。换句话说，如果一位收件人打开你的邮件两次，则计为一次独立打开。</span>
    </li>
    <li>
      <strong>独立点击次数</strong>
      <span>点击邮件的唯一收件人数。换句话说，如果一位收件人点击你的邮件两次，则计为一次独立点击。</span>
    </li>
    <li>
      <strong>总打开次数*</strong>
      <span>邮件被打开的总次数。换句话说，如果一位收件人打开你的邮件两次，则计为两次总打开。</span>
    </li>
    <li>
      <strong>总点击次数*</strong>
      <span>邮件被点击的总次数。换句话说，如果一位收件人点击你的邮件两次，则计为两次总点击。</span>
    </li>
  </ul>
</section>

<aside style="border-left: 4px solid #334155; background: #f8fafc; border-radius: 8px; padding: 16px 18px; margin: 0 0 34px;">
  <h3 style="font-size: 17px; margin: 0 0 8px; color: #111827;">Apple Mail 与打开跟踪</h3>
  <p style="margin: 0 0 12px;">随着 iOS 15、macOS Monterey、iPadOS 15 和 watchOS 8 的发布，Apple Mail 隐私保护（MPP）会预取跟踪像素，从而改变 Klaviyo 接收邮件打开数据的方式。因此，打开率可能会被抬高。</p>
  <p style="margin: 0;">如果想确认打开数据是否受到影响，建议创建包含 MPP 属性的 <a href="https://help.klaviyo.com/hc/en-us/articles/4416803987739" style="color: #111827; text-decoration: underline; text-underline-offset: 3px;">自定义报告</a>，也可以在单个 <a href="https://help.klaviyo.com/hc/en-us/articles/4416791883163" style="color: #111827; text-decoration: underline; text-underline-offset: 3px;">订阅者细分</a> 中识别这些打开。关于 MPP 打开的完整说明，请参考 <a href="https://www.klaviyo.com/blog/apple-ios15-klaviyo" style="color: #111827; text-decoration: underline; text-underline-offset: 3px;">iOS 15：如何准备 Apple 的更改</a>。</p>
</aside>

<section id="campaign-opens-clicks" style="margin-bottom: 32px;">
  <h2 style="font-size: 24px; line-height: 1.35; margin: 0 0 14px; color: #111827;">查看 Campaign 的打开量和点击量</h2>
  <p style="margin: 0 0 14px;"><strong>Campaigns</strong> 标签会显示每个已发送 Campaign 的打开、点击和转化数据。这里展示的数字基于执行打开、点击、购买等行为的唯一用户。</p>
  <p style="margin: 0;">点击某个已发送的 Campaign 后，你会先看到该 Campaign 的概览报告，其中包含高层级的表现指标。</p>
</section>

<section id="unique-opens-clicks" style="margin-bottom: 32px;">
  <h2 style="font-size: 24px; line-height: 1.35; margin: 0 0 14px; color: #111827;">独立打开次数和独立点击次数</h2>
  <p style="margin: 0 0 18px;"><strong>Engagement over time</strong> 模块中的核心打开和点击数据代表独立打开与独立点击；这些数字会与 <strong>Campaigns</strong> 标签首页中看到的数字一致。</p>

  <figure style="margin: 22px 0 18px; border: 1px solid #e5e7eb; border-radius: 12px; overflow: hidden; background: #ffffff;">
    <img src="https://cdn.sanity.io/images/6ct6b26e/help-center-prod/1ca037740739012ea8cb45d4066d82e68b568a7b-1600x752.jpg?w=687" alt="Klaviyo 中随时间变化的参与度图表，展示 Campaign 打开和点击表现" style="display: block; width: 100%; height: auto; margin: 0;">
    <figcaption style="font-size: 14px; color: #6b7280; padding: 12px 16px; border-top: 1px solid #e5e7eb; background: #f9fafb;">Engagement over time 模块用于查看 Campaign 的独立打开和独立点击趋势。</figcaption>
  </figure>

  <p style="margin: 0;">请注意，在少数 Klaviyo 无法控制的情况下，某些独立打开事件可能无法被跟踪。例如，一些第三方邮件客户端和浏览器扩展会阻止跟踪像素，包括用于追踪邮件打开的像素。这类情况并不常见，但可能会影响部分客户的打开率。</p>
</section>

<section id="total-opens-clicks" style="margin-bottom: 32px;">
  <h2 style="font-size: 24px; line-height: 1.35; margin: 0 0 14px; color: #111827;">总打开次数和总点击次数</h2>
  <p style="margin: 0 0 14px;">在报告底部，你还会看到 <strong>Total Opens</strong> 和 <strong>Total Clicks</strong> 数据。</p>
  <p style="margin: 0 0 14px;">这些总数代表记录到的所有打开和点击。例如，一个人收到你的 Campaign 并打开了两次，系统会计算为 2 次总打开。因此，总数通常会高于独立计数。</p>
  <p style="margin: 0;">如果总打开数或总点击数明显高于独立打开数或独立点击数，可能意味着收件人经常将你的邮件转发给其他人。</p>
</section>

<section id="additional-resources" style="border-top: 1px solid #e5e7eb; padding-top: 22px; margin-top: 34px;">
  <h2 style="font-size: 22px; line-height: 1.35; margin: 0 0 14px; color: #111827;">其他资源</h2>
  <ul class="dc-resource-list">
    <li>
      <a href="https://help.klaviyo.com/hc/en-us/articles/115000201131">电子邮件送达率监控和绩效指标入门</a>
      <p>了解不同行业中较好的电子邮件送达指标，以及可以用来改善邮件表现的策略。在本指南中，你可以了解按垂直行业或业务类型应该争取达到的电子邮件 Campaign 和 Flow 消息打开率、点击率，并学习如何缓解潜在的送达问题以及持续监控这些指标。</p>
    </li>
    <li>
      <a href="https://help.klaviyo.com/hc/en-us/articles/115005258568">了解可用的 Campaign 分析</a>
      <p>学习如何使用 Klaviyo 的 Campaign 报告，了解消息表现以及用户打开或点击之后发生了什么。你可以通过 Campaign 分析进一步查看网站行为、结账开始和直接归因于每条消息的收入。</p>
    </li>
  </ul>
</section>

<!-- klaviyo_id: 115005085427 -->
</div>
</div>
