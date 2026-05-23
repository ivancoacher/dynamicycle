<h1>Troubleshooting PrestaShop authorization error PHP as CGI</h1>

## You will learn

Learn how to solve the authorization issue “It appears you are running PHP as a CGI” when configuring the Klaviyo module in PrestaShop. Solving this issue involves changing a setting in PrestaShop, then regenerating your .htaccess file. Follow the steps in this article to finish integrating with PrestaShop properly.
![](https://klaviyo.zendesk.com/hc/article_attachments/35197436760091)

## Before you begin

If you have made any manual code changes to your .htaccess file, please note that the following steps will force PrestaShop to regenerate the file and erase them.

## Steps to resolve

1. In PrestaShop, navigate to ****Advanced Parameters > Web Service****.
2. Toggle on **Enable CGI mode for PHP**, then click ****Save****.
   ![A settings page in PrestaShop showing Enable CGI mode for PHP toggled on](https://klaviyo.zendesk.com/hc/article_attachments/28713385281179)
3. To regenerate the .htaccess file, navigate to ****Shop Parameters > Traffic & SEO****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/35197407426843)
4. Click ****Save**** (you do not need to make any changes). Clicking Save here forces PrestaShop to regenerate the .htaccess file which, with the CGI toggle on, will solve the authorization issue.

Now, you can return to the module settings page and continue with the integration process.

## Additional resources

- [Getting started with PrestaShop](https://help.klaviyo.com/hc/en-us/articles/360054551492)
- [PrestaShop data reference](https://help.klaviyo.com/hc/en-us/articles/360055123191)
- [Klaviyo Community](https://community.klaviyo.com/)
