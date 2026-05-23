---
id: "7954040204827"
title: "如何在库存流程中使用短信"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/7954040204827-How-to-use-SMS-in-your-back-in-stock-flows"
section: "Revenue-generating SMS flows"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:05Z"
language: "zh"
---
## 你将会学到

了解如何通过 Klaviyo 在库存流中使用短信。通过将短信添加到您的库存流中，您可以立即提醒订阅者他们感兴趣的产品。库存消息会营造一种紧迫感，促使您的收件人在收到短信后立即购买。短信通常会在 3 分钟内被阅读，并且比电子邮件更快地被看到，这使其成为库存消息的最佳选择。 ## 开始之前

在将 SMS 添加到库存流中之前，请注意以下事项：

- 您的 Klaviyo 帐户必须已[打开短信](https://help.klaviyo.com/hc/en-us/articles/4404274419355)。 - 个人必须是当前的短信订阅者才能从库存流中接收短信
- 库存流中的 SMS 回复仅适用于 Shopify、BigCommerce、PrestaShop 和 Magento 2 商店，以及具有通过自定义目录源或 API 同步的库存感知目录的商店。 - 您必须已为您的电子商务商店设置了库存：
  - [Shopify 补货说明](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
  - [BigCommerce 补货说明](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
  - [PrestaShop 补货说明](https://help.klaviyo.com/hc/en-us/articles/33059375555099)
  - [Magento 2 重新有货](https://developers.klaviyo.com/en/docs/set-up-back-in-stock-for-magento-2)
  - [库存中的自定义目录反馈](https://developers.klaviyo.com/en/docs/how-to-enable-back-in-stock-for-custom-catalog-feeds)
  - [API 重新有货](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)
- 将库存流中的短信数量限制为 1 或 2 条。 ## 在库存流程中使用短信

在库存流程中使用 SMS 有 2 个选项：

- 在流程中同时使用短信和电子邮件（推荐）
- 在库存流程中创建一个单独的、仅通过短信返回的流程

  这些选项具有类似的设置；主要区别在于：
- 第一种方法更加全渠道，并且更容易分析受众对短信和电子邮件的反应
- 对于仅短信流程，您需要配置[返回库存流程的设置](https://help.klaviyo.com/hc/en-us/articles/115003872251)（例如，最低库存和客户通知规则）

由于全渠道方法更容易维护、分析和改进，因此我们在本文中仅讨论该方法。 ### 将短信添加到库存流程中

1. 导航至****流****选项卡。 2. 要么：
   1. 找到您现有的库存流（如果您之前创建过）。 2. 搜索库存流回模板：
      1. 点击****创建流程****
      2.搜索“有货”
      3. 在库存流中选择后面一项
      4. 为模态中的流程命名
      5. 单击****使用模板****
3. 在延迟返货后添加有条件拆分。 ![有条件的分割直接放置在“库存延迟”下方](https://klaviyo.zendesk.com/hc/article_attachments/28715964512667)
4. 将分割设置为**如果某人可以或不能接收营销>无法接收>短信营销**。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33955881875483)
5. 单击“****保存****”进行条件拆分。 6. 将 SMS 消息拖至 **否** 路径。 ![](https://klaviyo.zendesk.com/hc/article_attachments/33955881878427)
7. 选择短信，然后单击 **内容** 旁边的 ****编辑 .****
8. 添加您的内容：

   - 示例：“[商品名称] 又有货了！在它们再次消失之前购买您的商品：
     - 要动态插入产品名称，必须使用事件变量。查看这篇文章，了解有关[查找事件变量和示例]的说明。](https://help.klaviyo.com/hc/en-us/articles/115002779071)![](https://klaviyo.zendesk.com/hc/article_attachments/33955910919067)
9. 在文本后面，插入库存商品的目录标签。 - 注意：目录标签特定于您的集成；例如，点击下面您的电子商务平台的名称：

****大商务****

|  |  |
| --- | --- |
| ****产品详情**** | ****动态事件变量（BigCommerce 商店）**** |
| **产品标题** | {% 目录事件.VariantId 集成='bigcommerce' %} {{ 目录\_item.title }} {% endcatalog %} |
| **变体图像** | {% 目录事件.VariantId 集成='bigcommerce' %} {{ 目录\_item.variant.featured\_image.full.src|默认:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **产品网址** | {% 目录事件.VariantId 集成='bigcommerce' %}{{ 目录\_item.url }}{% endcatalog %} |
| **产品价格** | {% 目录事件.VariantId 集成='bigcommerce' %}{% 货币\_format 目录\_item.metadata.price|floatformat:2 %}{% endcatalog %} |
| **变体标题** | {% 目录事件.VariantId 集成 =“bigcommerce” %} {{ 目录\_item.variant.title }} {% endcatalog %} |
| **变体网址** | {% 目录事件.VariantId 集成='bigcommerce' %}{{ 目录\_item.url }}?variant={{ 目录\_item.variant.id }}{% endcatalog %} |

- ****Shopify****

  |  |  |
  | --- | --- |
  | ****产品详情**** | ****动态事件变量（Shopify 商店）**** |
  | **产品标题** | {% 目录事件.VariantId 集成='shopify' %} {{ 目录\_item.title }} {% endcatalog %} |
  | **变体图像** | {% 目录事件.VariantId 集成='shopify' %} {{ 目录\_item.variant.featured\_image.full.src|默认:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
  | **产品网址** | {% 目录事件.VariantId 集成='shopify' %}{{ 目录\_item.url }}{% endcatalog %} |
  | **产品价格** | {% 目录事件.VariantId 集成='shopify' %}{% 货币\_format 目录\_item.variant.price|floatformat:2 %}{% endcatalog %} |
  | **变体标题** | {% 目录事件.VariantId 集成 =“shopify” %} {{ 目录\_item.variant.title }} {% endcatalog %} |
  | **变体网址** | {% 目录事件.VariantId 集成='shopify' %}{{ 目录\_item.url }}?variant={{ 目录\_item.variant.id }}{% endcatalog %} |
- ****Magento 2****

|  |  |
| --- | --- |
| ****产品详情**** | ****动态事件变量（Magento 2 商店）**** |
| **产品标题** | {% 目录事件.VariantId 集成='magento\_two' %} {{ 目录\_item.title }} {% endcatalog %} |
| **变体图像** | {% 目录事件.VariantId 集成='magento\_two' %} {{ 目录\_item.variant.featured\_image.full.src|默认:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **产品网址** | {% 目录事件.VariantId 集成='magento\_two' %}{{ 目录\_item.url }}{% endcatalog %} |
| **产品价格** | {% 目录事件.VariantId 集成='magento\_two' %}{% 货币\_format 目录\_item.variant.price|floatformat:2 %}{% endcatalog %} |
| **变体标题** | {% 目录事件.VariantId 集成 = "magento\_two" %} {{ 目录\_item.variant.title }} {% endcatalog %} |
| **变体网址** | {% 目录事件.VariantId 集成='magento\_two' %}{{ 目录\_item.url }}?variant={{ 目录\_item.variant.id }}{% endcatalog %} |

1. 点击****预览&测试****测试回货短信。 2. 确认库存恢复消息按预期显示后，单击右上角的****保存并继续****。 3. 选择****更新操作状态****。 4. 从下拉列表中选择****Live****，然后单击****Update****。 ![选择 Live 时更新所有流程操作状态的模式](https://klaviyo.zendesk.com/hc/article_attachments/28715971073051)

## 结果和后续步骤

您现在可以通过短信发回库存流消息。 ### 优化流程

我们建议密切关注您的受众对这些消息的反应，因为确保您看到高参与度非常重要。如果参与度较低，请测试您的受众更喜欢电子邮件还是短信。每个企业都是独一无二的，其受众也是如此。您的受众可能更喜欢通过电子邮件而不是短信接收库存提醒。