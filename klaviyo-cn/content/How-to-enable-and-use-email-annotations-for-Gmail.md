---
id: "23145809959707"
title: "如何启用和使用 Gmail 电子邮件注释"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/23145809959707-How-to-enable-and-use-email-annotations-for-Gmail"
section: "Advanced template design"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-11T10:57:19Z"
language: "zh"
---
## 你将会学到

了解电子邮件注释，它使您能够在 Gmail 收件箱的列表视图中显示关键信息（即在有人打开电子邮件之前）。电子邮件注释允许您突出显示交易或优惠（例如优惠券代码），或直接在收件箱中显示产品图像。仅自定义 HTML 或混合电子邮件支持实现 Gmail 注释所需的代码。无法将此代码与 Klaviyo 的拖放电子邮件编辑器一起使用。我们仅建议精通技术的营销人员或有权访问开发人员的任何人使用电子邮件注释。虽然我们的产品确实支持此功能，但我们的支持团队除了提供本文档中涵盖的一般指导之外，无法帮助您构建自定义模板。为了维护您的数据安全，Klaviyo 的支持团队无法打开您的 HTML 文件。 ## 关于电子邮件注释

对于启用了**促销**选项卡的用户，Gmail 移动收件箱支持电子邮件注释。这些注释仅出现在 **促销** 选项卡中，而不是主收件箱中。注释有 3 种类型：

- ****交易/报价****
  突出显示优惠或优惠，例如优惠券代码或免费送货，包括优惠到期日期。 ![Bolas烘焙食品交易注释](https://klaviyo.zendesk.com/hc/article_attachments/28718022989339)
- ****产品轮播****
  显示产品图像轮播，可以选择包括名称和价格等产品详细信息。 ![产品轮播注释](https://klaviyo.zendesk.com/hc/article_attachments/28718022991771)
- ****单张图像****
  显示单个图像以及可选的附加文本。 ![单图注释](https://klaviyo.zendesk.com/hc/article_attachments/28718022993947)

添加此代码可为 Gmail 提供显示电子邮件注释的选项。即使电子邮件包含注释代码，它们也可能不会显示给每个收件人。 Gmail 根据收件人设置和收件箱密度选择何时以及如何显示注释。 。 ## 开始之前

Google 维护着一份可以使用注释的发件人白名单。在使用注释之前，您必须请求将您的品牌添加到此允许列表中。要请求 Google 将您添加到其注释许可名单中，[发送电子邮件至p-Promo-Outreach@google.com](mailto:p-Promo-Outreach@google.com?subject=Allowlisting%20for%20email%20annotations&body=REPLACE%20ALL%20PLACEHOLDERS%20W ITH%20YOUR%20COMPANY%20INFORMATION%20BEFORE%20SENDING%0AHello%20team%2C%20%0AI'm%20a%20Klaviyo%20customer%20writing%20to%20request%20that%20www.example .com%20be%20已添加%20至%20您的%20电子邮件%20注释%20白名单。%20%0AMy%20发送%20domain%20is%20www.example.com%0AWe%20use%20the%20following%20subd omains%3A%20%0A-%20send.example.com%0A-%20marketing-messages.example.com%0A我们的%20landing%20page%20URL%20is%20www.example.com%0A谢谢%2C%0AYOUR%20NAME)包含以下信息：

- 所有域（例如 example.com）
- 所有子域（例如，send.example.com、blog.example.com、marketing-messages.example.com）
- 您的着陆页网址（例如您的主页）

添加到您的邮件中的任何注释代码都将被忽略，直到您被添加到 Google 许可名单中，这可能需要 7-10 个工作日或更长时间。 Klaviyo 无法了解列入许可名单的流程，因此无法加快您的请求。如果您对白名单流程或请求状态有疑问，请联系 [p-Promo-Outreach@google.com](mailto:p-Promo-Outreach@google.com)。 ## 添加注释到您的电子邮件

在 HTML 电子邮件模板的正文部分中添加以下代码以添加电子邮件注释。 有 3 种类型的注释可用：

- [交易注释](#h_01HQ6P8JEGEDJR27ZSC5YYHXTX)
- [产品轮播注释](#h_01HQ6P8JEG583BSXQXXMHHGPQN)
- [单张图像注释](#h_01HQ6P8JEGERCMEAT35S9P4CV2)

#### 交易

````
  <div itemscope itemtype="http://schema.org/DiscountOffer">
    <meta itemprop="描述" content="描述"/>
    <meta itemprop="discountCode" content="DISCOUNT_CODE"/>
    <meta itemprop="availabilityStarts" content="START_DATE_TIME"/>
    <meta itemprop="availabilityEnds" content="END_DATE_TIME"/>
  </div>
````

![Bolas烘焙食品交易注释](https://klaviyo.zendesk.com/hc/article_attachments/28718022989339)

替换代码中的以下占位符：

- ****描述****
  优惠的简短（1-2 行）文字描述
- ****折扣\_代码****
  收件人可以在结帐时输入的代码以接收优惠
- ****START\_DATE\_TIME****优惠开始日期/时间，使用 [ISO 8601 格式](https://support.google.com/merchants/answer/12756212?visit_id=638424907272835479-1199962788&rd=1)
- ****END\_DATE\_TIME****
  优惠结束日期/时间，使用 [ISO 8601 格式](https://support.google.com/merchants/answer/12756212?visit_id=638424907272835479-1199962788&rd=1)

#### 产品轮播

````
  <div itemscope itemtype="http://schema.org/PromotionCard">
    <meta itemprop="image" content="IMAGE_URL1"/>
    <meta itemprop="url" content="PROMO_URL1"/>
    // （可选）包含以下 PromotionCard 属性：
    <meta itemprop="headline" content="HEADLINE1"/>
    <meta itemprop="价格" content="PRICE1"/>
    <meta itemprop="priceCurrency" content="PRICE_CURRENCY1"/>
    <meta itemprop="discountValue" content="DISCOUNT_VALUE1"/>
    <meta itemprop="position" content="POSITION"/>
  </div>
  // 在产品轮播中构建第二个图像预览：
  <div itemscope itemtype="http://schema.org/PromotionCard">
    <meta itemprop="image" content="IMAGE_URL2"/>
    <meta itemprop="url" content="PROMO_URL2"/>
    // （可选）包含以下 PromotionCard 属性：
    <meta itemprop="headline" content="HEADLINE2"/>
    <meta itemprop="价格" content="PRICE2"/>
    <meta itemprop="priceCurrency" content="PRICE_CURRENCY2"/>
    <meta itemprop="discountValue" content="DISCOUNT_VALUE2"/>
    <meta itemprop="position" content="POSITION"/>
  </div>
  // 要包含更多图像预览，请添加其他 PromotionCard 对象。 // 您最多可以在产品轮播中包含 10 个图像预览。 ````

![产品轮播注释](https://klaviyo.zendesk.com/hc/article_attachments/28718022991771)

替换代码中的以下占位符：

- ****IMAGE\_URL1****、****IMAGE\_URL2**** 等 要在轮播中显示的产品图像的 URL。支持的宽高比为 4:5、1:1 和 1.91:1。每个图像的长宽比必须相同。 - ****PROMO\_URL1****、****PROMO\_URL2**** 等 单击产品图像的收件人的登录页面的 URL。 - ****标题1、标题2等****
  1-2 行的简短产品描述。 - ****PRICE1****、****PRICE2**** 等 产品的基本价格（仅数字，无货币）。 - ****PRICE\_CURRENCY1****、****PRICE\_CURRENCY2**** 等。商品价格的 3 个字母货币代码（例如 USD）。 - ****DISCOUNT\_VALUE1****、****DISCOUNT\_VALUE2**** 等。如果适用，商品折扣金额（仅数字，无货币）。 - ****职位****
  （可选）指示该项目在轮播中的位置的数字。 #### 单张图像

````
  <div itemscope itemtype="http://schema.org/PromotionCard">
    <meta itemprop="image" content="IMAGE_URL1"/>
    <meta itemprop="url" content="PROMO_URL1"/>
  </div>
````

![单图注释](https://klaviyo.zendesk.com/hc/article_attachments/28718022993947)

替换代码中的以下占位符：

- ****图片\_URL1****
  要在轮播中显示的产品图像的 URL。支持的宽高比为 4:5、1:1 和 1.91:1。 - ****促销\_URL1****
  单击产品图像的收件人的登录页面的 URL。 ## 关于自动注释提取

有时，即使发件人没有添加上述代码，Google 也会自动提取电子邮件数据以添加注释。这是由 Google 自行决定的，发件人无法控制。 ## 对注释进行故障排除

Google 对注释执行严格的要求，并且注释可能会因多种原因而不会显示。 如果按照上述本文的设置说明进行操作后您的注释没有出现，请尝试执行以下故障排除步骤：

### 确保您的品牌已列入许可名单

Google 保留了有限的批准品牌许可名单，这些品牌可以使用电子邮件注释来防止垃圾邮件和滥用。如果您无权访问，则可能需要向 Google 请求：

1. 按照上述步骤[联系 Google](#h_01HQ6P8JEFJ8HXDR85SCV96C66)。 2. 需要 7-10 个工作日才能得到回复。一旦您提出请求，我们无法保证您的品牌一定会被添加到许可名单中，因为这由 Google 全权酌情决定。 ### 检查您的图像质量

用于电子邮件注释的所有图像都必须通过 Google 的质量过滤器。不符合要求的图像将不会显示在收件箱中。确保您的图像符合以下标准：

- 高质量（即大于 500 KB）
- 文字内容非常少（如果有的话）
- 是矩形的（不要使用遮罩使图像变成圆形或其他形状）
- 尺寸至少为 256x256 像素

### 不要为每个收件人使用唯一的图像

所有收件人必须使用相同的图像。您可以将唯一的跟踪参数添加到促销网址，但不能添加到图像网址。避免使用生成 CID 图像的工具（即每个收件人都是唯一的图像），因为如果使用，注释将不会显示。 ### 考虑 Gmail 的密度上限

Google 限制用户一次可以在收件箱中看到的注释图像的数量（即“密度上限”）。如果收件人的收件箱中已经有几封带注释的最新电子邮件，则您的收件箱可能无法防止混乱。此上限由 Google 自行决定实施，发件人无法控制。 ### 请注意，注释可能不会出现在预览电子邮件发送中

对于仅发送给少数收件人的测试电子邮件，注释通常不会出现在收件箱中。注释功能专为批量发送而设计，因此注释可能仅在将邮件发送给超过 100 个收件人时才会出现。 ### 确保您正在支持的 Gmail 选项卡中查找

支持注释仅显示在 Gmail 移动应用程序的 **促销** 选项卡中。注释不支持显示在：

- Gmail 应用程序中除**促销**之外的任何其他选项卡
- 在任何网络浏览器（例如移动或桌面网站）中查看 Gmail
- 未在 Gmail 设置中启用 **促销** 选项卡的用户的收件箱

## 其他资源

- [如何使用Klaviyo的主题行助手](https://klaviyo.zendesk.com/hc/en-us/articles/5051278887835)
- [了解 Gmail 的标签式收件箱](https://klaviyo.zendesk.com/hc/en-us/articles/115005078307)