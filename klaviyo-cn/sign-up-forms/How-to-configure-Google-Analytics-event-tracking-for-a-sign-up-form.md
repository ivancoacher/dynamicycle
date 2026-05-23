---
id: "115005077027"
title: "如何为注册表单配置 Google Analytics 事件跟踪"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005077027-How-to-configure-Google-Analytics-event-tracking-for-a-sign-up-form"
section: "Build and use forms"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:17Z"
language: "zh"
---
## 你将会学到

了解如何为您的 Klaviyo 注册表单设置 Google Analytics 事件跟踪，以深入了解有关表单的重要用户操作。您可以通过在 Google Analytics（分析）中将 Klaviyo 事件（例如 form\_open、form\_close、form\_submit）标记为转化来衡量表单活动。通过以下两步过程进行设置：

1. 将代码片段添加到您的网站，以将 Klaviyo 注册表单数据发送到 Google Analytics。 2. 在 Google Analytics（分析）中将您的事件标记为转化。请注意，Google Analytics 事件跟踪可能需要 24-48 小时才能更新。本指南介绍了如何在 Google Analytics 4 中配置 Klaviyo 注册表单的跟踪活动。 ## 开始之前

在 Google Analytics 中为注册表单配置事件跟踪需要在您的网站上粘贴一段代码。如果您不习惯粘贴代码并且没有开发人员协助，Klaviyo 在我们的[合作伙伴目录](https://connect.klaviyo.com/) 中拥有庞大的合作伙伴网络。 ## 跟踪使用 Klaviyo 表单提交的注册情况

您可以通过向 [klaviyoForms 事件](https://developers.klaviyo.com/en/v1-2/docs/track-klaviyo-form-activity-using-javascript) 添加事件监听器来跟踪 Google Analytics（分析）中的 Klaviyo 表单活动，然后对每种类型的事件执行不同的 GA 跟踪调用。必须将此代码粘贴到您网站的主主题文件中。 - 如果您使用的是 Shopify，请将代码段粘贴到 theme.liquid 文件中结束 </body> 标记上方的新行中。请注意，如果您使用自定义产品页面，则可能需要将此代码段添加到不同的主题文件或单个自定义产品页面。 - 如果您使用的是 Shopify 2.0，请将代码添加到自定义 Liquid 块中。 - 如果您使用的是 BigCommerce，请从 BigCommerce 管理面板导航至****店面 > 页脚脚本****，然后将代码片段粘贴到新行的页脚代码框中。以下是用于在 Google Analytics 中跟踪所有 klaviyoForms 事件类型的通用代码。如果您使用 [gtag.js](https://developers.google.com/tag-platform/gtagjs) 加载 Google Analytics（分析），也应该使用此代码：

````
<脚本>
  window.addEventListener("klaviyoForms", 函数(e) {
    if (e.detail.type == 'open' || e.detail.type == 'embedOpen') {
      gtag('event', 'form_open', {'form': 'Klaviyo form', 'form_id': e.detail.formId});
    }
    if (e.detail.type == '提交') {
      gtag('event', 'form_submit', {'form': 'Klaviyo form', 'form_id': e.detail.formId});
    }
    if (e.detail.type == 'stepSubmit') {
      gtag('event', 'form_step_submit', {'form': 'Klaviyo form', 'step_name': e.detail.metaData.$step_name});
    }
    if (e.detail.type == 'redirectedToUrl') {
      gtag('event', 'form_url_redirect', {'form': 'Klaviyo form', 'form_id': e.detail.formId});
    }
    if (e.detail.type == '关闭') {
      gtag('event', 'form_close', {'form': 'Klaviyo form', 'form_id': e.detail.formId});
    }
  });
</脚本>
````

如果您想跟踪不同的表单版本或变体，请将代码片段修改为

````
gtag('event', 'form_open', {'form': 'Klaviyo form', 'form_id': e.detail.formId, 'form_version_id': e.detail.formVersionId })
````

使用相关的“form_id”而不是

````
gtag('event', 'form_open', {'form': 'Klaviyo form', 'form_id': e.detail.formId })
````

如果您正在跟踪多步骤表单的表单提交，请注意，每次填写表单时只会触发 1 个“提交”事件。提交事件将在以下情况下触发：

- 对于具有电子邮件或短信订阅操作的表单，提交电子邮件或电话会触发提交事件。 - 对于跨多个步骤同时包含电子邮件和短信字段的表单，提交表单中第一个出现的字段会触发提交事件。 - 对于没有电子邮件或短信订阅操作的表单（例如，仅包含文本字段的表单），单击 **操作** 设置为 ****提交表单**** 的按钮会触发提交事件。提交每个步骤时都会触发“stepSubmit”事件。 ## 测试您的跟踪代码

在网站上安装跟踪代码后，您可以对其进行测试以确保数据被跟踪。要测试您的代码：

1. 导航到您的网站并与您的表单交互（例如，提交或关闭它）。 2. 打开 Google Analytics，然后打开****报告 > 实时。****
3. 在**按事件名称划分的事件计数**下，您应该会看到表单所跟踪的数据的详细信息。 每个事件的指标应根据您所采取的操作反映准确的计数（例如，如果您关闭了表单，您将在表单\_close 的 **事件计数** 中看到这一点）。 ![GA222.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716301162779)

如果您没有看到事件，请确保 Google Analytics 设置正确，并且您使用的代码片段正确。另请注意，您的活动只能实时显示 30 分钟。有关更多详细信息，请参阅 [[GA4] 实时报告](https://support.google.com/analytics/answer/9271392)。 ## 配置要标记为转化的事件

在 Google Analytics（分析）中设置新注册事件的跟踪后，您可以将相应的事件配置为标记为转化，以帮助您监控用户如何与表单交互。从 Google Analytics 中的 **现有事件表**（****管理 > 事件****），将开关切换至 **标记为转化** 对于您想要跟踪的任何事件。如果某个事件不在现有列表中，您需要[创建一个新事件并将其标记为转化](https://support.google.com/analytics/answer/12966437?sjid=13312267381996017623-NA)。如果您只想在满足特定条件（例如特定表单 ID）时将事件标记为转化，则需要[根据事件参数的值配置转化](https://support.google.com/analytics/answer/11053133?hl=en#zippy=%2Cin-this-article)。当您将事件标记为转化时，Google Analytics（分析）每次看到您的事件\_name（例如 form\_open）时都会注册一次转化。在**转化报告**上跟踪 Klaviyo 表单数据的转化。请注意，在您开始跟踪 klaviyoForms 事件后 24-48 小时内，您的事件的转化可能不会显示。 ## 其他资源

- [如何使用 Google 跟踪代码管理器添加 Klaviyo 网络跟踪](https://help.klaviyo.com/hc/en-us/articles/360015392131)
- [了解 Klaviyo 中的 UTM 跟踪](https://help.klaviyo.com/hc/en-us/articles/115005247808)
- [使用 Javascript 跟踪 Klaviyo 表单活动](https://developers.klaviyo.com/en/docs/track_klaviyo_form_activity_using_javascript)
- 课程：[通过战略注册表单吸引新订阅者](https://academy.klaviyo.com/create-strategic-sign-up-forms)