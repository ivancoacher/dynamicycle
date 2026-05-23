<h1>了解 Klaviyo 中的身份解析转换</h1>

<h2>你将会学到</h2>
<p>了解作为高级 KDP 一部分的 Klaviyo 身份解析功能。这建立在 Klaviyo 的标准[身份解析](https://help.klaviyo.com/hc/en-us/articles/12902308138011) 功能的基础上，可以更可靠地处理基于重叠标识符识别的重复配置文件。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。 ## 身份解析转换与身份解析</p>
<p>Klaviyo 本身提供[身份解析](https://help.klaviyo.com/hc/en-us/articles/12902308138011)，将客户跨多个渠道的交互整合到单个记录下。 Klaviyo 中的这种标准身份解析使用确定性配置文件合并，根据您帐户中的现有数据解析共享公共标识符（最常见的是唯一的电子邮件地址）的不同配置文件的身份。同时，高级 KDP 中的身份解析转换基于这种确定性合并功能，通过探索具有不同电子邮件地址但其他重叠标识符（例如相同电话号码）的配置文件。 ## 身份解析转换</p>
<p>作为 AKDP 的一部分提供的第一个可用身份解析转换旨在减少由于电子邮件地址中的拼写错误或拼写错误而导致的联系人重复配置文件的数量。将来，Klaviyo 将提供额外的合并逻辑，例如由于使用电子邮件别名而存在的重复数据删除配置文件，以及基于共享名字、姓氏、地址等的概率合并。这些转换可以打开和关闭，但不需要进一步配置。 ### 管理身份解析转换</p>
<p><strong><em>*配置文件合并是一项永久性操作。</strong></em>* 从身份解析转换合并的任何配置文件都无法取消合并。要激活身份解析转换：</p>
<p>1. 导航到<strong><em>*高级 KDP</strong><strong></em></strong><em>><strong></em></strong><strong><em>数据管理 > 转换</strong><strong>下的 </strong>转换<strong> 选项卡。 2. 选择</strong><strong>身份解析</strong><strong>选项卡。 3. 在您想要启用的身份解析转换上选择</strong><strong>激活</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/40442765151515)</p>
<p>4. 我们强烈建议您在激活任何合并规则之前<strong><em>*下载预览版</strong></em>*，以确保您了解激活后配置文件将如何集群和合并</p>
<p>5. 完成确认提示并选择<strong><em>*激活</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/40442765166619)</p>
<p>激活后，您将在 <strong>身份解析</strong> 选项卡上看到转换的 <strong>活动</strong> 状态。通过单击活动转换，您可以使用<strong><em>*下载合并日志</strong><strong>按钮下载过去 30 天内的合并日志，或通过选择</strong><strong>停用</strong></em>*按钮禁用转换。 ![](https://klaviyo.zendesk.com/hc/article_attachments/40442773443995)</p>
<h3>合并日志</h3>
<p>要查看转换执行的配置文件合并的记录，请选择转换并单击<strong><em>*下载合并日志</strong></em>*按钮。这将导出过去 30 天内合并的 CSV，其中包含以下信息：</p>
<ul>
<li>****源配置文件 ID****</li>
</ul>
<p>源配置文件的 [Klaviyo ID](https://help.klaviyo.com/hc/en-us/articles/115005247088#h_01H93XCYWWRTEWCFEMEADSYC0Q)。 - <strong><em>*源电子邮件</strong></em>*</p>
<p>源配置文件的电子邮件地址。 - <strong><em>*来源外部ID</strong></em>*</p>
<p>源配置文件的外部 ID。 - <strong><em>*来源电话号码</strong></em>*</p>
<p>源配置文件的电话号码。 - <strong><em>*目的地配置文件 ID</strong></em>*</p>
<p>目标配置文件的 [Klaviyo ID](https://help.klaviyo.com/hc/en-us/articles/115005247088#h_01H93XCYWWRTEWCFEMEADSYC0Q)。 - <strong><em>*目标电子邮件</strong></em>*</p>
<p>目标配置文件的电子邮件地址。 - <strong><em>*目的地外部ID</strong></em>*</p>
<p>目标配置文件的外部 ID。 - <strong><em>*目的地电话号码</strong></em>*</p>
<p>目标配置文件的电话号码。 - <strong><em>*合并于</strong></em>*</p>
<p>配置文件合并的时间戳。 ## 身份解析转换方法</p>
<p>Klaviyo 支持以下身份解析转换方法。 ### <strong><em>*电子邮件拼写错误合并</strong></em>*</p>
<p>电子邮件拼写错误合并可识别共享相同电话号码且由于电子邮件地址拼写错误而看起来重复的配置文件。例如，假设 2 个个人资料具有相同的电话号码，但电子邮件地址为 example@klaviyo.com 和 excampke@klaviyo.com。这些个人资料很可能属于同一客户，但他们在特定环境下（例如注册营销列表）与您的品牌互动时犯了拼写错误。电子邮件拼写错误合并转换在激活时将自动合并这些配置文件。 <strong><em>*合并逻辑</strong></em>*</p>
<p>对于要通过电子邮件拼写错误重复数据删除转换合并的 2 个配置文件，它们必须满足以下条件：</p>
<ul>
<li>个人资料必须共享相同的电话号码。 - 个人资料的电子邮件地址仅相差 1 个字符。 - 电子邮件地址之间的差异要么是由于域名中的拼写错误，要么是由于无效或退回的电子邮件（即无法访问）而抑制了一个配置文件。如果这些条件全部满足，则合并将按以下方式进行：</li>
<li>如果个人资料的电子邮件地址无效，则保留具有有效电子邮件地址的个人资料（即可访问且域名中没有拼写错误）。请注意，没有任何其他问题的手动抑制的配置文件被认为是可以访问的。 - 如果配置文件 A 和配置文件 B 均不可达，则不合并。 - 如果两个配置文件均可访问</li>
<li>如果电子邮件 A 具有更标准的域（例如，gmail 与 gnail），则保留电子邮件 A。 - 如果无法确定哪封电子邮件更标准，请勿合并。与无效电子邮件地址关联的任何电子邮件事件（例如，**收到的电子邮件**）将不会合并到目标配置文件中。但是，其他事件（例如，**查看的产品**等现场事件）将合并到目标配置文件中。 ### ****电子邮件别名合并****</li>
</ul>
<p>该功能尚未发布，但即将推出。电子邮件别名合并可识别共享相同电话号码的配置文件，并且由于用于创建电子邮件别名的“+”而显得重复。电子邮件别名是将电子邮件转发到主电子邮件帐户收件箱的备用电子邮件地址。例如，假设 2 个个人资料具有相同的电话号码，但电子邮件地址为 example@klaviyo.com 和 example+marketing@klaviyo.com。发送到 [example+marketing@klaviyo.com](mailto:example+@klaviyo.com) 的电子邮件将被转发到 [example@klaviyo.com](mailto:example@klaviyo.com) 或进入同一收件箱，因此将始终属于同一客户。通过此转换，具有别名电子邮件地址（即末尾带有“+”的相同电子邮件地址）的配置文件将合并到相应的主要配置文件中。</p>
