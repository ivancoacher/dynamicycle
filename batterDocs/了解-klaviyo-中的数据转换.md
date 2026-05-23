<h1>了解 Klaviyo 中的数据转换</h1>

<h2>你将会学到</h2>
<p>了解 Klaviyo 中的数据转换工具，以及如何使用它来使数据更有用。 [高级 KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) 不包含在 Klaviyo 的标准营销应用程序中，需要订阅才能访问相关功能。请参阅我们的[计费指南](https://help.klaviyo.com/hc/en-us/articles/115000976672)，了解如何购买此计划。 ![](https://fast.wistia.com/embed/medias/r18x9gg89n/swatch)</p>
<h2>转换数据</h2>
<p>要在 Klaviyo 中转换数据：</p>
<p>1. 导航到<strong><em>*高级 KDP</strong><strong></em></strong><em>><strong></em></strong><strong><em>数据管理 > 转换</strong><strong>下的 </strong>转换<strong> 选项卡。 2. 选择一个预先构建的转换，或选择</strong><strong>创建</strong><strong>按钮从头开始定义您自己的转换规则。 3. 如果创建您自己的转换，请选择您想要转换的配置文件属性以及转换方法。转换后的属性和值将保存在名为 </strong>Property\_transformed<strong> 的新配置文件属性下； </strong>属性<strong> 是原始配置文件属性的名称，并附加 </strong>\_transformed<strong> 后缀。附加转换不能应用于属性的转换版本（即 </strong>Property\_transformed</em>*）。 ![CDP 导航中的“转换”选项卡](https://klaviyo.zendesk.com/hc/article_attachments/28716356228123)</p>
<p>只有以下角色可以创建、编辑和删除转换：</p>
<ul>
<li>业主</li>
<li>管理员</li>
<li>经理</li>
</ul>
<h2>转换方法</h2>
<p>Klaviyo 中的数据转换工具允许您对配置文件属性值进行以下转换：</p>
<ul>
<li>****格式****</li>
</ul>
<p>重新格式化配置文件属性值。 - <strong><em>*标准化</strong></em>*</p>
<p>设置规则以自动替换特定的配置文件属性值。 - <strong><em>*合并</strong></em>*</p>
<p>将多个自定义配置文件属性合并为 1 个属性</p>
<p>每个配置文件属性只能应用一个 <strong>格式</strong> 和 <strong>标准化</strong> 转换</p>
<p>配置文件属性值的转换适用于所有现有配置文件，并将持续应用。 ### 格式</p>
<p>格式转换方法有 5 种格式选项：</p>
<p>1.<strong><em>*删除空格</strong></em>*</p>
<p>删除值开头和结尾的空格（例如，“ABC”到“ABC”）。 2.<strong><em>*删除引号</strong></em>*</p>
<p>删除值开头和结尾的引号（例如，“ABC”到 ABC）。 3.<strong><em>*删除特殊字符</strong></em>*</p>
<p>删除所有非数字和字母的字符（例如，A、B、C 到 ABC）。 4. <strong><em>*每个单词的第一个字母大写</strong></em>*</p>
<p>每个单词的第一个字母大写（例如，John doe 到 John Doe）。 5.<strong><em>*修改日期格式</strong></em>*</p>
<p>修改日期和时间格式，以便可以以一致的格式存储它们。您可以仅设置日期格式，也可以设置日期和时间的格式。日期在我们的系统中以 ISO 8601 格式存储（YYYY-MM-DD 和 YYYY-MM-DD HH:MM:SS.SS），但它们在应用程序中的显示方式取决于您的区域设置。转换属性值时，您可以根据需要选择任意多个格式选项。 ![修改日期.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716356253723)</p>
<p>多个格式规则按以下顺序应用：</p>
<p>1. 删除空格</p>
<p>2.删除引号</p>
<p>3.删除特殊字符</p>
<p>4.单词大写</p>
<p>5. 修改日期</p>
<p><strong><em>*格式转换示例</strong></em>*</p>
<p>在此示例中，使用格式规则将 <strong>Format</strong> 转换应用于 Klaviyo 中的 <strong>Name</strong> 配置文件属性：</p>
<ul>
<li>删除空格</li>
<li>删除特殊字符</li>
<li>每个单词的第一个字母大写</li>
</ul>
<p>如果原始 <strong>Name</strong> 配置文件属性的值设置为 <strong>“alex!”</strong>，则此转换将导致创建一个名为 <strong>name\_transformed</strong> 的新配置文件属性，其值设置为 <strong>Alex。</strong></p>
<p>###</p>
<h3>标准化</h3>
<p>通过标准化转换方法，您可以设置规则以自动替换特定的配置文件属性值。 ![标准化转换规则](https://klaviyo.zendesk.com/hc/article_attachments/28716356234395)</p>
<p>创建标准化规则：</p>
<p>1. 在 <strong>If value</strong> 条件中，选择 <strong>Contains</strong> 或 <strong>Equals。</strong></p>
<p><strong>Contains</strong> 运算符要求替换属性值以包含您为 <strong>If 值</strong> 输入的指定子字符串。请注意，整个属性值将被替换，而不仅仅是匹配的子字符串。 <strong>包含</strong>仅支持文本值。 <strong>等于</strong>运算符要求被替换的值和替换值之间完全匹配。 整个财产价值将被重置价值所取代。 2. 为<strong>If 值</strong>选择[数据类型](https://help.klaviyo.com/hc/en-us/articles/115005237648)。 3. 在 <strong>If value</strong> 条件中输入要替换的所需值。您将看到一个下拉列表，其中显示您的帐户中最多存在 512 个正在转换的资源的唯一值。您可以在一个条件中包含最多 30 个值，或者通过选择下拉列表中的 <strong>输入新值</strong> 选项来创建新值。 ![从下拉菜单中设置多个值以实现标准化条件](https://klaviyo.zendesk.com/hc/article_attachments/28716333272091)</p>
<p>具有大量唯一值（例如<strong>电子邮件</strong>、<strong>电话号码、</strong><strong>名字、</strong>和<strong>姓氏</strong>）的属性不会出现在下拉列表中。 4. 在 <strong>替换为</strong> 条件中，选择替换值的[数据类型](https://help.klaviyo.com/hc/en-us/articles/115005237648)。 5. 在 <strong>替换</strong><strong>为</strong> 条件中输入所需的替换值。对于列表数据类型，值必须位于方括号内，并用逗号分隔值（例如 [1,2,3] 或 [A,1,True]）</p>
<p>您最多可以创建 10 条标准化规则，这些规则用“If else”逻辑进行解释。如果第一个条件不匹配，则将评估下一个条件，并且这将继续，直到条件匹配为止。匹配完成后，其余条件不再评估。如果没有条件匹配，将为转换后的配置文件属性设置原始值。 <strong><em>*标准化转换示例</strong></em>*</p>
<p>在此示例中，使用标准化规则将 <strong>Standardize</strong> 转换应用于 <strong>Country</strong> 配置文件属性：</p>
<ul>
<li>如果值包含 **America** 替换为 **USA**</li>
<li>如果值等于 **可以** 替换为 **加拿大**</li>
<li>**如果值等于“加拿大”，则替换为加拿大**</li>
</ul>
<p>如果 <strong>Country</strong> 配置文件属性的值设置为 <strong>America</strong>，则此转换将导致创建一个名为 <strong>country\_transformed</strong> 的新配置文件属性，其值设置为 <strong>USA。</strong> 如果 <strong>Country</strong> 属性的值最初设置为“<strong>Canada”</strong>，则这将创建 <strong>country\_transformed</strong> 属性，其值设置为 <strong>Canada</strong>。 ### 合并</p>
<p><strong>合并</strong> 转换允许您将多个自定义配置文件属性合并为 1 个，从而使您能够有效地使用模板中分段中的数据。转换按以下顺序应用：</p>
<p>1. 合并</p>
<p>2. 格式</p>
<p>3.标准化</p>
<p>要创建合并规则：</p>
<p>4. 选择最多 10 个要合并的配置文件属性。默认情况下，合并必须包含 2 个属性，但可以使用 <strong>添加</strong> 按钮包含更多属性。转换中包含的属性的顺序决定了合并过程中值的优先级，列表顶部的项目具有最高优先级。在上面的示例中，<strong>头发类型</strong> 将是作为此合并的一部分在配置文件上设置的主要属性。 ![marge_hair_type.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716356261659)</p>
<p>2. 要更改合并中包含的属性的优先级，请使用向上和向下箭头。 3. 设置合并转换后，选择<strong><em>*保存</strong><strong>。您可以通过单个 </strong>合并<strong> 转换组合最多 10 个属性。请注意，保存转换后，您将无法再更改最高优先级。相反，您可以删除该转换并创建一个新转换。 </strong><strong>合并转换示例</strong></em>*</p>
<p>在此示例中， <strong>合并</strong> 转换应用于 <strong>Birthday</strong> 和 <strong>Birthdate</strong> 属性，以合并为一个名为 <strong>Birthday\_transformed</strong> 的属性。 ![生日:生日.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716356256027)</p>
<p>如果一个配置文件的 <strong>Birthday</strong> 属性设置为 06/07/1998，而另一个配置文件的 <strong>Birthdate</strong> 属性设置为 06/04/2001，则转换将导致每个唯一属性更新为 <strong>Birthday\_transformed</strong>，并保留其原始值。 ## 预建转换</p>
<p>您可以使用 <strong>转换</strong> 工具快速启用 4 个预构建的转换。 1.<strong><em>*格式化名字</strong></em>*</p>
<p>将个人资料的名字大写，以确保消息传递的一致性（例如，<strong>alex</strong> 到 <strong>Alex</strong>）。 ![预先构建的转换，以大写字母格式化名字](https://klaviyo.zendesk.com/hc/article_attachments/28716333274139)</p>
<p>2. <strong><em>*标准化国家/地区名称</strong></em>*</p>
<p>标准化常见国家/地区名称，使它们都具有相同的值，从而实现相似配置文件的一致性并更容易进行细分（例如，<strong>美国</strong>或<strong>美国</strong>到<strong>美国</strong>）。 ![预先构建的转换以标准化国家/地区名称的变体](https://klaviyo.zendesk.com/hc/article_attachments/28716333281179)</p>
<p>3. <strong><em>*美国州名标准化</strong></em>*</p>
<p>对所有 50 个州的值进行标准化，以便在相似的配置文件之间保持一致性并更容易进行细分（例如，<strong>纽约</strong> 或 <strong>纽约</strong> 到 <strong>纽约</strong>）。 ![预先构建的转换以标准化美国州名的变体](https://klaviyo.zendesk.com/hc/article_attachments/28716356247195)</p>
<p>4.<strong><em>*格式化生日</strong></em>*</p>
<p>设置生日属性的格式以确保分段和消息传递的一致性。 ![格式日期预建.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716333294363)</p>
<p>要实施预构建的转换，请导航至 <strong>高级 KDP</strong> 下的 <strong>转换</strong> 选项卡。如果这是您的第一次转换，您将立即在页面上看到预构建的转换。如果您之前已有转换，请选择<strong><em>*创建</strong></em>*。 ![prebuilt_transform .jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716333296539)</p>
<p>当您选择预构建的转换时，您将进入转换构建器，其中已定义规则。您可以根据您的品牌需求在此处添加或编辑任何这些规则。 ![标准化状态预建转换的转换构建器](https://klaviyo.zendesk.com/hc/article_attachments/28716333286043)</p>
<p>如果您尝试将预构建的转换应用到已具有该类型转换（即 <strong>标准化</strong> 或 <strong>格式</strong>）的配置文件属性，您将看到一条错误消息，因为每种类型的属性只有一个转换。准备好应用预构建的转换后，请在转换构建器中选择<strong><em>*保存</strong></em>*。转换将被激活，并将在您的转换列表中可见。 ![保存的转换](https://klaviyo.zendesk.com/hc/article_attachments/28716356251291)</p>
<h2>管理转型</h2>
<p>在 Klaviyo 中创建数据转换后，您将看到它列在 <strong>转换</strong> 页面上，并包含以下详细信息：</p>
<ul>
<li>****配置文件属性****</li>
</ul>
<p>正在转换的原始配置文件属性的名称。 - <strong><em>*新配置文件属性名称</strong></em>*</p>
<p>转换后的配置文件属性的名称。 - <strong><em>*转化方法</strong></em>*</p>
<p>使用的变换方法。 - <strong><em>*状态</strong></em>*</p>
<p>转换的状态（即 <strong>活动</strong>、<strong>进行中</strong>、<strong>非活动</strong>）。 - <strong><em>*最后编辑</strong></em>*</p>
<p>最近的配置文件属性转换的时间戳。 ![帐户上活动转换的列表视图](https://klaviyo.zendesk.com/hc/article_attachments/28716356224667)</p>
<p>您最多可以同时激活 30 个转换。首次创建新转换时，其状态为<strong>进行中</strong>。在此状态下，转换将批量应用于现有配置文件。批量转换完成后，状态将变为 <strong>Active</strong>。任何新的配置文件或现有配置文件的更新都将实时转换。从每个转换旁边的菜单中，您可以：</p>
<ul>
<li>编辑现有的转换</li>
<li>删除转换</li>
<li>启用非活动转换</li>
</ul>
<p>要更新或重新转换属性，您可以使用 <strong>编辑</strong> 选项。 ![编辑选项以更改现有转换](https://klaviyo.zendesk.com/hc/article_attachments/28716333279643)</p>
<p>请注意，删除转换不会删除保存在 <strong>Property\_transformed</strong> 下的已转换属性，但转换将不再应用于任何新数据。如果您因试用期结束或不再使用高级 KDP 附加组件而无法访问数据转换功能：</p>
<ul>
<li>所有转换将设置为**非活动**状态。 - 转换将不再适用于新数据。 - 之前转换的数据将继续可用。如果您决定将来再次使用高级 KDP 附加组件，您可以再次手动将任何非活动转换设置为**活动**。</li>
</ul>
