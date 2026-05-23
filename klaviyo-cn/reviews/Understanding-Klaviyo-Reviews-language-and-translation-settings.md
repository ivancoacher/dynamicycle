---
id: "28858764961947"
title: "了解 Klaviyo 评论语言和翻译设置"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/28858764961947-Understanding-Klaviyo-Reviews-language-and-translation-settings"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:49:49Z"
language: "zh"
---
## 你将会学到

了解评论小部件的语言、翻译和区域设置。这些设置决定您的小部件和审阅提交表单显示的语言。

## 设置默认小部件语言

默认情况下，所有 Klaviyo 评论内容均为英文。要选择不同的语言：

1. 导航至 Klaviyo 中的****评论****选项卡。
2. 单击****评论设置****。
   ![评论设置选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28858800593179)
3. 选择****常规****。
   ![评论设置的常规部分](https://klaviyo.zendesk.com/hc/article_attachments/28858800595611)
4. 在 **选择语言** 菜单中，选择您的首选语言。

更新 Klaviyo 评论的语言会影响以下所有内容：

- 审核提交页面
- 现场小部件
  - 星级小部件
  - 审查摘要小部件
  - 评论列表小部件
  - 产品评论小部件
  - 精选评论轮播小部件
  - SEO 小部件（以前称为“所有评论小部件”）

您无法使用此方法更新单个小部件的语言设置。所选语言适用于所有小部件，包括您网站上已存在的小部件，并且更改会立即应用。

更新 Klaviyo 评论的语言****不适用于其他 Klaviyo 功能（例如自定义问题、流程、注册表单、同意页面、客户提交评论的内容等）。这些必须手动翻译和编辑。

## 根据每个访问者的浏览器设置设置语言

Klaviyo 可以使用网站访问者的浏览器设置确定其所在国家/地区。要使用此信息自动选择评论小部件语言：

1. 导航至 Klaviyo 中的****评论****选项卡。
2. 单击****评论设置****。
   ![评论设置选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28858800593179)
3. 选择****常规****。
   ![评论设置的常规部分](https://klaviyo.zendesk.com/hc/article_attachments/28858800595611)
4. 打开****根据访客偏好设置语言****开关。
5. 可选：选中选项 **如果可用，请使用访客的送货地点来设置语言。**
6. 选择****保存更改****。

评论小部件只能翻译成默认语言下拉菜单中显示的语言。如果 Klaviyo 检测到站点访问者位于尚不支持的区域，则会使用您的默认语言。

送货地点只能在评论提交页面上使用。如果访问者的送货地点不可用，语言将回退到他们的浏览器设置。如果浏览器设置不可用，语言将默认为您在 Klaviyo Reviews 设置中选择的语言。

## 以编程方式设置语言（需要自定义代码）

此选项仅适用于 Klaviyo Reviews 的自定义编码实现。如果您使用拖放编辑器来安装评论小部件，则此选项不可用。

如果您有权访问开发人员，则可以为评论小部件实施自定义编码的语言选择流程。

所有评论小部件都接受 lang 参数，该参数接受 [2 个字母的 ISO 639 语言代码](https://www.iso.org/iso-639-language-code)。您只需将此参数应用于页面上的 1 个评论小部件。一旦为 1 个小部件设置，所有其他小部件也将使用此参数。

正确实现后，评论代码中的语言参数如下所示：

`<div id="klaviyo-reviews-all" data-id="{{product.id}}" lang="en"></div>`

### **lang** 参数和单页应用程序

该设置是在注入小部件代码时获取的。在单页应用程序中，只有在卸载并重新安装小部件占位符元素时，对 **lang** 参数的实时更改才会生效。

## 其他资源

- [如何根据语言自定义内容](https://klaviyo.zendesk.com/hc/en-us/articles/115005239028)
- [如何自定义评论小部件](https://klaviyo.zendesk.com/hc/en-us/articles/16691401577883)
- [如何自定义评论提交页面](https://klaviyo.zendesk.com/hc/en-us/articles/19481466872859)