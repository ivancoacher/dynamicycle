---
id: "4425956184731"
title: "如何为 Shopify 启用现场跟踪"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/4425956184731-How-to-enable-onsite-tracking-for-Shopify"
section: "Shopify troubleshooting"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-15T09:38:02Z"
language: "zh"
---
## 你将会学到

了解如何在您的 Shopify 商店中启用 Klaviyo 现场跟踪，其中包括多个事件来帮助您吸引可识别的浏览器。此外，启用现场跟踪允许您在网站上使用 Klaviyo 注册表单。 ## 开始之前

在启用应用程序嵌入之前，请确保您已[将 Shopify 与 Klaviyo 集成](https://help.klaviyo.com/hc/en-us/articles/115005080407)。集成时，请注意，启用“从 Shopify 同步数据”和“将数据同步到 Shopify”中的设置将帮助您在帐户中看到更多现场跟踪事件，因为更多配置文件同步。此外，请注意以下事项：

- 您可以随时启用应用程序嵌入和现场跟踪设置，无论您何时集成。 - 您的 Klaviyo 帐户的应用嵌入只能与 1 个 Shopify 商店关联。 - 您最近是否在 Shopify 商店中添加了全新主题？如果是这样，您需要按照本文中的说明重新启用应用程序嵌入。根据您在 Shopify 中的客户隐私设置，Klaviyo 可能不会跟踪欧盟、欧洲经济区、英国和瑞士的 Shopify 商店访客的现场活动，除非他们同意。 ## 关于 Shopify 现场跟踪

通过打开 Shopify 中嵌入的应用程序并确保在 Klaviyo 中选择某些设置来启用 Klaviyo 现场跟踪。我们跟踪以下事件：

- ****现场活跃****
  当有人访问您的商店时触发。此活动可帮助您根据参与度对联系人进行细分。 - ****查看产品****
  当有人查看您商店中的产品页面时触发。使用此事件向[浏览放弃流程](https://help.klaviyo.com/hc/en-us/articles/115002775252)中的客户发送提醒。 - ****查看收藏****
  当有人查看您商店中的产品系列时触发。 - ****已提交搜索****
  当有人在您的商店中提交搜索时触发。 - ****已添加到购物车****
  当有人将商品添加到购物车时触发。上述所有事件在同步到 Klaviyo 时都会带有 Shopify 图标，但**在网站上活动**和**查看的产品**除外，它们具有齿轮图标。 Shopify 品牌的跟踪事件通过 Shopify 像素进行跟踪，而齿轮事件则由 Klaviyo 通过我们嵌入的应用程序安装的代码片段进行跟踪：
- 了解 [Shopify 跟踪对象](https://help.klaviyo.com/hc/en-us/articles/28709780787355#h_01J9236790CK2WW8WMZFD8QS17)（Shopify 图标）
- 了解 [Klaviyo 跟踪的人](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACVVC4BXQ0ES5Y50TC)（齿轮图标）

## 在 Shopify 中启用 Klaviyo 应用嵌入

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 单击****Shopify**** 访问集成设置页面。 3. 在**现场跟踪**部分中，选中****跟踪行为事件****以启用对**查看的集合**、**提交的搜索**和**添加到购物车**的跟踪。请注意，默认情况下启用**查看的产品**，因此一旦您启用应用程序嵌入以及**在网站上活动**，它将开始跟踪。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28707968856347)
4. 您将看到一条消息，指出您的 Klaviyo 应用程序嵌入已关闭。单击****打开****即可进入 Shopify。 5. 如果出现提示，请使用您与 Klaviyo 集成的帐户登录 Shopify。 6. 您将进入主题设置的“应用程序嵌入”选项卡。确保 Klaviyo 应用程序嵌入已打开。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28707972485275)
7. 在主题编辑器中单击****保存****。 8. 导航回到 Klaviyo 中的 Shopify 集成设置页面，并根据需要刷新页面。您应该会看到一个绿色横幅，表明您的应用程序嵌入现已启用。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28707972494235)

## 测试 **现场活动** 和 **查看的产品** 跟踪

**现场活跃**和**查看产品**事件通过 Klaviyo 应用程序嵌入进行跟踪。启用现场跟踪事件后，在开始同步之前可能会有一小段延迟。我们建议在测试前等待 15 分钟。要确认现场跟踪是否有效，请按照以下步骤操作：

1. 导航到您的 Shopify 网站。 2. 在您的主页上，将以下内容添加到 URL 末尾，并将 **example@gmail.com** 替换为您的电子邮件地址：
   `?utm_email=example@gmail.com`
3. 重新加载页面。 4. 导航至您网站上的产品页面。 5. 返回 Klaviyo 并搜索您的电子邮件地址。 您将看到已为您创建了 Klaviyo 个人资料（如果尚不存在），并且已在您的活动源上跟踪了**网站活跃**和**查看的产品**指标。 ## 测试 **添加到购物车**、**查看的收藏** 和 **提交的搜索** 跟踪

**添加到购物车**、**查看收藏品**和**提交搜索**事件通过 Shopify 像素进行跟踪。如果个人资料执行以下操作之一，他们将被识别：

- 提交 Klaviyo 表格。 - 您必须启用将配置文件从 Klaviyo 同步到 Shopify 才能正常工作。 - 提交 Shopify 表单。 - 在结账页面输入他们的信息。 - 在结账页面登录他们的商店帐户。 - 登录商店的客户帐户。您可以完成上述项目之一，然后采取所需的操作，以便测试对每个事件的跟踪。 ## 结果

您现在已在 Shopify 商店中启用并测试了 Klaviyo 现场跟踪。