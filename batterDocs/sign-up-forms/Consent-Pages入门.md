---
id: 6430
title: "Consent Pages入门"
slug: "consent-pages"
category: "注册表单与渠道（Sign-up Forms + Channels）"
category_slug: "sign-up-forms"
wp_url: "https://dynamicycle.com/docs/consent-pages/"
wp_modified: "2026-01-12T07:00:47"
---

了解与 Klaviyo 列表（Lists）相关的各种同意页面（Consent Pages），包括偏好设置页面（Preferences Page）、订阅页面（Subscribe Page）和退订页面（Unsubscribe Page），以及如何自定义它们。

在您的 Klaviyo 账户中，有一套所有列表默认使用的****账户级同意页面****。这些页面包括您的默认偏好设置页面、订阅页面、电子邮件确认页面和电子邮件退订页面。

您可以编辑样式和设计，使账户默认同意页面的外观标准化，以获得一致的品牌体验。但是，如果您希望某个特定列表拥有自己的同意页面（例如，为您的 VIP 列表设置专属的订阅页面），您可以将该列表与默认页面断开连接，并为该特定列表自定义一套唯一的同意页面。

本文将涵盖如何在 Klaviyo 内部使用和管理同意页面；但是，如果您更愿意设计自己的自定义代码页面，可以探索 ****Klaviyo 的托管页面（Hosted Pages）功能****。导航至 ****Settings > Other > Hosted pages**** 可启用此功能。只有通过了账户验证的付费计划账户才能访问此设置。

##### 关于邮件中的同意页面

您的账户默认同意页面在以下情况中会被默认使用：

- 发送至Segments的邮件
- 同时发送至多个列表和/或细分群体的邮件
- 由细分群体触发的Flows
- 由Event触发的自动化流
- 由日期触发的自动化流
- 降价（Price drop）触发的Flows

这意味着，当您在发送给Segment的Campaign中插入退订标签 `{% unsubscribe %}` 或偏好管理标签 `{% manage_preferences %}` 时，将使用账户默认的同意页面。对于由事件触发的流邮件，插入这些标签时的逻辑也是一样的。

如果您在邮件中将偏好管理标签添加为文本链接，请使用 `{% manage_preferences %}`。但是，如果您是将偏好管理标签添加到邮件中的****按钮****或****图片****，则必须使用 `{% manage_preferences_link %}`。

当您向一个使用了自定义同意页面的List发送邮件时，将不会使用默认同意页面。相反，系统会使用您为该特定列表创建的自定义同意页面。若要进一步编辑这些页面，请导航至您想要编辑的列表，然后选择 ****Subscribe and preference pages****。

虽然账户默认同意页面有助于为订阅者集中提供一致的体验，但为特定列表自定义唯一的一套页面通常也很有帮助。例如，如果某个特定List是用于****特别竞赛或订阅者优惠****，您可能希望该列表的同意页面呈现特定的外观，并显示一组独特的订阅者偏好选项。

##### 查找您的账户默认同意页面

要导航至您的默认同意页面：

1. 在 Klaviyo 中，导航至 ****Audience > Growth tools****。
2. 选择 ****Customize subscribe and preferences pages****。
3. 选择 ****Account default pages****。

可编辑的页面包括：

![Klaviyo 同意页面管理界面，包括偏好设置页面、订阅页面、电子邮件确认页面和退订页面的编辑选项](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-88.png?resize=1024%2C775&ssl=1)

##### 偏好设置页面 (Preference Pages)

- ****偏好设置页面 (Preferences Page)**** 现有订阅者可以更新其偏好信息的页面。在这里，您可以让订阅者分享更多信息，如年龄、性别或生日，也可以提供更详细的选项，如首选邮件频率或感兴趣的产品。在偏好设置页面上收集的信息将显示在访问者的个人 Profile 中。
- ****偏好设置成功页面 (Preferences Success Page)**** 订阅者在更新完偏好信息后看到的确认页面。

##### 订阅页面 (Subscribe Pages)

- ****订阅页面 (Subscribe Page)**** 感兴趣的购物者可以注册以接收品牌信息的页面。如果您的列表使用单次确认（Single Opt-in），订阅者在提交****弹窗****后会直接跳转到订阅成功页面。对于双重确认（Double Opt-in）列表，订阅者会先看到一个确认页面，然后需要在确认邮件中点击确认，最后才会被引导至订阅成功页面。
- ****确认页面 (Confirmation Page)**** 如果您的列表是双重确认，这是新订阅者在提交订阅页面后看到的页面，指示他们检查邮件以确认订阅。请注意，只有付费账户才能在此页面上添加或编辑链接及源代码。

##### 邮件确认页面 (Email Confirmation Pages)

- ****确认邮件 (Confirmation Email)**** 针对双重确认列表，这是在用户通过订阅页面或注册****弹窗****订阅后发送给他们的邮件。邮件包含一个按钮，点击后将跳转至订阅成功页面。请注意，只有付费账户才能在邮件中添加或编辑链接及源代码。
- ****订阅成功页面 (Subscribe Success Page)**** 订阅者通过订阅页面完成注册后看到的页面。默认情况下，此页面包含一个指向偏好设置页面的链接按钮，允许新订阅者管理其偏好。请注意，如果有人重复填写订阅页面，管理偏好的按钮将不会出现，因为系统不会创建新的 Profile。

##### 邮件退订页面 (Email Unsubscribe Pages)

- ****邮件退订页面 (Email Unsubscribe Page)**** 当有人点击邮件中的退订链接时看到的页面。默认的邮件退订页面底部包含一个指向偏好设置页面的链接。结合使用退订页面和偏好管理页面，可以鼓励接收者修改其邮件接收偏好，而不是完全退订。
- ****邮件退订成功页面 (Email Unsubscribe Success Page)**** 用户在成功退订邮件后看到的页面。在账户退订成功页面上，按钮设置会显示“主要操作（Primary Action）”和“次要操作（Secondary Action）”。当特定列表使用此页面时，次要操作才会生效。例如，如果一个列表使用默认同意页面而非自定义页面，该列表的订阅者在点击按钮时将看到次要操作（例如：重新订阅 Resubscribe）。

![图像显示了一个电子邮件退订页面，包含一个主要按钮，指向网站链接，以及一个次要按钮，允许用户重新订阅。页面上有一条消息，指出用户已经成功退订，并提供了重新订阅的说明。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-89.png?resize=1024%2C572&ssl=1)

上述列出的这些同意页面（Consent Pages）在您构建用于向列表添加新订阅者的注册****弹窗****时会发挥作用。通过审查和更新这些页面，您可以掌控订阅者在首次加入、更新偏好以及退订时看到的体验和信息。

当您选择创建一个新列表时，每个列表都将默认使用您账户的默认同意页面。

##### 为特定列表自定义同意页面

您可以选择将列表与默认同意页面断开连接，转而为特定列表自定义一套唯一的同意页面。请按照以下步骤为列表进行自定义：

1. 导航至 ****Audience > Growth tools****。
2. 选择 ****Customize subscribe and preferences pages****。
3. 选择 ****For a specific list****（针对特定列表）。
4. 选择 ****Unlink and customize****（取消关联并自定义）以覆盖默认页面。
5. 在这里，您将看到一套可供编辑的新同意页面。找到您想要编辑的页面（例如：偏好设置页面 Preferences Page），点击 ****Edit Page****。
6. 在编辑器中完成页面自定义后，点击 ****Publish****。

##### 编辑同意页面的设计

无论是您的账户默认同意页面，还是某个特定列表的唯一页面集，您都可以自定义每个页面的样式和设计，从而为网站访问者提供一致且符合品牌形象的体验。

如果您更倾向于使用自定义代码来编写偏好设置、订阅或退订页面，请点击下拉箭头并选择 ****Use Hosted Page****（使用托管页面）。

找到您想要编辑的同意页面（例如：偏好设置页面 Preferences Page），点击 ****Edit Page****。

选择某个同意页面后将进入其相应的编辑器，您可以在此处自定义样式和设计以匹配您的品牌。您可以选择编辑以下内容：

- ****样式 (Styles)**** 使用此部分来编辑设计设置，例如 ****Form Background****（****弹窗****背景）、****Page Background****（页面背景）、****Form Styles****（****弹窗****样式）等。
- ****添加模块 (Add Blocks)**** 使用此部分向您的同意页面添加元素，例如文字或图片模块。您还可以通过点击预览界面中的任何文本，将默认文本替换为您自己的内容。

![一个电子邮件偏好设置页面，包含输入电子邮件和姓名的字段，以及选择接收邮件类型的复选框和更新偏好的按钮。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-90.png?resize=1024%2C704&ssl=1)

****按钮 (Button)**** 点击预览界面中的按钮（例如：****Unsubscribe**** 退订按钮或 ****Update your preferences**** 更新偏好按钮），即可看到编辑 ****Button Text****（按钮文本）、****Button Styles****（按钮样式）和 ****Block styles****（模块样式）的选项。

![An interface showing settings for a button, including options for button click action, button text, button styles, and block styles.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-91.png?resize=596%2C560&ssl=1)

当您准备好共享您的同意页面时，点击 ****Publish****。

##### 添加 Profile 属性

如果您在同意页面中添加了输入字段（例如：日期字段），请使用 ****Profile property****（Profile 属性）下拉菜单选择对应的属性（例如：生日）。这使得 Klaviyo 能够在访客提交****弹窗****时，在其专用 Profile 中追踪并记录该信息。Klaviyo 支持多种 Profile 属性供您选择，以便将个人信息添加到用户的 Profile 中。

****注意：**** 您不能在一个****弹窗****中的多个输入字段中使用相同的 Profile 属性，因为这会导致追踪问题。例如，如果您在****弹窗****中有两个文本输入字段分别用于收集“名”和“姓”，则每一个字段都必须拥有自己专属的 Profile 属性，如 `First Name`（名）和 `Last Name`（姓）。

![A user interface showing a text input configuration with fields for label text, placeholder text, profile property selection, and a hint.](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-92.png?resize=584%2C474&ssl=1)

##### 将同意页面翻译成不同语言

如果您的客户群由使用不同母语的人组成，那么创建他们能够理解的内容至关重要。同意页面上的语言默认为美式英语。如需编辑语言，请按照以下步骤操作：

1. 导航至您想要翻译的任何同意页面的编辑器。
2. 点击预览界面中的任何文本进行编辑。
3. 在左侧出现的菜单中，删除默认文本，然后输入您选择的语言文本。
4. 请注意，您可以点击预览****弹窗****中的任何文本将其自定义为不同的语言，这包括****错误提示信息****和输入字段的****必填项警示文本****。

当您准备好共享您的同意页面时，点击 ****Publish****。

##### 查找您的订阅页面 URL

Klaviyo 会为账户中的每个列表自动创建一个订阅页面，您可以利用该页面让潜在订阅者注册加入您的邮件或短信营销。完成设计编辑后，您可以复制订阅页面的 URL，将其分享在邮件或其他地方，以扩大您的受众规模。

****要查找列表的订阅页面 URL：****

1. 导航至 [****Lists and Segments****。](https://www.klaviyo.com/lists)
2. 选择您的列表。
3. 从菜单栏中选择 ****Sign-up forms****。

![Klaviyo账户中的主要列表设置界面，展示了成员数量、设置、注册表单、偏好设置页面等选项的标签。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-93.png?resize=1024%2C159&ssl=1)

在这里，您将看到与此列表关联的所有****弹窗****。请向下滑动并跳过这些内容，即可找到该列表的订阅页面。

![Klaviyo订阅页面的界面，显示默认偏好设置和订阅页面的选项，以及自定义列表的按钮。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-94.png?resize=1024%2C458&ssl=1)

您的订阅页面 URL 现在已复制到剪贴板，可以随时在营销活动或社交渠道中使用。

##### 将已选择加入的接收者重定向至其他网页

当网站访问者通过双重确认（Double Opt-in）完成订阅并跳转到确认页面时，您可以选择将他们重定向到另一个 URL（例如您网站上的特定页面）。这是最大化利用高意向订阅者所带来的网站流量的绝佳方式。

****要在确认页面中使用重定向 URL：****

- 导航至您的同意页面（这可以是您账户的默认同意页面，也可以是特定列表的同意页面）。
- 在 ****Subscribe Page****（订阅页面）下方，点击 ****Edit Page****。

![Klaviyo 同意页面设置界面的截图，展示偏好设置页面和订阅页面的编辑选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-95.png?resize=1024%2C448&ssl=1)

- 在顶部菜单栏中，选择 ****Success page****（成功页面）。
- 点击 ****Custom Redirect****（自定义重定向）。

![Klaviyo同意页面设置界面，包括样式、重定向和模块添加选项，显示订阅成功消息的预览。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-96.png?resize=1024%2C355&ssl=1)

- 勾选 ****Skip page and redirect****（跳过页面并重定向）复选框。
- 粘贴希望订阅者被重定向到的目标 URL。

![界面展示了自定义重定向设置，选项包括跳过页面并重定向以及输入目标 URL。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-97.png?resize=658%2C344&ssl=1)

- 当您完成所有其他设计编辑后，点击 ****Publish****。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)