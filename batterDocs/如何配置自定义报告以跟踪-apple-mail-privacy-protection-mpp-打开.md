<h1>如何配置自定义报告以跟踪 Apple Mail Privacy Protection (MPP) 打开</h1>

<h2>你将会学到</h2>
<p>了解如何跟踪和分析 Klaviyo 自定义报告中人为夸大的 Apple Mail 打开情况。随着 2021 年 9 月 iOS15、macOS Monterey、iPadOS 15 和 WatchOS 8 的发布，Apple 还发布了新功能邮件隐私保护 (MPP)。 Apple Mail 用户在使用 Apple Mail 时可以选择加入 MPP。 MPP 通过预取我们的跟踪像素来改变 Klaviyo 接收电子邮件打开率数据的方式，从而导致一些 Klaviyo 分析显示潜在更高的电子邮件打开率。对于专门选择加入 MPP 的订阅者，使用 Apple Mail 应用发送到其设备的任何电子邮件的打开率都会受到影响（例如，将 Gmail 帐户连接到选择加入 MPP 的 Apple Mail 仍会受到受影响的打开率影响）。任何显示为“Apple Privacy Open”的打开电子邮件均来自使用启用 MPP 的设备的订阅者，无论他们是否打开了该电子邮件。当启用 MPP 时，我们无法区分真正的人工打开和自动打开。请注意，Apple 隐私开放属性适用于 2021 年 11 月 20 日或之后发生的开放。该日期之前的开放事件可能不会包含在您的 Apple Mail 数据中。要单独查看这些开放，您将需要构建包含 Apple 隐私开放属性之一的自定义报告。您还可以调整帐户中的[电子邮件转换设置](https://help.klaviyo.com/hc/en-us/articles/11118357030555)，以跟踪默认情况下 MPP 的打开情况。 ## 配置您的自定义报告</p>
<p>为了检测与 MPP 相关的打开情况，您需要将属性添加到单一指标、营销活动或流程绩效报告中。 1. 导航至<strong><em>*分析</strong><strong></em></strong><em>> 自定义报告<strong></em><em>。 2. 您可以选择预先构建的报告或从头开始创建您自己的报告。使用任一选项，您都可以添加 Apple opens 相关指标。请注意，</strong>Apple Privacy Opens 总数<strong>和 </strong>Unique Apple Privacy Opens</em>* 属性在产品性能或多指标报告中不可用。 ![Screen_Shot_2022-01-25_at_1.44.53_AM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705637710235)</p>
<h3>活动或流程绩效报告</h3>
<p>1. 在现有报告或新营销活动或流程绩效报告中，单击<strong><em>*标准营销活动指标</strong><strong>字段以显示下拉列表。 2. 在此处，您可以选择添加 </strong>Total Apple Privacy Opens<strong>、</strong>Unique Privacy Opens</em>* 或同时添加这两个属性。这就是这两个属性的区别：</p>
<ul>
<li>*****Apple 隐私全面开放******</li>
</ul>
<p>所有MPP设备打开的累计数量。这包括同一订户可能多次打开。 - <strong><em></strong>独特的苹果隐私开放<strong></em></strong></p>
<p>所有MPP设备开放的唯一编号。这包括在 MPP 设备上首次打开的所有邮件，但不包括订阅者此后手动打开电子邮件的情况。选择属性后，您将看到它们出现在报告生成器视图中。 3. 如果您无需对报告进行更多更改，请单击<strong><em>*保存并运行报告</strong></em>*。 ### 单一指标报告</p>
<p>1. 在现有报告或新的单一指标报告中，单击 <strong><em>*Group 或 Filter</strong><strong> 字段以显示下拉列表。请注意，</strong>Apple Privacy Open<strong> 属性仅适用于报告中的 </strong>打开的电子邮件</em>* 指标。 ![Screen_Shot_2022-01-25_at_2.28.33_AM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705637715227)</p>
<p>2. 在这里，您可以选择搜索或查找 <strong>Apple Privacy Open</strong> 的属性。添加此新属性后，请确保 Apple Privacy Open 等于处显示为 <strong>True</strong>、<strong>False</strong> 或两者。 ![Screen_Shot_2022-01-25_at_2.31.45_AM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705664535323)</p>
<p>3. 如果您无需对报告进行更多更改，请单击<strong><em>*保存并运行报告</strong></em>*。 ## 检查并导出您的数据</p>
<p>添加 Apple 开放属性后，您可以预览、计划或导出原始数据。当您预览报告时，数据将显示在报告下方，如下例所示。 ![preview_ios_data.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705637719067)</p>
<p>如果您选择[安排报告](https://help.klaviyo.com/hc/en-us/articles/4407838420123)供以后查看或将其导出为 CSV，您的 CSV 文件将包含归因于 Apple 打开的新列。 请务必注意，在导出的报告中，我们无法区分订阅者开放与 MPP 开放。任何显示为“Apple Privacy Open”的打开电子邮件均来自使用启用 MPP 的设备的订阅者，无论他们是否打开了该电子邮件。当启用 MPP 时，我们无法区分真正的人工打开和自动打开。在您的营销活动或流程绩效报告中，您将看到标有“Total Apple Privacy Opens”或“Unique Apple Privacy Opens”的适用列。这些列将包括在使用 MPP 的设备上打开的电子邮件的总数或唯一数量。 ![Screen_Shot_2022-01-25_at_3.05.50_AM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705664539291)</p>
<p>在单一指标报告中，您将在数据导出中看到标有“Apple Privacy Open”的列，如下所示。如果 <strong>Apple Privacy Open</strong> 为“True”，则表示消息已在具有 MPP 的设备上打开。 ![Screen_Shot_2022-01-25_at_2.13.48_PM.png](https://klaviyo.zendesk.com/hc/article_attachments/28705637723931)</p>
