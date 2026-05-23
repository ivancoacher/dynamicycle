---
id: "22698234676507"
title: "Dutchie POS 数据参考"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/22698234676507-Dutchie-POS-data-reference"
section: "Dutchie POS"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:34Z"
language: "zh"
---
此参考资料涉及 Dutchie v1 集成，该集成由 Klaviyo 构建，不再允许新安装。新客户应该使用由 KAV Labs 构建的 [Klaviyo 应用程序市场中的 Dutchie 集成](https://marketplace.klaviyo.com/en-us/apps/01KHYQR9B6SBS6Z9WY49PVNYX4)。请访问 [KAV Labs 帮助中心](https://kavlabs.co/documentation/dutchie) 了解更多信息。

## 你将会学到

了解哪些数据从 Dutchie POS 同步到 Klaviyo、如何查看数据以及 Dutchie 事件包含哪些属性。此外，了解如何在 Klaviyo 中查看 Dutchie 数据。

如果您还没有阅读我们的文章 [Dutchie POS 入门](https://help.klaviyo.com/hc/en-us/articles/22698258709531)，了解有关如何集成的分步说明以及其他注意事项，然后再继续阅读本文。

## 数据从 Dutchie POS 同步到 Klaviyo

要检查从 Dutchie POS 到 Klaviyo 的数据同步：

1. 在您的 Klaviyo 帐户中，选择****分析 > 指标****。
2. 在顶部，按 **Dutchie** 进行过滤。

![](https://klaviyo.zendesk.com/hc/article_attachments/28716118875035)

从 Dutchie 同步到 Klaviyo 的数据包括：

- 与订单事件相关的个人资料信息。
- 以下订单事件：
  - **已下订单**
  - **订购的产品**

## 客户信息详情

Klaviyo 只会同步具有电子邮件地址的个人资料。我们建议在 Dutchie Ecommerce 中打开设置 **需要电子邮件地址进行访客结帐**，该设置可以在****设置 > 选项 > 结帐**** 下找到。电子邮件地址将同步到 Dutchie POS。

在电子商务结账期间同意电子邮件营销的客户不会同步到 Dutchie POS，因此：

- 从 Dutchie POS 同步到 Klaviyo 的个人资料均未显示为明确同意电子邮件营销。
  - Klaviyo 将 Dutchie 的同步个人资料标记为 **从未订阅**。
  - 标记为**从未订阅**的个人资料在技术上可以接收电子邮件，尽管他们没有提供明确的同意。

    客户资料信息从 Dutchie 同步到 Klaviyo，具有以下属性：
- 电子邮件
- 电话\_号码
- 名字\_name
- 姓氏\_name
- 出生日期
- Dutchie 在位置创建
- Dutchie 创建日期
- Dutchie 客户 ID
- Dutchie 客户类型
- Dutchie 是忠诚会员
- Dutchie 最后修改日期UTC
- 荷兰人身份

## 同步事件及其属性

### 已下订单

**已下订单** 事件从 Dutchie POS 同步到 Klaviyo，具有以下属性：

- 订单编号
- 物品
- 交易类型
- 地点名称
- $事件\_id
- 价值$

### 订购的产品

仅当以下属性已[添加到 Dutchie POS Backoffice 目录中](https://support.dutchie.com/hc/en-us/articles/12882361852563-Add-products-to-Catalog) 时才会收到。建议检查目录以确保所有信息完整。

订购产品事件从 Dutchie POS 同步到 Klaviyo，具有以下属性：

- 应变
- 菌株类型
- 品牌名称
- 交易ID
- 产品编号
- 总价
- 数量
- 单价
- 单位成本
- 包ID
- 源包 ID
- 总折扣
- 单位ID
- 单位重量
- 单位重量单位
- 花当量
- 花当量单位
- 折扣
- 税收
- 返回日期
- 已退回
- 按交易ID返回
- 退货原因
- 批次名称
- 交易项目ID
- 地点名称
- 供应商
- 是优惠券
- 客户ID
- 交易日期
- $事件\_id
- 价值$