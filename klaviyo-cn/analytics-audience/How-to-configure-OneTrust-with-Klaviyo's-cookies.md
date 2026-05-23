---
id: "4764571493275"
title: "如何使用 Klaviyo 的 cookie 配置 OneTrust"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4764571493275-How-to-configure-OneTrust-with-Klaviyo-s-cookies"
section: "About cookies in Klaviyo"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: "zh"
---
## 你会学到的

了解如何配置 OneTrust cookie 管理工具（包括其 Auto-BlockingTM 功能和 Cookie Pro 产品）以与 Klaviyo 的跟踪和现场功能配合使用。 Klaviyo.js 是 Klaviyo 的 JavaScript 代码段，可启用网站上的活动跟踪和注册表单。您可以选择通过电子商务集成或将代码粘贴到网站主题中来启用此跟踪。通常，当启用 Klaviyo 的 JavaScript 时，\_\_kla\_id cookie 可以跟踪和识别网站访问者。当未被阻止时，此 cookie 会暂时保存个人身份信息，一旦识别出访问者（例如，单击通过 Klaviyo 发送的电子邮件中的链接），此 cookie 信息就会传递给 Klaviyo。但是，OneTrust 需要额外的设置步骤来确保捕获此信息，然后将其合规地发送到 Klaviyo。在本文中，我们将逐步完成确保 OneTrust 正确捕获访客信息并将其发送到 Klaviyo 的步骤。请注意，您需要按照下面列出的顺序完成本指南中的所有 cookie 设置步骤。 ## 先决条件

我们建议访问我们的 [Klaviyo 网络跟踪指南](https://help.klaviyo.com/hc/en-us/articles/115005076767)，了解有关我们的 cookie 如何以不同方式捕获已知访客信息的更多信息。此外，您必须直接通过[电子商务集成](https://help.klaviyo.com/hc/en-us/categories/115000032731-Ecommerce-Integrations)启用Klaviyo.js，或者[手动](https://developers.klaviyo.com/en/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration#javascript-track-api-for-on-site-metrics)。 ## 配置 Klaviyo 和 OneTrust 的工具

OneTrust 的工具将自动阻止 cookie，除非访问者已通过 OneTrust 明确同意。这些工具可以阻止 cookie，但也会导致 Klaviyo 表单完全停止工作，甚至是不需要跟踪的表单。为了遵守此合规协议并允许某些表单发挥作用，Klaviyo 需要配置 OneTrust，以便在未经同意的情况下不跟踪事件。 Klaviyo 的跟踪包括：

- 如果访问者在网站上处于活动状态，则网站引荐来源网址
- 如果访客查看产品或将产品添加到购物车（如果您已单独启用此功能）

为了使基于同意的跟踪在 OneTrust 和 Klaviyo 之间兼容，以及一些注册表单功能继续工作，您需要在 OneTrust 的 CookiePro 工具中执行以下步骤。 ## 将您的网站添加到 CookiePro

如果您还没有这样做，您需要将您的网站添加到您的 CookiePro 帐户。 1. 登录您的 [CookiePro 帐户](http://app.cookiepro.com/)，然后单击“我的应用程序”下的 ****Cookie 合规性**** 部分。 ![突出显示 Cookie 合规性部分的 CookiePro 仪表板视图](https://klaviyo.zendesk.com/hc/article_attachments/28717390181531)

2. 单击右上角的****添加网站****。 ![CookiePro 仪表板页面右上角的“添加网站”按钮](https://klaviyo.zendesk.com/hc/article_attachments/28717390183579)

3. 从这里，您将看到用于设置和添加网站和扫描详细信息的部分。在前两个字段中填写您的网站 URL 和组织名称。 ![扫描网站模式，其中包含填写网站 URL 和组织信息的字段](https://klaviyo.zendesk.com/hc/article_attachments/28717383884059)

请注意，如果您已经有一个与您的 CookiePro 帐户关联的组织，它将作为一个选项显示在下拉列表中。 4. 在****高级选项****部分下，您可以选择调整或添加扫描设置。 5. 您可以通过更改 **限制扫描** 字段中的数字来调整 CookiePro 将扫描的网站页面数量。默认情况下，CookiePro 将建议扫描前 1,000 页。 ![在扫描设置页面内，可以在字段中输入扫描页码并打开选项](https://klaviyo.zendesk.com/hc/article_attachments/28717390188315)

6. 您还可以将 CookiePro 扫描限制在您网站的某一区域。为此，请打开网站内**限制到此路径****旁边的选项。** 确保您上面的网站 URL 反映了此 URL 路径（例如，retail.com/signups）。 ![在“扫描设置”页面内，切换选项仅扫描网站某一区域内的页面](https://klaviyo.zendesk.com/hc/article_attachments/28717383946907)

7. 最后，如果您希望 CookiePro 扫描某些页面或页面类型，您可以在接下来的几个字段中添加它们。将用逗号分隔的页面 ID 添加到 **使用查询****参数扫描页面** 字段，以按 ID 号扫描页面。您还可以通过在 **要扫描的目标页面** 字段中添加这些 URL 来按 URL 扫描页面。如果您有较长的 URL 或站点地图列表，您可以将其复制并粘贴到 **站点地图 URL** 字段中。这些 URL 将在扫描队列中首先被扫描。 ![在“扫描设置”页面中，用于在要扫描的网站的某些页面或区域上添加附加信息的字段](https://klaviyo.zendesk.com/hc/article_attachments/28717383893403)

8. 完成所有设置后，单击右下角的****扫描和配置****。 ## 配置静态跟踪 Cookie

在下面的部分中，我们将逐步设置您的静态跟踪 cookie，以确保您能够收集第三方 cookie 并将其传递给 Klaviyo。 1. 添加您的网站后，导航至左侧导航栏中的 ****Cookiepedia**** > ****分类****。 2. 通过在上面的字段中搜索或滚动下面的列表来查找 Klaviyo 静态跟踪 \_\_kla\_id cookie。它应该是标记为“持久”的选项，主机名为 **static-tracking.klaviyo.com**。 3. 单击****\_\_kla\_id**** cookie 选项。 ![在“分类”页面内，列表中 __kla_id cookie 的突出显示视图](https://klaviyo.zendesk.com/hc/article_attachments/28717390192411)

4. 进入 **Cookie 详细信息** 页面后，导航至 **分类**** 选项卡。 5. 如果您尚未使用 Klaviyo 和 OneTrust 运行扫描，请确保从 **选择类别** 下拉列表中选择 **定位 Cookie****。确保 **第三方 Cookie** 已填充在 **选择一方** 下拉列表中。 ![在“分类”选项卡上，显示用于选择 Cookie 类别和 Cookie 方的下拉菜单的模式](https://klaviyo.zendesk.com/hc/article_attachments/28717390194715)

6. 完成这些更新后，单击右下角的****保存****。 7. 在同一区域中，导航至****Source**** 选项卡。您应该会看到您的网站 URL 出现在列表中，如下例所示。 ![在“来源”页面内，显示网站 URL 的视图](https://klaviyo.zendesk.com/hc/article_attachments/28717383898267)

8. 单击您的****网站 URL****。 9. 将出现一个带有新 URL 的下拉菜单；单击右侧的铅笔图标。 ![网站 URL 右侧铅笔编辑图标的突出显示视图](https://klaviyo.zendesk.com/hc/article_attachments/28717383900315)

10. 在模式中，删除当前 URL 并将其替换为：**https://static-tracking.klaviyo.com**。 11. 更新 URL 后，单击****确认****。 ![资源 URL 的模式视图，右下角带有确认按钮](https://klaviyo.zendesk.com/hc/article_attachments/28717383943067)

12. 要确认 Klaviyo cookie 已更新，请导航至左侧导航栏中的****Cookpedia********> 分类****。 1

3. 单击 ****Cookies**** 选项卡。 14. 从这里开始，您的 \_\_kla\_id cookie 应在 **Domain Category Overrides** 和 **Domains** 列下显示“1”。 ![在确认屏幕上，列表视图显示您的 __kla_id cookie，其中包含域类别覆盖和域作为数字](https://klaviyo.zendesk.com/hc/article_attachments/28717390203035)

## 配置 Static.Klaviyo Cookie

在下面的部分中，我们将逐步设置您的 static.Klaviyo cookie，以确保您能够收集第三方 cookie 并将其传递给 Klaviyo。 1. 在左侧导航栏中导航至 ****Cookiepedia > 分类****。 2. 通过在上面的字段中搜索或滚动下面的列表来查找 static.Klaviyo \_\_kla\_id cookie。它应该是标记为“持久”的选项，主机名为 **static.klaviyo.com**。 3. 单击****\_\_kla\_id**** cookie 选项。 ![在“分类”页面上，__kla_id cookie 选项在列表视图中突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28717383910299)

4. 进入 **Cookie 详细信息** 页面后，导航至 **分类**** 选项卡。 5. 从 **选择类别** 下拉列表中选择 **定位 Cookie****。确保 **第三方 Cookie** 已填充在 **选择一方** 下拉列表中。 ![在“分类”选项卡上，显示用于选择 Cookie 类别和 Cookie 方的下拉菜单的模式](https://klaviyo.zendesk.com/hc/article_attachments/28717390194715)

6. 完成这些更新后，单击右下角的****保存****。 7. 在同一区域中，导航至****Source**** 选项卡。您应该会看到您的网站 URL 显示在下面的列表中。 ![您网站 URL 的模式视图](https://klaviyo.zendesk.com/hc/article_attachments/28717383898267)

8. 单击您的****网站 URL****。 9. 将出现一个带有新 URL 的下拉菜单；单击出现在右侧的铅笔图标。 ![网站 URL 右侧铅笔编辑图标的突出显示视图](https://klaviyo.zendesk.com/hc/article_attachments/28717383900315)

10. 在模式中删除当前 URL 并替换为：**https://static-tracking.klaviyo.com**[.](https://static-tracking.klaviyo.com.)

11. 更新 URL 后，单击****确认****。 ![右下角带有确认按钮的网站 URL 模式](https://klaviyo.zendesk.com/hc/article_attachments/28717383943067)

12. 要确认 Klaviyo cookie 已更新，请导航至左侧导航栏中的 ****Cookiepedia > 分类****。 13. 从这里开始，您的 \_\_kla\_id cookie 应在 **Domain Category Overrides** 和 **Domains** 列下显示“1”。 ![在确认屏幕上，列表视图显示您的 __kla_id cookie，其中包含域类别覆盖和域作为数字](https://klaviyo.zendesk.com/hc/article_attachments/28717390203035)

## 配置您网站的第一方 Cookie

在下面的部分中，我们将介绍如何直接设置您的网站或第一方 cookie 以捕获电子商务网站上的事件。 1. 在左侧导航栏中导航至 ****Cookiepedia > 分类****。 2. 通过在上面的字段中搜索或滚动下面的列表来查找您网站特定的 \_\_kla\_id cookie。它应该是标记为“持久”的选项，并以您的网站 URL 作为主机名。 3. 单击****\_\_kla\_id**** cookie 选项。 ![在分类页面上，您的 __kla_id cookie 在列表视图中突出显示](https://klaviyo.zendesk.com/hc/article_attachments/28717383916315)

4. 进入 **Cookie 详细信息** 页面后，导航至 **分类**** 选项卡。 5. 从 **选择类别** 下拉列表中选择 **定位 Cookie****。确保**第一方 Cookie** 已填充在 **选择一方** 下拉列表中。 ![在“分类”选项卡上，显示用于选择 Cookie 类别和 Cookie 方的下拉菜单的模式](https://klaviyo.zendesk.com/hc/article_attachments/28717390209819)

6. 完成这些更新后，单击右下角的****保存****。 7. 在同一区域中，导航至****Source**** 选项卡。您应该会看到您的网站 URL 显示在下面的列表中。 ![您网站 URL 的模式视图](https://klaviyo.zendesk.com/hc/article_attachments/28717383898267)

8. 单击您的****网站 URL****。 9. 将出现一个带有新 URL 的下拉菜单；单击出现在右侧的铅笔图标。 ![网站 URL 右侧铅笔编辑图标的突出显示视图](https://klaviyo.zendesk.com/hc/article_attachments/28717383900315)

10. 在模式中删除当前 URL 并替换为：**https://static-tracking.klaviyo.com**。 11. 更新 URL 后，单击****确认****。 ![显示您网站 URL 的模式，右下角带有确认按钮](https://klaviyo.zendesk.com/hc/article_attachments/28717383943067)

## 预览更新的 Cookie

1. 导航至左侧导航栏中的****脚本****。 2. 在“脚本”页面上，单击下面显示的****网站 URL****。 ![在脚本页面上，您的网站 URL 将出现在下面的列表中以供单击](https://klaviyo.zendesk.com/hc/article_attachments/28717383922971)

3. 然后，单击右上角的****发布作品****。 ![单击脚本页面右上角的“发布作品”按钮的视图](https://klaviyo.zendesk.com/hc/article_attachments/28717383924507)

4. 在出现的右侧边栏中，单击****确认****。 5. 进入 **Review** 选项卡后，向下滚动并单击 ****Continue****。 6. 最后，在**确认****并发布**选项卡上，单击****发布测试和预览****。您的预览可能需要几秒钟的时间来加载，但一旦准备好，您将看到下面出现一个绿色的勾号。 ![](https://fast.wistia.com/embed/medias/2b9o3tsibi/swatch)

7. 出现此成功消息后，单击下面的****确认****。 ## 发布您更新的 Cookie

在发布 Cookie 之前，请务必注意，生产脚本最多可能需要四个小时才能在您的网站上生效。按照以下说明操作后，请等待四个小时才能看到这些更新。 1. 导航至左侧导航栏中的****网站****。 2. 在 **网站** 页面上，从下面的列表中单击您的****网站 URL****。 ![在网站页面上，您的网站网址将出现在下面的列表中以供单击](https://klaviyo.zendesk.com/hc/article_attachments/28717390222491)

3. 在此处，单击右上角的****发布****。 4. 将出现一个侧边栏模式，确认您要发布的版本。点击右下角****确认****。 ![右侧边栏中将出现一个模式，用于发布您的网站 cookie，并在右下角带有确认按钮](https://klaviyo.zendesk.com/hc/article_attachments/28717390226715)

5. 在同一模式中，您将进入 **审阅和发布** 屏幕。单击****启用自动阻止 Cookie**** 上的切换按钮。您可以在[指南](https://community.cookiepro.com/s/article/UUID-5b03e81d-8b3b-5da8-eed5-b3b015730f3c?language=en_US)中阅读有关 CookiePro 自动阻止功能的更多信息。 ![在审阅和发布屏幕上，突出显示的区域可打开自动阻止 Cookie](https://klaviyo.zendesk.com/hc/article_attachments/28717383934235)

6、点击右下角****发布****。 7. 将出现一个弹出窗口，其中包含您的制作脚本。单击****复制脚本****。 ![显示要复制并粘贴到网站的生产脚本的弹出窗口](https://klaviyo.zendesk.com/hc/article_attachments/28717390232603)

8. 将这些脚本放入您的电子商务网站的 html 中。在 CookiePro 的分步 [指南](https://community.cookiepro.com/s/article/UUID-7478d3b4-18eb-3ac0-a6fd-fb7ebff9f8dc?language=en_US) 中了解有关将这些脚本放入电子商务网站的更多信息。 ## 结果

您已成功设置 OneTrust cookie 跟踪软件，以确保捕获您的访客信息，然后将其合规地发送至 Klaviyo。