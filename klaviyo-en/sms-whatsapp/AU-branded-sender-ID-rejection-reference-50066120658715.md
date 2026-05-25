---
id: "50066120658715"
title: "AU branded sender ID rejection reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/50066120658715-AU-branded-sender-ID-rejection-reference"
section: "Getting started with SMS"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-05-07T20:32:48Z"
language: "en"
---
Use this checklist before resubmitting a rejected Australia branded sender ID registration.

## ****How to fix a rejected application:****

Find the rejection reason from your email or in-app notification in the first column, then complete every check in that row before resubmitting.

ACMA requires that a Sender ID is clearly linked to the entity's ****registered business name, company name, trademark, or domain name****. Full registration guidelines: [acma.gov.au/registering-sender-ids](https://www.acma.gov.au/registering-sender-ids).

****Fix every rejection reason listed in your notification before resubmitting.****

### ****Business Registration:****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****Official business registration document is missing****    **K0012** | Businesses must have an active ABN or ACN registered with the relevant Australian authority. Status must be Active (ABR) or Registered (ASIC). | ☐ Document is a current, official government-issued registration record    ☐ Business name on document exactly matches the registration form    ☐ ABN or ACN is shown and correct    ☐ Business status is Active or Registered (not cancelled or deregistered)    ☐ Pty Ltd: fresh ASIC company extract from [connectonline.asic.gov.au](http://connectonline.asic.gov.au). Ensure that this is a **complete** extract that lists "Registered Officers". An example of the correct, complete extract can be [seen here](https://download.asic.gov.au/media/ldmneiyw/current-company-extract-paid-feb-2026.pdf).    ☐ Sole trader: ABN confirmation from abr.business.gov.au    ☐ Trust: ABN registration for the trust entity    ☐ Partnership: ABN registration for the partnership entity |
| ****Authorised Representative is not listed on the Business Registration Extract****    **K0129** | The authorised representative must be the ABR contact for the ABN — the person who manages the business's ABN. For companies: must be a listed director or officer on the ASIC extract. | ☐ Rep is listed as a current director or officer on ASIC extract (Pty Ltd)    ☐ OR is the ABN holder shown on ABR registration (sole trader)    ☐ OR is the named trustee on the trust deed (trust)    ☐ OR is a named partner in the partnership agreement (partnership)    ☐ If rep is not a listed officer: ensure an LOA signed by a listed officer is uploaded when you resubmit. The LOA must be [this template](https://docs.google.com/document/d/1CGC76PLzmMl3Qo9AfgZGmU5BsG_ykUXE/edit).    ☐ Rep's name on document exactly matches name on form |
| ****Details on document do not match registration form****    **K0028** | All details on the uploaded document must exactly match the details entered on the registration form. | ☐ Business name matches form exactly — check punctuation, spacing, abbreviations (Pty Ltd vs Pty. Ltd.)    ☐ ABN/ACN on document matches form exactly    ☐ Address on document matches form exactly    ☐ Document is a fresh copy — not an old extract with outdated details    ☐ Scan is clear and all text is readable |

### ****Business & Representative Verification****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****Contact person must be an official business representative with verification authority****  **K0058** | The authorised representative must be an official business representative verifiable against the business registration extract. | ☐ Rep is listed on the business registration extract as a director or officer  ☐ If not listed: ensure an LOA signed by a listed officer is uploaded when resubmitting  ☐ Rep's name, email, and phone number on form are correct and match exactly |
| ****Email address of Authorised Representative does not align with the business domain****  **K0057** | The rep's email must use the business's official domain — not a generic provider such as Gmail or Outlook. | ☐ Email ends with business domain (e.g. @mybusiness.com.au)  ☐ Email is not @gmail.com, @yahoo.com, @outlook.com, or similar generic domain  ☐ Email domain matches the business website domain |
| ****Email domain does not match the website domain****  **K0109** | The email domain and website domain must match. | ☐ Email domain (part after @) matches the website domain  ☐ e.g. email: name@mystore.com.au, website: mystore.com.au |
| ****Business name does not match the website SSL certificate or URL****  **K0010** | The business name must be verifiable against the website. The site must be live, secure, and display the registered business name. | ☐ Website is publicly accessible  ☐ Website URL begins with https:// (valid SSL certificate)  ☐ Business name is clearly displayed on the website  ☐ Business name on website matches the name on the registration exactly |
| ****Website is not affiliated with or representative of the business****  **K0110** | Website must be owned and operated by the registered entity. | ☐ Website is owned by the business and not a marketplace storefront (e.g. not a Shopify/Etsy/Amazon seller page)  ☐ Website displays business name, contact details, and ABN if possible |

### ****Letter of Authority (LOA)****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****A Letter of Authority (LOA) is required****  **K0131** | An LOA is required when the person completing the registration is not a listed officer on the business registration extract. | ☐ Correct LOA template is being used. You must use [this template.](https://docs.google.com/document/d/1CGC76PLzmMl3Qo9AfgZGmU5BsG_ykUXE/edit)  ☐ LOA clearly identifies the business by name and ABN/ACN  ☐ States the full legal name of the person being authorised  ☐ States their authority (e.g. 'to register and manage SMS Sender IDs on behalf of [Business]')  ☐ Signed by a director or officer whose name appears on the business registration extract  ☐ Includes the date of signing  ☐ Signatory's full name and role are clearly stated |
| ****Letter of Authority (LOA) contains incomplete information****  **K0130** | LOA must be complete with all required fields present. | ☐ All required fields are present: reason, authorised person's name, business name/ABN, signatory name and role  ☐ Signatory is a listed officer on the business registration extract |
| ****Letter of Authority (LOA) is not dated****  **K0132** | LOA must include the date it was signed. | ☐ Date of signing is clearly shown on the LOA  ☐ LOA has been re-signed if date was added after original signing |
| ****Letter of Authority (LOA) is not signed****  **K0133** | LOA must be signed by an authorised officer whose name appears on the business registration extract. | ☐ Ensure that documentation listing authorised officers is uploaded when resubmitting your registration  ☐ LOA is signed by a director, officer, or business owner listed on the registration extract |

### ****Sender ID****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****Sender ID not clearly associated with your legal business name****  **K0015** | Sender ID must clearly represent the entity via one of: registered business name (ASIC, Registered), company name (ABR, Active), registered trademark (IP Australia, Registered), or registered domain (WHOIS, entity is registrant, active). | ☐ Sender ID matches registered business name at asic.gov.au — status is Registered  ☐ OR matches company name at abr.gov.au — status is Active  ☐ OR matches trademark at search.ipaustralia.gov.au — status is Registered  ☐ OR matches domain at whois.auda.org.au — entity is registrant, site/email is active  ☐ If using a brand name: ensure that trademark cert or domain ownership cert is uploaded when resubmitting  ☐ Sender ID is not generic, misleading, or impersonating another entity |
| ****The Sender ID was rejected by ACMA****  **K0101** | Sender ID must not contain prohibited, offensive, deceptive, or restricted words as defined by ACMA. | ☐ Sender ID does not contain a restricted word — check acma.gov.au/restricted-terms-sender-ids  ☐ Sender ID is not offensive, deceptive, or misleading  ☐ Sender ID does not contain the word 'Unverified'  ☐ If required, create a new Sender ID and update in Klaviyo: Settings > Text Message > Sender Information |
| ****Sender ID is too generic and does not relate to your brand or business name****  **K0104** | Sender ID must be specific to the brand or business — generic terms are not accepted. | ☐ Sender ID is specific to this business — not a common word (e.g. not 'Store', 'Shop', 'Deals')  ☐ If borderline: ensure a trademark cert or domain ownership cert is uploaded when resubmitting to prove the link |
| ****Sender ID is missing or does not match the expected format****  **K0146** | Sender ID format rules (ACMA):  • 2–11 characters (ASCII 32–126)  • Not solely numbers  • No leading/trailing space or underscore  • Does not contain 'Unverified' | ☐ Sender ID is between 2 and 11 characters  ☐ Contains only letters, numbers, and spaces — no special characters  ☐ No leading or trailing spaces  ☐ Sender ID exactly matches Klaviyo account settings |

### ****Use Case****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****Use case description is missing****  **K0141** | A specific, accurate description of the SMS use case must be provided. | ☐ Description is specific — not just 'marketing messages'  ☐ Includes: message type, audience, and how recipients opted in  ☐ Example: 'Promotional campaigns and transactional order notifications sent to customers who opted in via our website checkout.' |
| ****Sample message is missing or exceeds 160 characters****  **K0142** | A realistic sample message must be provided, 160 characters or fewer. | ☐ Sample message is 160 characters or fewer  ☐ Sample reflects an actual message that will be sent (not a placeholder)  ☐ Includes opt-out language where relevant (e.g. 'Reply STOP to unsubscribe') |
| ****Estimated message volume per month is missing****  **K0143** | Estimated monthly message volume must be provided. | ☐ A realistic monthly volume estimate has been entered  ☐ Field is not blank |

### ****Business Address****

| Rejection reason | ACMA requirement | Check before resubmitting |
| --- | --- | --- |
| ****A PO Box is not an acceptable form of address****  **K0113** | ACMA requires a full physical business address. PO Boxes are not accepted. | ☐ Address is a full physical street address  ☐ Address matches the address on the official business registration extract |
| ****Partial addresses are not accepted****  **K0114** | A complete address must be provided, partial addresses are not accepted. | ☐ Address includes: street number, street name, suburb, state, and postcode  ☐ Address matches the official business registration extract |

### ****Government-Issued ID****

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