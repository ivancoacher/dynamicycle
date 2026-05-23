---
id: "115005254188"
title: "如何创建混合电子邮件模板"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254188-How-to-create-a-hybrid-email-template"
section: "Advanced template design"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-04-21T13:54:24Z"
language: "zh"
---
## 你将会学到

了解如何创建与 Klaviyo 拖放编辑器兼容的自定义 HTML 模板（即混合模板）。通过执行这些步骤，您可以设计完全自定义的 HTML 电子邮件，同时保持对仅在拖放编辑器中可用的功能（例如产品块或通用内容块）的访问。我们仅建议精通技术的营销人员或有权访问开发人员的任何人使用自定义 HTML。虽然我们的产品确实支持自定义 HTML，但我们的支持团队除了提供本文档中涵盖的一般指导之外，无法帮助您构建自定义模板。需要帮助吗？ [联系 Klaviyo 合作伙伴。](https://connect.klaviyo.com/)

为了维护您的数据安全，Klaviyo 的支持团队无法打开您的 HTML 文件。 ## 将代码片段添加到您的 HTML 模板中

每个电子邮件模板仅添加下面概述的代码片段之一。一个代码片段允许您添加多个拖放块，因此您无需添加多个代码片段。例如，如果您想使用拖放编辑器添加图像和表格块，只需按照下面的[**添加可自定义图像块**](https://help.klaviyo.com/hc/en-us/articles/115005254188#h_01HDH0B0301Y7FG9KGBM0RRWW0)步骤即可。将模板上传到 Klaviyo 并在活动或流程中使用它后，您将能够在图像块上方或下方添加块。 ****添加可编辑文本块****

1. 使用您喜欢的 HTML 编辑器创建自定义 HTML 模板。 2. 将以下代码片段添加到您的 HTML 模板中。将其放置在您想要在模板中添加文本块的任何位置。 ````
   <tdalign=“中心”data-klaviyo-region=“true”data-klaviyo-region-width-pixels=“600”>
       <div class="klaviyo-block klaviyo-text-block">世界你好！</div>
   </td>
   ````
3. 在 Klaviyo 中，导航至****内容 > 模板****。 4. 选择****电子邮件模板****选项卡。 5. 单击****导入****。 6. 输入模板的名称，上传 HTML 文件，然后导入。 7. 如果您从 **模板** 选项卡打开模板，您将在 Klaviyo 的 HTML 编辑器中看到模板的代码。 ![混合电子邮件模板的 html](https://klaviyo.zendesk.com/hc/article_attachments/28720656075931)
8. 要访问 Klaviyo 拖放编辑器中的模板，请将其添加到营销活动或流程中。 9. 选择****拖放**** 作为模板类型。 ![拖放电子邮件选项](https://klaviyo.zendesk.com/hc/article_attachments/28720667865243)
10. 请注意显示 **Hello world!** 的文本块，这是您的可编辑文本块。 11. 根据需要将其他块拖放到文本块上方或下方。 ****添加可定制的图像块****

1. 使用您喜欢的 HTML 编辑器创建自定义 HTML 模板。 2. 将以下代码片段添加到您的 HTML 模板中。确保在导入模板后将其放置在您想要添加图像块的任何位置。 1. 或者，您可以在 div 中添加预设图像。如果您选择这样做，您的代码将如下所示：

      ````
      <tdalign=“中心”data-klaviyo-region=“true”data-klaviyo-region-width-pixels=“600”>
          <div class="klaviyo-block klaviyo-image-block">
              <a href="http://klaviyo.com><img src="example.com/my_image.png" alt="我的图片" /></a> </div>
      </td>
      ````

   ````
   <tdalign=“中心”data-klaviyo-region=“true”data-klaviyo-region-width-pixels=“600”>
       <div class="klaviyo-block klaviyo-image-block"></div>
   </td>
   ````
3. 在 Klaviyo 中，导航至****内容 > 模板****。 4. 选择****电子邮件模板****选项卡。 5. 单击****导入****。 6. 输入模板的名称，上传 HTML 文件并导入。 7. 如果您从 **模板** 选项卡打开模板，您将在 Klaviyo 的 HTML 编辑器中看到模板的代码。 ![混合模板的 HTML](https://klaviyo.zendesk.com/hc/article_attachments/28720656075931)
8. 要访问 Klaviyo 拖放编辑器中的模板，请将其添加到营销活动或流程中。在内容步骤中，选择您导入的模板。 9. 请注意图像块，其中包含上传图像的按钮或您包含的图像。 10. 根据需要将其他块拖放到图像块上方或下方。 ![图像块](https://klaviyo.zendesk.com/hc/article_attachments/28720656083611)

****添加通用内容块****

此过程支持通用内容块，****不****通用部分。 1. 使用您喜欢的 HTML 编辑器创建自定义 HTML 模板。 2. 将以下代码片段添加到您的 HTML 模板中。确保在导入模板后将其放置在您想要添加图像块的任何位置。 ````
   <td data-klaviyo-region="true" data-klaviyo-region-width-pixels="600"> <div data-klaviyo-universal-block="block_id_1"><div></td>
   ````
3. 将 **block\_id\_1** 替换为通用内容块的 ID。要查找通用内容块的 ID：
   1. 导航至****内容 > 通用内容****。 2. 打开通用内容块进行编辑。 3. 此页面的 URL 将遵循以下格式：**https://www.klaviyo.com/email-template-editor/universal/block/BLOCK\_ID**。 4. 从 URL 复制块 ID。 4. 在 Klaviyo 中，导航至****内容 > 模板****。 5. 选择****电子邮件模板****选项卡。 6. 单击****导入****。 7. 输入模板的名称，上传 HTML 文件并导入。 8. 如果您从 **模板** 选项卡打开模板，您将在 Klaviyo 的 HTML 编辑器中看到模板的代码。 ![混合模板的 HTML](https://klaviyo.zendesk.com/hc/article_attachments/28720656075931)
9. 要访问 Klaviyo 拖放编辑器中的模板，请将其添加到营销活动或流程中。在内容步骤中，选择您导入的模板。 10. 注意通用内容块。您可以使用单个代码片段添加多个通用内容块。为此，请使用不同块的 ID，在上面代码片段中的第一个元素之后立即添加另一个 **div** 元素。 ****添加另一种类型的块（即产品块、表块）****

1. 使用您喜欢的 HTML 编辑器创建自定义 HTML 模板。 2. 将以下代码片段添加到您的 HTML 模板中。导入模板后，将其放置在您想要添加块的任何位置。 ````
   <tdalign=“中心”data-klaviyo-region=“true”data-klaviyo-region-width-pixels=“600”>
       <div class="klaviyo-block klaviyo-text-block">世界你好！</div>
   </td>
   ````
3. 在 Klaviyo 中，导航至****内容 > 模板****。 4. 选择****电子邮件模板****选项卡。 5. 单击****导入****。 6. 输入模板的名称，上传 HTML 文件并导入。 7. 如果您从 **模板** 选项卡打开模板，您将在 Klaviyo 的 HTML 编辑器中看到模板的代码。 ![模板的 html](https://klaviyo.zendesk.com/hc/article_attachments/28720656075931)
8. 要访问 Klaviyo 拖放编辑器中的模板，请将其添加到营销活动或流程中。在内容步骤中，选择您导入的模板。 9. 请注意显示 **Hello world!** 的文本块，将另一个块（例如产品块）拖动到该块下方。 10. 根据需要删除文本块并添加其他自定义块。 ![添加块](https://klaviyo.zendesk.com/hc/article_attachments/28720667866779)

## 示例混合电子邮件模板代码

下面的示例显示了一个功能性 HTML 文件，其中包含文本块的混合代码片段。使用此代码来测试混合编辑器功能。 ````
  <html>
  <头>
    <meta content =“宽度=设备宽度，初始比例= 1.0”名称=“视口”/>
    <title>简单的混合电子邮件</title>
    <风格>
      身体{
        背景颜色：#f6f6f6；
        字体系列：无衬线字体；
        边距：20 像素；
      }
      .main{
        背景：#ffffff；
        边框半径：3px；
        宽度：100%；
      }
      .容器{
        边距：0 自动！重要；
        宽度：600 像素；
      }
      .包装器{
        框大小：边框框；
        内边距：15px；
      }
      表{
        宽度：100%；
      }
    </风格>
  </头>
  <正文>
    <div 类=“容器”>
      <表类=“主”>
        <tr>
          <td class="wrapper">这是一封非常简单的 HTML 电子邮件</td>
        </tr>
        <tr>
          <td类=“包装”>
            <表>
              <tr>
                <tdalign=“中心”data-klaviyo-region=“true”data-klaviyo-region-width-pixels=“600”>
                  <div class="klaviyo-block klaviyo-text-block">
                    世界你好！ </div>
                </td>
              </tr>
            </表>
          </td>
        </tr>
        <tr>
          <td class="wrapper">{% 取消订阅 %}</td>
        </tr>
      </表>
    </div>
  </正文>
</html>
````

## 表情符号和混合电子邮件模板

截至 2024 年 2 月，所有 Klaviyo 电子邮件编辑器（即拖放编辑器、混合编辑器、纯文本编辑器和自定义 HTML 编辑器）均支持所有表情符号。 ## 结果

完成这些步骤后，您将能够添加和编辑自定义 HTML 模板的某些区域。请注意，您无法在自定义模板的任何区域添加或编辑拖放块，放置初始块的位置除外。