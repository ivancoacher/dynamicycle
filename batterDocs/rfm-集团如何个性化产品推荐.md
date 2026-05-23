<h1>RFM 集团如何个性化产品推荐</h1>

<h2>你将会学到</h2>
<p>了解如何使用 RFM（新近度、频率和货币）属性通过产品推荐来定位客户。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 和 [营销分析](https://help.klaviyo.com/hc/en-us/articles/33789259613595) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。前往我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672) 了解如何购买这些计划。 ## 创建 RFM 段</p>
<p>如果您已创建要在 RFM 报告中使用的[新自定义指标](https://help.klaviyo.com/hc/en-us/articles/22311085738395/)，则此更改最多可能需要 48 小时才会反映在您的数据中。根据 RFM 组创建客户细分，您可以轻松地定位具有与其购物模式最相关的不同产品组的目标群体。创建后，这些细分可用于向不同组发送个性化营销活动，并在客户进入特定 RFM 组时触发流程。例如，您可能希望在发送给当前<strong>有风险</strong>或<strong>不活跃客户</strong>的电子邮件中包含折扣产品，或者与<strong>最近</strong>组中的客户使用交叉销售内容。要基于 RFM 组创建分段，请使用以下条件，并将所需组设置为值（即下例中的 <strong>Champions</strong>）。 - 关于某人的属性 > 当前 RFM 组 > 等于 > RFM 组名称</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28717418753947" alt="使用当前 RFM 组属性的段" />
<p>详细了解[基于 RFM 组构建细分](https://help.klaviyo.com/hc/en-us/articles/18193920339483)。基于 RFM 组的分段的一些其他用例包括：</p>
<ul>
<li>针对**忠诚**和**冠军**客户提供对商品的评论。 - 针对**忠诚**或**最近**客户提供新产品或产品优惠，进行交叉销售和追加销售。 - 针对**最近**的订阅客户，使他们成为**冠军**或**忠诚**。 - 通过赢回活动针对**不活跃**或**面临风险**的客户。 - 以较低成本的商品瞄准**不活跃**或**有风险**的客户。 - 向**不活跃**或**有风险**客户提供独家或限时折扣。 ## 使用基于 RFM 组的显示/隐藏逻辑</li>
</ul>
<p>您可以使用 Klaviyo 的[模板中的显示/隐藏逻辑](https://help.klaviyo.com/hc/en-us/articles/7655965301531) 根据个人资料的 RFM 组动态显示电子邮件中的不同内容。此功能允许您根据收集的订阅者信息个性化您的电子邮件内容，以便每个收件人都拥有高度相关的营销体验。基于配置文件数据（即配置文件或自定义属性）的显示/隐藏条件可以在任何 Klaviyo 电子邮件中使用。在这种情况下，您可以使用 <strong>当前 RFM 组</strong> 或 <strong>上一个 RFM 组</strong> 属性来显示基于收件人 RFM 组的产品推荐。例如，对于 <strong>冠军</strong> 或 <strong>忠诚客户</strong> 群体，请考虑发送更高价值的物品。同时，对于<strong>不活跃</strong>或<strong>有风险</strong>组的客户，发送成本较低的产品或畅销产品。或者，您可以发送 <strong>Loyal</strong> 或 <strong>Champions</strong> 组的早期访问或新产品中的个人资料，以查看它们是否表现得更好。了解[如何根据动态变量显示或隐藏模板块和部分](https://help.klaviyo.com/hc/en-us/articles/7655965301531)。您需要向特定 RFM 群组显示一段内容的条件是<strong>当前 RFM 群组 > 等于 > 冠军</strong>。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30443751496475)</p>
<p>在此示例中，<strong>当前 RFM 组</strong>是条件中引用的属性，属性值为 <strong>Champions</strong>。您可以将 <strong>Champions</strong> 替换为您要定位的 RFM 组。同样，要隐藏特定 RFM 组的一段内容，请使用条件 <strong>当前 RFM 组 > 不等于 > Champions</strong>。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30443751503515)</p>
<p>此条件仅向不属于 <strong>Champions</strong> RFM 组的收件人显示内容。 ### 发送具有显示/隐藏逻辑的个性化营销活动</p>
<p>在 Klaviyo 中发送营销活动时，您可以使用 Klaviyo 中的显示/隐藏逻辑来包含基于配置文件的 RFM 组（即 <strong>当前 RFM 组</strong> 或 <strong>以前 RFM 组</strong>）的个性化产品推荐。您可以在电子邮件中包含多个产品，并创建显示/隐藏规则，以便不同组中的个人资料在其电子邮件中看到适当的产品。一些例子包括：</p>
<ul>
<li>针对**忠诚**或**最近**客户提供新产品或产品优惠，进行交叉销售和追加销售。 - 针对**最近**的订阅客户，使他们成为**冠军**或**忠诚**。 - 针对**需要注意**或**有风险**群体的客户，他们更有可能购买成本较低的商品。 - 针对**冠军**或**忠诚**客户群体提供更高价值的物品。了解[如何将产品块添加到电子邮件](https://help.klaviyo.com/hc/en-us/articles/115000219092)。 ## 发送个性化流</li>
</ul>
<p>您还可以使用 RFM 属性来发送与您的流更相关的内容。除了使用显示/隐藏逻辑动态显示内容之外，您还可以根据配置文件的 RFM 组[创建条件拆分](https://help.klaviyo.com/hc/en-us/articles/115003872171)，以将不同的组成员发送到不同的流路径。您可以在每个路径的流电子邮件中包含不同的产品推荐或其他内容。当配置文件通过流程时，他们将根据其 RFM 组沿着相关路径走下去。了解[如何在流中创建条件分割](https://help.klaviyo.com/hc/en-us/articles/115003872171)。 ![按 RFM 组划分的分支流程](https://klaviyo.zendesk.com/hc/article_attachments/28717391505051)</p>
<p>在流程中，您可以尝试根据特定产品进入流程及其 RFM 组所采取的操作的详细信息来交叉销售或追加销售特定产品。例如，如果您的购买后流程具有基于 RFM 组的有条件拆分，则您可以通过产品审核请求定位 <strong>Loyal</strong> 或 <strong>Champions</strong>。同时，对于“最近”组中的客户，您可以针对他们提供与其购买相补充的新产品。了解[如何创建由 RFM 组和客户行为变化触发的保留流程](https://help.klaviyo.com/hc/en-us/articles/25408596027547)。在流中使用 RFM 组的其他示例包括：</p>
<ul>
<li>根据一个人是否满足以下条件创建条件分割：</li>
</ul>
<ul>
<li>经常购买者（**冠军**或**忠诚**）</li>
<li>或者他们有时或从不购买（**最近**、**需要注意**、**不活跃**或**有风险**）。 - 根据客户组最近的浏览行为创建有条件的拆分。 - 例如，**冠军**、**忠诚**或**最近**的用户可能会收到常规浏览放弃消息，而**需要注意**、**不活跃**或**有风险**的用户会收到带有额外折扣的浏览放弃消息。 - 为**冠军**、**忠诚**或**最近组**中的人员创建一个流程，突出显示新产品或发布。 - 鼓励**冠军**、**忠诚**或**最近**组中的人留下对其产品的评论。 ## 其他资源</li>
</ul>
<p><a href="https://help.klaviyo.com/hc/en-us/articles/17797937793179">了解新近度、频率和货币分析 (RFM) 报告中的评分和客户群体</a></p>
<p><a href="https://help.klaviyo.com/hc/en-us/articles/25408596027547">如何创建由 RFM 组和客户行为变化触发的保留流</a></p>
<p><a href="https://help.klaviyo.com/hc/en-us/articles/18194102384539">如何在营销活动和流程中战略性地使用 RFM 属性</a></p>
