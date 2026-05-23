---
id: 6330
title: "WooCommerce迁移至Klaviyo"
slug: "woocommerce"
category: "集成（Integrations）"
category_slug: "integrations"
wp_url: "https://dynamicycle.com/docs/woocommerce/"
wp_modified: "2026-01-08T09:00:49"
---

了解如何安装 Klaviyo WooCommerce 扩展程序并在您的 Klaviyo 账户中启用 WooCommerce 集成。

与 WooCommerce 集成的主要步骤包括：

1. 在 WooCommerce 中安装 ****Klaviyo 扩展程序****（也称为 Klaviyo 插件）。
2. 在 Klaviyo 中启用 ****WooCommerce 集成****。

##### 在 WooCommerce 中安装 Klaviyo 扩展程序

Klaviyo 的 WooCommerce 扩展程序允许您在网站中添加新闻信订阅****弹窗****、启用网站活动追踪，并获取用户“开始结账”和“查看产品”的数据，以便您发送弃购挽回邮件。我们的扩展程序同时也兼容“高性能订单存储 (HPOS)”。

****在开始之前：**** 我们建议您先登录您的 Klaviyo 和 WooCommerce 账号。如果您拥有多个 Klaviyo 账号，请退出所有您不希望与 WooCommerce 集成的账号。

****操作步骤：****

1.在 WooCommerce 中，点击左侧导航栏的 ****WooCommerce**** 选项卡，然后选择 ****Extensions**** (扩展)。

2.搜索 ****Klaviyo****，然后选择 ****Klaviyo for WooCommerce****，进入 WooCommerce 市场中的 Klaviyo 扩展程序页面。

![Klaviyo for WooCommerce 插件的介绍，包括功能描述和免费下载选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-72.png?resize=1024%2C521&ssl=1)

3.点击 Add to cart。

4.请确保您已登录 WooCommerce Marketplace账户，然后进行Check out。

5.继续完成结算流程，系统将带您进入订单确认页面，随后点击 Add to Site（添加至网站）。

6.如果您的 WooCommerce 市场账户尚未连接到您的 WooCommerce 网站，请在框中复制并粘贴您的商店 URL。如果已经连接，请直接从下拉菜单中选择您的网站。然后，点击 Add to site。

![A form prompting users to enter the URL of their WooCommerce site to add a Klaviyo extension.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-73.png?resize=888%2C590&ssl=1)

7.返回您的 WooCommerce 管理后台，然后选择 Plugins（插件）。在已安装的插件列表中找到 Klaviyo，点击 Activate（启用）。

8。从左侧导航栏中选择 Marketing（营销），然后点击 Klaviyo。

9.点击 Connect Account（连接账户）开始操作，随后进入下一部分。

![Klaviyo和WooCommerce集成的登录界面，包含Klaviyo和WooCommerce的标志，提供连接账户和创建账户的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-74.png?resize=1024%2C320&ssl=1)

##### 在 Klaviyo 中启用 WooCommerce 集成

1.如果系统提示，请登录 Klaviyo。为了确保您登录的是正确的 Klaviyo 账号，您可以打开一个新标签页，导航至您的 Klaviyo Dashboard并检查账号名称。如果需要切换账号，请在继续操作前点击 Logout（登出），然后登录正确的账号。

2.查看各项权限要求，然后点击 Approve（批准）予以授权。

![Klaviyo 请求连接到您的 WooCommerce 商店的授权提示，展示所需权限和确认按钮。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-75.png?resize=1024%2C818&ssl=1)

3.在集成设置页面，确认账号名称无误。

![](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-76.png?resize=1024%2C572&ssl=1)

4.勾选 Add email marketing consent checkbox to your checkout page（在结账页面添加邮件营销授权复选框）旁边的框，即可轻松为您的 WooCommerce 网站添加此选项。

- 在 Add email subscribers to this list（将邮件订阅者添加至此列表）下方的下拉菜单中选择一个列表。如果下拉菜单中没有可选列表，请前往 Lists & Segments（列表与细分）选项卡创建一个新列表。
- 任何在结账过程中通过该复选框订阅的用户都将被添加至此列表。授权信息将在客户点击结账页面的 Submit order（提交订单）按钮后发送至 Klaviyo。
- 在 Email marketing consent label（邮件营销授权标签）下方，输入您希望显示在结账页面复选框旁边的授权文案。默认文案为：Sign me up to receive Email updates and news（订阅以接收邮件更新和新闻）。

![Klaviyo WooCommerce 订阅设置界面，包含添加邮件营销授权复选框、选择订阅列表及授权文案选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-77.png?resize=1024%2C552&ssl=1)

5.如果您想为 WooCommerce 网站添加短信订阅选项，请勾选 Add SMS marketing consent checkbox to your checkout page（在结账页面添加短信营销授权复选框）。请注意，如果您的公司设有年龄限制 (Age-gated)，短信授权将无法同步至 Klaviyo。

- 在 Add SMS subscribers to this list（将短信订阅者添加至此列表）下方的下拉菜单中选择一个列表。通过此复选框同意短信营销的用户将被加入您选择的列表。授权信息将在客户点击结账页面的 Submit order（提交订单）按钮且 WooCommerce 生成订单后发送至 Klaviyo。
- 在 SMS marketing consent label（短信营销授权标签）下方，输入您希望显示在结账页面复选框旁边的文本。
- 接下来，添加 SMS consent disclosure text（短信授权披露文本），这是符合 TCPA（美国电话消费者保护法）合规性所必需的。您可以使用 Klaviyo 默认的授权文案，也可以自行添加。

6.如果您希望在处理后续所有的“已下单 (Placed Order)”和“订购产品 (Ordered Product)”事件时，按处理时的汇率将其转换为选定的货币，请勾选 Convert all currencies to one standard currency（将所有货币转换为一种标准货币），然后选择一种货币。更改此设置不会影响之前已集成的数据，也不会更改您账户的默认货币。

7.当您对这些设置感到满意时，点击 Complete setup（完成设置）。您可以随时通过导航至 Integrations 选项卡并选择 WooCommerce 来回过头编辑这些设置。

##### 故障排除

如果您收到错误消息 ****“Unable to test API by fetching order count. Invalid count”****（无法通过获取订单计数来测试 API。计数无效），这意味着当 Klaviyo 尝试验证 WooCommerce 集成并获取订单总数时，其 API 没有返回 Klaviyo 预期的数值，或者完全没有返回任何内容。由于此时集成尚未正式连接到 Klaviyo，因此该问题需要在 ****WooCommerce 内部****解决。

若要获取有关此错误的更多信息，可以使用 Postman 等应用程序对“订单计数”端点发起 API 调用，这将有助于深入了解传递给 Klaviyo 的具体数据。

- ****您需要的端点为：**** `{customers-url}/wc-api/v1/orders/count`
- 请将 `{customers-url}` 替换为您真实的 WooCommerce 商店 URL。

##### 测试您的 WooCommerce 集成

若要测试集成是否成功，请访问您的网站并按照以下步骤操作：

1. 将一件商品****加入购物车****。
2. 进入****结账页面****。
3. 在结账页面填写您的****邮箱地址****和****电话号码****。如果已启用订阅功能，请勾选订阅邮件和短信营销的复选框。
4. ****提交您的测试订单****。
5. ****检查以下各项****（这些数据可能需要一两分钟才会更新）：
   - 在 ****Recent Data****（近期数据）下记录了 ****Started Checkout****（开始结账）事件。
   - 在您选定的邮件和短信营销 ****List**** 中已创建了相应的 Profile（个人档案）。
   - 在 ****Recent Data**** 下记录了 ****Placed Order****（已下单）事件。

##### 数据同步说明

- ****近期数据 (Recent Data)：**** 此板块显示该事件最近一次发生的实例。
- ****历史数据 (Historical Data)：**** 进度条会随着您的历史数据同步进程实时更新。

##### 了解如何利用 WooCommerce 数据在 ****Abandoned Cart Flow**** 中实现“重建购物车”功能。

当用户触发 ****Started Checkout****事件时，Klaviyo 会生成一个唯一的密钥（Key）。利用此密钥，您可以创建一个特殊的链接，让客户即使在不同设备上打开邮件，也能恢复之前购物车中的商品。

###### 如何构建链接

在由 ****Started Checkout**** 触发的 ****Abandoned Cart Flow**** 邮件中，您可以使用以下 URL 参数：

`/cart?wck_rebuild_cart={{ event.extra.CartRebuildKey }}`

****完整的链接组合如下：****

`{{ organization.url|trim_slash }}/cart?wck_rebuild_cart={{ event.extra.CartRebuildKey }}`

###### 关键细节

- ****动态链接：**** 邮件中动态生成的产品标题链接会直接提取您在账户设置中输入的 URL。如有需要，您可以在邮件模板编辑器中手动更新该 URL。
- ****用户体验：**** 这个功能对于那些通过****弹窗****获取优惠券后开始结账，但因故中断的用户非常有效。它能让用户一键回到结账页，无需重新添加商品。

![A screenshot of a button editing interface displaying options for the button text 'Return to your cart' and a link URL related to a shopping cart.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-78.png?resize=750%2C564&ssl=1)

如果您正在使用 `{{ organization.url }}` 链接到一个非安全的 HTTP URL，您需要手动将其更改为 ****HTTPS****，这样购物车重建功能才能正常运作。

##### 扩展程序参考信息

###### 启用自动更新 (Enable auto-updates)

为了确保您能使用最新的功能（如更稳定的****弹窗****展示）：

1. 点击 ****Plugins****（插件）选项卡，向下滚动找到 ****Klaviyo**** 插件。
2. 点击 ****Enable auto-updates****（启用自动更新）。 **如果您愿意，也可以从 WooCommerce 市场手动[下载 Klaviyo WooCommerce 扩展程序](https://wordpress.org/plugins/klaviyo/)。**

###### 查看更新日志 (Find the changelog)

每次扩展程序更新的发行说明都会包含在更新日志中。您可以在 [WordPress 插件目录](https://www.google.com/search?q=https://wordpress.org/plugins/klaviyo/%23developers)查看我们扩展程序的更新日志。

##### 如果我使用的是旧版 (Legacy) API，该如何升级到实时同步？

如果您之前是通过旧版 API 集成的，请按照以下步骤升级：

1. ****安装最新扩展：**** 按照前文所述的安装步骤安装最新的 WooCommerce 扩展程序。
2. ****创建 v3 REST API 密钥：**** 为 v3 集成创建一个具有 ****读/写 (read/write)**** 权限的 REST API 密钥。这与您第一次安装插件时创建的 Legacy API 密钥不同。
3. ****更新 Klaviyo 设置：**** 在 Klaviyo 的 WooCommerce 集成设置页面点击 ****Save settings****（保存设置）。

****版本要求：**** 要使用 WooCommerce API v3，您的 WooCommerce 版本必须为 ****3.5x 或更高****，且 WordPress 版本为 ****4.4 或更高****。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)