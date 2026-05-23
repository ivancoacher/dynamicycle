---
id: "360034666712"
title: "了解 Klaviyo 中的 cookie"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360034666712-Understanding-cookies-in-Klaviyo"
section: "About cookies in Klaviyo"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:45Z"
language: "zh"
---
## 你将会学到

详细了解 Klaviyo 如何使用 cookie 作为我们网络跟踪的一部分来收集信息并帮助提高转化率和电子邮件性能。本文解释了我们使用的具体 cookie 及其用途，以便您了解如何跟踪客户。此信息可帮助您了解 Klaviyo 如何收集数据，以及这可能如何影响客户隐私和合规法律。为了[保持 GDPR 合规性](https://help.klaviyo.com/hc/en-us/articles/360003211651)，您应该在所有电子邮件中显示隐私政策、服务条款和 Cookie 政策的链接。 ## Klaviyo 跟踪 cookie

当 Klaviyo 的 JavaScript 启用时，“__kla_id”cookie 可以通过自动生成的 ID 跟踪和识别网站访问者。该 cookie 可以暂时保存个人身份信息。一旦识别出访问者，cookie 就可以将他们的数据传递到 Klaviyo。访客在以下情况下即可被识别：

- 填写 Klaviyo 注册表
- 单击 Klaviyo 电子邮件或短信中的链接。 SMS 点击和转化跟踪取决于是否有链接，并且该链接必须使用 Klaviyo 链接缩短程序。设置短信时，务必选中“****自动缩短链接****”选项，以确保您使用默认跟踪。 ## Cookie 识别时间、扩展 ID 和 Shopify 品牌现场跟踪

### 默认时间

当访问者被识别时（例如，通过填写表格或单击电子邮件链接），`__kla_id` cookie 将被设置为持续最多 2 年。下面详细了解[扩展此临时 cookie 以更长时间地保存 PII](https://help.klaviyo.com/hc/en-us/articles/32053410094619)。在 Safari 桌面和 iOS 移动网络浏览器上，Apple 的智能跟踪预防 (ITP) 可能会将 cookie 有效期限制为 7 天，而不是持续整整 2 年。活动电子邮件/短信链接使用“_kx”参数，该参数被存储
在会话存储中，并且不受 ITP cookie 限制。 ### 扩展ID

如果您选择开启扩展 ID，强烈建议您向客户重新发出 Cookie 通知，并告知他们 Klaviyo 将使用第一方 Cookie 来重新发出 Klaviyo cookie。这将允许 Klaviyo 和您的企业在用户的浏览器 cookie 过期后重新识别用户。此外，建议您更新隐私声明，以确保您的客户了解此重新识别过程。对于某些桌面浏览器（例如 Safari）和移动操作系统（iOS），Apple 的 ITP 可能会将跟踪 cookie 的有效期限制为 7 天。如果您的 Klaviyo cookie 很快过期（例如 24 小时后），您可能会错过有价值的跟踪事件，例如用户何时访问您的网站或查看产品。购物者也可能不会收到在这些浏览重新访问时触发的自动流程或活动。如果您想在 Klaviyo cookie 过期或删除后跟踪用户未来的访问，您可以打开扩展 ID 选项。扩展 ID 是一项第一方身份图功能，允许您跟踪此 cookie 并将其保留长达 1 年。所有 Klaviyo 计划均提供扩展 ID。 ### 扩展 ID 如何工作？扩展 ID 的工作原理是读取存储在用户浏览器中的通用确定性标识符（即精确的唯一标识符）。这些持久的第一方唯一标识符（即 cookie）是由其他平台创建的，用于分析等用例。当用户返回网站并发出新的 Klaviyo cookie 时，扩展 ID 会读取浏览器中的第一方标识符信息并恢复之前的 Klaviyo 身份 cookie，以便重新识别用户。如果没有匹配且无法识别用户，Klaviyo 会将第一方唯一标识符和唯一 Klaviyo 标识符之间的关联存储在其 cookie 中，以便将来可能重新识别。对于其他平台或解决方案，您将需要设置自定义标识符。扩展 ID 是一种更持久的用户跟踪形式，普通第三方 cookie 跟踪所获得的用户同意可能不涵盖该形式。它可能需要您向客户解释扩展 ID 使用第一方 cookie 标识符，并且即使以前的 Klaviyo cookie 已被清除，也可能会重新识别他们。在使用扩展 ID 之前，您可能还需要征求每次客户访问的特定用户同意。 您还可能希望查看您的隐私政策和同意措辞，以确保您的客户得到适当的通知，并同意此重新识别过程。需要注意的是，虽然扩展 ID 可以帮助更长时间地识别购物者，但它不会根据其他网站的购物者信息自动创建新的个人资料。购物者需要已经拥有 Klaviyo 配置文件以获取扩展 ID，以便重新识别他们并更新他们的 Klaviyo 身份 cookie。了解如何[打开并设置扩展 ID](https://help.klaviyo.com/hc/en-us/articles/32053410094619)。 ### Shopify 品牌现场跟踪

除了作为[标准网络跟踪](https://help.klaviyo.com/hc/en-us/articles/115005076767)一部分的 Klaviyo 识别方法之外，如果客户提交信息，Shopify 的现场跟踪像素还可以在结账时进行识别。为了在结帐期间捕获访问者的身份，他们必须完成以下 [Shopify 事件](https://shopify.dev/docs/api/web-pixels-api/standard-events) 之一：

- 结帐\_已完成
- 付款\_信息\_已提交
- 结帐\_contact\_info\_subscribed
- 结帐\_shipping\_info\_已提交

这将导致匿名活动同步到关联的个人资料，即使他们从未提交过 Klaviyo 表单或单击过 Klaviyo 电子邮件或短信中的链接。为了在结帐时捕获访客的身份，必须满足以下要求：

1. 必须启用匿名活动跟踪。 2. Shopify [必须启用行为事件](https://help.klaviyo.com/hc/en-us/articles/4425956184731)。 3. 网站访问者必须接受营销和分析 cookie。 ## 禁用cookie

在某些情况下，您可能会选择禁用 Klaviyo cookie 的跟踪。这些原因可能包括：

- 由于隐私、GDPR 或其他安全问题，您不想跟踪用户。 - 客户要求不要被追踪。 - 您有一个精益的营销计划，或者希望所有客户都收到相同的营销，无论他们之前是否与您的品牌进行过互动、购买过等。无论您是否关闭或打开 cookie，Klaviyo 表单（包括弹出窗口）都将继续出现在您的网站上。但是，您将无法为不同类型的用户（例如，他们已经订阅）个性化不同类型的表单，或者无法看到他们填写表单后在您的网站上执行的操作。如果 JavaScript 选项关闭，客户将不会被 cookie 记录，并且您将无法访问网络跟踪或他们在您网站上的特定行为。 **static-tracking.klaviyo.com** 域用于提供与跟踪相关的所有 Javascript（例如，analytics.js）。如果您希望阻止所有跟踪，也可以使用 Cookie 同意管理工具（例如 [OneTrust](https://help.klaviyo.com/hc/en-us/articles/4764571493275) 或其他域级阻止工具）来阻止该域。如果您想保留 Klaviyo JavaScript 但删除 cookie，有一种解决方法。通过创建新的 cookie `__kla_off` 并运行 `document.cookie = "__kla_off=true"` 来打开和关闭 Klaviyo 跟踪。 ## 使用API访问cookie

使用 API 访问 cookie 对于检查 Klaviyo 是否可以识别客户很有用。您可以通过运行 JavaScript 并输入 klaviyo.isIdentified() 来完成此操作。然后响应将为 **true** 或 **false**。 ## 发送电子邮件至网站跟踪

启用[电子邮件到网站跟踪](https://help.klaviyo.com/hc/en-us/articles/115005248128) 后，Klaviyo 会识别点击 Klaviyo 电子邮件并浏览您网站的个人。您可以在帐户的电子邮件设置中打开和关闭 Klaviyo 跟踪电子邮件到网站活动的功能。随着 iOS15、macOS Monterey、iPadOS 15 和 WatchOS 8 的发布，Apple Mail 隐私保护 (MPP) 通过预取跟踪像素改变了我们接收电子邮件打开率数据的方式。随着这一变化，重要的是要了解开放率将会上涨。要查看您的打开是否受到影响，我们建议创建一个包含 MPP 属性的[自定义报告](https://help.klaviyo.com/hc/en-us/articles/4416803987739)。您还可以在您的个人[订阅者细分](https://help.klaviyo.com/hc/en-us/articles/4416791883163)中识别这些开放。有关 MPP 打开的完整信息，请访问我们的 [iOS 15：如何准备 Apple 的更改](https://www.klaviyo.com/blog/apple-ios15-klaviyo) 指南。 要导航到您的电子邮件设置页面，请单击****帐户 > 设置 > 电子邮件 > 跟踪****。 ![通过电子邮件发送到网站跟踪，并勾选复选框选项](https://klaviyo.zendesk.com/hc/article_attachments/28716055138715)

启用此功能后，我们会向您电子邮件中的所有 URL 添加一个附加参数以跟踪活动。这称为 \_kx 参数，\_kx 将直接出现在 URL 中。然后，我们的网络跟踪会对唯一的加密值进行解密，使我们能够识别点击该 URL 的用户。对于 Shopify 商店：根据您在 Shopify 中的客户隐私设置，Klaviyo 可能不会跟踪欧盟、欧洲经济区、英国和瑞士的 Shopify 商店访客的现场活动，除非他们已表示同意。因此，电子邮件到网站的跟踪不会识别这些人的身份。要了解更多信息，请查看我们关于 [Klaviyo 现场跟踪] 的文章(https://help.klaviyo.com/hc/en-us/articles/115005076767)。