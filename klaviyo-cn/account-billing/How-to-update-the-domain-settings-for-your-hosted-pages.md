---
id: "360052334451"
title: "如何更新托管页面的域设置"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360052334451-How-to-update-the-domain-settings-for-your-hosted-pages"
section: "Domains and hosting"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:54:51Z"
language: "zh"
---
## 你将会学到

了解如何更新 Klaviyo 中托管页面的专用域设置。在大多数情况下，如果您在 Klaviyo 中托管了内容管理系统 (CMS) 的页面，那么您将需要执行此操作，CMS 是一种用于创建、修改和管理数字内容（例如 WordPress）的软件。

## 更新托管页面的专用域设置

1. 单击左下角您的帐户名称。
2. 选择****设置 > 其他 >**** [****同意页****](https://www.klaviyo.com/settings/other/consent-pages)。
3. 向下滚动到**自定义托管页面**部分。
4. 如果您[为您的帐户启用了托管页面](https://help.klaviyo.com/hc/en-us/articles/115005077067#h_01J5970D8J98RVN0GADKN2VJ6W)，您将在此页面底部看到用于更新内容管理设置的选项。
5. 选择一个主机名（子域 + 您的域）并将其 CNAME 记录添加到您的域名服务 (DNS)。
   - 例如，如果您拥有一家名为 The Book Exchanger 的公司，则此处选择的主机名可能是：**pages.bookexchanger.com**，其中“pages”是任意选择的子域，“bookexchanger.com”是您的业务域。
   - 此主机名将用作您帐户的 **内容管理设置** 部分中提供的 yourbusiness.myklpages.com 域的别名。对于 The Book Exchanger 的示例，配置可能如下所示：

     ![](https://klaviyo.zendesk.com/hc/article_attachments/28717382438171)
6. 确保 CNAME 记录如下所示：

   |  |  |  |
   | --- | --- | --- |
   | ****类型**** | ****主机名**** | ****价值**** |
   | **别名** | **pages.bookexchanger.com** | **bookexchanger.myklpages.com** |

7. 在 **托管页面专用域** 下的框中，确保该值显示为：****[子域].[您的域]****
   - 示例：pages.bookexchanger.com
8. 当您确认此信息准确反映您添加的 CNAME 记录后，单击****更新专用域设置****将此信息保存到您的帐户中。

## 其他资源

- [如何将同意页面翻译成不同语言](https://help.klaviyo.com/hc/en-us/articles/360049498631)
- [如何自定义代码同意页面](https://help.klaviyo.com/hc/en-us/articles/115005077067)