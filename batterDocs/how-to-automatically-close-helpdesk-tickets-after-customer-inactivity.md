<h1>How to automatically close Helpdesk tickets after customer inactivity</h1>

Learn how to automatically close Klaviyo Helpdesk tickets after a set period of customer inactivity. By setting up ticket auto-close, you can streamline your support workflow and keep your Inbox organized.

## About auto-close

Auto-close lets you define how long a ticket stays open if a customer hasn’t replied. Once your specified inactivity period is reached, Klaviyo will automatically close the ticket.

This setting applies to all ticket types (i.e., email, SMS, and web chat), and also works for tickets being handled by the AI Service Agent, if enabled.

## Set up ticket auto-close

1. Navigate to ****Conversations > Inbox****.
2. Click ****Settings****.
   ![Inboxsettings.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39690028974747)
3. Make sure you are on the **General** tab.
4. Under **Ticket auto-close**, select ****On****.
   ![autoclose2.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39690023347611)
5. Set the ****Inactivity period**** to determine how long to wait before closing a ticket without a customer response. You can set a period from 1 to 90 days.

   - Tip: The default is 2 days, but choose a timeframe that matches your typical customer response patterns to avoid closing tickets too soon.
6. Click ****Save****.

When a ticket is auto-closed, its status automatically changes to **Closed******.**** You will also see a notice in the ticket thread: “Ticket closed due to inactivity.”

![autoclose3.jpg](https://klaviyo.zendesk.com/hc/article_attachments/39690023352731)

You can still access closed tickets by filtering the **All tickets** view to ****Closed****.

## FAQs about auto-closed tickets

### If I re-open a closed ticket, does the auto-close period reset?

Yes. If a closed ticket is re-opened, the inactivity timer restarts once the customer replies. Auto-close will apply again if the customer does not respond within your set period.

Note that web chat tickets cannot be reopened once closed. Only email and SMS tickets can be reopened. Learn more about [ticket reopening by channel](https://help.klaviyo.com/hc/en-us/articles/360059002271#h_01JMFEZW49XRXVQGQX7PC6ZKNJ).

### Will snoozed tickets be auto-closed?

Yes. Snoozed tickets can still be auto-closed if the inactivity window is reached and the customer hasn’t replied.

### What if a customer is typing when the timer expires?

Auto-close will be delayed for a few minutes if a customer is actively typing, giving them a chance to send their message.

### Do human agent or AI Agent messages reset the inactivity window?

No. Only customer replies reset the inactivity timer. The timer starts after the agent or AI Agent’s last message and will auto-close the ticket if the customer hasn’t replied within the set window.
