---
id: "16680027976731"
title: "收到负面评论时如何创建客户服务票"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16680027976731-How-to-create-a-customer-service-ticket-when-you-receive-a-negative-review"
section: "Build and use reviews"
category: "Reviews"
category_slug: "reviews"
klaviyo_updated: "2026-04-20T16:48:53Z"
language: "zh"
---
## 你将会学到

了解如何在 Klaviyo 中创建流程，以便在有人提交负面评论时创建客户服务票证。通知您的客户服务团队可以让他们主动联系并纠正您的客户可能拥有的任何负面体验。

## 创建负面评论流程

首先，创建一个流：

1. 单击 Klaviyo 左侧导航栏中的 ****Flows****。
2. 单击****创建流程****。
3. 单击****从头开始创建****。
   ![从头开始创建流程](https://klaviyo.zendesk.com/hc/article_attachments/28715972707483)
4. 将您的流程命名为描述性名称，然后单击****创建流程****。
5. 在**什么会触发此流程？**下，选择****指标****。
6. 从**什么操作将触发此流程？**菜单中，选择****已提交的审核****。
7. 单击****触发过滤器 > 添加触发过滤器****。
8. 设置以下触发过滤器：
   ****评论\_评级 > 最多 > 3****

   这将识别提交 1 星、2 星或 3 星评论的客户。如果需要，您可以使用不同的号码。

![评论评分触发过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28715966169499)

## 添加电子邮件通知操作

接下来，添加一个操作来通知您的客户服务团队有关负面评论的信息。

1. 在触发器正下方的流程中添加 ****Notification**** 操作。
   ![通知操作](https://klaviyo.zendesk.com/hc/article_attachments/28715972713627)
2. 在通知的 **发送至** 字段中，添加您的客户支持电子邮件地址。
3. 设置主题，例如“{{ event.review\_author|default:'Someone' }} 提交了 {{ event.review\_ rating }} 星级评论”。
   ![通知操作主题行](https://klaviyo.zendesk.com/hc/article_attachments/28715972705051)
4. 添加包含评论详细信息的正文，例如：
   评级：{{ event.review\_ rating }}
   评论正文：{{ event.review\_content }}
   客户姓名：{{ event.review\_author }}
   客户电子邮件：{{ event.review\_email }}
5. 单击****保存****。

## 设置直播流

自定义通知操作后，单击****查看并设置实时****以将流程设置为实时。任何未来的负面评论都会自动发送给您的客户服务团队，然后他们可以主动联系客户。

如果您的客户服务团队能够解决投诉，他们可以指示审阅者在提交后 30 天内返回原始审阅请求电子邮件，并根据需要编辑其审阅。