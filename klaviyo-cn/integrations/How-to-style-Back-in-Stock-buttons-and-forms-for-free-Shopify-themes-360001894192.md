---
id: "360001894192"
title: "如何免费设置“返回库存”按钮和表单的 Shopify 主题样式"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360001894192-How-to-style-Back-in-Stock-buttons-and-forms-for-free-Shopify-themes"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:41Z"
language: "zh"
translation_strategy: "google_html_text_nodes_preserve_attributes"
---
<h2 id="h_01HTJAZ94K6JYQJEQ6E8WS3R8G">你会学到</h2>
<p>了解对每个免费 Shopify 主题进行哪些关键更改，以快速确保您的“返回库存”按钮和表单与您的主题样式相匹配。 Klaviyo“可用时通知我”按钮和表单具有高度可配置性。您可以根据您的设计偏好更改颜色、字体、文本和其他元素。 </p>
<div class="bs-callout bs-callout-default">
<p>仅某些免费 Shopify 主题支持安装 back in stock，而不支持使用自定义主题的 Shopify 商店。目前，Klaviyo 支持人员无法协助使用自定义主题的商店实施补货。要检查您的商店正在使用哪个 Shopify 主题，您可以使用 <a href="https://pagefly.io/blogs/shopify/shopify-theme-detector">Shopify 主题检测器</a>. </p>
</div>
<h2 id="h_01HTJAZ94K01343CFQ6RVYXJ0F">开始之前</h2>
<p>如果您还没有阅读我们的指南 <a href="https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify">开始使用 Shopify</a> 在继续本文之前，请参阅有关集成的分步说明。</p>
<p>要更全面地了解“返回库存”功能以及如何启用该功能，请阅读我们的指南： <a href="https://klaviyo.zendesk.com/hc/en-us/articles/360001895651">install back in stock for Shopify.</a></p>
<h2 id="h_01HTJAZ94K1AQ45YDC6N2FE0MN">如何设计按钮和表单的样式</h2>
<ol>
<li>当你在 <a href="https://help.klaviyo.com/hc/en-us/articles/360001895651-How-to-Install-Back-in-Stock-for-Shopify#install-the-snippet5">安装你的代码片段</a>，在本文中找到您的免费​​主题的样式片段。</li>
<li>默认代码片段如下所示。更新（或添加）内的行项目 <code>trigger: {} </code>和 <code>modal: {}</code> 根据样式片段中显示的内容，默认片段的部分
<ol>
<li>For example, if you have the Crave theme, you only need to add the the following line within the modal section: <code> font_family: '"Archivo", serif;'</code>
</li>
</ol>
</li>
<li>根据您认为合适的情况，对订单项进行任何其他所需的样式更新。</li>
</ol>
<pre><code class="language-text">&lt;script src="https://a.klaviyo.com/media/js/onsite/onsite.js"&gt;&lt;/script&gt;
&lt;script&gt;
    var klaviyo = klaviyo || [];
    klaviyo.init({
      account: "PUBLIC_API_KEY",
      platform: "shopify"
    });
    klaviyo.enable("backinstock",{ 
    trigger: {
      product_page_text: "Notify Me When Available",
      product_page_class: "button",
      product_page_text_align: "center",
      product_page_margin: "0px",
      replace_anchor: false
    },
    modal: {
     headline: "{product_name}",
     body_content: "Register to receive a notification when this item comes back in stock.",
     email_field_label: "Email",
     button_label: "Notify me when available",
     subscription_success_label: "You're in! We'll let you know when it's back.",
     footer_content: '',
     additional_styles: "@import url('https://fonts.googleapis.com/css2?family=Roboto+wght@400;700&amp;display=swap');",
     drop_background_color: "#000",
     background_color: "#fff",
     text_color: "#222",
     button_text_color: "#fff",
     button_background_color: "#439fdb",
     close_button_color: "#ccc",
     error_background_color: "#fcd6d7",
     error_text_color: "#C72E2F",
     success_background_color: "#d3efcd",
     success_text_color: "#1B9500"
    }
  });
&lt;/script&gt;</code></pre>
<h2 id="h_01J2F85JJ53HRHS8WMDD6C07SS">渴望</h2>
<pre><code class="language-text">trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Archivo", serif;'
}</code></pre>
<h2 id="h_01J2F85JJ5WZA9KGJZ806TM109">黎明</h2>
<pre><code class="language-text">trigger: {
 product_page_class: 'button'
},
modal: {
font_family: '"Assistant", sans-serif;' 
}</code></pre>
<h2 id="h_01J2F87TMW1R2RSYY6FF4D2EXJ">工作室</h2>
<pre><code class="language-text">trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Electra", serif;' 
}</code></pre>
<h2 id="h_01J2F87TMWBB5A5VQCEE3V1Z6Q">色块</h2>
<pre><code class="language-text">trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Futura", sans-serif;' }</code></pre>
<h2 id="h_01J2F87TMWXY6QN1P1AD5SMVT3">感觉</h2>
<pre><code class="language-text">trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Harmonia Sans", sans-serif;'
}</code></pre>
<h2 id="h_01J2F87TMW07RH4748SVRSHZTS">品尝</h2>
<pre><code class="language-text">trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Anonymous Pro", sans-serif;'
}</code></pre>
<h2 id="h_01J2F87TMWCKTN1BQP2X5WF6F2">工艺</h2>
<pre><code class="language-text">trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Quattrocento Sans", sans-serif;'
}</code></pre>
<h2 id="h_01J2F87TMW91YFSZNTKTDGNHHZ">骑</h2>
<pre><code class="language-text">trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Avenir Next", sans-serif;'
}</code></pre>
<h2 id="h_01J2F87TMWB1K2S579NCBKBVYQ">刷新</h2>
<pre><code class="language-text">trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Questrial", sans-serif;'
}</code></pre>
<h2 id="h_01HTJAZ94KFEMRXC16B0PMFA0K">简单的</h2>
<h3 id="h_01HTJAZ94KE5YBW7YKS6F7ZT02">美丽</h3>
<pre><code class="language-text">modal: {
 font_family: '"PT Serif",serif;'
}</code></pre>
<h2 id="h_01HTJAZ94KK5A0T1589HE2XQ6V">流行音乐</h2>
<h3 id="h_01HTJAZ94KCWCQ6RNE05TC1ZE6">骨</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Raleway');",
 font_family: '"Raleway","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94KDV2DK2DBGTF35EKE">玩具</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--large btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Open+Sans');",
 font_family: '"Open Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94KKTK759FYPFREEY0E">黑与白</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--large btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Open+Sans');",
 font_family: '"Open Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94KTC4X262P89A9NJV8">充满活力</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--large btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Open+Sans');",
 font_family: '"Open Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h2 id="h_01HTJAZ94K4QV5DMEG0Q55DN0E">创业</h2>
<h3 id="h_01HTJAZ94KQQAZE7AJEG74467N">单板滑雪</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Karla');",
 font_family: '"Karla","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94KS71GJ6QSQ931XA9X">户外活动</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Roboto');",
 font_family: '"Roboto","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94KJGVP5SMWB7EZBKMS">拳击</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');",
 font_family: '"Source Sans Pro","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h2 id="h_01HTJAZ94KQKMC6KS0F3T2VSW9">首次亮相</h2>
<h3 id="h_01HTJAZ94KVS37RMFCTK3R37E5">默认</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Work+Sans');",
 font_family: '"Work Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94MY21NCQBAZY9FKST6">光</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Muli');",
 font_family: '"Muli","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h2 id="h_01HTJAZ94MAK1HPKX769XA19ES">供应</h2>
<h3 id="h_01HTJAZ94MW0GM8ZPFDNY7T4KR">光</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Roboto');",
 font_family: '"Roboto","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94M51W750WK83D1E576">蓝色的</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--large btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Montserrat');",
 font_family: '"Montserrat","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h2 id="h_01HTJAZ94MR1PJBBP149XGTHPQ">叙述</h2>
<h3 id="h_01HTJAZ94M88VJ6QCT4P6HTKK0">温暖的</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Avenir');",
 font_family: '"Avenir","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94MWDVVR4WMD58SH2XV">光</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Open+Sans');",
 font_family: '"Open Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94MHCZVPYQ0ASSWX5TB">寒冷的</h3>
<pre><code class="language-text">trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Lato');",
 font_family: '"Lato","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h2 id="h_01HTJAZ94MYXSCD69NGT3AJV9M">布鲁克林</h2>
<h3 id="h_01HTJAZ94MSPCNQC3YE8W622VW">经典的</h3>
<pre><code class="language-text">modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Arapey');",
 font_family: '"Arapey",serif;'
}</code></pre>
<h2 id="h_01HTJAZ94MEFK6CHKP4DS9PP7N">最小</h2>
<h3 id="h_01HTJAZ94MPAMWTXGT6D10FDB0">现代的</h3>
<pre><code class="language-text">modal: {
 font_family: '"PT Serif",serif;'
}</code></pre>
<h3 id="h_01HTJAZ94MCP4ZBK0S2KPVM8C6">优质的</h3>
<pre><code class="language-text">modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=PT+Sans');",
 font_family: '"PT Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h3 id="h_01HTJAZ94MGC0N5YQYRP048018">时尚</h3>
<pre><code class="language-text">modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=PT+Sans');",
 font_family: '"PT Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}</code></pre>
<h2 id="h_01HTJAZ94MPQAQQ60MC5CVGCDK">结果</h2>
<p>您现在已经更新了 Shopify 商店中的“返回库存”按钮和表单的样式。 </p>