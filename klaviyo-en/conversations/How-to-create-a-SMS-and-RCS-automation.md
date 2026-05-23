---
id: 34158785231515
title: "How to create a SMS and RCS automation"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/34158785231515-How-to-create-a-SMS-and-RCS-automation"
section: "Automations"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-21T13:54:40Z"
language: en
---

Only Owners, Admins, and Managers can access this feature, and you must have also set up SMS in Klaviyo.

## You will learn

Learn how to build an automation, a type of text message conversation that allows you to ask questions, followup to responses, and send personalized recommendations. You can build two types of automations

- Branched automation from keywords and/or question choices
- Single-step automation with a message

For instance, you can run quizzes, surveys, one message keyword responses, and buying guides all through SMS and RCS. Not only is this a quick and easy way to engage your audience, it is a great way to gather zero-party data to inform your marketing strategies.

Note that this article focuses on the steps to create an automation. For details on how automations work, their settings, etc., see [getting started with automations](https://help.klaviyo.com/hc/en-us/articles/34158391513627).

## Before you begin

Please note the following:

- Automations only reply to text messaging SMS subscribers.
- SMS automations are not available for [branded sender IDs](https://help.klaviyo.com/hc/en-us/articles/6637671573403#branded-sender-ids2), as this number type cannot receive text messages. They are available for RCS-enabled accounts and RCS-enabled phones.
- Your outbound messages use credits in your billing plan.

## Setup an automation

1. Navigate to ****Automations****.
2. Click ****Create automation****.
3. Once in the new automation, click on the ****Trigger****.
4. Select a trigger type from the right sidebar, either:

- ****Always on**** (automation will always send and is not time bound).
  or
- ****Message response**** (specific to a campaign or flow message).
  ![](https://klaviyo.zendesk.com/hc/article_attachments/36044245577243)

- Automations require an inbound channel match. If a customer messages a brand through an automation, their message must be sent through the same channel in order for the automation to work.
  - For example, there's an automation configured via SMS. A customer must reply to that automation via the SMS thread in order for it to work. They can't reply via WhatsApp, etc.

## Set up trigger keywords

1. Type in the word you want as the trigger keyword. Please note that:

   - Depending on the type of trigger, each one works differently
     - ****Always on****
       - Matching type: Needs an exact match.
         - Ex: if you use “Pets” as a trigger keyword, the automation will not trigger for “Pets,” and not “pet” or “petsitter."
     - ****Message response****
       - Matching type: It checks to see in an inbound message text contains a match, or what's called "fuzzy matching."
         - Ex: if you use “Pets” as a trigger keyword, the automation will trigger for “Pets,” and “pet” or “petsitter.
   - Please note that trigger keywords:
     - Must be 3 or more characters. Max characters is 20.
     - Must be unique (i.e., they cannot be used for any other automation)
     - Can be a phrase and contain spaces: "I love pets"
     - Trigger keywords are not case sensitive. "PETS" will still trigger "pets."
     - Cannot contain special characters (i.e., +, -, &)
     - Cannot be linked to a subscribe or compliance keyword (i.e., STOP, JOIN)
2. Click ****Save****.

   - Optional: to add more trigger keywords:
     - Click the trigger again.
     - Select ****Add keyword****.
3. Optional, but highly recommended: to set profile properties based on the keyword trigger, toggle on the ****Assign responses as a profile property**** option.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47685210935835)

   - For the example below, this creates a new custom profile property of “Shopping Category” to be either “Bags,” “Jackets” or “Bottoms”
4. Select ****Save****.

## ****Build a branched automation****

### Branching from Keywords

1. Click the ****black dot**** on the keyword tile to open the ****Action Menu****
2. From here, you can Add Question or Add Message from ****an individual keyword**** if you want create a custom response from a keyword

   - For example, asking a new set of questions, or sending a single message, if someone replies with "Bags" "Jackets" or "Bottoms"![](https://klaviyo.zendesk.com/hc/article_attachments/47685210939035)

   A branched keyword automation with personalized questions for each keyword

   ![](https://klaviyo.zendesk.com/hc/article_attachments/47687079582491)
3. Or you can have all keywords branched to the same message or question by clicking on the large Add question button

- For example, adding the same question or message from all keywords: or a single message if someone replies with "Bags" "Jackets" or "Bottoms"

![](https://klaviyo.zendesk.com/hc/article_attachments/47685210943131)

### Creating Branches from Questions

1. After adding a question, you can add another card branching from a question's choice. The branched path can be a Question, Message, or Recommendation
2. To open the A****ction Menu,**** click the black dot on the question choice

![](https://klaviyo.zendesk.com/hc/article_attachments/47687068899611)

#### Add Question

1. Click ****Add Question**** to ask a question with multiple choices.

   - Optional: name your question in the **Internal name** field. Naming your messages makes it easier to refer back to them later.
2. Add your question in the Question box.

   - Include at least 2 choices for the question. Note that:
     - Choices are numbered sequentially.
     - Subscribers can reply with either the choice text or the number.
     - Choices are recognized using “fuzzy” logic:
       - A choice can appear anywhere in a message (including as part of another word).
       - Abbreviations or misspelled words may be recognized (although it is not guaranteed).
     - Be 1 or more characters. Max characters is 20.
     - Best practices for choices are to not use:
       - Single numbers or letters as choices (e.g., the number “21” or only the letter “A”).
       - Hard-to-spell words.
       - Long phrases.
3. Select ****Save****.
4. Unique questions can be added to every question's response if desired.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47687068906779)
5. Optional, but highly recommended: to set profile properties based on choices, toggle on the ****Assign response as a profile property**** option in the Settings tab.
   1. For the example below, the response "Backpack" can be saved as a new custom profile property for "Bag Type Preference."

![](https://klaviyo.zendesk.com/hc/article_attachments/47687079594651)

#### Add Message

1. Click ****Add Message**** to respond with plain text.
   1. Optional: name your message in the **Internal name** field. Naming your messages makes it easier to refer back to them later.
2. Select ****Save****.
   1. You cannot add Recommendation or Question after adding a Message

![](https://klaviyo.zendesk.com/hc/article_attachments/47687079597083)

#### Add Recommendation

1. Click ****Add Recommendation**** to respond with plain text and an image.
2. Select the Response Combinations for the Recommendation
   1. Note: Recommendation combinations are automatically selected for you because that's what matches the branched path you have already create
3. Select ****Save****.
   1. You cannot add a Message or Question after adding a Recommendation
4. To view where the recommendation is connected and associated branches, click the branch or hover over the Recommendation in the drawer.

![](https://klaviyo.zendesk.com/hc/article_attachments/47687079604123)

![](https://klaviyo.zendesk.com/hc/article_attachments/47687068941211)

![](https://klaviyo.zendesk.com/hc/article_attachments/47687079618075)

#### Connect To

1. Click ****Connect to**** to branch an existing question response to another card: question, message, or recommendation
   ![](https://klaviyo.zendesk.com/hc/article_attachments/47685210948251)
2. Select the card in the dropdown menu. Hovering over the card name will help you see which one you will be selecting.
3. Click ****Connect**** to build a branch from the question choice to another card

- You can have multiple branches leading, or converging, to one card

![](https://klaviyo.zendesk.com/hc/article_attachments/47685221202587)

### Branching from Questions

1. After adding a question, you can add another action from a question's choice
2. For example, if a user replies with "Beginner" for a skiing experience question, you can create a new automation path for that response.
3. The automation path could be a message, question, or recommendation

### Isolated Cards or Branches

1. It's possible for a card to be isolated from a branch when a question, message, or recommendation is disconnected from an original path
2. Once a card becomes isolated, Recommendations need to be reset with the updated combinations.
3. Isolated cards appear underneath the primary branched paths
4. Automations cannot be activated with isolations. They need to be connected to a card in order to continue. The easiest way to do this is by selecting Connect To and selecting exists cards. The card will be automatically re-branched in the area where it's newly connected

![](https://klaviyo.zendesk.com/hc/article_attachments/47687068952219)

###

## ****Build a Single-step Automation****

### Set up trigger keywords

1. Type in the word you want as the trigger keyword. Please note that:

   - Depending on the type of trigger, each one works differently
     - ****Always on****
       - Matching type: Needs an exact match.
         - Ex: if you use “Pets” as a trigger keyword, the automation will not trigger for “Pets,” and not “pet” or “petsitter."
     - ****Message response****
       - Matching type: It checks to see in an inbound message text contains a match, or what's called "fuzzy matching."
         - Ex: if you use “Pets” as a trigger keyword, the automation will trigger for “Pets,” and “pet” or “petsitter.
   - Please note that trigger keywords:
     - Must be 3 or more characters. Max characters is 20.
     - Must be unique (i.e., they cannot be used for any other automation)
     - Can be a phrase and contain spaces: "I love pets"
     - Trigger keywords are not case sensitive. "PETS" will still trigger "pets."
     - Cannot contain special characters (i.e., +, -, &)
     - Cannot be linked to a subscribe or compliance keyword (i.e., STOP, JOIN)
2. Click ****Save****.

- Optional: to add more trigger keywords:
  - Click the trigger again.
  - Select ****Add keyword****.

### Add Message for Single-Step Automation

1. Click ****Add Message**** to respond with plain text to the keywords.

   - Optional: name your message in the **Internal name** field. Naming your messages makes it easier to refer back to them later.![](https://klaviyo.zendesk.com/hc/article_attachments/47685210951963)
2. Select ****Save****.

- Please note:
  - At this point you can save the automation and are ****not required to add a Recommendation or Question.****
  - You cannot add Recommendation or Question after adding a Message

![](https://klaviyo.zendesk.com/hc/article_attachments/47685210954523)

### Add Question

1. Click ****Add Question**** to ask a question with multiple choices.

   - Optional: name your question in the **Internal name** field. Naming your messages makes it easier to refer back to them later.
2. Add your question in the Question box.

- Include at least 2 choices for the question. Note that:
  - Choices are numbered sequentially.
  - Subscribers can reply with either the choice text or the number.
  - Choices are recognized using “fuzzy” logic:
    - A choice can appear anywhere in a message (including as part of another word).
    - Abbreviations or misspelled words may be recognized (although it is not guaranteed).
  - 3. Optional: to add more choices, select ****Add Choice****.

    4. Optional, but highly recommended: to set profile properties based on choices, toggle on the ****Assign response as a profile property**** option in the Settings tab.

- For the example below, this creates a new custom profile property of “Favorite Season” to be either “Summer" or “Winter."
  ![](https://klaviyo.zendesk.com/hc/article_attachments/44707568373275)

  5. Select ****Save****.

  6. Optional: add more questions by clicking the plus (+) button and selecting ****Add question****.
- Number of messages are limited depending on the automation trigger.
  - Always on
    - Limited to 4 questions.
  - Message response
    - Limited to 3 questions.

### ****Note: Questions formatted for RCS****

1. Click ****Add Question**** to ask a question with multiple choices.

- If your account is RCS-enabled, you will see a RCS toggle in the Question previewer
- RCS formatting depends on the phone device
  - iOS are buttons
  - Android are a chiplist
- Users can click on these interactive components to reply to a question in an automated conversation
- RCS formatting only appears for RCS-enabled phones
- Note: The RCS messages are formatted as Basic RCS to keep the credits cost aligned with SMS
- To learn more about RCS, [visit this article](https://help.klaviyo.com/hc/en-us/articles/41066240307483)

****iOS****

![](https://klaviyo.zendesk.com/hc/article_attachments/46642244907931)

****Android****

![](https://klaviyo.zendesk.com/hc/article_attachments/46642244910235)

## Complete your automation

### Add recommendations or Add Message

1. After your questions, select the plus (+) button and then click ****Add recommendation or Add Message**** to finish the automation.

### Optional: adjust your settings

Optional: adjust any session settings for your automation. To do so:

1. Click the gear icon in the upper right.
2. Select ****Session settings****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/34194150418715)
3. You can update the following settings:

- Reprompt response
- Fallback response
- Maximum number of reprompts
- Maximum timeout (in hours)
- Channels (WhatsApp)

### Preview and turn on an automation

Once you're happy with your automation:

1. Preview the automation by clicking the "play" button in the upper right

   - The preview is slightly different from the live experience. It doesn't catch typos or show link shortening. Learn more about [previewing an automation](https://help.klaviyo.com/hc/en-us/articles/34175751807515).
   - For RCS automations, the buttons and chiplist will appear correctly
2. Double-check your trigger keywords, questions and choices, messages, and recommendations.

   - Once the automation is on, you must turn it off to edit it, which causes it to immediately drop everyone currently in the automation.
3. Click ****Turn on**** in the upper right.

Once you turn on an automation, it will send to any SMS subscriber who sends a trigger keyword.