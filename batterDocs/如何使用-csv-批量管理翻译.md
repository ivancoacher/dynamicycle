<h1>如何使用 CSV 批量管理翻译</h1>

<p>您必须拥有付费 Klaviyo 帐户并启用智能翻译才能使用此功能。通过导出和编辑 CSV 文件，然后将其导回以批量更新翻译或与其他人协作，在 Klaviyo 之外管理翻译。 ## 导出您的翻译的 CSV</p>
<p>请按照以下步骤导出单条消息的当前翻译：</p>
<p>1. 打开您要更新的消息（活动电子邮件、流程电子邮件、短信、WhatsApp 消息等）。 2. 单击<strong><em>*翻译</strong><strong> 打开翻译编辑器。 3. 在翻译编辑器中，打开操作菜单并单击</strong><strong>导出 CSV</strong></em>*。 ![操作菜单中突出显示“导出 CSV”选项的翻译编辑器](https://klaviyo.zendesk.com/hc/article_attachments/45177653196699)</p>
<p>4. 在导出模式中，您可以选择 <strong><em>*Smarting CSV</strong><strong> 或 </strong><strong>CSV</strong></em>*</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/45987097006619" alt="" />
<h3>导出 Smartling CSV</h3>
<p>1. 您的浏览器下载一个 CSV 文件，其中包括：</p>
<p>1. 以下默认 Smartling 指令：<strong><em>*# smartling.first\_row\_header=TRUE</strong></em>*</p>
<p><strong># smartling.paths=2</strong>**</p>
<p><strong># smartling.source\_key\_paths=1</strong>**</p>
<p><strong># smartling.translations\_in\_columns=TRUE</strong>**</p>
<p>2. <strong><em>*block\_id</strong><strong> – 此消息中每个可翻译字符串的唯一标识符。 3.</strong><strong>源语言代码</strong></em>*（例如，en）——该字符串的原始源文本。 ![Google 表中的示例翻译 CSV，显示 smartling 指令、block_id、源语言列代码，一行。](https://klaviyo.zendesk.com/hc/article_attachments/45987074722971)</p>
<p>您可以按原样使用此文件将字符串导入 Smartling。 Smartling 会自动解析 CSV、提取字符串并让您触发翻译作业。作业完成后，下载生成的 CSV 并使用 <strong><em>*import</strong></em>* 按钮将其导入回来。 ### 导出简单的 CS</p>
<p>1. 您的浏览器下载一个 CSV 文件，其中包括：</p>
<p>1. <strong><em>*block\_id</strong><strong> – 此消息中每个可翻译字符串的唯一标识符。 2. </strong><strong>source</strong><strong> – 该字符串的原始源文本。 3. </strong><strong>语言列</strong></em>* – 每种语言一列，以其语言代码命名（例如 en、fr、es-MX）。 ![Google 表格中的示例翻译 CSV，显示多行的 block_id、来源和语言列。](https://klaviyo.zendesk.com/hc/article_attachments/45177659814683)</p>
<p>您现在可以在 Excel、Google Sheets 或其他电子表格编辑器中打开此文件。 ## 更新 CSV</p>
<p>编辑 CSV 时，您只需在语言列中进行操作。请勿编辑、添加或删除 block\_id 列中的任何值。如果某行具有无效或缺失的块\_id，则该行在导入期间将被忽略，并且其翻译不会更新。 ### 你可以安全地改变什么</p>
<p>在 CSV 中：</p>
<ul>
<li>通过编辑适当的语言列来更新现有翻译。 - 通过填写语言列的空单元格来添加缺失的翻译。 - 如果您不想更新某种语言，请保持该语言的值不变。 - 添加一个或多个****新语言栏****：</li>
<li>使用有效的 BCP-47 语言代码（例如 fr-CA、de、ca）。 - 导入时，如果支持这些语言，则会将这些语言添加到此消息的翻译编辑器中。 ### 你不应该改变什么</li>
</ul>
<p>避免以下情况：</p>
<ul>
<li>****不要编辑或删除块\_id值。****</li>
<li>****不要添加行。**** 每行必须继续映射到消息中现有的可翻译字符串。 - ****不要更改 CSV 中的源值****：</li>
<li>要更改源内容，请直接在 Klaviyo 编辑器中编辑消息，然后导出新的 CSV。 - ****不要重命名所需的列****（块\_id、源和语言列）。 - ****不要更改文件格式****：</li>
<li>将文件保存为 .csv 文件。 - 以 ****UTF‐8**** 编码保存。 ### 处理空单元格</li>
</ul>
<p>如果清除 CSV 中的翻译单元格并将其留空：</p>
<ul>
<li>导入将该空字符串视为一个值。 - 该单元格的现有翻译被空值覆盖。这可以有效地删除翻译。如果您想****避免更改翻译****，请在导入之前将其现有值保留在 CSV 中或完全删除该语言列。完成编辑后，将文件另存为 UTF-8 编码的 .csv。 ## 导入 CSV 文件</li>
</ul>
<p>更新并保存 CSV 后：</p>
<p>1. 返回同一消息的翻译编辑器。 2. 单击<strong><em>*导入 CSV</strong></em>*。 3. 在导入模式中，可以：</p>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/45177653207835" alt="使用选择文件和拖放选项在翻译编辑器中导入 CSV 模式。" />
<ul>
<li>单击****选择文件****并选择您的 CSV，或者</li>
<li>将 CSV 拖放到上传区域。 4. Klaviyo 运行****验证“试运行”****并显示：</li>
<img src="https://klaviyo.zendesk.com/hc/article_attachments/45177653210779" alt="导入摘要对话框显示已更新、未更改和忽略的行数，并在“导入”按钮上方列出警告。" />
</ul>
<ul>
<li>有多少行将被更新、不变或忽略的****摘要****</li>
<li>检测到的任何****警告或错误****</li>
</ul>
<p>5. 仔细查看摘要和警告。 6. 如果一切看起来正确，请单击<strong><em>*导入</strong></em>*应用更改。在验证过程中，Klaviyo 还会检查：</p>
<ul>
<li>文件大小和行限制（例如，大于 10MB 的文件将被拒绝）。 - 必填列（例如 block\_id、源和至少一语言列）。 - 频道无法识别或不支持的语言代码。 - 空翻译值和其他潜在问题。如果验证失败，您会看到一条错误消息，并且可以选择一个新文件，而无需对翻译进行任何更改。 ## 了解导入结果</li>
</ul>
<p>验证后，导入摘要会显示如果您继续操作将会发生什么。 ### 计数摘要</p>
<p>摘要可以包括如下计数：</p>
<ul>
<li>****更新**** – 至少一个转换值将发生更改的行数。 - ****未更改**** – CSV 中存在的行，但所有值均与已存储的值匹配。 - ****忽略/跳过**** – 将不会导入的行（例如，因为此消息中不存在块\_id 或缺少所需数据）。计数是按行计算的，而不是按语言计算的。例如，如果 CSV 有两行和两个语言列：</li>
</ul>
<ul>
<li>如果一行以一种语言更新，****Updated**** 计数为 1。 - 如果一行以两种语言更新，****Updated**** 计数仍为 1。 - 如果两行以一种或所有语言更新，****Updated**** 计数为 2。 ## 最佳实践</li>
</ul>
<p>为了确保您的翻译数据准确且易于管理：</p>
<p>1. <strong><em>*从最新的导出开始。</strong><strong> 避免重复使用旧的 CSV，尤其是在更改消息中的内容或语言之后。 2. </strong><strong>保留每次导出的备份。</strong><strong> 在进行更改之前保存 CSV 的副本，以便您可以在需要时回滚。 3. </strong><strong>与译者协调。</strong><strong> 解释哪些列可以编辑（仅限语言列）以及哪些列不能更改（</strong>block\_id<strong>、</strong>source<strong>）。 4. </strong><strong>如果需要，以较小的批次进行工作。</strong><strong> 如果您的文件非常大，请考虑将工作拆分到多个消息或运行多个较小的导入。 5. </strong><strong>使用支持的语言代码。</strong><strong> 添加新语言列时，请使用 </strong>智能翻译</em>* 文章中支持的 BCP-47 代码，以避免“无法处理”的语言。 ## 解决验证警告和导入错误</p>
<p>如果您在导入验证期间看到警告或错误，请查看以下部分以了解它们的含义以及如何修复它们。 <strong><em>*“缺少必需的列。”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 一个或多个必需列（</strong>block\_id<strong> 或 </strong>source<strong>）丢失或重命名。 </strong><strong>要做什么：</strong><strong> 确保 CSV 包含 </strong>block\_id<strong> 和 </strong>source<strong> 列。如果您将数据复制到新工作表中，请确认标题行与原始导出匹配。 </strong><strong>“您有空翻译值。空字符串将被视为值。”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 您的 CSV 具有空翻译值，空字符串将被视为值。 </strong><strong>该怎么做：</strong><strong> 如果继续，这些空单元格将覆盖该键和语言的任何现有翻译。如果您想要保留这些翻译不变，请恢复以前的值或删除该语言列并重新导入文件。 </strong><strong>“<count> 个密钥在您的项目中不存在，并且不会包含在导入中。”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> CSV 中的某些 </strong>block\_id<strong> 值对于此模板来说不存在（例如，如果 </strong>block\_id<strong> 值是手动编辑的）。 </strong><strong>该怎么做：</strong><strong> 这些行将被忽略，并且这些键的翻译不会改变。要解决此问题，请从 CSV 中删除这些行或根据需要导出新文件。 </strong><strong>“您的文件包含具有冲突值的重复键。 将使用第一个值。"</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> CSV 中的两行或多行具有相同的 </strong>block\_id<strong> 值（例如，如果行被错误地重复）。 </strong><strong>要做什么：</strong><strong> 使用第一行的值，并忽略其余的重复行。要解决此问题，请从 CSV 中删除重复行或根据需要导出新文件。 </strong><strong>“多个列解析为同一种语言。仅使用最后一列，其他列将被忽略。"</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> CSV 中的两个或多个列具有相同的语言代码或解析为相同的语言（例如，如果语言列被错误地重复）。 </strong><strong>要做什么：</strong><strong> 使用最后一个重复列的值，并忽略其余的重复列。要解决此问题，请从 CSV 中删除重复的列或根据需要导出新文件。 </strong><strong>“您的文件包含此通道不支持的语言代码的列：<无效的语言代码>。这些将被忽略，但将导入有效的区域设置。"</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> CSV 中的列标题使用了不受支持或识别的语言代码。 </strong><strong>要做什么：</strong><strong> 要添加新语言，请使用 </strong>智能翻译<strong> 文档中受支持的 BCP-47 代码之一。具有不受支持的代码的列将被忽略。 </strong><strong>“您的文件中包含项目中没有的语言。以下语言将添加到您的翻译编辑器中：<检测到的语言>。"</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 您的 CSV 包含当前不属于此模板的语言列。 </strong><strong>做什么：</strong></em>*</p>
<ul>
<li>如果您想添加这些语言，请查看列表并单击****导入****将它们添加到翻译编辑器中。 - 如果您不想添加它们，请删除这些列并重新导入文件。 ****“未找到区域设置列。”****</li>
</ul>
<p><strong><em>*含义：</strong><strong> CSV 包含 </strong>block\_id<strong> 和 </strong>source<strong> 列，但未检测到其他列标题。 </strong><strong>该怎么做：</strong><strong> 添加至少一种受支持的语言列，然后重试。 </strong><strong>“找不到有效的区域设置列。”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> CSV 包含 </strong>block\_id<strong> 和 </strong>source<strong> 列，但没有有效的语言列。 </strong><strong>该怎么做：</strong></em>* 添加至少一种受支持的语言列，然后重试。如果您仅看到警告并了解其影响，则可以继续导入。如果您看到错误，则必须更正 CSV 并重新上传，然后才能继续。如果您仍然看到错误，请从翻译编辑器导出新的 CSV，进行最少的更改，然后尝试再次导入以隔离问题。如果检查这些项目后仍然看到错误，请从翻译编辑器导出一个新的 CSV，进行最少的更改，然后尝试另一次导入以找出导致问题的更改。</p>
