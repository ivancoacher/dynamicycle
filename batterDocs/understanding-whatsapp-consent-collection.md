<h1>Understanding WhatsApp consent collection</h1>

Learn how you can collect consent to send WhatsApp messages, including what methods are available and best practices for doing so.

## Meta (WhatsApp) Opt-In Requirements

To send messages to customers on WhatsApp, businesses must comply with Meta’s WhatsApp Business Messaging Policy. Businesses are required to obtain opt-in permission before messaging people on WhatsApp.

### What qualifies as valid opt-in

Customers may be contacted on WhatsApp only if both of the following are true:

- The customer has provided their mobile phone number
- The business has received explicit opt-in permission confirming that the customer wants to receive messages or calls from that specific business

The permission needs to be valid and compliant with local laws.

### Requirements for collecting opt-in

When collecting opt-in permission, businesses must ensure that:

- It is clear that the customer is opting in to receive communications
- The business name is clearly stated so the customer knows who they are opting in to hear from
- The opt-in method complies with all applicable local laws and regulations

Businesses are responsible for maintaining records of opt-in and ensuring continued compliance with Meta’s [WhatsApp Business Messaging Policy](https://business.whatsapp.com/policy?fbclid=IwY2xjawPM6lJleHRuA2FlbQIxMABicmlkETFGWE8zTm5iUG1Mb0tCaXl2c3J0YwZhcHBfaWQQMjIyMDM5MTc4ODIwMDg5MgABHoG09ahzu-ZnkZ0n8iAO9vfZC2SKMaBKDg8YQ-hlLjaUu1nSMedgy0Vwo2nO_aem_OvOB23fZQ5hV4BWV0s7NRQ). For additional info, please see Meta's [help documentation](https://developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in).

## Types of WhatsApp messages and consent

WhatsApp classifies their messages into 4 categories.

| ****Type of message**** | ****Available in Klaviyo?**** | ****Requires explicit consent?**** |
| --- | --- | --- |
| Marketing (also called “promotional” in Klaviyo) | Yes | Yes |
| Utility (called “transactional” in Klaviyo) | Yes | Yes |
| Support | Yes | N/A |
| Authentication | No | N/A |

In most cases, you need [explicit consent](https://help.klaviyo.com/hc/en-us/articles/4404203889947) to send a WhatsApp message, meaning that someone must directly tell you that they wanted to receive certain messages from your brand.

### Best practices when collecting WhatsApp consent

A few practices are to:

- Never assume that you have someone’s consent already.
  - If someone consents to another channel (e.g., signing up for SMS) or provides their phone number, this isn’t the same as agreeing to receive WhatsApp messages.
- Include clear disclosure language wherever you collect consent for WhatsApp.
  - This includes on forms, your website, emails, etc.
- Verify the phone number before sending (i.e., use double opt-in to confirm the number is real and belongs to the person who signed up).

****Do I need to use disclosure language when collecting consent for WhatsApp?****

Disclosure (also called disclaimer) language is recommended but not required when growing your WhatsApp list.

Generally, disclosure language is a best practice when collecting any type of consent. It tells potential subscribers what they’ll be signing up for, so there’s no confusion or false expectations. However, the only channel where disclosure language is truly required is SMS.

## Ways to collect WhatsApp consent

There are several ways you can grow your WhatsApp subscriber list:

- Klaviyo form
- Keyword
- Klaviyo API
- WhatsApp subscribe link or QR code

### Build a sign-up form

By creating a sign-up form, you can ask anyone on your website to consent to WhatsApp.

If you want to add WhatsApp to a form:

1. Navigate to the ****Sign-up forms**** tab.
2. Find the form you want to update.
3. Click the ****3 vertical dots**** on the right-hand side.
4. Select ****Edit**** from the dropdown.

![Form dropdown where Edit is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/40772365929371)

#### Option 1: Add a new step

- Click ****+Step****.
- Choose ****Mobile opt-in****, then click ****Next****.
- Choose ****WhatsApp****.
- Pick the list you want to add subscribers to, then click ****Add step****.
- To also collect consent for text messages, click the ****Phone Number**** block, open the ****Channel**** dropdown, and select ****WhatsApp****.
- Finally, add a Consent dropdown field with options: Promotional, Transactional, or Both

#### Option 2: Add a new block (Phone number block)

- Select ****Add block****.
- Drag in a ****Phone Number**** block.

#### Option 3: Add a new block (Button block – tap-to-text form)

Using a ****Button block**** instead of a Phone Number block makes subscribing as easy as possible. With a single click, subscribers are taken directly into WhatsApp with a ****pre-filled opt-in message****, so all they need to do is hit ****Send**** to confirm.

- Select ****Add block****.
- Drag in a ****Button**** block.
- Set the action to ****Subscribe to WhatsApp****.
- Review the ****pre-filled message**** and select the ****subscribe keyword**** your subscribers will send to confirm consent.

Finally, select ****Publish**** to set your changes live!

### Use a keyword

You can add ****keywords**** to make it easier for people to opt in. For example, you can post the keyword along with your WhatsApp number so that anyone who sends it will be signed up to receive your WhatsApp marketing messages.

You can also add a keyword to the ****Subscribe link**** that’s configured in your WhatsApp Business Account. When someone clicks the link and sends the prefilled message with the keyword, they’ll automatically be subscribed.

You can create or edit your keywords anytime in your ****WhatsApp settings****.

### Collect via API

You can use an API call to collect consent similar to email and SMS by including WhatsApp in your API call.

```
"whatsapp": {
  "marketing": {
    "consent": "SUBSCRIBED",
    "consented_at": "2025-01-01T00:00:00+00:00"
  }
  "transactional": {
    "consent": "SUBSCRIBED",
    "consented_at": "2025-01-01T00:00:00+00:00"
  }
}
```

- Full curl request example

```
curl --location
'<https://a.klaviyo.com/api/profile-subscription-bulk-create-jobs>' \\
--header 'Authorization: Klaviyo-API-Key <private-key>' \\
--header 'accept: application/vnd.api+json' \\
--header 'content-type: application/vnd.api+json' \\
--header 'revision: 2024-10-15' \\
--data '{
    "data": {
        "type": "profile-subscription-bulk-create-job",
        "attributes": {
            "profiles": {
                "data": [
                    {
                        "type": "profile",
                        "attributes": {
                            "phone_number": "+18573905002",
                            "subscriptions": {
                                "whatsapp": {
                                    "marketing": {
                                        "consent": "SUBSCRIBED",
                                        "consented_at":
                                        "2025-01-01T00:00:00+00:00"
                                    },
                                    "transactional": {
                                        "consent": "SUBSCRIBED",
                                        "consented_at":
                                        "2025-01-01T00:00:00+00:00"
                                    }
                                }
                            }
                        }
                    }
                ]
            },
            "historical_import": true
        }
    }
}'
```

To learn about about how to [collect channel consent via API](https://developers.klaviyo.com/en/docs/collect_email_and_sms_consent_via_api).

### Create WhatsApp subscribe link or QR account

If you log in to your WhatsApp Business account, you can create a link or QR code to allow people to easily subscribe. You can add this link in an email, use the link as a button in a form, or print the QR code on business cards.

![Subscribe link in WhatsApp](https://klaviyo.zendesk.com/hc/article_attachments/40772397275035)

## Next steps

- [Import WhatsApp consent](https://help.klaviyo.com/hc/en-us/articles/40116243735579)
- [Verify your WhatsApp account](https://help.klaviyo.com/hc/en-us/articles/40116148219163)
