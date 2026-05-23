---
id: 10952782535579
title: "How to set up SCIM user provisioning"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/10952782535579-How-to-set-up-SCIM-user-provisioning"
section: "Security"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:56:35Z"
language: en
---

## You will learn

Learn how to set up a system for cross-domain identity management (SCIM) user provisioning in an account or portfolio.

You must have a paid plan and be an Admin or Owner to set up this feature.

## Before you begin

You also have [SSO turned on in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/9353860331035) before you set up SCIM.

Note that SCIM provisioning is often an add-on for identity providers (IdPs). For instance, IdPs often require a separate SCIM plan in addition to an SSO plan. If you don't see the following steps in your IdP, please confirm you have the correct plan.

## Turn on SCIM user provisioning

1. Click your organization name in the lower left corner.
2. Click ****Settings > Security****.
   ![Security tab in Account settings](https://klaviyo.zendesk.com/hc/article_attachments/28704477982875)
3. Check the **SCIM Provisioning** box.
4. Copy or download the access key, including the prefix `Klaviyo-API-Key`.
   Note that this key is only shown once, so make sure you can access it. If copying it, paste it somewhere secure immediately.
   ![Example of an access key](https://klaviyo.zendesk.com/hc/article_attachments/28704486111131)
5. Click ****Done****.
6. Copy the base URL and paste it somewhere, preferably where you stored the access key.

Next, you must go to your SSO provider to finish the process. This process varies by provider. Below, we have instructions for OKTA, One Login, and Azure, although you can set it up using any other provider.

****OKTA****

1. Navigate to ****Application > Applications****.
2. Select the Klaviyo app.
3. Go to the ****Sign On**** tab.
   ![Four tabs for an app with SSO: General, Sign On, Import, and Assignments](https://klaviyo.zendesk.com/hc/article_attachments/28704477997723)
4. Under **Credential Details**, check that:

   - **Application username format** is set to ****Email****.
   - **Update application username on** is set to ****Create and update****.![Credental Details section in the Sign On tab](https://klaviyo.zendesk.com/hc/article_attachments/28704486118683)
5. Click into the ****General**** tab.
   ![General tab for app, when there's no provisioning](https://klaviyo.zendesk.com/hc/article_attachments/28704477985051)
6. Select ****Edit****.
7. Under **Provisioning**, select SCIM.
   ![Selecting SCIM for the provisioning](https://klaviyo.zendesk.com/hc/article_attachments/28704486124827)
8. Click ****Save****.
9. Click into the ****Provisioning**** tab.
10. Select ****Edit**** to open the **SCIM Connection** page (shown below).
    ![SCIM Connection page with no information](https://klaviyo.zendesk.com/hc/article_attachments/28704477991963)
11. In **SCIM connector base URL**, paste the base URL from Klaviyo.
12. For **Unique identifier field for users**, type in “userName.”
13. Under **Supported provisioning actions**, check the following boxes:

    - Import New Users and Profile Updates
    - Push New Users
    - Push Profile Update
14. Change the **Authentication Mode** option to HTTP Header.
15. Paste in the access key under **Authorization**.
    ![How the SCIM Connection should look once filled out](https://klaviyo.zendesk.com/hc/article_attachments/28704486119195)
16. Click ****Test Connector Configuration****.
17. Click ****Save****.
18. Next to **Provisioning to App**, click ****Edit****.
19. Check ****Enable**** for the following features:

    - **Create Users**.
    - **Update User Attribute**.
    - **Deactivate Users.**![Enabled features in the Provisioning to App page](https://klaviyo.zendesk.com/hc/article_attachments/28704486120731)
20. Click ****Save****.
21. Scroll down to your app’s attribute mappings section.
22. Click ****Go to Profile Editor****.
23. Click ****Add Attribute****.
    ![Top of the Profile Editor page in Okta, showing the button to add an attribute](https://klaviyo.zendesk.com/hc/article_attachments/28704477999899)
24. Type “role” for **Display name**, **Variable name**, and **External name**.
25. In **External namespace**, enter the following:
    urn:ietf:params:scim:schemas:core:2.0:User
26. Check the box for ****Define enumerated list of values****.
    ![The first of the required settings for the role attribute](https://klaviyo.zendesk.com/hc/article_attachments/28704486132763)
27. Add in the roles and values; valid role values are as follows:

    - admin
    - manager
    - analyst
    - campaign\_coordinator
    - content\_creator
    - support![All roles with the correct values for the role attribute](https://klaviyo.zendesk.com/hc/article_attachments/28704486134171)
28. Scroll down to **Attribute required** and check ****Yes****.
29. Choose the attribute type (personal or group).
30. Recommended: leave the **User permission** as ****Read Only****.
    ![The rest of the required settings for the role attribute](https://klaviyo.zendesk.com/hc/article_attachments/28704478000539)
31. Click ****Save****.
32. Navigate to ****Applications > Applications**** and then select your app.
33. Click ****Assign****.
34. Choose whether to assign the app to an individual (i.e., people) or to a group.
    ![Assignments tab showing the Assign dropdown](https://klaviyo.zendesk.com/hc/article_attachments/28704486135323)
35. Find the people or groups you want to assign Klaviyo to, and click ****Assign**** next to their name(s).
    ![Example of searching for a user to assign to an app](https://klaviyo.zendesk.com/hc/article_attachments/28704478005915)
36. Scroll down to the **role** field and assign them the correct role.
    ![Role dropdown, showing all the values for roles within Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28704486114843)
37. Click ****Save and go back****.

****One Login****

1. In the Admin Portal, click ****Applications****.
2. Click ****Add App****.
3. Search “Klaviyo.”
4. Click ****Klaviyo**** to add it.
5. Optional: Rename the connection.
6. Click ****Configuration.****
7. In the **SCIM Bearer Token** field, paste your SCIM access key.
8. Click ****Enable**** under **API Connection**.
9. Click ****Save.****
10. Go to ****Provisioning**** in the left sidebar.
11. Check the ****Enable Provisioning**** box.
12. Do not uncheck the **Create user**, **Delete user**, or **Update user** boxes.
    ![Credential details section with the correct settings](https://klaviyo.zendesk.com/hc/article_attachments/28704477975451)
13. Recommended: select ****Delete**** in the dropdown for **When users are deleted in OneLogin, or the user's app access is removed, perform the below action**.
14. Click ****Save****.

****Microsoft Entra ID (formerly Azure AD)****

1. Log into [Microsoft Entra ID](https://portal.azure.com/#home.).
2. Click ****Microsoft Entra ID**** (formerly called “Azure Active Directory”)
3. Click ****Enterprise Applications**** on the left side.
   ![The Enterprise applications option in the left sidebar](https://klaviyo.zendesk.com/hc/article_attachments/28704486140699)
4. Select your application.

   - If you haven’t created your application yet, follow the steps in the [SSO guide](https://help.klaviyo.com/hc/en-us/articles/9353860331035).
5. Click ****Provisioning**** on the left, then select ****Get Started****.
   ![Left sidebar for app when Provisioning is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28704478008731)
6. In the field named **Provisioning Mode**, select ****Automatic****.
   ![Changing the Provisioning mode to automatic](https://klaviyo.zendesk.com/hc/article_attachments/28704478010011)
7. Go to the **Admin Credentials**.
8. Paste the SCIM base URL from Klaviyo into the **Tenant URL** field.
9. Paste the SCIM API key into the **Secret Token** field. Note that this token should be pasted in without any prefixes (e.g., don’t include "Bearer" or "Klaviyo-API-Key").
10. Test the connection.
11. Once the connection is successful, click ****Save**** in the upper left.
12. In that same page, scroll down and open the ****Mappings**** dropdown.
    ![Mappings dropdown to provision (in order) Azure AD groups or users](https://klaviyo.zendesk.com/hc/article_attachments/28704486146459)
13. Select ****Provision Azure Active Directory Users****.
14. Optional: delete non-supported attributes. Note that Klaviyo only supports the following attributes in c**ustomappsso Attribute** column for SCIM:

    - "userName"
    - "active"
    - emails[type eq "work"].value'
    - "name.givenName"
    - "name.familyName"
    - emails[primary eq "True"].value'
    - roles[primary eq "True"].value'
    - SingleAppRoleAssignment([appRoleAssignments])
      - appRoleAssignments is not supported
15. Click ****Save**** and then click ****Home****.
16. Navigate back to ****Microsoft Entra ID > Enterprise applications > Klaviyo > Provisioning****.
17. Select ****Start Provisioning****.

![Provisioning tab, showing the start provisioning button](https://klaviyo.zendesk.com/hc/article_attachments/28704478011931)