---
id: "115000976672"
title: "How Klaviyo billing works"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115000976672-How-Klaviyo-billing-works"
section: "How Klaviyo bills"
category: "Account & billing"
category_slug: "account-billing"
klaviyo_updated: "2026-05-15T10:18:29Z"
language: "en"
---
Only Owners and Admins can edit Klaviyo billing settings.

Learn how Klaviyo bills customers for Profiles and Emails, Mobile Messaging, Reviews, Advanced Klaviyo Data Platform (formerly “CDP”), Marketing Analytics, Customer Hub, Helpdesk, and Customer Agent.

This article is only for customers who are not using [manual billing](https://help.klaviyo.com/hc/en-us/articles/18745921973915) (i.e., are on a contract).

## View & change your billing plan

To view your plans, follow these steps:

1. Click your organization’s name in the bottom left corner.
2. Click ****Billing****.

   Once in the **Overview** tab, you’ll be able to view the plans you are currently paying for. The Monthly Total reflects the upcoming monthly total you will pay if you do not make any changes to your account before your billing cycle renews.

   You can also view the cost of other Klaviyo plans when changing plans. To do so:
3. Select your account name in the bottom left.
4. Navigate to ****Billing > Change plan****.
5. Open the dropdown under a plan type to view all the plans.
6. Select a plan to view its cost.

### When do billing plans renew?

All Klaviyo plans renew automatically on a monthly basis. The exact date depends on your personal billing cycle:

- Free plans always renew on the first of the month.
- Paid plans renew on the date your account began to pay for Klaviyo.

To view when your billing cycle renews:

1. Click your organization name in the lower-left corner.
2. Click ****Billing****.
3. Review the dates for your cycle, which are at the top of the page in the **Overview** tab.

Beginning on October 8, 2025, Klaviyo aligned customers’ usage cycles with their billing cycle. Your billing cycle is based on when you first signed up for a paid plan with Klaviyo, which you can view on the [**Billing Overview**](https://www.klaviyo.com/settings/billing/overview)page. Historically, your usage cycle ended at midnight on that same day. With this new streamlined approach, your usage cycle and billing cycle will share the same date and time. Only the time is changing, the billing date remains the same, and there is no action needed on your part.

Your billing date remains the same and there is nothing that you need to do.

****What is my billing cycle?****

A billing cycle is the 30-day interval of time from the end of one billing, or invoice, statement date to the next billing statement date. Your billing cycle is based on when you first signed up for a paid Klaviyo plan, and is visible on your overview page.

****Will my billing date or time change?****

No, your billing date and time remains the same. However, your usage cycle will now align with your billing cycle to ensure consistency.

****Where can I see my billing date and time?****

You can see your billing date and time in the **Billing Overview** page next to **Billing Cycle**.

****Is there anything I need to do?****

No, the change will occur automatically.

****Can I change my billing cycle?****

No, this is not supported right now.

****Why are you making this change now?****

We are always working to streamline our customer experiences. This particular change improves backend operations with little to no impact on customers.

****Can I opt out of this change?****

No, the change will occur automatically.

****What happens if my usage period is longer or shorter this month?****

The change this month will be less than a day and should not impact usage.

## Understanding Klaviyo's Products & Plan Types

All Klaviyo plans are billed on a monthly basis, which starts the day you begin a paid plan.

There are 9 products available:

- Klaviyo Marketing
  - Profile and Email
  - Mobile Messaging (SMS, MMS, Whatsapp, & other mobile channels)
  - Reviews
- Klaviyo Service
  - Customer Hub
  - Customer Agent
  - Helpdesk
- Klaviyo Data Platform
  - Advanced Klaviyo Data Platform, or KDP (previously called CDP)
- Klaviyo Analytics
  - Marketing Analytics
- Klaviyo Success

### Profile and Email (i.e., the base plan)

Profile and Email plans are based on both the number of:

- [Active profiles](https://help.klaviyo.com/hc/en-us/articles/24263920096027) in your account.
- Emails sent during the current billing cycle

Your billing plan must cover the number of active profiles in your account. If not, you will be moved to a profile-compliant plan as of the next billing cycle. To avoid changing plans due to profile enforcement, you will need to reduce your active profile count to be within your current plan's limits at least 24 hours before your next billing cycle.

****What are active profiles?****

Any profile, regardless of consent status, that can be emailed through Klaviyo is considered an active profile. This includes your subscribers and those who are added by general engagement (such as sharing their email on a store’s checkout page but not actually opting in).

This means that if you have 7,000 active profiles, your plan must allow for at least that amount.

Your emails can be to any of your active profiles. You can send an equal amount across all of your profiles (10 to each), or send more to certain groups and less to others (e.g., 100 to group A, and 1 to group B).

Klaviyo charges for any messages that leave the system: any received or bounced emails count toward your plan limit, but skipped emails do not.

### Mobile Messaging

The Mobile Messaging plans are dependent entirely on [message credits](https://help.klaviyo.com/hc/en-us/articles/13502982552347); i.e., how many mobile messages you want to send per month.

Note that the number of credits required when sending text messages depends on 3 key factors:

- Where the subscribers are located (US, UK, AUS, etc)
- The type of messages you send (SMS, MMS, or WhatsApp)
- The number of message segments

****What is a message segment?****

Text messages allow for a certain number of characters:

- SMS has a limit of 160 characters normally, but only 70 characters when there's an emoji or special character.
- MMS always allows up to 1600 characters.
- WhatsApp messages have a character limit of 168 characters.

If you exceed this character amount for a send, your text is broken into message segments so it can be delivered.

When a text contains multiple message segments, it still shows a single message on the recipient’s phone.

Additionally, to render these segments in the correct order, an invisible header of about 7 characters is added to all message segments. This means that rather than 160 characters, you'll instead have a 153 character limit.

As an example, say you want to send a single SMS to 100 people: 50 to the United States and 50 to Canada. The table below breaks down the credit cost:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ****Country**** | ****Credit**** | ****# or recipients**** | ****Message segments**** | ****Total**** |
| United States | 1 | 50 | 1 | 1 x 50 x 1 = 50 |
| Canada | 3 | 50 | 1 | 3 x 50 x 1 = 150 |
|  | | | | 50 + 150 = ****200**** |

See this article for a full breakdown of [credits by country](https://help.klaviyo.com/hc/en-us/articles/13502982552347). Note that while skipped and inbound messages do not cost credits, [failed deliveries](https://help.klaviyo.com/hc/en-us/articles/360039239172) do. Further, short codes are billed separately from the Mobile Messaging plan.

#### WhatsApp

Klaviyo follows Meta’s billing model: charging per template instead of per conversation. This means that there is a charge for any delivered marketing or utility/transactional template message.

In Klaviyo, WhatsApp messages are billed as credits using the same system as your overall Mobile Messaging Plan. After you purchase a plan with credits, you can use all of them for SMS, MMS, WhatsApp, or any combination.

****How many credits are WhatsApp messages?****

Like an SMS message, the credit per WhatsApp message varies based on:

- The country you’re sending to.
- The type of message it is:
  - Marketing (also called “promotional”)
  - Transactional (also called “utility”)

![](https://klaviyo.zendesk.com/hc/article_attachments/41423376396187)

If your country is not listed in the table above, it falls under one of the following regions, which were grouped by Meta.

****How can I purchase credits for WhatsApp?****

To begin sending WhatsApp messages through Klaviyo, you must have Mobile Messaging credits in your account.

For contracted customers (those who are [manually billed](https://help.klaviyo.com/hc/en-us/articles/18745921973915)), reach out to your Klaviyo success representative to add credits to your plan. If you have credits already, you can use them to send WhatsApp messages.

If you’re not on a contract, you can get credits at any time:

- If you have an Mobile Messaging plan already, simply start using your credits to send WhatsApp messages or [get more credits by upgrading](https://help.klaviyo.com/hc/en-us/articles/8356575957275).
- If you don’t have an Mobile Messaging plan, you must [set up Mobile Messaging](https://help.klaviyo.com/hc/en-us/articles/4404274419355) in Klaviyo.

###

### Klaviyo Reviews

Klaviyo Reviews is only available for Shopify and WooCommerce stores.

By using this product, you can collect, display, and manage your product reviews.

Klaviyo Reviews pricing is based on how many orders are placed on your website each month.

****What counts as an “order”?****

"Order" means when a "Ready to review" event is generated in the Klaviyo platform based on Customer's configuration. Each **Ready to review** event counts toward your Klaviyo reviews plan. A **Ready to review** event is triggered when:

- A certain number of days have elapsed since the order was fulfilled or delivered, depending on your settings, and
- The order is eligible for reviews

****Can I exclude orders from being eligible for reviews?****

You can [make a product, customer, or order ineligible for reviews](https://help.klaviyo.com/hc/en-us/articles/16684841274139) by applying the **klaviyo\_reviews\_exclude** tag to that item in your e-commerce platform.

****Will I be charged for reviews that are ineligible?****

Orders that are ineligible for review do not count toward your plan limit. The **klaviyo\_reviews\_exclude** tag does not apply retroactively (i.e., if a review request has already been sent, applying this tag cannot undo that action and it will still count toward your Klaviyo reviews billing plan).

###

### Customer Hub

Customer Hub delivers a personalized customer accounts experience by combining personalization, merchandising, and self-service support into one on-site surface for shoppers.

Customer Hub is priced based on your active profile count, starting at $20 per month for up to 10,000 active profiles.

###

### Helpdesk

Helpdesk brings AI and human agents into a unified workspace across email, chat, SMS, WhatsApp and social.

Helpdesk is priced based on the amount of shopper-initiated tickets opened, starting at $10 per month for up to 50 tickets.

A Ticket is a shopper- initiated message or, where applicable, a “Customer Agent”- initiated support escalation, sent through a supported channel that requires human agent support. A Ticket becomes billable upon creation.

Helpdesk has AI spam detection, which reviews incoming messages from your customer and auto flags any tickets on any channel that are not legitimate customer outreach (iMessage Auto Responder, email OOO responses, spam/phishing attempts from bad actors). these are not charged as tickets.

****How is a ticket defined?****

A Ticket is a shopper- initiated message or, where applicable, a “Customer Agent”- initiated support escalation, sent through a supported channel that requires human agent support. A Ticket becomes billable upon creation.

****How long can tickets remain open?****

Each Ticket remains open until it is automatically closed at a time period of 48 hours, or manually closed by the Customer, or closed through other rules-based automations, whichever occurs first.

****What happens when tickets are closed?****

Once a Ticket has closed, if the same shopper initiates another message that requires human agent support, a new Ticket will be created. Customers are separately responsible for any additional service usage that occurs in connection with a Ticket (e.g., SMS or email sends).

****Am I charged for Spam tickets created in Helpdesk?****

No! We do not charge for tickets in your spam folder of Helpdesk. If you choose to mark it as not spam, it will not be charged either.

###

### Customer Agent

Customer Agent is a 24/7 AI assistant that helps before and after the purchase—answering questions, recommending products, and resolving issues instantly. Customer agent is currently available on SMS, web chat, email, and coming soon to WhatsApp and RCS.

Customer Agent is priced based on the amount of shopper-initiated conversations resolved, starting at $50 per month for up to 75 conversations. A Conversation is a shopper-initiated conversation on a supported channel that is handled end-to-end by Klaviyo’s ”Customer Agent."

****How long can conversations remain open?****

A Conversation becomes billable when the “Customer Agent” provides a response and 48 hours have passed with no response from the shopper.

****What if the customer agent does not resolve the conversation?****

Conversation consumption excludes conversations that are escalated to a human agent (including Helpdesk if applicable). You are separately responsible for any other Service consumption alongside an AI Conversation (e.g. Mobile messages or email).

### Marketing Analytics

Marketing Analytics provides actionable customer and product insights that enable you to enrich your marketing strategy with additional data and use cases for better personalization. Marketing Analytics is not included in Klaviyo’s base email and profiles plan, and a subscription is required to access the associated functionality.

Marketing Analytics is priced based on your active profile count, starting at $100 per month for up to 13,500 active profiles.

****What are active profiles?****

Any profile, regardless of consent status, that can be emailed through Klaviyo is considered an active profile. This includes your subscribers and those who are added by general engagement (such as sharing their email on a store’s checkout page but not actually opting in).

This means that if you have 7,000 active profiles, your plan must allow for at least that amount.

****How can I add Marketing Analytics to my account?****

If you currently have an Advanced KDP plan, you must first cancel this before you can add Marketing Analytics. See [how to cancel a plan in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/1260805595309).

For everyone else, or once you cancel the KDP plan, simply follow the steps to [adding or changing a plan](https://help.klaviyo.com/hc/en-us/articles/8356575957275).

### Advanced Klaviyo Data Platform (previously called CDP)

Advanced Klaviyo Data Platform (KDP) was previously called CDP. From here, we’ll refer to it as “Advanced KDP.”

Advanced KDP is not included in Klaviyo’s base email and profiles plan, and a subscription is required to access the associated functionality.

Since Advanced KDP allows you to better understand all customers (not just the ones you send to), the plans are based on total profiles in your Klaviyo account.

Total profiles comprises any profile that is stored and tracked in Klaviyo, including:

- Subscribers (email, mobile messaging, push, etc.)
- Suppressions
- Non-subscribers

You can view your profile count by going to ****Audience > Profiles****.

****Why Advanced KDP is based on total profiles and not active profiles****

With Advanced KDP, you are able to activate, transform, and analyze all profiles as well as the data associated with them. It doesn’t simply cover the profiles you’re marketing to (i.e., your active profiles).

This functionality helps you better understand your customers, their behaviors, and trends in order to refine your marketing and business strategies.

Here are some ways you can get smarter across their entire customer base, even if they are suppressed:

- Identify ways and segments of customers to re-engage by reviewing historical trends through RFM analysis and audience performance comparison.
- Decrease your unsubscribe rate by identifying patterns in opt-out behavior via funnel analysis.
- Personalize on-site experiences, regardless of subscription status, by using the [Group membership API](https://help.klaviyo.com/hc/en-us/articles/17760675787419).
- Transform profile properties, promote data hygiene, and create a customer source of truth for trusted analysis via data transformation.

## Starting 10/24/25: Proration for Customer Hub, Marketing Analytics, and Advanced Klaviyo Data Platform

Beginning on October 24, 2025, purchases of Customer Hub, Marketing Analytics, and Advanced Klaviyo Data Platform will be prorated. Proration will happen in the following situations:

- If you purchase one of these plans for the first time in the middle of your billing cycle
- If you upgrade one of these plans in the middle of their billing cycle

Your prorated payment will be calculated according to the amount of time remaining in your billing cycle. For example, if you purchase a $100 Marketing Analytics plan halfway through your billing cycle, you will only pay $50 for that cycle. In the following cycle, you will pay the full $100 for your plan.

You will see the prorated charge reflected on the invoice that is emailed to you. (You can also download these invoices in your Klaviyo account, under Billing Settings.) Proration will automatically apply starting on October 24, 2025: there is nothing that you need to do in order to receive prorated charges for Customer Hub, Marketing Analytics, and Advanced Klaviyo Data Platform.

## What happens if you reach your plan’s limits

What happens when you reach your plan’s limits depends on what type of product it is.
Consumption-based products like Email, Mobile Messaging, Helpdesk, and Customer Agent operate similarly when overages are incurred. Meanwhile, products like Advanced KDP, Marketing Analytics, and Customer Hub are all based on Active Profiles, which grows as your business grows. These 3 products operate similarly with respect to overages.

### Email and Mobile Messaging

For marketing products, what happens varies by which limit you reached (i.e., profile or send) as well as your product type:

#### Profile limit

When you exceed your plan’s active profile limit, Klaviyo does not stop you from sending or adding additional profiles. However, you are notified and will be moved to a higher plan tier (one with enough profiles) as of your next billing cycle. Profile enforcement is different from the **Automatically upgrade** setting, which is an optional setting that moves you to the next tier when you reach your message limit.

If you don’t want to be upgraded, you can [manage your active profiles to stay within your current plan limits](https://help.klaviyo.com/hc/en-us/articles/24312135764251).

If you are on the free Profiles & Email plan and are over your profile limit, you won’t be upgraded but you also cannot send emails (or set flow emails live) until you are under your active profile limit.

#### Send or credit limit

When your account reaches your plan’s sending limits (i.e., emails or mobile messaging credits), there are 3 options you can choose from. You can:

- Flexible overage plans (i.e., use flexible sending), which provides the next tier’s amount of sends in full. The cost to flex is based on the unit pricing of your base plan (the plan you started the month on).
- Upgrade (manually or via auto-upgrade) to a higher-tiered plan. Upgrading is generally more economical than flex sending if your upgrade needs are consistent.
- Stop all sending until the next billing cycle.

Want more information about these options? Jump ahead to this [billing preferences section](#h_01JM3GR9TC6HHCTQKCCGJ0DTBV).

![](https://klaviyo.zendesk.com/hc/article_attachments/34136600769435)

### Helpdesk & Customer Agent

Helpdesk and Customer Agent plans are similar to Email and Mobile Messaging plans, but Helpdesk is based on tickets and Customer Agent is based on conversations.

For Service products your ability to use these products does not stop when your plan limit is reached. When your purchase Customer Agent or Helpdesk, you are committing to a minimum spend on this product with overages for any additional usage.

There is a usage fee for exceeding your plan's limits. Upon purchasing Helpdesk or Customer Agent, you will be automatically enrolled into Flexible Overages as your default billing preference option for any overages that you incur. You may change this billing preference at any time to Auto-Upgrade in ****Billing > Billing Preferences.****

****You must be enrolled in either Flexible Overages or Auto-Upgrade**** in order to continue using Helpdesk and Customer Agent. If you wish to stop accruing overages for these products, you may turn Customer Agent or Helpdesk off within the product or cancel your plan(s).

### Reviews

Review plans are similar to email and SMS plans, but are based on orders from your store rather than messages.

If your plan allows you 20 orders, you can send review requests for only those orders. When you reach your plan’s limit, you can either upgrade manually or pause sending review requests until your billing cycle renews.

### Advanced Klaviyo Data Platform (KDP)

Advanced KDP plans are priced so that you pay based on the selected plan and for overages beyond that plan.

There is a usage fee for exceeding a plan’s limits. The fee is defined as: the number of profiles that exceed your current tier (in 1,000s) multiplied by the price per 1,000 profiles at the current tier.

****Example of usage fee****

Say that the company Funky T-shirts pays $4,765 per month for a Advanced KDP plan that allows 1 million profiles. However, the next month, their profile count grows to 1.52 million, exceeding their plan by 520,000.

Instead of forcing Funky T-shirts to upgrade to the next tier (2 million profiles at $9,100), they pay a usage fee that is:

- Number of 1,000 profiles that exceed the current tier: 520
  X
- Price per 1,000 profiles at the current tier: $4.77
  =
- Total usage fee: $2,480.40.

This means that between their plan ($4,765) and usage fee ($2,480.40), the total cost is $7,245.40. This is less than what Funky T-shirts would pay if they upgraded. Unlike with other products (where you pay before), this fee is billed after usage.

Generally, if you’re using less than 85% of the next tier up, it is more cost-efficient to incur the usage fee. Once you’re using 85% or more of the next tier, it’s better to upgrade.

The fee is applied to the next month’s invoice.

### Marketing Analytics

Marketing Analytics plans are priced based on active profiles, so your plan automatically upgrades or downgrades based on the number of active profiles in your account at the end of your billing cycle. Your plan is automatically upgraded at the start of the next billing cycle.

### Customer Hub

Customer Hub plans are priced based on active profiles, so your plan automatically upgrades or downgrades based on the number of active profiles in your account at the end of your billing cycle. Your plan is automatically upgraded at the start of the next billing cycle.

## Upgrading and downgrading your billing plan

You can upgrade or downgrade at any time during the billing cycle, but please note:

- Upgrading takes effect immediately and is permanent until you choose to downgrade.
  - Whenever you upgrade, the cost per message goes down, meaning you get a better deal as you go up tiers.
- Downgrading takes effect at the start of your next billing cycle.
  - You cannot downgrade to a plan if you have more active profiles than that lower-tiered plan allows.
  - Klaviyo does not issue refunds if you downgrade in the middle of a billing cycle, as stated in our [terms of service](https://www.klaviyo.com/legal/terms-of-service).
  - If you choose to downgrade, but then upgrade (either manually or automatically), the downgrade is canceled.
  - The only time downgrades take effect sooner than the next billing cycle is if you:
    - Cancel your plan(s).
    - Close your account and choose for it to take effect immediately.

![](https://fast.wistia.com/embed/medias/qumxpyj0de/swatch)

****How to change plans****

Note that if you're on the Advanced KDP plan and want to change to Marketing Analytics, you must [cancel your Advanced KDP plan](https://help.klaviyo.com/hc/en-us/articles/1260805595309) before you can add Marketing Analytics.

1. Select your account name in the lower left.
2. Click ****Billing****.
3. Select ****Change plan****.
4. Open the dropdown for the plan type you want to change.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34136574671515)
5. Choose your plan.

   - To downgrade your email and profiles plan, your account must have fewer active profiles than the plan you want to change to.
6. Click ****Continue to payment**** to confirm the plan change.

Klaviyo also provides several settings you can use to automatically switch plans:

|  |  |  |
| --- | --- | --- |
| ****Klaviyo setting**** | ****Based on**** | ****Available for**** |
| \*[Automatically upgrade](#h_01JM3GR9TCDT36QKB89ME9MC5N) (also called auto-upgrade) | # Overage units (Messages, Tickets, Conversations) | Mobile Messaging  Email and profile  Helpdesk  Customer Agent |
| [Flexible sending](#h_01JM3GR9TCAB23CNFRHGJJY7EC) | # Overage units (Messages, Tickets, Conversations) | Email and profile  Mobile Messaging (only for accounts on $495+ plans)  Helpdesk  Customer Agent |
| \*\*[Auto-downgrade](#h_01JM3GR9TCSJS7V8E62Y7Y8MGY) | Profiles | Email and profiles only when using flexible sending |
| Manually upgrade (the **None** option) | Anything | All plans, except Marketing Analytics |

\* Both the Marketing Analytics as well as emails profiles are automatically upgraded based on profiles. However, this is not a setting you can turn off.

\*\* Auto-downgrading based on profiles happens automatically for Marketing Analytics and Customer Hub, so it’s not a setting you can turn on or off.

You can switch between these options at any time.

****How to choose a different upgrade/downgrade option****

1. Select your account name in the lower left.
2. Go to ****Billing > Preferences****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34136600772507)
3. Find the plan you want to change options for (e.g., email, Mobile Messaging, etc.).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34136574673819)
4. Open the dropdown.
5. Select one of the following options to change what happens when that plan type reaches its plan limits:

   - ****None**** to stop sending or manually upgrade.
   - ****Automatically upgrade**** to enable auto-upgrade.
   - ****Flexible overages**** to flex plans.
6. Note the cost associated with upgrading or flexible sending.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34136600777115)
7. Click ****Update**** to save.

### Use flexible overages

Flexible sending is available for Email, Mobile Messaging, Helpdesk, and Customer Agent plans. Flexible sending is not available for Reviews, Advanced KDP, Marketing Analytics, and Customer Hub plans.

When you hit your plan’s limit while using flexible overages, it is a 1-time add-on of all of the profiles and messages included in the next highest tier without permanently upgrading your account. This way, you stay on your current plan and don’t need to worry about downgrading before the next billing cycle.

The amount it costs to flex is based on the unit cost of your current plan and the capacity in the following tier(s). Flexing is a 1-time purchase that includes all of the capacity in the next tier (credits for SMS, profiles and messages for email) at the unit rate of your current plan. This means that while there are no additional fees to flex, it generally costs more than upgrading, as upgrading makes you eligible for a reduced cost per unit with a higher volume.

You can check how much it will cost to flex either in the **Billing Preferences** tab or at checkout.

****Who is flexible overages best for?****

Flexible overages is best for people who occasionally need extra usage (e.g. sends) during the year and who want to go back to their original plan once these times are over. It is not optimal for those who are growing consistently and frequently need more profiles or messages throughout the year.

****Example of flexing up plans****

Say that Funky T-shirts pays $7,000 for an emails and profiles plan that allows 7,000 profiles and 70,000 emails. However, next month is Black Friday/Cyber Monday, and they’ll need to send 80,000 emails.

Rather than permanently upgrade their account, Funky T-shirts can flex up:

- Plan cost ($7,000) / number of emails (70,000) = current unit rate (0.1)
  X
- Difference in the number of emails for next tier (80,000) and current tier (70,000) = 10,000
  =
- Flex cost: $1,000

****When to upgrade vs. flex plans****

Flexing is typically more expensive than upgrading. When you flex plans, you are buying all of the profiles, sends, or credits of the next tier at the cost per message of your current tier. If you are frequently flexing plans, it can be more cost effective to upgrade.

Flexing is better if you don’t consistently exceed your plan’s limits. It’s also good for anyone who doesn’t want to worry about remembering to downgrade.

****What are unit rates?****

In Klaviyo, the unit rate is essentially the cost of 1 message. You can calculate unit rate by dividing the number of messages in a plan by its cost.

**cost of plan / # of messages**

#### Auto-downgrading based on profiles

Auto-downgrade is:

- Available for profiles plans only when using flexible sending
- Always on for Marketing Analytics & Customer Hub plans

You cannot auto-downgrade based on message sends.

You can choose to auto-downgrade your profiles and email plan in Klaviyo’s billing preferences page. Your plan will automatically downgrade to the lowest tier that can cover your active profile count 24 hours before the end of your billing cycle. The downgrade goes into effect for the next billing cycle.

### Automatically upgrade based on usage (also called auto-upgrade)

Auto-upgrading your plan limit is only available for the Profile & Email plan, Mobile Messaging plan, Helpdesk plan, and Customer Agent plan. It automatically moves you to the next tier when you reach your usage limit (mobile messages, email messages, tickets, or conversations). It does not apply when you reach your profile limit, since Klaviyo now enforces profiles.

Klaviyo automatically upgrades your plan based on profiles for the Profiles & Email plan as well as Marketing Analytics and Customer Hub plans. This is also known as Profile Enforcement.

|  |  |
| --- | --- |
| ****Available to auto-upgrade**** | ****Not available to auto-upgrade**** |
| Email | Reviews |
| Mobile Messages (SMS & more) | Advanced KDP |
| Helpdesk |  |
| Customer Agent |  |

This feature ensures you don’t hit monthly sending limits so that you can continue to send mobile messages, email, and automated flows unimpeded.

****What happens when I’m automatically upgraded?****

After you [turn on auto-upgrade](https://help.klaviyo.com/hc/en-us/articles/4405883690651):

1. When you either:

   - Reach your plan's message limits (e.g., if your plan allows for 2,000 emails, but you try to send more).
   - Schedule a campaign that will take you over your message limit for the current billing window.
2. Auto-upgrade moves you to the next plan up.
   Note: you can be auto-upgraded at any time in the billing cycle.
3. As soon as the account is upgraded, an email is sent to the owner informing them of this change.
4. Once you're on this next level of plan, you will stay there until you choose to downgrade, upgrade, or are auto-upgraded. You will not be auto-downgraded.

When you upgrade, you pay the difference between your base plan (i.e., the plan you entered the billing cycle with) and the plan you’re upgrading to during that first month.

It is recommended that you upgrade (rather than flexing) if you have flexed more than a few times a year, it can be more cost effective.

### Manually upgrade or stop sending: use the None option

If you want to manually choose when you upgrade or to stop sending when you reach your plan’s limits, you can set your billing upgrade preference to the **None** option. Go to ****Settings > Billing > Preferences.****

This means that you won’t be able to send any flow and campaign messages, and any messages scheduled during the current billing cycle will be canceled. However, if you decide to upgrade or flex plans, you can resume sending.

Note: The **None** option is only available for Email and Mobile Messaging (SMS) plans.

## Adjust credit card details

Klaviyo does not support multiple credit cards in a single account. If you purchase a plan with a different credit card than the one in your account, this changes the credit card on file. If your payment ever fails, the account Owner and [billing contact](https://help.klaviyo.com/hc/en-us/articles/1260805043069-) will be alerted via email.

For details on how to change the credit card on file, check out our article on how to [update your credit card information](https://help.klaviyo.com/hc/en-us/articles/115005232048). To see invoices and other details regarding your recent charges, select ****Billing > Payment History****.