---
id: 34158391513627
title: "Getting started with SMS automations"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/34158391513627-Getting-started-with-SMS-automations"
section: "Automations"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-21T13:54:40Z"
language: en
---

Only Owners, Admins, and Managers can access this feature.

## You will learn

Find out about Automations in Klaviyo, which you can use to create automated 1-on-1 conversations with your SMS subscribers. Automations make it easy to ask questions, recognize responses, and provide personalized recommendations to your customers.

By building automations, you can:

- Create surveys to gather customer feedback.
- Build buying guides that provide personalized recommendations.
- Run quizzes to learn more about your subscribers’ and collect profile properties.

## Before you begin

Please note the following:

- You must [set up SMS](https://help.klaviyo.com/hc/en-us/articles/360035285472) before using automations.
- Automations only reply to SMS subscribers.
- SMS automations are not available for[branded sender IDs](https://help.klaviyo.com/hc/en-us/articles/6637671573403#branded-sender-ids2), as this number type cannot receive text messages.
- Your outbound SMS messages use credits in your billing plan.
  - Inbound SMS (i.e., messages sent to your brand) do not cost credits.
- Each automation must include at least:
  - 1 message.
  - OR
  - 1 recommendation with questions preceding it.

****Flows vs. conversation automations****

In both cases, these features work as automatic touch points for you to communicate with customers and can be used to:

- Create custom messages
- Collect profile properties on the trigger keyword and choices
- Automate communications

The main differences between them are shown in the table below.

|  |  |  |
| --- | --- | --- |
|  | ****Flows**** | ****Conversations**** |
| ****Trigger**** | Can be triggered by a customer’s actions on your website, segments and lists, dates, etc. | Only triggered when someone texts a certain word. |
| ****Message types**** | Any channel (email, SMS, mobile push) | Only SMS |
| ****Response timing**** | Cannot wait for a response, messages always send either immediately or a set period of time. | Waits for a subscriber’s text to contain a recognized answer. |

This means that flows are better for reaching out to subscribers at key moments in their customer journey (such as via welcome messages, abandoned cart reminders, post-purchase follow-ups).

As for automations, these are better at handling back-and-forth communication, asking questions and following up with recommendations.

### Automation example: survey

Automations are a type of conversational SMS: say that you are a pet shop wanting to gather information about your customers’ pets.

In this case, you can send an SMS campaign that asks subscribers to send the word “PETS” to enter a survey and receive a custom coupon.

When they text back “PETS,” the subscriber enters an automation.

![Customer texts the word PETS to your brand](https://klaviyo.zendesk.com/hc/article_attachments/34179397822875)

Then, you can ask what kind of pet they have (1. Cat, 2. Dog, etc.). If you want, you can ask another question (e.g., What size are they?).

![An automation triggers to ask about their pets, the customer replies with the word dog, and the automation asks about the pet's size](https://klaviyo.zendesk.com/hc/article_attachments/34179435230747)

At the end of the automation, you can provide a recommendation (like for the perfect-sized bed or harness) as well as the coupon you promised.

![After the customer replies Large, the automation recommends a Jumbo-sized dog bed and provides a coupon](https://klaviyo.zendesk.com/hc/article_attachments/34179397838747)

Not only is this helpful to driving purchases immediately, you can also store this information so that you can send more targeted messages in the future.

## Key terms and settings for automations

### Automation functionality

When it comes to setting up an automation, you must have 1 or more:

- ****Trigger keyword(s)****
  Word or phrases subscriber texts to enter into an automation. There can be several trigger keywords for a single automation. These keywords must be unique, the same word cannot be used in multiple automations or be a compliance or subscribe keyword.
- ****Questions(s)****
  SMS you send within the automation, containing a question. Questions must include 2 or more choices. At minimum, you need 1 question per automation if including a recommendation.
- ****Choice(s)****
  Options for how your subscribers can answer a question. Choices are always numbered, and a subscriber can text either the choice word/phrase or its corresponding number. At minimum, you must have 2 choices per question.
- ****Message****
  SMS sent at the end of an automation. Sending a message does not require questions before it.
- ****Recommendation****
  SMS sent at the end of an automation. At minimum, you must have at least 1 recommendation at the end of the automation.

### Automation settings

Automations have the following key settings:

- ****Reprompt response****
  This is the reply sent to subscribers if, while part of an automation, they send an inbound text that cannot be matched to a choice. See this section to learn [how choices are recognized](#h_01JMDF730GNVBDJ683KATS00D0).
- ****Fallback response****
  Message sent when someone either reaches the maximum number of reprompts or the maximum timeout.
- ****Maximum number of reprompts****
  The number of times Klaviyo tries to re-engage the user when they send an inbound SMS that does not contain a recognized choice for a message. By default, this is set to 1. If a subscriber reaches this maximum and then sends another unrecognized choice, they exit the automation and receive the fallback response.
- ****Maximum timeout (in hours)****
  The session time for an automation; i.e., how long an automation is active for. By default, session time is set for 24 hours. The time starts when someone texts a trigger keyword and receives the first message. The time does not reset when someone receives follow-up messages. If someone reaches the maximum timeout without receiving a recommendation, they exit the automation.

#### Access an automation’s settings

To access all of an automation’s settings:

1. Click the gear icon in an automation.
2. Select ****Session settings****.

![Session settings option under the gear icon](https://klaviyo.zendesk.com/hc/article_attachments/34179397843995)

## How automations work

The way it works is that:

1. Someone texts you a trigger keyword for the automation.
2. If they are an SMS subscriber, they receive the first message in the automation.
   1. Non-SMS subscribers receive the auto-responder message from your SMS settings.
3. If the subscriber responds with a recognized choice, they move on to the next question or message
   1. If the answer isn’t recognized, they receive the reprompt message.
4. Subscribers exit the automation when any of the following occur:
   1. The subscriber receives a recommendation.
   2. The subscriber receives a message.
   3. The subscriber reaches the maximum number of reprompt responses and then receives the fallback response.
   4. The subscriber reaches the maximum timeout.

While someone is in automation, they cannot enter any other automation until they exit.

## Triggering an automation

### Trigger type

There are 2 types of triggers:

- ****Always on****
  This means that any time someone texts a trigger keyword, that person enters into an automation.
- ****Message response****
  With this option, you must select a campaign or flow message. To enter an automation, someone must have received the selected message within a set timeframe as well as texted the trigger keyword.

![Automation trigger types](https://klaviyo.zendesk.com/hc/article_attachments/36044065155099)

The main difference between these 2 trigger types is if someone can enter at any point in their customer journey or only once they received another, specific message. For instance, “Always on” is better when the automation acts as a support tool, ongoing quiz or survey, etc. For this case, you may trigger the keyword based on a commonly texted word or when showing the keyword on a certain form, in your store, etc.

On the other hand, message response is better when you want to drive campaign or flow recipients to an automation. Say that you only want to survey those who recently reached the second message of your welcome series. In this case, you craft the second message to include the trigger keyword, and set the automation to send to only those who recently received that message.

![Message response trigger where you can select either a campaign or flow](https://klaviyo.zendesk.com/hc/article_attachments/36044065161755)

### Trigger keywords

SMS subscribers enter an automation when they send a trigger keyword. There can be more than 1 trigger keyword per automation.

Please note that trigger keywords:

- Must be 3 or more characters.
- Emojis allowed.
- Are not case sensitive.
- Are recognized if a subscriber’s inbound message is an exact match for a trigger keyword.
- Do not recognize typos or abbreviations by default.
- Can be a phrase.
- Can be a single word.
- Have to be unique for each automation (i.e., you cannot use the same keyword for multiple automations).
- Cannot be linked to a subscribe or compliance keyword (i.e., STOP, JOIN).

For our pet example, let’s say we use 2 separate triggers, shown in the table below.

|  |  |  |
| --- | --- | --- |
| ****Trigger keywords**** | ****Recognized**** | ****Not recognized**** |
| Survey | SURVEY, survey | Usrvey |
| Pets | Pets | Pet |

For the trigger, we recommend using short, easy-to-spell words. If you do use a phrase (like “Quiz me”) or a word with a common abbreviation, include only the first word of that phrase or the abbreviation as another trigger (e.g., use both “Quiz me” and “Quiz”).

## Questions, message, and recommendations

There are 3 options within any automation, all of which are an outbound SMS message:

- Questions
- Message
- Recommendation

All automations require at least 1 message, or 1 recommendation with questions before it.

You can use template tags (e.g., first name) or JSON within messages and recommendations, but note these tags and code are not visible in the preview. If you want to use them, make sure you test the live automation before you tell the trigger keyword to subscribers.

### Questions

When you create a question, you must have:

- Question text (e.g., a question like “what’s kind of pet do you have?”)
- 2 or more choices (e.g., “Cat” and “Dog”)

For instance, the first question may ask what kind of pet someone has.

|  |  |
| --- | --- |
| Question | ****Preview**** |
| What kind of pet do you have?   1. CAT 2. DOG 3. BIRD 4. OTHER | ![Preview of a message asking about the type of pet someone has](https://cdn.sanity.io/images/6ct6b26e/help-center-dev/7a27327fdf858a75118375fe82fca802d096d9b6-784x590.png) |

****How many questions can I have in an automation?****

Number of questions are limited depending on the automation trigger. Always on Limited to 4 questions. Campaign or Flow limited to 3 questions. However, including no more than 2 questions is the best practice.

### Question choices

Choices are numbered in sequential order, as shown in the example above. We recommend limiting the number of choices to ~3-5 per question.

Choices can be:

- Single words or phrases
- Any case or capitalization
- Recognized:
  - Within a longer word of message (i.e., the automation checks if a subscriber’s inbound message “contains” a choice).
    - Some typos (particularly for words longer than 5 letters) may be recognized thanks to fuzzy matching.
  - As either the choice text or number.

    Continuing the pet example, the automation would attribute all of the following to the first choice (“1. Cat”):
- Cat, cat, or CAT
- 1
- I have a cat
- Catch

### Recommendations

You must also either include a recommendation for every choice or use a default recommendation.

****What is a default recommendation?****

## Metrics

There are 3 metrics for any automation:

- ****Started Automation****
  When a profile enters an automation.
- ****Fulfilled Automation****
  When a profile received a recommendation from an automation.
- ****Ended Automation****
  When a profile exited an automation (e.g., when they time out or receive a recommendation).