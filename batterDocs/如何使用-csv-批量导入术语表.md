<h1>如何使用 CSV 批量导入术语表</h1>

<p>您必须拥有付费 Klaviyo 帐户并启用智能翻译才能使用此功能。 # 导入现有的词汇表</p>
<p>Klaviyo 的智能翻译功能使用 <strong>词汇表</strong> 来控制特定术语的翻译方式 - 品牌名称、产品名称、口号或技术术语，需要在每个活动中进行一致的翻译。如果您已经在另一个翻译系统（DeepL、Lokalise、Phrase、内部电子表格）中维护术语表，您可以将其作为 CSV 直接导入 Klaviyo，而无需手动重新创建每个条目。 ## 何时使用 CSV 导入</p>
<p>当您想要执行以下操作时，CSV 导入非常有用：</p>
<ul>
<li>将现有词汇表从 DeepL、Lokalise、Phrase 或 memoQ 等 TMS（翻译管理系统）导入 Klaviyo。 - 一次添加一大批术语（数十或数百），而不是在用户界面中逐一输入。 - 将共享电子表格中维护的术语表迁移到 Klaviyo 中的单一事实来源。对于少数术语，在术语表面板中手动将它们逐一添加通常会更快。导入是单向的。您将术语上传到 Klaviyo，但目前没有 CSV 导出。如果需要备份，请保留源文件的副本。 ## 准备您的 CSV 文件</li>
</ul>
<h3>文件格式</h3>
<ul>
<li>****编码：**** UTF-8</li>
<li>****文件类型：**** `.csv`</li>
<li>****分隔符：**** 逗号 (`,`)</li>
<li>****标题行：**** 必需（见下文）</li>
</ul>
<h3>示例文件</h3>
<p>|来源术语 |目标术语 |源语言环境 |目标语言环境 |</p>
<p>| --- | --- | --- | --- |</p>
<p>|你好 |你好 | zh |法国 |</p>
<p>|你好 |你好| zh |德 |</p>
<p>| tschüß |再见|德 | zh |</p>
<h3>必填列</h3>
<p>每行必须包含四列：</p>
<ul>
<li>`源术语` — 源语言中的术语</li>
<li>`目标术语` — 该术语应该如何翻译</li>
<li>`source locale` — 源语言的 BCP-47 区域设置标签</li>
<li>`target locale` — 目标语言的 BCP-47 区域设置标签</li>
</ul>
<p>所有四个标头必须出现在文件的第一行中。列顺序并不重要。 ### 区域设置代码 (BCP-47)</p>
<p>区域设置代码遵循 [BCP-47](https://www.rfc-editor.org/info/bcp47) 标准。最常见的形式是两个字母的语言代码，可选地后跟一个区域：</p>
<ul>
<li>`en` — 英语</li>
<li>`en-US` — 英语（美国）</li>
<li>`en-GB` — 英语（英国）</li>
<li>`fr` — 法语</li>
<li>`fr-CA` — 法语（加拿大）</li>
<li>`de` — 德语</li>
<li>`ja` — 日语</li>
<li>`pt-BR` — 葡萄牙语（巴西）</li>
</ul>
<p>使用与您在 Klaviyo 中配置的区域设置相匹配的最具体的标记。 ### 一个文件中的多个语言对</p>
<p>单个 CSV 可以包含<strong><em>*许多语言对</strong></em>*的条目。每行都是独立处理的，因此您可以自由混合对：</p>
<p>|来源术语 |目标术语 |源语言环境 |目标语言环境 |</p>
<p>| --- | --- | --- | --- |</p>
<p>|你好 |你好 | zh |法国 |</p>
<p>|你好 |你好 | zh | es |</p>
<p>|你好 |你好| zh |德 |</p>
<p>|你好 |布宜诺斯艾利斯|法国 | es |</p>
<p>如果您维护一个支持多个语言环境翻译的主词汇表，这将非常有用。 ### 术语表术语是对称的</p>
<p>每个术语表条目都定义了术语之间的<strong><em>*双向</strong></em>*等效项。如果您导入：</p>
<p>|来源术语 |目标术语 |源语言环境 |目标语言环境 |</p>
<p>| --- | --- | --- | --- |</p>
<p>|你好 |你好 | zh |法国 |</p>
<p>克拉维约将：</p>
<ul>
<li>翻译英语 → 法语时，将“hello”翻译为“bonjour”。 - 翻译法语 → 英语时，将“bonjour”翻译为“hello”。这意味着你****不能****定义非对称映射，例如：</li>
</ul>
<p>|来源术语 |目标术语 |源语言环境 |目标语言环境 |</p>
<p>| --- | --- | --- | --- |</p>
<p>|你好 |你好 | zh |法国 |</p>
<p>|你好 |你好|法国 | zh |</p>
<p>这两行都将“bonjour”映射到不同的英语术语，这是一个冲突。每个区域设置对术语组合仅允许一个映射。导入器将跳过冲突行并报告错误（请参阅[导入错误疑难解答](#troubleshoot-import-errors)）。如果您需要根据上下文对“bonjour”进行不同的英语翻译，那么词汇表术语并不是正确的工具——它们适用于每次都以相同方式翻译的术语。 ### 导入模式</p>
<p>导入时，选择以下两种模式之一：</p>
<ul>
<li>****添加**** — 保留现有术语表条目。添加 CSV 中的新条目。与现有条目冲突的行将被跳过。 - ****全部替换**** — 您当前的整个词汇表将被删除并替换为 CSV 的内容。 ****全部替换**** 删除整个当前词汇表。仅当您确信 CSV 是新的事实来源时，才使用****全部替换****。无法撤消。 ## 导入文件</li>
</ul>
<p>1. 转到<strong><em>*帐户→设置→翻译→词汇表</strong><strong>。 2. 单击</strong><strong>导入 CSV</strong></em>*。 ![突出显示“导入 CSV”按钮的词汇表面板](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/b5276c1e1afee879a200bb1152311bcae5a99e24-1476x882.png)</p>
<p>3. 在对话框中，选择<strong><em>*添加</strong><strong> 或</strong><strong>全部替换</strong></em>*。 ![词汇表导入模式](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/c928305cb7b49c52aee43d0e6fc23cbe72098b20-1660x1322.png)</p>
<p>4. 单击文件区域并选择“.csv”文件（或将文件拖动到该区域）。 5. 单击<strong><em>*下一步</strong><strong>。 Klaviyo 验证了文件，但</strong><strong>不</strong></em>*保存任何内容。您将看到预览屏幕。 6. 查看预览：</p>
<ul>
<li>****总行数**** — 文件中有多少行。 - ****有效条目**** — 将导入多少条目。 - ****跳过的行**** — 由于验证问题而删除了多少行。 7. 如果出现任何警告，您仍然可以继续，或者先返回并修复文件。 8. 单击****导入****保存更改。 ![验证成功，确认导入。 ](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/2c855c6011a469d53e5daf8cfa4b53f78aaf9b62-1664x462.png)</li>
</ul>
<p>如果文件有问题，您将看到<strong><em>*导入失败</strong></em>*屏幕，而不是预览。 ![失败的导入示例，带有警告和错误。 ](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/82924f88e6415e2b0c24cef666409b31f8d2ec93-1642x782.png)</p>
<h2>解决导入错误</h2>
<p>当导入失败时，Klaviyo 会显示一条或多条错误消息，解释出现的问题。有些错误适用于整个文件；其他的则指向特定的行。 ### 文件级错误</p>
<p>这些完全停止导入。修复它们并重试。 <strong><em>*“上传的文件为空。”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 该文件不包含任何内容。 </strong><strong>要做什么：</strong><strong> 确保文件不是 0 字节并且至少有一行加上标题。 </strong><strong>“缺少必需的标头。”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 标题行不包含所有四个必需列。 </strong><strong>做什么：</strong><strong> 检查第一行是否包含“源术语”、“目标术语”、“源语言环境”和“目标语言环境”。标头顺序并不重要；拼写确实如此。 </strong><strong>“没有有效的术语表条目。”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 验证后，无法导入任何行。 </strong><strong>做什么：</strong><strong> 打开文件并检查数据行是否符合预期格式。 </strong><strong>“编码错误。”</strong></em>*</p>
<p><strong><em>*含义：</strong></em>* 文件不是 UTF-8 编码的</p>
<p><strong><em>*该怎么做：</strong><strong> 使用 UTF-8 编码从电子表格工具重新保存文件。在 Excel 中，使用</strong><strong>另存为 → CSV UTF-8</strong><strong>。 </strong><strong>“术语超出了最大长度。”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 一个或多个术语太长。 </strong><strong>该怎么做：</strong></em>* 术语表术语应该是短语。缩短或分割很长的条目。 ### 行级错误</p>
<p>这些标记特定行。文件的其余部分仍然可以导入 - 错误的行将被跳过。 <strong><em>*“第 N 行：意外的列数”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 该行的逗号分隔值太少或太多。 </strong><strong>该怎么做：</strong><strong> 检查 CSV 中的行 — 术语内的多余逗号需要用引号引起来（“你好，世界”）。 </strong><strong>“N行：空项值”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 源术语或目标术语单元格为空。 </strong><strong>该怎么做：</strong><strong> 填写缺少的术语，或删除该行。 </strong><strong>“N 行：空区域设置代码”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 源或目标区域设置单元格为空白。 </strong><strong>该怎么做：</strong><strong> 填写缺少的区域设置（例如“en”、“fr-CA”）。 </strong><strong>“N 行：无法识别的区域设置代码”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 区域设置字符串不是有效的 BCP-47 标记。 </strong><strong>该怎么做：</strong><strong> 使用标准区域设置代码，如“en”、“fr”、“de”、“pt-BR”。请参阅[区域设置代码](#locale-codes-bcp-47)。 </strong><strong>“N 行：检测到重复的区域设置列”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 同一区域设置在单个条目上下文中出现多次。 </strong><strong>该怎么做：</strong><strong> 每行都需要不同的源和目标语言环境 - 您无法翻译“en → en”。 </strong><strong>“N 行：同一术语和区域设置的翻译冲突”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 该行尝试将相同的源术语映射到与文件中的另一行不同的目标。 </strong><strong>该怎么做：</strong><strong> 确定哪个翻译是正确的并删除重复的翻译。 </strong><strong>“N 行：术语与现有条目冲突”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 该行尝试定义与词汇表中已有术语相矛盾的翻译（仅限</strong><strong>添加</strong><strong>模式）。 </strong><strong>要做什么：</strong><strong> 更新 UI 中的现有条目，或者如果新文件正确，则使用</strong><strong>全部替换</strong><strong>模式。 </strong><strong>“N 行：为了安全起见，删除了前导公式字符”</strong></em>*</p>
<p><strong><em>*含义：</strong><strong> 以“=”、“+”、“-”或“@”开头的术语，电子表格应用程序会将其解释为公式。 </strong><strong>该怎么做：</strong></em>* 这是警告，而不是失败。导入该术语时会删除前导字符。如果您需要该字符，请将术语用引号引起来。 ### 一般验证错误</p>
<p>如果您看到“<strong><em>*发生验证错误。请检查您的文件并重试。”</strong></em>* 导入器遇到无法分类的问题。仔细检查文件是否符合预期格式，如果错误仍然存​​在，请联系支持人员。</p>
