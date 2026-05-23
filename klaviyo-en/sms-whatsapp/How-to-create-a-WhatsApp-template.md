---
id: 40116644987675
title: "How to create a WhatsApp template"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40116644987675-How-to-create-a-WhatsApp-template"
section: "Send and use WhatsApp with Klaviyo"
category: "WhatsApp"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-20T16:50:33Z"
language: en
---

Learn how to create a WhatsApp template through Klaviyo. Once you have created a template and it has been approved by Meta, you can begin to send it through campaigns and flows.

![](https://fast.wistia.com/embed/medias/h7q0ucgzdv/swatch)

## Before you begin

In order to create message templates for WhatsApp, you must first [activate the channel](https://help.klaviyo.com/hc/en-us/articles/40111819732635) in your Klaviyo account.

## Create a WhatsApp template

To get started with creating a WhatsApp template in Klaviyo:

1. Navigate to ****Content**** > ****Templates****.
2. On the **Templates** page, navigate to ****WhatsApp: saved****.
3. Select the ****Create template**** button.

![Page to create your first WhatsApp template in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/40770373812251)

In the **Create template** panel, set the following information for your template:

- ****Channel**** Select the channel for your template (i.e., **WhatsApp**).
- ****Name**** Set an easily identifiable name for your WhatsApp template. You can only use lowercase letters, numbers, and underscores for your WhatsApp template name.
- ****Language**** Select the language of your WhatsApp template.
- ****Message intent**** Select the message intent of your WhatsApp template (i.e., **Marketing** or **Transactional**).

## Components of a WhatsApp template

There are a few key components that make up your WhatsApp template when designing it in the editor.

### Header

The header is an optional field for WhatsApp templates that stores content at the top of the WhatsApp message. The header can either be text or an image.

Image headers can include static images, dynamic images using tags or URLs, and carousels. Supported file types are .jpg, .jpeg, and .png with a maximum file size of 5 MB.

![Image header example](https://klaviyo.zendesk.com/hc/article_attachments/40770373818523)

Text headers can be up to 60 characters and allow for the use of [personalization variables](https://help.klaviyo.com/hc/en-us/articles/4408802648731). Note the tag itself counts towards the character limit.

It is strongly recommended including a default value to prevent messages from being skipped.

![Text header example](https://klaviyo.zendesk.com/hc/article_attachments/40770373821979)

### Body

The body is a required section for WhatsApp templates that acts as the main content. The message body has a limit of 1024 characters.

![WhatsApp message where the body is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/40770359791131)

### Footer

The footer is an optional field for WhatsApp templates that stores content that appears below the body. Consider including any supplemental information or opt-out instructions. Note that the footer only supports text and can be up to 60 characters.

It is strongly recommended to include opt-out instructions in your WhatsApp message’s footer.

![The footer in a WhatsApp message](https://klaviyo.zendesk.com/hc/article_attachments/40770373835547)

### Buttons

Buttons are an optional field for WhatsApp templates that appear at the bottom of the WhatsApp message. You can select from the following types of actions for buttons:

- ****Quick replies**** Allow the recipient to send a preset response. You can have up to 10 quick replies on each template. Follow-up messages can also be created in [Automations](https://help.klaviyo.com/hc/en-us/articles/40116727375771), enabling you to continue the conversation automatically after a quick reply is selected.
- ****Visit website**** Send recipients to the website URL you set. You can have up to 2 buttons of this type and URLs have a 2000 character limit.
- ****Call phone number**** Send the recipient to their phone app with a prepopulated phone number.
- ****Copy code**** Automatically copy a coupon code to the recipient’s clipboard. Both [static and unique coupons codes](https://help.klaviyo.com/hc/en-us/articles/115005084727) can be added.
  - ****Note:**** Meta only supports alphanumeric characters (A–Z, 0–9) in coupon codes used with the “Copy Code” button, so special characters such as dashes, spaces, or symbols are not allowed.

    Additionally, buttons have the following requirements:
- Labels cannot be more than 25 characters.
- The URL must be valid and cannot exceed 2000 characters.

![Example of using buttons in a WhatsApp message](https://klaviyo.zendesk.com/hc/article_attachments/40770359795867)

## Previewing your WhatsApp template

To get a sense of what your WhatsApp template will look like when it is received by customers, you can use Klaviyo’s preview functionality.

To preview a WhatsApp template, select the ****Preview & test**** button in the editor.

![Preview and test button in the WhatsApp message](https://klaviyo.zendesk.com/hc/article_attachments/40770373840283)

You’ll see an example of what your template will look like for a recipient. Additionally, if you have any dynamic content, you can select a specific profile to preview the message as. This will populate the dynamic content with the appropriate information for the profile you are previewing as.

## Template approval

You can see the approval status of your templates by navigating to ****Content**** > ****Templates**** > ****WhatsApp: saved****. You can also view your templates’ quality scores, message intent, and language here.

WhatsApp only allows you to start conversations with customers using templates that have been approved by Meta in advance. Typically the approval process takes a few minutes, but may take up to 24 hours.

Once a template has been approved, you can begin sending it to customers. If a template is rejected, you’ll need to make edits and resubmit it for approval.

Follow these [guidelines](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) to increase your template’s chances of being approved:

- Avoid vague or irrelevant messages, and personalize messages for specific recipients using placeholders.
- Make sure your messages are timely, and respect quiet hours.
- Avoid sending multiple messages to a single profile in a day.
- Use templates to initiate conversations and encourage end users to respond with quick replies.
- Avoid open-ended welcome or introductory messages.
- Clearly specify the purpose of each message, preferably within 5 lines.
- Keep messages concise and informative.
- Avoid abusive or threatening language.
- Select the appropriate message type and language.
- Replace the word "survey" with "feedback."
- Upload samples for media files, placeholders, and call-to-action buttons when registering templates.
- Include opt-out instructions.
- Avoid duplicate templates. If a template is submitted with the same wording in the body and footer of an existing template, the duplicate template will be rejected.
- Make sure the message template does not contain content that violates the [WhatsApp’s Business Policy](https://business.whatsapp.com/policy).
- Do not request sensitive identifiers from users.
  - Do not ask people to share full-length payment card numbers, financial account numbers, and other sensitive identifiers. This also includes documents that might contain sensitive identifiers.
  - Requesting partial identifiers (e.g., the last 4 digits of their social security number) may be permitted.
- ****Other formatting guidelines for templates****
  - Be careful when using variable parameters:
    - Do not start or end with a variable parameter.
    - Avoid too many variable parameters relative to the message length.
    - Avoid adjacent variable parameters (e.g., {{ person.first\_name }} {{ person.last\_name}}).
    - Avoid variable parameters that are missing or have mismatched curly braces.
    - Do not include special characters (such as a #, $, or %) in a variable parameter.
    - Do not start newline characters (e.g., /n) with variable parameters.
  - Avoid emojis or newline characters in the footer.
  - Refrain from using emojis, asterisks, formatting markup, or **\n** in the header.
  - Avoid grammatical or spelling errors.
  - Only share URLs that include your brand name and avoid URLs with random characters.

### Quality ratings

Individual templates also have quality ratings assigned by Meta.

The [quality ratings for your templates](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) are:

- High Quality
- Medium Quality
- Low Quality

  When your template gets approved, it will initially have a rating of **Quality pending**.

  You also see the following statuses related to your template approval status:
- Pending
- Rejected
- Paused
- Disabled
- Appeal Requested

You should reach out to Meta support if you have questions regarding a template’s approval.