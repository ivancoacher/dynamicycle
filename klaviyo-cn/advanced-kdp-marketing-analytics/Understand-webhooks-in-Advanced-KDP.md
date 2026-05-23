---
id: "17760478970907"
title: "了解高级 KDP 中的 webhook"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/17760478970907-Understand-webhooks-in-Advanced-KDP"
section: "Webhooks"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:56:43Z"
language: "zh"
---
## 你将会学到

了解 Webhook 以及如何使用它们将信息发送到第三方应用程序，以响应 Klaviyo 中捕获的事件。有关如何接收系统 Webhooks 的更多详细信息，请访问我们的开发人员资源[使用系统 Webhooks](https://developers.klaviyo.com/en/docs/working_with_system_webhooks)。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。 [Klaviyo CDP 视频中的 Webhooks](https://fast.wistia.net/embed/iframe/kwiicwga5w?web_component=true&seo=true)

## 什么是 webhook？ Webhooks 允许 Klaviyo 通过 HTTP 请求传递信息或“调用”其他应用程序、工具和服务器。他们可以发送有关已发生事件的信息（例如下的订单、新客户订阅等）或通知您的外部系统事件已发生。 Klaviyo 支持 2 种 Webhooks：

1.****高级 KDP 中的 Webhooks****
   作为高级 KDP 的一部分提供的 Webhook 用于通知您的外部系统已发生特定事件，并允许您发送信息以响应各种事件，而不受流中的限制。 2.****Flow webhook****
   流 webhook 仅在流界面内可用，并在流到达特定阶段或步骤时触发。它们可用于发送有关触发流的事件或接收者的数据。 ### webhooks 的关键组件

Webhook 由几个关键组件组成：

- ****主题****
  导致 webhook 触发的事件
- ****主体（或“有效负载”）****
  Webhook 发送的数据
- ****标题****
  传递附加信息（例如身份验证）的地方

## 高级 KDP 中的 Webhook 与 Flow Webhook 有何不同？您可以根据需要在高级 KDP 或 Flow webhook 中使用 webhook。 ### 包含的活动

Flow Webhooks 只能响应 Klaviyo 事件的子集，并且不支持与消息相关的事件，例如 **取消订阅**、**收到的电子邮件**或 **点击的电子邮件**，因为流通常以消息接收结束，而不是以消息开始。同时，高级 KDP 中的 Webhooks 允许您发送信息以响应帐户中的任何事件。这些包括：

- 电子邮件事件（例如，**收到电子邮件**、**点击电子邮件**、**将电子邮件标记为垃圾邮件、取消订阅**）
- 短信事件（例如，**发送短信**、**接收短信**）
- 推送通知事件（例如，**收到推送**、**退回推送**）
- 来自集成的事件（即来自 Klaviyo 创建的第一方集成的事件）
- API 事件（例如，通过 [Klaviyo 的 API](https://developers.klaviyo.com/en/reference/api_overview) 同步的事件）

### 有效负载

Flow Webhooks 允许您自定义请求中包含的数据，但您必须手动构建有效负载。同时，高级 KDP 中的 Webhook 使用预构建的有效负载，不需要您进行任何手动操作，并用于通知外部系统已发生事件。 ### 流量限制

流 Webhook 必须在流界面中配置，并且不允许您同时使用多个触发器。不同的触发器必须通过各个流创建，并且取决于流的整体状态（例如，草稿中的流不会通过流 webhook 发送数据）。同时，高级 KDP 中的 Webhook 存在于 Flows 接口之外，并且不像 Flow Webhook 那样依赖于导致 Webhook 操作的一系列步骤。 ## 设置网络钩子

要在 Klaviyo 中设置 Webhook，请导航至 Klaviyo 中****高级 KDP**** ****>**** ****数据管理 > Webhooks**** 下的 **Webhooks**。要添加新的 Webhook，请单击****创建 Webhook**** 按钮。 1. 在 **创建 Webhook** 模式中，输入信息。这包括：
   - ****姓名****
     如何识别您的网络钩子
   - ****端点 URL****
     与 Webhook 请求的目标关联的 URL
   - ****秘密密钥****
     用于识别其他系统中的 Klaviyo Webhook 请求的唯一标识符
   - ****描述****
     Webhook 的可选描述。 2. 在 **主题** 部分中，选择您想要触发 Webhook 通知的事件

![创建 webhook 模式](https://klaviyo.zendesk.com/hc/article_attachments/28704486678683)

回调 URL 必须：

- 是有效的 URL 格式
- 以 HTTPS:// 开头
- 没有自签名 SSL 证书
- 不重定向到另一个 URL

创建 Webhook 后，它将与以下内容一起列在 **Webhooks** 页面上：

- 网络钩子名称
- 网络钩子 URL
- 最近一次同步的时间
- 状态

![已创建的 webhook 列表](https://klaviyo.zendesk.com/hc/article_attachments/28704478568859)

请注意，Webhook 最多可能需要 15 分钟才能开始发送到 URL。您可以使用该项目旁边的菜单删除或禁用 Webhook。 ## 测试系统网络钩子

在 Klaviyo 中设置 Webhook 时，您可以对其进行测试以确保连接成功。要测试您的 Webhook，请在输入必填字段后使用****测试连接****按钮。 ![测试连接.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39030496797723)

将出现一个菜单，您可以在其中选择主题并将测试发送到您的回调 URL。 ![测试 webhook 模式](https://klaviyo.zendesk.com/hc/article_attachments/28704478571931)

执行测试后，您将看到一条消息，指示测试是否成功，以及**响应**选项卡中填充的请求的标头和正文。要验证 Webhook 通知是否来自 Klaviyo，请使用您创建的密钥来识别请求。 ![测试成功指标](https://klaviyo.zendesk.com/hc/article_attachments/28704478574491)

## 负载示例

以下是响应 **电子邮件已发送** 主题的 Webhook 请求的负载示例。请注意，根据您的帐户特定数据，有效负载可能会有所不同。 ````
{
  “元”：{
    "时间戳": "2023-08-10T07:25:23.700369+00:00",
    "klaviyo_webhook_id": "ID",
    “版本”：“2023-06-03”
  },
  “数据”：[
    {
      "topic": "事件：email_delivered",
      "external_id": "ID",
      “有效负载”：{
        “数据”：{
          “id”：“ID”，
          “类型”：“事件”，
          “链接”：{
            “自我”：“https://a.klaviyo.com/api/events/ID/”
          },
          “属性”：{
            “uuid”：“96150200-374e-11ee-8001-a163313bc6c2”，
            “日期时间”：“2023-08-10 07:21:56+00:00”，
            “时间戳”：1691652116，
            “事件属性”：{
              “$ESP”：0，
              “主题”：“？免费（酷！）赃物警报？”，
              "$message": "01H7F525FKR31P27Y7PNGVBBKK",
              "$event_id": "01H7F525FKR31P27Y7PNGVBBKK:125423419905414052533228990613763937641",
              “$group_ids”：[
                “V7adxq”
              ],
              “$属性”：{
                “$send_ts”：0，
                “$attributed_event_id”：“”
              },
              “电子邮件域名”：“klaviyo-demo.com”，
              “活动名称”：“每日通讯：2023-08-10”，
              "Inbox Provider": "Amazon SES 入站",
              "$_cohort$message_send_cohort": "1691652081:01H7F525FKR31P27Y7PNGVBBKK"
            }
          },
          “关系”：{
            “公制”：{
              “数据”：{
                “id”：“ID”，
                “类型”：“公制”
              },
              “链接”：{
                “自我”：“https://a.klaviyo.com/api/events/ID/relationships/metric/”，
                “相关”：“https://a.klaviyo.com/api/events/ID/metric/”
              }
            },
            “个人资料”：{
              “数据”：{
                “id”：“ID”，
                “类型”：“个人资料”
              },
              “链接”：{
                “自我”：“https://a.klaviyo.com/api/events/ID/relationships/profile/”，
                “相关”：“https://a.klaviyo.com/api/events/ID/profile/”
              }
            }
          }
        }
      }
    },
````

## 其他资源

[如何将 webhook 操作添加到流](https://developers.klaviyo.com/en/docs/how_to_add_a_webhook_action_to_a_flow)

[了解 Klaviyo webhooks](https://help.klaviyo.com/hc/en-us/articles/4534329515931)

[使用系统 Webhooks（Klaviyo 的 Webhooks API）](https://developers.klaviyo.com/en/docs/working_with_system_webhooks)