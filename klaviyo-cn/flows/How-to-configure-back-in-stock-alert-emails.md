---
id: "360051612751"
title: "如何配置缺货提醒电子邮件"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360051612751-How-to-configure-back-in-stock-alert-emails"
section: "Back in stock flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:54:51Z"
language: "zh"
---
## 你将会学到

了解如何使用预构建模板或为库存流电子邮件配置自定义模板。创建库存流回电子邮件时，设置消息以使其显示正确的产品数据非常重要。 Klaviyo 支持与 Shopify、BigCommerce、Magento 2、PrestaShop、Shopware 和 SFCC 集成的账户以及通过自定义目录源或 API 同步库存感知目录的账户的库存流。以下说明涵盖 Shopify、BigCommerce 和 Magento 2 集成。如果您使用自定义集成，请了解[如何通过 API 设置 back in stock](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)。 ## 开始之前

在为您的补货流程配置补货电子邮件之前，您必须已为您的电子商务商店设置补货：

- [Shopify 补货说明](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
- [BigCommerce 补货说明](https://help.klaviyo.com/hc/en-us/articles/38767539287323)
- [PrestaShop 补货说明](https://help.klaviyo.com/hc/en-us/articles/33059375555099)
- [Magento 2 重新有货](https://developers.klaviyo.com/en/docs/set-up-back-in-stock-for-magento-2)
- [库存中的自定义目录反馈](https://developers.klaviyo.com/en/docs/how-to-enable-back-in-stock-for-custom-catalog-feeds)
- [API 重新有货](https://developers.klaviyo.com/en/docs/how_to_set_up_custom_back_in_stock)

## 使用预先构建的模板

您将在流程库中找到预先构建的库存流程，并配置了默认电子邮件内容。如果您已经构建了自己的流程，为了帮助您入门，您将在**电子邮件模板**选项卡中找到预先构建的库存电子邮件模板。配置库存提醒电子邮件时，只需搜索“有货”即可。 ## 创建您自己的库存电子邮件

要配置电子邮件内容，您将需要使用一组特定的动态事件变量。鉴于商品可能需要数天、数周甚至数月才能重新进货，我们意识到该商品的详细信息（例如图像或价格）可能会发生变化。因此，Klaviyo 为此电子邮件使用一组特殊的动态事件变量，该变量将在发送时在您的目录中查找重新进货的产品，并填充可用的最新详细信息。请注意，电子邮件模板中的表块必须设置为静态而不是动态才能正常运行。 ### Shopify 商店

|  |  |
| --- | --- |
| ****产品详情**** | ****动态事件变量（Shopify 商店）**** |
| **产品标题** | {% 目录事件.VariantId 集成='shopify' %} {{ 目录\_item.title }} {% endcatalog %} |
| **产品网址** | {% 目录事件.VariantId 集成='shopify' %}{{ 目录\_item.url }}{% endcatalog %} |
| **产品价格** | {% 目录事件.VariantId 集成='shopify' %}{% 货币\_format 目录\_item.variant.price|floatformat:2 %}{% endcatalog %} |
| **变体图像** | {% 目录事件.VariantId 集成='shopify' %} {{ 目录\_item.variant.featured\_image.full.src|默认:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **变体标题** | {% 目录事件.VariantId 集成 =“shopify” %} {{ 目录\_item.variant.title }} {% endcatalog %} |
| **变体网址** | {% 目录事件.VariantId 集成='shopify' %}{{ 目录\_item.url }}?variant={{ 目录\_item.variant.id }}{% endcatalog %} |

### BigCommerce 商店

如果您的 BigCommerce 中库存电子邮件中的商品显示不正确，则可能是由于您的某些商品的 VariantID 与 BigCommerce 中其他商品的 ProductID 相匹配而导致。要解决此问题，请在电子邮件中使用下面的动态事件变量时将 VariantID 替换为 ProductID。进行此替换应该可以解决不正确的项目问题，但将不再显示特定于变体的信息。 |  |  |
| --- | --- |
| ****产品详情**** | ****动态事件变量（BigCommerce 商店）**** |
| **产品标题** | {% 目录事件.VariantId 集成='bigcommerce' %} {{ 目录\_item.title }} {% endcatalog %} |
| **产品网址** | {% 目录事件.VariantId 集成='bigcommerce' %}{{ 目录\_item.url }}{% endcatalog %} |
| **产品价格** | {% 目录事件.VariantId 集成='bigcommerce' %}{% 货币\_format 目录\_item.metadata.price|floatformat:2 %}{% endcatalog %} |
| **变体图像** | {% 目录事件.VariantId 集成='bigcommerce' %} {{ 目录\_item.variant.featured\_image.full.src|默认:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **变体标题** | {% 目录事件.VariantId 集成 =“bigcommerce” %} {{ 目录\_item.variant.title }} {% endcatalog %} |
| **变体网址** | {% 目录事件.VariantId 集成='bigcommerce' %}{{ 目录\_item.url }}?variant={{ 目录\_item.variant.id }}{% endcatalog %} |

### Magento 2 商店

|  |  |
| --- | --- |
| ****产品详情**** | ****动态事件变量（Magento 2 商店）**** |
| **产品标题** | {% 目录事件.VariantId 集成='magento\_two' %} {{ 目录\_item.title }} {% endcatalog %} |
| **产品网址** | {% 目录事件.VariantId 集成='magento\_two' %}{{ 目录\_item.url }}{% endcatalog %} |
| **产品价格** | {% 目录事件.VariantId 集成='magento\_two' %}{% 货币\_format 目录\_item.variant.price|floatformat:2 %}{% endcatalog %} |
| **变体图像** | {% 目录事件.VariantId 集成='magento\_two' %} {{ 目录\_item.variant.featured\_image.full.src|默认:catalog\_item.featured\_image.full.src }} {% endcatalog %} |
| **变体标题** | {% 目录事件.VariantId 集成 = "magento\_two" %} {{ 目录\_item.variant.title }} {% endcatalog %} |
| **变体网址** | {% 目录事件.VariantId 集成='magento\_two' %}{{ 目录\_item.url }}?variant={{ 目录\_item.variant.id }}{% endcatalog %} |

### 示例

以下是模板生成器中具有动态事件变量的模板的外观，并与使用真实事件数据预览时相同模板的外观进行了比较：

![内容块的示例，其中图像和文本使用动态事件变量，旁边是预览中填充内容的同一块](https://klaviyo.zendesk.com/hc/article_attachments/28717811792795)

## 其他资源

查看有关库存流量的其他文章

- [如何创建库存流](https://help.klaviyo.com/hc/en-us/articles/115003872251)
- [了解库存流量如何运作](https://help.klaviyo.com/hc/en-us/articles/360051612551)
- [如何在库存流程中使用短信](https://help.klaviyo.com/hc/en-us/articles/7954040204827)

了解有关动态变量的更多信息，请参阅[使用动态事件数据个性化流电子邮件](https://help.klaviyo.com/hc/en-us/articles/115002779071)