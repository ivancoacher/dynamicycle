---
id: "48920041574811"
title: "Hotel Enablement Guide"
source_url: "https://help.klaviyo.com/hc/en-us/articles/48920041574811-Hotel-Enablement-Guide"
section: "General"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:53Z"
language: "en"
---
# Hotel Enablement Guide

## ****Crawl****

**This section covers the initial set up required to start getting value out of Klaviyo. It does not cover all steps (e.g. adding brand assets), but focuses on solving the core hotel use cases.**

## ****Integrations****

For Klaviyo to effectively function as a brain, it needs data:

- Integrate your PMS →
  - This will automatically (1) create Klaviyo profiles based on your historic guest data (2) create reservation events and objects based on guest actions.
    - **Note: If you installed the integration before 1/30/26, you need to follow the steps to update your integration to sync reservation objects:** [**Mews**](https://help.klaviyo.com/hc/en-us/articles/38311148860955)**,** [**Cloudbeds**](https://help.klaviyo.com/hc/en-us/articles/39406849361691#h_01K45A8TV1MNXM2CV3TMGRSWWR)**, and** [**Guesty**](https://help.klaviyo.com/hc/en-us/articles/37673288455323#01KG8CX52V9GG13ZHD68DRRFHD)**.**
  - Getting started guides for [Mews](https://help.klaviyo.com/hc/en-us/articles/38311148860955), [Cloudbeds](https://help.klaviyo.com/hc/en-us/articles/39406849361691), and [Guesty](https://help.klaviyo.com/hc/en-us/articles/37673288455323).
- Set up other core integrations →
  - Previously-used ESPs (e.g. Mailchimp) may be helpful for porting over data.

## ****Segments****

Sending effective campaigns depends on determining the right audience to message. By connecting your PMS, Klaviyo automatically creates the following segments for you:

- First time customers →
  - Person has Confirmed Reservation once over all time AND Person can receive email marketing
- VIP customers →
  - Person has Confirmed Reservation is greater than 5 over all time AND Person can receive email marketing
- Churn risks →
  - Person has Confirmed Reservation at least once over all time AND Person has Confirmed Reservation zero times in the last 180 days AND Person has Received Email at least 2 in the last 90 days AND Person has Opened Email zero times in the last 90 days AND Person can receive email marketing
- Winback opportunities →
  - Person has Confirmed Reservation at least once over all time AND Confirmed Reservation zero times in the last 180 days AND Person can receive email marketing
- Repeat guests →
  - Person has Confirmed Reservation is greater than 1 over all time AND Person can receive email marketing

    We also recommend setting up a couple of date-based segments with reservation objects (see step #1). Then you can create a **Future Guests** segment, which will be useful for sending campaigns to everyone with a reservation from tomorrow onwards:
- Create a future guest segment →
  - Navigate to ****Audience > Lists & Segments****.
  - Click ****Create New**** and choose ****Create new segment****.
  - Name the segment (e.g., "Future Guests") and add tags if desired.
  - Under ****Definition****, select:
    - ****Properties about someone**** > ****Reservation**** > ****has at least one****
    - Click ****Add filter**** and select: ****where**** > ****StartDate**** > ****is in the next**** > ****1000 weeks****
  - Click ****Create segment****.

    And you can create a **Current and Future Guests** segment. This will be useful for excluding people from promotional emails:
- Create a current and future guests segment →
  - Navigate to ****Audience > Lists & Segments****.
  - Click ****Create New**** and choose ****Create new segment****.
  - Name the segment (e.g., "Current & Future Guests") and add tags if desired.
  - Under ****Definition****, add two conditions joined by ****OR****:
    - ****Condition 1 (future guests):****
      - ****Properties about someone**** > ****Reservation**** > ****has at least one**** > ****where**** > ****StartDate**** > ****is in the next**** > ****1000 weeks****
    - ****Condition 2 (currently checked in):****
      - ****Properties about someone**** > ****Reservation**** > ****has at least one**** > ****where**** > ****StartDate**** > ****is in the last**** > ****90 days****
      - Click ****Add filter**** and select: ****where**** > ****EndDate**** > ****is in the next**** > ****90 days****.

These provide a good starting point for people to reach through your campaign strategy.

## ****Onsite JS****

Setting up onsite JS will allow you to set up Klaviyo forms on your booking engine (see next step) as well as track user events on your website, which enables ****abandoned cart and browse abandonment flows**** and enhanced segmentation:

- Set up onsite JS →
  - If you're using the Mews/Cloudbeds/Guesty booking engine, you can follow [this guide](https://help.klaviyo.com/hc/en-us/articles/46643094275099) to set up Klaviyo onsite JS via Google Tag Manager.
    - This will start syncing onsite events (e.g. Started Checkout, Viewed Listing) from the booking engine.
  - Otherwise, you can follow the steps to [set up Klaviyo JS manually](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01GMEAQZXKADF4FR7P1FMNC7EB).
  - Once you have it set up, follow the [testing steps](https://help.klaviyo.com/hc/en-us/articles/115005076767#h_01HADAYAACFYSN7F22XPPCGT6B) to make sure you're getting the expected events.
    - Note: You will not get **Viewed Product** events as those are specific to e-commerce stores.

## ****Forms****

Now that you have onsite JS set up, you can start using Klaviyo forms to capture the contact information of potential guests that land on your website. Later, you'll be able to message these guests to drive direct bookings, thus avoiding the 15-30% fee OTAs take:

- Set up Klaviyo forms →
  - Follow the steps outlined in the [help center](https://help.klaviyo.com/hc/en-us/articles/360026474752) or the [academy](https://academy.klaviyo.com/en-us/courses/getting-started-with-sign-up-forms).

## ****Flows****

Klaviyo flows are automated email and SMS sequences triggered by specific customer behaviors. They allow you to message the right person at the right time. By connecting your PMS, Klaviyo provides you with the following flow templates:

| ****Flow**** | ****Trigger**** | ****When it sends**** | ****Why it matters**** |
| --- | --- | --- | --- |
| Welcome Series | Guest joins your list (e.g. via sign-up form) but hasn't yet booked | 2-3 emails over 7 days | Converts website visitors into first-time bookers; particularly effective for driving direct bookings away from OTAs. |
| Guest Winback | Time-based (e.g. 12 months since last checkout) | Ongoing | Lapsed guests are cheaper to re-engage than acquiring new ones. |
| Pre-Arrival | Check-in date (via Reservation Object) | 1-14 days before check-in | Best opportunity for up-sells and cross-sells (e.g. room upgrades, spa, dining, etc.). |
| Guest Thank You | Guest confirms a reservation | Immediately | Thank the guest for making a reservation. |
| Reservation Cancellation | Guest cancels a reservation | Immediately | Opportunity to understand why they cancelled + win back the booking. |
| Abandoned Checkout Reminder\* **Note: only available for websites using either the Guesty booking engine or a custom one.** | Guest started checkout | Wait 2 hours | Remind the guest to complete checkout. Opportunity to offer a discount. |
| Browse Abandonment\* **Note: only available for websites using either the Guesty booking engine or a custom one.** | Guest viewed listing | Wait 2 hours | Re-engage the guest. Share more details about the room and/or offer a discount. |

- Set up your flows →
  - Go to ****Flows > Create Flow**** and filter by your PMS (Mews, Cloudbeds, or Guesty) to find pre-built versions of the flows above.
    - **Note: Pre-Arrival requires reservation objects, see step #1 or the getting started guide (**[**Mews**](https://help.klaviyo.com/hc/en-us/articles/38311148860955#h_01KG8CE0CWN9M7TGWZ52YJY0VK)**,** [**Cloudbeds**](https://help.klaviyo.com/hc/en-us/articles/39406849361691#h_01K45A8TV1MNXM2CV3TMGRSWWR)**, and** [**Guesty**](https://help.klaviyo.com/hc/en-us/articles/37673288455323#01KG8CX52V9GG13ZHD68DRRFHD)**).**
  - Klaviyo's [flow help center](https://help.klaviyo.com/hc/en-us/articles/115002774932) and [academy](https://academy.klaviyo.com/en-us/courses/getting-started-with-flows) cover the full setup process.

## ****Campaigns****

Campaigns are what you send intentionally to specific audiences — promotions, seasonal offers, newsletters, and anything that isn't tied to a single guest action. Here are some good places to start:

1. Seasonal & Promotional Campaigns →

   - Timely sends aligned to holidays, local events, or low-occupancy periods (e.g. Valentine's Day, summer early-bird rate, etc.).
2. Re-Engagement / Winback Campaigns →

   - Send a special rate, a loyalty perk, or a "we miss you" message to lapsed guests who haven't booked in over a year.
3. Loyalty & VIP Campaigns →

- Send your VIP segment exclusive offers, first access to new packages, or a personal note acknowledging their loyalty.

- Set up your campaigns →
  - Go to ****Campaigns > Create Campaign**** and select Email or SMS.
  - Choose the relevant segment as your audience and exclude ([help guide](https://help.klaviyo.com/hc/en-us/articles/360007016571)) the **Current & Future Guests** segment set up above when appropriate.

---

## ****Your Guest Journey After Crawl****

Great work! This is what your guest journey looks like after completing this phase:

| ****Guest Journey Stage**** | ****Guest Action**** | ****How Klaviyo Engages**** | ****Type**** |
| --- | --- | --- | --- |
| 🟢 ****Discovers website**** | Visits your hotel website | Sign-up form captures contact info → Welcome Series email sequence nurtures them toward a first booking | Form + Flow |
| 🟢 ****Books**** | Confirms a reservation | Reservation Confirmation / Thank You flow fires automatically | Flow |
| 🟢 ****Cancels**** | Cancels a reservation | Cancellation flow fires with a soft win-back message and reason to rebook | Flow |
| 🟢 ****Pre-Arrival**** | 1-14 days before check-in | Pre-Arrival flow sends upsell offers (room upgrades, dining, spa) | Flow |
| ⬜ ****Arrival Day**** | Checks in | Not yet enabled → **unlocked in Run** | — |
| ⬜ ****Post-Stay**** | Checks out | Not yet enabled → **unlocked in Walk** | — |
| 🟢 ****Lapsed**** | No booking in 6–12 months | Winback flow fires automatically | Flow |
| 🟢 ****All Guests**** | Broad audience outreach | Seasonal promotions, VIP perks, and re-engagement sends to the right segments | Campaign |

---

# ****Walk****

**This section is for teams who have completed the Crawl stage and are ready to get more out of their data. The focus here is understanding performance, reaching the right guests with more precision, and driving direct bookings.**

## ****Reporting****

Klaviyo functions as a unified data platform. It is easy to set up core hotel reports within the app:

- Set up key hotel reports →
  - The [Mews](https://help.klaviyo.com/hc/en-us/articles/47194724598555) and [Cloudbeds](https://help.klaviyo.com/hc/en-us/articles/47187823602459) help guides show how to set up hotel reports based on ****Room Night**** event metrics.
    - **Note: If you are using Guesty, these event metrics are not yet available.**
- View revenue reports →
  - Klaviyo tracks revenue attributed to each campaign and flow automatically when a guest clicks through and completes a booking. To see overall revenue performance:
    - Navigate to ****Analytics**** > ****Dashboards**** > ****Business review****.
    - Track attributed revenue, orders, and conversion rates.

## ****Advanced Segments****

- Set up an OTA bookers segment →
  - Mews →
    - OTA bookings arrive via the channel manager and are stamped with an `Origin` of `ChannelManager`. To build the segment:
      - Navigate to ****Audience > Lists & Segments > Create new segment****.
      - Name the segment (e.g., "OTA Bookers").
      - Set the definition to: ****What someone has done**** > ****Confirmed Reservation (Mews)**** > ****at least once**** > ****over all time****
      - Click ****Add filter**** and select: ****where**** > ****Origin**** > ****equals**** > ****ChannelManager****
      - Click ****Create segment****.
      - **Optional: To target guests who booked through a specific OTA (e.g., Booking.com), add a second filter:** ******where****** **>** ******TravelAgency****** **>** ******equals****** **>** ******[OTA name]********. Note that** `TravelAgency` **is only populated for channel manager bookings, so this filter works alongside the** `Origin` **filter above.**
  - Cloudbeds →
    - The booking source is captured in the `Source` property on the Confirmed Reservation event. To build the segment:
      - Navigate to ****Audience > Lists & Segments > Create new segment****.
      - Name the segment (e.g., "OTA Bookers").
      - Set the definition to: ****What someone has done**** > ****Confirmed Reservation (Cloudbeds)**** > ****at least once**** > ****over all time****
      - Click ****Add filter**** and select: ****where**** > ****Source**** > ****does not equal**** > ****Direct****
      - Click ****Create segment****.
      - **Optional: If you want to target a specific OTA, change the filter to** ******Source****** **>** ******equals****** **>** ******[OTA name]****** **(e.g., "Booking.com").**
  - Guesty →
    - The booking channel is captured in the `Source` property on the Confirmed Reservation event. To build the segment:
      - Navigate to ****Audience > Lists & Segments > Create new segment****.
      - Name the segment (e.g., "OTA Bookers").
      - Set the definition to: ****What someone has done**** > ****Confirmed Reservation (Guesty)**** > ****at least once**** > ****over all time****
      - Click ****Add filter**** and select: ****where**** > ****Booking Source**** > ****does not equal**** > ****Direct****
      - Click ****Create segment****.
      - **Optional: To target a specific channel (e.g., Airbnb or Booking.com), change the filter to** ******Source****** **>** ******equals****** **>** ******[channel name]********.**

## ****Advanced Flows****

These flows require a bit more setup but tend to have a strong ROI because they reach guests at highly personal moments:

- Set up a post-stay review request flow →
  - Go to ****Flows > Create Flow**** and filter by your PMS to find the pre-built ****Reservation Check Out**** flow.
  - Set the trigger to the ****Reservation Check Out**** event.
  - Add a single email that sends 24 hours after checkout, thanking the guest and including direct links to your preferred review platforms (Google, TripAdvisor, etc.).
- Set up a birthday or stay anniversary flow →
  - Go to ****Flows > Create Flow > Build your own****.
  - Select the ****Date property**** trigger and choose the relevant date field (birthday from the guest profile, or their first check-in date).
  - Add an email with a personalized offer (e.g., complimentary upgrade, F&B credit, or a special rate) that expires within 30 days to create urgency.
  - **Note: Birthday flows require that guest birthday data is being synced from your PMS. Confirm this is populating on guest profiles before setting up the flow.**

## ****Advanced Campaigns****

- Set up a direct booking campaign →
  - Target guests who previously booked via an OTA and offer them an incentive to book direct next time (e.g. early check-in, discounted rate, etc.). Use your **OTA Bookers** segment for this.
  - Since OTAs charge 15-30% commission, you can pass some of that savings on to the guest as a perk while still coming out ahead on every direct booking.
- Set up a first-stay-to-repeat campaign →
  - Set up a campaign to encourage people who stayed for the first time to return.
  - Use your auto-created **First time customers** segment as the audience.
  - Send 2-4 weeks after checkout with a personalized incentive to return: a rate discount, a room upgrade, or early access to a package.
  - Exclude the **Current & Future Guests** segment so you don't send to guests who have already rebooked.
- Set up a high-value guest campaign →
  - Target guests who have paid above-average nightly rates and treat them accordingly — think early access to new packages, room upgrade offers, or a personal note from the GM.
  - **For Mews and Cloudbeds only:** Use the Room Night event data from your reporting dashboards (set up above) to determine your average nightly rate, then build a segment:
    - Navigate to ****Audience > Lists & Segments > Create new segment****.
    - Name the segment (e.g., "High-Value Guests").
    - Set the definition to: ****What someone has done**** > ****Confirmed Room Night**** > ****at least once**** > ****over all time****
    - Click ****Add filter**** and select: ****where**** > ****Value**** > ****is greater than**** > ****[your average nightly rate]****
    - Click ****Create segment****.

---

## ****Your Guest Journey After Walk****

**New touchpoints unlocked in Walk are marked 🟢. Previously enabled touchpoints are marked ✅.**

| ****Journey Stage**** | ****Guest Action**** | ****How Klaviyo Engages**** | ****Type**** |
| --- | --- | --- | --- |
| ✅ ****Discovers website**** | Visits your hotel website | Sign-up form → Welcome Series | Form + Flow |
| ✅ ****Books**** | Confirms a reservation | Reservation Confirmation flow | Flow |
| ✅ ****Cancels**** | Cancels a reservation | Cancellation win-back flow | Flow |
| ✅ ****Pre-Arrival**** | 1–14 days before check-in | Pre-Arrival flow (upsell) | Flow |
| ⬜ ****Arrival Day**** | Checks in | Not yet enabled → **unlocked in Run** | — |
| 🟢 ****Post-Stay**** | Checks out | Review request email fires 24 hours after checkout; return incentive fires at day 7 | Flow |
| 🟢 ****Birthday / Anniversary**** | Guest's birthday or stay anniversary | Personalized offer email with expiring incentive | Flow |
| ✅ ****Lapsed**** | No booking in 6–12 months | Winback flow | Flow |
| ✅ ****All Guests**** | Broad audience outreach | Seasonal, VIP, re-engagement campaigns | Campaign |
| 🟢 ****OTA Bookers**** | Previously booked via an OTA | Direct booking incentive campaign | Campaign |
| 🟢 ****First-Time Guests**** | Completed their first stay | Second-stay incentive campaign (sent 2–4 weeks post-checkout) | Campaign |
| 🟢 ****High-Value Guests**** | Paid above-average nightly rate | Premium offer campaign (upgrades, exclusive packages) | Campaign |

---

# ****Run****

**This section is for teams who have completed the Crawl and Walk stages and are ready to operate like best-in-class hotel marketers. The focus here is personalization at scale, multichannel messaging, and paid media amplification.**

## ****Personalization****

Klaviyo's dynamic content blocks let you show different content to different guests within the same email — no separate sends required:

- Add dynamic content to your templates →
  - In the template editor, use ****conditional content blocks**** to show different sections based on guest properties. Examples:
    - Show a room upgrade offer only to guests who have never stayed in a suite (filter by room type from past Confirmed Reservation events).
    - Show a loyalty acknowledgment ("Welcome back!") only to guests in the **VIP customers** segment.
    - Show property-specific imagery and offers when you manage multiple properties (filter by `PropertyName`).
  - Learn more in Klaviyo's [personalization help guide](https://help.klaviyo.com/hc/en-us/articles/115005082927).

## ****A/B Testing****

Once your forms, flows, and campaigns are running, small improvements compound significantly at scale:

- Create an A/B testing plan →
  - Follow this [A/B testing roadmap guide](https://www.klaviyo.com/blog/how-to-build-an-ab-testing-roadmap) to create a test plan that makes sense for your business.
- Run A/B tests on your forms →
  - Follow this [help guide](https://help.klaviyo.com/hc/en-us/articles/360045462071) for A/B testing forms.
- Run A/B tests on your campaigns →
  - Follow this [help guide](https://help.klaviyo.com/hc/en-us/articles/115005228148) for A/B testing campaigns.
- Run A/B tests on your flows →
  - Follow this [help guide](https://help.klaviyo.com/hc/en-us/articles/6960371049115) for A/B testing flow messaging.

## ****SMS & WhatsApp****

Adding SMS to your flows dramatically increases engagement for time-sensitive messages. Klaviyo supports SMS natively alongside email in the same flows, so you don't need a separate tool:

- Set up SMS →
  - Navigate to ****Settings > SMS**** to configure your sending number and opt-in compliance settings.
  - Once set up, add SMS steps directly inside your existing flows. The highest-value SMS touchpoints for hotels are:
    - ****Day-of check-in:**** A text the morning of arrival with a mobile check-in link, directions, parking info, and/or check-in time.
    - ****Pre-Arrival:**** A short text 1-2 days before check-in with a room upgrade offer or a preview of on-property amenities.
    - ****Post-Stay:**** A review request text the morning after checkout (short, direct, one link).
    - ****Flash sales:**** A last-minute availability offer sent to your **Winback opportunities** segment on a slow day.
  - Learn more in Klaviyo's [SMS getting started guide](https://help.klaviyo.com/hc/en-us/articles/4404274419355).
- Set up WhatsApp →
  - Navigate to ****Settings > WhatsApp**** and click ****Connect to WhatsApp**** to get started.
  - Setup requires a Meta Business Account and a dedicated phone number (this cannot be the same number used for SMS). Meta may take up to several hours to verify new accounts.
  - Once connected, add WhatsApp steps directly inside your existing flows alongside email and SMS. The use cases largely mirror SMS: pre-arrival reminders, day-of check-in messages, and post-stay review requests.
  - Learn more in Klaviyo's [WhatsApp getting started guide](https://help.klaviyo.com/hc/en-us/sections/40111669484187) and [how to connect your WhatsApp Business account](https://help.klaviyo.com/hc/en-us/articles/40111819732635).
    - **Note: As of April 2025, Meta has paused support for WhatsApp marketing message templates sent to US phone numbers, though transactional messages are still allowed (e.g. booking confirmations, check-in notifications, etc.). Marketing messages to non-US numbers are unaffected.**

## ****Additional Integrations****

### Ad integrations

The segments you've built in Klaviyo can be pushed directly to Google, Meta, TikTok, and Pinterest — letting you reach the same audiences with paid advertising and creating a unified owned + paid strategy.

- Connect your ad platforms →
  - Go to ****Integrations > Explore apps**** and install the Google Ads, Meta Ads, TikTok Ads, or Pinterest Ads integration.
  - Once connected, navigate to any segment and enable the ****Sync to ads**** option to push that audience to your ad platform.
  - The highest-value use cases for hotels are:
    - ****Retargeting lapsed guests**** — serve display or social ads to your **Winback opportunities** segment before (or alongside) your winback email campaign.
    - ****Lookalike audiences**** — upload your **VIP customers** segment to Meta or Google and let the platform find new guests who look like your best ones.
    - ****Suppression**** — exclude your **Future Guests** segment from paid acquisition campaigns so you don't pay to acquire someone who already has a booking.

### Restaurant & spa integrations

Connecting your restaurant and spa platforms enriches each guest's Klaviyo profile with on-property spend data — giving you a complete picture of the guest beyond just the room booking, and enabling highly personalized upsell and retention messaging.

- Connect your restaurant platforms (if applicable) →
  - Go to ****Integrations > Explore apps**** and search for your reservation or POS platform (e.g. OpenTable).
    - If you don't find it there, please send an email to [Arjun Madgavkar](mailto:arjun.madgavkar@klaviyo.com) and we can consider it for our roadmap.
  - Once connected, dining reservation events will appear on guest profiles, letting you:
    - ****Pre-arrival upsell**** — in your Pre-Arrival flow, add a conditional block that shows a restaurant CTA only to guests who **haven't** made a dining reservation for their stay.
    - ****Post-dining follow-up**** — trigger a flow after a dining visit to request a review or share a return offer.
    - ****High-value diner campaigns**** — build a segment of guests who dine on-property frequently and treat them as VIPs with exclusive F&B offers or early access to special menus.
- Connect your spa platforms (if applicable) →
  - Go to ****Integrations > Explore apps**** and search for your spa or wellness booking platform (e.g. Mindbody).
    - If you don't find it there, please send an email to [Arjun Madgavkar](mailto:arjun.madgavkar@klaviyo.com) and we can consider it for our roadmap.
  - Once connected, spa booking events will appear on guest profiles, letting you:
    - ****Pre-arrival upsell**** — similar to dining, add a conditional block in your Pre-Arrival flow that promotes spa offers to guests who haven't yet booked a treatment.
    - ****Repeat spa guest campaign**** — identify guests who have booked spa treatments across multiple stays and send them exclusive offers (e.g., a package deal or early booking access).
    - ****Lapsed spa guests**** — build a segment of guests who have used the spa in the past but not in the last 12 months, and target them with a re-engagement offer tied to their next stay.

### E-commerce integrations

If you sell merchandise — branded goods, local products, gift sets, or anything else — connecting your e-commerce platform brings purchase and browse data into Klaviyo alongside your reservation data, letting you drive incremental revenue before, during, and after each stay.

- Connect your e-commerce platforms (if applicable) →
  - Go to ****Integrations > Explore apps**** and search for your e-commerce platform (e.g. Shopify).
  - Once connected, purchase and browse events will appear on guest profiles, letting you:
    - ****Merchandise upsell in Pre-Arrival**** — add a conditional block in your Pre-Arrival flow promoting relevant products (e.g., branded robes, local goods, gift sets) to guests who haven't yet made a purchase.
    - ****Post-stay purchase follow-up**** — after checkout, trigger a flow promoting your online shop to guests while the experience is still fresh (e.g., "Take a piece of [Property Name] home with you").
    - ****Repeat buyer campaigns**** — identify guests who have purchased merchandise and send them early access to new products, seasonal collections, or exclusive bundles.

### Other integrations

Klaviyo has hundreds of integrations beyond the ones covered above — from design tools like Canva to event management apps like Eventbrite. As your marketing program matures, connecting additional platforms helps ensure Klaviyo reflects the full picture of how guests interact with your property.

- Connect other platforms →
  - Go to ****Integrations > Explore apps**** and search for the apps that make sense for your business.

---

## ****Your Complete Guest Journey****

**This is the full picture — every stage of the guest journey, and how Klaviyo is now engaging at each one. New touchpoints unlocked in Run are marked 🟢.**

| ****Journey Stage**** | ****Guest Action**** | ****How Klaviyo Engages**** | ****Type**** |
| --- | --- | --- | --- |
| 🟢 ****Discovery**** | Browsing online before visiting your site | Lookalike ads (Meta/Google) built from your VIP guest segment attract new high-value guests | Paid Ads |
| 🟢 ****Consideration**** | Visited your site but didn't book | Retargeting ads re-engage lapsed guests across social and display | Paid Ads |
| ✅ ****Discovers website**** | Lands on your hotel website | Sign-up form captures contact info → Welcome Series nurtures toward first booking | Form + Flow |
| ✅ ****Books**** | Confirms a reservation | Reservation Confirmation flow (now with personalized dynamic content by guest type) | Flow |
| ✅ ****Cancels**** | Cancels a reservation | Cancellation win-back flow | Flow |
| ✅ ****Pre-Arrival**** | 1–14 days before check-in | Pre-Arrival email with personalized upsell + 🟢 SMS upgrade offer 1–2 days out | Flow (Email + SMS) |
| 🟢 ****Arrival Day**** | Day of check-in | SMS with mobile check-in link sent morning of arrival | SMS |
| ✅ ****Post-Stay**** | Checks out | Review request email (24hr) + 🟢 SMS review request; return incentive at day 7 | Flow (Email + SMS) |
| ✅ ****Birthday / Anniversary**** | Guest's birthday or stay anniversary | Personalized offer email with expiring incentive | Flow |
| ✅ ****Lapsed**** | No booking in 6–12 months | Winback flow + 🟢 retargeting ads running in parallel | Flow + Paid Ads |
| ✅ ****OTA Bookers**** | Previously booked via an OTA | Direct booking incentive campaign | Campaign |
| ✅ ****First-Time Guests**** | Completed their first stay | Second-stay incentive campaign | Campaign |
| ✅ ****High-Value Guests**** | Paid above-average nightly rate | Premium offer campaign | Campaign |
| ✅ ****VIP Guests**** | More than 5 confirmed reservations | Exclusive loyalty campaign | Campaign |