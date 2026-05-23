---
id: "4418052317339"
title: "单击按钮时如何触发注册表单出现"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4418052317339-How-to-trigger-a-sign-up-form-to-appear-when-a-button-is-clicked"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:55:01Z"
language: "zh"
---
## 你将会学到

了解当访问者单击某个按钮时如何触发注册表单显示在您的网站上。本指南将引导您调整表单以在自定义触发器上显示、创建新按钮并将其添加到您的网站，以及将简短的代码片段粘贴到网站的 HTML 中，以便单击按钮触发注册表单。如果您是开发人员并且想要为注册表单编写触发器，请访问我们的开发人员资源，了解如何[自定义触发弹出或弹出表单](https://developers.klaviyo.com/en/docs/how_to_custom_trigger_a_popup_or_flyout_form)。由于粘贴此代码需要访问您网站的 HTML 和电子商务平台，因此我们的支持团队无法提供实际帮助。如果您的团队中没有开发人员并且不方便自己添加代码，[考虑向 Klaviyo 合作伙伴寻求帮助](https://klaviyo.partnerpage.io/)。 ## 创建一个新按钮

![](https://fast.wistia.com/embed/medias/gssdg2muww/swatch)

首先，在您的网站上创建一个新按钮，单击该按钮将触发注册表单出现。在将按钮添加到您的网站之前，您需要确保您的注册表单在 Klaviyo 中设置正确。为此：

1. 单击按钮时将显示[创建新注册表单](https://help.klaviyo.com/hc/en-us/articles/360026474752-Guide-to-Creating-a-Signup-Form)，或选择您已创建的表单。 2. 在****样式****选项卡中，您的**表单类型**应设置为****弹出式、********浮出式或整页****。单击按钮时无法触发嵌入表单。 3. 在****定位和行为****选项卡中，选择**计时下的****仅在自定义触发器上显示****。
   ![表单编辑器中“目标和行为”选项卡的“计时”部分显示了“在选定的自定义触发器上显示”选项。](https://klaviyo.zendesk.com/hc/article_attachments/28705664743067)
4. 当您对表单的设计和内容感到满意时，单击****发布。****
5. 接下来，打开表单编辑器并选择以下设置
6. 复制以下代码：

   ````
   <button class="klaviyo_form_trigger">点击此处</button>
   ````
7. 将代码粘贴到网站上您希望显示该按钮的任何页面的 HTML 中。此按钮将使用站点模板中的默认样式。如果您想进一步自定义按钮的外观，请咨询您的开发人员或 [Klaviyo 合作伙伴](https://connect.klaviyo.com/)。请注意，如果您向网站添加多个按钮，每个按钮都会触发不同的注册表单，则需要使用唯一的名称来对每个按钮进行分类（例如，klaviyo\_form\_trigger1、klaviyo\_form\_trigger2）。 ## 设置按钮来触发您的注册表单

![](https://fast.wistia.com/embed/medias/l2a8gcpnen/swatch)

现在您已经向网站添加了一个新按钮，接下来您需要设置触发器，以便在单击该按钮时显示您的注册表单。通过向您的网站添加一个小的自定义 JavaScript 片段来设置触发器：

1. 复制下面的代码片段：

   ````
   <脚本类型=“文本/javascript”>
   	document.querySelector('.klaviyo_form_trigger').addEventListener('click', function (){
   		窗口._klOnsite = 窗口._klOnsite || []；
   		window._klOnsite.push(['openForm', 'FORM_ID']);
   	});
   </脚本>
   ````
2. 将代码片段直接粘贴到您在上一部分中添加到站点的按钮代码下方。 3. 在您刚刚粘贴的代码片段中，将 FORM\_ID 替换为您的注册表单 ID。 - 要查找表单 ID，请导航回 Klaviyo 并打开注册表单的表单编辑器。复制 URL 末尾的 6 位代码以添加到您的代码段中；这是表单 ID。！[表单编辑器中示例注册表单的 URL，末尾突出显示六位数代码以显示唯一的表单 ID。](https://klaviyo.zendesk.com/hc/article_attachments/28705637889691)
4. 完成的代码应包括新按钮代码以及带有您唯一表单 ID 的注册表单触发器。确保将其粘贴到添加按钮代码的每个页面上。 - 以下是 Shopify 页面编辑器中完整代码的示例：！[在 Shopify 页面编辑器中显示按钮代码和表单触发器的完整代码示例。](https://klaviyo.zendesk.com/hc/article_attachments/28705664741275)

   如果您在最后一步中调整了按钮的类（即，您用其他文本替换了 klaviyo\_form\_trigger 或添加了数字），请确保使用您使用的文本更新此代码。 5. 保存您的更改。 ## 测试你的按钮

保存对站点代码的所有更改后，访问您的站点并单击新按钮。当您这样做时，将出现注册表单。有麻烦吗？前往 Klaviyo 的[社区论坛](https://community.klaviyo.com/) 寻求其他 Klaviyo 用户的指导。