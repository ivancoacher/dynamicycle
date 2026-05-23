---
id: "20920631501979"
title: "Klaviyo 中的数据捕获入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/20920631501979-Getting-started-with-data-capture-in-Klaviyo"
section: "All integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:33Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 中可用于收集数据的各种数据捕获方法。 Klaviyo 允许您统一从营销堆栈中的多个来源捕获的数据，并从数百万个数据点创建单一客户视图，以个性化您的营销。 ## Klaviyo 中的数据类型

Klaviyo 中的数据主要分为三种类型：

1.****事件数据****
   每当客户采取特定操作时，事件就会沿着客户的时间线填充。每个事件，例如**现场活跃**、**已下订单**或**已履行订单**，都称为指标。一个联系人可以有多个指标数据实例，只要他们多次执行相应的操作即可。例如，当客户在您的网站上下了多个订单时，他们的时间线上会列出多个**已下订单**指标。 2.****个人资料数据****
   配置文件数据描述联系人身份的一个方面，由 Klaviyo 属性和自定义属性组成。 Klaviyo 属性是本机跟踪的，包括诸如 **First Active**、**Last Active**、**Source**、**First Name** 和 **Last Name** 等属性。自定义属性是您可以创建的附加配置文件数据，并且通常特定于您的业务。常见的自定义属性包括性别、生日或产品偏好。您还可以通过第三方集成引入自定义属性，这允许您导入评论、评级和其他未在 Klaviyo 中本地跟踪的信息。 3.****目录数据****
   目录数据描述在产品目录中找到的项目。当您在商店中添加或删除产品时，这些数据会在您的电子商务平台上经常被修改。目录数据的示例包括颜色和尺寸等变体。在 Klaviyo 中，目录数据会引入并填充产品源、活动和流消息。有关更多信息，请参阅我们的指南[了解 Klaviyo 和应用程序之间交换的信息类型](https://help.klaviyo.com/hc/en-us/articles/360030696012)。 ## 数据捕获方法

### 注册表单

[注册表单](https://help.klaviyo.com/hc/en-us/articles/360026474752) 是一种从网站访问者那里收集信息并扩大订阅者列表的工具。这可以包括联系信息（例如，电子邮件地址和电话号码）或其他个人信息和偏好（例如，姓名、生日或客户感兴趣的产品）。通过注册表单收集的信息可用于细分您的客户群并个性化您的营销。 ### 同意页面

[同意页面](https://help.klaviyo.com/hc/en-us/articles/115005251848) 用作登陆页面，您可以在其中收集网站访问者的信息和营销同意。与注册表单类似，这些页面可以收集个人信息和客户偏好，用于个性化您的营销。 ### 集成和应用程序

Klaviyo 的大型应用程序市场允许您捕获整个营销生态系统的数据并获得统一的客户视图。 Klaviyo 与许多常见的电子商务平台集成，并从您的商店提取订单数据，例如**下订单**、**结帐开始**和其他事件。 Klaviyo 还与其他工具（例如，您可用于支付、购物车和订单管理、支持票证、订阅、运输、调查、推荐等的平台）进行了许多集成，因此您可以从各种渠道捕获数据。 [Klaviyo 的 API](https://developers.klaviyo.com/en/reference/api_overview) 还使各种[第三方](https://help.klaviyo.com/hc/en-us/articles/360049626051) 能够构建自己的与平台的集成。同样，如果您的营销堆栈中有一个工具尚未与 Klaviyo 集成，您可以[开发自己的](https://developers.klaviyo.com/en/docs/build_your_integration)。有关可用集成的完整列表，请参阅 Klaviyo 的[应用程序市场](https://marketplace.klaviyo.com/en-us/)。 ### 饼干

Klaviyo 使用 [cookies](https://help.klaviyo.com/hc/en-us/articles/360034666712) 作为其身份捕获功能的一部分，以自动识别点击您的电子邮件或提交 Klaviyo 表单的用户。由于 Klaviyo 仅使用第一方 cookie，因此网络跟踪仅适用于选择加入并收到您营销信息的客户。 Klaviyo 的 cookie 还启用[现场跟踪](https://help.klaviyo.com/hc/en-us/articles/115005076767)，允许您收集有关浏览活动的有用信息。然后，您可以利用这些信息进一步个性化您的营销并了解客户的购物行为。 ### 匿名访客活动回填

通过 Klaviyo 的[匿名访客活动回填](https://help.klaviyo.com/hc/en-us/articles/17928628922395)，您可以在识别之前捕获购物者的现场活动。一旦将来识别出该访客，您就可以访问他们的历史现场活动。这使您可以更全面地了解客户的旅程，无论他们何时通过 Klaviyo 的网络跟踪被识别。为了收集匿名访问者的现场数据，Klaviyo 会记录有关访问者发生的操作的数据，并将其存储在本地浏览器中。将来，当该访问者被识别时，该数据就会发送到 Klaviyo 并从浏览器中清除。任何未来的现场活动一旦被识别，都将像往常一样通过 Klaviyo cookie 进行跟踪。 ### 数据源

可以使用数据源将目录数据发送到 Klaviyo。 Klaviyo 中的[产品源](https://help.klaviyo.com/hc/en-us/articles/115005082787) 从商店的产品目录和客户行为（例如，他们过去查看或购买的产品）中获取数据。您还可以设置自己的[自定义网络源](https://help.klaviyo.com/hc/en-us/articles/115005258768)，以从 Klaviyo 电子邮件中的外部 URL 动态填充数据。这些选项非常适合经常更新的数据（例如产品目录或博客文章），并允许您在与客户的沟通中自动包含营销堆栈不同部分的最新内容。 ### API

Klaviyo 有许多 [API](https://developers.klaviyo.com/en/reference/api_overview)，您可以使用它们以编程方式从您的商店和电子商务生态系统的其他部分发送数据。 Klaviyo 的 REST API 允许您发送和请求有关您的数据：

- 指标
- 个人资料
- 列表和片段
- 数据隐私
- 活动
- 模板
- 目录

同时，[Events API](https://developers.klaviyo.com/en/reference/events_api_overview) 用于跟踪人员以及他们触发的事件或他们执行的操作。 ### 手动上传

Klaviyo 还允许您手动将数据上传到平台。您可以在 Klaviyo 中手动导入两种主要类型的数据：

1. ****历史事件数据****如果您与 Klaviyo 的集成没有自动同步历史事件数据，您可以使用 CSV 文件[手动上传数据](https://help.klaviyo.com/hc/en-us/articles/115005081247)。 2.****个人资料和订阅数据****
   您可以通过 CSV 上传将个人资料数据导入到 Klaviyo。这包括可用于存储有关个人资料的信息的个人资料属性，以及有关各种渠道的联系人同意状态的数据。 ### SFTP

Klaviyo 可以通过 [SFTP](https://developers.klaviyo.com/en/docs/use_klaviyos_sftp_import_tool)（安全文件传输协议）将数据从外部系统提取到 Klaviyo，让您安全地传输文件。此功能非常适合想要使用自己选择的 SFTP 客户端批量导入 CSV 数据的客户。目前，Klaviyo 通过 SFTP 支持以下功能：

- 个人资料创建和更新
- 活动创建

## 其他资源

- [了解集成](https://help.klaviyo.com/hc/en-us/articles/115000256472)
- [了解数据类型](https://help.klaviyo.com/hc/en-us/articles/115005237648)
- [有关集成的常见问题](https://help.klaviyo.com/hc/en-us/articles/115005081007)