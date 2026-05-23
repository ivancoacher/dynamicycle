---
id: "115002451292"
title: "将 Shopify 注册表单同步到 Klaviyo 中的列表"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115002451292-Sync-a-Shopify-Signup-Form-to-a-List-in-Klaviyo"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:12Z"
language: "zh"
---
## 概述

本指南介绍了将 Shopify 注册表单同步到 Klaviyo 帐户中的列表。我们使用 Shopify 的 10 个免费主题作为示例。如果您打算使用此方法从自定义主题同步表单，请记住，如果您编辑了注册表单，则可能需要编辑下面使用的代码片段中的某些项目。 #### 了解更多

我们还有[将 Klaviyo 表单添加到 Shopify 的所有免费主题](https://help.klaviyo.com/hc/en-us/articles/115001618871-Add-a-Klaviyo-Form-to-a-Shopify-Free-Theme) 的指南。添加到 Shopify `theme.liquid` 文件的代码段会因您的主题而略有不同。从下面的列表中选择您的主题，然后按照相应的说明进行操作。如果您在下面的列表中没有看到您的主题，您还可以查看我们关于[使用自定义主题](https://help.klaviyo.com/hc/en-us/articles/115002451292#using-a-custom-theme)的部分。 |  |  |
| --- | --- |
| [jQuery 3.2.1 或更高版本的主题](https://help.klaviyo.com/hc/en-us/articles/115002451292#shopify-themes-that-include-jquery-3-2-1-or-higher) | [jQuery 版本 < 3.2.1 的主题](https://help.klaviyo.com/hc/en-us/articles/115002451292#shopify-themes-with-a-jquery-version-lower-than-3-2-1-or-no-jquery) |
| - 布鲁克林 - 供应 - Jumpstart - 流行 - 简单 | - 最小 - 叙事 - 首次亮相 - 冒险 - 无边 |

## 包含 jQuery 3.2.1 或更高版本的 Shopify 主题

使用以下代码片段将您的 Shopify 注册表单同步到您的 Klaviyo 帐户中的列表。请记住更新代码片段中的列表 ID。基本流程如下：

1. 在您的 Shopify 后台中点击****在线商店****，然后从**操作**下拉列表中点击****编辑代码****以打开您的网页编辑器。 2. 打开“theme.liquid”文件并粘贴下面的代码片段。将代码片段粘贴到结束“</body>”标记之前。 ````
   <脚本类型=“文本/javascript”>
       $("input[name='contact[email]']").on('blur', function(e) {
           e.preventDefault();
           var email = $(this).val();
           变量设置 = {
               “异步”：正确，
               “跨域”：正确，
               "url": "https://manage.kmail-lists.com/subscriptions/external/subscribe",
               “方法”：“发布”，
               “标题”：{
                   “内容类型”：“应用程序/x-www-form-urlencoded”，
                   “缓存控制”：“无缓存”
               },
               “数据”：{
                   "g": "LIST_ID",
                   "$fields": "$source",
                   “电子邮件”：电子邮件，
                   "$source": "Shopify 表单"
               }
           };
           $.ajax(设置).done(函数(响应){
               控制台.log(响应);
           });
       });
   </脚本>
   ````
3. 从您的 Klaviyo 帐户中，选择要同步的列表并复制 [列表 ID](https://help.klaviyo.com/hc/en-us/articles/115005078647-Find-a-List-ID)。 ![listID.png](https://klaviyo.zendesk.com/hc/article_attachments/28716062299547)
4. 在您的 Shopify 帐户中，将列表 ID 添加到“theme.liquid”文件中的代码段。在此步骤中，您还可以[根据需要修改此表单的 $source](https://help.klaviyo.com/hc/en-us/articles/115002451292#modify-the--source-of-your-form)。 ![shopifyDefaultFormListid.png](https://klaviyo.zendesk.com/hc/article_attachments/28716062302107)
5. 保存更新后的“theme.liquid”文件。您现在可以测试您的注册表单以确保其正常工作。首先，在表格中输入您的电子邮件地址。接下来，检查您的收件箱并通过选择加入的电子邮件确认您的订阅。最后，在您的 Klaviyo 帐户中搜索您的电子邮件地址，以确认您的个人资料已添加。如果您仍然遇到任何困难，请[联系我们的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。 ## jQuery 版本低于 3.2.1 或没有 jQuery 的 Shopify 主题

使用以下代码片段将您的 Shopify 注册表单同步到您的 Klaviyo 帐户中的列表。请记住更新代码片段中的列表 ID。基本流程如下：

1. 在您的 Shopify 后台中点击****在线商店****，然后从**操作**下拉列表中点击****编辑代码****以打开您的网页编辑器。 2. 打开“theme.liquid”文件并粘贴下面的代码片段。将代码片段粘贴到结束“</body>”标记之前。 ````
   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
   <script>var $KL = jQuery.noConflict(true);</script>
   <脚本类型=“文本/javascript”>
       $KL("input[name='contact[email]']").on('blur', function(e) {
           e.preventDefault();
           var email = $KL(this).val();
           变量设置 = {
               “异步”：正确，
               “跨域”：正确，
               "url": "https://manage.kmail-lists.com/subscriptions/external/subscribe",
               “方法”：“发布”，
               “标题”：{
                   “内容类型”：“应用程序/x-www-form-urlencoded”，
                   “缓存控制”：“无缓存”
               },
               “数据”：{
                   "g": "LIST_ID",
                   "$fields": "$source",
                   “电子邮件”：电子邮件，
                   "$source": "Shopify 表单"
               }
           };
           $KL.ajax(设置).done(函数(响应){
               控制台.log(响应);
           });
       });
   </脚本>
   ````
3. 从您的 Klaviyo 帐户中，选择要同步的列表并复制 [列表 ID](https://help.klaviyo.com/hc/en-us/articles/115005078647-Find-a-List-ID)。 ![listID.png](https://klaviyo.zendesk.com/hc/article_attachments/28716062299547)
4. 在您的 Shopify 帐户中，将列表 ID 添加到“theme.liquid”文件中的代码段。在此步骤中，您还可以[根据需要修改此表单的 $source](https://help.klaviyo.com/hc/en-us/articles/115002451292#modify-the--source-of-your-form)。 ![shopifyDefaultFormListid.png](https://klaviyo.zendesk.com/hc/article_attachments/28716062302107)
5. 保存更新后的“theme.liquid”文件。您现在可以测试您的注册表单以确保其正常工作。首先，在表格中输入您的电子邮件地址。接下来，检查您的收件箱并通过选择加入的电子邮件确认您的订阅。最后，在您的 Klaviyo 帐户中搜索您的电子邮件地址，以确认您的个人资料已添加。如果您仍然遇到任何困难，请[联系我们的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。 ## 使用自定义主题

如果您使用自定义主题，您首先必须验证主题使用的 jQuery 版本，然后相应地选择代码片段。此外，如果您的主题修改了标准 Shopify 注册表单，您将需要修改代码片段，以便它定位具有正确 ID 的电子邮件输入元素。 1. 导航到您的网站并打开网络浏览器的控制台（如果您在 Mac 上使用 Chrome，则可以按 `⌥`-`⌘`-`J）。`
2. 以下命令返回您网站上 jQuery 的当前版本：`$.fn`。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28716051920923)
3. 如果您的 jQuery 版本为 3.2.1 或更高版本，您可以使用[包含 jQuery 3.2.1 或更高版本的 Shopify 主题](https://help.klaviyo.com/hc/en-us/articles/115002451292#shopify-themes-that-include-jquery-3-2-1-or-higher) 部分中的说明。 4. 如果您的 jQuery 版本低于 3.2.1，您可以使用[jQuery 版本低于 3.2.1 的 Shopify 主题](https://help.klaviyo.com/hc/en-us/articles/115002451292#shopify-themes-with-a-jquery-version-lower-than-3-2-1) 部分中的说明。如果您仍然遇到任何困难，请[联系我们的支持团队](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-Contact-Support)。 ## 修改表单的 `$source`

在此页面的默认代码段中，如果您想更改 Klaviyo 中客户个人资料中显示的 `$source` 属性，则可以修改包含 `$source": "Shopify form"` 的行。仅更改此表达式的值。例如，更新为 `“$source”: “Homepage form”` 将在用户的个人资料上设置用户的 `$source`，如下所示：

![](https://klaviyo.zendesk.com/hc/article_attachments/28716051912347)

修改此表单的元素时要小心。如果您发现表单无法正常工作，请联系客户支持或尝试使用本文中的默认代码片段从头开始添加表单。