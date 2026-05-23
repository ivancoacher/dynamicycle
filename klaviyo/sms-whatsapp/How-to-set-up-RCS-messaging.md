---
id: 46581422667035
title: "How to set up RCS messaging"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/46581422667035-How-to-set-up-RCS-messaging"
section: "RCS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-05-11T17:31:01Z"
language: en
---

RCS allows you to send branded, rich, interactive messages to your customers using a verified sender called an RCS Agent. This guide explains what an RCS agent is, how to request and enable one in Klaviyo, and how to manage its status.

## What is an RCS agent?

An RCS agent is a verified sender used to send RCS business messages. When you send messages usign RCS, your subscribers receive messages from your brand's contact card, which includes brand name, logo, banner, and contact details.

## How to create an RCS agent in Klaviyo

#### Step 1: Choose your country

1. Go to ****Settings****
2. Select ****Text message****
3. In the RCS section:

   - Click '****Get Started****' if you are setting-up RCS for the first time.
   - Click '****Add country****' if you are adding a new agent.
4. Select the country where you want to create the agent

![](https://klaviyo.zendesk.com/hc/article_attachments/46630500128411)

****Note****. You must complete setup separately for each country.

#### Step 2: Create your RCS contact card

RCS recipients see your brand as a contact card. You will need to complete the following fields:

- ****Brand Display Name**** – The name shown to end users.
- ****Brand Logo**** – The logo that displays alongside the display name (224×224px, JPG, max 90KB).
- ****Cover Photo**** – The banner image that appears at the top of the brand info page (1440×448px, JPG, max 200KB).
- ****Brand Colour**** – The hex colour value used to theme the brand info page.
- ****Brand Description**** – A short description of the brand or service that appears on the brand info page.
  - **US only** - Carriers require a concise and specific use case, not a brand description or tag line. **E.g., "Promotional messages, abandoned cart reminders, and order updates"**
- ****Contact Details**** – Contact information that appears on the brand info page. You must include at least one form of contact (phone or email), and your brand's website:
- ****Privacy Policy**** - A URL link to the Privacy Policy that appears on the brand info page.
- ****Terms of Service**** - A URL link to the Terms of Service that appears on the brand info page.

![](https://klaviyo.zendesk.com/hc/article_attachments/47145760257819)

#### Step 3: Testing

After creating your contact card, your agent status will change to 'Test mode'. This may take a few minutes.

In Test mode, you will soon be able to:

- Add approved test numbers
- Send test RCS messages
- Review how your contact card renders before submitting for carrier approval

****Note****. Test numbers and test message sending will be available shortly but are not currently supported. Until this functionality is released, you can proceed directly to registration once your contact card details are complete and accurate.

When you are ready, continue to Step 4 to submit your agent for carrier approval.

#### Step 4: Registration

Once you have created and tested your RCS agent, you must submit it for Google and carrier approval. This step verifies your business and ensures you meet RCS messaging and compliance requirements.

In order to start the registration process:

1. Go to ****Settings****
2. Select ****Text message****
3. In the RCS section, ****select the country**** where you want to register the agent
4. Click the ****three dot menu****
5. Click '****View****'
6. Click '****Register****'

![](https://klaviyo.zendesk.com/hc/article_attachments/46715502152219)

Carrier review typically takes 4 or more weeks and registration requirements vary by country and carrier. The exact information requested may differ depending on where you are registering your agent.

Below is an example of the typical information requested during registration:

![](https://klaviyo.zendesk.com/hc/article_attachments/46632063400219)

****1/ Company contact details:****

- ****Company name**** - Your legal entity name. This must match public records and your website.
- ****Website**** - Your primary domain. It must be live and publicly accessible.
- ****Industry**** - Select the industry that best represents your business.
- ****First name and last name**** - Contact person name.
- ****Job title**** - Contact person job title.
- ****Business email address**** - Contact email address.
- ****Phone number**** - Contact number.

  ****Note****. The contact details provided here will be used by the RCS for Business support team during review.

  ****2/ Business registration details:****
- ****Country of registration**** - The country where your business is legally registered.
- ****Registered street address**** - Registered street address.
- ****City -**** Registered city.
- ****State/Province/Region**** - Registered state or region.
- ****ZIP/Postal code**** - Registered postal code.
- ****Business registration number**** - For example, EIN for US businesses or the equivalent local registration number in other countries.
- ****Legal entity type**** - For example, Private company, Public company, Sole trader etc.

  If owned by a parent company, you must also provide:
- ****Parent company name****
- ****Parent company website****

  ****3/ Proof of opt in collection:****

  You must upload a screenshot of a sign up form that shows how SMS consent is collected.
- The screenshot must clearly display your messaging consent language and any required disclosures.
- You can take the screenshot from the Klaviyo forms section.

****4/ Estimated monthly RCS sends:****

You must provide a realistic estimate of your expected monthly RCS message volume.

#### Step 5: Authorisation & Country Specific Requirements

After you submit your RCS registration, your agent status will change to '****Under review'**** and your registration information will be reviewed by Google and local carriers. In some countries, additional manual steps are required before your agent can be approved for launch.

****Google Authorisation:****

All brands must complete a Google authorisation step. The brand contact listed on the RCS registration form will receive an email from Google requesting authorisation to launch an RCS agent on your behalf.

You must review and approve this request promptly. Your agent cannot be reviewed by carriers until Google confirms brand authorisation.

****Country Specific Requirements****:

In the following countries, extra actions are required in addition to Google authorisation. Any required forms or templates will be provided to you by email.

|  |  |
| --- | --- |
| ****Country**** | ****Requirements**** |
| United States | Aegis Mobile will send a verification email to your brand contact. You must complete the steps in that email within the required timeframe. |
| United Kingdom | Your brand contact must send approval emails to major UK carriers using the template provided.  EE and BT also require third party verification via Brand Assure. Your brand contact must approve the verification email sent by Brand Assure. |
| Germany | A completed form letter must be submitted by email to the designated carrier contact. |
| France | A French carrier will contact your customer facing support email to test French language support and request approval for your RCS Agent. You must respond in French and follow their instructions exactly. |
| Austria | A completed form letter must be submitted by email to the designated carrier contact. |
| Netherlands | A completed form letter must be submitted by email to the listed carrier contacts. |

#### Step 6: Approval

If additional information is required during review, the status will change to '****Action required'**** and corrective feedback will be provided so you can update and resubmit your registration.

Carrier review typically takes 4 or more weeks.

Once approved, the agent status will change to '****Approved****'. At this stage, the agent will not begin sending messages automatically and must be manually activated in Klaviyo.

We do not automatically activate approved agents to allow you to:

- Update existing flows and scheduled campaigns
- Review segmentation and targeting
- Inform or prepare customers before switching to RCS

#### Step 7: Activation

Once your agent is Approved, you must manually activate it before it can send RCS messages.

To activate or deactivate an agent:

1. Go to ****Settings****.
2. Select ****Text message****.
3. In the RCS countries section, locate the relevant country.
4. Click the three dot menu next to the agent.
5. Select ****Activate****.

Once you activate an agent, RCS becomes the default text message channel in that country and messages will automatically be delivered via RCS to all eligible devices. SMS will only be used as a fallback for recipients whose devices do not support RCS.

For more information on using RCS after activation, see the [Getting started with RCS](https://klaviyo.zendesk.com/hc/en-us/articles/41066240307483) article.

## How to deactivate or reactivate an RCS agent in Klaviyo

You can deactivate or reactivate an RCS agent at any time from your Text message settings.

To deactivate or reactivate an agent:

1. Go to ****Settings****.
2. Select ****Text message****.
3. In the RCS countries section, locate the country you want to manage.
4. Click the three dot menu next to the agent.
5. Select '****Activate****' or '****Deactivate****' from the dropdown menu.

The agent will immediately switch status.

If you ****deactivate**** an agent, the status will update to '****Paused****' and ****all RCS sending for that country will stop immediately**** and revert back to SMS if you have an active SMS SID.

If you ****activate**** the agent, the status will update to '****Active****' and ****RCS sending will resume immediately**** for eligible recipients in that country and SMS will only be sent as the fallback.

## Agent Statuses

The full range of statuses can be found below:

- ****Draft**** - Agent setup has started but has not been created with Google.
- ****Test mode**** - Agent has been created with Google and is ready for testing.
- ****Under review**** - Agent has been submitted to carriers and is being reviewed for approval.
- ****Approved**** - Agent has been approved by all required carriers and is ready to be activated in Klaviyo.
- ****Active**** - Agent is live and can send RCS messages to eligible recipients.
- ****Paused**** - Agent has been deactivated in Klaviyo and will not send messages until reactivated.
- ****Action required**** - Agent was not approved and requires updates before it can be resubmitted.

##