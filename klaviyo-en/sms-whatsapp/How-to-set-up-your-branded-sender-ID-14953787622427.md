---
id: "14953787622427"
title: "How to set up your branded sender ID"
source_url: "https://help.klaviyo.com/hc/en-us/articles/14953787622427-How-to-set-up-your-branded-sender-ID"
section: "About sending numbers"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-05-06T19:38:24Z"
language: "en"
---
For setup, you must be an Owner, Admin, or Manager.

Learn about branded sender IDs in Klaviyo, including how to set them up, where they’re available, and more.

This article only discusses branded sender IDs. For information about other number types, see our [article on all SMS sending numbers](https://help.klaviyo.com/hc/en-us/articles/6637671573403).

## Before you begin

Branded sender IDs, also called alphanumeric sender IDs, are the default sending number option in the following countries:

- \*Australia
- Austria
- Denmark
- Finland
- France
- Germany
- \*\*Ireland
- Italy
- Luxembourg
- Norway
- Poland
- Portugal
- Spain
- Sweden
- Switzerland
- UK

\* In Australia, you must register your branded sender ID before you can begin collecting SMS consent or sending messages.

\*\* Ireland requires that branded sender IDs must be registered via ComReg and the ID needs to be unique for a given SMS provider.

Branded sender IDs are not available in the United States, Canada, New Zealand, Belgium, or Hungary.

Every country uses the same branded sender ID, so you can’t have a unique ID for each region. Additionally, if you set up an ID for 1 country, that branded sender ID is activated for every other country automatically.

## What branded sender IDs can and cannot do

Unlike other sending numbers, branded sender IDs are not simply a string of numbers. Instead, they can use a mix of both letters and numbers to represent your brand.

As an example, the brand SWAK Lipcare can make their branded sender ID: SWAKLipcare

Because branded sender IDs allow for customization, you can ensure that your recipients always know who the text messages are coming from.

### Branded sender ID limitations

There are 2 key downsides with branded sender IDs; they:

1. Cannot receive text messages, meaning the following features aren’t available:

   - Tap-to-text forms and email banners.
   - Subscribe and unsubscribe keywords.
   - SMS conversations and two-way messaging.
2. Cannot send MMS.

- MMS is also not available for other sending numbers, depending on the country.

Note that you can [use Smart Opt-in](https://help.klaviyo.com/hc/en-us/articles/24743883751451) for a branded sender ID.

****Can I have both a long code and branded sender ID in a single country?****

Yes, but this is not recommended. The long code will take precedence over the branded sender ID, so registering both number types will not benefit your business.

Further, your choice of sending number should be based on your business case. See this [article comparing sending numbers](https://help.klaviyo.com/hc/en-us/articles/6637671573403) for more information.

## Set up your branded sender ID

If you did not create a branded sender ID when initially [setting up SMS](https://help.klaviyo.com/hc/en-us/articles/4404274419355), you can make one at any time.

Setting up a branded sender ID will make it active in every country where it’s available. The only exception is when there’s already a sending number for that country (i.e., if you use a long or short code, those numbers take precedence over a branded sender ID).

1. Select your account name in the lower left.
2. Navigate to ****Settings > SMS****.
3. Near the top of the **Countries** box, select ****Add country****.

   ![Add country.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28715965418139)
4. From the dropdown, choose a country where a branded sender ID is available (e.g., United Kingdom).
5. Choose ****Branded Sender ID**** (this may be the only option, depending on the country you selected).

   ![Select branded ID.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28715965414811)
6. Select ****Next****.
7. Either:

   - Customize your branded sender ID, which must contain:
     - 4 to 11 standard characters.
     - At least 1 letter (capitalized or uncapitalized).
     - No special characters or punctuation.
     - No space at the beginning or end.
     - Only 1 space between characters (no double spaces).
   - For Ireland, go to ComReg to register your branded sender ID.
8. Click ****Next****.

If you plan to use your branded sender ID in Ireland or Australia, you must register your number before you collect consent or send messages to residents in that country.

For all other countries, you can start growing your list and sending messages immediately.

## Registration for Ireland and Australia

****Ireland****

In Ireland, each branded sender ID must be unique per SMS service provider. For instance, 2 companies using Klaviyo cannot use the ID “SWAK Lipcare.”

Ireland requires that you register your branded sender ID via [ComReg’s sender ID registry](https://senderid.comreg.ie/). You'll need to:

- Add information about your business (the type of business, contact information, eircode, etc.)
- Either:
  - Input 1 of the following:
    - Irish Companies Registration Office (CRO) number
    - Trademark numbers
    - Tax registration number
  - Select the option that says “I don’t have a CRO number” and, include any additional information if possible, such as:
    - A copy of your Certificate of Incorporation/Company Registration Certificate (or the equivalent in your country)
    - Any other supporting documents
- Ensure that the OPA and Third Party sections in your ComReg account reflect Twilio as the OPA and Klaviyo as the third party:

1. Log in to your ComReg portal account and navigate to **My Sender IDs**. There, you’ll see a list of your registered Sender ID(s).
2. Ensure the Sender ID in ComReg exactly matches your Sender ID in Klaviyo.
3. In the **OPA** section, add "Twilio". Twilio is Klaviyo's upstream partner for Ireland SMS.
4. In the **Third Parties** list, add "Klaviyo".

Unlike with other countries, Klaviyo does not have visibility into the registration process and cannot assist you with the registration. If you have questions about the process, you must contact ComReg directly.

Once your Ireland branded sender ID is approved by ComReg, you will receive a confirmation email. If you have added Twilio as the OPA and Klaviyo as the third party, Klaviyo will then be notified to activate your branded sender ID. This process can take between 7-10 business days from the date of approval. If you have not added the OPA and third party fields correctly, Klaviyo will not be able to activate your sender ID even after ComReg has approved it.

****Australia****

**This information is intended solely for educational and informational purposes and should** ******not****** **be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.**

As of July 1st 2026, ****All businesses using a branded (alphanumeric) sender ID to send SMS messages to recipients in Australia must register their sender ID through Klaviyo.**** This includes customers who have previously registered their ID.

#### ****What you need to know about the 1 July 2026 deadline****

|  |  |
| --- | --- |
| ****Registration opens in Klaviyo**** | April 2026 |
| ****Registration deadline**** | 1 July 2026 |
| ****What happens after the deadline**** | Unregistered sender IDs will be blocked from sending to Australian recipients |

****Allow enough time.**** Registration takes ****7–10 business days**** to process, and re-submissions after rejection take the same amount of time. There is no way for Klaviyo to expedite this process. We strongly recommend registering as early as possible — accounts that have not submitted a complete registration by mid-June may not receive approval before the deadline.

#### ****Who needs to register****

You must register if ****both**** of the following apply:

- You send SMS or MMS to recipients with Australian phone numbers
- You use a branded (alphanumeric) sender ID (e.g., "YourBrand" rather than a numeric short code or long code)

If you're not sure whether your account uses a branded sender ID, check your SMS settings in Klaviyo.

#### ****Can I continue sending while my registration is pending?****

****Existing senders:**** If you already have an active branded sender ID in Klaviyo and are currently sending to Australian recipients, you may continue sending while your ACMA registration is in progress, up until 1 July 2026.

****New senders:**** If you have not yet started sending to Australian recipients, do not send any SMS messages — including welcome messages — until your sender ID is successfully registered.

#### ****What you'll need before you start****

##### ****Business documentation****

You must provide proof of a valid business registration. Accepted documentation includes:

- Australian Business Number (ABN)
- Australian Company Number (ACN)
- Australian Registered Body Number (ARBN) — available to non-Australian businesses
- Indigenous Corporation Number (ICN)
- Corporate registration in the country in which you are incorporated — available to non-Australian businesses

****Important:**** Your business name must match the name on your business license. If there is a discrepancy, your application is likely to be rejected. See ****What if my sender ID doesn't match my business name? below.****

#### ****Business Registration****

#### ****ABN Businesses: ASIC company extract (ABN businesses)****

In addition to your ABN or equivalent, you must provide a ****full, current company extract**** from the Australian Securities and Investments Commission (ASIC). You can retrieve this on [the ASIC registry](https://connectonline.asic.gov.au/RegistrySearch/faces/landing/bn/SearchBnRegisters.jspx).

- The extract must be complete — partial or abbreviated extracts are a common cause of rejection. Note: this is **not** found under the “View Summary (PDF)” link
- The extract must list current company officeholders

#### ****Non-ABN business documentation (non-Australian businesses)****

If your business is not registered in Australia, you are not required to provide an ASIC company extract. Instead, you must submit an equivalent official company registration document from your country of incorporation. This document must confirm your business's legal name, registration number, and current status.

Accepted non-ASIC documentation includes:

- Certificate of Incorporation — issued by your country's national or state business registry (e.g., Companies House in the UK, SEC registration in the Philippines, a Delaware Certificate of Incorporation in the US)
- Company Registration Certificate — an official document issued by the relevant government authority confirming your business is legally registered
- Articles of Incorporation or Constitution — a founding document that establishes the legal existence of your company, where this is the standard registration instrument in your jurisdiction
- Memorandum of Association — used in many Commonwealth and European jurisdictions as the primary company registration document

The document must be current, unobscured, and issued by or verifiable through an official government or statutory body. Unofficial summaries, self-generated documents, or documents from third-party aggregators are not accepted.

#### ****Identity verification****

A company officer listed in the "Officeholders and Other Roles" section of your ASIC extract (or equivalent document) must verify their identity using a government-issued ID as part of the registration process.

If a company officer is unable to complete identity verification, another company individual must complete identity verification and upload a Letter of Authorization signed by a company officer.

Make sure you identify the right person at your company before starting, as you will need their involvement to complete registration.

#### ****Sender ID ownership documentation (if your sender ID doesn't match your business name)****

If your branded sender ID does not exactly match your registered business name, you will need to provide at least one of the following:

- Proof of domain ownership
- Trademark documentation showing your right to use that name

See ****What if my sender ID doesn't match my business name?**** for your options.

#### ****How to register your sender ID****

Registration is completed directly in your Klaviyo account, available from April 2026.

1. Log in to your Klaviyo account
2. Navigate to ****Settings > SMS****
3. Select the sender ID you want to register
4. Click ****Start registration****
5. Complete the guided form — Klaviyo will pre-fill information already on your account where possible. Ensure the pre-filled information is up to date.
6. Upload required documentation (ASIC company extract, identity verification for a company officer **or** verification of another individual and a signed LOA, and ownership proof if your sender ID doesn't match your business name)
7. Submit your registration

Once submitted, your application is reviewed and submitted to the ACMA Sender ID Register. You can track your status at any time in your Klaviyo SMS settings.

#### ****Registration statuses****

After submitting, you'll see one of the following statuses in Klaviyo:

- ****Action Required:**** You have either not yet completed a registration request, or you submitted the request but Klaviyo hasn't processed it yet.
- ****Under Review:**** Your registration request was submitted and is being reviewed.
- ****Active:**** Your registration has been approved and you can continue using your branded sender ID to send in Australia.
- ****Action Required:**** Your registration was rejected, likely due to missing or incorrect information, or is in an unverified state.

The account owner will receive an email once the registration has been processed (whether approved or rejected).

#### ****What if my sender ID doesn't match my business name?****

If your sender ID and registered business name don't align, you have two options:

****Option 1 – Provide supporting documentation.**** Submit proof that you own or are authorized to use the sender ID — domain ownership records or trademark documentation.

****Option 2 – Update your sender ID.**** Change your sender ID to match your registered business name or domain. This is often the faster path to approval and avoids the need for additional ownership documentation.

Contact Klaviyo Support if you need guidance on which option is right for your account.

#### ****What if my registration is rejected?****

If your registration is rejected, review the rejection reason provided by email and correct your submission before resubmitting. The review process takes another 7–10 business days, so act promptly.

****Common reasons for rejection:****

- The business name on the license does not match the business legal name on the registration form
- Lack of evidence to prove the relationship between a parent and subsidiary company
- Lack of evidence to prove ownership of the branded sender ID
- The document provided is partially or fully obscured
- The document provided is not a valid business license or company extract
- An incomplete or partial ASIC company extract was submitted

#### ****How to fix a rejected application:****

Use this checklist before resubmitting a rejected registration. Find the rejection reason from your email or in-app notification in the first column, then complete every check in that row before resubmitting.

ACMA requires that a Sender ID is clearly linked to the entity's ****registered business name, company name, trademark, or domain name****. Full registration guidelines: [acma.gov.au/registering-sender-ids](https://www.acma.gov.au/registering-sender-ids).

****Fix every rejection reason listed in your notification before resubmitting.****

##### ****Business Registration:****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****Official business registration document is missing****  **K0012** | Businesses must have an active ABN or ACN registered with the relevant Australian authority. Status must be Active (ABR) or Registered (ASIC). | ☐ Document is a current, official government-issued registration record  ☐ Business name on document exactly matches the registration form  ☐ ABN or ACN is shown and correct  ☐ Business status is Active or Registered (not cancelled or deregistered)  ☐ Pty Ltd: fresh ASIC company extract from connectonline.asic.gov.au. Ensure that this is a **complete** extract that lists "Registered Officers"  ☐ Sole trader: ABN confirmation from abr.business.gov.au  ☐ Trust: ABN registration for the trust entity  ☐ Partnership: ABN registration for the partnership entity |
| ****Authorised Representative is not listed on the Business Registration Extract****  **K0129** | The authorised representative must be the ABR contact for the ABN — the person who manages the business's ABN. For companies: must be a listed director or officer on the ASIC extract. | ☐ Rep is listed as a current director or officer on ASIC extract (Pty Ltd)  ☐ OR is the ABN holder shown on ABR registration (sole trader)  ☐ OR is the named trustee on the trust deed (trust)  ☐ OR is a named partner in the partnership agreement (partnership)  ☐ If rep is not a listed officer: ensure an LOA signed by a listed officer is uploaded when you resubmit  ☐ Rep's name on document exactly matches name on form |
| ****Details on document do not match registration form****  **K0028** | All details on the uploaded document must exactly match the details entered on the registration form. | ☐ Business name matches form exactly — check punctuation, spacing, abbreviations (Pty Ltd vs Pty. Ltd.)  ☐ ABN/ACN on document matches form exactly  ☐ Address on document matches form exactly  ☐ Document is a fresh copy — not an old extract with outdated details  ☐ Scan is clear and all text is readable |

##### ****Business & Representative Verification****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****Contact person must be an official business representative with verification authority****  **K0058** | The authorised representative must be an official business representative verifiable against the business registration extract. | ☐ Rep is listed on the business registration extract as a director or officer  ☐ If not listed: ensure an LOA signed by a listed officer is uploaded when resubmitting  ☐ Rep's name, email, and phone number on form are correct and match exactly |
| ****Email address of Authorised Representative does not align with the business domain****  **K0057** | The rep's email must use the business's official domain — not a generic provider such as Gmail or Outlook. | ☐ Email ends with business domain (e.g. @mybusiness.com.au)  ☐ Email is not @gmail.com, @yahoo.com, @outlook.com, or similar generic domain  ☐ Email domain matches the business website domain |
| ****Email domain does not match the website domain****  **K0109** | The email domain and website domain must match. | ☐ Email domain (part after @) matches the website domain  ☐ e.g. email: name@mystore.com.au, website: mystore.com.au |
| ****Business name does not match the website SSL certificate or URL****  **K0010** | The business name must be verifiable against the website. The site must be live, secure, and display the registered business name. | ☐ Website is publicly accessible  ☐ Website URL begins with https:// (valid SSL certificate)  ☐ Business name is clearly displayed on the website  ☐ Business name on website matches the name on the registration exactly |
| ****Website is not affiliated with or representative of the business****  **K0110** | Website must be owned and operated by the registered entity. | ☐ Website is owned by the business and not a marketplace storefront (e.g. not a Shopify/Etsy/Amazon seller page)  ☐ Website displays business name, contact details, and ABN if possible |

##### ****Letter of Authority (LOA)****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****A Letter of Authority (LOA) is required****  **K0131** | An LOA is required when the person completing the registration is not a listed officer on the business registration extract. | ☐ LOA clearly identifies the business by name and ABN/ACN  ☐ States the full legal name of the person being authorised  ☐ States their authority (e.g. 'to register and manage SMS Sender IDs on behalf of [Business]')  ☐ Signed by a director or officer whose name appears on the business registration extract  ☐ Includes the date of signing  ☐ Signatory's full name and role are clearly stated |
| ****Letter of Authority (LOA) contains incomplete information****  **K0130** | LOA must be complete with all required fields present. | ☐ All required fields are present: reason, authorised person's name, business name/ABN, signatory name and role  ☐ Signatory is a listed officer on the business registration extract |
| ****Letter of Authority (LOA) is not dated****  **K0132** | LOA must include the date it was signed. | ☐ Date of signing is clearly shown on the LOA  ☐ LOA has been re-signed if date was added after original signing |
| ****Letter of Authority (LOA) is not signed****  **K0133** | LOA must be signed by an authorised officer whose name appears on the business registration extract. | ☐ Ensure that documentation listing authorised officers is uploaded when resubmitting your registration  ☐ LOA is signed by a director, officer, or business owner listed on the registration extract |

##### ****Sender ID****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****Sender ID not clearly associated with your legal business name****  **K0015** | Sender ID must clearly represent the entity via one of: registered business name (ASIC, Registered), company name (ABR, Active), registered trademark (IP Australia, Registered), or registered domain (WHOIS, entity is registrant, active). | ☐ Sender ID matches registered business name at asic.gov.au — status is Registered  ☐ OR matches company name at abr.gov.au — status is Active  ☐ OR matches trademark at search.ipaustralia.gov.au — status is Registered  ☐ OR matches domain at whois.auda.org.au — entity is registrant, site/email is active  ☐ If using a brand name: ensure that trademark cert or domain ownership cert is uploaded when resubmitting  ☐ Sender ID is not generic, misleading, or impersonating another entity |
| ****The Sender ID was rejected by ACMA****  **K0101** | Sender ID must not contain prohibited, offensive, deceptive, or restricted words as defined by ACMA. | ☐ Sender ID does not contain a restricted word — check acma.gov.au/restricted-terms-sender-ids  ☐ Sender ID is not offensive, deceptive, or misleading  ☐ Sender ID does not contain the word 'Unverified'  ☐ If required, create a new Sender ID and update in Klaviyo: Settings > Text Message > Sender Information |
| ****Sender ID is too generic and does not relate to your brand or business name****  **K0104** | Sender ID must be specific to the brand or business — generic terms are not accepted. | ☐ Sender ID is specific to this business — not a common word (e.g. not 'Store', 'Shop', 'Deals')  ☐ If borderline: ensure a trademark cert or domain ownership cert is uploaded when resubmitting to prove the link |
| ****Sender ID is missing or does not match the expected format****  **K0146** | Sender ID format rules (ACMA):  • 2–11 characters (ASCII 32–126)  • Not solely numbers  • No leading/trailing space or underscore  • Does not contain 'Unverified' | ☐ Sender ID is between 2 and 11 characters  ☐ Contains only letters, numbers, and spaces — no special characters  ☐ No leading or trailing spaces  ☐ Sender ID exactly matches Klaviyo account settings |

##### ****Use Case****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****Use case description is missing****  **K0141** | A specific, accurate description of the SMS use case must be provided. | ☐ Description is specific — not just 'marketing messages'  ☐ Includes: message type, audience, and how recipients opted in  ☐ Example: 'Promotional campaigns and transactional order notifications sent to customers who opted in via our website checkout.' |
| ****Sample message is missing or exceeds 160 characters****  **K0142** | A realistic sample message must be provided, 160 characters or fewer. | ☐ Sample message is 160 characters or fewer  ☐ Sample reflects an actual message that will be sent (not a placeholder)  ☐ Includes opt-out language where relevant (e.g. 'Reply STOP to unsubscribe') |
| ****Estimated message volume per month is missing****  **K0143** | Estimated monthly message volume must be provided. | ☐ A realistic monthly volume estimate has been entered  ☐ Field is not blank |

##### ****Business Address****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****A PO Box is not an acceptable form of address****  **K0113** | ACMA requires a full physical business address. PO Boxes are not accepted. | ☐ Address is a full physical street address  ☐ Address matches the address on the official business registration extract |
| ****Partial addresses are not accepted****  **K0114** | A complete address must be provided, partial addresses are not accepted. | ☐ Address includes: street number, street name, suburb, state, and postcode  ☐ Address matches the official business registration extract |

##### ****Government-Issued ID****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****Provided identity document is not an acceptable form of proof of identity****  **K0115** | Must be a government-issued photo ID. | ☐ ID is a government-issued photo ID (Australian passport or Australian driver's licence or is issued from a non-Australian government)  ☐ Not a Medicare card, employee ID, membership card, or any non-photo document |
| ****Provided identity document has expired****  **K0116** | ID must be current and not expired. | ☐ Check the expiry date, ID must be valid at time of submission  ☐ New, current ID obtained and uploaded |
| ****Name on government-issued ID does not match Authorised Representative details****  **K0117** | Name on the ID must exactly match the authorised representative's name as entered on the form. | ☐ Full legal name on ID exactly matches name on form — including middle names, hyphens, initials  ☐ No nicknames or shortened names used on the form  ☐ If name changed (e.g. marriage): supporting document uploaded (marriage cert, statutory declaration) |
| ****Issuing authority or country of the document does not match the information provided****  **K0118** | Issuing authority and country of ID must be consistent with information provided on the form. | ☐ Country on form matches the country of the ID document  ☐ If foreign passport: contact Klaviyo support before resubmitting |
| ****Proof of identity does not show a visible address****  **K0119** | ID must display a visible physical address. | ☐ ID shows a physical address  ☐ For Australian driver's licence: both front AND back uploaded as the address is on the back |
| ****Date of birth indicates the applicant is under 18****  **K0120** | An authorized representative must be 18 years of age or older. | ☐ Representative is 18 or older  ☐ If under 18: a different representative has been nominated |
| ****ID document quality issue****  **K0121 / K0122 / K0123 / K0124 / K0125 / K0126** | ID must meet all quality requirements:  • Government-issued photo ID  • Colour copy (not black and white)  • Both sides if double-sided  • Clear and legible  • Authentic and unaltered | ☐ ID is a government-issued photo ID (passport or driver's licence)  ☐ Upload is a colour copy  ☐ Both front AND back uploaded for double-sided IDs (e.g. Australian driver's licence)  ☐ Image is clear, in focus, and fully visible  ☐ All four corners of the document are visible  ☐ Not a photocopy or screenshot of a screen |
| ****Supporting document is not legible****  **K0127** | All supporting documents must be clear and readable. | ☐ All uploaded documents are clear and all text is readable  ☐ Re-scanned or re-photographed any document that was blurry, dark, or cropped |

#### ****Frequently asked questions****

****I don't plan to use my branded sender ID in Australia. Do I need to register?****

No. Registration only applies if you send SMS or MMS to recipients in Australia using a branded sender ID. However, if you think you may expand to Australian recipients in the future, we recommend registering proactively to avoid delays later.

****I previously registered my branded sender ID with another SMS provider. Do I need to register again through Klaviyo?****

Yes. When you switch SMS providers, Australia's ACMA has no way to confirm your identity or that you previously registered the same sender ID with a different provider. You must re-register through Klaviyo regardless of prior registrations.

****I already registered my branded sender ID through Klaviyo. Do I need to register again for the ACMA requirement?****

Yes. The ACMA registration is a new, separate requirement. Your existing Klaviyo sender ID registration does not satisfy the ACMA mandate. You must complete the new registration process described in this article.

****I'm an international business, not based in Australia. Do I still need to register?****

Yes, if you send SMS or MMS to Australian recipients using a branded sender ID, the requirement applies regardless of where your business is headquartered. International businesses may use an ARBN or corporate registration from their country of incorporation. Contact Klaviyo Support for guidance specific to your situation.

****How long does registration take?****

7–10 business days for initial review. Re-submissions after rejection take the same amount of time. Klaviyo cannot expedite this process. It’s important to register as early as possible to ensure ample time for approval.

****What happens if I miss the 1 July 2026 deadline?****

After 1 July 2026, any sends to Australian recipients using an unregistered branded sender ID will be blocked by Klaviyo. You can re-register at any time, but sending to Australian recipients will remain paused until your registration is approved.

#### ****Additional resources****

- [ACMA Sender ID Register information](https://www.acma.gov.au)
- [ASIC company extract](https://www.asic.gov.au)