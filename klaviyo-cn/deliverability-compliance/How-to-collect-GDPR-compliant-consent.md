---
id: "360003536031"
title: "如何收集符合 GDPR 规定的同意书"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360003536031-How-to-collect-GDPR-compliant-consent"
section: "GDPR and CCPA"
category: "Deliverability & compliance"
category_slug: "deliverability-compliance"
klaviyo_updated: "2026-05-11T11:07:32Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 中如何存储同意书以帮助您遵守 GDPR，以及如何收集 GDPR 以获得合规同意书。 GDPR（通用数据保护条例）是欧盟委员会于 2016 年颁布的一项法律，于 2018 年 5 月 25 日生效。它旨在通过实施有关个人数据的法规来保护所有欧盟公民的隐私，包括当这些公民与欧盟以外的企业打交道时的隐私。有关 GDPR 的更多信息，请[查看我们的博客系列](https://www.klaviyo.com/blog/gdpr-for-ecommerce)。由于 GDPR 要求您在向联系人发送营销电子邮件之前获得知情且自由的同意，因此拥有符合 GDPR 的注册表至关重要。虽然我们仍然建议您联系法律顾问以检查表单上传达的语言，但 Klaviyo 提供了内置的符合 GDPR 的表单作为起点。如果您有想要导入 Klaviyo 的现有列表并且您已经收集了同意，请查看我们的[将同意属性应用于现有列表的指南](https://help.klaviyo.com/hc/en-us/articles/115005078967-Create-and-Add-Contacts-to-a-New-List#upload-and-map-your-data)。本指南中提供的信息旨在提供教育意义，不应被视为法律建议。 Klaviyo 鼓励我们的所有客户和所有电子商务商家寻求法律建议，了解他们具体应如何确保遵守 GDPR。 ## 使用符合 GDPR 的表格

[在您的网站上安装 Klaviyo 注册表单](https://help.klaviyo.com/hc/en-us/articles/360002035871-Install-Klaviyo-Signup-Forms) 后，您可以开始在帐户的****注册表单**** 选项卡中构建表单。单击****从头开始创建****，然后****启用数据保护字段****，以确保默认模板包含符合 GDPR 的语言。 ![带有启用数据保护字段复选框的注册表单创建模式](https://klaviyo.zendesk.com/hc/article_attachments/28716329606683)

您可以编辑此表单的语言或使用复选框添加其他字段以满足您的需求。请记住，GDPR 需要细粒度的同意，这意味着订阅者必须有权选择订阅某些但不是全部类型的营销。例如，订阅者可能希望接收您发送的电子邮件，但不想被您的企业在社交媒体上重定向。使用复选框可以让订阅者选择他们希望从您那里收到的尽可能多或尽可能少的营销类型。订阅者选择的任何值都将作为 **$consent** 属性存储在其个人资料中。同意记录为[列表数据类型](https://help.klaviyo.com/hc/en-us/articles/115005237648-Data-Types#list)，因此可能包含任意数量的值。 ![带有电子邮件地址字段的注册表单](https://klaviyo.zendesk.com/hc/article_attachments/28716329581339)

一旦您的表单样式适合您的需求并包含必要的复选框，您就可以在您的网站上[发布它](https://help.klaviyo.com/hc/en-us/articles/360002049952)，以便您今后按照 GDPR 的要求收集和跟踪同意。不应预先选中复选框，并且需要明确的用户操作。但请注意，无论是否选中该复选框，提交表单的用户都将被订阅。在这种情况下，您应该根据与该复选框关联的[自定义属性](https://help.klaviyo.com/hc/en-us/articles/115005074627)对客户进行[细分](https://help.klaviyo.com/hc/en-us/articles/360040841811)，表明该个人资料已同意发送电子邮件。此外，您可以选择仅向位于欧盟或**不在**欧盟的浏览器显示此表单。为此，请导航至****定位 &**** ****行为 > 定位> 按位置****。在这里，您可以指定在特定位置向浏览器显示/隐藏表单的位置。 Klaviyo 使用 IP 地址确定浏览器的位置。 ![用于注册的行为选项卡，用于根据位置控制可见性设置](https://klaviyo.zendesk.com/hc/article_attachments/28716302267163)

## 使用符合 GDPR 的嵌入式表单

除了弹出窗口或弹出窗口之外，您可能还希望在网站上包含符合 GDPR 的嵌入式表单。为此，请在注册表单生成器中创建符合 GDPR 的嵌入式表单，如上所述。 或者，您可以复制下面提供的代码并[将其安装在您的网站上。](https://help.klaviyo.com/hc/en-us/articles/115005249588-Add-and-Customize-an-Embedded-Signup-Form)请注意，您必须将每个 **LIST\_ID** 值替换为简讯列表的 ID，以确保将联系人添加到列表中。 [详细了解如何查找给定列表的 ID](https://help.klaviyo.com/hc/en-us/articles/115005078647-Find-a-List-ID)。 ````
<form id="email_signup" class="klaviyo_styling klaviyo_gdpr_embed_LIST_ID" action="//manage.kmail-lists.com/subscriptions/subscribe" data-ajax-submit="//manage.kmail-
lists.com/ajax/subscriptions/subscribe" 方法 = "GET"
目标=“_blank”novalidate=“novalidate”>

 <输入类型=“隐藏”名称=“g”值=“LIST_ID”>

 <输入类型=“隐藏”名称=“$字段”值=“$同意”>

 <输入类型=“隐藏”名称=“$list_fields”值=“$同意”>

 <div class="klaviyo_field_group">

 <label for="k_id_email">订阅新闻通讯</label>

 <input class="" type="email" value="" name="email" id="k_id_email" placeholder="您的电子邮件"/>

 <div class="klaviyo_field_group klaviyo_form_actions">

 <div class="klaviyo_helptext">您希望如何收到我们的来信？ （请至少选择一个选项）</div>

 <input type="checkbox" name="$consent" id="consent-email" value="email">

 <label for="consent-email" >电子邮件</label><br>

 <input type="checkbox" name="$consent" id="consent-web" value="web">

 <label for="consent-web">在线广告</label>

 <div class="klaviyo_helptext klaviyo_gdpr_text"> 我们根据我们收集的有关您的信息（例如您的电子邮件地址、一般位置以及购买和网站浏览历史记录），使用电子邮件和有针对性的在线广告向您发送产品和服务更新、促销优惠和其他营销信息。 <br>

<br>

 我们按照隐私政策{插入隐私政策链接}中的规定处理您的个人数据。 您可以随时通过点击我们任何营销电子邮件底部的取消订阅链接或通过发送电子邮件至 {insert customer support email address} 来撤回您的同意或管理您的偏好。</div>

 </div>

 </div>

 </div>

 <div class="klaviyo_messages">

 <div class="success_message" style="display:none;"></div>

 <div class="error_message" style="display:none;"></div>

 </div>
 <div class="klaviyo_form_actions">

 <button type="submit" class="klaviyo_submit_button">订阅</button>
 </div>

</形式>
<样式类型=“文本/css”>

.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID {

 字体系列：“Helvetica Neue”，Arial；

}.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_helptext,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_helptext {

 字体系列：“Helvetica Neue”，Arial；

 顶部填充：10px；
 底部填充：10px；

}
.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_gdpr_text,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_gdpr_text {

 字体大小：14px；

 行高：1.3；

}

.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID 标签，

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID 标签 {

 颜色：#222；

}

.klaviyo_styling .klaviyo_field_group .klaviyo_form_actions {

 文本对齐：左对齐；

 }

.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID 输入[type=checkbox] + 标签，

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID 输入[类型=复选框] + 标签 {

 显示方式：内嵌；

 字体粗细：正常；

 左内边距：5px；

}.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID 输入[类型=文本],

.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID 输入[类型=电子邮件]，

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID 输入[类型=文本]，

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID 输入[类型=电子邮件] {

 边框半径：2px；

}.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_submit_button,

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_submit_button {

 背景颜色：#0064cd；

 边框半径：2px；

}.klaviyo_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_submit_button：悬停，

.klaviyo_condensed_styling.klaviyo_gdpr_embed_LIST_ID .klaviyo_submit_button：悬停{

 背景颜色：#0064cd；

}

</风格>

<script type="text/javascript" src="//www.klaviyo.com/media/js/public/klaviyo_subscribe.js"></script>

<脚本类型=“文本/javascript”>

 KlaviyoSubscribe.attachToForms('#email_signup', {

 hide_form_on_success：true，

 额外属性：{

 $来源：'$嵌入'，

 $method_type: "Klaviyo 形式",

 $method_id: '嵌入',

 $consent_version: '嵌入默认文本'

 }

 });

</脚本>
````

## Klaviyo 中如何存储同意

要查找特定联系人的[同意状态](https://klaviyo.zendesk.com/hc/en-us/articles/360037101072)，请前往他们在 Klaviyo 中的个人资料。 ![通过电子邮件同意的个人资料](https://klaviyo.zendesk.com/hc/article_attachments/28716302288027)

当订阅者通过表单提交同意时，Klaviyo 会在其个人资料中存储几个关键的自定义属性：

- ****表单 ID ****这是唯一的表单 ID，可让您识别某人用于选择加入的特定表单。在 Klaviyo 中创建的每个表单都有一个唯一的 ID，可以在表单的 URL 中以六位字母数字代码的形式找到该 ID。 ![浏览器 URL 中的表单 ID](https://klaviyo.zendesk.com/hc/article_attachments/28716329592987)
- ****方法****这标识订阅者用于选择加入的方法。如果您使用如上所述的 Klaviyo 注册表，则会显示 **Klaviyo 表单**。 - ****表单版本****这标识特定订户看到的表单的迭代。 Klaviyo 保留您创建的每个版本的表单所使用的确切文本和语言的记录，如有必要，您可以向支持人员请求。例如，如果您看到“2”作为同意版本，则意味着订阅者签署了您对表单所做的第二个变体。 - ****时间戳****这是他们提交表格并获得同意时准确记录的时间戳。 ## 如何处理数据或删除请求

根据 GDPR，如果他们要求，您可能需要提供其所有用户数据的联系人。此外，如果联系人请求删除其数据，您可能需要删除某些信息并保留此删除的记录，以证明该请求已得到满足。 请查看我们的[处理 GDPR 请求](https://help.klaviyo.com/hc/en-us/articles/360004217631-How-to-Handle-GDPR-Requests) 指南，了解具体说明。 ## 建立欧盟联系人部分

要隔离您帐户中位于欧盟的一组联系人，请创建满足以下条件的分段：

![欧盟配置文件的细分条件](https://klaviyo.zendesk.com/hc/article_attachments/32061224864539)

## 从流量中过滤欧盟联系人

对于任何非交易流，您需要添加一个过滤器，以仅包含那些同意的人（电子邮件、短信或两者，具体取决于您计划发送的内容）或不在欧盟和英国的人。需要此过滤器的一些常见流程是：

- 浏览放弃
- 赢回
- 追加销售
- 交叉销售
- 产品评论

有关事务性流和非事务性流之间差异的更多信息，请查看[本指南](https://help.klaviyo.com/hc/en-us/articles/360003165732)。此列表的一个例外可能是废弃的购物车电子邮件。许多组织认为，在合法利益的基础上，您仍然可以在没有明确同意营销传播的情况下发送废弃购物车电子邮件。您可以将废弃购物车电子邮件视为与与您的企业完成交易的明确意图相关的通信。另一方面，除非客户事先同意以符合 GDPR 的方式接收您发送的营销电子邮件，否则可能不允许其他触发的电子邮件，例如浏览放弃和赢回。也就是说，合法权益或任何其他法律依据的适用性将取决于具体情况；例如，电子邮件的数量和频率以及自购物车被放弃以来经过的时间。我们强烈建议您就您的营销活动和流程咨询您的法律团队，以确认它们符合适用法律。 ## 压制不同意的欧盟联系人

您的欧盟订阅者群体中任何在 2018 年 5 月 25 日之前未选择重新许可活动的人都应在您的帐户中被禁止，以防止您意外向他们发送电子邮件。为确保您已过滤掉所有提供同意的订阅者，请将以下条件添加到上述 EU 部分。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33882741047067)

[禁止显示此分段](https://help.klaviyo.com/hc/en-us/articles/115005073867-Bulk-Delete-or-Suppress-Contacts-in-Klaviyo#bulk-suppress-contacts-in-klaviyo)，以确保您不会无意中向这些联系人发送电子邮件。如果他们后来决定重新加入，他们可以重新订阅。 ## 最佳实践

一旦您建立了符合 GDPR 的注册框架，请使用分段和流过滤器来确保您仅发送给同意接收营销电子邮件的个人资料。以下条件概述了您要添加的过滤器，以确保您所定位的群组已同意接收电子邮件。 ![同意电子邮件营销的个人资料的条件](https://klaviyo.zendesk.com/hc/article_attachments/32061211318811)

为了保持 GDPR 合规性，您还需要遵守以下最佳实践：

- 在您的所有电子邮件中显示隐私政策、服务条款和 cookie 政策的链接。 - 使用[双重选择加入](https://help.klaviyo.com/hc/en-us/articles/115005251108-Overview-of-the-Double-Opt-In-Process)。 - 了解同意的含义：
  - ****免费给予****。换句话说，您不能误导或强迫某人让您使用他们的信息。必须给予他们合法的选择——如果同意不是服务或交易的组成部分，则您不能基于同意而拒绝提供服务或交易。 - ****具体的****。处理个人数据的同意必须包括有关处理目的和处理类型的详细信息。 -****通知****。知情同意与特定同意的概念密切相关，它仅意味着必须告知个人数据主体其数据将如何使用、其数据的具体用途以及您正在使用的数据处理类型。 -****明确****。更进一步，必须通过明确的语言获得 GDPR 的同意，并通过数据主体的平权行动表明同意。 - ****易于取款****。 尽管在同意的定义中没有预先指出，但 GDPR 第 7 条(https://gdpr-info.eu/art-7-gdpr/) 继续规定同意必须像授予一样容易撤回。 ## 其他资源

- [了解有关 GDPR 的常见问题](https://help.klaviyo.com/hc/en-us/articles/360003211651-Frequently-Asked-Questions-About-GDPR)
- [如何处理 GDPR 和 CCPA 请求](https://help.klaviyo.com/hc/en-us/articles/360004217631-How-to-Handle-GDPR-and-CCPA-Requests)