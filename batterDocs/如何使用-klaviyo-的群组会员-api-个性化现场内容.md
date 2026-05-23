<h1>如何使用 Klaviyo 的群组会员 API 个性化现场内容</h1>

<h2>你将会学到</h2>
<p>了解如何使用 <strong>klaviyo</strong> JavaScript 对象的 getGroupMembership 方法，该方法可用于在您的网站上实现现场个性化。这需要加载 <strong>klaviyo</strong> 对象并传递一组列表或段进行检查，这将返回一个输出，您可以利用该输出进行现场个性化。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。 ## 开始之前</p>
<p>此功能仅适用于高级 KDP 客户，并且只能通过 <strong>klaviyo</strong> 对象使用。要了解有关 <strong>klaviyo</strong> JavaScript 对象及其功能的更多信息，请阅读 [Klaviyo 对象简介](https://developers.klaviyo.com/en/docs/introduction_to_the_klaviyo_object)</p>
<p>当您将 Klaviyo 的现场跟踪添加到您的网站时，只会跟踪“已知浏览器”的浏览活动（即已访问、参与并被识别或“cookied”的浏览器）。 Klaviyo 的现场跟踪不会跟踪匿名浏览器。 Klaviyo 可通过 3 种主要方式识别网站访问者以进行现场跟踪：</p>
<ul>
<li>如果有人点击通过 Klaviyo 电子邮件访问您的网站</li>
<li>如果有人通过 Klaviyo 表格订阅</li>
<li>如果有人登录您的网站并且您安装了跟踪</li>
</ul>
<p>请观看我们的 Klaviyo 的[视频](https://www.youtube.com/watch?v=0MYFjCsm9nw)，了解如何使用群组成员身份 API。 ## 安装 Klaviyo.js 并加载 Klaviyo 对象</p>
<p>如果您还没有安装 Klaviyo.js，您首先需要安装它。 Klaviyo.js，也称为 [Klaviyo 的 Active on Site JavaScript](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration#active-on-site-tracking-snippet)，自动支持 <strong>klaviyo</strong> 对象。如果您启用了与 Klaviyo 帐户的集成或手动安装了 Klaviyo.js，您将能够启动 <strong>klaviyo</strong> 对象来侦听相关调用。要在页面加载时立即使用 <strong>klaviyo</strong> 对象，我们建议在您的网站上手动安装以下代码段（除了如上所述安装 Klaviyo.js 之外）。 <strong>klaviyo</strong> 对象每页只需加载一次。要加载 <strong>klaviyo</strong> 对象：</p>
<p>````</p>
<p>!(函数(){</p>
<p>如果（！window.klaviyo）{</p>
<p>窗口._klOnsite = 窗口._klOnsite || []；</p>
<p>尝试{</p>
<p>window.klaviyo = 新代理(</p>
<p>{},</p>
<p>{</p>
<p>得到：函数（n，i）{</p>
<p>返回“推”===我</p>
<p>？函数（）{</p>
<p>变量n；</p>
<p>(n = window._klOnsite).push.apply(n, 参数);</p>
<p>}</p>
<p>：函数（）{</p>
<p>对于（</p>
<p>var n = 参数长度，o = 新数组(n)，w = 0;</p>
<p>w < n；</p>
<p>w++</p>
<p>）</p>
<p>o[w] = 参数[w]；</p>
<p>变量t =</p>
<p>“函数”== typeof o[o.length - 1] ？ o.pop() : 无效 0,</p>
<p>e = 新 Promise(函数 (n) {</p>
<p>window._klOnsite.push(</p>
<p>[i].concat(o, [</p>
<p>函数（一）{</p>
<p>t && t(i), n(i);</p>
<p>},</p>
<p>]),</p>
<p>）；</p>
<p>});</p>
<p>返回e；</p>
<p>};</p>
<p>},</p>
<p>},</p>
<p>）；</p>
<p>} 捕获 (n) {</p>
<p>(window.klaviyo = window.klaviyo || []),</p>
<p>(window.klaviyo.push = 函数 () {</p>
<p>变量n；</p>
<p>(n = window._klOnsite).push.apply(n, 参数);</p>
<p>});</p>
<p>}</p>
<p>}</p>
<p>})();</p>
<p>````</p>
<p>要使用 <strong>klaviyo</strong> JavaScript 对象的 getGroupMembership 方法进行现场个性化：</p>
<p>1. 在您的代码中，选择您要检查其成员资格的列表或分段 ID。限制为 50 个列表或段。 2. 通过 Klaviyo 表单或其他方式识别您网站上的用户。 3. 按照以下格式进行调用，并使用要检查成员资格的列表或分段 ID 的数组：</p>
<p>````</p>
<p>klaviyo.getGroupMembership(['listID1', 'listID2', 'listID3'])</p>
<p>````</p>
<p>提供的输出将是已识别用户所属的列表/段 ID 的数组，前提是这些 ID 位于输入数组中。 如果返回空数组，则意味着您传入了太多 ID，或者该用户不属于您提供的任何列表或段。您可以使用返回的细分和列表会员数据，根据 Klaviyo 的客户细分，使用相关产品、内容等自定义您的网站。 ### 代码示例</p>
<p>以下示例展示了如何使用多个分段 ID 调用 getGroupMembership API。 ````</p>
<p>const customerSegments = 等待 klaviyo.getGroupMembership([</p>
<p>VIPSegmentID,</p>
<p>未参与的段ID，</p>
<p>DogLoversSegmentID</p>
<p>]);</p>
<p>````</p>
<h2>对站点性能的影响</h2>
<p>组成员身份 API 对站点性能的影响极小。 Klaviyo 在您网站上加载的 Javascript 文件（即 web\_personalization.js）仅约 1.2KB，并且该文件的捆绑请求不会阻塞主线程，因此不会影响任何页面的可用性。根据客户配置文件自定义站点而加载的数据在首次请求后会缓存在浏览器中，因此其他请求不需要后端 API 调用。 ## 结果</p>
<p>现在，您可以将 <strong>klaviyo</strong> JavaScript 对象与 Web 个性化工具结合使用，并根据细分或列表成员资格对网站内容进行个性化。</p>
