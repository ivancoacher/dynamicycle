<h1>How to manage your account&#039;s API keys</h1>

Only Owners or Admins can access the API keys tab.

Find out how to access and manage your API keys for your Klaviyo account.

If you want to learn about creating or cloning a private API key, read [how to create private API keys](https://help.klaviyo.com/hc/en-us/articles/7423954176283).

## Difference between public and private API keys

Your public API key is also called your **Site ID**. This is a short alphanumeric value. This public key is a unique identifier for your Klaviyo account, and there is only one per account. It is safe to expose your public API key, as this key cannot be used to access data in your Klaviyo account.

Private API keys are used for reading data from Klaviyo and manipulating some sensitive objects, such as lists. Treat private API keys like passwords: kept in a safe place and never exposed to the public. A Klaviyo account can generate as many private API keys as needed.

### What to do if your API key is exposed

Since public API keys are generally an identifier, there's no risk if a public API key is exposed.

The same is not true for private API keys. Private API keys can give someone access or permissions that they shouldn't have, such as allowing them to view or edit customer data.

If a private API key is exposed, you should immediately [create a new private API key](https://help.klaviyo.com/hc/en-us/articles/7423954176283) and deactivate the old one. In addition, consider what permissions that private API key should have and use a different private API key for each application.

## Find your API keys

You will not be able view any private API key after creating it. Instead, you should treat private API keys like a password: only sharing these keys with parties you trust and saving them in a secure place, such as a vault or password manager.

1. Click your account name in the lower left.
2. Click ****Settings****.
   ![settings.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28705662510747)
3. Select the ****API keys****tab.
4. View your public API key (i.e., s**ite ID**).
   - You can see the names of your private API keys but will not be able to view the key itself.
     ![API key tab in account settings](https://klaviyo.zendesk.com/hc/article_attachments/28705662509467)

### Cloning private API keys

While you can [clone existing private API keys](https://help.klaviyo.com/hc/en-us/articles/7423954176283), the cloned key will:

- Be an entirely different key from the original.
- Use the same name as the original.
- Have the same scopes as the original.

## Additional resources

- [How to create private API keys](https://help.klaviyo.com/hc/en-us/articles/7423954176283)
- [Klaviyo's API reference guide](https://developers.klaviyo.com/en/reference/api_overview)
- [Understand how information is exchanged between Klaviyo and apps](https://klaviyo.zendesk.com/hc/en-us/articles/360030265051)
