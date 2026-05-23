---
id: 9674090873883
title: "Troubleshoot SSO and SCIM errors"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/9674090873883-Troubleshoot-SSO-and-SCIM-errors"
section: "Security"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:55:06Z"
language: en
---

## You will learn

Learn how to troubleshoot errors for single sign-on (SSO) with Klaviyo. This article is meant for those familiar with SSO, such as IT professionals.

For more information, please see this article on [how to set up single sign-on](https://help.klaviyo.com/hc/en-us/articles/9353860331035).

## List of errors and how to fix them

We break down all the potential errors you can experience when setting up SSO. Errors tend to happen when there’s missing or incorrect information.

The table below shows all potential errors, where to go to fix them, and how to fix them.

|  |  |
| --- | --- |
| ****Error**** | ****How to fix it**** |
| Missing SSO configuration for {email} ({company\_id}) | Make sure the SSO configuration settings are saved in Klaviyo. |
| SSO disabled for {email} ({company\_id}) | Enable SSO in the SSO configuration panel in Klaviyo. |
| Missing SSO configuration for ({company\_id}) | Make sure the SSO configuration settings are saved. |
| SSO disabled for ({company\_id}) | Enable SSO in the SSO configuration panel in Klaviyo. |
| Cannot provision new SSO user for {email} in account ({company\_id}) (Just-in-Time provisioning not enabled) | If you would like to use Just-in-Time user provisioning, turn it on in the SSO configuration panel for your IdP SSO provider. |
| IdP-Initiated SSO is disabled for {email} ({company\_id}) | If you would like to use IdP-initiated SSO, you can enable it in the SSO configuration panel. |
| **Missing SSO configuration for ({company\_id})** | Make sure your SSO configuration is set up and saved. |
| This user is part of more than 1 company in Klaviyo. Their first or last name in Klaviyo is different from the value you have provided. Please contact this user and update their name in your IdP to match the value in Klaviyo | The admin should ask the user to update their name if it does not match what is in their IdP. |

### SSO configuration errors

|  |  |  |  |
| --- | --- | --- | --- |
| ****Error**** | ****How to fix it**** | |  |
| Unsupported SAML version | Go to your IdP SSO provider and update to SAML 2.0. | |  |
| Missing ID attribute on SAML Response | Check that you have the correct ID in your IdP setting and that it’s in the correct format. | |  |
| Missing role attribute | Navigate to your SSO provider and make sure to include the role attribute in the SAML assertion. Role value must be one of the following. | |  |
| [Account user roles](https://help.klaviyo.com/hc/en-us/articles/115005231648):   - owner - admin - manager - analyst - campaign\_coordinator - content\_creator - support | [Portfolio user roles](https://help.klaviyo.com/hc/en-us/articles/25181702319643):   - portfolio\_owner - portfolio\_admin - portfolio\_manager - portfolio\_analyst |  |
| SAML Response must contain 1 assertion | Navigate to your SSO provider and make sure to include the role attribute in the SAML assertion. | |  |
| Invalid SAML Response. Not match the saml-schema-protocol-2.0.xsd | Make sure your SAML response adheres schema protocol for SAML 2.0. | |  |
| The assertion of the Response is not encrypted and the SP require it | Klaviyo requires the assertion to be encrypted. Make sure you’re using an assertion that is encrypted. | |  |
| The Assertion must include a Conditions element | Ensure that the SAML response assertion for your IdP includes a conditions element. | |  |
| The Assertion must include an AuthnStatement element | Ensure that the SAML response assertion for your IdP includes an AuthnStatement element. | |  |
| There is no AttributeStatement on the Response | Ensure that the SAML response assertion for your IdP includes an AttributeStatement element. | |  |
| There is an EncryptedAttribute in the Response and this SP not support them | Klaviyo does not support when an attribute is encrypted. Check the settings for your IdP and make sure no attribute is encrypted. | |  |
| The response has an empty Destination value | Go to your IdP and fill in the destination. Note that the name for this value may not be “destination,” as it varies. If you don’t see “destination,” look for other common names for this value: “Reply URL,” “ACS URL,” “Assertion Consumer Service URL,” “Trusted URL,” and “Endpoint URL.” | |  |
| %s is not a valid audience for this Response | Make sure that the audience Id in your IdP matches exactly with the Audience URI (Service Provider Entity ID) provided in your SSO configuration panel, including the https:// prefix. | |  |
| Invalid issuer in the Assertion/Response (expected %(idpEntityId)s, got %(issuer)s) | Make sure the IdP SSO URL field in the SSO admin panel matches with the SSO URL provided by your identity provider | |  |
| The attributes have expired, based on the SessionNotOnOrAfter of the AttributeStatement of this Response | Retry logging in. If that doesn’t work, extend the expiration window for your SAML response in your IdP, as it may be too short. | |  |
| A valid SubjectConfirmation was not found on this Response | Check the settings for your IdP and look for the subject confirmation method. Make sure it’s formatted correctly. | |  |
| The Assertion of the Response is not signed and the SP require it | Either   - Go to the SSO page for workspace and uncheck the box for Assertions Signed    Or - Go to your IdP settings and turn on signing assertions of responses   Contact your IdP if you need help. | |  |
| The Message of the Response is not signed and the SP require it | Either:   - Go to the SSO page for workspace and uncheck the box for Responses Signed    Or - Go to your IdP settings and turn on signing responses   Contact your IdP if you need help. | |  |
| No Signature found. SAML Response rejected | Check that the SAML message from your IdP is properly signed. | |  |
| Signature validation failed. SAML Response rejected | Go to your workspace’s SSO page and make sure the certificate matches the certificate sent from your IdP. | |  |
| SAML Response not found, Only supported HTTP\_POST Binding | Check that your IdP is sending a HTTP\_POST request. | |  |

## Other troubleshooting tips

Open the dropdown that best matches the issue you're having for information on how to solve it.

****I can't edit a user's role in Klaviyo****

The most likely cause of this is if you're using just-in-time (JIT) provisioning. When JIT is turned on, you are not able to edit a user's role in Klaviyo.

To do so, the best option is to:

1. Temporarily turn off JIT provisioning.
2. Update the user's role in Klaviyo.
3. Turn JIT back on.

****I can't view the exemption list****

You need to have SSO set up in order to see the exemption list. For instructions, see our [article on how to enable SSO in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/9353860331035).