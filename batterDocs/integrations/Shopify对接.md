---
id: 5368
title: "Shopify对接"
slug: "start-with-shopify"
category: "集成（Integrations）"
category_slug: "integrations"
wp_url: "https://dynamicycle.com/docs/start-with-shopify/"
wp_modified: "2025-12-24T06:15:28"
---

##### ****如何********对接****

1.在 Klaviyo 中，选择 [Integrations](https://www.klaviyo.com/integrations) 选项卡。

![Klaviyo dashboard showing the 'Integrations' tab option.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-88.png?resize=352%2C88&ssl=1)

2.点击 [Explore apps。](https://marketplace.klaviyo.com/en-us/)

![Klaviyo integrations page showing the option to explore apps with a list of app categories and their statuses.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-91.png?resize=1024%2C661&ssl=1)

3.搜索 [Shopify](https://marketplace.klaviyo.com/en-us/browse/?searchTerm=shopify) 并点击对应卡片，然后点击 [Install](https://marketplace.klaviyo.com/en-us/apps/01h3z8tkt4fdj8yzwenj89077h/)。

![Klaviyo app marketplace search result showing 'Shopify' with an installed status, along with a description about syncing Shopify data for personalized experiences.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-90.png?resize=1024%2C568&ssl=1)

4.在输入框中粘贴你 Shopify 店铺的 URL。确保格式为 mystore.myshopify.com。

5.点击 Connect to Shopify。系统将跳转至你的 Shopify 账户，此时可能需要你登录 Shopify。

6.进入 Shopify 后，查看权限说明并点击 Install app，随后你将被重新引导回 Klaviyo。

7.点击 Integrate 确认集成，这将带你回到集成设置页面。

8.连接 Shopify 后，系统会提示你配置 onsite tracking，因此该部分目前尚不可用。

9.勾选 Sync your Shopify email subscribers to Klaviyo 复选框，以便将那些在结账时接受邮件营销或通过任何 Shopify 表单注册的客户，自动添加到你从下拉菜单中选择的名单中。

10.作为收集 consent 的最佳实践，你应该在 Shopify 的结账设置中自定义 Accepts marketing 复选框的标签文案。

11.如果你选择了上述设置：请从下拉菜单中选择一个用于添加邮件订阅者的名单。我们建议选择能够触发你 welcome series 的主邮件名单。

![Klaviyo集成设置界面，包含Sync your Shopify email subscribers和Sync your Shopify SMS subscribers选项，用户可选择邮件和短信订阅者的同步名单。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-92.png?resize=1024%2C456&ssl=1)

12.勾选 Sync your Shopify SMS subscribers to Klaviyo 复选框，以便将未来所有在 Shopify 中接受短信营销的客户（包括在结账时和通过 Shopify 注册表单）自动添加到你从下拉菜单中选择的名单中。你可以随时设置短信功能并在稍后编辑此设置。注意： 只有当用户是首次在 Shopify 中订阅短信时，其 consent 才会同步到 Klaviyo。

13.如果你选择了上述设置：请从下拉菜单中选择一个用于添加短信订阅者的名单。我们建议为邮件订阅者和短信订阅者使用不同的名单。

14.如果你想要同步任何数据，请勾选 Sync profiles and profile data from Klaviyo to Shopify。我们建议将所有 profiles 和所有类型的数据同步到 Shopify。如果你勾选了此设置，请执行以下操作：

- 选择是同步所有 Klaviyo profiles 的更新，还是仅同步已存在于 Shopify 中的 profiles 的更新。
- 选择你想要同步的 profile 数据：姓名、邮件地址、电话号码、邮件订阅状态、短信订阅状态（如果你已启用 SMS）、邮件事件、短信事件以及自定义 profile properties。

![Klaviyo与Shopify同步数据设置页面，展示配置选项，包括同步所有个人资料、电子邮件、电话号码及订阅状态等。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-93.png?resize=1024%2C757&ssl=1)

15.完成设置后，点击 Complete setup。

16.随后会出现一个绿色的成功提示，表明你的数据正在与 Klaviyo 同步。

不建议在 Klaviyo 中更新那些通过 Shopify 同步过来的自定义 profile properties（例如 Shopify tags），因为这些数据在下一次集成同步时会被覆盖。

##### ****启用 Klaviyo 的 [onsite tracking](https://www.klaviyo.com/integration/shopify)****

它由多个事件组成。利用这些追踪事件可以帮助你触达店铺中可识别的访问者。此外，启用追踪功能后，你才能使用 Klaviyo 的 sign-up forms。启用 Shopify 数据向 Klaviyo 同步以及 Klaviyo 数据向 Shopify 同步将有助于你在账户中查看到更多的Onsite Tracking 事件，因为会有更多的 Profiles 进行同步。

1.在 Onsite tracking 部分，勾选 Track behavioral events，以启用对 Viewed Collection、Submitted Search和 Added to Cart的追踪。另外两个事件 Viewed Product和 Active on Site是默认启用的，一旦你开启应用嵌入，它们就会开始进行追踪。

2.你会看到一条提示消息，告知你的 Klaviyo app embed 处于关闭状态。点击 Turn on，系统将带你进入 Shopify。

![Klaviyo app embed settings for onsite tracking, with options to enable tracking of 'Viewed Product' events and behavioral events.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-97.png?resize=1024%2C565&ssl=1)

3.如果出现提示，请使用你已集成至 Klaviyo 的账号登录 Shopify。

4.你将被引导至主题设置的 App embeds 选项卡。请确保 Klaviyo 的 app embed 已切换为开启状态。

![Klaviyo Onsite Javascript app embed settings in Shopify integration page.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-84.png?resize=390%2C498&ssl=1)

5.在你的theme editor中点击保存。

6.返回 Klaviyo 中的 Shopify 集成设置页面，如果需要的话请刷新页面。你应该会看到一个绿色横幅，表明你的 app embed 现在已启用。

![Klaviyo应用嵌入设置界面，显示已启用的Klaviyo应用嵌入、查看产品跟踪选项以及行为事件跟踪功能的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2025/12/image-96.png?resize=1024%2C609&ssl=1)

你现在已经完成了 Klaviyo 与 Shopify 的集成，并设置好了 onsite tracking。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)