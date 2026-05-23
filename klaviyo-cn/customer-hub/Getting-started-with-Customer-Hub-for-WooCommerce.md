---
id: "47792369863451"
title: "WooCommerce 客户中心入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/47792369863451-Getting-started-with-Customer-Hub-for-WooCommerce"
section: "Getting started with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:56:58Z"
language: "zh"
---
# WooCommerce 客户中心入门

**预计阅读 10 分钟**

## 目录

- [关于客户中心](https://www.google.com/search?q=%23about-customer-hub)
- [开始之前](https://www.google.com/search?q=%23before-you-begin)
- [1.启用客户中心](https://www.google.com/search?q=%231-enable-customer-hub)
- [2.连接您的 WooCommerce 商店](https://www.google.com/search?q=%232-connect-your-woocommerce-store)
- [3.更新您的帐户页面链接](https://www.google.com/search?q=%233-update-your-account-page-link)
- [4.启用扩展程序以定制购物体验](https://www.google.com/search?q=%234-enable-extensions-to-tailor-the-shopping-experience)
- [5.链接您的隐私政策和服务条款](https://www.google.com/search?q=%235-link-your-privacy-policy-and-terms-of-service)
- [6.设置客户中心上线](https://www.google.com/search?q=%236-set-customer-hub-live)
- [7.分析您的表现](https://www.google.com/search?q=%237-analyze-your-performance)
- [常见问题](https://www.google.com/search?q=%23frequently-asked-questions)
- [其他资源](https://www.google.com/search?q=%23additional-resources)

---

## 关于客户中心

客户中心是您的客户管理他们与您的品牌关系的地方。它将传统帐户功能与个性化购物体验相结合，例如将产品保存到收藏夹、显示独特的优惠券以及显示产品推荐。客户中心将所有内容整合到一处，提高与最有价值的营销工具（包括忠诚度计划、订阅等）的互动，从而增加收入并减轻支持负担。客户中心通过 WooCommerce 扩展支持 WooCommerce 店面。由于 WooCommerce 不使用 Klaviyo 的本机 Shopify 应用程序，因此与 Shopify 相比，设置需要一些额外的步骤 - 具体来说，连接您的商店凭据并重定向您的帐户页面链接。 > ****注意：**** 有关客户中心功能的反馈，请发送电子邮件至 customerhub@klaviyo.com。 ---

## 开始之前

在为 WooCommerce 设置客户中心之前，请确认：

- 您有一个与 Klaviyo 集成的活跃 WooCommerce 商店。 - 您可以访问您的 WooCommerce ****消费者密钥**** 和 ****消费者秘密****（从您的 WooCommerce REST API 设置生成）。 - 您拥有 Klaviyo 帐户和 WooCommerce 商店的管理员访问权限。 ---

## 1.启用客户中心

1. 导航至 Klaviyo 主导航中****服务****下的****客户中心****选项卡。 2. 单击****开始**** 开始免费试用和入职流程。在接下来的指导工作流程中，您将：

- 定制您的客户中心的设计和品牌。 - 自定义您的现场小部件以帮助购物者发现您的 Hub。 - 从预先构建的内容块库中将个性化内容添加到您的中心，包括显示忠诚度积分和订阅状态等动态数据的合作伙伴构建的块。 - 基于三种不同身份验证状态的目标购物者：

| ****身份验证状态**** | ****描述**** |
| --- | --- |
| ****已注销**** |没有跟踪历史记录的新访客 |
| ****认可**** |通过“_kx”令牌识别但尚未登录的回头客 |
| ****已登录**** |已完全验证其帐户的购物者 |

完成入职工作流程后，您将进入客户中心仪表板。 ****暂时不要设置客户中心**** — 首先完成步骤 2 和 3，以确保您的 WooCommerce 商店正确连接。 ---

## 2. 连接您的 WooCommerce 商店

由于客户中心通过 WooCommerce REST API 连接到您的商店数据，因此您必须在上线之前提供商店凭据。这使得客户中心可以在中心体验中显示订单历史记录、客户资料和其他商店数据。 ### 生成您的 WooCommerce API 凭据

1. 在 WordPress 管理面板中，导航至 ****WooCommerce > 设置 > 高级 > REST API****。 2. 单击****添加密钥****。 3. 将权限设置为****读/写****并指定一个描述性名称（例如“Klaviyo Customer Hub”）。 4. 单击****生成 API 密钥****。 5. 复制您的****消费者密钥****和****消费者秘密****——这些只会显示一次。 > ****重要提示：**** 在离开此页面之前，请安全存储您的消费者密钥和消费者秘密。 在您离开后，WooCommerce 将不会再次显示消费者机密。 ### 将您的凭据添加到 Klaviyo

1. 在 Klaviyo 中，导航至****客户中心 > 扩展****。 2. 单击****扩展设置****选项卡。 3. 在 WooCommerce 部分下，输入：

   - ****商店 URL 域**** — 您商店的基本域（例如“example.com”）
   - ****消费者密钥**** — WooCommerce 中生成的密钥
   - ****消费者秘密**** — WooCommerce 中生成的秘密
4. 单击****保存****。保存后，Klaviyo 将使用这些凭据从您的 WooCommerce 商店获取订单和客户数据并将其显示在客户中心中。 ---

## 3. 更新您的帐户页面链接

与 Shopify 不同，WooCommerce 不会自动重定向您的“/my-account”页面以打开客户中心。您必须手动更新网站上的帐户页面链接，使其指向客户中心体验。 ### 客户中心如何触发

当购物者导航到以“#k-hub”结尾的 URL 时，客户中心就会打开。要将默认的 WooCommerce 帐户体验替换为客户中心，请更新网站上指向“/my-account”页面的所有链接，以便它们重定向到：

`https://your-store-domain.com/#k-hub`

### 在哪里更新帐户链接

常见的更新位置包括：

- ****导航菜单**** — 网站页眉或页脚中的“我的帐户”或“登录”链接。 - ****主题模板**** — 主题文件中指向“/my-account”的任何硬编码链接。 - ****小部件或短代码**** — 嵌入侧边栏或页面模板中的任何 WooCommerce 帐户小部件。 > ****提示：**** 您可以使用主题的定制器、页面构建器或直接编辑模板文件来更新这些链接。如果您不确定帐户链接出现在网站上的哪个位置，请在主题文件中搜索“/my-account”的引用。 ### 保留特定链接的默认 WooCommerce 帐户体验

如果您有一个链接应该直接打开标准 WooCommerce 帐户页面而不是客户中心，请向该链接添加“data-k-hub-ignore”属性：

超文本标记语言

````
<a href="/my-account" data-k-hub-ignore>查看我的帐户</a>
````

这告诉客户中心跳过该特定链接并允许默认行为。 ---

## 4.启用扩展来定制购物体验

扩展是通过客户中心提高参与度和收入的附加功能。打开****扩展****菜单以启用以下功能：

- ****产品推荐**** — 基于 Klaviyo 的 AI 提供个性化产品推荐。 - ****收藏夹**** — 使购物者能够保存产品并将其显示在客户中心。 - ****优惠券**** — 向购物者展示独特的静态优惠券，包括细分目标，以推动更多转化。 - ****常见问题解答**** — 创建常见问题列表，在购物者发起对话之前显示在“聊天”选项卡中。 - ****网络聊天**** — 添加“聊天”选项卡，并允许购物者通过 Klaviyo 帮助台或支持的帮助台提供商与 Klaviyo 的客户代理和/或人工代理聊天。 - ****支持**** — 允许购物者从订单详细信息页面单击“获取帮助”，方法是将他们引导至 Klaviyo Helpdesk、外部帮助页面链接、Gorgias 聊天，或完全隐藏该选项。 > ****注意：**** WooCommerce 店面目前不支持评论、忠诚度 (Smile.io / Yotpo)、订阅管理、订单跟踪（第三方）和退货管理。 ---

## 5.链接您的隐私政策和服务条款

为了保持合规性并告知购物者有关管理其与客户中心互动的条款，请在客户中心设置菜单中添加指向您网站的隐私政策和服务条款的链接。这些链接会在购物者登录之前以及发送网络聊天消息之前出现。 ---

## 6. 启用客户中心

在发布之前，使用****查看实时****按钮预览并测试所有添加的功能是否按预期工作，尤其是来自 WooCommerce 商店的订单数据。当您准备好发布时：

1. 导航至****客户中心设置****菜单。 2. 在**客户中心可见性**下，选择****实时 > 保存****。一旦上线，所有保存的更改都会立即应用于现场体验。 ---

## 7. 分析你的表现

客户中心上线后，请在客户中心仪表板上监控其性能。 查看关键收入指标和报告以了解客户帐户体验的价值，并使用此数据来告知您如何针对特定客户群定制客户中心。 ---

## 常见问题

### 我的客户如何发现或打开客户中心？当客户中心设置为“实时”并且您的帐户页面链接已更新（请参阅步骤 3）时，任何指向“/#k-hub”的链接都将打开客户中心。我们还建议启用客户中心小部件以推动持续参与。 ### 为什么当购物者点击“我的帐户”时，客户中心不会自动打开？与 Shopify 不同，WooCommerce 不使用可以自动拦截帐户页面链接的本机 Klaviyo 应用程序。您需要手动更新帐户页面链接以指向“/#k-hub”而不是“/my-account”。详细信息请参见步骤 3。 ### 为什么有些购物者无需登录就能看到自己的姓名和最近的订单？客户中心使用 Klaviyo 的“识别状态”通过浏览器令牌识别回头客。这可以提供长达 28 天的个性化体验（例如显示收藏夹列表）。在购物者完成完整登录之前，完整地址和付款方式等敏感信息将保持隐藏状态。 ### 客户中心从 WooCommerce 提取哪些订单数据？客户中心使用 WooCommerce REST API 来获取订单历史记录、订单状态和客户资料数据。确保您的消费者密钥具有读/写权限，以允许客户中心准确显示此数据。 ### 在哪里可以找到我的 WooCommerce 消费者密钥和消费者秘密？在 WordPress 管理面板中，导航至 ****WooCommerce > 设置 > 高级 > REST API****。如果您尚未生成凭据，请单击****添加密钥****并按照提示操作。请注意，消费者秘密仅在生成时显示一次。