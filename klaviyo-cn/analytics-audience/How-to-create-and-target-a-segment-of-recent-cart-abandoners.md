---
id: "360032334511"
title: "如何创建并定位近期放弃购物车的人群"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360032334511-How-to-create-and-target-a-segment-of-recent-cart-abandoners"
section: "Segment examples and types"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:44Z"
language: "zh"
---
## 你将会学到

了解如何识别最近放弃购物车的网站访问者，以便跨营销渠道定位他们。例如，您可以创建最近的购物车放弃者细分并将其同步到 Facebook 自定义受众以将他们带回您的网站，或者您可以在购物者即将离开您的网站时创建针对他们的退出意图弹出窗口。虽然无法像在废弃购物车电子邮件中那样动态显示某人购物车中留下的特定商品，但您仍然可以使用您使用的语言和 CTA 提醒他们留下的商品。想在某人放弃购物车时向其发送电子邮件吗？查看我们的[创建废弃购物车流程的指南。](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow)应使用流程而不是发送到细分的营销活动来向购物车放弃者发送电子邮件，以便及时向购物者发送购物车中仍保留商品的提醒。 ## 创建最近购物车放弃者的细分

1. 从 Klaviyo 导航菜单导航至****受众 > 列表和细分****。 2. 单击****创建列表/细分****。 3. 选择****段****。 4. 创建一个具有以下定义的段：
   ****某人已完成（或未完成）的操作 > 已开始结账 > 过去 1 周内至少完成一次
   和
   过去 1 周内某人已完成（或未完成）的操作 > 已下订单 > 0 次
   ![最近放弃购物车的网站访问者](https://klaviyo.zendesk.com/hc/article_attachments/28705663512731)****

可以根据您的营销需求调整分段内的时间限制（本例中为 1 周）。由于[具有相对时间条件的分段的工作原理](https://help.klaviyo.com/hc/en-us/articles/115005233488-How-Dynamic-Segments-Update)，该分段不会实时更新，而是每 24 小时更新一次。 ### 您是否使用亚马逊 Prime 购买？如果您使用“Buy with Prime”来支持商店中任何产品的付款和履行，则您应该在细分中添加另一个条件。首先，请确保执行以下操作：

- [将 Buy with Prime 与 Klaviyo 集成](https://klaviyo.zendesk.com/hc/en-us/articles/14708088221467) 将 Buy with Prime 数据引入您的 Klaviyo 帐户。然后：

- 添加另一个 AND，后跟条件 **下订单**（使用 Prime 购买）**过去 1 周内**零次** 添加到上面的细分。 ## 目标购物车放弃者

### 带有退出意向表

使用[注册表单生成器](https://help.klaviyo.com/hc/en-us/articles/360026474752) 设计您希望在某人即将离开您的网站但购物车中仍有商品时显示的表单。您可能需要选择弹出窗口、浮出窗口或整页表单，以便吸引购物者的注意力。在****定位和行为****选项卡中，配置以下设置：

- 在****显示****选项卡上：
  - 在 **计时** 下，配置表单以显示 ****基于规则 > 当访问者退出页面时****。 - 在**频率**下，取消选中**如果提交表单或单击“转到 URL”按钮，则不再显示**。这可以确保有人在多次放弃购物车的情况下多次看到该表格。然后，在**访问者关闭此表单后，在**时间范围后再次显示，以确保购物者不会在同一浏览会话中始终看到此表单。在我们的示例中，我们设置了 30 天的时间范围，之后购物者才会再次看到该表单。 ![表单生成器的“定位和行为”选项卡中的“显示”菜单显示了一个示例表单，该表单设置为在访问者退出页面时显示，并设置为在 30 天后再次显示。](https://klaviyo.zendesk.com/hc/article_attachments/28706697860763)
- 在****定位****选项卡上：
  - 在 **访客** 下，选择 ****显示到列表或细分中的特定个人资料****，然后将表单配置为仅向最近的购物车放弃者细分中的访客显示。 - 作为保护措施，在 **URL** 下，将其排除在订单确认页面上。或者，仅将表单定位到您网站上的某些页面，例如您的主页。 ![表单生成器的“定位和行为”选项卡中的“定位”菜单显示一个示例表单，设置为仅向废弃购物车部分中的访问者显示，并且仅显示在主页 URL 上。](https://klaviyo.zendesk.com/hc/article_attachments/28706697867291)

此外，配置号召性用语 (CTA)，将购物者带回购物车或直接带至结帐页面。单击表单预览中的主 CTA 按钮，然后选择 ****转到 URL**** 作为按钮 **操作**。然后，将结帐或购物车 URL 设置为目标 URL。 ### 在脸书上

您可以使用 Klaviyo 与 Facebook 的集成以类似的方式定位 Facebook 用户。在将近期购物车放弃者的一部分同步到自定义受众之前，请确保您[已设置 Facebook 集成](https://help.klaviyo.com/hc/en-us/articles/115005082127-Integrate-Facebook-Advertising-with-Klaviyo)。配置集成后，您可以将 Klaviyo 中的任何片段同步到 Facebook 自定义受众。如上所述，如果您计划将片段同步到 Facebook 以覆盖更广泛的受众，您可能需要延长该片段的时间范围。按照提示创建新的自定义受众。接下来，在 Facebook 中制作一个广告，向最近放弃购物车的受众展示。更新广告中的 CTA 链接，将购物者引导回购物车、结帐页面或您的常规网站。有关此过程的更多信息，请前往我们的课程[将自有营销与 Facebook 广告策略相结合](https://academy.klaviyo.com/integrate-owned-marketing-with-your-facebook-advertising-strategy)

## 其他资源

- [高级分割参考](https://klaviyo.zendesk.com/hc/en-us/articles/360035312491)
- [如何创建废弃的购物车流程](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)