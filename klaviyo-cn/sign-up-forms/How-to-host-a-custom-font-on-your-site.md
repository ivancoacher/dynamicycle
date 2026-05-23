---
id: "360047999812"
title: "如何在您的网站上托管自定义字体"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360047999812-How-to-host-a-custom-font-on-your-site"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-05-11T10:59:25Z"
language: "zh"
---
## 你将会学到

了解如何将字体（即非 Google 或 Adobe 托管的字体）上传到您的电子商务网站，以导入到您的 Klaviyo 注册表单中。如果您想在注册表单中使用导入的字体，有 2 个选项：

1. 使用您网站上托管的公共字体。
2. 公开托管您自己的字体，并使用 URL 将您的字体导入您的注册表单中。

本文将引导您了解如何将自定义字体上传到电子商务网站以在表单中使用，而不是在电子邮件模板中使用。有关向电子邮件模板添加自定义字体的信息，请参阅我们关于[电子邮件模板中的自定义字体]的文章(https://klaviyo.zendesk.com/hc/en-us/articles/115005256008)。

## 使用您网站的字体

首先，您可以使用站点上的公共 URL 在 Klaviyo 中上传字体。

请注意，Shopify 商店不支持此托管自定义字体的方法。

1. 前往您的网站。
2. 右键单击​​选择****检查**** 或****检查元素****，具体取决于您的互联网浏览器。
3. 从那里导航至****网络**** > ****字体。****
4. 刷新页面。
   您将看到列出的所有字体。如果字体名称未填充，而是看到一串数字和字母，请选择预览选项卡来决定要在注册表单中使用哪种字体。
5. 在**名称**下，单击要导入的字体。
6. 选择****标题选项卡。****
7. 复制您要使用的字体的 URL。
8. 在 Klaviyo 中，导航至****内容 > 图像和品牌 > 字体。****
9. 选择****导入字体****。
10. 通过将 URL [粘贴 URL](https://help.klaviyo.com/hc/en-us/articles/360047955672#h_01HK5YMHFNNG6988YPM8E5FRY1) 上传到 **源地址**。

## 上传自托管字体

首先，如果该字体尚未在线公开托管，请将您想要使用的字体下载到您的计算机上。请注意，文件必须采用 WOFF、WOFF2、TTF、EOT 或 SVG 格式才能在 Klaviyo 中使用。另外，从互联网下载字体文件时要小心，因为它们可能包含恶意软件。从那里：

1. 将字体上传到您的电子商务网站的资产。您需要在您网站的代码中执行此操作。
2. 保存。

有关更多信息，请前往相应的电子商务平台帮助中心，了解有关如何将资产添加到您的网站的更多信息

- [Shopify](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads#upload-a-file-on-the-files-page)
- [BigCommerce](https://support.bigcommerce.com/s/article/How-do-I-add-and-link-to-a-file-in-my-store)

获得 URL 后，导航回 Klaviyo 并选择****内容 > 图像和品牌 > 字体****。从这里，单击****导入****字体选项卡并[导入您的字体](https://help.klaviyo.com/hc/en-us/articles/360047955672#h_01HK5YMHFNNG6988YPM8E5FRY1)。

![Klaviyo 中图像和品牌选项卡的导入字体菜单。](https://klaviyo.zendesk.com/hc/article_attachments/28713332394139)

## 受 Klaviyo.js 影响的网站字体

Klaviyo [主动现场跟踪](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAABB803T7AGQ6G3HM6B) (Klaviyo.js)，必须手动安装或通过电子商务集成安装，才能在您的网站上发布 Klaviyo 注册表单。如果您只加载了一些字体变体，Klaviyo.js 会在将其注入您的网站时加载库中的其余变体。因此，在此过程中可能会对您网站上的字体进行轻微编辑，例如网站标题粗细的更改。

有 2 个选项可用于解决 Klaviyo.js 对字体所做的任何更改。您可以：

- 从 Klaviyo 字体库中删除相关字体。
- 更新网站标题上的 CSS，以便在 Klaviyo.js 加载其他变体时它不会被覆盖。

  由于此选项需要深入的 CSS 知识，因此您可能需要开发人员的帮助。 Klaviyo 无法提供调整网站 CSS 的帮助，但我们确实拥有庞大的[合作伙伴网络](https://connect.klaviyo.com/)。

## 其他资源

- [如何在注册表单中使用自定义字体](https://klaviyo.zendesk.com/hc/en-us/articles/360047955672)
- 课程：[使用注册表单创建有效的获取策略](https://academy.klaviyo.com/creating-an- effective-acquisition-strategy-using-signup-forms)
- [如何在电子邮件模板中添加自定义字体](https://help.klaviyo.com/hc/en-us/articles/115005256008)