---
id: "15311862315803"
title: "排除 PrestaShop 授权错误 PHP 作为 CGI"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/15311862315803-Troubleshooting-PrestaShop-authorization-error-PHP-as-CGI"
section: "PrestaShop"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:29Z"
language: "zh"
---
## 你将会学到

了解如何解决在 PrestaShop 中配置 Klaviyo 模块时出现的授权问题“您似乎正在将 PHP 作为 CGI 运行”。解决此问题需要更改 PrestaShop 中的设置，然后重新生成 .htaccess 文件。按照本文中的步骤正确完成与 PrestaShop 的集成。
![](https://klaviyo.zendesk.com/hc/article_attachments/35197436760091)

## 开始之前

如果您对 .htaccess 文件进行了任何手动代码更改，请注意以下步骤将强制 PrestaShop 重新生成文件并删除它们。

## 解决步骤

1. 在 PrestaShop 中，导航至****高级参数 > Web 服务****。
2. 打开**启用 PHP CGI 模式**，然后单击****保存****。
   ![PrestaShop 中的设置页面显示已启用 PHP 的 CGI 模式](https://klaviyo.zendesk.com/hc/article_attachments/28713385281179)
3. 要重新生成 .htaccess 文件，请导航至****商店参数 > 流量和 SEO****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35197407426843)
4. 单击****保存****（您无需进行任何更改）。单击此处的“保存”会强制 PrestaShop 重新生成 .htaccess 文件，在打开 CGI 开关的情况下，该文件将解决授权问题。

现在，您可以返回模块设置页面并继续集成过程。

## 其他资源

- [PrestaShop 入门](https://help.klaviyo.com/hc/en-us/articles/360054551492)
- [PrestaShop数据参考](https://help.klaviyo.com/hc/en-us/articles/360055123191)
- [Klaviyo 社区](https://community.klaviyo.com/)