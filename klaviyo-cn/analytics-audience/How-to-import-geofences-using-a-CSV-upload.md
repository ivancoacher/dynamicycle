---
id: "49977781377563"
title: "如何使用 CSV 上传导入地理围栏"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/49977781377563-How-to-import-geofences-using-a-CSV-upload"
section: "Geofences"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-05-05T20:35:45Z"
language: "zh"
---
## 你将会学到

了解如何通过上传 CSV 文件将多个地理围栏位置导入 Klaviyo。 ## 目录

要使用 CSV 上传导入地理围栏：

1. [创建 CSV 文件](https://docs.google.com/document/d/19AiD4EFBohtGGgMzmpLFNwwnY8CIIM2vp1azP2EfBww/edit#create-your-csv-file)。 2. [上传 CSV 文件](https://docs.google.com/document/d/19AiD4EFBohtGGgMzmpLFNwwnY8CIIM2vp1azP2EfBww/edit#upload-your-csv-file)。 3. [查看您的导入历史记录](https://docs.google.com/document/d/19AiD4EFBohtGGgMzmpLFNwwnY8CIIM2vp1azP2EfBww/edit#review-your-import-history)。 ## 创建 CSV 文件

上传之前，您需要一个格式正确的 CSV 文件。文件中的每一行代表一个地理围栏位置。每个位置都需要以下列：

- ****姓名****
- ****地址**** 或 ****纬度**** 和 ****经度****

  您还可以包含以下任意可选列：
- ****半径**** — 地理围栏区域的大小（以米为单位）
- ****描述****
- **状态**** — **活动**或**不活动**；是否启用地理围栏触发事件
- **输入**** — **真**或**假**；当个人资料进入地理围栏时是否触发事件
- **退出**** — **真**或**假**；当配置文件退出地理围栏时是否触发事件

![包含名称、地址和半径列的表。第 1 行：我的第一家商店，123 Main St, Anytown, NY 12345, 500。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/61bee3e4148007b66b5aca09ac89d374163c32ce-848x100.png)

您可以直接从导入流程下载预先格式化的模板。导航至****观众**** > ****地理围栏**** > ****导入位置**** 并选择****创建您自己的模板****。在出现的模式中，选择要包含的列，然后选择****下载****。在任何电子表格工具（例如 Excel 或 Google Sheets）中打开下载的文件，然后填写您的位置数据。然后将文件另存为 .csv、.text/csv 或 .applications/csv。 ![用于下载 CSV 模板的对话框，提供名称和纬度/经度等列选择，并带有“下载”按钮。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/751fbf43bfa0ed6d9569eb5352ba7107a7f8c350-1448x880.png)

## 上传您的 CSV 文件

文件准备好后：

1. 导航至****观众**** > ****地理围栏****。 2. 选择****导入位置****。 3. 在****上传位置以创建地理围栏****屏幕上，将文件拖放到上传区域，或单击****选择文件****进行浏览。 4. 文件更新后，选择****下一步****。 5. 将 CSV 列映射到 Klaviyo 中的地理围栏字段。 ![数据导入映射屏幕显示 CSV 列“名称”、“地址”、“半径”映射到具有示例数据的相应字段。选择导入 3/3 项。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/7d632d3b57d8d8717c092692002a2404c5e9c4d7-866x332.png)
6. 当所有映射看起来都正确时，选择****下一步****。 7. 为 CSV 中未包含的任何地理围栏属性或给定行中的空白选择默认值。 1. 屏幕右侧的地图为您提供地理围栏半径的直观预览。您可以在地图上方的搜索栏中输入示例地址，以了解地理围栏在真实位置中的大致大小。 ![标题为“应用默认值”的地理围栏设置面板，其中包含“输入事件：True”、“退出事件：False”、“状态：活动”和“半径：500 米”已选择。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/68943d9928260257f3eccdaa2f0b6d59248be1de-982x1296.png)
8. 设置默认值后，选择****导入****。 ## 查看您的导入历史记录

开始导入后，您可以在****导入历史记录****中跟踪其状态。每个条目显示导入的日期和时间、导入的位置数量以及结果：

- ****完成**** — 所有位置均已成功导入
- ****部分完成**** — 一些位置已导入，但其他位置失败；选择 ****下载失败的行**** 以获取未导入行的 CSV，您可以更正并重新上传
- ****失败**** — 未导入任何位置

![“过去 7 天内的导入”仪表板，显示一项完整导入（1/1 位置）和一项部分完成（1/4 位置）导入条目。](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/c3e56fa5ce70ca6ddb7d97a57738f7b1e22e1a08-1224x584.png)

导入可能需要几秒钟到几分钟的时间，具体取决于文件的大小。 您可以离开该页面，导入将在后台继续。 ## 最佳实践

- 保持地点名称的描述性和一致性。 Klaviyo 使用 ****Name**** 字段作为主要标识符，因此清晰的名称可以让您以后更轻松地管理地理围栏。 - 当您需要精确放置时，例如建筑物的特定入口或大型综合体中的某个位置，请使用****纬度/经度****列，而不是****地址****。 - 在导入大批量之前，从两个或三个位置的小测试文件开始。此方法可让您在提交完整上传之前确认列映射和默认值是否正确。 - 在任何部分导入后查看失败的行报告。常见问题包括格式错误的地址、****Status**** 或 ****Enter/Exit**** 列中不支持的值或缺少必填字段。 ## 结果

成功导入后，您的位置将显示在 Klaviyo 的****位置****部分中，并包含您配置的状态和设置。您可以在流和段中使用这些地理围栏来根据您的个人资料位置触发消息。