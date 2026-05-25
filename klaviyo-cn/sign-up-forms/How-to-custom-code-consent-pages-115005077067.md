---
id: "115005077067"
title: "如何自定义代码同意页面"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005077067-How-to-custom-code-consent-pages"
section: "Getting started with consent pages"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:18Z"
language: "zh"
translation_strategy: "google_html_text_nodes_preserve_attributes"
---
<h2 id="h_01J5970D8JQERTQ81M9RYBQYPF">你会学到</h2>
<p>了解如何启用和使用 Klaviyo 的托管页面功能，该功能允许您自定义代码自己的首选项页面、订阅页面和取消订阅页面。</p>
<div class="bs-callout bs-callout-default">
<p>本文适用于开发者； Klaviyo 目前不提供帮助构建自定义代码的服务，也不提供自定义代码故障排除的支持。要了解我们的内置应用程序同意页面，请访问我们的 <a href="https://help.klaviyo.com/hc/en-us/articles/115005251848" rel="noopener" target="_blank">有关同意页面入门的文章</a>.</p>
</div>
<h2 id="h_01J5970D8J98RVN0GADKN2VJ6W">开始之前</h2>
<p>在配置托管页面之前，启用此功能：</p>
<ol>
<li>导航至 <strong>设置 &gt; 其他</strong>.</li>
<li>选择 <strong>同意书页 </strong>从下拉菜单中。</li>
<li>在下面 <em>自定义托管页面</em>，将开关切换至 <em>对托管页面使用自定义专用域</em>.<br/><img alt="The Custom Hosted Pages section on the Consent Pages tab in Klaviyo showing the switch to enable hosted pages." height="448" src="https://klaviyo.zendesk.com/hc/article_attachments/33232831304219" width="519"/>
</li>
</ol>
<div class="bs-callout bs-callout-default">
<p>请注意，只有通过了付费计划的帐户<a href="https://help.klaviyo.com/hc/en-us/articles/115000628331" rel="noopener" target="_blank"> 账户验证</a> 有权访问此设置。</p>
</div>
<h2 id="h_01J5970D8JJCQ078TWYT1ADHV9">创建自定义同意页面</h2>
<ol>
<li>前往 <strong>设置 &gt; 其他</strong>.</li>
<li>点击 <strong>托管页面</strong>. </li>
<li>旁边 <em>页数</em>，单击 <strong>+</strong> 符号添加新页面。</li>
<li>命名此页面（例如，unsubscribe.tmpl）；您可以将其用于任何同意页面，但如果您愿意，可以创建多个页面。 <br/>
<div class="bs-callout bs-callout-default">
<p>托管页面名称不能包含空格，否则会导致错误。避免使用空格或使用下划线来分隔标题。</p>
</div>
</li>
<li>设计一个包含您选择的字段和功能的 HTML 页面。可以为自定义同意页面插入的示例字段包括：<br/>
<ul>
<li>电子邮件频率的选择：<br/>
<ul>
<li>取消订阅的选项</li>
<li>接收所有电子邮件的选项</li>
<li>每日、每周、每月等时事通讯的频率选项</li>
</ul>
</li>
<li>可用于定位和细分的信息：
<ul>
<li>用户是否想要销售公告的复选框</li>
<li>用户是否想要产品公告的复选框</li>
<li>用户是否想要博客更新的复选框</li>
<li>用户可能想要加入的其他列表</li>
</ul>
</li>
</ul>
</li>
</ol>
<div class="accordion accordion--default">
<div class="accordion__item">
<div class="accordion__item-title"><strong>同意页面的 HTML 代码示例</strong></div>
<div class="accordion__item-content">
<p>您可以在 unsubscribe.tmpl 中使用此代码来获取功能齐全的同意页面，其中包含电子邮件类型和频率首选项：</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
   &lt;head&gt;
      &lt;meta charset="utf-8"&gt;
      &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
      &lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;
      &lt;!-- Latest compiled and minified CSS --&gt;
      &lt;link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"&gt;
      &lt;style type="text/css"&gt;
        /* Space out content a bit */
        body {
            padding-top: 20px;
            padding-bottom: 20px;
        }

        form {
            margin-bottom: 18px;
        }

        /* Custom page header */
        .header {
            border-bottom: 1px solid #e5e5e5;
            margin-bottom: 10px;
        }

        .header h1 {
            margin: 10px 0;
        }

        .required-fields {
            text-align: right;
        }

        .required-fields span {
            color: #a94442;
            font-weight: bold;
        }

        .list-group-item label {
            font-weight: normal;
            margin-top: 17px;
        }

        .list-group-item label input[type="checkbox"] {
            margin-right: 4px;
        }

        .form-group span.required {
            position: absolute;
            top: 0;
            right: 0;
            font-size: 20px;
            color: #a94442;
            font-weight: bold;
            user-select: none;
        }

        label.error {
            color: #a94442;
            font-weight: bold;
            margin-top: 4px;
        }

        .form-actions {
            margin: 25px 0;
        }

        .form-control+.form-control {
            margin-top: 6px;
        }

        .panel-group .panel-title .closed-icon,
        .panel-group .panel-title .open-icon {
            margin-right: 0.5em;
            top: 2px;
        }

        .panel-group .panel-title a:hover,
        .panel-group .panel-title a:active {
            text-decoration: none;
        }

        .panel-group .panel-title a:hover .text,
        .panel-group .panel-title a:active .text {
            text-decoration: underline;
        }

        .panel-group .panel-title .closed-icon {
            display: none;
        }

        .panel-group.closed .panel-title .open-icon {
            display: none;
        }

        .panel-group.closed .panel-title .closed-icon {
            display: inline;
        }

        /* Custom page footer */
        .footer {
            padding-top: 18px;
            border-top: 1px solid #e5e5e5;
        }

        /* Customize container */
        @media (min-width: 768px) {
            .container {
                max-width: 730px;
            }
        }
    &lt;/style&gt;
      &lt;!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries --&gt;
      &lt;!-- WARNING: Respond.js doesn't work if you view the page via file:// --&gt;
      &lt;!--[if lt IE 9]&gt;
      &lt;script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"&gt;&lt;/script&gt;
      &lt;script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"&gt;&lt;/script&gt;
      &lt;![endif]--&gt;
   &lt;/head&gt;
   &lt;body&gt;
      &lt;div class="container"&gt;
         &lt;div class="header"&gt;
            &lt;img src="http://via.placeholder.com/300x75" /&gt;
            &lt;h1&gt;Email Preferences&lt;/h1&gt;
         &lt;/div&gt;
         &lt;form action="" id="preferences_form" method="POST" role="form" class="form-horizontal"&gt;
            {% if form.non_field_errors %}
            &lt;div class="alert alert-danger"&gt;
               {% for error in form.non_field_errors %}
               {{ error }}{% if not forloop.last %}&lt;br /&gt;{% endif %}
               {% endfor %}
            &lt;/div&gt;
            {% endif %}
            &lt;input type="hidden" name="$fields" value="EmailInterests,EmailFrequency" /&gt;
            &lt;input type="hidden" name="$list_fields" value="EmailInterests" /&gt;
            &lt;!-- &lt;input type="hidden" name="$unsubscribed_url" value="/p/preferences_updated" /&gt; --&gt;
            &lt;!-- &lt;input type="hidden" name="$updated_profile_url" value="/p/preferences_updated" /&gt; --&gt;
            &lt;!--&lt;p class="required-fields"&gt;
               &lt;span&gt;*&lt;/span&gt; Required Information
               &lt;/p&gt;--&gt;
            &lt;div class="form-group{% if form.errors|lookup:'$email' %} has-error{% endif %}"&gt;
               &lt;label for="email" class="col-sm-3 control-label"&gt;Email Address&lt;span class="required"&gt;*&lt;/span&gt;&lt;/label&gt;
               &lt;div class="col-sm-9"&gt;
                  &lt;input type="email" class="form-control" id="email" name="$email" value="{% if request.POST|lookup:'$email' %}{{ request.POST|lookup:'$email' }}{% else %}{{ person.email|default:'' }}{% endif %}" /&gt;
                  {% if form.errors|lookup:'$email' %}
                  &lt;p class="help-block"&gt;{% for error in form.errors|lookup:'$email' %}{{ error }}{% endfor %}&lt;/p&gt;
                  {% endif %}
               &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
               &lt;label for="first_name" class="col-sm-3 control-label"&gt;First Name&lt;/label&gt;
               &lt;div class="col-sm-9"&gt;
                  &lt;input type="text" class="form-control" id="first_name" name="$first_name" value="{% if request.POST|lookup:'$email' %}{{ request.POST|lookup:'$first_name' }}{% else %}{{ person.first_name|default:'' }}{% endif %}" /&gt;
               &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
               &lt;label for="last_name" class="col-sm-3 control-label"&gt;Last Name&lt;/label&gt;
               &lt;div class="col-sm-9"&gt;
                  &lt;input type="text" class="form-control" id="last_name" name="$last_name" value="{% if request.POST|lookup:'$email' %}{{ request.POST|lookup:'$last_name' }}{% else %}{{ person.last_name|default:'' }}{% endif %}" /&gt;
               &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
               &lt;label for="interests" class="col-sm-3 control-label"&gt;Interests&lt;/label&gt;
               &lt;div class="col-sm-9"&gt;
                  &lt;div class="checkbox"&gt;
                     &lt;label&gt;
                     &lt;input type="checkbox" name="EmailInterests" value="New Releases" {% if 'New Releases' in person.EmailInterests or 'New Releases' in request.POST.EmailInterests %}checked="checked"{% elif not person.EmailInterests and not request.POST.EmailInterests %}{% endif %} /&gt;
                     New Product Releases
                     &lt;/label&gt;
                  &lt;/div&gt;
                  &lt;div class="checkbox"&gt;
                     &lt;label&gt;
                     &lt;input type="checkbox" name="EmailInterests" value="Promotions" {% if 'Promotions' in person.EmailInterests or 'Promotions' in request.POST.EmailInterests %}checked="checked"{% elif not person.EmailInterests and not request.POST.EmailInterests %}{% endif %} /&gt;
                     Promotions &amp; Sales
                     &lt;/label&gt;
                  &lt;/div&gt;
                  &lt;div class="checkbox"&gt;
                     &lt;label&gt;
                     &lt;input type="checkbox" name="EmailInterests" value="Blog" {% if 'Blog' in person.EmailInterests or 'Blog' in request.POST.EmailInterests %}{% elif not person.EmailInterests and not request.POST.EmailInterests %}{% endif %} /&gt;
                     Latest from the Blog
                     &lt;/label&gt;
                  &lt;/div&gt;
                  &lt;div class="checkbox"&gt;
                     &lt;label&gt;
                     &lt;input type="checkbox" name="EmailInterests" value="Events" {% if 'Events' in person.EmailInterests or 'Events' in request.POST.EmailInterests %}{% elif not person.EmailInterests and not request.POST.EmailInterests %}{% endif %} /&gt;
                     Events
                     &lt;/label&gt;
                  &lt;/div&gt;
               &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
               &lt;label for="interests" class="col-sm-3 control-label"&gt;How often would you like to hear from us?&lt;/label&gt;
               &lt;div class="col-sm-9"&gt;
                  &lt;div class="radio"&gt;
                     &lt;label&gt;
                        &lt;!-- Default value. --&gt;
                        &lt;input type="radio" name="EmailFrequency" id="email_frequency_0" value="All" {% if person.EmailFrequency == 'All' or request.POST.EmailFrequency == 'All' %}checked="checked"{% elif not person.EmailFrequency and not request.POST.EmailFrequency %}checked="checked"{% endif %} /&gt;
                        Twice per Week
                     &lt;/label&gt;
                  &lt;/div&gt;
                  &lt;div class="radio"&gt;
                     &lt;label&gt;
                     &lt;input type="radio" name="EmailFrequency" id="email_frequency_1" value="Weekly" {% if person.EmailFrequency == 'Weekly' or request.POST.EmailFrequency == 'Weekly' %}checked="checked"{% endif %} /&gt;
                     Once per Week
                     &lt;/label&gt;
                  &lt;/div&gt;
                  &lt;div class="radio"&gt;
                     &lt;label&gt;
                     &lt;input type="radio" name="EmailFrequency" id="email_frequency_2" value="Monthly" {% if person.EmailFrequency == 'Monthly' or request.POST.EmailFrequency == 'Monthly' %}checked="checked"{% endif %} /&gt;
                     Once per Month
                     &lt;/label&gt;
                  &lt;/div&gt;
               &lt;/div&gt;
            &lt;/div&gt;
            &lt;div class="checkbox"&gt;
               &lt;label&gt;
               &lt;input type="checkbox" name="$unsubscribe" value="true" /&gt;
               &lt;span class="text"&gt;Unsubscribe me from all emails.&lt;/span&gt;
               &lt;/label&gt;
            &lt;/div&gt;
            &lt;div class="clearfix form-actions"&gt;
               &lt;div class="pull-right"&gt;
                  &lt;button type="submit" class="btn btn-default btn-primary"&gt;Update Preferences&lt;/button&gt;
               &lt;/div&gt;
            &lt;/div&gt;
         &lt;/form&gt;
         &lt;footer class="footer"&gt;
            &lt;p&gt;
               © 2017 Company Name — &lt;a href="https://www.klaviyo.com" target="_blank"&gt;Privacy Policy&lt;/a&gt;
            &lt;/p&gt;
         &lt;/footer&gt;
      &lt;/div&gt;
      &lt;!-- /container --&gt;
      &lt;!-- jQuery (necessary for Bootstrap's JavaScript plugins) --&gt;
      &lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"&gt;&lt;/script&gt;
      &lt;!-- Latest compiled and minified JavaScript --&gt;
      &lt;script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"&gt;&lt;/script&gt;
      &lt;script src="//cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.13.1/jquery.validate.min.js"&gt;&lt;/script&gt;
      &lt;script&gt;
        $(function() {
            $('#preferences_form').validate({
                rules: {
                    $email: {
                        required: true
                    }
                },
                messages: {
                    $email: 'Please enter your email address.',
                    $first_name: 'Please enter your first name.',
                    $last_name: 'Please enter your last name.'
                }
            });
            // Toggle validation based on selection.
            $('input[name="$unsubscribe"]').on('change', function() {
                $('form .form-actions button[type="submit"]').toggleClass('cancel', $(this).is(':checked'));
            });
        });
        $('input[name="$unsubscribe"]').on('change', function(){
          $('input[type=checkbox]').not(this).prop('checked', false);
        });
        $('input[type=checkbox]').not('input[name="$unsubscribe"]').on('change', function(){
          $('input[name="$unsubscribe"]').prop('checked', false);
        });
    &lt;/script&gt;
   &lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
</div>
</div>
<h3 id="h_01JB21JMP9H68PS5P5AJT591RR">提交后设置托管页面的重定向（可选）</h3>
<p>默认情况下，成功提交托管页面（例如托管首选项页面）后，用户将被重定向到以下两个位置之一：</p>
<ul>
<li>如果他们请求取消订阅，他们将被发送到您帐户的默认取消订阅确认页面。</li>
<li>If they've updated their profile (or done anything that's not an unsubscribe request), the user will be sent to your account's default preferences confirmation (success) page.</li>
</ul>
<p>如果您使用上面的示例 HTML，这将在 &lt;body&gt; 中反映为：</p>
<pre><code class="language-html">&lt;!-- &lt;input type="hidden" <br/>name="$unsubscribed_url" value="/p/preferences_updated" /&gt; --&gt;<br/>&lt;!-- &lt;input type="hidden" <br/>name="$updated_profile_url" value="/p/preferences_updated" /&gt; --&gt;</code></pre>
<p>要自定义提交托管页面后将某人重定向到的位置，请将 value="..." 行调整为 HTML 中您的首选 URL。</p>
<h3 id="h_01J5970D8JMRWSME7B6FSA219D">将自定义资源添加到托管页面（可选）</h3>
<p>如果您想在托管页面上使用自己的 CSS 文件、JS 文件或图像，请通过单击 <strong>+</strong> 旁边的符号 <em>资产</em> 并在页面的源代码中引用它们。</p>
<p>使用以下标签来引用您已上传到 Klaviyo 帐户的资产： <code>{% asset_url 'style.css' %}</code></p>
<p class="wysiwyg-text-align-center"><img alt="source code of your consent page showing uploaded custom asset tag" src="https://klaviyo.zendesk.com/hc/article_attachments/30388426692507"/></p>
<h2 id="h_01J5970D8K3QFCJHTXHB4WQ31R">使用自定义同意页面</h2>
<p>您可以将每个帐户的默认同意页面替换为自定义编码页面，以便所有电子邮件默认使用这些自定义页面。或者，您可以仅配置 1 个特定列表以使用自定义编码页面，以便只有发送到该列表的电子邮件才会使用自定义页面。 </p>
<ul>
<li>如果您为特定列表自定义了同意页面，则发送到该列表的任何电子邮件都将使用这些唯一的同意页面。</li>
<li>您尚未为其自定义唯一同意页面的任何列表都将使用您帐户的默认同意页面。此外，任何未发送到特定列表的电子邮件，包括指标触发的流电子邮件、发送到分段的营销活动或 <a href="https://help.klaviyo.com/hc/en-us/articles/115005246328-Email-a-Single-Person-using-Klaviyo">个人电子邮件</a>，还将使用您的默认同意页面。</li>
</ul>
<h3 id="h_01J5970D8KFKEWWJ7P70V947GW">将默认同意页面更改为托管页面</h3>
<p>如果您想将帐户的 1 个或多个默认同意页面（例如首选项页面、订阅页面或电子邮件取消订阅页面）替换为自定义编码页面，请按照以下步骤操作： </p>
<ol>
<li>单击 Klaviyo 左下角您的公司名称。 </li>
<li>选择 <strong>设置</strong>.<br/><img alt="Account tab in the bottom left corner with settings selected from the navigation menu" height="451" src="https://klaviyo.zendesk.com/hc/article_attachments/28723623382427" width="369"/>
</li>
<li>选择 <strong>其他</strong> 从顶部。</li>
<li>单击您计划替换的同意页面上的 3 点下拉菜单，然后选择 <strong>使用托管页面</strong>.<br/><img alt="The Consent Pages tab in Klaviyo showing an the additional options menu open on an example preference page." src="https://klaviyo.zendesk.com/hc/article_attachments/33232831319067"/>
</li>
<li>在出现的对话框窗口中，选择您的自定义页面文件，然后单击 <strong>节省</strong>. </li>
</ol>
<div class="bs-callout bs-callout-default">
<p>如果您想对发送到分段的流电子邮件或营销活动使用自定义页面，则必须将帐户的默认同意页面切换为使用自定义页面。按照与上述相同的流程，将默认同意页面替换为自定义编码页面。 </p>
</div>
<h3 id="h_01J5970D8KQQAMFFKSBMBWB3P6">使用自定义同意页面作为列表</h3>
<p>您必须配置要使用自定义页面而不是默认同意页面的每个单独列表。</p>
<ol>
<li>导航到您想要连接到自定义页面的列表。 </li>
<li>单击 <strong>订阅和偏好页面</strong> 选项卡可查看该列表的所有可编辑同意页面。 </li>
<li>在您想要替换为自定义页面的同意页面下，单击 3 点下拉菜单并选择 <strong>使用托管页面</strong>. <br/><img alt="The Subscribe &amp; preferences pages tab for an example list in Klaviyo showing the additional actions menu open on the preferences page." height="445" src="https://klaviyo.zendesk.com/hc/article_attachments/33232831322779" width="539"/><br/>
<div class="bs-callout bs-callout-default">
<p>请注意，如果您愿意，您可以选择对所有同意页面使用托管页面。</p>
</div>
</li>
<li>在出现的对话框窗口中，选择您的自定义页面文件，然后单击 <strong>节省</strong>.</li>
</ol>
<div class="bs-callout bs-callout-default">
<p>在您的电子邮件中，您仍然应该使用标准的 Klaviyo 取消订阅和管理首选项标签 <span style="font-weight: 400;">（即 {% unsubscribe %} 和 {% manage_preferences %}）。这些标签将作为链接填充在您的实时电子邮件中，并自动将收件人带到您的自定义页面。 </span></p>
</div>
<h2 id="h_01J5970D8KBWN7ZDXDH73P5895">托管页面常见问题解答</h2>
<p><strong>我是否需要在页面中添加任何 JavaScript 才能正确提交此表单？</strong><br/>由于您的自定义表单将包含在托管页面内，因此您无需向 &lt;form&gt; 添加任何额外的 JavaScript 或操作 URL 即可使其正确提交。 只要通过 Klaviyo 发送的电子邮件访问托管页面，它就会自动绑定回正确的联系人。</p>
<p><strong>该页面必须是 HTML 格式吗？</strong><br/>此页面必须为 HTML 格式。您可以通过链接或添加包含文件的文件夹来包含其他图像、样式表等。</p>
<p><strong>Klaviyo 可以帮助我构建自定义页面吗？</strong><br/>Klaviyo 目前不提供帮助构建自定义代码的服务，也不提供自定义代码故障排除的支持。这 <strong>托管页面</strong> 该功能旨在为 <a href="https://connect.klaviyo.com/" rel="noopener" target="_blank">开发人员或精通代码的营销人员</a>.</p>
<div class="bs-callout bs-callout-default">
<p>了解有关 Klaviyo 内置同意页面的自定义功能的更多信息 <a href="https://help.klaviyo.com/hc/en-us/articles/115005251848-Getting-started-with-opt-in-related-pages-for-a-list" rel="noopener" target="_blank">同意页面入门</a>.</p>
</div>
<h2 id="h_01J5970D8KN8JEFXY19PXZJJR2">其他资源</h2>
<ul>
<li><a href="https://klaviyo.zendesk.com/hc/en-us/articles/115005079627" rel="noopener" target="_blank">如何自定义列表的取消订阅页面</a></li>
<li><a href="https://klaviyo.zendesk.com/hc/en-us/articles/115005080327" rel="noopener" target="_blank">了解 Klaviyo 中的列表增长工具</a></li>
<li><a href="https://help.klaviyo.com/hc/en-us/articles/360057676272-Understand-custom-hosted-pages-in-Klaviyo" target="_self">了解 Klaviyo 中的自定义托管页面</a></li>
</ul>