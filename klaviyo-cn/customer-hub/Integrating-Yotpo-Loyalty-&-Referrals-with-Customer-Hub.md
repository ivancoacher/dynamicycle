---
id: "46364536713755"
title: "将 Yotpo 忠诚度和推荐与客户中心集成"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/46364536713755-Integrating-Yotpo-Loyalty-Referrals-with-Customer-Hub"
section: "Integrate other platforms with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:55:02Z"
language: "zh"
---
本文概述了客户中心的 Yotpo 忠诚度和推荐集成，它允许您直接在网站上提供本机忠诚度体验。通过将 Yotpo 与客户中心集成，购物者无需离开商店或与第三方小部件交互即可查看自己的积分、跟踪 VIP 状态并兑换奖励。

## 集成的好处

- ****减少摩擦****：购物者可以完全在客户中心内完成忠诚度操作（例如兑换），减少重定向并保持他们在现场的参与度。
- ****统一的品牌体验****：使用客户中心的基本布局和语音呈现忠诚度信息，创造一个有凝聚力的购买后旅程。
- ****提高可见性****：向登录会员和非会员展示忠诚度价值，以推动计划注册和保留。

## 开始之前

要启用此集成，请确保您拥有：

1. 一个活跃的 Yotpo 忠诚度和推荐帐户。
2. 客户中心位于您的网站上。
3.您的 Yotpo ****API 密钥**** 和 ****GUID****。
4. Yotpo 内管理现有的 Yotpo x Klaviyo 集成，以同步配置文件属性和事件。

## 如何启用 Yotpo 集成

1. 在 Klaviyo 应用程序中，导航至 ****KService > 客户中心****。
2. 打开****扩展设置****页面。
3. 从忠诚度提供商列表中选择 ****Yotpo****。
   ![屏幕截图 2026-02-06 1.38.57 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46364536700955)
4. 在必填字段中输入您的 Yotpo ****API 密钥**** 和 ****GUID****（这些内容将被安全存储以方便后端 API 调用）。
   ![屏幕截图 2026-02-06 1.39.04 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46364536706971)
5.****保存您的更改****。启用后，忠诚度体验将在中心内对您的客户可见。

## 购物体验

Yotpo 集成向客户中心添加了两个主要视图：

### 1.“为你”忠诚总结

当购物者打开客户中心时，他们将看到一个简洁的奖励摘要块。根据他们的状态，他们将看到：

- ****当前积分余额****：他们的实时积分总数。
- ****VIP 等级****：他们当前的会员级别（例如铜牌、银牌、金牌）。
- ****最佳/下一个奖励****：突出显示他们当前有资格获得的最有价值的奖励或他们可以获得的下一个奖励。

![屏幕截图 2026-02-06 1.50.30 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46365040867611)

### 2.奖励页面

为了更深入地了解，购物者可以导航到中心内的专用奖励页面来访问：

- ****赚取方式****：有关如何累积更多积分的信息。
- ****可用奖励****：固定或可变兑换选项列表。
- ****中心内兑换****：购物者可以直接用积分兑换优惠券代码，然后显示该优惠券代码以供立即使用。
- ****推荐链接****：供购物者与朋友分享的独特链接。

![屏幕截图 2026-02-06 1.50.15 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/46365049996187)

## 数据和配置文件属性

该集成利用从 Yotpo 同步到 Klaviyo 的多个配置文件属性来个性化体验：

- `swell_point_balance`：显示客户当前的积分。
- `swell_vip_tier_name`：表示客户当前的等级。
- `swell_referral_link`：提供客户的唯一推荐 URL。
- `swell_has_account`：确定购物者是否是您的忠诚度计划的会员。

Customer Hub 还实时调用 Yotpo 的 API 以获取最新的计划详细信息，例如主动兑换选项和等级定义，确保购物者始终看到准确的数据。