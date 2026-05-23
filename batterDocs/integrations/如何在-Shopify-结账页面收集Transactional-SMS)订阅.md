---
id: 7230
title: "如何在 Shopify 结账页面收集Transactional SMS)订阅"
slug: "transactional-sms"
category: "集成（Integrations）"
category_slug: "integrations"
wp_url: "https://dynamicycle.com/docs/transactional-sms/"
wp_modified: "2026-04-27T05:40:41"
---

### ****关于SMS app blocks****

您可以使用短信应用块来收集营销类同意、交易类同意，或两者兼而有之。

您可以创建多个短信应用块，并将它们放置在不同的页面上，包括：

仅限 Shopify Plus 用户：

结账页面（账单、运送和信用卡信息页面，以及单页结账页面）。

感谢页面 (Thank you pages)

订单状态页面 (Order status pages)

您可以在 Klaviyo 中查看和编辑您的短信应用块，但必须在 Shopify 内部进行添加或删除操作。

设置您的短信应用块

请按照以下说明设置SMS app blocks。如果您想创建多个应用块以在不同位置收集不同形式的同意，只需重复此过程即可。您也可以在多个 Shopify 页面上安装同一个应用块。

1.在 Klaviyo 中，选择 Audience> Growth tools。

2.在 Add an app to your Shopify page to collect SMS subscribers（在您的 Shopify 页面添加应用以收集短信订阅者）旁边，选择 Set up。

![收集订阅者的网页体验界面，包括管理注册表单、自定义订阅和偏好页面，以及添加应用以收集短信订阅者。](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_626949_8JHtLF4lqsPZcTRW_1773799188?w=1708&h=758&type=image/png)

- 为您当前的 app block 起一个具有描述性的名称，例如它所在的页面名称。一个 app block 可以放置在多个页面上，或者您也可以创建多个 app blocks。

![设置 SMS 应用块的界面，包含应用块名称和 SMS 订阅者列表的选项。](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_203004_U5LVpdYencP-JdfO_1773799227?w=982&h=646&type=image/png)

4.选择短信订阅者将同步到的列表。

通常，您会希望选择与集成设置中相同的列表。您的客户将根据该列表的设置收到双重确认 (Double opt-in) 短信。仅限交易类 (Transactional-only) 的订阅者不会收到双重确认短信。

5.点击 Next。

6.在 Select a consent type (选择同意类型) 下，选择以下选项之一：

- 交易类与营销类 (Transactional and marketing)
- 交易类及可选营销类 (Transactional with optional marketing)
- 仅限交易类 (Transactional only)
- 收集电话号码但不获取同意 (Collect phone number without consent)

![短信类型选择界面，包括推荐的交易和营销消息选项，用户可以选择是否接受新闻和优惠的订阅。](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_993399_pLx6Xs40iZBE-TTL_1773799361?w=984&h=992&type=image/png)

- 接下来，为您的 app block 添加标题文本，如下图所示。在右侧，您将看到该 app block 在 Shopify 中的样式预览。请注意，此预览不会反映您的 Shopify 主题颜色，因为当该 app block 安装到 Shopify 后，它会自动继承主题颜色。

![一个注册新闻和优惠的表单，包含手机号输入框和注册按钮。](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_63818_C45hTk4-iHQbW8ZM_1773799401?w=1134&h=602&type=image/png)

8.点击 Next。

9.如果需要，请编辑您的 Disclosure text (披露文本)。然后，点击 Next (下一步)。

10.编辑您的 app block 的其他内容。这些字段包括：

- 输入标签 (Input label)：电话号码输入框上的标签。
- 无效文本 (Invalid text)：当 A/B 测试 或常规提交遇到错误时显示的提示信息。
- 提交按钮文本 (Submit button text)：提交按钮上的文字（例如：“立即注册”）。
- 成功消息 (Success message)：用户成功提交电话号码后收到的消息。

11.完成后，点击 Next。

12.在下一页中，点击复制图标以复制该 app block ID，并将其保存在易于访问的地方。

![包含应用块和应用块ID的界面，显示了结账页面的选项](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_685438_6oCfpOK16z5LRBqb_1773799551?w=1466&h=368&type=image/png)

13.现在，您可以停用原有的同意收集功能（如果需要），然后在 Shopify 中安装 app block。

##### ****在 Shopify 中停用短信同意收集****

如果您符合以下情况，请考虑停用 Shopify 原生的勾选框，以避免在结账页面出现重复的勾选框：

您是 Shopify Plus 客户，

之前通过 Shopify 原生勾选框在结账时收集营销同意，并且

现在想通过 SMS app block 在结账时收集营销同意。

操作步骤如下：

- 在 Shopify 管理后台，点击左侧边栏底部的 Settings (设置)。
- 在设置页面，点击 Checkout (结账)。
- 在 Marketing options (营销选项) 下，关闭 SMS 选项。
- 点击保存

![营销选项的设置界面，包含电子邮件和短信营销的选择框，允许客户选择在特定区域注册。](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_189302_j51kdBbHLo3MfoxB_1773799642?w=1448&h=678&type=image/png)

请注意，您需要保持 Shopify 集成设置中的 Sync your Shopify SMS subscribers to Klaviyo（同步您的 Shopify 短信订阅者到 Klaviyo）处于勾选状态，以便继续将通过其他方式（如 Shopify 弹窗）收集的订阅者同步到 Klaviyo。

如果您希望通过 SMS app block 订阅的 Profile 同步回 Shopify，请确保该设置已开启。

##### ****在 Shopify 中安装 app block****

- 在您的 Shopify 管理后台，选择 Online Store (网上商店)。
- 找到您的 Shopify 主题并点击 Customize (自定义)。
- 选择顶部的 Home page (主页) 下拉菜单，点击 Checkout and customer accounts (结账和客户账户) 以进入结账编辑器。
- 选择 Checkout (结账) 下拉菜单，然后选择您想要放置 app block 的页面。
- 滚动到您想要添加 app block 的区域，点击 + Add app block。了解更多关于放置 app block 的信息。

![结账页面，包含交付和运输选项，显示交付方式、运输地址和运输费用。](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_200402_-QK0246ZqLzuL2gI_1773799696?w=940&h=816&type=image/png)

- 点击标记为 Opt-in at checkout 的 Klaviyo app block。
- 在 Klaviyo App Block ID 下方，粘贴您之前从 Klaviyo 保存的 ID。

![结账行为设置界面，包含应用块在Shop Pay中的选项和Klaviyo应用块ID的输入框。](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_410288_Wlao0ZuPuAMrE1RN_1773799737?w=806&h=786&type=image/png)

- 如果需要，您可以开启 Include app block in Shop Pay（在 Shop Pay 中包含 app block）选项。
- 点击 Save (保存)。
- 您现在应该可以在所选页面上看到已上线的 app block。

##### ****管理您的 SMS app blocks****

若要管理您的 app blocks：

- 导航至 Audience> Growth tools。
- 在 Add an app to your Shopify checkout page to collect SMS subscribers 旁边，点击 Manage 。

![列表增长工具界面，包含管理注册表单、定制订阅和偏好页面，以及将应用添加到Shopify页面以收集短信订阅者的选项。](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_958993_Z23wMmq5hGvCOFLK_1773799809?w=1390&h=664&type=image/png)

- 在这里，您将能够查看所有的 SMS app blocks。

![SMS应用块管理界面，包含三个应用块的列表，显示应用块名称、应用块ID和提交数量。](https://wdcdn.qpic.cn/MTY4ODg1NzU3MjU5NTc3Ng_593998_xzXhzk7ojan3CNUF_1773799843?w=1884&h=534&type=image/png)

若要创建新的 app block，请点击 Create app。

点击 app block 旁边的“三个点”图标，您将看到以下选项：

- 管理列表 (Manage list) 管理与您的 app block 关联的列表。
- 重命名 (Rename) 重命名您的 app block。
- 编辑 (Edit) 编辑您的 app block 内容。
- 安装 (Install) 查看关于在 Shopify 中安装 app block 的说明。
- 克隆 (Clone) 克隆您的 app block。
- 删除 (Delete) 在 Klaviyo 中删除您的 app block。请注意，这不会在 Shopify 中将其删除，但它会变为一片空白且不占用任何空间。您可以点击该 app block 并点击垃圾桶图标，在 Shopify 中彻底移除它。

![一组操作选项，包括管理列表、重命名、编辑、安装、克隆和删除。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/03/image-21.png?resize=826%2C668&ssl=1)

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)