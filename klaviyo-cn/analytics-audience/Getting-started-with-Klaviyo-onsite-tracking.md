---
id: "115005076767"
title: "Klaviyo 现场跟踪入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005076767-Getting-started-with-Klaviyo-onsite-tracking"
section: "Getting started with metrics"
category: "Analytics"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-15T08:50:35Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 支持电子商务网站现场跟踪的不同方式。现场跟踪有两种主要类型：

- *****现场活跃***** ****跟踪****
  每当可识别的浏览器访问您的网站时，就会跟踪此指标。 - *****查看的产品****** ****跟踪****
  每当可识别的浏览器查看您网站上的产品页面（对于电子商务商店）时，就会跟踪此指标。 **活跃的网站**跟踪可以帮助根据参与程度对您的联系人进行细分，而**查看的产品**跟踪可以让您在[浏览放弃流程](https://help.klaviyo.com/hc/en-us/articles/115002775252)中发送产品提醒。对于 Shopify，我们还提供[其他类型的现场跟踪](https://help.klaviyo.com/hc/en-us/articles/4425956184731#h_01J6F7TREZAJM7M3R3DFVZSDGT)。 ## 开始之前

对于每个电子商务集成，启用现场跟踪都是不同的。在本文中，您将了解如何执行此操作以及 Klaviyo 跟踪谁。用于现场跟踪的代码片段被称为 Klaviyo 的现场 JavaScript 或“Klaviyo.js”。如果您通过以下电子商务集成之一启用了主动现场跟踪，则无需单独添加 Klaviyo.js：

- [****Shopify****](https://help.klaviyo.com/hc/en-us/articles/115005080407)
  **现场活动**跟踪是通过集成或通过 [Klaviyo 应用程序嵌入](https://help.klaviyo.com/hc/en-us/articles/4425956184731) 自动添加的（如果已打开）。 - [****BigCommerce****](https://help.klaviyo.com/hc/en-us/articles/115005082547)
  如果您还检查了设置 **自动添加 Klaviyo 现场 javascript，则在集成时会添加 **现场活动** 跟踪。**
- [****WooCommerce****](https://help.klaviyo.com/hc/en-us/articles/115005255808)
  **现场活动**跟踪会在您集成时自动添加。 - [****Magento****](https://help.klaviyo.com/hc/en-us/articles/115005254348)
  **现场活动**跟踪会在您集成时自动添加。 - [****Wix****](https://help.klaviyo.com/hc/en-us/articles/6202669053723)
  如果您选中设置 **自动添加 Klaviyo 现场 javascript**，则在集成时会添加 **现场活动** 跟踪。 - [****PrestaShop****](https://help.klaviyo.com/hc/en-us/articles/360054551492)
  **现场活动**跟踪会在您集成时自动添加。 - [****Salesforce 商务云****](https://help.klaviyo.com/hc/en-us/articles/360033744951)
  **现场活动**跟踪会在您集成时自动添加。 - [****广场在线****](https://help.klaviyo.com/hc/en-us/articles/11117215837211)
  如果您选中设置 **自动添加 Klaviyo 现场 javascript，则在集成时会添加 **现场活动** 跟踪。**
- [****商店软件****](https://help.klaviyo.com/hc/en-us/articles/13001662470939)
  **现场活动**跟踪会在您集成时自动添加。如果您使用的是其他电子商务平台或自定义平台，您可以[手动安装 Klaviyo.js。](#h_01GMEAQZXKADF4FR7P1FMNC7EB)

由于粘贴此代码需要访问您网站的 HTML 和电子商务平台，因此我们的支持团队无法提供实际帮助。如果您的团队中没有开发人员资源并且不愿意添加代码，请考虑[向 Klaviyo 合作伙伴寻求帮助](https://klaviyo.partnerpage.io/)。 ## 活跃的现场事件数据

**现场活动**事件捕获有关已识别访问者的以下信息，并在事件数据中表示。 **浏览器**、**操作系统**和**页面**之外的事件数据仅适用于 2025 年 1 月 3 日之后捕获的**站点上活动**事件。 - ****浏览器****
  原始浏览器的用户代理（例如“Chrome”）。 - ****操作系统****
  原始操作系统（例如“Mac”）的用户代理。 - ****页****
  访问页面的 URL。 - ****utm\_medium****
  用户访问网站的营销渠道。 - ****utm\_源****
  网站的流量来源。 - ****utm\_campaign****
  与流量关联的营销活动的名称。 - ****utm\_id****
  与流量关联的营销活动的唯一标识符。 - ****utm\_term****
  这是一个可选的 UTM 参数，营销人员可以设置该参数来跟踪付费搜索词。对于每个 [UTM 参数](https://help.klaviyo.com/hc/en-us/articles/115005247808)，Klaviyo 将返回 URL 查询参数中的第一个值。 如果 URL 上不存在 UTM 参数，则事件中不会提供任何值。 - ****碎片****
  URL 中的任何其他项目，例如指示用户将登陆页面的位置的锚标记。如果 URL 上没有片段，则不会设置任何值。 - ****身份\_来源****
  触发Klaviyo接收现场事件的事件。 - ****参数****
  URL 中的前 10 个参数中的每一个都有自己的事件数据，**\_kx** 和 UTM 除外。如果 URL 上没有参数，则不会设置任何值。不捕获前 10 个之外的参数。 - ****第一\_页\_路径****
  客户登陆的第一页的路径。如果第一页视图上没有路径，则不设置任何值。 - ****Kx\_现在****
  如果 URL 上存在 \_kx，则为维度返回 **true**。如果不是，则返回 **false**。这会突出显示该会话是否可以与 Klaviyo 消息中的链接点击相关联。 ## 手动添加现场跟踪

1. 复制以下 **Active on Site** 代码片段，也称为 Klaviyo.js：

   ````
   <script type="text/javascript" async="" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   ````
2. 在 Klaviyo 中，单击左下角您的帐户名称，然后导航至****设置 > 帐户 > API 密钥****，然后记下您的公共 API 密钥。 3. 将代码片段粘贴到站点的主模板中。在代码片段中看到 PUBLIC\_API\_KEY 的地方，将其替换为您的密钥。 4. 保存并发布您的站点模板。现在您已经安装了 **Active on Site** 跟踪，只要可识别的人员访问您的网站，Klaviyo 就会进行跟踪。 ## 了解 **查看的产品** 跟踪

Klaviyo 中的**已查看产品** 跟踪专为电子商务商店设计，可让您在[浏览放弃流程](https://help.klaviyo.com/hc/en-us/articles/115002775252) 中发送产品提醒。安装**查看的产品**后，每当可识别人员查看您网站上的产品页面时，它就会记录一个指标。对于每个电子商务平台，启用**查看的产品**跟踪都是不同的。如果您没有看到从此指标捕获的数据，请仔细检查其安装是否正确。了解如何为这些电子商务平台启用**查看的产品**跟踪：

- ****Shopify****
  通过[Shopify 中嵌入的 Klaviyo 应用](https://help.klaviyo.com/hc/en-us/articles/4425956184731) 启用 **V****iewed 产品** 跟踪。 - ****BigCommerce****
  [了解如何向您的 BigCommerce 商店添加已查看商品跟踪](https://help.klaviyo.com/hc/en-us/articles/115005082547#add-viewed-product-tracking4)。 **查看的产品** 跟踪是通过这些电子商务集成自动安装的：
- [Magento 1 集成](https://help.klaviyo.com/hc/en-us/articles/115005082187)
- [Magento 2 集成](https://help.klaviyo.com/hc/en-us/articles/115005254348)
- [WooCommerce 集成](https://help.klaviyo.com/hc/en-us/articles/115005255808)
- [PrestaShop 集成](https://help.klaviyo.com/hc/en-us/articles/360054551492)
- [Salesforce Commerce Cloud 集成](https://help.klaviyo.com/hc/en-us/articles/360033744951)
- [商店软件集成](https://help.klaviyo.com/hc/en-us/articles/13001662470939)

**查看的产品**跟踪也可以添加到其他电子商务平台和自定义购物车。有关如何执行此操作的说明，请参阅我们的[详细介绍如何为自定义电子商务商店添加查看的产品跟踪的指南](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration#viewed-product-tracking-snippet)。 ## 测试您的现场跟踪

在网站上启用跟踪后，您可以按照以下步骤测试跟踪设置是否正确：

1. 导航到您的网站。 2. 将以下内容添加到商店网址末尾，将 example@gmail.com 替换为您的电子邮件地址：
   ****?utm\_email=example@gmail.com****
3. 重新加载页面后，在 Klaviyo 中搜索您的电子邮件地址。 4. 您应该看到已为您创建了 Klaviyo 个人资料（如果尚不存在），并且已在您的活动源中跟踪此网站访问。 5. 要查看 **现场活动** 和 **查看的产品** 指标的所有跟踪活动的摘要，请导航至 ****分析 > 指标****。您可以单击每个指标，通过活动源、活动地图、图表、最佳人员和群组报告来分析跟踪数据。 您还可以按来源过滤。按 ****API**** 过滤以查看现场活动和查看的产品事件（这些事件有一个齿轮图标）。 ![Klaviyo 中的“指标”选项卡按 API 过滤，显示现场活动并在带有齿轮图标的列表中查看产品](https://klaviyo.zendesk.com/hc/article_attachments/28723623317403)

## Klaviyo 追踪谁

通过在网站上启用基本的现场跟踪，您可以收集有关浏览活动的有用信息，这些信息可用于您的营销策略。当您将 Klaviyo 的现场跟踪添加到您的网站时，它仅跟踪“已知浏览器”的浏览活动（即访问过或参与您的网站、通过特定操作提交表单、到达表单成功步骤、到达短信点击文本的最终可到达步骤、或已被识别或“cookied”的浏览器）。如果电子邮件被转发，然后被后续人员打开并单击，这将导致该设备链接到打开/单击。它还可以更新和覆盖最初收到该电子邮件的人的个人资料信息。 ![名为 Johan 的订阅者个人资料示例，时间线上有登录和活动网站事件](https://klaviyo.zendesk.com/hc/article_attachments/28723623315867)

Klaviyo 可通过多种方式识别网站访问者以进行现场跟踪：

- 如果有人在某个时候通过 Klaviyo 电子邮件或短信点击了您的网站。 - 如果有人在某个时候通过 Klaviyo 表格订阅/选择加入。 - 如果有人已通过特定操作提交了 Klaviyo 表格。为了跟踪提交的表单，访问者必须提交一个与其关联的提交操作的表单步骤（例如，**提交并转到下一步**、**提交选择加入代码**、**提交表单并转到 UR**L）；如果表单步骤的提交操作仅为 **转到 URL** 或 **关闭表单**，则不会计算在内。如果表单同时具有 **提交表单** 和 **转到 URL** 操作，则仅当有人提交表单时才会计数事件。 - 如果某人已达到表单的成功步骤，或达到点击文本（**通过短信订阅**）表单的最终可达步骤。 - 如果有人在某个时候登录了您的网站（并且您已经安装了[登录用户的自定义跟踪](https://developers.klaviyo.com/en/docs/javascript_api#identify-people)，这不包含在 Klaviyo 的本机电子商务集成中）。因此，除非您使用 Klaviyo 发送电子邮件或消息并扩大您的列表，否则您可能不会看到很多跟踪的现场活动。随着时间的推移，Klaviyo 将识别出越来越多的您的联系人，您的现场跟踪数据将变得更加全面。对于 Shopify 商店，根据您在 Shopify 中的客户隐私设置，Klaviyo 可能不会跟踪欧盟、欧洲经济区、英国和瑞士的 Shopify 商店访客的现场活动，除非他们已表示同意。 ## 如何使用现场跟踪的示例

使用现场跟踪的方法包括：

- ****根据参与程度细分您的联系人。****
  通过深入了解哪些联系人与您的网站互动以及互动频率，您可以制定更加个性化的沟通策略，从而推动更深入的互动。 - ****向那些多次浏览但未购买的用户触发自动流程电子邮件或短信。****
  虽然您不想在某人每次访问您的网站时都向他们发送电子邮件或短信，但您可能希望向那些在短时间内多次访问但不进一步参与的人发送一个简单的接触点。例如，您可以触发流向那些在过去 30 天内**在网站上活跃**至少 4 次但尚未开始或完成结账的用户。需要注意的是，特别是对于 **Active on Site** 事件，虽然您可以对事件本身进行分段，但其中的数据不能用于分段或流过滤。 ## \_kx 参数

当您启用**电子邮件到网站**跟踪并在您的网站上安装 Klaviyo.js 时，Klaviyo 将识别点击 Klaviyo 电子邮件然后最终浏览您网站的个人。这是 Klaviyo 识别新网站访问者并对他们进行 cookie 的基本方法之一，以便他们在以后访问您的页面时能够被识别。 SMS 消息点击和转化跟踪取决于是否有链接，并且此链接必须使用 Klaviyo 链接缩短程序。 设置短信时，务必选中“****自动缩短链接****”选项，以确保您使用默认跟踪。 Klaviyo 的电子邮件网站跟踪的工作原理是向您发送的所有 URL 添加一个附加参数（即 **\_kx** 参数）。然后，唯一的加密值由 **Active on Site** 片段解密，并允许我们识别点击 URL 的用户。请参阅下面的示例链接，了解其在 URL 中的外观：

`http://example.com/?_kx=J8fjcn003Wy6b-3ILNlOyZXabW6dcFwTyeuxrowMers%3D.McN66`

发送实时电子邮件时会自动附加此参数，并且不会影响链接的加载时间或根据其位置破坏任何链接。请注意，预览电子邮件时，为 \_kx 参数设置的值将只是一个占位符，以防止被 cookie 为收件人。但是，如果您使用包含查询参数的 URL 来通知服务器自动下载文件，则 \_kx 参数可能会导致链接中断。为了使下载正常运行，请在您的帐户电子邮件设置中关闭电子邮件到网站的跟踪，或将您的服务器配置为忽略此参数。截至目前，您只能在您的帐户中关闭此功能；您无法针对单个广告系列将其关闭。