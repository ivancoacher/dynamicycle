---
id: "40493034144795"
title: "How to create a custom user role"
source_url: "https://help.klaviyo.com/hc/en-us/articles/40493034144795-How-to-create-a-custom-user-role"
section: "Users"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: "en"
---
Find out how to create, edit, and assign custom user roles so each user on your account only sees the area of the product that they need.

## Before you begin

- ****Who can do this****
  All users who have the user management permission set or the admin or owner user role.
- ****Availability****
  All Klaviyo plans. Best suited for mid-market and enterprise accounts with multiple users.

## Overview

Custom User Roles allow you to tailor user permissions to your team's specific needs, ensuring each user has access only to the areas of the product required for their job. Fine-grained access control shortens onboarding, reduces security risk, and keeps billing, data, and messaging settings in the right hands — improving deliverability and ROI.

Klaviyo provides 7 static roles (Owner, Admin, Manager, Analyst, Campaign Coordinator, Content Creator, Support) by default. Custom roles enable you to mix and match specific permission sets (e.g., **Content View**, **Account Settings Edit**) to create roles that precisely match your organization's structure. Use Custom roles when the static roles provide either too much or too little access.

## Set it up

1. Go to ****Settings > Accounts > Users****.
2. Click ****Roles********>********Add****
3. In the ****Name**** field, enter a clear, unique name (e.g., “Lifecycle Marketer – EU”).
4. In the ****Description**** field, enter a description of the role and who this role is for. This description will be visible in the users tab and when you are assigning a role to a user.
5. Under ****Permissions****, check the permission sets this role needs. Permission set breakdown below

   - Click ****View full details**** to open the Help Center article ****User management and privileges reference****.
6. Click ****Create****
7. Your new custom user role is now created and will appear in the ****Roles**** section of the Users tab in Settings.
8. Assign the role:
   a. Still in ****Settings > Accounts > Users****, click ****Add user**** or select an existing user → ****Edit role****.
   b. Choose your Custom role, then click ****Save****.

### Edit a Custom role

1. Go to ****Settings > Users › Roles.****
2. Select the role.
3. Open  ****Menu**** → ****Edit****.
4. Change the name, description, or permissions → ****Save****.
   ****Warning****: Updates apply to ****all**** users in that role immediately.

### Delete a Custom role

1. ****Settings > Users › Roles****.
2. Select the 3 vertical dots, then click ****Delete****.
3. If users are still assigned, you’ll be unable to delete those roles. Reassign the user's role, then delete.
   ****Note****: Static roles can’t be deleted.

## Best practices

- ****Align Roles to Job Functions:**** Create roles that correspond to real job functions in your organization (e.g., Creative, Growth, Finance). This makes it easier to audit and manage permissions.
- ****Leverage Content Permissions:**** For users who only need to view data or content (e.g., external agencies), use the **Content View** permission set without granting **Edit** access.
- ****Limit Billing Access:**** Grant the **Billing Edit** permission set to as few users as possible to prevent unauthorized changes to your plan or payment information.
- ****Conduct Regular Audits:**** Review roles and user assignments quarterly, or whenever a team member changes departments.
- ****Keep Descriptions Clear:**** Use short, specific descriptions (e.g., "Can build flows; no billing access") so other admins can understand the role's purpose at a glance.

## Permission

### Permission set breakdown

Access to the product areas outlined below can be broken down between the following access controls.

- View
- View and Export
- Edit
- Publish

### Product areas

You can choose between the following areas to create your own custom user role

|  |  |
| --- | --- |
| ****Product area**** | ****Description**** |
| Content | View, manage or publish dashboards, campaigns, flows, sign-up forms, templates, products, [Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675) content, and all other content assets. Users can also access analytics, conversations, and intelligence data.    With this permission, users can see some profile data within UIs like flows and reports, but they cannot edit a full profile, view all profile data, or use any of the export functionality that exists on the Profiles, Lists, and Segments tabs. |
| Profiles, Lists and Segments | View, create, export or edit lists, segments, and individual user profiles. Users can also manage inactive segments, view and edit subscriber growth, manage suppressed profiles, and view or edit all details on a profile. |
| Billing | View or edit all billing details for the account. |
| Account Settings | View or edit all account-level settings, including security, translations, domains, tags, email, SMS, push, attribution, data, all downloads from the app and monitors. |
| User Management | Add and remove users, create and update custom roles, and assign roles to users. |
| Data Platform | View and edit advanced data features, such as transformations, custom objects, webhooks, and the data warehouse sync.  With access to "All of Data Platform", users will also gain access to Integrations. |
| API Keys and Integrations | Create and edit API keys and manage all integrations, including those from the [Customer Hub](https://klaviyo.zendesk.com/hc/en-us/articles/33660324811675). |
| Cross account cloning | Allows cloning of flows, campaigns, segments, forms, and templates across accounts. Requires Content Edit access and does not grant standalone content permissions. |
| Help Desk | Access to help desk workflows such as inbox, tickets, tags, and customer orders. View access is read-only; Edit access allows responding to tickets and updating orders. |
| Customer Agent | View or manage Customer Agent functionality, including agent status. Edit access allows configuration changes; View access is read-only.  Integrations and API keys EDIT permission set is required to set up Customer Agent. |
| Customer Hub | View or manage Customer Hub surfaces. View access allows read-only access to Customer Hub data and UI. Edit access allows users to modify Customer Hub configuration and perform write actions. |

## Troubleshooting

| ****Symptom**** | ****Likely cause**** | ****Fix**** |
| --- | --- | --- |
| User can’t see ****Create role**** | Their role lacks ****Account & User Management › Edit**** | Have an Owner or Admin update their permissions. |
| “Can’t delete role while users assigned” message | At least one user is in that role | Reassign or remove users, then delete. |
| Feature missing after assigning role | Permission set not included | Edit the role and add the required permission set. |
| Export buttons greyed out | Role only has ****View**** permission | Add the corresponding ****Export**** or ****Edit**** permission set. |

## FAQ

****How many Custom roles can I create?****

There is no limit to the amount of custom roles you can create.

****Do Custom roles change the 7 static roles?****

No. Static roles stay the same; you simply get more options and flexibility in creating new roles.

****Can I copy a static role into a Custom role?****

Not today. Re-create it by selecting equivalent permission sets.

****Will future Klaviyo features appear automatically?****

New features inherit the closest existing permission set. Review release notes regularly and adjust roles if needed.

****Do Custom roles sync via SCIM?****

Yes. SCIM can create, update, and deactivate users in your Custom roles. After you create a custom role in the app, be sure to copy the Custom SCIM ID.

## Next steps

- Audit existing users and migrate them to cleaner Custom roles.
- Turn on [single sign-on (SSO)](https://help.klaviyo.com/hc/en-us/articles/9353860331035) and ****MFA enforcement**** for stronger security.