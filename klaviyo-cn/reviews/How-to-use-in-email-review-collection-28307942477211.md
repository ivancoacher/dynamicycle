---
id: "28307942477211"
title: "如何使用电子邮件内评论收集"
source_url: "https://help.klaviyo.com/hc/en-us/articles/28307942477211-How-to-use-in-email-review-collection"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:46Z"
language: "zh"
translation_strategy: "html_text_nodes_preserve_attributes"
---
<p>了解如何允许您的客户直接通过电子邮件提交评论。配置此选项后，审阅者无需打开新窗口即​​可发表审阅。  </p>
<div class="bs-callout bs-callout-default">
<p>此功能目前仅适用于语言设置为 <em>英语</em> 在 <strong>评论 &gt; 评论设置 &gt; 常规</strong>. </p>
</div>
<h2 id="h_01J5BMHT1HAPZRQDVCY9KB8XP4">启用电子邮件内评论收集 </h2>
<ol>
<li>在 Klaviyo 中，导航至 <strong>评论</strong>. </li>
<li>选择 <strong>审核设置 &gt; 审核请求</strong>. </li>
<li>在 <em>电子邮件内评论集合</em> 卡，选择 <strong>使能够</strong>，然后在出现的模式中确认您的选择。 </li>
</ol>
<p>如果 <strong>使能够</strong> 按钮不可见，您已经启用了此功能；继续下一节。 </p>
<p>完成此步骤后，Klaviyo 会将通用内容块添加到您的帐户。您必须将此块添加到审核请求流程中的电子邮件中。 </p>
<h2 id="h_01J5BMHT1HJDSSE974PV89X6K4">将评论收集块添加到流程电子邮件 </h2>
<div class="bs-callout bs-callout-default">
<p>该块仅在由以下触发的流中受支持 <em>准备审核</em> 事件。如果您将此块添加到任何其他流程或活动中，它将无法正确呈现。 </p>
</div>
<ol>
<li>导航至您的审核请求流程。 </li>
<li>在流程中打开电子邮件模板。 </li>
<li>从 <em>内容</em> 选项卡，选择 <strong>普遍的</strong>.<br/>
<img alt="The universal content tab" height="165" src="https://klaviyo.zendesk.com/hc/article_attachments/28722600135067" width="428"/>
</li>
<li>搜索<strong> 电子邮件内评论集 - Klaviyo 评论</strong>. </li>
<li>单击电子邮件内审阅请求块并将其拖动到您的电子邮件中。 </li>
<li>从您的消息中删除之前的星级评级块。</li>
</ol>
<p>在编辑电子邮件内审阅请求块之前， <a href="https://help.klaviyo.com/hc/en-us/articles/115005413888">保存副本</a> 首先。更改后无法将块恢复为其原始设置。编辑此块需要直接编辑代码，仅建议开发人员或精通代码的营销人员使用。 </p>
<h3 id="h_01J5BMHT1H2J2HJAA2X7ABAAY4">应用内电子邮件阻止代码</h3>
<p>如果您需要恢复到电子邮件内评论收集块的原始版本，请复制下面您的首选代码片段并将其粘贴到 HTML 块或文本块的源代码字段中： </p>
<div class="accordion accordion--default">
<div class="accordion__item">
<div class="accordion__item-title"><strong>无评论标题</strong></div>
<div class="accordion__item-content">
<pre><code class="language-text">&lt;div class="kl_reviews__email_submission" style="display: block; margin: auto; padding: 24px;"&gt;&lt;!--[if !mso]&gt;&lt;!--&gt;&lt;form action="{{ event.review_link }}" method="GET"&gt;
    &lt;h4 class="kl_reviews__email_submission__header" style="font-weight: bold;"&gt;Rating&lt;/h4&gt;
    &lt;table class="kl_reviews__email_submission__ratings" style="width: 100%; margin-bottom: 32px;"&gt;
        &lt;tbody&gt;
            &lt;tr&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating1" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="1"&gt; &lt;label style="display: block; cursor: pointer;" for="rating1"&gt;1 ★&lt;/label&gt;&lt;/td&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating2" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="2"&gt; &lt;label style="display: block; cursor: pointer;" for="rating2"&gt;2 ★&lt;/label&gt;&lt;/td&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating3" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="3"&gt; &lt;label style="display: block; cursor: pointer;" for="rating3"&gt;3 ★&lt;/label&gt;&lt;/td&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating4" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="4"&gt; &lt;label style="display: block; cursor: pointer;" for="rating4"&gt;4 ★&lt;/label&gt;&lt;/td&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating5" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="5"&gt; &lt;label style="display: block; cursor: pointer;" for="rating5"&gt;5 ★&lt;/label&gt;&lt;/td&gt;
            &lt;/tr&gt;
        &lt;/tbody&gt;
    &lt;/table&gt;
    &lt;h4 class="kl_reviews__email_submission__header" style="font-weight: bold;"&gt;Your review&lt;/h4&gt;
    &lt;textarea class="kl_reviews__email_submission__content" style="display: block; width: 99%; height: 120px; border: 1px solid #d9d9d9; border-radius: 4px; margin-bottom: 32px; font-size: 16px;" name="content"&gt;&amp;#8203;&lt;/textarea&gt; &lt;button class="kl_reviews__email_submission__submit" style="display: block; width: 100%; border-radius: 2px; background-color: #000; color: #fff; cursor: pointer; border: none; height: 50px; font-size: 16px; margin-bottom: 32px;" type="submit"&gt; Submit review &lt;/button&gt;&lt;/form&gt;&lt;!--&lt;![endif]--&gt;
   &lt;h4 class="kl_reviews__email_submission__fallback" style="text-align: center; font-weight: bold;"&gt;Having trouble with the form?&lt;/h4&gt;
   &lt;a class="kl_reviews__email_submission__fallback_link" href="{{ event.review_link }}" style="display: block; text-align: center; cursor: pointer; font-size: 14px; font-weight: 400;"&gt;Write review on the web&lt;/a&gt;
&lt;/div&gt;</code></pre>
</div>
</div>
<div class="accordion__item">
<div class="accordion__item-title"><strong>带有评论标题</strong></div>
<div class="accordion__item-content">
<pre><code class="language-text">&lt;div class="kl_reviews__email_submission" style="display: block; margin: auto; padding: 24px;"&gt;&lt;!--[if !mso]&gt;&lt;!--&gt;&lt;form action="{{ event.review_link }}" method="GET"&gt;
    &lt;h4 class="kl_reviews__email_submission__header" style="font-weight: bold;"&gt;Rating&lt;/h4&gt;
    &lt;table class="kl_reviews__email_submission__ratings" style="width: 100%; margin-bottom: 32px;"&gt;
        &lt;tbody&gt;
            &lt;tr&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating1" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="1"&gt; &lt;label style="display: block; cursor: pointer;" for="rating1"&gt;1 ★&lt;/label&gt;&lt;/td&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating2" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="2"&gt; &lt;label style="display: block; cursor: pointer;" for="rating2"&gt;2 ★&lt;/label&gt;&lt;/td&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating3" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="3"&gt; &lt;label style="display: block; cursor: pointer;" for="rating3"&gt;3 ★&lt;/label&gt;&lt;/td&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating4" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="4"&gt; &lt;label style="display: block; cursor: pointer;" for="rating4"&gt;4 ★&lt;/label&gt;&lt;/td&gt;
                &lt;td style="width: 20%;"&gt;&lt;input id="rating5" style="display: block; cursor: pointer; margin-bottom: 8px;" name="rating" type="radio" value="5"&gt; &lt;label style="display: block; cursor: pointer;" for="rating5"&gt;5 ★&lt;/label&gt;&lt;/td&gt;
            &lt;/tr&gt;
        &lt;/tbody&gt;
    &lt;/table&gt;
    &lt;h4 class="kl_reviews__email_submission__header" style="font-weight: bold;"&gt;Your review&lt;/h4&gt;
    &lt;textarea class="kl_reviews__email_submission__content" style="display: block; width: 99%; height: 120px; border: 1px solid #d9d9d9; border-radius: 4px; margin-bottom: 32px; font-size: 16px;" name="content"&gt;&amp;#8203;&lt;/textarea&gt;
    &lt;h4 class="kl_reviews__email_submission__header" style="font-weight: bold;"&gt;Review headline&lt;/h4&gt;
    &lt;input class="kl_reviews__email_submission__headline" style="display: block; width: 99%; height: 36px; border: 1px solid #d9d9d9; border-radius: 4px; margin-bottom: 32px; font-size: 16px;" name="headline" type="text"&gt; 
    &lt;button class="kl_reviews__email_submission__submit" style="display: block; width: 100%; border-radius: 2px; background-color: #000; color: #fff; cursor: pointer; border: none; height: 50px; font-size: 16px; margin-bottom: 32px;" type="submit"&gt; Submit review &lt;/button&gt;&lt;/form&gt;&lt;!--&lt;![endif]--&gt;
    &lt;h4 class="kl_reviews__email_submission__fallback" style="text-align: center; font-weight: bold;"&gt;Having trouble with the form?&lt;/h4&gt;
    &lt;a class="kl_reviews__email_submission__fallback_link" href="{{ event.review_link }}" style="display: block; text-align: center; cursor: pointer; font-size: 14px; font-weight: 400;"&gt;Write review on the web&lt;/a&gt;
&lt;/div&gt;</code></pre>
</div>
</div>
</div>
<h3 id="h_01J5BMJCFEA3JF0QPFE2H8K92X">关于电子邮件内审阅阻止</h3>
<p>电子邮件内审阅块包含 3 个字段： </p>
<ul>
<li>
<strong>评论评级</strong><br/>
用于选择 1-5 颗星的单选按钮选项 </li>
<li>
<strong>评论内容</strong><br/>
用于评论内容的开放文本字段 </li>
<li>
<strong>评论标题</strong><br/>
用于评论标题或标题的开放文本字段（仅在评论提交页面编辑器中选择时才可见）</li>
</ul>
<p>这些字段不可编辑。自定义问题不会出现在电子邮件内审阅块中。</p>
<p><img alt="An example of the in-email review collection form" height="494" src="https://klaviyo.zendesk.com/hc/article_attachments/28722600137371" width="510"/></p>
<h2 id="h_01J5BMJCFEBPA5NSVYAHHNX7BG">局限性 </h2>
<p>此功能依赖于 HTML &lt;form&gt; 元素，该元素是 <a href="https://www.caniemail.com/features/html-form/">并非所有收件箱提供商都支持</a>。如果收件人在不支持表单元素的收件箱中打开您的审阅请求电子邮件，他们将看到一个用于提交审阅的链接。 </p>
<p>电子邮件内评论收集不支持自定义问题。如果您有自定义问题，审阅者只会在某些情况下看到它们。 </p>
<ul>
<li>如果你有 <strong>必需的</strong> 自定义问题，提交电子邮件内审核表单会将审核者重定向到新选项卡，他们必须在其中完成自定义问题才能提交审核。部分审核提交的内容将不会被存储。 </li>
<li>如果你有 <strong>非必需</strong> 自定义问题，审阅者从收件箱提交审阅后将看到成功页面。仅那些导航至产品页面并单击 <strong>写评论</strong> 按钮将看到您的自定义问题。</li>
</ul>
<h2 id="h_01J5BMJCFEP38TDE6CCMQZGR4E">结果 </h2>
<p>完成这些步骤后，您的客户可以直接通过电子邮件提交评论，无需打开其他选项卡或窗口来访问您的评论申请表。 </p>