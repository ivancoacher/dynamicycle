---
id: "360058698511"
title: "如何在 Magento 2 结账时收集短信同意"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360058698511-How-to-collect-SMS-consent-at-checkout-on-Magento-2"
section: "Collect SMS consent at checkout"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:53Z"
language: "zh"
---
## 你将会学到

了解如何在 Magento 2 结帐时收集短信同意。

一旦有人提供电话号码、选择短信营销并下订单，同意将同步到 Klaviyo。

## 开始之前

请注意以下有关在结帐时收集短信同意的信息：

- 你必须有
  - [在 Klaviyo 中设置短信](https://klaviyo.zendesk.com/hc/en-us/articles/4404274419355)
  - [创建移动服务条款](https://klaviyo.zendesk.com/hc/en-us/articles/360049177511)
  - 遵循[隐私政策的最佳实践](https://klaviyo.zendesk.com/hc/en-us/articles/4404199571867)
- 您必须使用 [Magento 2 插件版本 2.1.0 或更高版本](https://help.klaviyo.com/hc/en-us/articles/115005254348) 才能使用此功能
  - 不适用于 Magento 1 商店
- 您只能在[可使用 Klaviyo SMS 的国家/地区收集短信同意书](https://help.klaviyo.com/hc/en-us/articles/4402914866843)

此外，如果您将客户同步到具有双重选择加入的列表，则客户在添加到该列表之前将收到一条确认其订阅的文本。

## 在结账时设置短信同意

1. 导航到您的 Magento 2 商店。
2. 从左侧边栏导航至****商店 > 配置****。 ****！[Magento 导航中突出显示的配置](https://klaviyo.zendesk.com/hc/article_attachments/28720772122651)****
3. 进入 **配置** 页面后，导航至 ****Klaviyo > 结账时同意****。 **！[配置页面中突出显示的“结账时同意”选项](https://klaviyo.zendesk.com/hc/article_attachments/28720772117147)**
4. 展开**短信**部分。
   - 这是一个独立的部分，与收集电子邮件同意的部分不同。
5. 在 **SMS** 下，为 **在结账时为联系人订阅 SMS 营销** 选择 **是****。
6. 选择您希望 SMS 联系人同步的列表（例如 SMS 订阅者）。
   - 如果您还收集电子邮件订阅者，请选择与电子邮件所用列表不同的 SMS 列表。
7. 可选：编辑 SMS 选择加入复选框的文本。
   - 默认文本如下：
     **订阅短信**
8. 可选：编辑短信同意文本。
   - 默认文本如下：
     **选中此框并在上面输入您的电话号码，即表示您同意通过所提供的号码接收来自[公司名称]的营销短信（例如[促销代码]和[购物车提醒]），包括自动拨号器发送的消息。同意不是任何购买的条件。消息和数据速率可能适用。消息频率各不相同。您可以随时通过回复“停止”或单击我们其中一封消息中的取消订阅链接（如果有）来取消订阅。查看我们的隐私政策 [链接] 和服务条款 [链接]。**
9. 在此披露语言中，替换 **[link]** 占位符，以包含指向您的隐私政策和服务条款页面的直接链接。
   - 示例：
     **查看我们的隐私政策 (<https://www.klaviyo.com/legal/privacy-policy>) 和服务条款 (<https://www.klaviyo.com/legal/terms-of-service>)
     ![在 Magento 商店结账时添加 SMS 同意的配置](https://klaviyo.zendesk.com/hc/article_attachments/28720772127515)**
10. 可选：编辑排序顺序以更改电子邮件和短信同意框的位置。
    - 默认情况下，这些框分别显示在第一个电子邮件输入字段和送货电话号码字段下。
    - 如果您没有重新排列结帐页面，则无需更改排序顺序。如果您更改了布局，请相应地调整排序顺序。
      ![结帐时短信同意处于活动状态时的 Magento 结帐页面示例](https://klaviyo.zendesk.com/hc/article_attachments/28720760346907)
11. 完成后，单击右上角的****保存配置****。

## 结果

现在，当有人添加电话号码、点击短信选择加入复选框并下订单时，他们的同意将同步到 Klaviyo。这使您可以更快速、更轻松地扩大短信列表并通过此渠道接触更多客户。

请注意，只有在他们完成下订单并且（如果适用）通过双重选择确认其订阅后，同意才会同步。

## 其他资源

- 了解如何[编写有影响力的短信副本](https://academy.klaviyo.com/en-us/courses/write-impactful-sms-copy/1823767)
- 了解[同时使用短信和电子邮件的基础知识](https://help.klaviyo.com/hc/en-us/articles/360056849631)