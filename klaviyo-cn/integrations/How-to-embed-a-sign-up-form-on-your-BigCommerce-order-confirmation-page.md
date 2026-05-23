---
id: "360031724251"
title: "如何在 BigCommerce 订单确认页面上嵌入注册表单"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360031724251-How-to-embed-a-sign-up-form-on-your-BigCommerce-order-confirmation-page"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:51Z"
language: "zh"
---
## 你将会学到

了解如何在 BigCommerce 确认页面上嵌入注册表单，以便在客户完成结账流程后收集更多信息。这些最近的客户已经对您的品牌感兴趣，因此确认提供了进一步与他们互动的绝佳机会。 ## 开始之前

确保您已[与 BigCommerce 集成](https://help.klaviyo.com/hc/en-us/articles/115005082547) 并检查设置 **自动添加 Klaviyo 现场 JavaScript**。 ## 构建你的表单

您可以创建注册表单并将其嵌入到确认页面中，以便在客户结帐后询问相关问题。例如，您可以提出问题以详细了解客户使用您产品的频率，或者他们可能有兴趣购买哪些潜在新产品。要构建您的注册表单：

1. 在 Klaviyo 中，导航至****注册表单 > 创建注册表单 > 从头开始构建****。 2. 在出现的菜单中，为您的表单命名并选择供新订阅者提交的列表。 3. 选择****嵌入**** 作为表单类型。 ![嵌入表单.jpg](https://klaviyo.zendesk.com/hc/article_attachments/34409763651355)
4. 点击****保存并设计****。 5. 这将带您进入表单编辑器，您可以在其中编辑以下样式：
   - **样式**：编辑表单的外观以匹配您的品牌，例如表单或输入字段样式和字体类型。您还可以通过单击任何文本并将默认语言替换为您自己的语言来编辑它。 - **添加块**：您可以在此处向表单添加内容以收集信息，例如问题的文本框或生日的日期字段。确保为您添加的每个字段设置一个[配置文件属性](https://help.klaviyo.com/hc/en-us/articles/115005074627-Profile-properties-reference)，并且不要让客户因太多问题而不知所措。 - **定位和行为**：选择是否希望表单显示在桌面、移动设备或两者上。将您的表单设置为****向所有访问者显示****或****不向现有的 Klaviyo 个人资料显示。****
6. 在菜单栏中，选择****成功****以编辑某人提交您的表单后显示的页面。 7. 当您对表单的设计感到满意时，单击****发布****。 8. 从出现的模式中，复制嵌入代码，以便准备粘贴。 ![](https://klaviyo.zendesk.com/hc/article_attachments/34409763654299)
9. 单击****发布****。在您将嵌入代码粘贴到网站代码中之前，您的表单不会出现在您的网站上。验证该列表的[选择加入设置](https://help.klaviyo.com/hc/en-us/articles/115005251108-The-Double-Opt-In-Process)，以便客户体验无缝。如果列表是双重选择加入的，您将需要编辑确认页面。默认情况下，所有 Klaviyo 列表都设置为双重选择加入。 ## 将嵌入添加到您的 BigCommerce 网站

1. 导航到您的 BigCommerce 管理员。 2. 转至****店面 > 脚本管理器****，然后单击****创建脚本。****
3. 命名脚本并使用以下内容进行配置：
   - 地点：头部
   - 描述（可选）：描述脚本的用途
   - 添加脚本的页面：订单确认
   - 脚本类型：脚本
     ![BigCommerce 中的“创建脚本”页面，您可以在其中填写位置、描述、将添加脚本的页面以及脚本类型。](https://klaviyo.zendesk.com/hc/article_attachments/28704485135131)
4. 删除脚本内容并粘贴以下代码以将 klaviyo.js 添加到您的确认页面。请注意，即使您之前在网站上安装了 klaviyo.js，您也需要执行此操作：

   ````
     <script src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js" async=""></script>
     <脚本>
        document.addEventListener("DOMContentLoaded", function() {
          var elem = document.createElement('div');
        elem.className = 'klaviyo-form-FORM_ID'
        document.body.appendChild(elem);
        });</脚本>
   ````
5. 在上面的代码片段中，将“PUBLIC_API_KEY”替换为[您网站的公共 API 密钥](https://klaviyo.zendesk.com/hc/en-us/articles/115005062267)
6. 在上面的代码片段中，将“FORM_ID”替换为您的表单 ID。要查找您的表单 ID，请导航至您的 Klaviyo 帐户中的嵌入表单。表单 ID 是 URL 末尾的 6 个字母代码。 ![Confirms3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28704477015963)
7. 填写脚本的所有详细信息后，点击****保存****。现在，有人下订单后，您的嵌入表单将显示在页面底部。根据您的主题，您可能需要在 **样式** 部分中编辑表单的边框、填充或大小，以确保其与订单确认页面的外观和风格相匹配；发布您所做的任何更改以查看它们的反映。 ## 后续步骤

开始使用嵌入表单收集回复后，每次提交都将作为[自定义属性](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile#how-to-use-custom-properties5)存储在客户的个人资料中，可在段、流程和电子邮件模板中使用。根据回复，您可以对[购买后](https://help.klaviyo.com/hc/en-us/articles/360028872611-Guide-to-Creating-a-Post-Purchase-Flow)体验进行分支。您可能还想根据此数据对您的[欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172-Guide-to-Creating-a-Welcome-Series)进行分支或[创建相关分段](https://help.klaviyo.com/hc/en-us/articles/115005237908-Guide-to-Creating-Segments#segment-conditions2) 将营销活动发送到。例如，假设我们决定发布一款新的睫毛膏。由于我们在此嵌入式表单上收集产品兴趣数据，因此我们可以通知任何在产品发布中告诉我们他们对睫毛膏感兴趣的人。 ## 其他资源

- [注册表单入门](https://help.klaviyo.com/hc/en-us/articles/360026474752)
- [如何在您的网站上嵌入注册表单](https://help.klaviyo.com/hc/en-us/articles/360006897412)