---
id: "360058194372"
title: "如何在 BigCommerce 结帐时关闭短信同意"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360058194372-How-to-turn-off-SMS-consent-at-checkout-for-BigCommerce"
section: "BigCommerce best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:54Z"
language: "zh"
---
## 你将会学到

了解如何在 BigCommerce 结帐时停止收集短信同意。

为此，您需要：

1. 从 BigCommerce 中的主题文件中删除代码片段。
2. 取消选中 Klaviyo 中的**收集短信订阅者**框。

## 在 BigCommerce 中

1. 前往您的 BigCommerce 商店。
2. 单击****设置 > 高级 > 数据解决方案****。
3. 查找**站点验证标签**并单击三个点以打开下拉菜单。
4. 从下拉列表中，单击****断开连接****。 ![BigCommerce 中的数据解决方案页面](https://klaviyo.zendesk.com/hc/article_attachments/28713332696603)
5. 在弹出的模式中，单击****断开连接****继续。
   ![断开站点验证标签的模式](https://klaviyo.zendesk.com/hc/article_attachments/28713338341787)

请注意，该脚本仍会显示在**站点验证标签**下；但是，它将不再在您的网站上处于活动状态。一旦您点击****断开连接****，就会停止短信同意收集。 （如果您想完全删除脚本，则必须输入一些其他文本（例如空格或其他脚本。）

## 在克拉维约

1. 在 Klaviyo 中，选择 ****Integrations**** 选项卡，然后单击 ****BigCommerce****。
2. 取消选中****将您的 BigCommerce SMS 订阅者同步到 Klaviyo**** 框**。**
3. 在模式中，单击****停止收集短信同意****。
4. 要保存更改，请单击****保存****。

## 其他资源

- 了解[如何将嵌入式表单添加到您的网站](https://help.klaviyo.com/hc/en-us/articles/360022594552)
- 了解如何[在结帐时重新启用短信同意](https://help.klaviyo.com/hc/en-us/articles/360058194032)