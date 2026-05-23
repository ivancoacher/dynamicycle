<h1>How to add a first name to an email, SMS, or push message</h1>

## You will learn

Learn how to add a variable that dynamically populates a recipient’s first name in an email, SMS, or push message. These are supported in campaigns and flows, the body of any message, and an email’s subject line.

## Add a first name variable

1. Open a message (i.e., email, SMS, or push) in Klaviyo.
2. Click the personalization icon from a text field's formatting bar.
3. Select ****First name**** from the list.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32002440882971)
4. Optional: in the **Default text** field, add text to display to recipients whose first name is not set. For example, if you have a line that says "Hey FIRST\_NAME," you can use **there** as the default text.
   - If a recipient’s first name is not set, their message will read "Hey there," instead of "Hey FIRST\_NAME,".
5. Optional: Choose an optional from the **Capitalization** menu:
   - ****As typed****
     The recipient's name will appear as it appears on their profile.
   - ****Ag**** (i.e., title case)
     The recipient's name will be converted to title case (i.e., the first letter will be capitalized and all other letters will be lowercase).
   - ****AG**** (i.e., upper case)
     The recipient's name will be converted to all upper case letters.
   - ****ag**** (i.e., lower case)
     The recipient's name will be converted to all lower case letters.
6. Click ****Insert****.
7. Note the tag that appears: `{{ first_name|title|default:'there' }}` (if you set **there**as the default text and choose ****Ag**** (i.e., title case).

When you send the message, this tag will be replaced with each recipient’s name.

## Customize your first name variable

In the example above, `|default:'there'` and `|title` are filters. Klaviyo offers a wide range of filters to customize how variables appear. Learn more about [using filters in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360058907911).

## Additional resources

- See further personalization options for messages: [Message personalization reference](https://help.klaviyo.com/hc/en-us/articles/4408802648731)
- Learn how to use the preview panel to find personalization tags: [How to use the preview panel for message personalization](https://klaviyo.zendesk.com/hc/en-us/articles/27843522951707)
- Learn how to use the email editor: [Guide to the email template editor](https://help.klaviyo.com/hc/en-us/articles/4407911841435)
- Blog post: [SMS marketing strategies for all levels [+12 Pro tips]](https://www.klaviyo.com/blog/sms-marketing-strategies)
