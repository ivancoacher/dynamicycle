---
id: "19896802561307"
title: "PAR Punchh data reference"
source_url: "https://help.klaviyo.com/hc/en-us/articles/19896802561307-PAR-Punchh-data-reference"
section: "PAR Punchh"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-05-19T19:09:19Z"
language: "en"
---
## You will learn

Learn what data syncs from PAR Punchh to Klaviyo and where to view it. This includes data related to account activity, rewards, and check-ins.

If you have not already, read our guide on [getting started with PAR Punchh](https://help.klaviyo.com/hc/en-us/articles/19895874407579) for step-by-step instructions on integrating, before continuing with this article.

## How to view your data

To view your PAR Punchh data:

1. Click the ****Analytics**** dropdown in the left-hand navigation sidebar.
2. Select ****Metrics****. Here, you can view all of the metrics in your account.
3. Filter this view to see PAR Punchh metrics by using the filter selector next to the search bar and selecting ****PAR Punchh****.

![](https://klaviyo.zendesk.com/hc/article_attachments/47678629583003)

## Synced metrics

### Signed Up

This event occurs when a customer signs up for your PAR Punchh loyalty program. You can filter and target Signed Up events based on the following criteria:

- ****Email Confirmation URL****
  Email confirmation URL
- ****Marketing Email Subscription****
  Whether the end-user has subscribed to marketing emails or not
- ****Marketing Push Subscription****
  Whether the end-user has subscribed to marketing push notifications or not
- ****SMS Subscription****
  Whether the end-user has subscribed to SMS services or not

## Redemption metrics

### Created Redemption, Updated Redemption

These events happen when a customer creates and updates a redemption. You can filter and target redemption events based on the following criteria:

- ****Barcode****
  Barcode generated for the order
- ****Channel****
  Redemption channel (i.e., POS, online order)
- ****Expiring On****
  Redemption code expiring on timestamp
- ****Location ID****
  ID from the location where redemption happened
- ****Location Name****
  Name of the location where redemption happened
- ****Additional Properties****
  Redemption met keys populated in case of configured
- ****Admin ID****
  ID of the admin that created the redemption code
- ****Created At****
  Redemption code created at timestamp
- ****Expired At****
  Redemption code expired at timestamp
- ****Force Message****
  Message in case of force redeem
- ****Internal Tracking Code****
  Redemption tracking code generated for the offer (i.e., reward or redeemable or banked reward)
- ****Redemption Code****
  Code for redemption
- ****Updated At****
  Redemption code created at timestamp
- ****Points Requested****
  Points requested to be redeemed on the order
- ****Redeemable ID****
  ID for redemption
- ****Redeemable Name****
  Name of the redeemable
- ****Redeemable Properties****
- ****Redeemed Points****
  Points redeemed on the order
- ****Redemption Code ID****
  Redemption code ID generated for the offer by PAR Punchh (i.e., reward or redeemable or banked reward)
- ****Redemption Code Pass****
- ****Redemption ID****
  Unique redemption ID generated in PAR Punchh for a redemption
- ****Redemption Status****
  Status of the redemption (i.e., redeemed, expired, redeemable, transferred, force\_redeemed, cancelled)
- ****Redemption Type****
  Type of redemption (i.e., BankedRewardRedemption, RedeemableRedemption, Redemption, RewardRedemption)
- ****Reward ID****
  Reward ID in case of reward redemption
- ****Store Number****
  Store number of the location where redemption happened
- ****Transferred to ID****
  ID of the transfer type (i.e., campaign ID in case of social cause campaign)
- ****Transferred to Type****
  Type of transfer (i.e., social cause campaign)
- ****Web****
  Whether the redemption is via iFrame or not

### Applied Redemption

This event is generated when a redemption gets applied. You can filter and target Applied Redemption events based on the following criteria:

- ****discountAmount****
  Discount amount associated with the redemption
- ****InternalTrackingCode****
  Redemption tracking code generated for the offer (i.e., reward or redeemable or banked reward)
- ****locationName****
  Location name of the check-in
- ****processedAt****
  Timestamp when the redemption was processed
- ****rewardName****
  Name of the reward

## Check-in metrics

### Checked-in for loyalty, Checked-in for gift

These events happen when a user checks in to the loyalty program or for a specific gift. You can filter and target checked-in events based on the following criteria:

- ****Approved****
  Check-in approved status
- ****Campaign ID****
  Campaign ID created in PAR Punchh
- ****Campaign Name****
  Name of campaign
- ****Campaign Type****
  Type of campaign
- ****Channel****
  Channel from where check-in happens (i.e., POS, OnlineOrder, Web, Mobile)
- ****Check-in ID****
  Unique check-in ID generated by PAR Punchh
- ****Check-in Type****
  OnlineCheckin, PosCheckin, ReceiptImageCheckin, BarcodeCheckin, QrcodeCheckin, POSConsoleCheckin
- ****Earnable Amount****
  Earnable amount based on earning qualifier for the order
- ****First Check-in at Business****
  Denotes if it is a first check-in for the business
- ****First Check-in at Location****
  Denotes if it is a first check-in for the location
- ****Gift Reason****
  Gift reason for points gifted to user
- ****Gifted By Type****
  Type of gifting (i.e., admin, check-in, etc.)
- ****Gifted For Type****
  Type of gifting (i.e., Mass Gifting, Feedback Reply, Game, etc.)
- ****Items****
  Menu items object
- ****Location ID****
  Location ID generated in PAR Punchh
- ****Location Name****
  Location name of the check-in
- ****Manual****
- ****Points Earned****
  Points earned on the order
- ****Points Spent****
  Points redeemed on the order
- ****PAR Punchh Key****
  Unique PAR Punchh key generated for the order
- ****Receipt Amount****
  Receipt amount for the order
- ****Redemption ID****
  Redemption ID populated in case the redemption is fully redeemed on the order
- ****Store Number****
  Store number of the location
- ****Barcode****
  Barcode generated for the order
- ****Created At****
  Timestamp when check-in gets created in PAR Punchh
- ****Expired At****
  Date on which the check-in expired
- ****Expiring On****
  Date on which the check-in will expire
- ****External UID****
  External UID generated for the transaction
- ****Referring ID****
  Check-in ID of the first check-in of the referred user
- ****Referring Full Name****
  Name of the referral user
- ****Referring User ID****
  ID of the referral user
- ****Gifted By ID****
  ID of the admin who gifted points
- ****Gifted For ID****
  ID for the type of gifting
- ****QR decoded****
  QR code value generated for the order
- ****Transaction Number****
  Transaction number of the order
- ****Updated At****
  TImestamp when check-in gets updated in PAR Punchh
- ****Receipt Date****
  Receipt date/time for the order
- ****Pending Refresh****
  Enabled per the pending points configuration
- ****Unverified Receipt Amount****
  Receipt\_amount populated in case of manual check-in (i.e., receipt image verification based)
- ****Refreshed At****
  Check-in refresh timestamp
- ****Verifications Count****
  This count increases if multiple reviewers or admins have approved a check-in (applicable for receipt image verification-based check-in).
- ****Verified At****
  Check-in approved timestamp (applicable for receipt image verification-based check-in)
- ****Reviewer ID****
  Admin ID of the reviewer who is verifying a check-in (applicable for receipt image verification-based check-in)

### Checked-in at POS scanner

This event is generated after a POS check-in. You can filter and target this check-in event based on points.

- ****Points****
  Points earned from check-in

## Reward metrics

### Earned Reward

This includes user rewards gifted/issued events triggered as they happen in PAR Punchh. You can filter and target Earned Reward events based on the following criteria:

- ****Discount Channel****
  Channels where the reward can be used. Possible values are:
  - "online\_only" for online orders
  - "offline\_only" for POS
  - "all" for both
- ****Gift Reason****
  Gift reason for reward gifted to user
- ****Reward Image URL****
  URL of the image depicting the reward
- ****Expiring At****
  Date/time when the reward expires (UTC)
- ****Status****
  Status includes honored, unredeemed, live, perished, expired
- ****Campaign Name****
  Name of the Punchh campaign used for the reward
- ****Campaign Type****
  Type of the Punchh campaign used for the reward
- ****Description****
  Description of the reward
- ****Discount Amount****
  Discount amount associated with the reward
- ****Gifted For Type****
  Type of gifting (i.e., mass gifting, feedback reply, game, etc.)
- ****Reward Name****
  Name of the reward
- ****Reward Points Redeemed****
  Number of reward points redeemed
- ****Reward Properties****
  Additional properties of the reward configured in Punchh
- ****Store Numbers****
  Store numbers of all locations where the reward can be redeemed

### Converted Points to Reward

This event is triggered when the points earned by a customer are turned into rewards. You can filter and target Converted Points to Reward events based on the following criteria:

- ****Bank Value****
  Value of banked rewards
- ****Current Banked Reward****
  Current value of banked rewards
- ****Reward****

## Other metrics

### Completed Card

This event is generated when a guest's loyalty card gets completed. You can filter and target Completed Card events based on the following criteria:

- ****Card Completion****
  Whether required visits are made for single card completion or not
- ****First Card Reminder****
  Whether a reminder is sent on completion of the first card or not
- ****Second Card Reminder****
  Whether a reminder is sent on completion of the second card or not
- ****Name****
  Name of the reward
- ****Description****
  Description of the redeemable that appears in the app
- ****Discount Amount****
  Discount amount associated with the redeemable
- ****Discount Channel****
  Channels where the reward can be used. Possible values are:
  - "online\_only" for online orders
  - "offline\_only" for POS
  - "all" for both
- ****Expiry Date****
  Expiry date of the redeemable
- ****Points Required to Redeem****
  Value of points required to redeem a particular redeemable
- ****Redeemable ID****
  Unique ID to identify a redeemable in the system
- ****Redemption Expiry****
  Expiry date of the redeemable
- ****Status****
  Status of the redeemable includes: activated, deactivated, draft, expired
- ****Applicable as Loyalty Redemption****
  Whether redeemables are allowed for loyalty reward redemption or not
- ****Created At****
  Date and time when the redeemable was created for an end-user in the system
- ****Expire Redemption Code with Reward End Date****
  Whether the redemption code is to expire along with the reward end date or not
- ****Metadata****
  Meta data that can be added to a redeemable. This can be used to program mobile apps to have certain behavior when specific data are received from the server, or can be used as the business wants. This can be configured from the PAR Punchh dashboard and has a maximum length of 255 characters.
- ****Updated At****
  Date and time when the redeemable was updated for an end-user in the system.
- Redeemable Image URL: URL of the image that is displayed in the app to depict the redeemable
- ****Redeemable Properties****
  Properties such as "Merchandise", "Food Item", etc. added to a particular redeemable

## Synced objects

### Reward

This object will be synced when a reward has been issued to a customer through your Punchh loyalty program by a Punchh campaign created in Klaviyo. This object will be updated anytime the reward is updated in Punchh. For more information on how to use Objects in Klaviyo, explore [these articles](https://help.klaviyo.com/hc/en-us/sections/35146497665435).

You can filter and target Reward objects based on the following criteria:

- ****RewardID****
  Unique ID of the reward.
- ****Description****
  Description of the reward
- ****GiftReason****
  Gift reason for reward gifted to user
- ****RewardName****
  Name of the reward
- ****ExpiringAt****
  Date/time when the reward expires
- ****Status****
  Status includes: honored, unredeemed, perished, expired
- ****CampaignName****
  Name of the Punchh campaign
- ****CampaignType****
  Informs about the type of campaign through which an end-user got a reward. Currently, the only possible value is "loyalty".
- ****RewardImageURL****
  URL of the image depicting the reward
- ****DiscountChannel****
  Channels where the reward can be used. Possible values are: “online\_only”, “offline\_only”, “all”.
- ****DiscountAmount****
  Discount amount associated with the reward
- ****GiftedForType****
  Type of gifting
- ****RewardPointsRedeemed****
  Reward points redeemed via this reward
- ****RewardProperties****
  Additional properties of the reward (e.g., "merchandise", "order ahead", "promo", etc.) that can be configured in the Punchh platform

## Synced guest data

In addition to the metrics Klaviyo syncs from PAR Punchh, Klaviyo will also create a unique profile for every customer that we sync. When we sync contact information, there are also certain custom properties that may get added to each Klaviyo profile. You can use these properties in segments and in flows. Here are the properties that are automatically synced from PAR Punchh:

- Email
- Phone Number
- First Name
- Last Name
- Punchh Anniversary
- Birthday
- Gender
- Punchh Guest Type
- Punchh Joined At
- Punchh Last Activity At
- Punchh Favorite Locations
- Punchh Favorite Store Numbers
- Preferred Language
- Punchh Referral Code
- Punchh Signup Channel
- Punchh Unsubscribe Reason
- Punchh Unsubscribed Status
- Punchh ID
- Punchh User Status
- Punchh Membership Level
- Punchh Last Visit
- Punchh Loyalty Points
- Punchh Total Credits
- Punchh Total Lifetime Points
- Punchh Total Point Credits
- Punchh Total Visit
- Punchh Unbanked Points

Email consent is synced from Punchh to Klaviyo. Please note that we do not sync SMS consent from Punchh.