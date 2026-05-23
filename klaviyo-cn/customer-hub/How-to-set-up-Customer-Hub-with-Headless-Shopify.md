---
id: "41413854379291"
title: "如何使用 Headless Shopify 设置客户中心"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/41413854379291-How-to-set-up-Customer-Hub-with-Headless-Shopify"
section: "Getting started with Customer Hub"
category: "Customer Hub"
category_slug: "customer-hub"
klaviyo_updated: "2026-04-21T13:54:56Z"
language: "zh"
---
## 你将会学到

您将客户中心连接到无头 Shopify 店面，选择登录方法，然后发布中心，以便购物者可以在站点范围内访问它。客户中心目前支持 Shopify 店面，包括 Shopify Headless。计划提供更多电子商务平台支持。有关客户中心功能的反馈，请发送电子邮件至 customerhub@klaviyo.com。 ## 开始之前

### 先决条件

1. 一个无头 Shopify 店面，可以访问 Storefront API（Shopify 无头管理中的公共访问令牌/Storefront API 公钥）。 2. 您的****Klaviyo 公司 ID****（由现场 JavaScript 加载程序使用）。 3. 决定购物者登录：Sh​​opify 客户帐户 API **或** Klaviyo 一次性密码 (OTP)。 1. 如果使用现有帐户，请准备好店面的登录、注销和（可选）管理帐户和管理地址路由。 4. 能够编辑店面代码并部署更改。 5.****谁可以进行此设置：**** 您需要一个可以编辑****客户中心****设置并发布小部件的帐户角色（所有者、管理员或对内容和 API 密钥具有写入权限的自定义角色）。 ## 概述

客户中心是一个全网站覆盖层，使购物者可以更快地访问帐户操作和有用的购物工具。对于无头 Shopify，您可以连接 Klaviyo 的现场脚本，选择登录方法（客户帐户 API 或 Klaviyo OTP），然后选择添加：

1. ****活动产品****：显示购物者正在 Hub 内查看的产品。 2.****最近查看****：使用 Klaviyo 跟踪列出最近查看的产品。 3.****收藏夹****和****常见问题解答****小部件：在 PDP 上和 Hub 内呈现。当您需要页面帮助层来推动产品发现和更快结帐、提高转化率和生命周期价值时，请使用客户中心。 ## 设置

### 1 - 配置客户中心设置

首先，按照[客户中心入门](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675) 并完成入职向导，就像任何其他设置一样。完成后，转到****客户中心 > 设置****。您将看到 Headless Shopify 配置部分。 ![](https://klaviyo.zendesk.com/hc/article_attachments/42187682618011)

打开****Headless Shopify 配置****，然后粘贴来自 Shopify 的 Headless Admin（公共访问令牌）的 Storefront API 公钥。在****购物者登录****下，选择 Shopify 客户帐户 API（推荐，以便您的所有店面应用程序都可以共享 Shopify 的登录信息）**或** Klaviyo 一次性密码（OTP，仅适用于 Klaviyo，不会让购物者登录任何其他应用程序）。 ![](https://klaviyo.zendesk.com/hc/article_attachments/42187686797083)

如果您选择 ****Shopify 客户帐户 API****，还需输入您的店面 ****登录****、****注销**** 和可选的 ****管理帐户****/****管理地址**** 路由（用于在 Hub 和您的站点之间重定向）。 ![](https://klaviyo.zendesk.com/hc/article_attachments/42187682622363)

发布可见性：将****客户中心****设置为****实时****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/42187682624283)

### 2 - 加载客户中心 JavaScript（开发人员说明）

****提示：**** 如果您已经运行 Klaviyo 现场功能，则您可能已经安装了加载程序。添加第二个脚本之前请确认。使用以下加载器创建 /public/customerHub.js （或等效文件）（将 COMPANY\_ID 替换为您的 Klaviyo [公共 API 密钥](https://klaviyo.zendesk.com/hc/en-us/articles/115005062267)，也称为您的公司 ID）：

````
// customerHub.js
// TODO：配置
常量 COMPANY_ID = '';
const script = document.createElement('script');
script.src = `https://static.klaviyo.com/onsite/js/${COMPANY_ID}/klaviyo.js`;
script.async = true;
script.onload = () => { console.log('Klaviyo JS 脚本加载成功'); };
script.onerror = () => { console.error('无法加载 Klaviyo JS 脚本'); };
document.body.appendChild(脚本);
````

现场脚本加载在每个页面上。查找控制台消息：“Klaviyo JS 脚本加载成功。”在您的根布局（例如 root.tsx）中，包含加载程序：

````
// 根.tsx
返回（
  <html>
    <正文>
      <script src="/customerHub.js" defer></script>
    </正文>
  </html>
）
````

执行此步骤后，window.customerHubApi 将在运行 Hub 的页面上可用。 ### 3 - 在客户中心显示活跃产品

在您的****产品详细信息页面 (PDP)**** 上添加水合物调用，以便当前产品出现在中心中：

![](https://klaviyo.zendesk.com/hc/article_attachments/41414430637979)

````
<!-- products.tsx -->
<脚本类型=“文本/javascript”>
  （函数（）{
    函数 waitForCustomerHubApi() {
      返回新的 Promise((resolve) => {
        常量检查 = () => {
          如果（window.customerHubApi && window.customerHubApi. HydroProduct）{
            解决（）；
          } 否则{
            请求动画帧（检查）；
          }
        };
        检查（）；
      });
    }
    waitForCustomerHubApi().then(() => {
      window.customerHubApi. HydroProduct("your-product-handle");
    });
  })();
</脚本>
````

****T****如果您启用了该功能，Hub 现在应该为购物者在“聊天”选项卡上查看的 PDP 显示附加产品卡。 ### 4 - 在客户中心启用最近查看的产品

实施****查看的产品****跟踪，以便中心可以填充****最近查看的****项目，并且您可以在 Klaviyo 的其他地方使用该指标。以下跟踪代码段也可以直接添加到您的店面，可以在我们的 Klaviyo 开发人员文档中找到说明：[在没有预先构建的 Klaviyo 集成的情况下集成电子商务平台](https://developers.klaviyo.com/en/docs/guide_to_integrating_a_platform_without_a_pre_built_klaviyo_integration#viewed-product-tracking-snippet)。 ![](https://klaviyo.zendesk.com/hc/article_attachments/41414422348059)

### 5 - 启用帐户链接接管

为了通过单击店面标题中的帐户图标来打开 Klaviyo 的客户中心，您需要已有一个引用 /account 链接的现有 a 标签（在这种情况下，我们将自动为您替换它）。或者您也可以手动定义图标链接以指向#k-hub 以打开抽屉。 ![](https://klaviyo.zendesk.com/hc/article_attachments/41414422348699)

### 6 - 使用客户帐户 API 身份验证设置客户中心（推荐）

为了使用您现有店面的客户帐户和身份验证设置，客户中心将要求您向您的店面添加新的 API 路由，该路由将安全地将登录购物者的访问令牌传递到我们的服务。重要的是新的 API 路由已命名，并且可以通过“/api/authenticateCustomerHub”访问。注意：以下代码片段示例适用于 Shopify 的 Hydrogen 框架，更多定制的店面可能需要一些额外的解决方法，但此处将概述一般方法。 ````
// ./app/routes/api.authenticateCustomerHub.js
// TODO：配置
常量 COMPANY_ID = '';
导出异步函数操作({context}) {
  // 从店面上下文中提取客户帐户 API 客户端
  const {customerAccount} = 上下文；
  尝试{
    // 获取当前客户的访问令牌
    const accessToken = 等待 customerAccount.getAccessToken();
    如果（！accessToken）{
      return new Response(JSON.stringify({message: '用户未登录'}), {
        状态：200，
      });
    }
    // 将访问令牌发送到客户中心 API
    常量响应 = 等待获取（
      'https://atlas-app.services.klaviyo.com/api/onsite/headless-shopify-login',
      {
        方法：'POST'，
        标题：{
          '内容类型'：'应用程序/json'，
        },
        正文：JSON.stringify({
          访问令牌：访问令牌，
          公司 ID：COMPANY_ID，
        }),
      },
    ）；
    const responseData = 等待response.text();
    // 返回来自客户中心的实际响应，具有相同的状态代码
    返回新的响应（responseData，{
      状态：响应.状态，
      标题：{
        “内容类型”：
          response.headers.get('内容类型') || '应用程序/json',
      },
    });
  } 捕获（错误）{
    返回新的响应（空，{状态：500}）；
  }
}
````

配置完成后，以及 Klaviyo 设置中定义的店面路由，客户中心将能够链接到您现有的身份验证设置，并为您现有的客户帐户提供无缝入口点。 ### 7 - 添加收藏夹小部件（推荐）

收藏夹和常见问题解答都可以在客户中心抽屉中使用。但是，您也可以在 PDP 上添加这些小部件以提高参与度。 要在 PDP 上和 Hub 内添加收藏夹入口点：

````
// 产品.tsx
// 标识符示例：
// ID：gid://shopify/Product/12345
// 数据产品 ID：12345
const gid = "gid://shopify/Product/12345";
const ProductId = gid.split('/').pop();

返回（
  <div
    类名=“kl-hub-favorites-slot”
    数据产品 ID={产品 ID}
  />
）
````

购物者现在可以在 PDP 上单击“****添加到收藏夹****”；该项目出现在中心的****最喜爱的项目****中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/41414422349723)

### 8 - 添加常见问题解答块（推荐）

与添加收藏夹类似，添加 [常见问题解答块](https://klaviyo.zendesk.com/hc/en-us/articles/36400427885979) 就像在产品页面上添加一个 div 并传入其产品 ID 一样简单，以呈现您可以在 Klaviyo 中编辑和设计的常见问题解答。添加您在 Klaviyo 中设计的产品特定常见问题解答块：

````
// 产品.tsx
// 示例：
const gid = "gid://shopify/Product/12345";
const ProductId = gid.split('/').pop();

返回（
  <div className="klaviyo-faqs-slot" data-product-id={productId} />
）
````

常见问题解答芯片/按钮现在应该在 PDP 上呈现（如果已设置），并且可以在 Klaviyo 中进行编辑

## 最佳实践

1. ****仅在验证后才发布到生产环境**** — 保持暂存隐藏状态，直到 QA 完成；然后设置****Live****以暴露集线器。影响：支持问题更少，价值实现时间更快。 2. ****始终与 PDP 上的活性产品水合**** — 使产品上下文在中心中可见并推动添加到购物车。影响：转化率、RPR。 3. ****尽早实施查看的产品跟踪**** — 填充最近查看的内容并解锁基于浏览的流程。影响：浏览恢复带来的参与度和收入。 4. **添加收藏夹**** — 创建一个低摩擦的保存操作和一个持久的候选列表。影响：重复访问、添加到购物车。 5. ****使用异议常见问题解答**** — 在线回答运输、材料或退货问题，以减少流失。影响：转化率。 6. ****首选使用客户帐户 API 进行服务器端身份验证****（如果可用）——提高登录购物者的连续性。影响：体验质量、支撑偏转。 ## 衡量成功

****在哪里查看结果：**** 使用****分析>指标****来监控****查看的产品****活动和下游流量/营销活动绩效。启用客户中心后，使用电子商务收入仪表板跟踪转化和 AOV 变化。 ****需要关注的关键指标：**** PDP 的转化率、添加到购物车率、与 Hub 打开的会话（如果已安装）、每个接收者的收入 (RPR) 以及与查看的产品事件相关的浏览驱动收入。快速修复清单：****最近查看的活动低？**** 验证****查看的产品****跟踪代码片段是否已触发，并且事件归因于配置文件。 ****Hub 添加到购物车的次数低？**** 确保****活性产品**** 水合在每个 PDP 上运行，并且型号/价格正确。 ****添加的收藏夹很少？**** 将收藏夹插槽移至核心 PDP CTA 附近，并确认数据产品 ID 与产品匹配。 ## 故障排除

****症状：**** 客户中心未出现在网站上。 ****可能的原因：**** 脚本未加载或集线器****隐藏****。 ****修复：**** 确认 customerHub.js 加载（检查控制台），****公司 ID**** 已设置，****客户中心****可见性在 ****客户中心 > 设置****中为****实时****。 ****症状：**** 控制台显示“无法加载 Klaviyo JS 脚本。”

****可能的原因：**** 脚本 URL 不正确或缺少 ****公司 ID****。 ****修复：**** 验证 https://static.klaviyo.com/onsite/js/<COMPANY\_ID>/klaviyo.js 并且 COMPANY\_ID 已填充。 ****症状：**** 活动产品卡未显示在 PDP 的集线器中。 ****可能原因：**** 水合物产品未调用或产品句柄错误。 ****修复：**** 确保等待循环运行并使用正确的产品句柄调用 window.customerHubApi.HydrateProduct("<handle>")。 ****症状：**** 最近查看的部分是空的。 ****可能的原因：**** 未实施查看的产品跟踪。 ****修复：**** 添加开发人员指南中的****查看的产品**** 跟踪片段并验证 Klaviyo 中的事件。 ****症状：**** 收藏夹或常见问题解答小部件无法在 PDP 上呈现。 ****可能的原因：**** 容器丢失或属性错误。 ****修复：**** 使用正确的产品 ID 添加 <div class="kl-hub-favorites-slot" data-product-id="..."> 和/或 <div class="klaviyo-faqs-slot" data-product-id="..."> 。 ****症状：**** 单击帐户图标无法打开 Hub。 ****可能的原因：**** 标头链接未指向 /account 或 #k-hub。 ****修复：**** 确保帐户锚点使用 /account （自动接管）或设置 href="#k-hub"。 ****症状：**** 购物者在 Hub 内无法识别为已登录。 ****可能的原因：**** 缺少 /api/authenticateCustomerHub 路由或 API 请求失败。 ****修复：**** 实现 Hydrogen 示例（或等效框架），将 access\_token 和 company\_id 发送到 Klaviyo 的登录端点，然后返回响应。 ## 常见问题解答

****问：**** 我是否必须使用 Shopify 客户帐户 API 才能登录？ ****A:**** 不。您可以使用 ****Klaviyo 一次性密码 (OTP)**** 代替。如果您已经使用 Shopify 帐户，请通过客户帐户 API 进行连接以获得无缝体验。 ****问：**** 我需要提供哪些店面路线？ ****A:**** 如果使用您现有的帐户，请提供 ****登录**** 和 ****注销**** 路线； ****管理帐户****和****管理地址****对于更深层次的链接是可选的。 ****问：**** 在哪里可以找到 Storefront API 公钥？ ****A:**** 在 Shopify 的 Headless Admin 下 ****Storefront API > 公共访问令牌****（也称为 ****Storefront API 公钥****）。 ****问：**** 客户中心可以接管我的帐户图标吗？ ****答：**** 是的。如果您的标题帐户链接使用/account，客户中心可以自动打开；您也可以将其指向#k-hub。 ****问：**** 是否需要 Shopify Hydrogen？ ****A:**** 不。身份验证示例使用 Hydrogen，但任何框架都可以在 /api/authenticateCustomerHub 实现服务器路由，将访问令牌和公司\_id 发布到 Klaviyo。 ****问：**** 收藏夹和常见问题解答可以存在于 PDP 上和 Hub 内吗？ ****答：**** 是的。在 PDP 上添加相应的容器 div；它们也将出现在 Hub 抽屉中。