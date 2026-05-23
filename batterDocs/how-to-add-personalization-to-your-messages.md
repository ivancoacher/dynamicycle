<h1>How to add personalization to your messages</h1>

## You will learn

Learn how to add basic personalization tags to your email, SMS, and push messages. Personalization allows you to use your customer data to create an individualized experience for every contact, and allows recipients to take subscription-related actions from within a message.

For specific examples of personalization variables and more advanced use cases, head to our [message personalization reference](https://klaviyo.zendesk.com/hc/en-us/articles/4408802648731).

## Key terms

- ****Profile personalization****
  Personalization based on special Klaviyo profile properties, like first name or email address. Learn about [profile personalization variables](https://help.klaviyo.com/hc/en-us/articles/4408802648731#h_01HBRGTJ3G3Q55VQ136Z977SBR).
- ****Custom personalization****
  Personalization based on custom profile properties you create and collect, like birthday or hair color. Learn about [custom personalization variables](https://help.klaviyo.com/hc/en-us/articles/4408802648731#h_01HBRGTJ3H2M4N326FXPBSA4AN).
- ****Event personalization****
  Personalization based on data stored within an event, like the products someone ordered in a **Placed order** event. Learn about [event personalization variables](https://help.klaviyo.com/hc/en-us/articles/4408802648731#h_01HBRGTJ3H2M4N326FXPBSA4AN).

## Personalization types

You can add profile, custom, and event personalization to email, SMS, and push messages in both campaigns and flows.

- Learn how to [add profile and custom personalization to a message](#h_01HBRK2VCRSQ7XS3CTQ5J32WKN).
- Learn how to [add event personalization to a message](#h_01HBRK2VCR47K2SY2Q6R4RYWE1).

## Add profile and custom personalization to an email, SMS, or push message

1. Click the personalization icon within a text block, or ****Add personalization**** in any other text field (e.g., text cell in a table block, SMS, or push message).
   ![](https://klaviyo.zendesk.com/hc/article_attachments/32002744507675)
2. Search for the property you’d like to add or scroll through the list.
3. Select a property.
4. If needed, add default text (i.e., text to appear if personalized data is unavailable).
5. Click ****Insert****.

![Personalization set up](https://klaviyo.zendesk.com/hc/article_attachments/28723662219419)

### Additional profile and custom personalization options

If you don't see the personalization options you'd like to use, visit the preview pane for more detailed options.

1. Click ****Preview & test****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627733950235)
2. Search or navigate through the available profiles to locate someone with the information you'd like to add to your message.
4. Hover over the variable’s name until you see the message **Copy {{ person.variable\_name }} variable**, then click to copy it.
   ![SMS profile personalization](https://klaviyo.zendesk.com/hc/article_attachments/28723662199963)
5. Paste the variable into a block in your message.

Learn more about [using the preview panel for message personalization](https://klaviyo.zendesk.com/hc/en-us/articles/27843522951707).

## Add event personalization to an email, SMS, or push message

Your message ****must**** be sent through a flow that is triggered by the event containing your event property (or properties) in order for event personalization to populate. Only use properties from a single metric in a template. However, you may also use profile variables in a template that uses event variables.

### Basic event personalization

Basic event personalization may be available in the ****Personalization**** menu, depending on your ecommerce platform.

1. Open a message (i.e., email, SMS, or push) within an event-triggered flow.
2. From any text field, click ****Personalization****.
3. Under ****All types****, select ****Event****.
4. Choose an event property.
5. Optionally, add a default value, then click ****Insert****.

### Advanced event personalization

For more advanced event properties, use the preview window to copy personalization tags.

1. Click ****Preview and test**** from the template editor.
   ![preview and test button](https://klaviyo.zendesk.com/hc/article_attachments/28723662189851)
2. Under **Preview data source**, click ****Event****.
3. Select an event from the dropdown.
   ![Choose an event](https://klaviyo.zendesk.com/hc/article_attachments/28723684384795)
4. Open an SMS/push message in a metric-triggered flow.
5. Click ****Preview & test****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/33627697204507)
6. Open the ****All properties**** menu.
7. Use the arrow buttons to find an event that includes the variable you’d like to add.

1. For an email template:
2. For an SMS or push message:
3. Scroll through their **Event Properties** until you find the variable you’d like to use.
4. Hover over the variable’s name until you see the message **Copy {{ event.variable\_name }} variable**, then click to copy it.
   ![event data](https://klaviyo.zendesk.com/hc/article_attachments/28723684394651)
5. Paste the variable into a block in your message.

## Set default text

Sometimes, you’ll send a message with personalization tags to someone who hasn’t provided all the data your tags reference. For example, you might send an email to someone who hasn’t shared their first name with you.

When this happens, it’s important to have default text set to prevent blank spaces in place of the missing data. Set default text using the examples below to determine what should appear if data isn’t available.

|  |  |
| --- | --- |
| ****Text with variables**** | ****Output**** |
| Hey `{{ first_name|default:'friend' }}`, any interest in some `{{ person|lookup:'Favorite Food'|default:'tasty treats' }}`? | **Hey friend, any interest in some tasty treats?** |

## Outcome

By using these steps, you can add basic personalization to your emails, like someone’s first name or a product they left in their cart. When the message sends, it will reference the data available for the recipient and populate the tags with custom data.
