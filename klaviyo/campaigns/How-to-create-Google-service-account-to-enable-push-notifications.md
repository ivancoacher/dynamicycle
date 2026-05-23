---
id: 19893982562203
title: "How to create Google service account to enable push notifications"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19893982562203-How-to-create-Google-service-account-to-enable-push-notifications"
section: "Push notification campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-20T16:49:18Z"
language: en
---

## You will learn

Learn how to set up your Google service account and enable Firebase Cloud Messaging so you can send Klaviyo push notifications to Android devices.

## Before you begin

Before following the steps below, you must have an existing Firebase project.

## Enable Cloud messaging API

1. Navigate to the [Google Cloud console](https://console.cloud.google.com/welcome).
2. Select your Firebase project from the dropdown in the top left corner.
3. Search for “Firebase Cloud Messaging API.”
4. Select ****Firebase Cloud Messaging API**** from the marketplace list.
   ![Searching for the Firebase Cloud Messaging API](https://klaviyo.zendesk.com/hc/article_attachments/28720761878939)
5. In the modal that appears, click ****Enable****.

![Page to enable Firebase Cloud Messaging API](https://klaviyo.zendesk.com/hc/article_attachments/28720790367387)

## Create a custom role that supports message creation

1. From the [Google Cloud console dashboard](https://console.cloud.google.com/welcome), select ****IAM & Admin**** under the **Quick Access** section.
   ![All Quick Access links, with only the IAM & Admin option highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28720790364315)
2. In the left menu, navigate to the ****Roles**** section.
   ![Roles highlighted in the left sidebar](https://klaviyo.zendesk.com/hc/article_attachments/28720790354971)
3. Click ****+Create Role****.
   ![Roles page, where Create role is shown in the upper left](https://klaviyo.zendesk.com/hc/article_attachments/28720761885595)
4. Fill out details about the role (name, description, etc.).
   ![Create Role window](https://klaviyo.zendesk.com/hc/article_attachments/28720761875611)
5. Click ****+Add Permissions****.
6. Add only the **cloudmessaging.messages.create** permission. (For more details, see Google’s instructions for [creating a custom role](https://cloud.google.com/iam/docs/creating-custom-roles#creating).).
   ![Searching for the correct role permission](https://klaviyo.zendesk.com/hc/article_attachments/28720790351643)
7. Click ****Add****.
8. When ready, create the role by selecting ****Create****.

## Create a Google service account

1. In the left side menu of the [IAM & Admin section](https://console.cloud.google.com/iam-admin/iam), navigate to the **Service Accounts** tab.
2. Click ****+Create Service Account****.
   ![Button to create a Google service account](https://klaviyo.zendesk.com/hc/article_attachments/28720790390043)
3. Fill out the **Service account name** and **Service account description** (optional) fields.
   ![First step of the wizard to create a new service account](https://klaviyo.zendesk.com/hc/article_attachments/28720761897883)
4. Click ****Create And Continue****.
5. Click into the **Select a role** field.
   ![Adding a role to a new service account](https://klaviyo.zendesk.com/hc/article_attachments/28720790375579)
6. Select the custom role that you just created. Here, we choose “Test Role,” but select the role you created in the previous section.
7. Click ****Done**** to finish creating the service account.

## Generate a service account key

1. In the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page, click on the email address for the service account that you created in the previous section.
   ![Service accounts page, where the accounts are blurred for security purposes](https://klaviyo.zendesk.com/hc/article_attachments/28720790388635)
2. Navigate to the ****Keys**** tab.
3. Click ****Add Key****.
4. Click ****Create new key****.
   ![Add key dropdown, when the Create new key option is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28720790379163)
5. Under **Key type**, select ****JSON****.
   ![Modal to select the key type when JSON is selected](https://klaviyo.zendesk.com/hc/article_attachments/28720790372379)
6. Click ****Create**** to download the service account key file.
   Note: you cannot download the file again, so ensure that you can locate the file on your computer. The downloaded JSON file should have the following format:
   `{ "type": "service_account",
   "project_id": "PROJECT_ID",
   "private_key_id": "KEY_ID",
   "private_key": "-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY\n-----END PRIVATE KEY-----\n",
   "client_email": "SERVICE_ACCOUNT_EMAIL",
   "client_id": "CLIENT_ID",
   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
   "token_uri": "https://accounts.google.com/o/oauth2/token",
   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL" }`

## Outcome

Now that you created and assigned the role to your Google service account, you can begin setting up Klaviyo Android push notifications.