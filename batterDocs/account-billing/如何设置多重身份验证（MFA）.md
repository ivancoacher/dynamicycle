---
id: 6643
title: "如何设置多重身份验证（MFA）"
slug: "multi-factorauthentication"
category: "账户与计费（Account &amp; Billing）"
category_slug: "account-billing"
wp_url: "https://dynamicycle.com/docs/multi-factorauthentication/"
wp_modified: "2026-01-28T08:05:32"
---

了解如何设置多重身份验证（MFA），以帮助提高你的 Klaviyo 账户或组合的安全性。启用 MFA 后，你需要使用用户名和密码登录，然后通过验证身份（例如输入验证码）来完成登录过程。

需要重置账户的 MFA 设置吗？请联系账户的拥有者或管理员，让他们为你重置 MFA。如果你因非 MFA 原因无法登录（或是唯一的账户拥有者），请提交请求，Klaviyo将为你提供帮助。

MFA 是一种简单的安全措施，它在你的标准用户名和密码之上增加了一个验证步骤。这一步额外的验证帮助保护账户中的敏感或机密信息，既保护你的员工，也保护你的客户。

可以将 MFA 想象为锁门。密码就像标准的门把手锁：比没有好，但对于那些有心破门而入的人来说，它并不能起到决定性的作用。

而 MFA 就像安装了一个插销：这是防止进入的又一步措施，更加安全，也更难绕过。

##### ****MFA 和两因素认证（2FA）有什么区别？****

MFA 和 2FA 非常相似。它们的主要区别在于验证用户身份所需的步骤数量。

- 2FA 只有 2 个身份验证步骤。
- MFA 至少有 2 个或更多身份验证步骤。

##### ****为什么使用 MFA？****

每天，诈骗者和黑客变得越来越狡猾，攻击更多的公司，并泄露关键的用户信息。

尽管使用 MFA 可能看起来有些繁琐，但你应该为任何在线账户启用 MFA。尤其是在存储公司或客户信息的地方（如 Klaviyo），使用 MFA 尤为重要。

MFA 是一个小步骤，但在防止以下问题上具有重要作用：

- 登录信息丢失或被盗
- 钓鱼攻击或短信钓鱼
- 其他安全漏洞

此外，如果你为账户启用 MFA，你可以在重新输入凭证之前，保持更长时间的 Klaviyo 登录状态。

##### 设置 MFA

MFA 有两种选项：

1. 使用身份验证应用（例如，Okta、Google Verify、OnePassword 等）
2. 接收短信，也称为 SMS。

请注意，SMS MFA 并非在所有国家/地区都可用。

身份验证应用更安全；然而，SMS MFA 通常更容易且更方便。尽管如此，任何形式的 MFA 都比没有 MFA 更好。

1.进入左下角的 Account 名称部分。
2.点击 Settings。

![显示帐户设置和最近帐户的侧边菜单，包含搜索框和选项，如账单和自动化。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-139.png?resize=1012%2C930&ssl=1)

3.前往 Security 标签。

![设置菜单，包括账户、账单、电子邮件、短信和安全选项](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-140.png?resize=568%2C934&ssl=1)

4.在 MFA Methods 部分，点击 Add method。

![安全设置界面，显示多因素认证（MFA）选项，包括启用和添加新方法的按钮。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-141.png?resize=1024%2C397&ssl=1)

5.选择 Set up authenticator app。

![多因素身份验证（MFA）设置界面，包括选择设置认证应用程序或短信通知选项的说明。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-142.png?resize=950%2C652&ssl=1)

6.在下一页，输入你的 Klaviyo 账户密码。

![密码确认界面，输入账户密码以验证身份](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-143.png?resize=726%2C602&ssl=1)

7.在 Klaviyo 中，你将看到一个设置页面，里面有说明和二维码（如下所示）。

![设置身份验证器的指南，包含下载应用程序和设置步骤。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-144.png?resize=979%2C1024&ssl=1)

8.下载或打开你的身份验证应用。
9.在应用中扫描或输入 Klaviyo 中显示的二维码。
请注意，具体的操作步骤因应用不同而有所差异。如需进一步帮助，请联系你的身份验证应用。
10.确认你的身份验证应用正在生成身份验证代码（也称为一次性密码、PIN 码、授权码、验证码等）。
11.准备好后，在 Klaviyo 中点击 Continue（继续）。
12.输入你应用中的身份验证代码。

![输入您的身份验证代码，填写6位数字并选择“继续”。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-145.png?resize=1024%2C419&ssl=1)

13.点击 Continue。
14.如果设置正确，你将进入下一页。
如果设置不正确，你将看到“你输入的验证码不正确”的提示。
首先，检查一下身份验证应用中的代码是否已过期。如果过期了，复制新代码并再试一次。
如果你输入的代码仍然有效，或者重试代码无效，
删除身份验证应用中的当前代码/授权。
返回第 4 步，扫描或输入新的二维码。
15.在下一页，你将看到 4 个随机备份代码；点击 Copy codes（复制代码）或 Download (.txt)（下载 .txt 文件）。

![界面提示用户保存备份代码以防止无法访问账户。包含备份代码示例以及下载和复制按钮。](https://i0.wp.com/dynamicycle.com/wp-content/uploads/2026/01/image-146.png?resize=1024%2C653&ssl=1)

16.将备份代码保存在一个安全的地方（例如加密的密码管理器或保险库）；请注意：

- 这些代码在你关闭弹窗后将不再显示。
- 每个代码只能使用一次。
- 你不能生成超过这 4 个代码。
- 如果代码用完，你需要重置 MFA 并下载一组新的备份代码。

17.点击 Finish。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)