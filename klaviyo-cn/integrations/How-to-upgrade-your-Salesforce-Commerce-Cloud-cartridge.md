---
id: "16708128591259"
title: "如何升级您的 Salesforce Commerce Cloud 墨盒"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/16708128591259-How-to-upgrade-your-Salesforce-Commerce-Cloud-cartridge"
section: "Salesforce Commerce Cloud"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: "zh"
---
## 你将会学到

了解如何升级您的 Klaviyo Salesforce Commerce Cloud 盒。您使用的墨盒版本是否早于 23.7.0？我们建议立即升级到版本 23.7.0 或更高版本。旧版本的卡带使用 Klaviyo 的 v1 和 v2 API，这些 API 已停用并且不再按预期运行。我们始终建议升级到最新版本（当前为 25.7.0）。 ## 开始之前

版本 23.7.0 包括许多有意义的改进，其中一些是围绕事件触发方式的架构更改。下面详细介绍了从低于 23.70 的任何版本升级到高于 23.70 的任何版本的特殊注意事项。 ## 了解您当前的集成

熟悉您当前的 SFCC 集成以及可能专门针对您的网站进行的更改或自定义非常重要。最重要的是，您应该考虑发送到 Klaviyo 的特定事件数据是否已被更改或增强，以及是否添加了任何自定义事件。我们建议将收集事件数据的代码与之前版本的 Klaviyo 盒进行比较，[可在 Klaviyo 的 Github 上找到](https://github.com/klaviyo/SFCC_Klaviyo/releases)。假设您的集成没有经过大量定制，您将在`int_klaviyo_core/cartridge/scripts/utils/klaviyo/klaviyoUtils.js`中找到当前的数据组装函数，并在`int_klaviyo_core/cartridge/scripts/utils/klaviyo/emailUtils.js`中找到**订单确认**。记下所有自定义设置，以便在安装新墨盒后可以重新应用它们。 ## 将 SFCC 沙箱连接到 Klaviyo 测试帐户

如果您尚未创建用于测试的辅助 Klaviyo 帐户（与与 SFCC 生产环境绑定的帐户分开），则应该这样做。然后，将您的 SFCC 沙箱环境连接到新帐户。我们建议使用您之前的 Klaviyo 卡带版本完成此步骤，以便您可以验证事件是否已成功发送到您的辅助 Klaviyo 帐户并由您的辅助 Klaviyo 帐户接收，然后再继续使用新的 Klaviyo 卡带升级您的代码库。 ## 删除之前的 Klaviyo 墨盒代码

如果您的集成没有经过深度定制，您只需从代码库中删除两个 Klaviyo 盒式文件夹：int\_klaviyo\_core 和 int\_klaviyo（用于 Site Genesis）或 int\_klaviyo\_sfra（用于 SFRA），即可删除以前的 Klaviyo 集成的大部分内容。但是，您还必须删除可能已添加到模板文件（可能还有 JavaScript 文件）中的任何 Klaviyo 特定代码。 ### 对于网站创世

Site Genesis 的标准集成将在 footer\_UI.isml 中添加以下代码：

````
<isinclude template="components/footer/klaviyoFooter"/>
````

他们还将以下块添加到 minicart.isml、cart.isml 和任何其他“购物车”isml 文件中：

````
<isif condition="${pdict.CurrentHttpParameterMap.cartAction == '添加' || pdict.CurrentHttpParameterMap.cartAction
  =='更新'}">
   <isinclude url="${URLUtils.url('Klaviyo-RenderKlaviyoAddToCart')}"/>
</isif>
````

### 对于 SFRA

SFCC 的标准集成将在 pageFooter.isml 中添加以下代码：

````
<isinclude template="klaviyo/klaviyoFooter"/>
````

他们还将以下代码添加到 Cart.js 控制器中的 AddProduct 路由中：

````
 if(dw.system.Site.getCurrent().getCustomPreferenceValue('klaviyo_enabled')){
   var KlaviyoUtils = require('*/cartridge/scripts/utils/klaviyo/klaviyoUtils');
 KlaviyoUtils.trackAddToCart();
}
````

对于 Site Genesis 和 SFRA，删除卡带文件夹和上述代码片段后，建议在代码库中搜索“Klaviyo”一词。在删除之前，请确保您熟悉代码库中保留的任何与 Klaviyo 相关的代码正在执行的操作，因为这些块可能代表您在安装新墨盒后需要放回原位的自定义设置。 ## 删除服务

之前的集成将在****管理 > 操作 > 服务**** 处创建 KlaviyoTrackService、KlaviyoTrackProfile 和 KlaviyoTrackCredentials。所有这三个都可以安全地删除，因为集成新 Klaviyo 墨盒的过程将创建具有不同名称的新服务。删除旧服务并不重要，但建议您清理它们以避免将来出现混乱。 ## 查看站点首选项

集成新的 Klaviyo 墨盒的过程将保留一些以前的 Klaviyo 站点首选项，并且还将添加一些新的首选项。在 **Klaviyo** 偏好设置组中查看您的网站偏好设置（**** 商家工具 > 网站偏好设置 > 自定义偏好设置 > klaviyo****），并检查是否专门为您的网站添加了任何自定义偏好设置。如果您自定义了墨盒以添加您自己的设置，您将需要保留它们。作为参考，以下是先前 Klaviyo 集成中内置的四个站点首选项：

- ****Klaviyo 已启用（ID：klaviyo\_enabled）**** 标记 Klaviyo 是否打开或关闭。 - ****Klaviyo 帐户（ID：klaviyo\_account）****您的 Klaviyo 公共 API 密钥或站点 ID。 - ****Klaviyo 私人 API 密钥（ID：klaviyo\_api\_key）****
  Klaviyo 私人 api 密钥。 - ****Klaviyo 的图像类型（ID：klaviyo\_image\_size）****
  大、小、缩略图等。在设置新的盒式磁带之前，我们建议通过在****管理 > 站点开发 > 站点导入和导出**** 中导出它们来备份您当前的站点首选项。展开****站点****，然后展开****站点名称****，并选中“站点首选项”框，然后输入要将其导出到的文件名。当您稍后安装新的墨盒时，您当前的 Klaviyo 首选项不应受到不利影响，但最好对其进行备份以供将来参考。 ## 从墨盒路径中取出 Klaviyo 墨盒

从****管理 > 站点 > 管理站点 > [站点名称] > 设置**** 的盒式磁带路径中删除 int\_klaviyo\_core 和 int\_klaviyo (Site Genesis) 或 int\_klaviyo\_sfra (SFRA)。如果不执行此步骤，您将收到因 SFCC 寻找要加载的不再存在的磁带而导致的错误。 ## 检查开发者控制台和服务器端日志是否有错误

此时，您的代码库中不应再有任何 Klaviyo 代码。我们建议检查您的前端，访问搜索结果、PLP 和 PDP 等页面，并执行将产品添加到购物车、输入和完成结账等操作。执行此操作时，请密切关注开发人员控制台以查看是否生成任何新错误。对请求日志执行相同的操作。如果您看到与 Klaviyo 相关的新错误，则很可能您尚未完全删除所有以前的 Klaviyo 代码。重要的是要追踪任何新错误的来源并在删除它们之前记下它们。 ## 安装新的 Klaviyo 墨盒

按照 [Salesforce Commerce Cloud 入门](https://help.klaviyo.com/hc/en-us/articles/360033744951) 中列出的步骤将新盒集成到您的代码库中。您可能不需要完成某些步骤 - 例如，您的 SFCC 实例可能已建立或尚未为 OCAPI 部分建立连接 - 但一般来说，您应该遵循每个集成步骤。您肯定需要更换两个 Klaviyo 墨盒并添加回代码片段。不要简单地将新的墨盒文件夹复制/粘贴到旧的墨盒文件夹上。根据上述说明，在添加新文件夹之前完全删除旧文件夹。请注意，导入metadata.zip 后，除了先前版本的盒式磁带创建的四个站点首选项之外，您还将获得四个新的站点首选项。您以前的首选项不应因导入新首选项而受到影响，但建议您在继续之前仔细检查所有 Klaviyo 站点首选项是否正确。由于您是从版本 23.7.0 之前的盒式磁带升级，因此新站点首选项 **将事件标记为 SFCC** 和 **将添加到购物车事件发送为“添加到购物车”** 应分别设置为 **否** 和 **是**。这将继续发送没有 **Salesforce Commerce Cloud** 指标标签的事件，并使用 **添加到购物车** 事件类型（而不是新的 **添加到购物车**）。这两个站点首选项设置不正确将导致报告中断，并可能导致 Klaviyo 中现有流程的中断。 ## 验证所有开箱即用的事件是否正常工作

在尝试添加回之前集成的任何自定义设置之前，请务必验证新安装的 Klaviyo 盒是否正常工作。 使用前端生成 **搜索站点**、**查看类别**、**查看产品、** **添加到购物车**、**开始结帐** 和 **订单确认** 的事件，然后检查您的 Klaviyo 帐户以确保正确跟踪这些事件。检查开发人员控制台是否有可能与生成 Klaviyo 事件的所有页面上的集成相关的任何新错误。通过在****管理 > 操作 > 服务 > KlaviyoEventService - 详细信息**** 处选中 **通信日志已启用** 复选框来启用详细服务日志记录，然后查看服务器端日志文件以验证是否没有错误，以及是否为每种事件类型正确生成了事件数据。 ## 将事件数据与生产数据进行比较

您现在应该比较测试和生产 Klaviyo 帐户中的事件数据，以确保没有丢失任何内容，并且当前值与预期类型匹配。确定新集成是否会影响任何报告或流量非常重要。您会发现与之前的墨盒版本相比，现在正在设置附加属性并将其发送到 Klaviyo。 ## 添加回特定于站点的自定义设置

您现在可以开始将自定义添加回您的 Klaviyo 代码中。由于最新的 Klaviyo 墨盒在结构和架构上发生了重大变化，因此您不可能简单地将自定义代码直接复制并粘贴到 Klaviyo 墨盒中。 Klaviyo 盒中的每个事件类型都有一个 getData 函数，该函数位于为每个事件类型命名的单独脚本文件中。这些文件可以在“int_klaviyo_core/cartridge/scripts/klaviyo/eventData”文件夹中找到，并且是您最有可能更改的位置，以便添加或更新为每个事件传递的数据对象。如果您要创建新的自定义事件，我们建议遵循向服务器端控制器添加代码的既定模式（**即直接在 SiteGen 中或通过 SFRA 中的 server.append），从专用于新事件的脚本文件调用 getData 函数，然后使用 trackEvent 函数通过 KlaviyoEventService 将该数据发送到 Klaviyo。 ## 结果

您现在已经升级了适用于 Salesforce Commerce Cloud 的 Klaviyo 墨盒。 ## 其他资源

- [Salesforce Commerce Cloud 入门](https://help.klaviyo.com/hc/en-us/articles/360033744951)
- [Salesforce Commerce Cloud 数据参考](https://help.klaviyo.com/hc/en-us/articles/360058323811)
- [集成同步参考频率](https://help.klaviyo.com/hc/en-us/articles/115005253208)
- [如何联系支持人员](https://help.klaviyo.com/hc/en-us/articles/115001002272)