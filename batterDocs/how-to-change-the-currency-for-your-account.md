<h1>How to change the currency for your account</h1>

## You will learn

Learn how to change the default currency symbol in your Klaviyo account from the dollar sign ($) to another currency. This change is useful if you conduct business in a different currency, as it can help save you time and minimize the risk of using an incorrect symbol.

Note that Klaviyo does not perform any currency conversions with the data provided to it, except within the Benchmarks tab. Changing your account's currency only updates the symbol displayed throughout your account.

## About currency in Klaviyo

Revenue data in Klaviyo is treated as a number, with the currency symbol set at the account level. Changing the symbol only updates how it appears alongside the revenue values; no conversion takes place. For example, a report showing $30 will display as £30 if you change the symbol from USD to British Pounds. but the numerical value will remain the same.

The only exception is the Benchmarks tab, where Klaviyo does perform currency conversions to allow industry comparison in USD.

- If you operate a single store that deals in multiple currencies, your ecommerce or payment platform typically handles these conversions in your store's backend.
- For a multi-national business with several regional stores and domains, it's best practice to have separate Klaviyo accounts for each one to allow for more accurate reporting and unique currency settings per account.

Click to expand the sections below to see what changing the default currency symbol will and will not affect.

****What it will affect****

By default, updating the default currency symbol will change how it appears in new and existing:

- Email templates (including drafted and scheduled emails) if you use a {% currency\_format ... %} tag. [Learn more about using currency tags](https://help.klaviyo.com/hc/en-us/articles/4408802648731#h_01JAB0VBMAP0P8EPX6XR7ZQTRP).
- Currency-based metrics in reports and dashboards
- Shopify coupons (when they're created in Klaviyo)

However, you can choose not to update the currency symbol in your flow emails or drafted and scheduled campaigns.

****What it will not affect****

Changing your account's currency will not impact the symbols in:

- Any revenue amounts, as Klaviyo does not currently convert attributed revenue; only the symbol will change
- Previously sent emails
- Emails where you manually added a symbol. If you added a currency symbol directly into the template (rather than using the {% currency\_format … %} tag), it will remain unchanged.
- Coupons created in Shopify itself or any other platforms

## Change the default currency symbol in Klaviyo

1. Click your organization name in the bottom left corner of Klaviyo.
2. Select ****Settings****.
   ![An example organization name selected in the bottom corner of Klayiyo showing Settings being selected from the navigation options.](https://klaviyo.zendesk.com/hc/article_attachments/30287185046683)
3. Along the lefthand menu, select****Organization****.
   ![The Account settings page showing Organization being selected from the left-hand side menu.](https://klaviyo.zendesk.com/hc/article_attachments/30287185051675)
4. Scroll down to the section labeled **Account currency**.
5. Click into the ****Currency**** dropdown.
   ![The Account currency tile on the Organization settings page.](https://klaviyo.zendesk.com/hc/article_attachments/30287176918171)
6. Select your account’s preferred currency symbol.
7. Optional: If you do not want to update the currency symbol for your flow-based emails and emails that are scheduled or in draft mode, uncheck the box below the dropdown.
8. Click ****Save****to confirm your changes.

Once you select a new currency, the change will take effect immediately across your applicable emails and flows, analytics reporting, on the Shopify coupon creation page, and in your live Shopify coupons. See above to the "What is included" and "What is not included" section of this guide for specific questions.

****More info on email templates****

When the currency symbol is changed, it updates automatically in new campaigns or flow emails that you create. If you checked the option to update existing templates during setup, then drafted and scheduled emails will reflect the change.

However, emails that have already been sent, and emails where the currency symbol was manually placed into the template ([rather than using the {% currency\_format … %} tag](https://help.klaviyo.com/hc/en-us/articles/4408802648731#h_01JAB0VBMAP0P8EPX6XR7ZQTRP)) will not update automatically.

If you need to change the symbol in a single email template, please check out this article: [How to change the currency for a specific template](https://help.klaviyo.com/hc/en-us/articles/115001201231).

****More info on reports****

When the account currency is updated in your account, it automatically appears throughout your analytics dashboards and reports.

For example, if your account's currency symbol is updated to British Pounds (£), the symbol change will reflect on your main dashboard and wherever revenue figures are reported in Klaviyo.

If you use multiple currency symbols and need to update an individual report or dashboard to reflect a different currency, please [contact our Support Team.](https://help.klaviyo.com/hc/en-us/requests/new)

****More info on Shopify coupons****

The account currency symbol will also update on the Shopify coupon creation page. This only applies to Shopify coupons created within Klaviyo, and not coupons created in Shopify or other platforms.

When you create a new coupon in Klaviyo, you'll see your chosen currency symbol for **Fixed Amount** or **Free Shipping** coupons.

Note the **Fixed Amount** tile will always show a dollar sign, but this does not mean your currency, should it be different from US dollars, hasn't updated.

![The Discount menu on a coupon creation modal in Klaviyo showing that the Fixed Amount tile has a dollar sign, while the Value off section shows your account's currency setting, in this case a GBP symbol.](https://klaviyo.zendesk.com/hc/article_attachments/30287185058971)

## Additional resources

- [How to change the currency for a specific template](https://help.klaviyo.com/hc/en-us/articles/115001201231)
- [How to change the language for your account](https://klaviyo.zendesk.com/hc/en-us/articles/25956849989531)
- [Klaviyo's support for multiple languages](https://klaviyo.zendesk.com/hc/en-us/articles/115005239028)
- [Create a location-based segment](https://klaviyo.zendesk.com/hc/en-us/articles/115005065887)
