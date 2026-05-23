---
id: 5913
title: "如何为 Customer Hub 创建 Content Blocks"
slug: "contentblocksforcustomerhub"
category: "自助客户中心（Customer Hub）"
category_slug: "customer-hub"
wp_url: "https://dynamicycle.com/docs/contentblocksforcustomerhub/"
wp_modified: "2025-12-30T06:29:38"
---

了解如何为您的 [Customer Hub](https://www.klaviyo.com/customer-hub/dashboard) 创建 Content Blocks。Content Blocks 是高度可定制且个性化的 Blocks，可以访问 Klaviyo 的 Profile数据，从而允许您展示集成信息（例如：忠诚度积分余额）、个性化优惠等。

目前 Customer Hub 支持 Shopify 店铺（包括 Shopify Headless）。计划未来将支持更多电商平台。

##### ****开始之前****

本指南将解释如何设置 Content Blocks，以便它们在您网站的 Customer Hub 中显示。

##### ****Content Blocks 的功能与应用****

Content Blocks 帮助您自定义 Customer Hub 界面中的 ****“[For you](https://www.klaviyo.com/customer-hub/design)”**** 选项。您可以使用它们显示针对特定客户的信息或鼓励访客执行某些操作，确保每位用户在与您的在线 Customer Hub 互动时都能享受量身定制的体验。您可以创建自己的自定义 Content Blocks，或使用 Klaviyo Content Block 库中的模板（包含针对常见场景预配置的 Blocks，以及从各种集成中提取客户数据，如忠诚度积分或订阅状态）。

###### ****Content Blocks 的常见用例****

- ****鼓励采取行动****：引导访客联系您（例如：“给我们发邮件”）；将购物者引导至特定的 URL 或页面（例如：订阅管理或引流奖励信息页面）。
- ****突出并引导客户旅程****：为已登录的购物者推送特别优惠或独家系列；展示带有评价和图片的优质产品。
- ****显示来自 Klaviyo Profile 的个性化信息****：使用个性化标签动态展示来自客户 Klaviyo Profile 的特定详细信息。这可以是您通过 Klaviyo 收集、导入或从其他平台及集成同步的信息，例如：
  - 忠诚度积分
  - 订阅状态
  - 会员等级
- ****高级个性化设置****：使用 ****if/else**** 条件逻辑，根据客户 Profile 数据控制 Content Block 中显示的信息（例如：仅向奖励计划会员显示奖励信息，而向其他人显示默认消息）。

![一个欢迎界面显示用户姓名，包含关于限量版商品的特别访问以及用户积分信息。界面下方有用户最近查看的商品缩略图和分类导航选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-171.png?resize=1024%2C637&ssl=1)

##### ****Content Block 事件****

创建 Content Block 时，您必须为其命名。Klaviyo 会将访客每次点击 Content Block 的行为记录为 “Customer Hub clicked on content block” 事件，并使用您提供的名称进行报告和过滤。因此，建议选择一个易于识别且与每个 Block 内容相关的名称。

请记住，名称仅供内部使用，您的客户不可见。此外，Block 的名称一旦创建便无法更改。

##### ****创建一个新的 Content Block****

创建并发布 Content Blocks 到您的 Customer Hub 界面需要遵循几个步骤。接下来的章节将详细介绍这些设置。

###### ****访问 Content Blocks****

1.导航至 Klaviyo 左侧导航栏中的 [****Service – Customer Hub****](https://www.klaviyo.com/customer-hub) 选项。

2.点击 [****Design****](https://www.klaviyo.com/customer-hub/design)。

3.在右侧的预览界面中，找到 ****“+”**** 按钮。

![A user interface design showing a welcome message and a section for recently viewed items, featuring a blue plus icon for adding new content.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-172.png?resize=832%2C588&ssl=1)

4.点击 ****“+”**** 按钮选择如何添加 Content Block：

- 使用来自 Content Block 库的预建模板。按类别（例如：忠诚度、优惠、名单增长）浏览库，或按集成进行筛选。点击任一模板上的 Add block，即可在 Content Block 编辑器中将其打开，其中的字段已预填，但完全可以编辑。
  - 针对特定集成的 Content Blocks 要求您已在 Klaviyo 中启用了相应的集成。
- 自行构建 Content Block。点击 Build your own，在编辑器中打开空白设置菜单。

![Content block library interface displaying various content block options such as seasonal deals, promotional deals, and gift cards.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-173.png?resize=1024%2C416&ssl=1)

##### ****配置您的 Content Block****

一旦您选择了起点（模板或从头开始），该 Content Block 将显示在预览中。您可以点击任何 Content Block 来编辑其配置。

1.在 Content 下，您可以编辑：

- Block title 编写一个标题或CTA（例如：选购春季系列）。
- Block description 使用常规静态文本添加详细信息或背景，或插入个性化标签以提取动态的、针对特定客户的信息（例如：可用奖励积分）。目前不支持 Event 数据。 如果您使用的是针对特定集成的模板，个性化标签已预先配置，以匹配该平台的自定义属性名称。
- Link提供一个 URL，以便在访客点击该 Block 时将其引导至特定页面（例如：产品页面）。您还可以选择链接是否在新标签页中打开。
- Internal name 创建一个易于识别的名称（例如：显示奖励积分的 Block 命名为“Rewards”）。请注意，此名称用于报告，且一旦保存便无法更改。
- Banner image上传一张显示在该 Content Block 顶部的图片。

2.在 Targeting 下，选择哪些类型的访客可以看到该 Content Block：

- Login status：根据登录状态选择可以看到该 Content Block 的访客类型。
- List/segment membership：针对特定的 Lists & Segments 显示或隐藏该 Block：
  - Show to：：选择应该看到该 Block 的 Lists & Segments。
  - Don’t show to：：选择不应该看到该 Block 的 Lists & Segments。

3.完成后，点击 Add。

若要预览您的 Content Block 在 Customer Hub 中的外观，请切换到左侧的 ****[Design](https://www.klaviyo.com/customer-hub/design)**** 菜单。在这里，您可以在 Customer Hub 预览画布中查看效果，并选择任何 Content Blocks 进行编辑。

![编辑内容块的界面，包括阻止标题、描述和链接设置，以及内容块及其个性化选项的配置。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-174.png?resize=1024%2C763&ssl=1)

### ****客户如何看到您的 Content Blocks****

网站访客看到的 Content Blocks 以及其中显示的详细信息，取决于他们是否已登录账户以及 Klaviyo 是否已识别他们的身份。请记住：

- Klaviyo 仅能向已登录账户或通过其他方式（例如：点击邮件中的链接或填写了注册弹窗）被 Klaviyo 识别的访客，显示针对特定 Lists & Segments 的 Content Blocks。匿名的未登录访客将看不到这些 Blocks。
- 带有个性化标签的 Content Blocks 仅会为已登录访客显示 Profile 数据。如果访客未登录，将显示默认值；如果没有设置默认值，则该文本不会显示。
- 如果您配置某个 Content Block 仅对特定的 Segment 显示，而该 Segment 变为不活跃状态，则该 Content Block 将不再对任何人可见或可用。为了防止您的 Segments 被停用并确保 Content Blocks 的持续访问，请在 Klaviyo 的 Segments 区域点击 Segment 名称旁的星标图标。

### ****使用个性化标签提取 Profile 数据****

Content Blocks 支持使用 Profile 和自定义个性化功能，从每个客户的 Klaviyo Profile 中动态提取信息。

Content Block 库包含多个针对特定集成的模板，这些模板已针对相应平台和特定用例设置了正确的个性化标签。但是，如果您有不同的集成或用例需求，可以在 Content Block 的描述中添加或修改个性化标签，以显示您需要的数据。

请注意，Customer Hub 中的 Content Blocks 目前不支持 Event 数据。

##### ****个性化标签的示例用例****

在个性化标签中引用自定义 Profile 属性时，请确保“lookup”部分的值与您在 Klaviyo 中存储该属性的方式一致。自定义属性的格式或命名可能与提供的示例不同。

- ****显示可用忠诚度积分：**** `You have {{ person|lookup:'loyalty_points'|default:'0'|floatformat:0 }} points`
- ****提醒购物者其会员等级（例如：青铜、白银、黄金）：**** `{{ person|lookup:'Membership Tier'|default:'No membership' }} Status`
- ****通过个性化引导特定的购物旅程：**** `Celebrate your {{ person|lookup:'breed_type'|default:'dog' }}`

****提示****：请记住，在使用个性化标签时，某些访客可能尚未提供标签所引用的所有数据。为了应对这些情况，****请使用默认文本****，以防止在缺失数据的地方出现空白。

##### ****使用条件逻辑****

对于更高级的定制，您可以使用 ****if**** 条件语句，根据购物者的 Profile 信息来控制 Block 对不同购物者的显示方式。

###### ****if/else 语句示例****

- ****帮助会员管理当前的订阅，同时激励非会员开启订阅计划：**** `{% if person.subscription_status not "Cancelled" and person.subscription_status %}Manage your subscription {% else %}Start a subscription & save! {% endif %}`
- ****与 VIP 忠诚会员互动，同时向非会员展示加入的CTA：**** `{% if person|lookup:'Loyalty Points' > 150 %}Hey VIP! You’ve always got free shipping & free returns {% else %}Have you heard about our VIP program? Join today on our website to start earning rewards. {% endif %}`

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)