---
id: 7593
title: "AI Prompt-Copy Writing"
slug: "prompt-librarycopywriting"
category: "DC 官方资源中心"
category_slug: "dc-resources"
wp_url: "https://dynamicycle.com/docs/prompt-librarycopywriting/"
wp_modified: "2026-04-27T05:43:06"
---

##### 为什么要构建Klaviyo运营的提示词案例库？

在电商营销领域，Klaviyo已成为品牌构建客户关系、驱动复购增长的核心工具。越来越多的品牌借助Klaviyo的全生命周期营销策略，在90天内将电子邮件收入占比从15%–20%提升到30%–40%。然而，拥有工具不等于拥有增长——真正决定效果的，是团队能否高效地借助Klaviyo实现精准细分、个性化触达和自动化流程优化。

随着AI技术的发展，将ChatGPT融入Klaviyo运营已成为行业趋势。Klaviyo官方推出的ChatGPT应用，让营销人员可以直接在ChatGPT中访问实时Klaviyo数据，通过自然语言对话即可获取洞察、优化策略。良好的提示词帮助ChatGPT正确调用Klaviyo的API能力，而模糊的提示则可能导致AI产生“幻觉”或不准确的输出。在这种背景下，构建一套高质量、可复用的Klaviyo运营提示词案例库，不仅能够大幅提高团队工作效率，更能将零散的经验沉淀为可规模化的组织能力。

本案例库基于实际运营场景，系统整理了针对Klaviyo邮件与短信营销的ChatGPT提示词模板，涵盖受众细分、个性化内容创作、自动化流程构建、数据分析归因、SMS营销和全生命周期策略等核心模块。每个案例均包含[角色设定] → [任务目标] → [步骤拆解] → [输出约束]四部分结构，确保提示词清晰、具体、可执行。

##### 1.不显推销感的稀缺性信息传达

- ****Business Type****：eCommerce
- ****Function Category****：General
- ****Prompt**** ：List 10 creative ways [store URL] can build scarcity or exclusivity into email and SMS campaigns — without sounding overly salesy or pushy.⁣ ⁣ For each idea, include:⁣ ⁣ – What the scarcity or exclusivity element is (e.g. limited stock, VIP access, early unlock)⁣ ⁣ – How to frame it in copy (tone, language style)⁣ ⁣ – Which campaign or flow to apply it to⁣ ⁣ – Why it drives urgency in a subtle or brand-aligned way⁣ ⁣ Focus on ideas that feel authentic, brand-safe, and actually influence behavior.

##### 2.利用零方数据个性化 Email 内容

- ****Business Type****：eCommerce
- ****Function Category****：General
- ****Prompt**** ：List 10 ways [store URL] can personalize their email content using zero-party and first-party data. For each method, include: – What data is used (e.g. quiz results, product viewed, purchase history) – How it’s applied in the email (subject line, product block, copy, send time, etc.) – Which flow or campaign it fits into – Why it improves performance Ideas should be practical, scalable, and aligned with retention goals.

##### 3.为您的店铺生成 Buyer Persona

- ****Business Type****：eCommerce
- ****Function Category：****General
- ****Prompt**** ：You’re building buyer personas for [store URL]. Create 3 detailed profiles that include:Name + quick descriptor (e.g. “Lisa – the wellness-obsessed millennial”) – Demographics (age, gender, location) – Key pain points – Purchase motivations – Shopping behavior – Favorite products from the store – What kind of email/SMS content they’d love Keep it practical and tailored to the actual store and products.

##### 4.Welcome Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 5-part welcome email sequence for a new subscriber to an eCommerce store. Use the following details to inform the tone, structure, and content of the emails: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Unique Selling Propositions (USPs): {{USPS}} • Primary Goal of Sequence: {{SEQUENCE\_GOAL}} • Offer or Incentive (if any): {{OFFER}} Each email should have: 1. A compelling subject line 2. A short preheader 3. Engaging, personalized body copy (keep it concise) 4. A clear CTA Email breakdown: • Email 1: Welcome & Brand Introduction • Email 2: Highlight Benefits/USPs • Email 3: Social Proof or Testimonials • Email 4: Education/Value (e.g. tips, how-to) • Email 5: Strong close + limited-time offer or urgency Keep tone aligned with {{BRAND\_VOICE}}. Make copy feel native to email marketing best practices.

##### 5.Cart Abandonment Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 3-part cart abandonment email sequence for an eCommerce store to recover lost sales. Use the following brand and customer context to tailor the tone, structure, and messaging: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Unique Selling Propositions (USPs): {{USPS}} • Offer or Incentive (if any): {{OFFER}} • Average Cart Value (optional): {{AVERAGE\_CART\_VALUE}} Each email should include: 1. A subject line that creates urgency or curiosity 2. A concise preheader 3. Persuasive, benefit-driven body copy (brief and conversion-focused) 4. A clear call-to-action (CTA) Email breakdown: • Email 1: Gentle Reminder (1–2 hours post-abandonment) • Email 2: Reinforce Value + Add Social Proof (24 hours later) • Email 3: Last Call + Scarcity or Incentive Push (48–72 hours later) Tone must reflect {{BRAND\_VOICE}} and focus on converting hesitation into purchase.

##### 6.Winback Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 3-part winback email sequence to re-engage inactive customers of an eCommerce store. Use the brand and customer context below to craft effective, personalized messaging that revives interest and encourages return purchases: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Unique Selling Propositions (USPs): {{USPS}} • Time Since Last Purchase (e.g., 60 days): {{TIME\_SINCE\_LAST\_PURCHASE}} • Offer or Incentive (if any): {{OFFER}} • Customer Purchase Behavior (optional): {{CUSTOMER\_BEHAVIOR}} Each email must include: 1. A compelling subject line (either nostalgic, benefit-focused, or urgent) 2. A preheader that complements the subject 3. Short, punchy body copy with a persuasive hook 4. A clear call-to-action Email breakdown: • Email 1: “We Miss You” – Reconnect with emotion or relevance • Email 2: Value Reminder – Showcase what they’re missing (best-sellers, USPs) • Email 3: Final Push – Include an offer or limited-time message to re-engage Keep tone aligned with {{BRAND\_VOICE}} and make the copy persuasive but non-pushy.

##### 7.Loyalty Program Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 4-part loyalty program email sequence for an eCommerce store to engage, reward, and retain loyalty members. Tailor each email to the stage of the customer in the loyalty journey using the information below: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Loyalty Program Name (if any): {{PROGRAM\_NAME}} • Point System/Reward Mechanism (briefly): {{REWARD\_SYSTEM}} • Offer or Incentives: {{OFFER}} • Customer Behavior or Segmentation (optional): {{CUSTOMER\_BEHAVIOR}} Each email should include: 1. An engaging subject line 2. A relevant, motivating preheader 3. Clear, benefit-driven body copy 4. A strong call-to-action (CTA) Email breakdown: • Email 1: Welcome to the Loyalty Program – Highlight benefits, how it works • Email 2: Points Earned Update – Notify about recent point activity or achievements • Email 3: Points Expiry Reminder – Alert them about expiring points and encourage redemption • Email 4: Tier Upgrade Opportunity or Bonus Offer – Show what’s next or give a re-engagement nudge Keep the tone consistent with {{BRAND\_VOICE}} and focus on rewarding loyalty and driving repeat purchases.

##### 8.Product Replenishment Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 3-part replenishment email sequence for an eCommerce store to remind customers to re-order consumable or repeat-use products. Use the following context to tailor the timing, messaging, and tone: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Typical Usage Duration (e.g., 30 days): {{USAGE\_DURATION}} • Customer’s Last Purchase Date (or Time Since): {{LAST\_PURCHASE}} • Offer or Incentive (if any): {{OFFER}} • Subscription Option (if available): {{SUBSCRIPTION\_OPTION}} Each email should include: 1. A helpful, timely subject line 2. A short preheader that supports the CTA 3. Personalized, benefit-focused body copy 4. A clear CTA to reorder or subscribe Email breakdown: • Email 1: Friendly Reminder – It’s almost time to restock • Email 2: Nudge with Benefits – Replenish now to avoid running out • Email 3: Final Reminder + Incentive – Last chance with a small discount or urgency Ensure the tone matches {{BRAND\_VOICE}} and the copy feels helpful, not salesy. Prioritize convenience, timing, and product trust.

##### 9.Review Request Email Flow (UGC Collection)

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：Create a post-purchase review request flow for [store URL] that maximizes reviews and turns them into marketing assets. Include – Total number of emails (3–4) – Timing of each email (days after delivery) – Subject line and core message per email – Incentive idea (if any) – What to do if the review is: – Positive (e.g. ask for UGC, referral, testimonial use) – Negative (e.g. trigger customer support follow-up) Make sure the tone fits the brand and keeps the customer experience positive throughout.

##### 10.Post-Purchase Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 4-part post-purchase email sequence for an eCommerce store to build trust, reduce buyer’s remorse, and encourage repeat purchases. Use the following brand and product details to tailor the copy: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Customer’s First or Repeat Purchase: {{CUSTOMER\_TYPE}} • Product Delivery Time (if relevant): {{DELIVERY\_TIME}} • Cross-Sell or Upsell Options: {{CROSS\_SELL\_UPSELL}} • Offer or Incentive for Next Purchase (if any): {{OFFER}} Each email should include: 1. A compelling subject line 2. A short, trust-building preheader 3. Helpful, clear body copy (personalized if possible) 4. A relevant call-to-action (CTA) Email breakdown: • Email 1: Thank You & Order Confirmation – Set expectations, build excitement • Email 2: Product Education – How to use/care for the item, benefits, setup • Email 3: Review Request or Feedback – Ask for honest input or a quick rating • Email 4: Next Purchase Prompt – Cross-sell, upsell, or offer incentive Keep the tone aligned with {{BRAND\_VOICE}} and ensure the flow feels like a helpful post-purchase experience, not a sales push.

##### 11.Transactional Shipping Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 5-part transactional email sequence for an eCommerce store focused on order fulfillment, shipping updates, and delivery tracking. The tone should reflect the brand voice and keep the customer informed, reassured, and engaged throughout the post-purchase journey. Use the following details to guide the messaging: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Average Fulfillment Time: {{FULFILLMENT\_TIME}} • Shipping Carrier (optional): {{SHIPPING\_CARRIER}} • Tracking Info URL Placeholder: {{TRACKING\_URL}} • Customer Support Contact Info: {{SUPPORT\_INFO}} Each email should include: 1. A status-specific subject line 2. A helpful preheader 3. Clear, friendly, informative body copy 4. A direct CTA to view or track the order Email sequence: • Email 1: Order Shipped – Notify customer that their order has left the warehouse; include tracking link. • Email 2: Shipment Stalled (Optional/Conditional) – Inform them of a delay or unusual transit pause; offer support and reassurance. • Email 3: In-Transit Update – Mid-shipment update with estimated delivery date and tracking reminder. • Email 4: Out for Delivery – Let them know the package is arriving today; encourage them to keep an eye out. • Email 5: Delivered Confirmation – Confirm successful delivery and provide options for support, reviews, or follow-up actions. Maintain clarity, reduce anxiety, and build trust at every step. Reflect {{BRAND\_VOICE}} while prioritizing transparency and customer service.

##### 12.VIP Reward Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 4-part VIP reward email sequence for an eCommerce store to recognize, engage, and retain high-value customers. The tone should reflect exclusivity, appreciation, and personalized value while encouraging continued loyalty and spending. Use the following context to shape your messaging: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • VIP Tier Name: {{VIP\_TIER\_NAME}} • Qualification Criteria (e.g., $500+ spent in 12 months): {{QUALIFICATION\_CRITERIA}} • VIP Perks (discounts, early access, gifts, etc.): {{VIP\_PERKS}} • Offer or Time-Sensitive Benefit (if any): {{OFFER}} Each email should include: 1. A premium-feel subject line 2. A personalized preheader 3. Gratitude-forward, benefit-driven body copy 4. A clear call-to-action (CTA) to use perks, browse products, or stay engaged Email breakdown: • Email 1: Welcome to VIP Status – Congratulate and outline perks of their new status • Email 2: Exclusive Benefits Highlight – Dive deeper into the value (e.g., early access, surprise rewards) • Email 3: VIP-Only Offer or Sneak Peek – Provide a limited-time reward or preview of new products • Email 4: Keep Your Status Reminder – Encourage continued engagement or requalification with personalized stats or reminders Keep the tone in line with {{BRAND\_VOICE}}, making the customer feel valued, special, and part of an elite inner circle.

##### 13.Browse Abandonment Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 3-part browse abandonment email sequence for an eCommerce store. These emails should re-engage visitors who viewed products but didn’t add anything to their cart. The copy must feel helpful and personalized, not pushy. Use the following store details to craft compelling messaging: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Typical Products Browsed: {{TYPICAL\_BROWSING\_BEHAVIOR}} • Offer or Incentive (optional): {{OFFER}} • Dynamic Product Block Available: {{DYNAMIC\_PRODUCT\_BLOCK}} Each email should include: 1. A relevant, curiosity-driven subject line 2. A soft-touch preheader 3. Short, benefit-driven body copy 4. CTA to return to browsing or complete a purchase Email breakdown: • Email 1: “Still Thinking About It?” – Re-engage with soft nudge and product preview • Email 2: “Need Help Deciding?” – Include social proof or a quick comparison • Email 3: “Limited Availability / Last Look” – Create urgency with inventory, offer, or popularity Keep the tone aligned with {{BRAND\_VOICE}} and make the emails feel natural, like a helpful follow-up from a personal shopper.

##### 14.First Purchase Anniversary Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 2-part email sequence to celebrate the 1-year anniversary of a customer’s first purchase from an eCommerce store. The goal is to express appreciation, re-engage the customer emotionally, and encourage another purchase. Use the following details to craft messaging that feels warm, personal, and aligned with the brand: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Anniversary Gift or Incentive (if any): {{ANNIVERSARY\_OFFER}} • Customer Purchase History or Highlights (optional): {{PURCHASE\_HISTORY}} Each email should include: 1. A heartfelt, attention-grabbing subject line 2. A preheader with emotional or value-driven tone 3. Body copy that celebrates the customer relationship and offers a clear next step 4. CTA (e.g. browse again, claim offer, explore new arrivals) Email breakdown: • Email 1: “Happy 1-Year Anniversary!” – Thank them for being a customer, reflect on the journey • Email 2: “A Gift to Celebrate You” – Deliver a small offer or exclusive incentive to re-engage Tone should reflect {{BRAND\_VOICE}} and feel like a relationship milestone, not just a promotion.

##### 15.Customer Milestone Celebration Email Flow

- Business Type：eCommerce
- Function Category：Flow Sequence
- Prompt ：You are an expert email copywriter. Write a 3-part milestone celebration email sequence for an eCommerce store. These emails are triggered when a customer hits key milestones—such as number of orders, total spend, or account age. The goal is to make customers feel recognized and valued, while encouraging continued loyalty and purchases. Use the following details to inform tone, structure, and messaging: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Milestone Type (e.g., 5th order, $1,000 spent, 2-year customer): {{MILESTONE\_TYPE}} • Reward or Incentive (if any): {{MILESTONE\_REWARD}} • Loyalty Program Mention (if applicable): {{LOYALTY\_PROGRAM}} Each email should include: 1. A celebratory subject line 2. A preheader that emphasizes appreciation or achievement 3. Warm, relationship-building body copy 4. A CTA to claim reward, continue shopping, or unlock next tier Email breakdown: • Email 1: “You Hit a Milestone!” – Acknowledge the achievement and express appreciation • Email 2: “Here’s a Thank-You Gift” – Deliver any reward tied to the milestone • Email 3: “Let’s Keep It Going” – Encourage next action or goal (e.g., unlock next level, try something new) Keep tone aligned with {{BRAND\_VOICE}} and prioritize emotional connection over hard selling.

##### 16.Cross-Sell & Upsell Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 3-part cross-sell/upsell email sequence for an eCommerce store. This flow targets customers after a purchase to recommend related products or upgrades. The goal is to increase customer lifetime value by offering complementary or premium items. Use the following store and customer data to personalize recommendations: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Recently Purchased Product(s): {{RECENT\_PURCHASE}} • Relevant Cross-Sell or Upsell Items: {{CROSS\_UPSELL\_PRODUCTS}} • Incentive (optional): {{OFFER}} Each email should include: 1. A smart, product-aware subject line 2. A helpful, relevant preheader 3. Personalized and benefit-driven body copy 4. A CTA to view or buy suggested products Email breakdown: • Email 1: “Customers Who Bought This Also Loved…” – Recommend complementary products • Email 2: “Upgrade Your Experience” – Offer premium versions or bundle deals • Email 3: “Your Perfect Add-On Awaits” – Use urgency, social proof, or limited-time incentives Keep tone aligned with {{BRAND\_VOICE}} and make suggestions feel helpful, not pushy.

##### 17.Subscription Renewal Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 3-part subscription renewal email sequence for an eCommerce store. This flow targets customers with active product subscriptions that are nearing renewal. The goal is to encourage renewals, reduce churn, and reinforce value. Use the details below to customize tone, timing, and messaging: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Subscription Type (e.g., monthly skincare box, supplement refill): {{SUBSCRIPTION\_TYPE}} • Renewal Interval: {{RENEWAL\_INTERVAL}} • Renewal Incentive (if any): {{RENEWAL\_OFFER}} • Customer Satisfaction or Usage Data (if available): {{CUSTOMER\_USAGE\_INFO}} Each email should include: 1. A proactive subject line 2. A preheader that clarifies timing or benefit 3. Simple, trust-building body copy 4. A clear CTA to renew, manage subscription, or adjust preferences Email breakdown: • Email 1: “Your Subscription Is Almost Up” – Notify with a friendly reminder + value reinforcement • Email 2: “Don’t Miss Out on Your Favorites” – Highlight what they’ll lose by not renewing • Email 3: “Last Chance to Renew + Bonus Offer” – Add urgency or offer a small incentive Keep tone aligned with {{BRAND\_VOICE}} and make the flow feel supportive and low-pressure.

##### 18.Birthday or Special Occasion Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 2-part birthday or special occasion email sequence for an eCommerce store. The goal is to create a personalized, celebratory customer experience that strengthens emotional loyalty and drives a purchase. Use the following information to tailor tone, timing, and messaging: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Occasion Type (e.g., birthday, customer anniversary): {{OCCASION\_TYPE}} • Offer or Incentive (e.g., gift, discount): {{SPECIAL\_OFFER}} • Celebration Timing (e.g., on the day, 3 days before): {{TIMING}} Each email should include: 1. A warm, personalized subject line 2. A preheader that builds excitement or emphasizes the gift 3. Short, joyful body copy that shows appreciation 4. A CTA to claim offer, browse gifts, or treat themselves Email breakdown: • Email 1: “It’s Your {{OCCASION\_TYPE}} – Here’s a Treat!” – Send main gift or discount • Email 2: “Don’t Miss Your {{OCCASION\_TYPE}} Gift!” – Follow-up reminder before expiry Keep tone festive, personal, and always aligned with {{BRAND\_VOICE}}.

##### 19.Failed Payment Recovery Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 3-part failed payment recovery email sequence for an eCommerce store. This flow should help recover a failed transaction from either a subscription renewal or one-time checkout. The tone should be helpful, professional, and urgency-driven—without sounding pushy. Use the following details to personalize and guide the messaging: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Type of Payment (e.g., subscription renewal, one-time order): {{PAYMENT\_TYPE}} • Reason for Failure (if known): {{FAILURE\_REASON}} • Link to Update Payment Info: {{PAYMENT\_UPDATE\_LINK}} • Support Contact (if applicable): {{SUPPORT\_CONTACT}} Each email should include: 1. A polite, action-focused subject line 2. A clear preheader that communicates the issue 3. Body copy that’s reassuring, concise, and helpful 4. A CTA to update payment or contact support Email breakdown: • Email 1: “There Was an Issue with Your Payment” – Inform the customer + next step • Email 2: “Still Need to Update Your Info” – Gentle reminder with benefits of resolving • Email 3: “Final Reminder: Avoid Disruption” – Add urgency and mention consequences (if applicable) Keep the tone aligned with {{BRAND\_VOICE}} and prioritize customer service and clarity.

##### 20.Back-in-Stock Notification Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 2-part back-in-stock email sequence for an eCommerce store. This flow is triggered when a previously sold-out product becomes available again. The goal is to convert high-intent customers quickly by creating urgency and excitement. Use the following details to guide tone, timing, and content: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Product Back in Stock: {{PRODUCT\_NAME}} • Stock Level (low, medium, high): {{STOCK\_LEVEL}} • Purchase Limit or Urgency Factor (if any): {{URGENCY\_DETAIL}} • CTA Link to Buy or View Product: {{PRODUCT\_URL}} Each email should include: 1. A high-converting subject line (with urgency or excitement) 2. A preheader that supports the message 3. Body copy that briefly builds desire and urgency 4. A strong CTA to purchase Email breakdown: • Email 1: “It’s Back! {{PRODUCT\_NAME}} Is Available Again” – Quick alert with product highlights • Email 2: “Going Fast: Get Yours Before It’s Gone (Again)” – Urgency-driven reminder Keep tone aligned with {{BRAND\_VOICE}} and design for high intent + fast action.

##### 21.Pre-Order Update Email Flow

- ****Business Type****：eCommerce
- ****Function Category****：Flow Sequence
- ****Prompt**** ：You are an expert email copywriter. Write a 3-part pre-order update email sequence for an eCommerce store. This flow is designed to keep customers informed and excited while they wait for a pre-ordered product to ship. The goal is to maintain trust, reduce support tickets, and reinforce brand loyalty. Use the following information to shape messaging and timing: • Store Name: {{STORE\_NAME}} • Product Type: {{PRODUCT\_TYPE}} • Target Audience: {{TARGET\_AUDIENCE}} • Brand Voice/Tone: {{BRAND\_VOICE}} • Pre-Ordered Product Name: {{PRODUCT\_NAME}} • Expected Ship Date: {{SHIP\_DATE}} • Any Delay or Update Notes: {{ORDER\_UPDATE\_INFO}} • Support Contact Info: {{SUPPORT\_CONTACT}} Each email should include: 1. A clear subject line that reflects status 2. A transparent preheader 3. Friendly, informative body copy 4. CTA (if applicable): View order, contact support, read FAQs, etc. Email breakdown: • Email 1: “Thanks for Pre-Ordering {{PRODUCT\_NAME}}!” – Confirm the order + reiterate ship date and excitement • Email 2: “Quick Update on Your Pre-Order” – Provide a timeline check-in or notify about delays • Email 3: “It’s Almost Here” – Final hype email before shipping (with tracking info if available) Keep tone positive and proactive, aligned with {{BRAND\_VOICE}}, and designed to turn waiting into anticipation.

##### 结语

这套Klaviyo运营提示词案例库的建立，并非为了取代运营人员的专业判断，而是将重复性高、可标准化的任务分配给AI，让团队得以专注于策略、创意和客户关系建设这些更高价值的工作。

在使用本案例库时，请记住一个关键前提：AI的输出质量与输入信息的质量成正比。你提供的品牌背景越详细、数据越完整、目标越清晰，ChatGPT的回答就越有价值。好的人工智能产出通常都依赖于清晰的输入指令。

随着Klaviyo Composer等新一代Agent工具的推出，未来从单个提示词直接生成包含受众、渠道、内容和投放时间的完整营销活动将成为可能。这意味着，学会高效书写提示词不仅是当前运营提效的手段，更是面向未来AI驱动态营销环境的必备技能。希望本案例库能为您的Klaviyo运营实践提供有益的参考与启发。

[免费Klaviyo](https://www.klaviyo.com/partners/signup?utm_source=001Nu00000BgpSoIAJ&utm_medium=partner)

[了解DC](https://connect.klaviyo.com/dynamic-cycle)

[Partners](https://dynamicycle.com/partner/)