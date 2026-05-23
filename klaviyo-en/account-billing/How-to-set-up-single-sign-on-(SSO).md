---
id: 9353860331035
title: "How to set up single sign-on (SSO)"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/9353860331035-How-to-set-up-single-sign-on-SSO"
section: "Security"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:56:59Z"
language: en
---

## You will learn

Learn how to set up single sign-on (SSO) for your Klaviyo account or portfolio. Currently, only identity provided (IdP) single sign-on is supported in Klaviyo.

****Why use SSO?****

Single sign-on (SSO) helps protect you, as well as your customers, by making your account more secure. If you have SSO set up for your business, you can require your Klaviyo users to log in using their SSO credentials.

Plus, if you use SSO for your organization, you and your users can remain logged in to Klaviyo for a longer period of time before re-entering your credentials.

## Before you begin

We strongly suggest reaching out to your company’s IT department to help you set this up because there are certain steps you will need to take within your company’s identity provider. If needed, you can temporarily [make them an admin in your account](https://help.klaviyo.com/hc/en-us/articles/360053547071) to set up SSO.

Please note:

- You must have a paid plan to use SSO.
- You must be an Owner or Admin to set up this feature.
- Klaviyo does not support service provider (SP) SSO, only IdP SSO.

If you use identity provided (IdP) single sign-on (SSO), you can use this to log in to Klaviyo. Security assertion markup language 2.0 (SAML 2.0) SSO gives members access to Klaviyo through an IdP of your choice.

Examples of IdP SSO providers include Okta, OneLogin, Microsoft Entra ID, and more.

If you enforce SSO for all users, any new user will need to accept the invitation and then log in using SSO.

****View and use the exemption list****

Users added to the exemption list will be able to bypass SSO and log in with a username and password when SSO is enforced for a company. This is important if there is an IdP outage or when you do not want to add a partner, contractor, or agency member to your IdP instance.

Note that you will only be able to view the exemption list once SSO is set up.

****What is a workplace ID?****

Also called the SSO login identifier, the workplace ID is required to set up SAML SSO in Klaviyo. It is usually the same name as your company. You'll create this ID as part of step 3 of the Klaviyo setup process (discussed in this section below).

After setting up a workplace ID, users can go directly to your company's custom URL (e.g., www.klaviyo.com/sso/workplace/<id>) to log in to Klaviyo. We recommend telling users to bookmark this URL to speed up the login process.

- The ID cannot be longer than 63 characters.
- The ID must be URL safe, so it can contain only upper- or lowercase letters, hyphens (-), periods (.), underscores (\_), and tildes (~).
- The ID should be simple and easy for users to remember (such as your company name).
  - For example, Klaviyo’s workplace ID is “Klaviyo.”

### About just-in-time (JIT) provisioning

After you set up SSO, you will have the option to enable just-in-time (JIT) provisioning in Klaviyo. When a user is added to an account with JIT provisioning, the user will need to accept the invite in their email to start accessing the account.

Note that once SSO is enabled and JIT provisioning is turned on, you can only update the [user's Klaviyo role](https://help.klaviyo.com/hc/en-us/articles/115005231648) inside of the IdP and will no longer be able to update any roles inside of Klaviyo. To update a role, you will need to do so inside your IdP or by temporarily turning off both JIT and [SCIM](https://help.klaviyo.com/hc/en-us/articles/10952782535579) to update inside of Klaviyo.

****What is JIT?****

When JIT provisioning is enabled, IT admins no longer need to create accounts manually for each user in each of their applications. Instead, user accounts are created the first time users try to log in to an application, as long as the user has permission for that app.

For instance, IT admins can automatically grant Klaviyo access to all users in their IdP so that those users' accounts will automatically be created the first time they log in to Klaviyo via their SSO portal or through Klaviyo-initiated login.

## Set up SAML SSO

1. In Klaviyo, click your organization name in the bottom left corner.
2. Click ****Settings****.
3. Select ****Security****.
4. Click ****Set up SSO****. (Note that multi-factor authentication is not required.)
   ![Security tab in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28716331657371)
5. Copy the **Klaviyo SSO URL** and **Audience URI (Service Provider Entity ID)** for use in the next section.

![Top of the SSO configuration page, where you copy the Klaviyo SSO URL and audience URI](https://klaviyo.zendesk.com/hc/article_attachments/28716354655515)

## Log in to your SSO provider

Open the dropdowns below for IdP-specific instructions. In general, you will need to:

1. Open a new tab and log in to your SSO provider.
2. Find the confirmation settings for your provider.
3. Paste in the Klaviyo SSO URL and save.
4. Download or locate your IdP’s metadata.
5. Assign users and their roles to the Klaviyo app.

- To have your role passing correctly to Klaviyo, we recommend using the key format. (Some IdPs convert attributes to lowercase in their protocol, so the label format is not recommended)

|  |  |
| --- | --- |
| ****Account user roles**** | ****Portfolio user roles**** |
| owner | portfolio\_owner |
| admin | portfolio\_admin |
| manager | portfolio\_manager |
| analyst | portfolio\_analyst |
| campaign\_coordinator |  |
| content\_creator |  |
| support |  |

The roles depend on the type of account where you're setting up SSO. In a normal account, only [account user roles](https://help.klaviyo.com/hc/en-us/articles/115005231648) are applicable. In a portfolio account, only [portfolio user roles](https://help.klaviyo.com/hc/en-us/articles/25181702319643) are applicable

****Okta****

1. Log in to your Okta admin account.
2. Navigate to ****Application > Applications****.
3. Select ****Create App Integration****.
   ![Applications page in Okta, where you can create app integration](https://klaviyo.zendesk.com/hc/article_attachments/28716331667611)
4. In the modal, select the option for ****SAML 2.0****.
   ![Sign-in options when SAML 2.0 is selected](https://klaviyo.zendesk.com/hc/article_attachments/28716354670747)
5. Click ****Next****.
6. Name the integration (e.g., “Klaviyo”).
   ![Step 1 of the Okta integration wizard, where you can name the app](https://klaviyo.zendesk.com/hc/article_attachments/28716331685403)
7. Click ****Next****.
8. In the **Single sign-on URL** field, paste in the **Klaviyo SSO URL** from the Klaviyo SSO setup screen.
9. In the **Audience URI (SP Entity ID)** field, paste the **Audience URI (Service Provider Entity ID)** from Klaviyo.
10. Set the **Name ID** format field to ****EmailAddress****.
11. Change the **Application username** to ****Email****.
12. Check that the **Update application username on** is set to ****Create and update****.
    ![SAML configuration settings to for the Klaviyo integration](https://klaviyo.zendesk.com/hc/article_attachments/28716354798619)
13. Click ****Next****.
14. Select ****I’m an Okta**** ****customer adding an internal app****.

    - You do not need to check or fill out any other information on this page.
15. Scroll to the bottom of the page and click ****Finish****.
16. Go to the ****Sign On**** tab.
    ![Sign On tab for an app in Okta](https://klaviyo.zendesk.com/hc/article_attachments/28716354685211)
17. Scroll down to the **SAML Signing Certificates** section.
18. Find an active certificate and then click the ****Actions**** dropdown.
19. Click ****View IdP metadata****.
    ![Actions dropdown when View IdP metadata is selected](https://klaviyo.zendesk.com/hc/article_attachments/28716354687515)
20. A new tab will open that should look like the one below.
    ![Example of the XML metadata page](https://klaviyo.zendesk.com/hc/article_attachments/28716331703067)
21. In the new tab, right click and select ****Save as > Save**** so that you can upload this file to Klaviyo later.
22. Navigate back to Okta.
23. Go to the ****Assignments**** tab.
24. Click ****Assign****.
25. Choose whether to assign the app to an individual (i.e., people) or to a group.
    ![Options to assign users to an app by people or groups](https://klaviyo.zendesk.com/hc/article_attachments/28716354673435)
26. Find the people or groups you want to assign Klaviyo to, and click ****Assign**** next to their name(s).
    ![Example of assigning a user by the People option](https://klaviyo.zendesk.com/hc/article_attachments/28716331705371)
27. If you’re selecting individuals:

    - Choose the username for each individual; the default is their username in Okta.
    - Click ****Save and go back****.![Modal to assign a username to an individual](https://klaviyo.zendesk.com/hc/article_attachments/28716331709211)
28. When you are finished, click ****Done****.

****One Login****

1. Log in to your One Login account.
2. Navigate to ****Applications > Applications****.
   ![Applications dropdown when the subitem Applications is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28716331678363)
3. Click ****Add App**** in the upper right corner.
   ![Applications page in One Login when Add App is selected](https://klaviyo.zendesk.com/hc/article_attachments/28716331682971)
4. Search for “Klaviyo” and then select the result that appears.
   ![Searching Klaviyo in the One Login apps](https://klaviyo.zendesk.com/hc/article_attachments/28716354700443)
5. Optional: choose the display name, upload a new icon, or add a description for this app.
6. Click ****Save**** in the upper right.
7. Navigate to ****Configuration**** in the left sidebar.
   ![Configuration page with no information in it](https://klaviyo.zendesk.com/hc/article_attachments/28716331718427)
8. In the **SAML Consumer URL** field, paste your **Klaviyo SSO URL**.
9. In the **Audience (SP EntityID)** field, paste your **Audience URI (Service Provider Entity ID)**.
10. Click ****Save****.
11. Click ****SSO**** in the left sidebar.
12. Open the **SAML Signature Algorithm** dropdown.
13. Select ****SHA-256****.
    ![SAML Signature Algorithm dropdown when SHA-256 is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28716354710939)
14. Optional: scroll down to change your login display settings.
    ![Login display settings for an app in One Login](https://klaviyo.zendesk.com/hc/article_attachments/28716331729179)
15. Click ****Save****.
16. Open the ****More Actions**** dropdown in the upper right.
17. Select ****SAML Metadata****. This will download the file you need to upload in the next section.
    ![More Actions dropdown when SAML metadata is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28716331734939)

    Before moving on to the next section, you need to add users to the Klaviyo app in One Login and then assign their roles.
18. To add users to the Klaviyo app, click ****Users > Users**** in the upper left.
    ![Users menu dropdown](https://klaviyo.zendesk.com/hc/article_attachments/28716331739163)
19. Select a user to access Klaviyo. We recommend assigning the person who is setting up SSO in Klaviyo.
20. Select ****Applications**** in the left sidebar.
21. Click the plus button on the right side to add an application to this user.
22. Select ****Klaviyo**** from the dropdown.
    ![Selecting Klaviyo as the application for a user](https://klaviyo.zendesk.com/hc/article_attachments/28716354727579)
23. Click ****Continue****.
24. In the resulting modal, scroll down to the **role** dropdown.
25. Open this dropdown and select the [Klaviyo role](https://help.klaviyo.com/hc/en-us/articles/115005231648) this user should be assigned.
    ![Selecting a Klaviyo role for a user](https://klaviyo.zendesk.com/hc/article_attachments/28716331715099)
26. Click ****Save****.

****Microsoft Entra ID (Azure AD)****

1. Log in to Microsoft Entra ID (formerly known as Azure AD).
2. Click ****Microsoft Entra ID****.
3. Select the ****Add**** dropdown and then click ****Enterprise Application****.
4. Click ****Create your own application****.
   ![Microsoft Entra ID Gallery, where you can create an application](https://klaviyo.zendesk.com/hc/article_attachments/28716354728219)
5. Name the application “Klaviyo,” then click ****Create****.
6. Click ****Single sign-on**** in the left sidebar.
   ![Single sign-on method page for an application, which defaults to disabled](https://klaviyo.zendesk.com/hc/article_attachments/28716331767067)
7. Select ****SAML****.
8. Click ****Edit**** in the **Basic SAML Configuration** box.
   ![Basic SAML configuration box, step 1 in the single sign-on page](https://klaviyo.zendesk.com/hc/article_attachments/28716331749787)
9. In the right sidebar that appears, click ****Add identifier**** under **Identifier (Entity ID)**.
   ![Sidebar to configure SAML for an application's SSO](https://klaviyo.zendesk.com/hc/article_attachments/28716331753115)
10. In the field that appears, paste in the **Audience URI****(Service Provider Entity ID)** from Klaviyo.
11. Under **Reply URL (Assertion Consumer Service URL)**, click ****Add reply URL****.
12. Here, paste the **Klaviyo SSO URL** from Klaviyo.
    ![Example of SAML configuration after adding an identifier and Reply URL](https://klaviyo.zendesk.com/hc/article_attachments/28716331755419)
13. Note: if you want to add in a **Sign on URL**, you must first create a workplace ID, which is discussed in the next section. We recommend finishing the setup process and then coming back to this step.
14. Click ****Save**** in the top left corner of the sidebar before clicking the ****X**** in the upper right.
15. Scroll down to the **SAML Certificates** box (step 3 on the **Single sign-on page** in Entra).
    ![Step 3 of the Single sign-on page](https://klaviyo.zendesk.com/hc/article_attachments/28716354742555)
16. Next to **Federation Metadata XML**, click ****Download****.
    ![SAML certificates box where only the Federated Metadata XML option is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28716354754203)
17. Still within the **SAML Certificates** box, click ****Edit**** in the upper right.
18. In the sidebar that appears on the right, check that the:

    - **Signing Option** requires that the SAML assertion be signed (here, we set it to ****Sign SAML assertion****). Note that signing the response is optional.
    - **Signing Algorithm** is set to ****SHA-256****.![Sidebar to edit the SAML certificates' signing option and algorithm](https://klaviyo.zendesk.com/hc/article_attachments/28716331761307)
19. Scroll back up to the **Attributes & Claims** box (step 2 on **Single sign-on page** in Entra) and click ****Edit****.
    ![Step 2 of the Single sign-on page, which is the Attributes and claims box](https://klaviyo.zendesk.com/hc/article_attachments/28716354759579)
20. Click ****Unique User Identifier (Name ID)**** in the **Required Claim** section.
    ![Manage claim modal where the Unique User Identifier row is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28716354763419)
21. Click the ****Source attribute**** dropdown.
    ![Source attribute field for the unique user identifier](https://klaviyo.zendesk.com/hc/article_attachments/28716331779995)
22. Search for “user.mail” and then select it.
    ![Searching user.mail for the source attribute](https://klaviyo.zendesk.com/hc/article_attachments/28716354776347)
23. Click ****Save**** in the upper left corner to go back to the **Attributes & Claims** page.
24. Select ****Add new claim**** in the upper left.
    ![Adding new claim in the Attributes & Claim page](https://klaviyo.zendesk.com/hc/article_attachments/28716354779419)
25. Enter “role” for the name.
26. Change the **Source attribute** to "user.assignedroles."
    ![Azure 14 new role claim.png](https://klaviyo.zendesk.com/hc/article_attachments/28716331810331)
27. Click ****Save****.
28. Click ****Home**** to go back to the directory.
29. In the left sidebar, click ****App registrations****.
    ![App registrations tab in the left sidebar](https://klaviyo.zendesk.com/hc/article_attachments/28716354789659)
30. Go to the ****All applications**** tab.
    ![All applications tab in the app registrations page](https://klaviyo.zendesk.com/hc/article_attachments/28716354791707)
31. Click into the Klaviyo app.
32. Select ****App roles > Create app role****.
    ![Create app role in the app roles page](https://klaviyo.zendesk.com/hc/article_attachments/28716354783003)
33. Create the display name for each role.
34. Select ****Users/Groups**** as the **Allowed member types**.
35. Assign one of these values exactly how it appears below:

    - admin
    - manager
    - analyst
    - campaign\_coordinator
    - content\_creator
    - support![Example of assigning a user as the owner of a Klaviyo account](https://klaviyo.zendesk.com/hc/article_attachments/28716331794459)
36. Add a description, then click ****Apply****.

    Then, to assign users to the Klaviyo app, follow these steps:
37. Navigate to ****Microsoft Entra ID > Enterprise applications****.
38. Click the ****Klaviyo**** app.
39. Navigate to ****Users and groups > Add user/group****.
    ![Users and groups page for the example Klaviyo application](https://klaviyo.zendesk.com/hc/article_attachments/28716331802267)
40. Click into ****Users**** to populate the right sidebar.
    ![Selecting users for an app](https://klaviyo.zendesk.com/hc/article_attachments/28716354796443)
41. Select the user(s) you want to add to the Klaviyo app.
42. Click ****Select****.
43. Click into ****Select a role****.
    ![Assigning roles for the selected users](https://klaviyo.zendesk.com/hc/article_attachments/28716331796635)
44. Choose the role this user should have in Klaviyo.
45. Click ****Select**** to confirm the role.
46. Click ****Assign**** in the bottom left.

## Finish setup in Klaviyo

1. Navigate back to your Klaviyo tab to the **SSO Setup** page.
2. Choose to either:

   - Add in your IdP issuer and SSO.
     Or
   - Upload a file with this information.![Second step of the SSO configuration page, where you add information about your iDP issuer](https://klaviyo.zendesk.com/hc/article_attachments/28716354659099)
3. Create your SSO login identifier (also called the workplace ID) for your SSO login; often, this is the same name as your company.

   - The ID cannot be longer than 63 characters.
   - The ID must be URL safe, so it can contain only upper- or lowercase letters, hyphens (-), periods (.), underscores (\_), and tildes (~).
   - The ID should be simple and easy for users to remember (such as your company name).
     - For example, Klaviyo’s workplace ID is “Klaviyo.”![Third step of the SSO configuration page, where you add your workplace ID](https://klaviyo.zendesk.com/hc/article_attachments/28716354664987)
4. Click ****Test SSO****.
5. Check the ****Enable SSO**** box.
6. Optional: check one or more of the following boxes.

- Require SSO for all users.
- IdP initiated log in.
- Just-in-time (JIT) provisioning.

![Options for using SSO once it's been set up](https://klaviyo.zendesk.com/hc/article_attachments/28716354646811)

## Outcome

Now you'll be able to log in to Klaviyo using your SSO provider.