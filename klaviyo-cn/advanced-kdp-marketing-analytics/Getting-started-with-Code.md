---
id: "18620644491035"
title: "代码入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/18620644491035-Getting-started-with-Code"
section: "Code"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: "zh"
---
## 你将会学到

了解代码以及如何创建由 Klaviyo 直接执行的自定义函数。代码需要定制开发，Klaviyo 的支持团队无法提供实际帮助。如果您的团队中没有开发人员并且不方便自己编写代码，请考虑向 Klaviyo 合作伙伴寻求帮助。 ## 开始之前

[高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。 ## 什么是代码？代码使您能够执行自定义函数以响应 Klaviyo 中捕获的事件。您可以在代码编辑器中编写自己的Javascript或Python函数，然后直接在平台中执行它们。使用 Code，您可以将数据发送到外部系统，而无需设置公共 HTTP 端点来接收 Webhook，并构建响应事件发生而触发的自定义功能。您还可以访问许多流行的预构建模块，以方便创建自定义解决方案。了解[如何使用代码构建自定义函数](https://academy.klaviyo.com/build-custom-functions-with-code)。 ## 主题

代码允许您执行自定义函数来响应可通过 [获取事件 API](https://developers.klaviyo.com/en/reference/get_events) 查询的任何事件。这些包括：

- 电子邮件事件（例如，**点击电子邮件**、**将电子邮件标记为垃圾邮件**）
- 短信事件（例如，**发送短信**、**接收短信**）
- 推送通知事件（例如，**收到推送**、**退回推送**）
- 来自集成的事件（即来自 Klaviyo 创建的第一方集成的事件）
- API 事件（即通过 Klaviyo 的 API 同步的事件）

Klaviyo Code 不支持以下事件作为主题：

1. 电子邮件已打开
2. 收到邮件

## 代码接口

要访问代码，请导航至****高级 KDP********> 数据管理 > 代码******** 下的 **代码** 选项卡。**

要创建自定义函数，请选择 **创建函数** 按钮：

![创建功能按钮](https://klaviyo.zendesk.com/hc/article_attachments/28722598719003)

您将进入 **Recipes** 页面，您可以在其中选择要执行的预构建解决方案，也可以选择空白的 Python 或 Node.js 函数。 ![图片 (9).jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722610653467)

如果您选择现有配方，您将看到代码编辑器，其中包含解决方案的代码以及功能描述。 ![图片 (10).jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598744219)

如果您选择空白函数以便创建自己的自定义解决方案，则**详细信息**模式将出现在您可以执行以下操作的位置：

- ****命名你的函数****
  识别您的功能的名称。 - ****为您的活动选择一个主题****
  将触发代码执行的事件。 - ****选择运行时间****
  执行代码的运行时环境（即 Python 或 Node.js）。 ![3.11.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722610665883)

  进行所需的选择并选择 **创建函数** 按钮后，您将进入包含以下选项卡的界面：
- 编辑
- 测试输出
- 日志

## 授予权限

第一次通过 Code 创建函数时，系统将提示您对 Code OAuth 应用程序进行身份验证。这是必需的，以便您的代码功能能够访问您的 Klaviyo 帐户中的数据。授予访问权限后，您将进入代码编辑器。 ## 编辑器

在代码的 **编辑器** 页面上，您会将页面分为 3 个选项卡：

- ****代码****
  代码选项卡有一个编辑器，您可以在其中编写 Python 或 Javascript 函数。 - ****模块****
  模块是为您的函数添加功能的第三方包。 - ****环境变量****
  环境变量是函数运行时访问的键值对。 ### 代码

在 **代码** 选项卡上，您将看到一个编辑器，可用于编写响应所选主题而执行的 Python 或 Javascript 函数。 ![3.11(2).jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722610658843)

![js.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598751003)

### 处理函数参数

为了让 Klaviyo 执行您编写的代码，必须将其包装在一个名为“handler”的函数中，该函数接受 2 个参数：

- ****活动****
  包含与触发事件关联的 JSON:API 格式的事件数据。如果触发器是非基于事件的（例如，**添加到列表**），则此参数的值将为 **None** 或 **Null**，具体取决于语言。 - ****背景****
  包含有关函数执行的其他元数据，包括与函数调用关联的配置文件。您可以通过 Javascript 中的 **context.profile** 或 Python 中的 **context["profile"]** 访问配置文件对象。以下是传递给处理函数的事件和上下文参数的示例。 ****事件格式示例****

````
{
    {
  “数据”：{
    “类型”：“事件”，
    "id": "7S2q9haejYG",
    “属性”：{
      “时间戳”：1694435729，
      “事件属性”：{
        “MfaEnabled”：假，
        "IP地址": "000.00.0.0",
        "UserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, 如 Gecko) Chrome/116.0.0.0 Safari/537.36",
        “用户角色”：“所有者”，
        "SessionId": "34sh0a9nh8ngnk2nfacjxmt592yx40ib",
        "LoginType": "用户名_密码",
        "current_company_id": "XXXXX",
        “$event_id”：“1694435729”
      },
      “日期时间”：“2023-09-11 12:35:29+00:00”，
      “uuid”：“b0b8fe80-509f-11ee-8001-278cc529fcd3”
    },
    “关系”：{
      “个人资料”：{
        “数据”：{
          “类型”：“个人资料”，
          “id”：“123456”
        },
        “链接”：{
          “自我”：“https://a.klaviyo.com/api/events/7S2q9haejYG/relationships/profile/”，
          “相关”：“https://a.klaviyo.com/api/events/7S2q9haejYG/profile/”
        }
      },
      “公制”：{
        “数据”：{
          “类型”：“公制”，
          “id”：“4Tdup6”
        },
        “链接”：{
          “自我”：“https://a.klaviyo.com/api/events/7S2q9haejYG/relationships/metric/”，
          “相关”：“https://a.klaviyo.com/api/events/7S2q9haejYG/metric/”
        }
      }
    },
    “链接”：{
      “自我”：“https://a.klaviyo.com/api/events/7S2q9haejYG/”
    }
  }
}
````

****上下文格式示例****

````
{
    "company_id": "XXXXX",
    "trigger": {"type": "event", "uid": "123456"},
    “function_id”：“123456”，
}
````

### 模块

在“模块”选项卡上，您可以从最流行的预构建模块中进行选择（即为您的函数添加功能的第 3 方包）。要添加在代码中使用的外部模块，请选择****添加模块****按钮：

![添加模块按钮](https://klaviyo.zendesk.com/hc/article_attachments/28722610608411)

在出现的模式中，您可以搜索并选择要添加的模块：

![添加模块模式](https://klaviyo.zendesk.com/hc/article_attachments/28722598684571)

添加后，您可以将该模块与您在 Klaviyo 中编写的代码一起使用。您应该参阅外部模块的本机文档以获取有关如何使用它的信息。 ![添加模块](https://klaviyo.zendesk.com/hc/article_attachments/28722598687771)

****klaviyo 模块****

所有代码功能都附带一个自定义 **klaviyo** 包，该包已预安装到您的代码环境中。该模块允许您的函数访问 Klaviyo 帐户中的数据，而无需提供任何凭据，例如 API 密钥。 **klaviyo** 模块的 API 取决于您的代码是用 Python 还是 Javascript 编写的。 ### Python **klaviyo** 模块

预安装的 **klaviyo** 模块的 API 与您通常使用 **klaviyo-api** Python 模块实例化的 [Klaviyo SDK](https://github.com/klaviyo/klaviyo-api-python) 对象相同。您可以将 **klaviyo** 模块视为预实例化的 **klaviyo** SDK 客户端。例如，在传统工作流程中，您首先通过将 API 密钥传递给构造函数来实例化新的 Klaviyo SDK 客户端，然后使用生成的 SDK 对象。 ````
from klaviyo_api import KlaviyoAPIimport osdef handler(event, context): klaviyo = KlaviyoAPI(api_key=os.getenv("KLAVIYO_API_KEY")) print(klaviyo.Metrics.get_metrics())
````

使用代码，您只需导入 klaviyo 对象，身份验证就会为您处理。 ````
导入 klaviyodef 处理程序（事件，上下文）： print(klaviyo.Metrics.get_metrics())
````

查看[可用的 Klaviyo 对象及其方法](https://pypi.org/project/klaviyo-api)。 ### Javascript **klaviyo** 模块

在 Javascript 函数中使用预安装的 **klaviyo** 模块时，请使用 **klaviyo** 模块中的大括号语法导入您想要访问的特定 Klaviyo 功能。然后像通常使用 [**klaviyo-api**](https://www.npmjs.com/package/klaviyo-api) [Javascript 模块](https://www.npmjs.com/package/klaviyo-api) 的 API 对象一样使用它们。 ````
import { Metrics } from 'klaviyo';导出默认 async (event, context) => { console.log(await Metrics.getMetrics())}
````

查看[可用的 Klaviyo 对象及其方法](https://www.npmjs.com/package/klaviyo-api)。 ### 环境变量

**环境变量**选项卡允许您设置 Klaviyo 中的代码在运行时可以引用的键值对。它们可用于存储凭据和密钥等信息，以便您的函数可以在运行时访问它们。要添加环境变量，请选择****添加变量****按钮：

![添加环境变量按钮](https://klaviyo.zendesk.com/hc/article_attachments/28722610624539)

在出现的模式中，您可以为环境变量设置键值对。 ![为环境变量设置的键值对](https://klaviyo.zendesk.com/hc/article_attachments/28722610627099)

创建后，环境变量将在页面上列出并可以在您的代码中使用。要访问代码中的环境变量，请使用 os.getenv("Key")（对于 Python）或 process.env.KEY（对于 Node.js）。 ![创建环境变量](https://klaviyo.zendesk.com/hc/article_attachments/28722598707611)

要更新现有环境变量的值，您必须使用要更新其值的相同键创建一个新变量。 ## 测试输出

代码中的 **测试输出** 选项卡允许您使用最近的事件测试代码，以确认输出的行为符合预期。要测试您的功能：

1. 选择****运行测试****按钮：
   ![运行测试按钮](https://klaviyo.zendesk.com/hc/article_attachments/28722598714907)
2. 在出现的模式中，选择要测试的事件。您可以从 Klaviyo 捕获的 10 个最新事件中进行选择。 ![最近要测试的事件](https://klaviyo.zendesk.com/hc/article_attachments/28722610636315)
3. 选择要测试的事件后，将显示测试输出：

![测试输出](https://klaviyo.zendesk.com/hc/article_attachments/28722610618651)

## 日志

**日志**选项卡显示您正在进行的代码功能的运行状况。你会看到：

- ****状态****
  函数执行的进度。 - ****响应时间****
  执行代码以响应事件所需的时间。 - ****日期****
  函数执行时间的时间戳。 ## 速率限制

Klaviyo 代码具有以下速率限制：

- ****函数超时****
  代码中的函数在超时之前最多可以执行 15 秒。 - ****功能速率限制****
  代码中的函数允许每个函数最多 25 个并发执行。 ## 部署代码

要部署您在编辑器中编写的代码，请将状态下拉列表切换为 **Live**。 ![切换部署代码](https://klaviyo.zendesk.com/hc/article_attachments/28722610634139)

设置为实时后，每次在 Klaviyo 中捕获主题事件时，您编写的代码都会执行。当某个功能设置为实时时，事件开始触发该功能之前可能会有最多 15 分钟的延迟。 ## 解决方案示例

以下是使用代码实现的自定义解决方案的示例。在示例中，事件数据被设置为配置文件属性，因此可以在目标电子邮件和分段中使用。当客户向该品牌预订拍摄时，**预订拍摄** 自定义事件会在 Klaviyo 中捕获，并且有关预订城市和关联 URL 的数据将设置为相应个人资料上的个人资料属性。还创建了一个名为 **最近预订** 的属性，它存储来自最近 5 个 **预订拍摄** 事件的数据，以便可以在电子邮件模板中循环和访问。 ### 代码

该解决方案的Python代码是在代码编辑器中编写的，并由Klaviyo直接执行。 ![Code_updates.jpg](https://klaviyo.zendesk.com/hc/article_attachments/32517910641819)

### 示例代码

[“已预订](https://www.napkin.io/api/embed/236e23398bf14a27)

### 模块

在此示例中，使用内置 **klaviyo** 模块。 **klaviyo** 模块依赖于添加到函数中的 **klaviyo-api** 模块。添加后，**klaviyo** 模块将为您处理身份验证，因此不需要 API 密钥。 ### 环境变量

环境变量可用于存储凭据和密钥等信息，以便您的函数可以在运行时访问它们。对于本示例，设置了以下键值对：

- ****MAX\_PROPERTIES\_TO\_STORE****
  用于定义为示例函数存储的最大属性数的环境变量。 ### 测试

创建将事件数据设置为配置文件属性的函数时，**测试输出**选项卡用于验证预期输出。 ![test_output.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722610647323)

### 日志

创建并测试该函数后，**日志**选项卡会显示该函数为响应 **预订拍摄** 事件而执行时的运行状况。 ![Logs.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598726043)

### 结果

有了此代码功能，当客户注册拍摄并触发自定义**预订拍摄**事件时，事件数据将存储在客户档案中，以用于细分和有针对性的活动。 ## 实施食谱

代码中的食谱允许您实施预构建的解决方案，而无需自定义开发。要在您的 Klaviyo 帐户中实施食谱：

1. 选择代码页上的 **创建函数** 按钮。 2. 选择您想要在帐户中实施的方案。您将进入编辑器，在这里您可以看到所选配方的代码以及该函数功能的描述。 3. 单击“**选择**”按钮继续。 ![Klaviyo 中的货币转换器配方](https://klaviyo.zendesk.com/hc/article_attachments/28722598756891)
4. 选择函数的名称以及将导致其执行的触发器。运行时间是根据配方代码自动设置的。 5. 选择**创建函数**按钮。 6. 创建函数后，设置相关的环境变量，以便函数拥有运行所需的数据。 7. 现在可以测试配方并将其设置为 **Live**。食谱可能要求您更新某些字段以匹配您所需的命名首选项和事件中的数据。请参阅配方说明以查看可以重命名和编辑哪些字段。