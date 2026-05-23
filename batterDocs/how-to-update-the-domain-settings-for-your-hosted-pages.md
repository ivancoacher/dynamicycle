<h1>How to update the domain settings for your hosted pages</h1>

## You will learn

Learn how to update the dedicated domain settings for your hosted pages in Klaviyo. In most cases, you'll want to do this if you have hosted pages in Klaviyo for a content management system (CMS), which is a software used to create, modify, and manage digital content (such as WordPress).

## Update the dedicated domain settings for your hosted pages

1. Click your account name in the bottom left corner.
2. Select ****Settings > Other >**** [****Consent Pages****](https://www.klaviyo.com/settings/other/consent-pages).
3. Scroll down to the **Custom Hosted Pages** section.
4. If you have [hosted pages enabled for your account](https://help.klaviyo.com/hc/en-us/articles/115005077067#h_01J5970D8J98RVN0GADKN2VJ6W), you will see the option to update your content management settings at the bottom of this page.
5. Pick a hostname (a subdomain + your domain) and add a CNAME record for it to your domain name service (DNS).
   - For example, if you own a company called The Book Exchanger, the chosen hostname here might be: **pages.bookexchanger.com**, where “pages” is an arbitrary choice as the subdomain, and “bookexchanger.com” is your business domain.
   - This hostname will serve as an alias for the yourbusiness.myklpages.com domain provided within the **Content Management Settings** section of your account. For the example of The Book Exchanger, the configuration may look like:

     ![](https://klaviyo.zendesk.com/hc/article_attachments/28717382438171)
6. Ensure that the CNAME record looks like:

   |  |  |  |
   | --- | --- | --- |
   | ****Type**** | ****Hostname**** | ****Value**** |
   | **CNAME** | **pages.bookexchanger.com** | **bookexchanger.myklpages.com** |

7. In the box under **Hosted Pages Dedicated Domain**, ensure that this value reads: ****[a subdomain].[your domain]****
   - Example: pages.bookexchanger.com
8. When you confirm that this information accurately reflects the CNAME record you have added, click ****Update Dedicated Domain Settings**** to save this information in your account.

## Additional resources

- [How to translate consent pages into different languages](https://help.klaviyo.com/hc/en-us/articles/360049498631)
- [How to custom code consent pages](https://help.klaviyo.com/hc/en-us/articles/115005077067)
