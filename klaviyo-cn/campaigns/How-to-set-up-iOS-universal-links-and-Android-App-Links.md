---
id: "41701832186523"
title: "如何设置iOS通用链接和Android应用程序链接"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41701832186523-How-to-set-up-iOS-universal-links-and-Android-App-Links"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:50:40Z"
language: "zh"
---
## ****关于通用链接和应用程序链接****

通用链接（适用于 iOS）和应用程序链接（适用于 Android）将您的客户引导至您的移动应用程序中的内容，或者如果未安装该应用程序，则引导至您网站上的相同内容。在电子邮件和短信中使用这些链接可以让您在所有营销渠道中使用一致的 URL，同时为您的客户（无论他们使用什么设备）打造无缝体验。它与传统的深度链接类似，但具有附加功能。 Klaviyo 中的通用链接和应用程序链接与点击跟踪和 UTM 跟踪完全兼容。 ## ****它是如何工作的****

配置后，当客户通过移动设备单击您的一封消息中的链接时，Klaviyo 能够正确识别并将他们路由到您的移动应用程序中的正确位置（如果他们的设备上安装了该应用程序）。如果未安装该应用程序，客户将照常访问您的网站。在不支持此功能的平台中，点击跟踪会干扰通用链接和应用程序链接。这是因为点击跟踪使用重定向来捕获点击事件，这会阻止应用程序直接打开。您的移动应用程序必须至少使用 iOS SDK 5.1.0 版、Android SDK 4.1.0 版或 React Native SDK 2.1.0 版才能在电子邮件和短信中设置通用链接。 ## ****开始之前****

在 Klaviyo 中设置通用链接和/或应用程序链接之前，您需要具备以下条件：

- 您的移动应用程序必须至少使用 iOS SDK 5.1.0 版、Android SDK 4.1.0 版或 React Native SDK 2.1.0 版才能在电子邮件和短信中设置通用链接。 - 对于****电子邮件****中的链接，****专用点击跟踪域****。有关设置说明，请参阅我们关于[如何设置专用点击跟踪域](https://help.klaviyo.com/hc/en-us/articles/360001550572) 的文章。 - 对于****短信****中的链接，****品牌的自定义链接****。有关设置说明，请参阅我们关于[如何为 SMS 创建品牌短链接](https://help.klaviyo.com/hc/en-us/articles/17649597637147) 的文章。 - ****Klaviyo SDK 安装在您的移动应用程序上。 - 在您的网站域上托管的“apple-app-site-association”****(AASA) 文件****（适用于 iOS）和/或“assetlinks.json”**** 文件****（适用于 Android）。 Apple 和 Google 分别需要这些文件来将您的网站与移动应用程序关联起来。 - 您的****移动应用程序必须配置为支持通用链接和/或应用程序链接****。 - 有关配置 iOS 和设置“apple-app-site-association”(AASA) 文件的更多信息，请参阅 [Apple 关于支持关联域的开发人员文档](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content/)。 - 有关配置 Android 和设置 `assetlinks.json` 文件的更多信息，请参阅 [Android 关于添加应用程序链接的开发人员文档](https://developer.android.com/training/app-links)。 ## ****如何在 Klaviyo 中设置通用链接和应用程序链接****

1. 导航至您的 Klaviyo 帐户中的****设置****。 2. 单击****推送通知****。 3. 选择****通用和应用程序链接****选项卡。 4. 在卡中，单击****设置****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/42123623612955)
5. 为您要启用的渠道（电子邮件和/或短信）选择点击跟踪域。 6. 输入您的目标域。这是您计划在邮件正文中使用的网站域。 7. 上传“apple-app-site-association”(AASA) 文件和/或“assetlinks.json”文件。 - 如果您同时拥有 iOS 和 Android 应用程序，则需要上传这两个文件。 - 如果您只有iOS应用程序，则只需上传AASA文件。 - 如果您只有 Android 应用程序，则需要上传这两个文件。 8. 单击****保存****。 9. 返回设置页面。选择应在您的应用程序上打开的点击跟踪域并****单击“启用”****

![](https://klaviyo.zendesk.com/hc/article_attachments/42123631357339)

## ****通用覆盖****

在某些情况下，您可能希望指定在应用程序中打开的特定链接，即使它与 AASA 或“assetlinks.json”文件中定义的路径不匹配。您可以通过将 `universal="true"` 属性添加到链接的 HTML 来完成此操作。 例如：<a href="trk.example.com" universal="true">链接到您的应用程序！</a>

或者，您可以通过将 `universal="false"` 属性添加到链接的 HTML 来执行相反的操作。注意：此功能仅适用于电子邮件。 ## ****测试您的设置****

要测试您的通用链接和应用链接，请创建新的营销活动或流程消息，并包含指向您网站上已配置为深层链接的页面的链接。向安装了您的应用的设备发送一条消息，向未安装您的应用的设备发送另一条消息。 - 在安装了您的应用程序的设备上，链接应直接在您的应用程序中打开。 - 在未安装应用程序的设备上，链接应在设备的网络浏览器中打开。注意：预览消息不使用点击跟踪，因此可能无法准确反映链接。为了正确测试，请勿使用预览消息。 ## ****查看您的 Klaviyo 托管的通用链接和应用程序链接文件****

完成设置后，Klaviyo 将托管您的配置文件版本。要查看它们，请在浏览器中导航到以下 URL，并将“<YOUR_TRACKING_DOMAIN>”替换为您自己的域：

- ****iOS:**** `https://<YOUR_TRACKING_DOMAIN>/.well-known/apple-app-site-association`
- ****Android:**** `https://<YOUR_TRACKING_DOMAIN>/.well-known/assetlinks.json`

## ****常见问题解答****

****我需要有专用的点击跟踪域吗？**** 需要专用的点击跟踪域才能使用电子邮件的通用链接和应用程序链接。对于短信，您需要设置品牌自定义短链接。 ****如果我有多个 Klaviyo 帐户共享一个跟踪域，会发生什么？**** 如果多个帐户共享一个跟踪域，则对域配置的更改将影响所有这些帐户。