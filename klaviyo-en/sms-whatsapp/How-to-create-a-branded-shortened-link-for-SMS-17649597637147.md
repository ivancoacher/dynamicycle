---
id: "17649597637147"
title: "How to create a branded shortened link for SMS"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17649597637147-How-to-create-a-branded-shortened-link-for-SMS"
section: "Set up SMS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: "en"
---
## You will learn

Learn how to add your brand name to shortened links in your Klaviyo SMS messages. Branding your shortened links makes them more personalized to your brand and credible, indicating to recipients that this link will take them to your website or page.

You must be on a paid SMS plan to create a branded Klaviyo or custom link.

## Before you begin

There are 2 options for branding your shortened links:

- A [branded Klaviyo link](#h_01H9N9JVZ6SPV89G6K6CKHN935), which is like a custom prefix for SMS shortened links.
- A [branded custom link](#h_01H9N9JVZ7RD0X0XNM1HNEWT6A), which is a fully customizable shortened link.

As an example, here’s what the beginning of your link may look like for a company called “James Black.”

|  |  |
| --- | --- |
| ****Link type**** | ****Example**** |
| Klaviyo link | klv3.io |
| Branded Klaviyo link | jblck.klv3.io |
| Branded custom link | sms.JamesBlack.com |

For more information about the different short link options, see [understanding the difference in SMS shortened links](https://help.klaviyo.com/hc/en-us/articles/17649677926299).

## Branded Klaviyo link

Include your organization name in the link to allow for a more streamlined experience between the SMS message and your website.

Your branded Klaviyo link must:

- Be 25 characters or less.
- Contain only letters or numbers (no special characters).
- Be unique (you cannot have the same subdomain as someone else).
- Not include any inappropriate words.

Note that when you create, edit, change, or remove any branded Klaviyo link, all previous links will continue to work as expected.

****Best practices****

There are 2 key best practices to consider when creating branded Klaviyo links.

- ****Make the link easy to understand****
  You always want your Klaviyo link to be a direct reflection of your brand. After all, there’s no point in using a branded Klaviyo link if your recipients can’t connect it back to you.
  - Good: Klaviyo, KLVYO
  - Bad: K
- ****Don’t make them too long.****
  Whatever branding you choose makes your links that much longer, meaning you’ll have fewer characters to use in your text messages.
  - Good: Klaviyo
  - Bad: KlaviyoMarketingTech

### Create a branded Klaviyo link

Create your unique branded Klaviyo link by following these steps.

1. Navigate to ****Settings > Domains****
2. Click the 3 vertical dots in the **Branded short links** box.
3. Select ****Customize****.

   - Branded Klaviyo links are only available to those on paid SMS plans. If you are not on a paid plan, you will first see prompts to upgrade.
4. On the right side under **Subdomain**, input what you want as your brand name in your shortened links (e.g., jamesblack).

   - Your subdomain must follow these requirements:
     - Be 25 characters or less.
     - Contain only letters or numbers (no special characters).
     - Be unique (you cannot have the same subdomain as someone else).
     - Not include any inappropriate words.
   - Note: You cannot edit the **Root domain** (e.g., "kvo.7.io" in the example below).![Settings interface for adding a Klaviyo branded link showing a modal with fields for root domain and subdomain](https://klaviyo.zendesk.com/hc/article_attachments/38091980603163)
5. Click ****Save****.

After you save, you’ll see the branded Klaviyo link in the SMS **Short links** page, along with the status.

### Edit a branded Klaviyo link

Before editing a branded Klaviyo link, know that once you change the prefix, it may not be available again. Editing the subdomain effectively releases it, allowing other companies the chance to use it.

To edit your branded Klaviyo link, follow these steps:

1. Navigate to ****Settings > Domains****
2. Click the 3 vertical dots in the **Branded short links** box.
3. Click ****Edit****.
   ![Edit button for a branded Klaviyo link](https://klaviyo.zendesk.com/hc/article_attachments/38092019422107)
4. Change your branding under **Subdomain**.

   - Note: you cannot change the **Root domain** of a branded Klaviyo link.
5. Click ****Save****.

### Delete a branded Klaviyo link

Deleting a branded Klaviyo link means that your shortened links no longer contain a branded prefix, removing it from shortened links in your account and allowing other companies to potentially use it.

Klaviyo allows only one branded link type at a time per account. So if you request a branded custom link and it’s approved, your branded Klaviyo link will be removed.

To remove your branded Klaviyo link, follow these steps:

1. Navigate to ****Settings > Domains****
2. Click the 3 vertical dots in the **Branded short links** box.
3. Click ****Remove subdomain****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38091980613787)
4. Select ****Remove link**** to confirm that you want to delete the branded Klaviyo link from your account.

![Modal to confirm the removal of a branded Klaviyo link](https://klaviyo.zendesk.com/hc/article_attachments/28716057116955)

## Branded custom links

Branded custom links don’t show any part of the default Klaviyo URL (e.g., klv.io). Instead, you can tailor to your organization or to your SMS program specifically. In addition, click tracking using a branded custom link is a prerequisite for using [universal links and App Links in text messages](https://klaviyo.zendesk.com/hc/en-us/articles/41701832186523-How-to-set-up-iOS-universal-links-and-Android-App-Links).

Unlike with Klaviyo branded links, branded custom links are approved and activated after DNS records propagate. This process typically completes in 10 minutes or less, but it can take up to 48 hours.

Branded custom links must:

- Be unique (you cannot have the same link as someone else).
- Clearly represent your brand.

The most important thing is that customers know that the link represents your brand. However, we recommend doing this in the least amount of character possible: the shorter your branded custom link is, the fewer characters it will use in your SMS messages.

### Request a branded custom link

Note that branded custom links are not editable. If you need to change this link, submit a support ticket for assistance.

To request a branded custom link:

1. Click your account name in the bottom left corner.
2. Go to ****Settings > Domains****.
3. Under **Branded short links**, select ****Connect a domain****.
4. In the resulting modal, choose whether to include a subdomain or not.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/38092019428763)
5. Select ****Next****.
6. Select whether you want to connect a domain with Entri, or set it up manually.
   Only domains eligible for an integration with Entri will see the automatic setup option.

![](https://klaviyo.zendesk.com/hc/article_attachments/38092019429787)

If you choose to manually set up your domain, the generated DNS records will be presented to you so you can manually add them to your DNS. With automatic configuration through Entri, the records will be added automatically on your behalf.

### ****Register a shortened version of your domain to save cost****

To save characters (and costs) in your SMS messages, you can register and take ownership of a shortened version of your domain. For example, instead of using ****sms.jamesblack.com****, you might register ****jb.co****. Shortened custom domains keep links brand-recognizable while using fewer characters, leaving you more space in each message.

To do this, you’ll need to:

- Register your chosen shortened domain with a domain registrar
- Take ownership and connect it in your Klaviyo account (via DNS setup or Entri)

Using a shorter branded domain reduces your per-message character count, helping optimize spend while maintaining trust and brand recognition.

##