---
id: "6353315757211"
title: "Google Ads 入门"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/6353315757211-Getting-started-with-Google-Ads"
section: "Google Ads"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: "zh"
---
## 你将会学到

了解如何将 Google Ads 与 Klaviyo 集成。此集成允许您自动：

- 将 Klaviyo 列表或细分连接到 Google Audience。 - 将配置文件从 Klaviyo 同步到 Google。在 Klaviyo 的帮助下更轻松地制定您的 Google Ads 策略。集成后，您将能够重新定位现有客户、优化定位，并根据购买数据等标准从广告活动中排除个人资料。 ## 开始之前

在与 Google Ads 集成之前，请先设置您的 Klaviyo 帐户并与您的电子商务平台集成。请参阅我们的 [Klaviyo 入门] 指南(https://academy.klaviyo.com/getting-started-with-klaviyo/1405979)。请务必注意以下几点：

- 不支持通过经理和 MCC（我的客户中心）帐户进行访问，因此在集成之前，请确保您是要连接的 Google Ads 帐户的直接管理员。 - 仅当您的 Google Ads 帐户符合目标客户匹配条件时，Klaviyo 的 Google Ads 集成才能正常运行。要了解详情，请阅读 [Google 的目标客户匹配政策](https://support.google.com/adspolicy/answer/6299717)。 ## 如何与 Google Ads 集成

1. 如果您需要在 Klaviyo 中创建新列表，请导航至 ****Audience**** 下的 ****Lists & Segments**** 选项卡。 2. 单击****创建列表/段****。 3. 为列表命名并分配任何标签。 4. 单击****创建列表****。 1. 登录您的 Klaviyo 帐户。 2. 选择****集成****选项卡。 3. 单击****探索应用程序****。 4. 搜索 **Google Ads** 并点击该卡，然后点击****安装****。 5. 单击****连接到Google****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720659468443)
6. 登录您的 Google 帐户。请注意，您登录的 Google 帐户需要对您要连接的 Google Ads 帐户拥有直接管理员权限。不支持通过经理/MCC 帐户进行访问。 7. 同意权限并单击****允许****以带回Klaviyo。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720659471899)
8. 从下拉列表中选择您想要集成的 Google Ads 帐户。在下拉列表中没有看到合适的帐户？确认您拥有该帐户的管理员权限，然后重试。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720659473819)
9. 选择您是向欧洲经济区（或 EEA，目前包括欧盟国家以及冰岛、列支敦士登和挪威）还是英国 (UK) 的用户进行营销。 10. 如果您向欧洲经济区或英国的用户进行营销，根据《数字市场法》，您必须同意仅将已同意广告定位的受众群体发送至 Google。 11. 在**连接**下，选择 Klaviyo 列表或分段以与受众建立联系。 12. 选择要与您的列表或细分群体建立联系的 Google 受众群体。如果您需要创建新的 Google 受众群体，请在搜索框中输入新名称，然后单击****+ 创建受众群体：[受众群体名称]****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720659476123)
13. 如果要添加其他连接，请单击****添加连接****。请注意，您可以随时返回此设置页面以添加其他连接。另外，请注意这是 1:1 同步；您无法为多个 Klaviyo 列表或分段选择相同的 Google 受众群体，也无法将相同的 Klaviyo 列表或分段连接到多个 Google 受众群体。 14. 添加完连接后，单击****完成设置。****
15. 将出现一条成功消息，让您知道您的 Google Ads 帐户现已连接到 Klaviyo。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720671293467)
16. 集成后，您将在收件箱中看到来自 google.integrations@klaviyo.com 的 Google Ads 经理关联请求，您应该接受该请求。 ## 集成如何运作

将 Klaviyo 列表或细分连接到 Google Audiences 时，您可以：

- 在 Klaviyo 列表或分段与 Google Audience 之间创建 1:1 同步。请注意，您无法为多个 Klaviyo 列表或分段选择相同的 Google 受众群体，也无法将相同的 Klaviyo 列表或分段连接到多个 Google 受众群体。 - 从 Klaviyo 中创建新的 Google Audience 以连接新列表或细分。当您创建从 Klaviyo 到 Google Ads 的新连接时，Google Ads 中的自定义受众群体最多可能需要 48 小时才能填充。 尽管 Google Ads 可能需要长达 48 小时的时间来处理从 Klaviyo 收到的数据，但从 Klaviyo 到 Google Ads 的持续同步是实时更新个人资料列表/细分会员资格。这是由于 Google 延迟接受和处理来自 Klaviyo 的个人资料。只有与 Google 帐户关联的个人资料才会出现在 Google Audience 中。因此，您可能会发现您的 Google 受众群体规模小于 Klaviyo 中相应的列表或细分，这是可以预料的。此外，Google 会在 540 天后[删除这些受众群体的个人资料](https://ads-developers.googleblog.com/2025/02/update-to-customer-match-membership.html)。 ## 从“列表和细分”选项卡管理您的广告集成

您可以在 Klaviyo 的 **列表和细分** 选项卡中创建或更新 Google 受众同步（或任何其他广告平台的同步）。为此：

1. 在 Klaviyo 中，选择左侧导航栏中的****列表和分段****。 2. 您将在“集成”列中看到连接到广告集成受众的每个列表和细分的广告平台图标。 3. 要查看给定列表或段的更多详细信息，请单击三个点并选择****链接的集成****。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720671274139)
4. 您将进入列表或分段的 **设置** 选项卡中的 **集成** 选项卡。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720671279387)
5. 在这里，您将能够执行以下操作：

   - 连接新的广告集成。 - 激活或停用列表或分段的同步。 - 为列表或细分添加新的同步，然后选择相应的 Google 受众群体。 6. 进行任何更改后，单击****保存****。 ## 集成用例

您可以通过多种方式利用这种集成来推动 Google Ads 的营销策略。我们将这些用例分为 4 个主要类别：

1. 重新定位现有的配置文件。 2. 从未来的广告中排除某些片段。 3. 使用现有细分来优化定位。 4. 观察并监控特定受众的表现。下面，我们将讨论每个类别的用例，并提供有关实施的 Google 资源。 ### 重新定位现有配置文件

用于定向电子邮件和文本的相同分段也可用于定向广告。考虑以下部分：

1.****购物车放弃者****
   定位过去 7 天内开始结帐但过去 7 天内未下订单的客户，并投放与您在废弃购物车流程中提供的消息或折扣相呼应的广告。 2.****赢回****
   通过包含流行趋势商品的广告来定位一段时间没有购买商品的客户。 3.****重新参与****
   通过相关广告定位不活跃的订阅者，其中包含他们在您网站上浏览过的商品或限时优惠促销。 4.****交叉销售****
   目标客户已经购买了一种产品和另一种不同但互补的产品。 5.****新客户****
   定位那些访问过您的网站但从未购买过的用户，以鼓励首次转化。 6.****跨渠道****
   针对您已通过电子邮件联系的受众，投放相关广告来强化信息并具有类似的号召性用语。 7. ****潜在的品牌爱好者****
   这些客户最近购买过商品，但购买频率不高，且金额不高。通过推广畅销产品和流行或相关产品，重点提高他们的购买频率或平均订单价值。 8. ****未参与的 VIP****
   如果曾经在您的 VIP 名单上的客户最近没有与您的品牌互动，您可以在不同的平台上定位他们，以将他们带回您的品牌。 1. 导航至****受众****下的****列表和细分****选项卡。 2. 单击创建****列表/段****，然后选择****段****。 3. 设计您的细分以匹配您想要定位的群体。以下是如何通过将受众群体应用到 Google Ads 中的广告组或广告系列来定位这些细分受众群之一：
9. 在 Klaviyo 中创建您的分段。 10. 与 Google Ads 集成时，将您的细分连接到新的 Google 受众群体，如上面的“如何集成”部分所述。 11. 集成后，前往 Google Ads。在那里，使用定位设置来缩小广告组范围或将您的广告系列定位到从 Klaviyo 同步的受众群体。要详细了解定位，请查看 Google Ads [实施指南](https://support.google.com/google-ads/answer/7374253)。 ### 从未来的广告中排除现有的个人资料

如果您想要从未来的广告中排除某个列表或细分（例如，排除最近向您购买过产品且不太可能很快再次购买的客户），您可以在 Klaviyo 中创建该列表或细分，将其同步到 Google Ads 中的自定义受众群体，然后将其从广告组或广告系列中排除。这与针对细分受众群描述的过程类似，唯一的区别是在 Google Ads 中，您排除该细分受众群。要了解如何从 Google Ads 中的广告组或广告系列中排除特定受众群体名单，请参阅 [Google 的排除实施指南](https://support.google.com/google-ads/answer/2549058)。 ### 使用现有细分来优化定位

您可以在 Klaviyo 中获取 VIP 列表或细分，然后使用 Google 中的优化定位来吸引与您的最佳客户类似的新潜在客户。您需要在 Klaviyo 中创建细分，或使用现有的 VIP 细分，然后通过集成将其同步到 Google 受众群体。然后，在 Google Ads 中，您将使用优化定位并将细分添加为广告系列的定位信号。 - 了解 [Google Ads 中的优化定位](https://support.google.com/google-ads/answer/10537509?sjid=7203013319057182442-NA)，它可以帮助您吸引可能转化的新受众群体。 - 了解[如何使用优化定位](https://support.google.com/google-ads/answer/10538014?sjid=7203013319057182442-NA)。 ### 观察并监控特定受众的表现

您还可以决定仅在广告系列运行时监控广告针对选定受众群体的效果（报告），而不更改广告系列或广告组的覆盖面。根据对您的配置文件的报告/观察，您可以决定创建一个新的广告组或广告系列来定位这些配置文件或进行出价调整。 - 了解[如何在 Google Ads 中观察和监控受众群体的表现](https://support.google.com/google-ads/answer/7374253)。 ## EEA 同意要求

自 2024 年 3 月 6 日起，Google 将开始在欧洲经济区 (EEA) 和英国 (UK) 执行[数字营销法案](https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/europe-fit-digital-age/digital-markets-act-ensuring-fair-and-open-digital-markets_en) (DMA)。因此，他们正在更新其[欧盟用户同意政策](https://www.google.com/about/company/user-consent-policy/?sjid=15416941068016224808-NA)，要求与 Google Ads 集成的平台在将欧洲经济区或英国个人资料同步到 Google 时包含广告同意。 Klaviyo 的 Google Ads 集成包括将必要的同意标记同步到 Google 的选项，方法是在设置集成时选择“**我同意仅将已同意广告定位的受众发送到 Google**”。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28720671271707)

当您选择此选项时，Klaviyo 会自动为同步中包含的个人资料设置广告个性化和广告用户数据同意，以便您可以通过 Google Ads 向他们进行营销。这包括在 Google Ads 中自动设置同意状态。因此，如果您向欧洲经济区或英国个人资料投放广告，您的品牌必须实际收集此同意书以确保合规，这一点非常重要。提醒一下，广告同意书与用于发送通信的营销同意书是分开的，如果您计划将广告定位到欧洲经济区或英国个人资料，则必须在 Klaviyo 之外收集。通常，这是通过 [OneTrust](https://www.onetrust.com/) 等 [CMP](https://support.google.com/admanager/answer/13554116?hl=en#zippy=%2Cgoogle-certified-cmps)（同意管理平台）完成的，您的品牌应与您的 CMP 合作，以更深入地了解如何最好地管理您的广告同意数据以及将其导出到其他平台的选项。这项新要求将于 3 月 6 日起提前实施，之前通过集成同步的个人资料无需使用广告同意数据进行更新。 Klaviyo 建议与您的法律顾问合作，确认您的广告同意收集做法合规，并且您符合 Google 更新的欧盟用户同意政策。 ## 在 Klaviyo 中管理广告同意数据

虽然将广告同意数据从 CMP 同步到 Klaviyo 不需要将同意发送到 Google Ads，但建议这样做。 以下解决方案可以帮助 OneTrust 用户更轻松地管理他们在 Klaviyo 中的广告同意。 Klaviyo 建议与开发人员合作来实施此解决方案。广告同意数据不会从 CMP 本地同步到 Klaviyo，但您可以使用 Javascript 代码片段在 Klaviyo 中设置自定义配置文件属性，以表示来自 OneTrust 的广告同意。该脚本仅适用于 OneTrust/CookiePro，但可以修改为适用于您自己的 CMP。开始之前，请将 OneTrust 中的同意首选项映射到 Google 所需的同意字段（即 **ad\_user\_data** 和 **ad\_personalization**）。要实施此解决方案，请将以下脚本添加到您的站点（通常，将其添加到 <head> HTML 标记中）。确保 [Klaviyo 对象已加载](https://developers.klaviyo.com/en/docs/introduction_to_the_klaviyo_object#how-to-load-the-klaviyo-object)，以便成功记录更新，因为同意代码在页面加载时首先执行。 [“示例](https://www.napkin.io/api/embed/c1e26f659b834bd0)

在此脚本中，将 **///OneTrust\_CookiePro 脚本** 替换为 OneTrust/CookiePro 中的现有同意脚本。此外，将 **category\_ID** 替换为您自己的 [OneTrust 中的 cookie 分类](https://my.onetrust.com/articles/en_US/Knowledge/UUID-66bcaaf1-c7ca-5f32-6760-c75a1337c226)。添加到您的网站后，此脚本将自动在 Klaviyo 中设置 **ad\_user\_data** 和 **ad\_personalization** 配置文件属性，其值为 **denied**。 ![Klaviyo 中的个人资料中的 ad_personalization 和 ad_user_data 属性设置为拒绝](https://klaviyo.zendesk.com/hc/article_attachments/28720659447963)

当客户通过您网站上的 OneTrust cookie 横幅提供必要的同意时，脚本会将 Klaviyo 中的 **ad\_user\_data** 和 **ad\_personalization** 属性的值更新为 **granted**。此脚本只会更新 Klaviyo 已识别的配置文件的配置文件属性，并且您已加载 Klaviyo 跟踪脚本。在 Klaviyo 中设置 **ad\_user\_data** 和 **ad\_personalization** 属性后，请更新 Klaviyo 中正在同步到 Google Ads 的分段，以便它们仅包含已提供广告同意的个人资料。 ![将群组限制为基于 ad_personalization 和 ad_user_data 属性提供广告同意的配置文件的示例](https://klaviyo.zendesk.com/hc/article_attachments/28720671268763)

## 结果

您已完成 Google Ads 与 Klaviyo 的集成，现在可以开始使用 Klaviyo 来帮助推动您在 Google Ads 上的广告策略。谷歌广告资源：

克拉维约资源：