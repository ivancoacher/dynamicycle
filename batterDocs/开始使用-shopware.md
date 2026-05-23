<h1>开始使用 Shopware</h1>

<h2>你将会学到</h2>
<p>了解如何与 Shopware 6 集成，以便将站点活动、订单、目录和订户数据引入 Klaviyo。 ## 开始之前</p>
<p>请注意以下事项：</p>
<ul>
<li>集成之前，请确保您已登录到要集成的 Klaviyo 帐户。 - Shopware 6 集成由 Klaviyo 通过第三方提供支持。如果您需要联系支持人员，请参阅[下面有关如何联系的部分](#h_01HBC3PT82ESVQCM2KR7GGVC80)。 ## 将插件添加到您的 Shopware 帐户</li>
</ul>
<p>1. 前往 Shopware 商店中的 [Klaviyo 插件页面](https://store.shopware.com/en/klavi31418217175f/klaviyo.html)。 2. 出现提示时登录，然后选择<strong><em>*添加到购物车</strong><strong>。 3. 继续结帐并完成您的订单。 4. 订单确认后，单击选项转至您的</strong><strong>Shopware 帐户</strong><strong>。 5. 在您的 Shopware 帐户中，导航至</strong><strong>商家 > 商店</strong></em>*。 6. 选择您购买插件的商店。 7. 在许可证部分下，找到 Klaviyo 插件并打开插件详细信息页面。 ## 下载并安装扩展</p>
<p>您可以通过以下两种方法之一进行安装：通过 Composer 或下载我们的扩展。选择安装方法后，每次更新时都应使用相同的方法。 ### 通过 Composer 安装</p>
<p>通过 Composer 安装时，您需要指定 Klaviyo 扩展版本；并非所有扩展都适用于所有 Shopware 版本。您使用的 Shopware 版本是否介于 6.4.4.0 和 6.4.XX.XX 之间？使用以下扩展版本运行命令：</p>
<p>````</p>
<p>作曲家需要 klaviyo/shopware-klaviyo:1.22.0</p>
<p>````</p>
<p>您使用的 Shopware 版本是否介于 6.5.0.0 和 6.5.XX.XX 之间？使用以下扩展版本运行命令：</p>
<p>````</p>
<p>作曲家需要 klaviyo/shopware-klaviyo:2.22.0</p>
<p>````</p>
<p>您使用的 Shopware 版本是否介于 6.6.0.0 和 6.6.XX.XX 之间？使用以下扩展版本运行命令：</p>
<p>````</p>
<p>作曲家需要 klaviyo/shopware-klaviyo:3.6.0</p>
<p>````</p>
<p>您使用的是 Shopware 版本 6.7.0.0 或更高版本吗？使用以下扩展版本运行命令：</p>
<p>````</p>
<p>堆肥器需要 klaviyo/shopware-klaviyo:4.2.0</p>
<p>````</p>
<h3>通过上传安装</h3>
<p>1. 打开插件详细信息页面并下载最新可用版本（或任何所需版本）：</p>
<ul>
<li>使用 6.4.4.0 和 6.4.XX.XX 之间的 Shopware 版本？下载[Klaviyo扩展版本1.22.0](https://github.com/klaviyo/shopware-klaviyo/archive/refs/heads/master-1.x.x.zip)。 - 使用 6.5.0.0 和 6.5.XX.XX 之间的 Shopware 版本？下载[Klaviyo扩展版本2.22.0](https://github.com/klaviyo/shopware-klaviyo/archive/refs/heads/master-2.x.x.zip)。 - 使用 6.6.0.0 和 6.6.XX.XX 之间的 Shopware 版本？下载[Klaviyo扩展版本3.6.0](https://github.com/klaviyo/shopware-klaviyo/archive/refs/heads/master-3.x.x.zip)。 - 使用 Shopware 版本 6.7.0.0 或更高版本？下载[Klaviyo扩展版本4.2.0](https://github.com/klaviyo/shopware-klaviyo/tree/master-4.x.x)。 2. 登录您要集成的商店的 Shopware 管理员。 3. 单击****扩展 > 我的扩展****。 4. 单击****上传扩展****并选择您从 Shopware 帐户下载的 ZIP 文件。上传过程中您可能会看到一条警告消息。单击****确认****继续。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711680131995)</li>
</ul>
<p>5. 扩展程序出现在扩展程序列表中后，单击<strong><em>*安装</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711701445019)</p>
<p>6. 打开 Klaviyo 扩展。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711680138523)</p>
<h2>在 Shopware 中配置扩展</h2>
<p>1. 在您的 Shopware 商店管理中，导航至<strong><em>*设置</strong><strong>并单击</strong><strong>扩展</strong><strong>选项卡。 2. 选择</strong><strong>Klaviyo</strong><strong>。您将进入 Klaviyo 扩展设置页面。 3. 在 </strong>销售渠道<strong> 下，从下拉列表中选择您希望与 Klaviyo 集成的销售渠道。每个 Shopware 商店仅将一个销售渠道与 Klaviyo 集成。您还必须单独配置每个销售渠道的设置。 4. 在 </strong>交互设置</em>* 下，选择您想要用于此集成的 cookie 同意工具。请注意，不接受 Klaviyo cookie 的访客将不会被 Klaviyo 跟踪，也无法查看 Klaviyo 表格。 Cookie 同意工具选项有：</p>
<ul>
<li>****没什么****</li>
</ul>
<p>如果选择此选项，Klaviyo 可以自由访问存储 cookie。 - <strong><em>*商店软件默认</strong></em>*</p>
<p>如果选择此选项，则在打开的情况下，将通过 Shopware 的默认方法实施 cookie 管理。要打开它，请导航至<strong><em>*设置>商店>基本信息</strong><strong>，找到</strong>安全和隐私<strong>部分，然后打开</strong><strong>使用默认Cookie通知</strong><strong>。 - </strong><strong>CookieBot</strong></em>*</p>
<p>如果选择此选项，cookie 管理将由 CookieBot 实施。如果您希望选择 CookieBot，您必须已将其安装在您的 Shopware 商店中。 - <strong><em>*同意管理器</strong></em>*</p>
<ul>
<li>如果选择此选项，同意管理将通过同意管理器实施。如果您希望选择 Consent Manager，则必须已将其安装在 Shopware 商店中。 - ****以用户为中心的 CMP****</li>
</ul>
<p>如果选择此选项，同意管理将通过 Usercentrics CMP 实施。如果您希望选择 Usercentrics CMP，则必须已将其安装在 Shopware 商店中。 5. 如果您不使用 cookie 管理工具（该工具已阻止 Klaviyo 的脚本加载）并希望加快页面加载时间，请打开设置 <strong>首次与页面交互后初始化 Klaviyo</strong>。这将启用以下行为：</p>
<ul>
<li>客户端开始与页面交互后，Klaviyo 脚本将被初始化。 - 在后续页面转换时，脚本将立即初始化。 ![Cookie 同意设置为 Shopware 默认值，并在首次与页面交互后初始化 Klaviyo 切换](https://klaviyo.zendesk.com/hc/article_attachments/28711701425051)</li>
</ul>
<p>6. 要继续，请从 Klaviyo 获取您的公共和私有 API 密钥。为此，请打开一个新选项卡并登录到要与 Shopware 集成的 Klaviyo 帐户。 1. 单击左下角您的帐户名，然后选择<strong><em>*设置</strong><strong>。 2. 选择</strong><strong>API 密钥</strong><strong>。 3. 单击</strong><strong>创建私有 API 密钥</strong><strong>。将密钥命名为“Shopware Integration”，然后选择</strong><strong>完全访问密钥</strong><strong>并单击</strong><strong>创建</strong><strong>。在下一页上，单击</strong><strong>复制密钥</strong><strong>。 4. 将私有 API 密钥粘贴到 Shopware 中的相应设置中。 5. 返回 Klaviyo，单击</strong><strong>完成</strong></em>*。然后，从页面复制您的公共 API 密钥。 6. 将 Shopware 中的公共 API 密钥粘贴到相应的框中。 7. 接下来，从下拉列表中选择一个 Klaviyo 列表，将通过 Shopware 表单订阅的配置文件添加到其中。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711680128027)</p>
<p>8. 选择用于返回库存变体字段映射的标识符。您应该使用与您在目录中使用的标识符相匹配的标识符。 9. 打开您想要从 Shopware 同步到 Klaviyo 的所有指标。 ![所有指标列表切换为蓝色](https://klaviyo.zendesk.com/hc/article_attachments/28711680104731)</p>
<p>10.如果您选择追踪“返货”，您可以自定义“返货”弹窗开启按钮、弹窗关闭按钮、订阅按钮的文字颜色和背景。单击正方形，然后使用选择器选择颜色，或者，如果您有品牌颜色的十六进制颜色代码，请将其粘贴到相应的框中。 ![弹出打开按钮设置，颜色设置为白色，背景设置为深蓝色](https://klaviyo.zendesk.com/hc/article_attachments/28711680111515)</p>
<p>11. 在 <strong>代码段名称</strong> 下，您将找到有关如何在 HTML 中引用不同的 Back in Stock 组件的参考。您可以选择在站点代码中自定义它们。 ![打开按钮、关闭按钮和电子邮件字段标签的片段名称](https://klaviyo.zendesk.com/hc/article_attachments/28711680120347)</p>
<p>12. 自定义字段映射：在这里，您将看到在 Shopware 中设置的自定义字段（技术名称为灰色）。分配给客户对象的任何字段都可以同步到 Klaviyo。要将这些自定义字段同步到 Klaviyo 配置文件，请将各个字段切换为<strong>活动</strong>。然后，在 <strong>字段名称</strong> 下，输入您希望字段在 Klaviyo 中具有的相应名称。 ![字段名称“Favorite Color”映射到favorite_color，字段切换为活动状态](https://klaviyo.zendesk.com/hc/article_attachments/28711680122651)</p>
<p>13. 完成后，单击<strong><em>*保存</strong><strong>。 14. 要运行历史事件同步，请单击页面顶部的</strong><strong>同步历史事件</strong><strong>。 15. 要运行现有订阅者的同步，请单击页面顶部的</strong><strong>同步订阅者</strong><strong>。在您最初手动运行这些同步后，它们将自动运行。 订阅者和事务事件同步每 5 分钟运行一次。现场事件（</strong>现场活动<strong>、</strong>查看产品<strong>和</strong>开始结账</em>*）实时同步。 ## 同步您的目录提要</p>
<p>要完成与 Klaviyo 的集成，您必须生成产品目录的源，然后将其同步到 Klaviyo。要生成提要：</p>
<p>1. 登录您的 Shopware 商店管理员。 2. 单击 <strong>销售渠道</strong> 旁边的 <strong>+</strong><strong> 添加新渠道。 3. 在</strong>产品<strong> </strong>比较<strong>旁边，单击</strong><strong>添加销售渠道</strong><strong>。 4. 在</strong>模板<strong>下，选择</strong><strong>Klaviyo XML</strong><strong>。 5. 为通道命名，例如 </strong>Klaviyo Export<strong>。 6. 在</strong>税收征收<strong>下，选择</strong><strong>逐行（水平）计算</strong><strong>。 7. 在</strong>店面销售渠道**下：</p>
<ul>
<li>选择该目录所属的店面销售渠道。 - 选择店面域。 - 选择货币。 - 选择语言。 - 选择客户组。 8. 在**产品出口**下：</li>
<li>命名文件（例如 **klaviyo.xml**）。 - 选择编码****UTF-8****。 - 选择文件格式****XML****。 9. 将**将变量导出为离散产品**保持关闭状态。 10. 选择间隔：****1 天****。 11. 将**通过调度程序生成**保持关闭状态。 12. 选择您的动态产品组。 13. 在 **状态** 下，打开 ****活动****。 14. 单击右上角的****保存****。 15. 向下滚动并复制 **导出 URL**，您将用于 Klaviyo 同步。 16. 现在 feed 已生成，您必须将其同步到 Klaviyo。按照说明[将自定义目录源同步到 Klaviyo](https://developers.klaviyo.com/en/docs/guide_to_syncing_a_custom_catalog_feed_to_klaviyo)。 ## 从 Shopware 同步的数据</li>
</ul>
<p>要了解有关从 Shopware 同步的数据以及如何在 Klaviyo 中访问这些数据的所有信息，请阅读我们的[Shopware 数据参考](https://help.klaviyo.com/hc/en-us/articles/13006716790299)。 ## Klaviyo 注册表单</p>
<p>您可以将 [Klaviyo 注册表单](https://help.klaviyo.com/hc/en-us/articles/360026474752-Getting-started-with-sign-up-forms) 添加到您的 Shopware 商店以收集订阅者。请注意，只有接受 Klaviyo cookie 的网站访问者才能看到 Klaviyo 注册表单。 ## 如何联系支持人员</p>
<p>Klaviyo Shopware 6 集成由 Klaviyo 通过第三方提供支持。如果您对集成有疑问并需要支持，可以通过[填写我们的表单](https://docs.google.com/forms/d/e/1FAIpQLSewwJzxlnFtsbn18ZVubgIORubQWpAKBuYQv6WKxy8xSxVZog/viewform)联系特定于集成的支持人员。如果您需要 Klaviyo 相关问题的一般支持，请[联系 Klaviyo 支持](https://help.klaviyo.com/hc/en-us/articles/115001002272-How-to-contact-support)。 ## 结果</p>
<p>您已将 Shopware 6 与 Klaviyo 集成，将站点活动、订单、目录和订户数据引入 Klaviyo。您现在可以开始使用 Klaviyo 来满足您自己的营销需求。 ## 其他资源</p>
<ul>
<li>[如何将自定义目录源同步到 Klaviyo](https://developers.klaviyo.com/en/docs/guide_to_syncing_a_custom_catalog_feed_to_klaviyo)</li>
<li>[Shopware 6 数据参考](https://help.klaviyo.com/hc/en-us/articles/13006716790299)</li>
</ul>
