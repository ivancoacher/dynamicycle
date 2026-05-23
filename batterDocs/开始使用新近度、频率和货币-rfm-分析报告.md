<h1>开始使用新近度、频率和货币 (RFM) 分析报告</h1>

<h2>你将会学到</h2>
<p>了解如何使用新近度、频率和货币价值 (RFM) 报告来更深入地了解客户的购买行为。 RFM 报告提供有关客户最近进行购买的数据、他们整体购买的频率以及他们通常在单笔交易上花费的金额。然后，Klaviyo 将这些数据汇总在一起，以确定个人资料最符合哪个客户群体（例如，忠诚客户）。这些见解非常有用，因为它们可以优化您的营销策略，包括如何个性化消息、如何鼓励重复购买、消息发送的频率和时间等。此外，对于可能面临风险的客户或细分群体，您可以使用这些见解来推动赢回营销活动并减少客户流失。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 和 [营销分析](https://help.klaviyo.com/hc/en-us/articles/33789259613595) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。前往我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672) 了解如何购买这些计划。 ## 开始之前</p>
<p>您的报告需要：</p>
<ul>
<li>至少有500名已下订单的客户。这并不是指个人资料总数，而是实际向您的企业下过订单的人数。请注意，如果此部分位于个人资料中但为空，则 Klaviyo 没有足够的有关该人的数据来进行预测。 - 您有电子商务集成（例如 Shopify、BigCommerce、Magento 等）或使用 Klaviyo API 发送下订单。 - 您有至少 180 天的订单历史记录，并且在过去 30 天内有订单。 - 您至少有一些客户下了 3 个或更多订单。只有所有者、管理员、经理和分析师才能访问此报告。此外，如果您创建了[新的自定义指标](https://help.klaviyo.com/hc/en-us/articles/22311085738395/)，则此更改最多可能需要 48 小时才会反映在您的报告中。 ## 最近的报告更新（截至 2024 年 5 月 2 日）</li>
</ul>
<p>自 2024 年 5 月 2 日起，RFM 报告正在推出新的属性和设置。请查看以下[现有]信息(https://klaviyo.zendesk.com/hc/en-us/articles/18193920339483#h_01HWWHY499J0M3QFMVG16Z3ZWY) 和[新](https://klaviyo.zendesk.com/hc/en-us/articles/18193920339483#h_01HWWJ5KRZPD5X16RRWRMN70BWQ)使用高级 KDP 的客户。 ### 使用 Klaviyo Advanced KDP 的现有客户</p>
<h4>配置文件属性更改</h4>
<p>RFM 报告将具有 3 个新属性。从 2024 年 5 月 2 日开始，Klaviyo 推出了下表所示的新属性。然后在 5 月 21 日，Klaviyo 自动更新您的分段以使用这些新属性并删除旧属性值。 | <strong><em>*旧房产</strong><strong> | </strong><strong>新房产</strong><strong> | </strong><strong>它测量什么？</strong><strong> | </strong><strong>其他注意事项</strong></em>* |</p>
<p>| --- | --- | --- | --- |</p>
<p>| <strong>$当前\_月\_rfm\_group</strong> | <strong>现任 RFM 小组</strong> |配置文件当前所属的 RFM 组。 |  |</p>
<p>| <strong>$前\_月\_rfm\_group</strong> | <strong>前 RFM 小组</strong> |最近的<strong>不同</strong> RFM 组，该配置文件属于其当前 RFM 组之前的组。 |在配置文件的 RFM 组发生更改之前，其<strong>之前的 RFM 组</strong>将显示为 <strong>未知</strong><strong><em></strong></em>。<em>*</em>* |</p>
<p>|不适用 | <strong>RFM 组最后更改</strong> |配置文件从 <strong>前一个 RFM 组</strong> 转换到 <strong>当前 RFM 组</strong> 的时间戳。仅当配置文件更改其 RFM 组时才会出现此情况。 |  |</p>
<h4>当配置文件属性刷新时</h4>
<p>此外，RFM 属性每晚都会刷新，而不是每月 1 号。这意味着 Klaviyo 将每 24 小时检查一次更新，如果配置文件上的这些 RFM 属性已更改，您将看到这些更改得到反映。但是，如果您更新 RFM 设置，配置文件属性更改将在 2 小时内反映出来。请记住，RFM 仪表板会立即更新，而配置文件记录上的更改会延迟更新。因此，您可能会在仪表板中看到每个 RFM 组的数字差异，但这些差异尚未反映在您的配置文件中。 ### 使用高级 KDP 的新客户</p>
<p>在 2024 年 5 月 2 日或之后刚刚加入高级 KDP 的新客户无需担心过渡到新的配置文件属性，因为这些属性已经成为标准。 此外，请记住，在入职或更新 RFM 模型时，当模型计算 <strong>当前 RFM 组</strong> 并检测先前状态时，您可能会看到 <strong>先前 RFM 组</strong> 的 <strong>未知</strong> 状态。 ## 导航至报告</p>
<p>导航到<strong><em>*高级 KDP > 智能 > 客户洞察 > RFM 分析</strong><strong></em></strong><em>。<strong></em><em> 或者，如果您是 Marketing Analytics 客户，请导航到 </strong><strong>营销分析</strong><strong> > </strong><strong>客户洞察</strong><strong> > </strong><strong>RFM 分析</strong><strong>。在这里，您将看到默认报告设置为当前日期之前 30 天的开始日期和当前日期的结束日期。每晚或 24 小时，系统都会自动更新 </strong>当前 RFM 组<strong>、</strong>上一个 RFM 组<strong>和 </strong>RFM 组上次更改</em>*属性。请记住，RFM 仪表板会立即更新，而配置文件记录的更改每 24 小时更新一次。因此，您可能会在仪表板中看到每个 RFM 组的数字差异，但这些差异尚未反映在您的配置文件中。 ###比较顾客卡分布情况</p>
<p><strong>比较客户分布</strong>卡细分：</p>
<ul>
<li>您的 RFM 组</li>
<li>显示每个组中添加或删除的客户。 - 显示特定时间范围内每组的百分比变化。此卡有助于了解客户如何在不同组之间分配以及您当前的营销工作是否产生了影响。详细了解 [Klaviyo 如何计算您的百分位数、分数和客户群体](https://help.klaviyo.com/hc/en-us/articles/17797937793179)。 ### 客户选项卡</li>
</ul>
<p><strong>客户</strong>选项卡以条形图格式按日期显示您的客户组。左侧是 Klaviyo 确定的客户组，蓝色条代表报告时间范围的开始日期，绿色条代表报告时间范围的结束日期。在这里，您可以比较您的客户群体在特定时期内的变化情况。 ![比较发行版-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730698651)</p>
<p>通过将鼠标悬停在图表中的任何条形上，您可以查看：</p>
<ul>
<li>开始和结束日期</li>
<li>适合该客户群的配置文件数量。 - 该组在所有组中所占的百分比。 ![悬停，客户选项卡.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701728923)</li>
</ul>
<h3>添加或删除选项卡</h3>
<p><strong>添加或删除</strong>选项卡显示每个客户组的条形图以及报告开始日期和结束日期之间发生的任何更改。您可以查看从每个客户组添加（每个条形的青色部分）或删除（每个条形的红色部分）的配置文件数量。此图表有助于查看每个客户组的总增加和减少以及您应该将营销工作集中在哪里。 ![比较客户分布tab.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701722651)</p>
<p>通过将鼠标悬停在图表中的任何条形上，您可以查看每个客户组删除和添加的配置文件的总数。 ![添加或删除，hover.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701724059)</p>
<h3>百分比变化选项卡</h3>
<p><strong>百分比变化</strong>选项卡按报告的开始日期和结束日期显示每个客户组的数据。此表显示每组的配置文件总数、占所有组的百分比，以及每组删除或添加的配置文件的百分比变化（正或负）。该表是静态的，不允许排序或过滤。 ![比较分布选项卡.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701726875)</p>
<h2>小组随时间变化卡</h2>
<p><strong>组随时间变化</strong>卡提供了您的客户组的直观表示以及从开始日期到结束日期这些组之间客户的潜在移动情况。 - 卡片的左侧是报告开始日期的所有客户组。 - 卡的右侧是结束日期的所有客户组。 - 这些日期之间的线条可视化客户的动向，以及他们是否留在同一组中，或者由于他们的购买行为而移动到不同的组。这张卡对于破译这些客户路径中是否存在模式非常有用，特别是当客户随着时间的推移可能会放弃购买时。 例如，如果您的许多忠诚客户主要是下降到较低的组别，而不是上升到冠军，这可能表明需要在他们可能流失之前重新吸引这些资料。详细了解 [Klaviyo 如何计算您的百分位数、分数和客户群体](https://help.klaviyo.com/hc/en-us/articles/17797937793179)。 <strong>从未购买</strong>组仅在左侧的开始日期可见。这是因为图表中显示的所有客户在结束日期之前都至少进行过一次购买。在结束日期之前从未进行过购买的客户根本不会反映在此图表中。 ![组随时间变化card-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730712859)</p>
<p>如下所示，通过将鼠标悬停在任何组名称上，您可以查看客户路径以及进出每个组的个人资料移动总数。 ![悬停、动作、组.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701734555)</p>
<p>此外，通过将鼠标悬停在图表中间的任何特定路径或线条上，您可以查看从一组移动到另一组的配置文件数量。 ## 中值性能卡</p>
<p><strong>中值绩效</strong>卡提供了每个客户组的中值绩效视图。通过单击此卡上的 <strong><em></strong>开始日期 <strong></em></strong> 和 <strong><em></strong> 结束日期 <strong></em></strong> 选项卡，您可以查看每个日期和关键指标的中值绩效（即 <strong>自购买后的天数</strong>、<strong>采购订单数量</strong> 和 <strong>下单收入</strong>）。详细了解 [Klaviyo 如何计算您的百分位数、分数和客户群体](https://help.klaviyo.com/hc/en-us/articles/17797937793179)。了解绩效数据中位数可以帮助您了解所有数据的中间点以及客户行为的中心趋势，特别是在您有异常值或不均匀数据的情况下。例如，如果您有不同的高价值、频繁购买和一些低价值、不频繁的客户购买，那么查看大多数订单通常发生的时间及其价值的中间交集可能会有所帮助。该表是静态的，不允许排序或过滤。 ![屏幕截图 2024-10-07 12.55.04 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/31276857610395)</p>
<h2>自定义报告</h2>
<p>默认情况下，您的 RFM 报告将开始日期设置为当天之前 30 天，将结束日期设置为当天。它还会自动确定您帐户特有的 RFM 分数 [使用阈值](https://help.klaviyo.com/hc/en-us/articles/17797937793179)。但是，您可以调整这些项目并定制报告以满足您特定的 RFM 跟踪需求。详细了解 [Klaviyo 如何计算您的百分位数、分数和客户群体](https://help.klaviyo.com/hc/en-us/articles/17797937793179)。 ### 选择开始和结束日期</p>
<p>在报告顶部，从日历选择器中选择开始日期和结束日期。您可以选择任何日期，只要开始日期早于结束日期即可。更新日期将触发所有数据和组的自动重新计算。 ![日历视图选择器.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730717979)</p>
<h3>选择不同的转化指标</h3>
<p>默认情况下，您的 RFM 报告将使用您帐户最常用的 <strong>已下订单</strong> 统计数据来计算初始 RFM 分数。大多数公司只有一项<strong>已下订单</strong>统计数据，但有些公司会有多项（例如，如果您有多个集成）。您可以将其调整为电子商务集成中的另一个基于价值的指标。 1. 要更改指标，请在报告顶部单击<strong><em>*高级设置</strong><strong>。从这里，您将看到 </strong>RFM 详细信息</em>* 菜单。 ![RFM 详细信息菜单.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730721691)</p>
<p>2. 在<strong>转化指标</strong>部分中，打开<strong><em>*选择选项</strong></em>*下拉列表。 3. 从下面的列表中选择不同的转化指标。更新指标将触发所有数据和组的重新计算。您还可以在 RFM 报告中使用[自定义指标](Custom%20metrics)，详细了解[策略性地使用这些指标](https://help.klaviyo.com/hc/en-us/articles/18194102384539#h_01JBYHZ18494EV5Y93DZ1D2237)。 ![转化指标下拉菜单选择.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701746715)</p>
<p>4.（推荐但可选）单击<strong><em>*预览</strong></em>*在保存之前查看您的更改。 建议预览您的更改，以确保新的转化指标提供您期望的数据。当您处于预览模式时，您将看到如下所示的横幅。 ![预览菜单横幅.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701748891)</p>
<p>5. 对更新感到满意后，单击<strong><em>*保存</strong></em>*。 ### 调整 RFM 值</p>
<p>您可能会发现需要调整从数据中派生的 RFM 值以查看特定类型的客户。例如，您可能希望报告显示更高的历史客户支出。根据您的<strong>货币定义</strong>调整到更高的分数或百分位将随着时间的推移生成更高支出客户的报告。您有 2 个选项来调整 RFM 值：</p>
<ul>
<li>****使用百分位数更改您的 RFM 分数****</li>
</ul>
<p>使用百分位数更改 RFM 分数可以精确控制生成分数和客户分组的特定百分比。例如，您可能只想查看购买非常频繁的客户，因此您可以将频率最小百分位设置为 75%。这只会在报告中为排名前 75% 的客户提供 3 分，并使其仅关注那些非常频繁的购买者。请注意，由于需要根据订单之间的平均天数来建立阈值，因此新近度百分比不可用。对于这些定义，请使用数字分数，如下定义。 - <strong><em>*使用值更改您的 RFM 分数</strong></em>*</p>
<p>使用值更改 RFM 分数可以让您控制导致客户分组的 Klaviyo 分数。由于您最了解客户，因此自定义分数可以帮助您更好地符合他们的特定行为。例如，您可以设置 4 次购买的频率值来分配您的高分。这意味着购买 4 件或更多商品的任何人都会自动获得 3 价值。如果您想在报告中关注非常频繁的购物者，这会很有帮助。但是，如上所述，为了精确控制百分比和数据，使用 RMF 百分位数切换来定义客户组可能更有利。 ### 更改您的 RFM 百分位</p>
<p>1. 在报告顶部，单击<strong><em>*高级设置</strong><strong>。 2. 选择要调整的定义（</strong>近期定义<strong>、</strong>频率定义<strong>或</strong>货币值定义</em>*）。单击打开适用的菜单，如下例所示。 ![RFM 值设置 open-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730730395)</p>
<p>3. 单击“<strong><em>*基于百分位数的分数</strong></em>*”的切换按钮。 4. 在此，通过在字段中填写新的百分比来调整您的最高分数或平均分数。请注意，值必须介于 1 到 100 之间，并且不应包含任何特殊字符，包括“%”字符。在下面的示例中，使用 66% 作为最低历史支出将使属于该较高百分位数的所有客户自动获得 3 值。如果您想随着时间的推移专注于支出较高的客户，这会很有帮助。 ![百分比字段已更改.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701753499)</p>
<p>5.（推荐但可选）单击<strong><em>*预览</strong></em>*在保存之前查看您的更改。建议预览您的更改，以确保新的百分位数提供您期望的数据。当您处于预览模式时，您将看到如下所示的横幅。 ![预览菜单横幅.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701748891)</p>
<p>6. 对更新感到满意后，单击<strong><em>*保存</strong></em>*。 ### 更改您的 RFM 分数</p>
<p>1. 在报告顶部，单击<strong><em>*高级设置</strong><strong>。 2. 然后选择您要调整的定义（</strong>近期定义<strong>、</strong>频率定义<strong>或</strong>货币值定义</em>*）。单击打开适用的菜单，如下例所示。 ![RFM 值设置 open-updated.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730730395)</p>
<p>3. 在此，通过在字段中填写新值来调整您的最高分数或平均分数。如果您要更新 <strong>货币价值</strong> 定义，您应该使用代表货币或货币价值的值（例如，250 代表我的帐户 250 美元）。在下面的示例中，使用 250 美元作为历史最低支出值，这样只有支出至少 250 美元的客户才会被评为“最佳”客户（值为 3）。 请注意，这些必须是整数，并且不能使用特殊货币字符。建议也使用与您的帐户设置相同的货币值，因为它不会在此处转换值。 ![货币定义设置_UPDATED.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730735515)</p>
<p>4.（推荐但可选）单击<strong><em>*预览</strong></em>*在保存之前查看您的更改。建议预览您的更改，以确保新的百分位数提供您期望的数据。当您处于预览模式时，您将看到如下所示的横幅。 ![预览菜单横幅.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711701748891)</p>
<h2>错误排查</h2>
<h3>编辑 RFM 设置</h3>
<p>如果您收到如下所示的错误消息，则您可能尝试使用不兼容的值或特殊字符保存 RFM 设置。价值观应该：</p>
<ul>
<li>为数值</li>
<li>为整数</li>
<li>彼此不冲突（例如，平均总支出高于最低总支出）</li>
<li>不包含特殊字符</li>
</ul>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/28711701757467" alt="错误横幅.jpg" />
<h3>空卡或报告</h3>
<p>有时，Klaviyo 可能无法立即检索您的数据。如果发生这种情况，您将看到如下所示的错误通知。如前所述，刷新整个报告页面以重新加载此卡。如果您收到一条带有绿色进度条的“正在应用更改”消息，则您的数据仍在加载。这不是数据错误，因此无需刷新页面。您的数据将立即加载到您的卡中。 ![rfm 空报告错误.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28711730739867)</p>
<h2>查看单个配置文件的 RFM 统计信息</h2>
<p>除了主 RFM 报告中提供的见解之外，您还可以查看各个配置文件的 RFM 数据和分组。为此，您将在每个配置文件上使用 <strong>RFM 分析</strong> 卡。 1. 如果您要浏览 <strong>个人资料</strong> 部分，请导航至<strong><em>*受众 > 个人资料 > 指标和见解</strong><strong>。如果您在细分生成器中，请导航至</strong><strong>受众 > 列表和细分</strong><strong> 并找到细分。单击</strong><strong>个人资料</strong><strong>并前往</strong><strong>指标和见解</strong><strong>。 2. 在 </strong>预测分析<strong> 卡下方找到 </strong>RFM 分析</em>* 卡。如下例所示，该卡将包含：</p>
<ul>
<li>配置文件的当前 RFM 组（请注意，RFM 组基于每日更新的每日值）。 - 该配置文件的先前 RFM 组用于比较。 - RFM 组上次更改的时间戳，或配置文件从 **前一个 RFM 组** 移动到 **当前 RFM 组** 的时间。仅当配置文件更改其 RFM 组时才会出现此情况。 - 与转化次数和潜在收入相关的数据。 （请注意，这些将是从您的 RFM 数据派生的基于收入的指标，例如**已下订单、已订购产品、已履行订单**等）。 ![](https://klaviyo.zendesk.com/hc/article_attachments/28711730743579)</li>
</ul>
