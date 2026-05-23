---
id: "18229698831003"
title: "如何将 Klaviyo 嵌入表单添加到您的 Square Online 网站"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18229698831003-How-to-add-a-Klaviyo-embed-form-to-your-Square-Online-site"
section: "Square"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: "zh"
---
## 你将会学到

了解如何将 Klaviyo 嵌入表单添加到您的 Square Online 网站，这需要在 Klaviyo 中创建一个表单，然后将其嵌入代码粘贴到您希望其显示的网站文件中（例如页脚）。

## 开始之前

在 Klaviyo 中创建嵌入表单之前，请确保您已将 Klaviyo 与 Square 集成并设置现场跟踪以启用注册表单功能。如果您在[与 Square 集成](https://help.klaviyo.com/hc/en-us/articles/11117215837211) 时选中了 **自动添加 Klaviyo 现场 JavaScript** 设置，则一切就绪。

如果没有：

1. 在 Klaviyo 中，选择****集成****选项卡。
2. 单击****方形****。
3. 检查设置 **自动添加 Klaviyo 现场 javascript**。
4. 单击****保存****。

## 将表单的嵌入代码添加到您的网站

首先，在 Klaviyo 中创建并发布您的嵌入表单。本节将介绍将表单的嵌入代码粘贴到 Square Online 网站上的后续步骤，以便正确显示和同步数据。

1. 导航到 Square Online 仪表板。
2. 单击****网站 > 编辑站点****。
3. 打开您要嵌入表单的页面。
4. 选择****添加部分 > 嵌入代码****，然后单击****添加****。
5. 复制以下脚本并将其粘贴到 **代码** 框中：

   ````
   <script type="text/javascript" src="https://static.klaviyo.com/onsite/js/PUBLIC_API_KEY/klaviyo.js"></script>
   ````
6. 在您刚刚粘贴的代码中，将 PUBLIC\_API\_KEY 替换为您的 [Klaviyo 公共 API 密钥。](https://help.klaviyo.com/hc/en-us/articles/115005062267#find-your-api-keys2)
   - 要查找您的公共 API 密钥，请导航至 Klaviyo 中的 ****设置 > API 密钥****。这是一个 6 字符代码，也称为您的“帐户 ID”。
7. 导航回 Klaviyo 并从表单编辑器内的 **定位和行为** 选项卡复制表单的嵌入代码。
   ![突出显示示例表单的嵌入代码，以从表单编辑器的“定位和行为”选项卡复制。](https://klaviyo.zendesk.com/hc/article_attachments/32015281228443)
8. 在 Square 中，将嵌入代码粘贴到您在步骤 5 中粘贴其他脚本的位置下方的 **代码** 框中。
9. 选择****完成****。
10. 选择****发布**** 保存您的更改。

在 Square 中粘贴嵌入代码并保存更改后，导航回您的网站并刷新页面。您的嵌入表单将显示在您的网站上，并将新订阅者直接添加到链接到该表单的 Klaviyo 列表中。

如果您没有看到表单，请参阅[嵌入表单疑难解答](https://help.klaviyo.com/hc/en-us/articles/360006897412#h_01JFAQY2NHMG3PPV523K4ESXEV)。

如果您决定断开 Square 集成，则需要从 Square Online 网站编辑器中手动删除此嵌入代码以删除您的表单。

## 后续步骤

接下来，[创建欢迎系列](https://help.klaviyo.com/hc/en-us/articles/115002775172)，以立即对您的新订阅者产生影响。

## 其他资源

- [Square 入门](https://help.klaviyo.com/hc/en-us/articles/11117215837211)
- [如何嵌入注册表单](https://klaviyo.zendesk.com/hc/en-us/articles/360006897412)
- [如何验证注册表单是否已启用](https://klaviyo.zendesk.com/hc/en-us/articles/360002035871)