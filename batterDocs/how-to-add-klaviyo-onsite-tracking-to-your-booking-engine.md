<h1>How to Add Klaviyo Onsite Tracking to Your Booking Engine</h1>

This guide will walk you through integrating ****Google Tag Manager (GTM)**** with your Property Management System (Mews, Cloudbeds, or Guesty) using the ****Klaviyo Hotels Tag****.

By the end of this setup, you’ll be able to track key website visitor behaviors like ****Active Onsite,**** ****Viewed Listing,**** and ****Started Checkout**** directly in your Klaviyo account. This will allow you to easily set up revenue-driving automations, such as Browse Abandonment and Abandoned Cart flows, and create highly-targeted segments.

****Before you begin, if you don't already have a Google Tag Manager account, please follow Google's**** [****guide****](https://support.google.com/tagmanager/answer/14842164?hl=en) ****on how to set one up.****

---

## Step 1: Locate Your GTM Container ID

Before you begin, you need to identify the specific container you want to use.

1. Log into your [Google Tag Manager](https://tagmanager.google.com/) account.
2. Select the ****Container**** associated with your hotel’s website.
3. At the top of the window, next to the "Submit" and "Preview" buttons, you will see your ****Container ID**** (it looks like `GTM-XXXXXXX`).
4. ****Copy this ID**** to your clipboard.

![0.9.png](https://klaviyo.zendesk.com/hc/article_attachments/46643062813851)

---

## Step 2: Connect GTM to Your Property Management System (PMS)

You need to tell your booking engine to "listen" to your GTM container. Follow the steps for your specific platform below:

### For Cloudbeds

1. Log into Cloudbeds.
2. Click on the ****Account Icon**** > ****Settings > Booking Engine****.
3. Select the ****Analytics**** tab****.****
4. Paste your ****Container ID**** into the GTM field and save.

![2.png](https://klaviyo.zendesk.com/hc/article_attachments/46643062816923)

For more instructions, follow the [Cloudbeds guide](https://myfrontdesk.cloudbeds.com/hc/en-us/articles/25825202111387-Connect-Google-Analytics-with-Cloudbeds-Booking-Engine).

### For Mews

1. Log in to Mews.
2. Go to ****Settings > Services****.
3. Select a Bookable service.
4. Click on ****Booking engines****.
5. Select the booking engine that you want to track with Google Tag Manager.
6. Under ****Google tag manager ID****, paste your ****Container ID.****
7. Click ****Save****.

![3.png](https://klaviyo.zendesk.com/hc/article_attachments/46643094244763)

For more instructions, follow the [Mews guide](https://help.mews.com/s/article/google-tag-manager).

### For Guesty

1. To install the code on your site:
2. Log in to Guesty.
3. Select the ****Operations**** dropdown at the top, then select ****Growth > Distribution****.
5. ![](https://klaviyo.zendesk.com/hc/article_attachments/46643062822683)
6. Select ****Guesty Booking Engine****.
7. Click the triple dots next to your booking engine and select ****Edit Booking Engine****.
8. Scroll to the **Web analytics** section and past your ****Container ID****.
10. ![4.png](https://klaviyo.zendesk.com/hc/article_attachments/46643062823963)
11. Select ****Save Booking Engine.****

For more instructions, follow the [Guesty guide](https://help.guesty.com/hc/en-gb/articles/16714065345821-Using-analytics-tools-in-your-Guesty-Booking-Engine).

---

## Step 3: Add the Klaviyo Hotels Template in GTM

Now that GTM is connected to your PMS, you need to add the Klaviyo-specific tracking logic.

1. Back in Google Tag Manager, click ****Templates**** on the left-hand sidebar.
2. In the ****Tag Templates**** section, click ****Search Gallery****.
3. Search for ****"Klaviyo Hotels Tag"****.
   ![6.png](https://klaviyo.zendesk.com/hc/article_attachments/46643094254363)
4. Select the template and click ****Add to Workspace****.
5. Confirm by clicking ****Add**** again.

---

## Step 4: Create and Configure Your Tag

This step connects the template to your specific Klaviyo account.

1. Go to ****Tags**** on the left sidebar and click ****New****.
2. ****Name your tag**** (e.g., `Klaviyo Hotels Tracking`).
3. Click ****Tag Configuration**** and select the ****Klaviyo Hotels Tag**** you just added.
4. ****Enter your Klaviyo Public API Key:**** This is the 6-character identifier found in your Klaviyo Account Settings (see our [guide to finding your public key](https://help.klaviyo.com/hc/en-us/articles/115005062267)).
5. ****Select your PMS:**** Choose Mews, Cloudbeds, or Guesty from the dropdown menu.
6. ![](https://klaviyo.zendesk.com/hc/article_attachments/46643062833051)
7. ****Set the Trigger:**** Hover over the ****Triggering**** section. Click on the pencil that appears in the top right corner. Select ****All Pages****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/46643094261531)
8. Give the tag a name (e.g. [Cloudbeds/Mews/Guesty] Tag). Click ****Save****.

---

## Step 5: Publish Your Changes

Your tracking will not go live until you submit these changes.

1. Click the blue ****Submit**** button in the top right corner of GTM.
   ![10.png](https://klaviyo.zendesk.com/hc/article_attachments/48511182753179)
2. Give your version a name (e.g., `Added Klaviyo Hotels Tracking`).
3. Click ****Publish****.

![](https://klaviyo.zendesk.com/hc/article_attachments/46643062844187)

---

## What Happens Next?

Once published, the tag will automatically start sending event data to Klaviyo for identified visitors on your booking engine. [Learn about who Klaviyo can track here](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACVVC4BXQ0ES5Y50TC). You can verify that events are being tracked by checking the Metrics tab in your Klaviyo account for the following events:

- ****Active Onsite:**** Fires when someone is active on the website.
- ****Viewed Listing:**** Fires when a traveler looks at a specific room or property.
- ****Started Checkout:**** Fires when a traveler enters the booking flow.

Now you are ready to use the browse abandonment and abandoned cart flow templates, which can be found [here](https://www.klaviyo.com/flows/create) after selecting your PMS integration. But that is only the beginning - learn more about what you can do with Klaviyo onsite tracking [here](https://help.klaviyo.com/hc/en-us/articles/115005076767)!
