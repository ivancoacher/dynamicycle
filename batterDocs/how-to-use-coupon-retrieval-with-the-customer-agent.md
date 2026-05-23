<h1>How to use coupon retrieval with the Customer Agent</h1>

## You will learn

This article explains how the K:AI Customer Agent can automatically retrieve and share active coupon codes with customers during conversations. This capability is enabled automatically with your Customer Agent so you can resolve common "where is my discount?" inquiries instantly, driving faster conversions and reducing support volume without human intervention.

## Before you begin

- ****Prerequisites:****
  - You must have the ****K:AI Customer Agent**** enabled in your account.
  - Your account must be integrated with ****Shopify**** to leverage full coupon data.
  - You must have active coupons created in Klaviyo or Shopify that are assigned to profiles or available globally.
- ****Availability:****
  - This feature is available for ****Web Chat and SMS****.
  - ****Web Chat:**** Customers must be signed in (authenticated) to receive profile-specific coupons. Anonymous users will be prompted to sign in or will only receive general public promotion details found in your knowledge base.
  - ****SMS/Email/WhatsApp:**** Users are automatically identified by their phone number or email, so no additional sign-in is required.
- ****Roles:**** You must have ****Owner, Admin, or Manager**** permissions to configure Agent settings.

## Overview

The Customer Agent uses a specialized "coupon skill" to handle inquiries about discounts, sales, or promo codes. When a customer asks a question like "Do you have any active codes?" or "Is there a sale?", the agent performs two searches simultaneously:

1. ****Content search:**** Checks your imported help articles and policies for public information about sitewide sales (e.g., "Black Friday 20% off everything").
2. ****Profile coupon retrieval:**** Securely checks the specific customer's profile for existing, valid coupon codes that have not yet been redeemed or expired.

If an active coupon is found, the agent displays the code directly in the chat. If no coupons are available, the agent politely informs the customer, resolving the query without hallucinating fake discounts.

## Set it up

The coupon retrieval skill is part of the AI Service Agent's core intelligence, but you must ensure your data is ready for it to function correctly.

1. ****Verify your active coupons****
2. From Content > Coupons, ensure you have active (unexpired) coupons. The agent can retrieve:

   - ****Static coupons:**** Codes available to many active users (e.g., `WELCOME20`).
   - ****Unique/Dynamic coupons:**** Existing unique codes already assigned to a specific profile (e.g., Welcome-John-123).
   - Note: The agent retrieves existing coupons; it does ****not**** generate new unique codes on the fly.
3. ****Test the experience****
   1. Navigate to Customer Agent > Agent Preview
   2. Impersonate a profile that you know has an active coupon (or assign one to a test profile for verification).
   3. Ask the agent: "Do I have any discount codes?"
   4. Expected result****:**** The agent should reply with the specific code.
4. ****Configure Agent Content (Optional)****
5. If you have sitewide sales that don't use individual codes (e.g., "Automatic 10% off at checkout"), ensure this information is present in a source synced to your Agent Content.

- ****Action:**** specific text in your FAQs like "We are currently running a Summer Sale with automatic discounts."

## Best practices

- ****Keep Content updated:**** For broad sales (e.g., "Free Shipping over $50"), make sure your policy pages or synced content sources are up to date so the agent captures these general offers alongside specific codes.

## Measure success

- ****Where to view results:**** Go to ****Customer Agent > Performance****.
- ****Key metrics to watch:****
  - ****Resolution Rate:**** Look for an increase in resolved conversations for topics related to "discounts" or "coupons."

## FAQ

Q: Can the agent generate a brand new unique code for a customer asking for one?

A: No. The agent currently only retrieves existing active coupons already assigned to that profile. It does not create new codes on demand.

Q: Does this work for SMS?

A: Yes. Since SMS users are inherently identified by their phone number, the agent can immediately look up their profile and return their specific coupons.

Q: What happens if a user has multiple coupons?

A: The agent will retrieve and display the available active coupons. This means multiple can be surfaced at once if they are all still valid.

## Next steps

- ****Review your Welcome Series:**** Ensure your automated flows are generating and assigning coupons correctly so the Agent has data to fetch.
- ****Optimize your Customer Agent Content:**** Add a specific "Current Promotions" article to your help center to give the Agent easy access to public sale info.
