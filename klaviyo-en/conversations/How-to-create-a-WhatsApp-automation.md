---
id: 40116727375771
title: "How to create a WhatsApp automation"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/40116727375771-How-to-create-a-WhatsApp-automation"
section: "Automations"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-21T13:54:55Z"
language: en
---

Only Owners, Admins, and Managers can access this feature.

See how to build a WhatsApp automation, which allows you to ask questions and send personalized recommendations.

For instance, you can run quizzes, surveys, and buying guides all through WhatsApp messages. Not only is this a quick and easy way to engage your audience, it is a great way to gather more data and inform your marketing strategies.

This article focuses on the steps to create an automation. For details on how automations work, their settings, etc., see [getting started with automations](https://help.klaviyo.com/hc/en-us/articles/34158391513627), although note that it currently does not mention WhatsApp specifically.

## ****Before you begin****

Please note the following:

- You must already have [WhatsApp set up](https://help.klaviyo.com/hc/en-us/articles/40111819732635).
- Your outbound messages are "service" messages and free.
- Each automation must include at least:
  - 1 message.
  - 2 choices per message.
  - 1 recommendation.
- Automations require an inbound channel match. If a customer messages a brand through an automation, their message must be sent through the same channel in order for the automation to work.
  - For example, there's an automation configured via WhatsApp and a message is sent to them. A customer must reply to that automation in WhatsApp in order for it to work. They can't reply via SMS.

## ****Build an automation****

### ****Set up an automation and its trigger keywords****

1. Navigate to ****Automations****.
2. Click ****Create automation****.
3. Once in the new automation, click on the ****Trigger****.
4. Select a trigger type from the right sidebar, either:

   - ****Always on****or
   - ****Message response**** (i.e., a campaign or flow message)![Automation Trigger](https://klaviyo.zendesk.com/hc/article_attachments/41251652348571)
5. Type in the word or phrase you want as the trigger keyword. Please note that:

- Trigger keywords work differently depending on the type
  - Always on works by checking if an inbound text is an exact match to those words.
    - Ex: if you use “Pets” as a trigger keyword, the automation will only trigger for “Pets,” and not “pet” or “petsitter.”
  - Message response works by checking if an inbound text contains those words.
    - Ex: if you use “Outdoor furniture” as a trigger keyword, the automation will trigger for “Outdoor,” and "Furniture"
- Trigger keywords must be:
  - 3 or more characters. Max characters is 20.
  - Unique (i.e., they cannot be used for any other automation)
  - Can contain spaces and be phrases: "I love pets"
  - Trigger keywords are not case sensitive. "PETS" will still trigger "pets."
  - Cannot contain special characters (i.e., +, -, &)
  - Not be linked to a subscribe or compliance keyword (i.e., STOP, JOIN)

    6. Click ****Save****.

    7. Optional: to add more trigger keywords:
- Click the trigger again.
- Select ****Add keyword****.

  8. Optional, but highly recommended: to set profile properties based on the keyword trigger, toggle on the ****Assign responses as a profile property**** option.
- For the example below, this creates a new custom profile property of “Favorite scent” to be either “Linen,” “Apple Cider,” or “Pumpkin.”

![](https://klaviyo.zendesk.com/hc/article_attachments/42749459707291)

### ****Create your messages and add choices****

1. Click ****Add message.****
   ![](https://klaviyo.zendesk.com/hc/article_attachments/42749462068635)
2. Add in your message text in the **Message** box.
3. Include at least 2 choices for the message. Note that:

   - Choices are numbered sequentially.
   - Subscribers can reply with either the choice text or the number.
   - Choices are recognized using “contains” logic:
     - A choice can appear anywhere in a message (including as part of another word).
     - Abbreviations or misspelled words may be recognized (although it is not guaranteed).
   - Best practices for choices are to not use:
     - Single numbers or letters as choices (e.g., the number “21” or only the letter “A”).
     - Hard to spell words.
     - Long phrases.![](https://klaviyo.zendesk.com/hc/article_attachments/42749462074139)
4. Optional: to add more choices, select ****Add Choice****.
5. Optional: name your message in the **Internal name** field under Settings. Naming your messages makes it easier to refer back to them later.
6. Optional: to set profile properties based on choices, toggle on the ****Assign response to a profile property**** option under Settings.

   - For the example below, this sets a custom profile property of “Pet” to be either “Cat,” “Dog,” or “Other.”![Automation Settings.png](https://klaviyo.zendesk.com/hc/article_attachments/41251652354459)
7. Select ****Save****.
8. Optional: add more messages by clicking the plus (+) button and selecting ****Add message****.

- We recommend limiting the number of messages to 2-3 per automation.

### ****Add recommendations****

Let's say you have a cupcake shop, and your automation is trying to direct customers to a product they'll love. Your recommendations can leverage all of the answers someone provided to questions like "vanilla or chocolate?" or "what's your favorite fruit?"

1. After your messages, select the plus (+) button and then click ****Add recommendation****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/42749462076571)
2. Name your recommendation something descriptive (e.g., “Chocolate strawberry lovers”).
3. Add in your message.

   - Example: “We also love chocolate and strawberry together. Try some of our favorites.”
4. Select which choice combination you want this recommendation to apply to (e.g., people who selected both “strawberry” and “chocolate”).

   - You can select multiple choice combinations for a single recommendation.![Create a recommendation.png](https://klaviyo.zendesk.com/hc/article_attachments/41251652360603)
5. Select ****Save****.
6. Click the arrow for ****Default recommendation****.
7. Name the recommendation.
8. Type out your default recommendation message, which acts as a fallback for your recommendations. Often, people use a best seller or new product as the default.

   - Example: “A classic combo! Check out our products here: [www.cupcakes123.com/products](http://www.cupcakes123.com/products)”![Default recommendation.png](https://klaviyo.zendesk.com/hc/article_attachments/41251652363291)
9. Click ****Save****.
10. Add a recommendation for each choice combination, or use your default recommendation to send to all other choice combinations.

### ****Optional: adjust your settings****

Optional: adjust any session settings for your automation. To do so:

1. Click the gear icon in the upper right.
2. Select ****Session settings****.
   ![Session settings.png](https://klaviyo.zendesk.com/hc/article_attachments/41251652368667)
3. You can update the following settings:

- Channel Scoping
- Reprompt response
- Fallback response
- Maximum number of reprompts
- Maximum timeout (in hours)

### ****Preview and turn on an automation****

Once you're happy with your automation:

1. Preview the automation by clicking the "play" button in the upper right

   - The preview is slightly different from the live experience. It doesn't catch typos or show link shortening. Learn more about [previewing an automation](https://help.klaviyo.com/hc/en-us/articles/34175751807515).
2. Double-check your trigger keywords, messages and choices, and recommendations.

   - Once the automation is on, you must turn it off to edit it, which causes it to immediately drop everyone currently in the automation.
3. Click ****Turn on**** in the upper right.

Once you turn on an automation, it will send to any WhatsApp subscriber who sends a trigger keyword.

### ****Coupons, personalization, and links****

You can include either static coupons or [dynamic coupons](https://help.klaviyo.com/hc/en-us/articles/115005084727) in your message. Static coupons use one shared code for all recipients. Dynamic coupons generate a unique code for each recipient.

You can also personalize your message with [profile and custom properties](https://help.klaviyo.com/hc/en-us/articles/4408802648731). Add these directly to your content using the appropriate variable syntax. Profile properties created within the automation will not populate in the message. Make sure the property already exists on the profile before the message sends.

All links in your message are automatically shortened.