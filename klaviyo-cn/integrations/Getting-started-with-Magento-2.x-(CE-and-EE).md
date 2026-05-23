---
id: "115005254348"
title: "Magento 2.x 入门（CE 和 EE）"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115005254348-Getting-started-with-Magento-2-x-CE-and-EE"
section: "Magento 2"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:40Z"
language: "zh"
---
## 你将会学到

了解如何将 Klaviyo 与您的 Magento 2 CE 或 EE 商店集成。您需要在 Magento 中安装 Klaviyo 扩展，配置扩展并设置 OAuth，然后在 Klaviyo 中启用集成。本指南涵盖了所有必需的集成步骤，以及如何确认历史数据同步成功。 ## 开始之前

请注意，不支持 2.4.0 以下的 Magento 2 版本。为了确保 Klaviyo 可以进行必要的 API 调用以进行集成，您的 Magento 2 服务器必须具有可公开访问的主机名。本地托管的 Magento 2 服务器将无法与 Klaviyo 完全集成。 Klaviyo 的 Magento 2 扩展应通过 Composer 安装。请注意，通过 Composer 安装需要 IT 管理员能够通过 SSH 访问托管 Magento 2 的服务器。 ## 在 Magento 2 中安装 Klaviyo 扩展

![](https://fast.wistia.com/embed/medias/yc7dejd9jw/swatch)

1. 登录到 Magento 2 服务器并从命令行工具导航到 Magento 应用程序的根目录。本指南显示了终端的示例输出，但可以针对您选择的任何命令行工具修改这些步骤。 2. 运行以下命令以从 Packagist 访问最新版本的 Klaviyo 扩展。 Packagist 是 PHP 代码库的存储库，可让您轻松安装最新版本的扩展。 `作曲家需要 klaviyo/magento2 扩展`
3. 运行以下命令启用您刚刚下载的 Klaviyo 扩展：
   `php bin/magento 模块：启用 Klaviyo_Reclaim --clear-static-content`
   ![composer2.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758835867)
4. 如示例输出所示，您现在必须启用所有其他模块。运行以下命令来启用它们：
   `php bin/magento 设置：升级`
5. 扫描“Module 'Klaviyo_Reclaim'”的输出，以确认 Klaviyo 模块已启用并正在运行。 6. 为了确保 Magento 2 商店上的 CSS 和 JS 继续正常工作，您需要运行静态内容部署命令。 `php bin/magento 设置：静态内容：部署 -f`
   ![composer3.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770744219)
7. 您现在可以从浏览器返回 Magento 管理仪表板。通过 Composer 安装完成！继续下一节了解配置说明。 ## 配置 Klaviyo 扩展

### 操作方法视频

![](https://fast.wistia.com/embed/medias/m7vqtc4psz/swatch)

1. 在您的 Klaviyo 帐户中，导航至 [API 密钥选项卡](https://www.klaviyo.com/settings/account/api-keys)。 2. 在新选项卡中，导航到您的 Magento 商店管理员。 3. 在**设置**下，单击****商店********>********配置****。 4. 从 Klaviyo 下拉列表中，单击****常规****。 5. 将**启用 Klaviyo 扩展**设置为****是****。 6. 从 API 密钥选项卡复制您的六位数 Klaviyo 公共 API 密钥，并将其粘贴到 Magento 中的相应框中。 7. 在 Klaviyo API 密钥选项卡上，生成新的私钥，然后将其粘贴到 Magento 中的相应框中。使用您的私有 API 密钥进行身份验证将允许您将新闻通讯订阅从 Magento 同步到 Klaviyo。在下一部分中，您将设置 OAuth，它支持集成的其他方面。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720770782235)

### 设置 OAuth

接下来，您将启用 OAuth 身份验证以将您的 Klaviyo 帐户安全地连接到 Magento 2 扩展。 1. 导航到 Magento 中的****设置 OAuth**** 选项卡。 2. 为您的集成指定一个容易记住的名称，因为稍后您需要通过该名称找到它。 3. 单击****保存配置****继续。 ![OAUTHtab.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758843931)
4. 在左侧导航窗格中找到****系统****，然后从**系统**托盘中选择****集成****。 5. 找到您的集成名称并单击****激活****。激活集成将打开一个窗口，请求您批准访问。 ![activateoauth.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770752923)
6. 单击 ****允许**** 重定向到 Klaviyo，您将在其中完成集成设置。 ![oauthperms.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770756379)
7. 如果出现提示，请登录 Klaviyo，或确认您的帐户名正确，然后单击 ****集成。**** 这会将 Magento 2 集成添加到与您用于设置的 API 密钥关联的 Klaviyo 帐户。如果您登录了多个 Klaviyo 帐户并且未显示正确的帐户，请注销任何其他会话。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720758864027)

如果窗口自动关闭，则连接成功。您还可以通过在新的浏览器选项卡或窗口中打开您的 Klaviyo 帐户、选择****集成****选项卡并在列表中查找 Magento 2 来确认成功。如果您收到以下错误，请确保第一步中使用的 API 密钥与您当前登录的帐户相对应。 ![apierror.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770768027)

在 Magento 和 Klaviyo 之间建立连接时，如果您收到错误列表，则可以单击每个错误以了解有关原因的更多信息。 ![oauthgenerror.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758849819)

### 设置时事通讯列表

接下来，您将选择一个 Klaviyo 列表来同步您的时事通讯订阅者。您还可以选择对所选列表使用 Klaviyo 选择加入设置或 Magento 2 选择加入设置。 1. 在 Magento 中，单击****新闻通讯****。 2. 从下拉列表中选择您想要将 Magento 注册表单同步到的 Klaviyo 列表。 3. 单击****保存配置****。 ![newsletterm2.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758855579)

### 结帐时启用同意

接下来，您可以选择在结账时启用电子邮件和短信同意。请注意，如果您在结账时启用同意，您还需要启用 Webhook（如下），以便结账时同意正常运行。 1. 在 **配置** 页面上的 **Klaviyo** 下，导航至****结账时同意****。 ![m2cac-new.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758860571)
2. 您将看到用于收集电子邮件同意和短信同意的部分。两者是分开处理的，因此您可以仅收集电子邮件、短信或两者都收集。如果您同时收集短信和电子邮件订阅者，请为短信选择与电子邮件不同的列表。这可以确保同意始终正确地归因于正确的渠道。 - 在客户完成下订单并（如果适用）通过双重选择确认其订阅之前，同意不会同步（对于电子邮件和短信）。 - 请注意，对于已经登录 Magento 2 商店的用户，默认情况下结账时不会出现电子邮件同意复选框。 3. 在“**电子邮件**”下，为“结账时为联系人订阅电子邮件营销**”选择“****是****”。 4. 选择要同步订阅者的电子邮件列表，例如新闻通讯。 5. 输入您要使用的电子邮件选择加入复选框文本。 ![2021-03-24_13-00-56.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758831387)
6. 在 **SMS** 下，为 **在结账时为联系人订阅 SMS 营销** 选择 **是****。 7. 选择您希望 SMS 联系人同步的列表。有关这些设置的更多详细信息，请查看我们的[在结帐时收集短信同意]指南(https://help.klaviyo.com/hc/en-us/articles/360058698511-How-to-Collect-SMS-Consent-at-Checkout-on-Magento-2)。 ![m2smscac.png](https://klaviyo.zendesk.com/hc/article_attachments/28720758825755)
8. 排序顺序允许您更改电子邮件和短信同意框的位置。默认情况下，这些框分别显示在第一个电子邮件输入和送货电话号码字段下。因此，如果您没有重新排列结帐页面，则无需更改排序顺序。如果您更改了布局，请相应地调整排序顺序。 9. 完成后，单击右上角的****保存配置****。 ### 启用网络钩子

接下来，您将在 Magento 2 帐户中启用 Klaviyo webhooks。请注意，需要在结帐时启用 Webhook 以获得同意才能正常运行。 1. 从管理仪表板，导航至****商店 > 配置****。 2. 单击****Klaviyo**** 并选择****Webhooks**** 选项卡。 3. 创建一个 Webhook Secret 并将其输入到相应的 ****Webhook Secret**** 字段中。 Webhook 密钥是 Klaviyo 将用于验证的密钥。此秘密可以是您选择的任何内容，但我们建议创建一个安全的字母和数字字符串。 出于安全目的，Magento 会用星号隐藏您的 webhook 秘密，因此请小心正确输入。如果您使用多商店集成，则应在默认配置中输入此字段中的 Webhook 密钥，并且相同的密钥将用作每个商店配置的验证。 Webhook 密钥只能添加到默认配置中，而不应该为每个商店添加。 ![m2webhooktab.png](https://klaviyo.zendesk.com/hc/article_attachments/28720770746779)
4. 在您要启用的 Webhooks 旁边，从下拉列表中选择****是****。要了解有关 Klaviyo 支持的 webhooks 的更多信息，请查看我们的 [Magento 2 webhooks 指南](https://help.klaviyo.com/hc/en-us/articles/360055336451)。 5. 单击****保存配置****。 ## 在 Klaviyo 中启用 Magento 2 集成

### 操作方法视频

![](https://fast.wistia.com/embed/medias/evlfi7fbya/swatch)

1. 打开 Klaviyo，然后从左侧导航栏中选择****集成****。在列表中找到 Magento 2 并选择它。 2. 在下一页上，您可以选择将新的 Magento 2 客户添加到 Klaviyo 列表中。单击复选框**将新的 Magento 2 客户添加到 Klaviyo 列表**，然后从下拉列表中选择一个列表。请注意，选中此设置只会将客户添加到所选列表，但不会为他们订阅营销消息。此设置只会同步新客户；现有客户需要[手动从您的 Magento 列表迁移到 Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005082407)。 ![](https://klaviyo.zendesk.com/hc/article_attachments/47104011603483)
3. 接下来，选择您想要将 Magento 2 中的哪些商店视图同步到 Klaviyo。默认情况下，所有商店视图都会同步到 Klaviyo。此设置允许您选择与哪些商店集成。如果您在 Magento 2 中使用多源库存 (MSI)，请检查 **特定 Magento 2 商店视图** 并选择您想要同步的商店，以便在 Klaviyo 中正确查看您的库存。 4. 在**高级**下，根据需要启用以下设置：

   - ****特价设置****
     此设置是指可以选择在特定日期范围内生效的商品的特价销售价格。如果您打算使用此功能，我们强烈建议您启用它，因为以后启用会更加困难。当您启用**适用时对产品价格使用特价**时，产品块将显示适用时的特价。使用动态产品 Feed 时，特价将在发送时填充。从目录中手动选择商品时，选择产品后就会显示特价。对于每个产品，有 4 个将同步的元数据字段：
     - ****价格****
       （必填，浮动）商品的标准价格。 - ****特价\_价格****
       （可选，浮动）这是该商品的特价。当此价格生效时，您将在价格删除线旁边看到此特殊价格。 - ****特别\_来自\_日期****
       （可选，日期）这指定特殊价格生效的开始日期。 - ****特别\_到\_日期****
       （可选，日期）这指定特殊价格生效的结束日期。 - ****自定义媒体根 URL****
     此设置允许您更改站点图像的默认路径。如果您将产品图片托管在与您的网站不同的 URL 上，请启用此设置。 5. 单击****保存****。您现在已成功启用 Magento 2 集成！您的数据将在几分钟内开始同步到 Klaviyo。初始历史数据同步完成后，Magento 2 集成每 30 分钟同步一次。 ## 与 Magento 2 集成同步的数据

Klaviyo 的 Magento 2 集成从您的 Magento 平台提取关键客户信息。以下是我们从 Magento 同步的一些数据：

- 客户信息，包括名字、姓氏和位置。 - 销售和订单数据，包括购买的商品、商品图像、商品类别以及应用的任何折扣。 - 履行、退款和取消订单数据。 - 人们何时访问您的网站以及他们查看了哪些项目；网络跟踪由扩展程序处理。要了解更多信息，请访问我们的 [Magento 2 数据参考](https://help.klaviyo.com/hc/en-us/articles/115003458852)。 ## 将 Magento 订单值转换为单一货币

Klaviyo 支持将 Magento 中的所有外币转换为 Klaviyo 中的一种主要货币。 请[联系支持人员](https://help.klaviyo.com/hc/en-us/articles/115001002272) 启用此功能。如果您有多家商店以不同货币进行交易，这尤其有用。 When this feature is enabled:

- 当 Magento 将订单数据同步到 Klaviyo 时，就会发生转换。 - Klaviyo 将检查 **order\_currency\_code** 是否与设置的 **global\_currency\_code** 相同。如果没有，Klaviyo 会将订单总额从订单货币转换为指定的全球货币，以确保您的财务分析准确。请注意，订单行项目将保留在订单货币代码中，不会进行转换。 ## Upgrade your extension

想要升级您的 Klaviyo Magento 2 扩展？请按照[**安装**](#h_01HGGJNFJT8CTEQ8PVGDVNB6GB) [a 部分](#h_01HGGJNFJT8CTEQ8PVGDVNB6GB)[上面](#h_01HGGJNFJT8CTEQ8PVGDVNB6GB) 中详细说明进行操作，并运行命令来安装最新版本。这将覆盖您当前的版本，并且您的更新将完成 - 无需重新配置扩展或重新启用 Klaviyo 中的集成。 ## 重新同步您的目录

您可以随时提示 Magento 2 目录的完整历史重新同步。重新同步您的目录可以帮助您利用 Klaviyo 对库存和变体相关功能的更新。要重新同步您的目录：

1. 在 Klaviyo 中，选择****集成****选项卡。 2. 从列表中选择您的 Magento 2 集成。 3. 单击****数据****选项卡。 4. 在**同步目录数据**下，单击****重新同步****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/38564204532379)