---
id: "20016490907163"
title: "同意参考的流量过滤的更改"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/20016490907163-Changes-to-flow-filtering-on-consent-reference"
section: "Understand flows"
category: "Flows"
category_slug: "flows"
klaviyo_updated: "2026-04-21T13:56:45Z"
language: "zh"
---
## 你将会学到

了解 Klaviyo 在流程中的个人资料过滤的更新，使您能够过滤同意记录。 ## 通过电子邮件发送同意条件变更

随着 Klaviyo 对流程中个人资料过滤的更新，以下电子邮件同意条件会受到影响：

****识别未被抑制的配置文件****

旧过滤条件：

- 如果有人被或未被禁止发送电子邮件 >
  人没有被压抑
  ![“人不受压制”的旧个人资料过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722611148699)

新的过滤条件：

- 如果某人可以或不能接受营销>
  人可以接收电子邮件营销
  ![“人员可以接收电子邮件营销”的新个人资料过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722611161371)

****识别被抑制的配置文件****

旧过滤条件：

- 如果有人被或未被禁止发送电子邮件 >
  人被压制了
  ![“人被压制”的旧过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722599205275)

新的过滤条件：

- 如果某人可以或不能接受营销>
  此人无法接收电子邮件营销
  ![“人员无法接收电子邮件营销”的新过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722599228827)

****识别已订阅且未被抑制的配置文件****

旧条件：

- 如果有人被或未被禁止发送电子邮件 >
  人没有被压抑

和

- 如果某人在或不在列表中 >
  此人位于[订阅者列表名称]中
  ![“人员不受抑制”和“人员在列表中”的旧过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722611151387)

新条件：

- 如果某人可以或不能接受营销>
  人可以接收电子邮件营销>
  因为人们订阅了电子邮件营销
  ![“人员可以接收电子邮件营销”的新过滤器和“人员订阅”的过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722611164315)

## 短信同意条件变更

随着 Klaviyo 对个人资料过滤器的更新，以下 SMS 同意条件会受到影响：

****识别同意短信的配置文件****

旧条件：

- 如果有人同意或不同意接收短信>
  此人同意接收短信
  ![“同意接收短信的人”的旧过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722611153435)

新条件：

- 如果某人可以或不能接受营销>
  人可以接收短信营销
  ![“人员可以接收短信营销”的新过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722611166235)

****识别不同意短信的配置文件****

旧条件：

- 如果有人同意或不同意接收短信>
  此人不同意接收短信
  ![旧过滤器“不同意接收短信的人”](https://klaviyo.zendesk.com/hc/article_attachments/28722611155867)

新条件：

- 如果某人可以或不能接受营销>
  个人无法接收短信营销
  ![“人员无法接收短信营销”的新过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722599234075)

## 移动推送同意条件变更

随着 Klaviyo 对个人资料过滤器的更新，以下推送通知同意条件会受到影响：

****识别具有移动推送令牌的配置文件****

旧条件：

- 如果有人有推送令牌>
  人有推送令牌
  ![“人有推送令牌”的旧过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722599220251)

新条件：

- 如果某人可以或不能接受营销>
  人可以接收移动推送营销
  ![“人员可以接收移动推送营销”的新过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722611170203)

****识别没有移动推送令牌的配置文件****

旧条件：

- 如果有人有推送令牌>
  该人没有推送令牌
  ![“人员没有推送令牌”的旧过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722611160091)

新条件：

- 如果某人可以或不能接受营销>
  用户无法接收移动推送营销
  ![“人员无法接收移动推送营销”的新过滤器](https://klaviyo.zendesk.com/hc/article_attachments/28722599243419)

## 新功能

通过配置文件过滤的更新，您还可以过滤配置文件如何订阅或取消订阅，以及其被抑制的原因（仅限电子邮件）。 ****识别通过特定方法（电子邮件）订阅的个人资料****

- 如果某人可以或不能接受营销>
  人可以接收电子邮件营销>
  因为此人订阅了电子邮件营销 >
  订阅方式为Klaviyo form [表单名称]
  ![使用订阅方法过滤“人员无法接收电子邮件营销”](https://klaviyo.zendesk.com/hc/article_attachments/28722599247899)

在此条件下，您还可以过滤：

- 订阅方式
- 方法细节
- 自定义方法细节
- 订阅日期
- 如果个人资料被双重选择

****识别通过特定方法（短信）订阅的个人资料****

- 如果某人可以或不能接受营销>
  人可以接收短信营销 >
  订阅方式为Klaviyo形式
  ![过滤‘persn可接收短信营销’及订阅方式](https://klaviyo.zendesk.com/hc/article_attachments/28722611186843)

****识别具有从未订阅状态的个人资料（电子邮件）****

- 如果某人可以或不能接受营销>
  人可以接收电子邮件营销>
  因为人们从未订阅过电子邮件营销
  ![过滤“人员可以接收电子邮件营销”且从未订阅](https://klaviyo.zendesk.com/hc/article_attachments/28722611208731)

****识别具有从未订阅状态的个人资料（短信）****

- 如果某人可以或不能接受营销>
  无法接收短信营销 >
  因为人们从未订阅过短信营销
  ![过滤“人员无法接收短信营销”并且从未订阅](https://klaviyo.zendesk.com/hc/article_attachments/28722599252635)

****识别由于特定原因取消订阅的个人资料****

- 如果某人可以或不能接受营销>
  此人无法接收电子邮件营销>
  因为有人取消订阅电子邮件营销>
  而取消订阅方法就是取消订阅页面
  ![过滤“无法接收电子邮件营销的人”和取消订阅方法](https://klaviyo.zendesk.com/hc/article_attachments/28722599261083)

您还可以过滤：

- 取消订阅方法
- 方法细节
- 取消订阅日期

****识别由于特定原因而被抑制的配置文件****

- 如果有人可以或不能接收电子邮件营销>
  此人无法接收电子邮件营销>
  因为电子邮件营销中的人被手动禁止
  ![过滤“人员无法接收电子邮件营销”，因为人员被手动抑制](https://klaviyo.zendesk.com/hc/article_attachments/28722611198363)

您可以过滤抑制，因为：

- 取消订阅
- 手动抑制
- 无效的电子邮件
- 硬退回电子邮件

## 其他资源

[了解 Klaviyo 中的同意](https://help.klaviyo.com/hc/en-us/articles/360037101072)