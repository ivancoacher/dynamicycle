---
id: 7210
title: "一个 Shopify 店铺需要对应几个 Klaviyo 账户？"
slug: "shopifyaccountklaviyo"
category: "DC 官方资源中心"
category_slug: "dc-resources"
wp_url: "https://dynamicycle.com/docs/shopifyaccountklaviyo/"
wp_modified: "2026-03-13T02:14:04"
---

在为 Shopify 品牌搭建 Klaviyo 邮件与短信营销系统时，经常会遇到一个问题：多语言或多国家站点，是否需要多个 Klaviyo 账户？

判断逻辑其实很简单，核心只有一个原则：Shopify 店铺数量决定 Klaviyo 账户数量。

##### ****核心原则：一个 Shopify = 一个 Klaviyo 账户****

Klaviyo 的数据是直接与 Shopify 店铺进行同步的，包括：

- 订单数据
- 用户数据
- 商品数据
- 浏览行为

因此：****一个 Shopify 店铺必须绑定一个 Klaviyo 账户。****

如果品牌拥有多个 Shopify 店铺（多个后台），那么：

- 每个 Shopify 店铺
- 都需要独立的 Klaviyo 账户

##### ****不同域名结构，对 Klaviyo 的影响****

###### ****情况 1：独立国家域名****

例如：

- [jiazhibo.fr](https://jiazhibo.fr)
- [jiazhibo.es](https://jiazhibo.es)

如果每个域名背后对应的是 ****独立的 Shopify 店铺****，那么：****每个站点都需要独立的 Klaviyo 账户****

结构示例：

|  |  |  |
| --- | --- | --- |
| ****域名**** | ****Shopify**** | ****Klaviyo**** |
| jiazhibo.fr | Shopify A | Klaviyo A |
| jiazhibo.es | Shopify B | Klaviyo B |

###### ****情况 2：子域名结构****

例如：

- <https://fr.jiazhibo.com>
- <https://es.jiazhibo.com>

如果这些子域名 ****都属于同一个 Shopify 店铺****（通常通过 Shopify Markets 实现多国家市场），那么：****可以共用一个 Klaviyo 账户****

结构示例：

|  |  |  |
| --- | --- | --- |
| ****域名**** | ****Shopify**** | ****Klaviyo**** |
| fr.jiazhibo.com | Shopify A | Klaviyo A |
| es.jiazhibo.com | Shopify A | Klaviyo A |

###### ****情况 3：目录语言结构****

例如：

- <https://jiazhibo.com/fr>
- <https://jiazhibo.com/es>

这类结构通常也是 ****同一个 Shopify 店铺的多语言页面****。

因此：****同样可以使用一个 Klaviyo 账户****

##### ****总结判断逻辑****

可以用一句话快速判断：****看 Shopify 后台数量，而不是看域名数量。****

规则如下：

|  |  |
| --- | --- |
| ****Shopify 店铺数量**** | ****Klaviyo 账户**** |
| 1 个 Shopify | 1 个 Klaviyo |
| 2 个 Shopify | 2 个 Klaviyo |
| 3 个 Shopify | 3 个 Klaviyo |

无论域名是：

- 国家域名
- 子域名
- 目录结构

****只要 Shopify 是同一个后台，就可以共用一个 Klaviyo。****

##### ****实际品牌架构建议****

对于做全球化 DTC 品牌的企业，通常有两种架构：

###### ****架构 A（推荐）****

一个 Shopify + Shopify Markets

- jiazhibo.com
- jiazhibo.com/fr
- jiazhibo.com/es
- jiazhibo.com/de

优点：

- 一个 Klaviyo 即可管理全球用户
- 数据统一
- 生命周期营销更完整

###### ****架构 B****

多国家独立 Shopify

- jiazhibo.fr
- jiazhibo.es
- jiazhibo.de

缺点：

- 需要多个 Klaviyo 账户
- 用户数据割裂
- 营销策略难统一

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)