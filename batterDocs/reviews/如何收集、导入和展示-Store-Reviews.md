---
id: 6410
title: "如何收集、导入和展示 Store Reviews"
slug: "storereviews"
category: "评论与评价（Reviews）"
category_slug: "reviews"
wp_url: "https://dynamicycle.com/docs/storereviews/"
wp_modified: "2026-01-12T02:49:05"
---

了解 ****Store Reviews****（也称为站点评价），它们反映的是您的整个品牌而非单一产品，并学习如何在您的店铺中展示它们。

##### 关于 Store Reviews

Klaviyo 中共有两种类型的 Reviews：

- ****Product Reviews：**** 与特定产品关联的评价。
- ****Store Reviews：**** 对您整个公司/品牌的评价。

##### 收集 Store Reviews (Collect Store Reviews)

要启用 ****Store Reviews**** 收集功能：

1. 导航至 ****Reviews > Review settings > Review submission page****。
2. 在 ****Success page****（成功页面）部分，勾选 ****Ask for store review**** 选项。
3. 选择 ****Save changes****（保存更改）。

一旦勾选此选项，如果评价者之前未曾留下过店铺评价，那么在评价提交成功页面上，将会出现一个供其留下 ****Store Reviews**** 的选项。

![Review submission confirmation with a thank you message and an option to edit the review, along with a prompt asking users to rate their shopping experience.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-81.png?resize=1024%2C841&ssl=1)

****Store Reviews**** 会显示在 ****SEO / All Reviews Widget****（SEO/所有评价小组件）中。将此小组件添加到您网站的独立页面上，可以提升 SEO 效果，并为购物者提供一个集中查看所有产品及整个店铺 ****Store Reviews**** 的位置。

##### 审核 Store Reviews

****Store Reviews**** 与产品评价一样，也可以进行****审核****。若要审核您的 ****Store Reviews****：

1.导航至 ****Reviews > All Reviews****。

2.在 ****Type****（类型）下方，勾选 ****Store****；如果已勾选 ****Product****，请取消勾选。

![一个下拉菜单，显示选项 'Store' 用于选择评论类型。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-82.png?resize=488%2C168&ssl=1)

3.检查任何待处理的 ****Store Reviews****。根据需要发布或拒绝它们。

##### 将 Product Review 转换为 Store Review

如果某条产品评价与您的整个店铺相关，您可以将其转换为 ****Store Review****。

1.导航至 ****Reviews > All Reviews****。

2.选择该条评价旁边的三个点（更多选项）图标。

3.选择 ****Save as store review****（保存为店铺评价）。

![显示产品评价选项的下拉菜单，包含保存为产品评价和保存为店铺评价的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-83.png?resize=546%2C470&ssl=1)

4.如果该 Review 尚未与特定产品关联，请在出现的****弹窗****中选择一个产品。 选择该 Review 是应同时作为 Product Review 和 ****Store Review****，还是仅作为 Product Review。 选择 ****Save review****（保存评价）。

##### 导入 Store Reviews

目前支持从 Yotpo、Stamped 和 Okendo 导入 ****Store Reviews****。对于自定义上传（即从其他服务商处上传），请参考下文中的步骤。您可以导入 ****Store Reviews**** 并直接在您的网站上展示（例如在 ****SEO / All Reviews Widget**** 中）。

****要导入 Store Reviews：****

1. 从您之前的服务商处导出 Reviews。
2. 在 Klaviyo 侧边栏点击 ****Reviews****。
3. 导航至 ****All Reviews**** 选项卡。
4. 选择 ****Options****。
5. 点击 ****Import Reviews****。

![Screenshot of the Klaviyo reviews management interface, displaying options for 'Import reviews,' 'View import history,' and 'Export reviews.' The 'All reviews' tab is highlighted, showing a published review for 'Zinnia Seeds' with a star rating.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-84.png?resize=1024%2C244&ssl=1)

选择 ****Stamped****、****Yotpo**** 或 ****Okendo**** 作为您之前的 Reviews 服务商。 按照导入****弹窗****中的步骤操作。 完成这些步骤后，导入文件中所有被标记为 ****Store Reviews**** 的评价都将以 ****Store Reviews**** 的身份出现在 Klaviyo 中。

##### 从其他平台导入 Store Reviews

要从上述列表之外的其他平台导入 ****Store Reviews****， 注意：您需要调整 CSV 文件以匹配此示例格式，否则上传将无法成功。

****请包含以下必填列：****

- ****Product ID (product\_id)**** 必须与您 ****Klaviyo Product Catalog**** 中的产品 ID 完全匹配（最多 255 个字符）；或者，也可以使用 `product_handle`、`product_sku` 或 `product_name` 作为产品标识符。
- ****Reviewer Email (reviewer\_email)**** 必须是有效的电子邮件地址（最多 3,000 个字符）。
- ****Review Score (rating)**** 1-5 的数字，代表客户提交的评分。
- ****Review Creation Date (review\_date)**** 使用[受支持的日期格式]排列的 Review 提交日期。
- ****Review Status (status)**** Review 的状态（即 `Published` 已发布、`Unpublished` 未发布）；未发布的 Reviews 在 Klaviyo 中会被标记为 `Pending`（待处理），直到您批准并发布它们。

即使您的 Reviews 仅针对店铺，Product ID 列也是必填的。如果该 Reviews 与特定产品无关，请将 Product ID 列保持为空。

****根据需要，您可以选择包含以下列：****

- ****Reviewer Display Name (reviewer\_name)**** 通常为“名字 + 姓氏首字母”（例如：Mark R.）（最多 300 个字符）。
- ****Review Content (review\_content)**** 客户提交的评价内容（最多 10,000 个字符）。
- ****Published Image URL (image\_urls)**** 有效的、公众可访问的图片 URL（或多个以逗号分隔的 URL）；Klaviyo 将保存并存储这些图片。
- ****Review Title (review\_title)**** Review 的简短标题（最多 3,000 个字符）。
- ****Review Is Verified Buyer (Yes / No) (verified)**** 评价者是否为已验证买家；仅接受 `Yes` 和 `No`。
- ****Reviewer Country (reviewer\_location)**** 例如：US、UK、Canada、Australia（最多 3,000 个字符）。
- ****Reply Content (reply\_content)**** 您的品牌对客户评价的回复内容（最多 3,000 个字符）。
- ****Reply Date (reply\_date)**** 品牌回复该客户评价的日期。
- ****Store review (true/false) (is\_store\_review)**** 该 Review 是否针对您的整个店铺。接受 `true` 或 `false`。

一旦您按照 Klaviyo 的模板完成了文件格式化，即可进行上传：

1. 从您之前的服务商处导出 Reviews。
2. 在 Klaviyo 侧边栏点击 ****Reviews****。
3. 导航至 ****All Reviews**** 选项卡。
4. 选择 ****Options****。
5. 点击 ****Import Reviews****。

![A display of the reviews management interface in Klaviyo, featuring options for importing, viewing import history, and exporting reviews, along with a highlighted published review.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-85.png?resize=1024%2C244&ssl=1)

选择 ****Other/Not sure**** 作为您之前的 Reviews 服务商。 按照导入****弹窗****中的步骤操作。

##### 展示 Store Reviews

导入 ****Store Reviews**** 后，您必须开启一项设置，以便它们与产品评价一起显示在您的 ****SEO / All Reviews Widget**** 中。

1. 导航至 Klaviyo 中的 ****Reviews****。
2. 点击 ****Reviews settings****。
3. 选择 ****Onsite widgets****。

![显示评论和样式设置界面，包含三个选项：站内小组件、评论提交页面和Google购物同步。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-86.png?resize=1024%2C628&ssl=1)

- 选择 ****SEO / All Reviews Widget****（SEO/所有评价小组件）卡片。
- 点击 ****Store Reviews****。
- 开启 ****Show store reviews****（显示店铺评价）设置。
- 选择 ****Store Reviews**** 的显示位置：****A single list with product reviews****（与产品评价混合在一个列表中）或 ****A separate tab for store reviews****（为店铺评价设置独立选项卡）。

![界面显示店铺评价的设置选项，允许用户选择将店铺评价与产品评价混合在一个列表中或设置为单独的标签。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-87.png?resize=872%2C566&ssl=1)

- 点击Publish changes.

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)