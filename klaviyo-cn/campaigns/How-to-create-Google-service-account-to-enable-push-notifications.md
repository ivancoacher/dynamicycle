---
id: "19893982562203"
title: "如何创建 Google 服务帐户以启用推送通知"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19893982562203-How-to-create-Google-service-account-to-enable-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:18Z"
language: "zh"
---
## 你将会学到

了解如何设置您的 Google 服务帐号并启用 Firebase Cloud Messaging，以便您可以向 Android 设备发送 Klaviyo 推送通知。 ## 开始之前

在执行以下步骤之前，您必须拥有一个现有的 Firebase 项目。 ## 启用云消息API

1. 导航至 [Google Cloud 控制台](https://console.cloud.google.com/welcome)。 2. 从左上角的下拉列表中选择您的 Firebase 项目。 3. 搜索“Firebase 云消息 API”。
4. 从市场列表中选择****Firebase Cloud Messaging API****。 ![搜索 Firebase 云消息 API](https://klaviyo.zendesk.com/hc/article_attachments/28720761878939)
5. 在出现的模式中，单击****启用****。 ![启用 Firebase Cloud Messaging API 的页面](https://klaviyo.zendesk.com/hc/article_attachments/28720790367387)

## 创建支持消息创建的自定义角色

1. 在 [Google Cloud 控制台信息中心](https://console.cloud.google.com/welcome) 中，选择 **快速访问** 部分下的 ****IAM 和管理****。 ![所有快速访问链接，仅突出显示 IAM 和管理选项](https://klaviyo.zendesk.com/hc/article_attachments/28720790364315)
2. 在左侧菜单中，导航至****角色****部分。 ![左侧边栏中突出显示的角色](https://klaviyo.zendesk.com/hc/article_attachments/28720790354971)
3. 单击****+创建角色****。 ![角色页面，左上角显示创建角色](https://klaviyo.zendesk.com/hc/article_attachments/28720761885595)
4. 填写有关角色的详细信息（名称、描述等）。 ![创建角色窗口](https://klaviyo.zendesk.com/hc/article_attachments/28720761875611)
5. 单击****+添加权限****。 6. 仅添加 **cloudmessaging.messages.create** 权限。 （有关更多详细信息，请参阅 Google 关于[创建自定义角色](https://cloud.google.com/iam/docs/creating-custom-roles#creating) 的说明。）。 ![搜索正确的角色权限](https://klaviyo.zendesk.com/hc/article_attachments/28720790351643)
7. 单击****添加****。 8. 准备就绪后，通过选择****创建****来创建角色。 ## 创建一个Google服务帐户

1. 在 [IAM 和管理部分](https://console.cloud.google.com/iam-admin/iam) 的左侧菜单中，导航到 **服务帐户** 选项卡。 2. 单击****+创建服务帐户****。 ![创建Google服务帐户的按钮](https://klaviyo.zendesk.com/hc/article_attachments/28720790390043)
3. 填写 **服务帐户名称** 和 **服务帐户说明**（可选）字段。 ![创建新服务帐户向导的第一步](https://klaviyo.zendesk.com/hc/article_attachments/28720761897883)
4. 单击****创建并继续****。 5. 单击进入“**选择角色**”字段。 ![向新服务帐户添加角色](https://klaviyo.zendesk.com/hc/article_attachments/28720790375579)
6. 选择您刚刚创建的自定义角色。在这里，我们选择“测试角色”，但选择您在上一节中创建的角色。 7. 单击****完成**** 完成服务帐户的创建。 ## 生成服务帐户密钥

1. 在[服务帐户](https://console.cloud.google.com/iam-admin/serviceaccounts)页面中，单击您在上一部分中创建的服务帐户的电子邮件地址。 ![服务帐户页面，出于安全目的，帐户被模糊化](https://klaviyo.zendesk.com/hc/article_attachments/28720790388635)
2. 导航至****按键****选项卡。 3. 单击****添加密钥****。 4. 单击****创建新密钥****。 ![突出显示“创建新密钥”选项时添加密钥下拉列表](https://klaviyo.zendesk.com/hc/article_attachments/28720790379163)
5. 在**密钥类型**下，选择****JSON****。 ![选择 JSON 时选择密钥类型的模式](https://klaviyo.zendesk.com/hc/article_attachments/28720790372379)
6. 单击****创建****下载服务帐户密钥文件。注意：您无法再次下载该文件，因此请确保您可以在计算机上找到该文件。 下载的 JSON 文件应具有以下格式：
   `{“类型”：“服务帐户”，
   "project_id": "PROJECT_ID",
   "private_key_id": "KEY_ID",
   "private_key": "-----开始私钥-----\nPRIVATE_KEY\n-----结束私钥-----\n",
   "client_email": "SERVICE_ACCOUNT_EMAIL",
   "client_id": "CLIENT_ID",
   “auth_uri”：“https://accounts.google.com/o/oauth2/auth”，
   "token_uri": "https://accounts.google.com/o/oauth2/token",
   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL" }`

## 结果

现在您已创建角色并将其分配给您的 Google 服务帐户，您可以开始设置 Klaviyo Android 推送通知。