---
id: "6294531159579"
title: "如何在 Instagram 上创建点击文字贴纸"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/6294531159579-How-to-create-a-tap-to-text-sticker-on-Instagram"
section: "Use email and social media to collect SMS consent"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:04Z"
language: "zh"
---
## 你将会学到

了解如何为 Instagram 故事创建点击文本（也称为点击文本）贴纸，以便您的关注者只需点击几下即可订阅短信更新。

只有拥有付费 Klaviyo 帐户并通过帐户验证的用户才能创建点击文本贴纸。

****贴纸如何发挥作用****

单击后，贴纸将：

1. 打开个人的消息应用程序
2. 自动填充来自 Klaviyo 的消息，其中包含某种类型的订阅关键字

然后，人们需要做的就是发送此消息，他们就会选择加入您的短信营销活动。这使您可以轻松收集短信订阅者并扩大您的列表。

## 开始之前

在开始之前，请注意：

- 您需要[在您的帐户中启用托管页面](https://help.klaviyo.com/hc/en-us/articles/360057679192)
- 贴纸仅适用于 Instagram 故事，不适用于帖子

## 为短信创建点击文本贴纸

1. 在 Klaviyo 中，导航至您帐户中的****托管页面****。

   - 请注意，仅当您的帐户已[启用托管页面](https://help.klaviyo.com/hc/en-us/articles/360057679192)时，才会显示此选项卡。
2. 在 **页面** 下，单击加号 ****(+)**** 添加新页面。
3. 命名该页面（例如，clicktotext.tmpl）。
   ![命名新托管页面的模式](https://klaviyo.zendesk.com/hc/article_attachments/28717994187803)
4. 单击****添加页面****。
   1. 在页面中添加以下代码片段：

      ````
      <html lang="en">
           <正文>
              <脚本>
              var phone_number = '您的短信发送号码'
              var message = "文本加入以注册文本"
              var sms_string = 'sms://'+phone_number+'?&body='+encodeURIComponent(message);
              位置.替换(sms_string);
              </脚本>
         </正文>
      </html>
      ````
5. 检查您是否已将“您的短信发送号码”替换为您的 Klaviyo 发送号码。

   - 要查找您的 Klaviyo 发送号码，请转到****帐户 > 设置 > 短信****。！[短信发送号码已被替换的代码片段示例](https://klaviyo.zendesk.com/hc/article_attachments/28717994198811)
6. 可选：将 JOIN 替换为[自定义订阅关键字](https://help.klaviyo.com/hc/en-us/articles/360050384091)。
7. 单击****预览****。
8. 复制预览页面的 URL。
9. 单击****保存****。
10. 登录您的 Instagram 帐户。
11. 向左滑动以访问 Instagram 故事生成器。
12. 拍摄一张新照片或单击左下角的图像选择器图标以访问您的最新照片。

    - 作为最佳实践，图像大小应为 1080 x 1920 像素。
    - 图片应包含[短信披露语言](https://help.klaviyo.com/hc/en-us/articles/4412878737051)。
13. 单击顶部菜单上的****贴纸****按钮，该按钮看起来像圆角正方形中的笑脸
    ![鼓励短信注册的图像示例以及 Instagram 故事的披露语言](https://klaviyo.zendesk.com/hc/article_attachments/28717988407323)
14. 选择****链接****贴纸选项
    ![Instagram 故事的贴纸选项](https://klaviyo.zendesk.com/hc/article_attachments/28717988409371)
15. 粘贴从预览中复制的链接
16.添加完成后，点击右上角的****完成****
17. 可选：点击并拖动以重新定位贴纸
    ![带有用于短信注册的点击文本贴纸的 Instagram 故事示例](https://klaviyo.zendesk.com/hc/article_attachments/28717994196507)
18. 单击****您的故事**** 将其发布到您的故事中

## 结果

帖子发布后，任何点击该贴纸的人都可以轻松地向您发送短信并同意短信营销。这使您可以更轻松地扩大短信订阅者列表，从而直接接触更多人。