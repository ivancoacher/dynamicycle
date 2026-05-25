---
id: "44439474248603"
title: "How to connect Loop Returns to Klaviyo Helpdesk"
source_url: "https://help.klaviyo.com/hc/en-us/articles/44439474248603-How-to-connect-Loop-Returns-to-Klaviyo-Helpdesk"
section: "Channel & Integration Management"
category: "Helpdesk"
category_slug: "helpdesk"
klaviyo_updated: "2026-04-17T07:02:42Z"
language: "en"
---
The Loop Returns integration for Klaviyo Helpdesk allows your support agents to view return statuses, initiate returns, and share return labels without ever leaving the ticket view. This guide covers how to set up the integration and how to use it in your daily workflow.

---

## Before you begin

To enable this integration, you must have:

- An active ****Loop Returns**** account.
- A ****Klaviyo**** account with Helpdesk enabled.
- User permissions of ****Owner****, ****Admin****, or ****Manager**** to access integration settings.

---

## Connect Loop Returns

Connecting Loop Returns requires generating a specific API key in Loop and adding it to your Klaviyo settings.

### Step 1: Generate your Loop API Key

1. Log in to your ****Loop Returns**** admin dashboard.
2. Navigate to ****Settings > Developers > API Keys****.
3. Click ****Generate API Key****.
4. ****Important:**** When selecting scopes for this key, you must check the boxes for both ****Orders**** and ****Returns****.

   - **Note: Without these specific permissions, the integration cannot look up order details or initiate returns.**
5. Copy the generated API Key.

### Step 2: Enable the integration in Klaviyo

1. Log in to ****Klaviyo****.
2. Navigate to ****Customer Hub -> Extension****
3. Set ****Loop Returns**** as your returns provider.
4. Toggle the ****Enable Loop Returns**** setting to ****On****.
5. Paste your ****API Key**** into the designated field.

   - **Caution: Double-check that you have copied the full key. Klaviyo does not validate the key upon saving, so an incorrect key will result in error messages for your agents later.**
6. Click ****Save****.

---

## How returns work in Helpdesk

Once connected, return status and ability to initiate returns will be added to the existing order card.

### View Return Status

When you open a ticket, the integration automatically checks for existing returns associated with the customer's order history. You will see:

- ****Current Status:**** The state of the return (e.g., **Open**, **Review**, **Closed**, **Cancelled**).
- ****Tracking:**** Carrier details and a clickable tracking number for the return shipment.

### Initiate a Return

If a customer requests a return or exchange, you can start the process directly from the sidebar:

1. Locate the specific order in the sidebar.
2. Click ****Initiate Return****.
3. Choose how you want to share the return portal with the customer:

- ****Copy Link:**** Generates a "Deep Link" that logs the customer directly into the return portal for that specific order. You can paste this into your chat or email reply.

---

## Frequently asked questions

****Why can't I see the "Initiate Return" button?**** The button only appears if the order is eligible for return according to your Loop policies (e.g., within the return window) and if there is no active return already open for that order.

****Can I create a return label for a customer manually?**** At this time, the integration allows you to generate Deep Links and QR codes that guide the customer to the portal to confirm their items. You cannot fully complete the return selection on their behalf from inside the Helpdesk.