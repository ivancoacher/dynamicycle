---
id: "1260804673530"
title: "Source value reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/1260804673530-Source-value-reference"
section: "Getting started with profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:26Z"
language: "en"
---
## You will learn

Learn about the source ($source) profile property to better understand how your subscribers signed up. Klaviyo automatically assigns a $source property for profiles added using certain methods. For example, a profile’s $source is set to **API** if they were added through [Klaviyo’s API](https://developers.klaviyo.com/en/reference/subscribe_profiles), or set to **Manually Initiated** if you added them manually.

Certain integrations and subscribe methods are tracked using a number, rather than a text description. The chart below outlines what these numbers mean.

## Using special $source values

When creating a segment or flow filter based on $source, you may need to use these numbers to identify the sources you’d like to include.

To check if you’ll need to use a number versus a text value, start creating a segment with this definition: ****Properties about someone > $source > equals****. Click into the ****Dimension value**** field to see a list of options. If you see numbers like the ones below (and don’t see the relevant text value), you’ll need to use the special number value in your segment definition.

![Dropdown menu of source values in segment builder](https://klaviyo.zendesk.com/hc/article_attachments/33780714599195)

To check a specific profile’s source, navigate to their their profile. Locate the **$source** property and try to edit the value. If a number is shown in the edit field, then that number must be used in any $source-based segments you’d like to include them in.

![Information section for a profile, showing the source](https://klaviyo.zendesk.com/hc/article_attachments/28705664314395)

Note that the value set for $source on a profile is overwritten when profiles takes actions that set this field. For example, submitting a form would update the existing $source value on the profile to reflect the form submission.

Values are set when a profile subscribes or unsubscribes through the associated method.

## $source value reference

|  |  |
| --- | --- |
| ****$source Value**** | ****Profile Source**** |
| -1 | Unknown (subscribe) |
| -2 | Modal (subscribe) |
| -3 | Flyout (subscribe) |
| -4 | Embedded Form (subscribe) |
| -5 | Subscribe Page (subscribe) |
| -6 | Manually Initiated (subscribe) |
| -7 | Twitter (subscribe) |
| -8 | Integration (subscribe) |
| -9 | API (subscribe) |
| -10 | Copied from Another List (subscribe) |
| -11 | Swapped Subscription (subscribe) |
| -12 | Unknown (unsubscribe) |
| -13 | Manually Initiated (unsubscribe) |
| -14 | Unsubscribe Page (unsubscribe) |
| -15 | Unknown Integration (unsubscribe) |
| -16 | Swapped Subscription (unsubscribe) |
| -17 | API (unsubscribe) |
| -18 | Copied from Another List (unsubscribe) |
| -19 | Spam Complaint (unsubscribe) |
| -20 | Hard Bounce (unsubscribe) |
| -21 | 3dcart (subscribe) |
| -22 | BigCommerce (subscribe) |
| -23 | Postmark (subscribe) |
| -24 | Celery (subscribe) |
| -25 | Constant Contact (subscribe) |
| -26 | Zoho (subscribe) |
| -27 | API (subscribe) |
| -28 | ActBlue (subscribe) |
| -29 | Help Scout (subscribe) |
| -30 | Zendesk (subscribe) |
| -31 | Olark (subscribe) |
| -32 | ShopDirect (subscribe) |
| -33 | Mailgun (subscribe) |
| -34 | MadMimi (subscribe) |
| -35 | Lightspeed (subscribe) |
| -36 | Unbounce (subscribe) |
| -37 | Janrain (subscribe) |
| -38 | WooCommerce (subscribe) |
| -39 | Magento (subscribe) |
| -40 | Mandrill (subscribe) |
| -41 | Wufoo (subscribe) |
| -42 | Sendgrid (subscribe) |
| -43 | Mailchimp (subscribe) |
| -44 | Commercev3 (subscribe) |
| -45 | Amazon Web Services (subscribe) |
| -46 | AfterShip (subscribe) |
| -47 | Klaviyo (subscribe) |
| -48 | Salesforce (subscribe) |
| -49 | NeonCRM (subscribe) |
| -50 | Shopify (subscribe) |
| -51 | Volusion (subscribe) |
| -52 | UserVoice (subscribe) |
| -53 | Eventbrite (subscribe) |
| -54 | Kickoff Labs (subscribe) |
| -55 | Amazon Marketplace (subscribe) |
| -56 | Magento 2. (subscribe) |
| -57 | Bloomerang Fundraising (subscribe) |
| -58 | StickyStreet (subscribe) |
| -59 | Segment (subscribe) |
| -60 | Chargebee (subscribe) |
| -61 | Recurly (subscribe) |
| -62 | Stripe (subscribe) |
| -63 | Campaign Monitor (subscribe) |
| -64 | Magento (subscribe) |
| -65 | GoFundMe Pro (subscribe) |
| -66 | Spree (subscribe) |
| -67 | Desk.com (subscribe) |
| -68 | Facebook Audiences (subscribe) |
| -69 | DonorPerfect (subscribe) |
| -70 | Donate.ly (subscribe) |
| -71 | ExactTarget (subscribe) |
| -72 | OpenCart (subscribe) |
| -73 | Funraise (subscribe) |
| -74 | 3dcart (unsubscribe) |
| -75 | BigCommerce (unsubscribe) |
| -76 | Postmark (unsubscribe) |
| -77 | Celery (unsubscribe) |
| -78 | Constant Contact (unsubscribe) |
| -79 | Zoho (unsubscribe) |
| -80 | API (unsubscribe) |
| -81 | ActBlue (unsubscribe) |
| -82 | Help Scout (unsubscribe) |
| -83 | Zendesk (unsubscribe) |
| -84 | Olark (unsubscribe) |
| -85 | ShopDirect (unsubscribe) |
| -86 | Mailgun (unsubscribe) |
| -87 | MadMimi (unsubscribe) |
| -88 | Lightspeed (unsubscribe) |
| -89 | Unbounce (unsubscribe) |
| -90 | Janrain (unsubscribe) |
| -91 | WooCommerce (unsubscribe) |
| -92 | Magento (unsubscribe) |
| -93 | Mandrill (unsubscribe) |
| -94 | Wufoo (unsubscribe) |
| -95 | Sendgrid (unsubscribe) |
| -96 | Mailchimp (unsubscribe) |
| -97 | Commercev3 (unsubscribe) |
| -98 | Amazon Web Services (unsubscribe) |
| -99 | AfterShip (unsubscribe) |
| -100 | Klaviyo (unsubscribe) |
| -101 | Salesforce (unsubscribe) |
| -102 | NeonCRM (unsubscribe) |
| -103 | Shopify (unsubscribe) |
| -104 | Volusion (unsubscribe) |
| -105 | UserVoice (unsubscribe) |
| -106 | Eventbrite (unsubscribe) |
| -107 | Kickoff Labs (unsubscribe) |
| -108 | Amazon Marketplace (unsubscribe) |
| -109 | Magento 2 (unsubscribe) |
| -110 | Bloomerang Fundraising (unsubscribe) |
| -111 | StickyStreet (unsubscribe) |
| -112 | Segment (unsubscribe) |
| -113 | Chargebee (unsubscribe) |
| -114 | Recurly (unsubscribe) |
| -115 | Stripe (unsubscribe) |
| -116 | Campaign Monitor (unsubscribe) |
| -117 | Magento (unsubscribe) |
| -118 | GoFundMe Pro (unsubscribe) |
| -119 | Spree (unsubscribe) |
| -120 | Desk.com (unsubscribe) |
| -121 | Facebook Audiences (unsubscribe) |
| -122 | DonorPerfect (unsubscribe) |
| -123 | Donate.ly (unsubscribe) |
| -124 | ExactTarget (unsubscribe) |
| -125 | OpenCart (unsubscribe) |
| -126 | Funraise (unsubscribe) |
| -127 | Facebook Lead Ad (subscribe) |
| -128 | Typeform (subscribe) |
| -129 | Suppressed by Flow (unsubscribe) |
| -130 | Back in Stock (subscribe) |
| -131 | Back in Stock (unsubscribe) |
| -132 | mi9 (subscribe) |
| -133 | mi9 (unsubscribe) |
| -134 | Invalid Email (unsubscribe) |
| -135 | Merged Profiles (unsubscribe) |
| -136 | Transferred Memberships (subscribe) |
| -137 | Transferred Memberships (unsubscribe) |
| -138 | NetSuite (subscribe) |
| -139 | Wix (subscribe) |
| -140 | Square (subscribe) |
| -141 | SFTP (subscribe) |
| -142 | Square (unsubscribe) |

## Additional resources

- [How to analyze revenue by source](https://help.klaviyo.com/hc/en-us/articles/115000713811)
- [How to segment for form results](https://help.klaviyo.com/hc/en-us/articles/360040841811)
- [Message personalization reference](https://help.klaviyo.com/hc/en-us/articles/4408802648731)