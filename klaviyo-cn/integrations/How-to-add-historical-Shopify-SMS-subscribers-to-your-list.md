---
id: "25184840445467"
title: "如何将历史 Shopify SMS 订阅者添加到您的列表"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/25184840445467-How-to-add-historical-Shopify-SMS-subscribers-to-your-list"
section: "Shopify best practices"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:47Z"
language: "zh"
---
## 你将会学到

了解如何将历史 Shopify SMS 订阅者添加到您的 Klaviyo SMS 列表。虽然历史电子邮件订阅者会通过 Klaviyo 的 Shopify 集成自动同步，但历史短信订阅者则不会。相反，必须通过以下过程手动添加它们。

## 开始之前

如果您尚未将 Shopify 商店与 Klaviyo 集成，请先参阅 [Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407)，然后再继续阅读本文。

## 如何添加历史短信订阅者

将历史短信订阅者添加到您的电子邮件列表需要 4 个步骤：

1. 从 Shopify 下载您的订阅者列表。
2. 编辑您的列表以仅包含 SMS 订阅者。
3. 将编辑后的列表上传到Klaviyo。
4. 将上传的列表与您在 Klaviyo 中的首选列表合并。

### 从 Shopify 下载您的客户列表

1. 在您的 Shopify 后台中，前往****客户****。
2. 单击右上角的****导出****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717881991579)
3. 选择****所有客户****。
4. 如果您想包含标签和/或元字段，请选择它们。
5. 选择 ****Excel、Numbers 或其他电子表格程序的 CSV****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717881994651)
6. 准备好后，单击****导出客户****。
7. 如果成功，Shopify 将通过电子邮件向您发送订阅者的 CSV 文件。
8. 前往您的收件箱并下载从 Shopify 发送的文件。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717881996699)

### 编辑您的列表以仅包含短信订阅者

1. 在您首选的电子表格程序中打开从 Shopify 下载的 CSV 文件。
2. 找到**接受短信营销**列。
3. 将此列重命名为**短信营销**同意。
4. 在此列中，更改以下内容：
   - “是”改为“订阅”。
   - 从“否”改为“从未订阅”。
5. 保存您的 CSV 文件。

### 将您的列表上传到 Klaviyo

1. 导航至****受众 > 列表和细分****。
2. 通过选择****新建>列表****来创建新列表。
3. 为您的列表命名，然后单击****新建****。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32805244586779)
4. 在下一页上，选择****导入联系人****。
5. 单击****上传****，然后选择要上传的 CSV 文件。
6. 仅映射以下列（其他必要的属性通过我们的集成同步）：
   - 电子邮件 > 电子邮件
   - 电话 > 电话号码
     ![](https://klaviyo.zendesk.com/hc/article_attachments/28717888051611)
7. 如果您有**短信营销同意栏**，则同意将自动应用于标记为“订阅”的任何人。
8. 单击 ****导入****。

处理导入可能需要一些时间。完成后将被标记为**已完成**。导入完成后，继续下一步。
![](https://klaviyo.zendesk.com/hc/article_attachments/28717882006427)

### 将上传的列表与您在 Klaviyo 中的列表合并

1. 导航至****受众 > 列表和细分****。
2. 单击您从 Shopify 上传的列表。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32805259414683)
3. 打开****管理列表****下拉列表。
4. 选择****合并列表****。
   ![合并列表按钮.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28717882013211)
5. 您需要选择用于短信订阅者的列表。您需要使用在 [Shopify 集成设置](https://help.klaviyo.com/hc/en-us/articles/115005080407#h_01HSERAG9Y1DNHNSCHTKV3G04D) 中选择的相同列表。
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32805259416091)
6. 选择是保留还是删除从 Shopify 上传的列表。
7. 单击 ****合并****。

合并过程可能需要几分钟。有关合并列表的更多信息，请参阅我们的[列表合并常见问题解答](https://help.klaviyo.com/hc/en-us/articles/115005078887#h_01H8YXX41PKBPHHVFJ751BD6CR)。

## 结果

您现在已将历史 Shopify SMS 订阅者添加到您的 Klaviyo 列表中。

## 其他资源

- [Shopify 入门](https://help.klaviyo.com/hc/en-us/articles/115005080407)
- [如何将 Shopify 电子邮件订阅者同步到 Klaviyo 列表](https://help.klaviyo.com/hc/en-us/articles/115005080667)