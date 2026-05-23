<h1>如何创建由 RFM 组和客户行为变化触发的保留流程</h1>

<h2>你将会学到</h2>
<p>了解如何基于 RFM 属性构建针对最近未购买的客户的保留流程。保留流是帮助赢回客户、在正确的时间向他们传达正确的信息的有用驱动力。您可以在客户群发生变化时自动联系这些订阅者，从而可能降低收入和流失风险。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 和 [营销分析](https://help.klaviyo.com/hc/en-us/articles/33789259613595) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。前往我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672) 了解如何购买这些计划。 ## 开始之前</p>
<p>您的 RFM 报告需要：</p>
<ul>
<li>至少有500名已下订单的客户。请注意，这并不是指个人资料总数，而是实际向您的企业下过订单的人数。请注意，如果此部分位于个人资料中但为空，则 Klaviyo 没有足够的有关该人的数据来进行预测。 - 您有电子商务集成（例如 Shopify、BigCommerce、Magento 等）或使用 Klaviyo API 发送下订单。 - 您有至少 180 天的订单历史记录，并且在过去 30 天内有订单。 - 您至少有一些客户下了 3 个或更多订单。 - 请注意，只有所有者、管理员、经理和分析师才能访问此报告。如果您已创建要在 RFM 报告中使用的[新自定义指标](https://help.klaviyo.com/hc/en-us/articles/22311085738395/)，则最多可能需要 48 小时才能反映此更改。 ## 如何创建流程</li>
</ul>
<p>您可以浏览[流库](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8Q0PAF1FY71QDZBJ7M)以使用预构建的模板之一或按照以下指南创建自定义保留流。无论哪种情况，根据 RFM 组分段触发流程都很重要。 ### 创建您的细分</p>
<p>如果您尚未这样做，则需要创建一个包含您的 <strong>有风险</strong> 或 <strong>需要关注</strong> 客户的细分。如果您已经设置了分段，请跳至[下面有关创建流程的部分](#h_01JCNG895SY86NN11V59RY58SJ)。 1. 如果您是高级 KDP 客户，请导航至<strong><em>*高级 KDP</strong><strong> > </strong><strong>情报</strong><strong> > </strong><strong>客户洞察</strong><strong> > </strong><strong>RFM 分析</strong><strong>。或者，如果您是 Marketing Analytics 客户，请导航至 </strong><strong>Marketing Analytics</strong><strong> > </strong><strong>客户洞察</strong><strong> > </strong><strong>RFM 分析</strong><strong>。 2. 滚动找到 </strong>RFM 分段<strong> 卡，然后单击 </strong><strong>创建分段</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682037019)</p>
<p>3. 进入细分生成器后，为您的细分命名并从 <strong>标签</strong> 下拉列表中添加任何适用的标签。例如，您可以将流程命名为“需要注意或有风险部分”或“需要注意或有风险部分 - 仅限一次性买家”，具体取决于您计划如何设置流程。 4. 在 <strong>定义</strong> 下拉列表中，选择 <strong>关于某人的属性</strong><strong>。 5. 在 </strong>维度<strong> 下拉列表中，选择 </strong>当前 RFM 组<strong><em>* 选项。确保在第二个下拉列表中选择</strong>等于<strong>。 6. 在 </strong>输入值<strong> 字段中，找到并选择 </strong>有风险<strong></em><em>。确保</strong>类型<strong>设置为</strong>文本</em>*。您的片段应如下图所示。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30931707859227)</p>
<p>7.<strong><em>*选择+添加条件</strong><strong>。确保您的连接器设置为 </strong>OR<strong>。 8. 从这里开始，重复上面的步骤 4-6，而不是选择 </strong>At Risk<strong>，而是选择 </strong><strong>Needs Attention</strong><strong> 作为您的 RFM 组。完成后，您的细分的前 2 个步骤应如下所示，并包括您的 </strong>需要注意<strong> 或 </strong>有风险</em>* 组中的任何人。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30931707861403)</p>
<p>9. 可选：<strong>有风险</strong>和<strong>需要注意</strong>组可以包括过去至少购买过一次的用户。但是，如果您希望定位过去购买过一定次数的客户（例如，仅一次性购买者），但现在属于 <strong>有风险</strong> 或 <strong>需要注意</strong> 组，则可以使用 <strong>**+添加条件</strong><strong> 添加 </strong>AND<strong> 连接器。 10. 可选：选择</strong><strong>某人已经做过（或没有做过）的事情</strong><strong>。 11. 可选：选择您的 </strong>已下订单<strong> 指标。 12. 选项：选择</strong>等于<strong>以及您选择的任何订单数量。然后选择“一直”</strong>。这应该类似于下面的示例。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30931707863067)</p>
<h3>设置您的流程</h3>
<p>1. 前往<strong><em>*Flows</strong><strong> 选项卡。 2. 单击</strong><strong>创建流</strong><strong>。 3. 单击</strong><strong>构建您自己的。</strong></em>*</p>
<p>4. 在 <strong>创建流程</strong> 侧面板中，将您的流程命名为可识别的名称，然后选择您希望其具有的任何标签。例如，“有风险或需要注意”流程。</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/30931682047259" alt="" />
<p>5. 单击<strong><em>*手动创建</strong><strong>。 6. 在右侧触发面板中，选择</strong><strong>添加到段</strong></em>*。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682048411)</p>
<p>7. 在 <strong>添加到分段</strong> 部分中，查找并选择您的分段。这应该是包含您的 <strong>有风险</strong> 或 <strong>需要注意</strong> 组的部分。您的触发器应类似于以下示例。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682050715)</p>
<p>8. 创建完触发器后，单击<strong><em>*保存</strong><strong>。然后在弹出窗口中单击</strong><strong>确认并保存</strong></em>*以保存您的触发器。 9. 从左侧面板拖入您的第一封保留式电子邮件。这应该是一条欢迎客户回来的消息。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682051867)</p>
<p>10. 在第一条消息之后拖入一个时间延迟，以便您的客户不会立即收到流中的所有消息。建议客户至少等待 2-3 天才能收到下一条消息。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682055323)</p>
<p>11. 从左侧面板拖入第二封保留式电子邮件。这应该是一条与您的第一封电子邮件不同的消息，并鼓励您的客户回来访问您的商店。 ![](https://klaviyo.zendesk.com/hc/article_attachments/30931682057883)</p>
<p>12. 可选：如果您想向流程中添加更多消息，请添加另一个时间延迟。确保这是您最后一条消息后至少 2-3 天。 13. 可选：从左侧面板拖入第三封电子邮件。此消息应与您的前两条消息不同，并且可能包含时效性折扣或优惠等内容。 14. 创建流程后，单击右上角的“<strong><em>*更新状态</strong><strong>”，然后选择“</strong>实时<strong>”或“</strong>手动<strong>”。实时流及其所有消息都会自动发送，而手动流则需要您手动查看和发送所有计划的消息。详细了解[流程状态](https://help.klaviyo.com/hc/en-us/articles/115002774932#h_01H9JGTZ8RVQANQHGVRJ6V4W63)。 15. 设置流程状态后，单击</strong><strong>保存</strong></em>*。 ## 保留电子邮件最佳实践</p>
<h3>有条件的分割</h3>
<p>它是可选的，但您可以根据向客户展示的产品类型使用[条件分割](https://help.klaviyo.com/hc/en-us/articles/115003872171)。通过这种方式，您可以针对客户提供与他们之前购买的产品相关的产品，或者根据他们的 RFM 组突出显示他们可能感兴趣的畅销产品（例如，较低成本或入门级产品）。 ### 使用模板标签</p>
<p>让客户感觉他们收到的电子邮件与他们完全相关且个性化，这一点很重要。考虑使用[模板标签](https://help.klaviyo.com/hc/en-us/articles/4408802648731)从客户的个人资料中提取信息，以个性化发送给他们的电子邮件。提取简单的项目，例如名字或地区，或者使用更高级的技术来提取他们最近可能查看过的项目，特别是对于您最初重新与他们互动后流程中稍后的电子邮件。此外，如果您需要更好地调整数据并使其更具可操作性，请考虑[数据转换](https://help.klaviyo.com/hc/en-us/articles/17760400736539)来标准化这些配置文件属性。 ### 在现有电子邮件中使用显示/隐藏逻辑</p>
<p>您还可以[使用模板编辑器的 <strong>显示/隐藏逻辑</strong> 功能](https://help.klaviyo.com/hc/en-us/articles/7655965301531) 定制现有电子邮件中的各个块或部分，并将目标锁定在 <strong>需要注意</strong> 或 <strong>有风险</strong> RFM 组中。 #### <strong>需要注意</strong>内容</p>
<p>由于该组中的客户比 <strong>有风险</strong> 的客户更有可能参与，并且在成为之前的 <strong>忠诚</strong> 或 <strong>最近</strong> 会员后可能有更多的客户进入该组，因此您可能需要考虑以下活动块：</p>
<ul>
<li>折扣或奖励</li>
<li>显示他们当前的忠诚度积分状态</li>
<li>与他们之前购买过的产品类似或相邻的产品</li>
<li>您浏览次数最多的产品</li>
<li>您评价最高的产品</li>
<li>您的最新产品</li>
</ul>
<h4>**有风险**内容</h4>
<p><strong>有风险</strong>的客户更容易流失，而且他们距离<strong>一次购买的时间可能比</strong>需要注意<strong>的会员更长。除了上述类型的消息之外，您可能还需要为 </strong>需要注意** 组中的客户考虑以下内容：</p>
<ul>
<li>较低成本或入门级物品，包括以下物品：</li>
<li>与他们之前购买过的产品类似或相邻的产品</li>
<li>您浏览次数最多的产品</li>
<li>您评价最高的产品</li>
</ul>
<h3>运行 A/B 测试</h3>
<p>使用 A/B 测试继续细化哪些电子邮件内容会促使您的 <strong>需要注意</strong> 或 <strong>有风险</strong> RFM 群体购买并退出这些群体。例如，您可能想根据以下条件测试不同的产品推荐：</p>
<ul>
<li>您最畅销的产品</li>
<li>与他们之前购买过的产品类似或相邻的产品</li>
<li>补充或重新订购之前购买的产品（如果适用）</li>
<li>您浏览次数最多的产品</li>
<li>您评价最高的产品</li>
<li>您的最新产品</li>
</ul>
<p>此外，请务必测试您的主题行、发送时间以及在特定时间段内发送的电子邮件数量，以了解哪些内容可以帮助激励这些客户群体。您可能希望在内容中使用主题行来营造紧迫感。详细了解[A/B 测试您的流程电子邮件](https://help.klaviyo.com/hc/en-us/articles/6960371049115)。 ## 其他资源</p>
<p><a href="https://help.klaviyo.com/hc/en-us/articles/18193920339483">如何使用 RFM 属性构建分段</a></p>
<p><a href="https://help.klaviyo.com/hc/en-us/articles/18194102384539">如何在营销活动和流程中战略性地使用 RFM 属性</a></p>
<p><a href="https://www.klaviyo.com/customers/case-studies/ruffwear-cdp">Ruffwear 使用 Klaviyo CDP 增加收入并提高利润（案例研究）</a></p>
