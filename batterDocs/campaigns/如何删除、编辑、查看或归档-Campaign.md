---
id: 7012
title: "如何删除、编辑、查看或归档 Campaign"
slug: "deleteeditviewarchivecampaigns"
category: "活动与营销（Campaigns）"
category_slug: "campaigns"
wp_url: "https://dynamicycle.com/docs/deleteeditviewarchivecampaigns/"
wp_modified: "2026-02-25T03:37:38"
---

##### 删除 Campaign

处于草稿模式（即尚未计划发送或未发送）的 Campaign 可以被删除。已计划发送、正在发送及已发送的 Campaign 无法删除，但您可以对其进行归档。

****一旦删除，Campaign 将无法恢复。****

1. 导航至 Campaigns 选项。
2. 点击您想要删除的 Campaign 右侧的“三点”菜单。
3. 点击 Delete。

![电子邮件营销活动管理界面，显示多个活动的状态、最后更新和操作选项，如克隆、编辑和删除。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-31.png?resize=1024%2C302&ssl=1)

##### 编辑 Campaign 内容

您可以编辑任何尚未发送的 Campaign（包括已计划在未来发送的 Campaign，但前提是您必须先将其暂停）。已经发送的消息无法进行编辑。

##### 编辑草稿或已暂停的 Campaign

1. 导航至 Campaigns 选项。
2. 点击您想要编辑的草稿 Campaign，或者选择右侧的“三点”图标并点击 Edit campaign。
3. 根据需要进行更新。

##### 编辑已计划发送（Scheduled）的 Campaign

1. 导航至 Campaigns 选项。
2. 点击您想要编辑的 Campaign 最右侧的“三点”图标。
3. 点击 Pause 以暂停该 Campaign。

![电子邮件活动列表，显示不同状态的活动，包括已安排、已发送和已取消的项目，操作选项包括暂停和重新安排](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-32.png?resize=1024%2C266&ssl=1)

##### 编辑已部分发送的 Campaign

如果您发现正在发送中的 Campaign 存在错误，可以取消该 Campaign 以进行调整。

请注意，已经发送的消息无法进行编辑。在发送途中取消 Campaign 并重新发送，仅能纠正那些已进入发送队列但尚未收到邮件的 Recipients（收件人）所收到的内容。

编辑发送中的 Campaign 主要分为三个步骤：

1. 取消 Campaign。
2. 创建一个已收到该 Campaign 的 Recipients Segment。
3. 编辑并重新发送 Campaign 给尚未收到邮件的用户，并排除掉第一批已收到邮件的 Segment。

##### 取消 Campaign

1. 导航至 Campaigns 选项。
2. 点击您想要取消的 Campaign 最右侧的“三点”图标。
3. 点击 Cancel。

![电子邮件活动管理界面，展示多个活动的状态和调度信息，包括已发送、计划中的和已取消的活动。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-33.png?resize=1024%2C406&ssl=1)

##### 识别已收到 Campaign 的用户

1. 导航至 Lists & Segments 选项。
2. 点击 Create List/Segment。
3. 点击 Segment。
4. 创建一个具有以下定义的 Segment： What someone has done（用户行为） > Received Email（已收到邮件） > at least once over all time（在所有时间内至少一次） > where campaign name equals（其中 Campaign 名称等于）\_\_\_。

![在用户界面中定义条件，筛选已收到电子邮件的用户，依据特定活动名称进行操作。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-34.png?resize=1024%2C154&ssl=1)

###### 编辑并重新发送 Campaign

1. 导航至 Campaigns 选项。
2. 打开已取消的 Campaign 旁边的“三点”图标。
3. 点击 Clone > Clone to this account（克隆至此账号）。
4. 对克隆版本的 Campaign 进行所需的修改。
5. 在 Don’t send to（不要发送至）字段中，选择您在上一步创建的 Segment。

![显示收件人设置的界面，包含'发送到'和'不发送到'的选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-35.png?resize=1024%2C308&ssl=1)

###### 重新计划 Campaign 发送时间

1. 导航至 Campaigns 选项。
2. 点击您想要重新安排时间的 Campaign 名称。
3. 在接下来的页面中，点击 Reschedule。

![调度发送页面，显示发送时间为2024年8月30日，上午10:30，包含暂停编辑和重新调度选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-36.png?resize=1000%2C396&ssl=1)

4.选择新的发送时间。

5.点击 Schedule 以应用更改。

##### 重命名 Campaign

您无法重命名已经发送的 Campaign。

若要更改 Campaign 的名称：

1. 导航至 Campaigns 选项卡。
2. 点击您想要重命名的 Campaign 旁边的更多选项菜单（三点图标）。
3. 点击 Edit details。
4. 在接下来的屏幕中，在 Campaign name 字段内编辑名称。
5. 点击 Save。

##### 查看 Campaign

一旦 Campaign 发送完毕，您将无法编辑其任何内容或设置，但可以查看其中的内容。

1. 导航至 Campaigns 选项。
2. 找到您想要查看的 Campaign，点击名称右侧的“三点”图标。
3. 点击 View Campaign。

![电子邮件活动记录，包含已发送和已取消的活动情况。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-37.png?resize=1024%2C181&ssl=1)

##### 归档 Campaign

您可以归档任何已发送或已取消的 Campaign。草稿状态的 Campaign 可以被删除，但无法归档。除非您通过筛选器进行搜索，否则归档后的 Campaign 不会显示在 Campaign 列表视图中。

1. 导航至 Campaigns 选项。
2. 找到您想要归档的 Campaign，点击名称右侧的“三点”图标。
3. 点击 Move to archive（移至归档）。

![电子邮件活动列表，显示三项活动的状态，包括已发送和已取消的活动，时间戳和操作选项](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-38.png?resize=1024%2C215&ssl=1)

###### 取消归档 Campaign

您可以在 Campaigns 选项卡中通过筛选来查看所有已归档的 Campaign。若要查看或取消归档某个 Campaign：

1. 点击 Archived 筛选器。
2. 导航至屏幕右上角的 Options（选项）下拉菜单。

![广告活动管理界面，包含搜索广告活动、时间范围选择、状态筛选和已归档选项。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-39.png?resize=1024%2C119&ssl=1)

3.点击 Campaign 名称右侧的“三点”图标，并选择 Unarchive，即可取消对该 Campaign 的归档。

##### 查看已计划 Campaign 的摘要详情

若要检查已计划发送（Scheduled）的 Campaign 详情（包括发送时间、消息内容、发送列表等）：

1. 导航至 Campaigns 选项。
2. 点击任何已计划 Campaign 的名称。
3. 在接下来的页面中，查看消息详情。
4. 如有需要，您可以暂停该 Campaign 以进行编辑。

##### 复制 Campaign ID

若要复制某个 Campaign 的 ID：

1. 导航至 Campaigns 选项。
2. 在列表视图或日历视图中，点击 Campaign 旁边的更多选项按钮（三点图标）。
3. 点击 Copy campaign ID。

![营销活动列表界面，显示最近的SMS和电子邮件活动，包含状态和时间信息。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/02/image-40.png?resize=1024%2C460&ssl=1)

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)