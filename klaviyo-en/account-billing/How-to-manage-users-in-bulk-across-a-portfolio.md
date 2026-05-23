---
id: 44579003241499
title: "How to manage users in bulk across a portfolio"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/44579003241499-How-to-manage-users-in-bulk-across-a-portfolio"
section: "Portfolio"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-04-21T13:55:01Z"
language: en
---

## ****Overview****

With bulk user management, portfolio users with the correct user roles can manage user access across multiple linked accounts from a single, centralized interface. This eliminates the need to toggle between individual accounts to add, edit, or remove users, providing a "bird's-eye view" of your organization’s active users.

In this article, you will learn how to:

- Add new users to multiple accounts simultaneously.
- Edit user roles and permissions in bulk.
- Off board users from all portfolio linked accounts in one action.
- Understand SSO and Activity Log implications.

## ****Before you begin****

Bulk user management is available exclusively at the Portfolio level. To access this functionality, you must have one of the following roles:

- ****Portfolio Owner****
- ****User Management EDIT**** permission set

## ****Add new users to linked accounts in bulk****

You can invite one or more users to multiple accounts at once, ensuring new team members have the access they need across your entire brand portfolio.

1. Navigate to the ****Users**** tab in the left navigation column.
2. Click ****Invite Users****.
3. In the ****Email Address(es)**** field, enter the email addresses of the individuals you wish to invite. You can separate multiple addresses using commas, spaces, or by pressing ****Enter****.
4. Select the preferred ****Language**** for these users.
5. Under ****Select Accounts****, check the box next to each account you want the users to access.
6. ****Assign a Role**** for each selected account. Note that **Support** is the default role; use the dropdown to change this if necessary.
7. Click ****Review Changes**** to see a summary of the invitations.
8. Click ****Send Invite****.

## ****Edit user roles in bulk****

There are two ways to edit roles: by clicking into a specific user's profile or by using the bulk checkbox selection for a group of accounts.

### ****Edit roles via User Profile****

1. Find the user in the ****Users**** list and click on their name.
2. View the list of every account the user currently accesses and their specific role.
3. To update a role, select a new role from the ****Role**** dropdown next to the specific account.
4. Review and ****Confirm**** the update.

### ****Bulk update roles across accounts****

1. Within the user's profile view, select the ****check box**** next to each account name you wish to modify.
2. Select a new ****Role**** from the bulk action bar.
3. Click ****Review Changes****.
4. Click ****Update Roles****.

## ****Remove users in bulk****

Quickly revoke access for users who no longer require permission to specific accounts or the entire portfolio.

1. Find the user in the ****Users**** list and click on their name.
2. View the list of accounts the user currently accesses.
3. ****To remove access from a single account:****

   - Click the ****More (three-dot)**** menu next to the account.
   - Select ****Remove Access****.
4. ****To remove access from multiple accounts:****

   - Select the ****check box**** next to each account name.
   - Select ****Remove Access**** from the bulk action menu.
5. Review the summary of removals and ****Confirm****.

## ****Activity logging and security****

Every action taken within the bulk user management interface is tracked for security and compliance:

- ****Audit Trail:**** When a user’s role is changed or removed from the portfolio, an event is automatically created in the ****Activity Log**** of each affected account.
- ****Traceability:**** The log entry will specify that the change was initiated from the ****Portfolio level****, identifying which Portfolio Admin performed the action.

## ****Troubleshooting****

- ****Why can't I edit a specific user?**** If a user is managed via an Identity Provider (SSO with JIT enabled), their role is locked within Klaviyo. You must update their permissions in your IDP (e.g., Okta or Azure).
- ****Why don't I see the Users tab?**** Ensure you are at the Portfolio level (not inside a specific brand account) and that your user role includes User Management edit permissions.
- ****Why can't I update or remove a user who is an Owner?**** You cannot update the role of an Account Owner or remove them from an account via the Portfolio bulk management interface. Because the Owner role holds the highest level of legal responsibility for an individual account, these changes must be performed at the individual account level by the current Owner.