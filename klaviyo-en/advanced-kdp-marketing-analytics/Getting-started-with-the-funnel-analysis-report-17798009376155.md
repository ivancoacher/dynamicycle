---
id: "17798009376155"
title: "Getting started with the funnel analysis report"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17798009376155-Getting-started-with-the-funnel-analysis-report"
section: "Customer insights"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:31Z"
language: "en"
---
## You will learn

Learn how to use funnel analysis reporting to review a customer’s journey with your brand and where they may potentially drop off before an action or conversion. Knowing more about where a customer may drop off is helpful in understanding where you can optimize your marketing funnel.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

![](https://fast.wistia.com/embed/medias/j3isaa11aj/swatch)

## Accessing the dashboard

1. If you are an Advanced KDP customer, navigate to ****Advanced KDP > Intelligence > Customer Insights > Funnel analysis********.**** Alternatively, if you are a Marketing Analytics customer, navigate to ****Marketing Analytics > Customer Insights > Funnel analysis****.
2. If this is your first time creating a funnel analysis, select ****Create funnel**** as shown below.

![Button labeled Create funnel in upper right corner](https://klaviyo.zendesk.com/hc/article_attachments/28711731143835)

You will only be able to create 1 funnel dashboard per account with up to 10 funnel analysis cards. As you follow the steps in the next section to customize your dashboard, you will be adding funnel cards or graphs to this 1 dashboard.

## Customizing and adding your funnel analysis cards

When creating a new card or funnel graph, you will have the options to name your card (note that this will apply to each individual card or graph in your dashboard), filter by a particular segment if you choose, and add your specific metric steps or actions.

You can also choose to add additional filters to each step to hone into more specific subsets of customers. These options will be available in the settings menu that appears from the right of your screen when selecting ****Create funnel****, as shown below.

![Settings menu that appears when clicking on Create funnel button](https://klaviyo.zendesk.com/hc/article_attachments/28711702172187)

1. Name your card as something that is identifiable to the customer journey you are trying to review. For example, “New customers who did not purchase in the last 90 days.”
2. Next, you have the option to filter by 1 customer segment. This is helpful if you want to focus on a particular subset of your customers and their behaviors. Open the ****Filter by segment (optional)**** dropdown and either choose your segment from the alphabetized list or search in the **Filter** field.

It is not required for you to choose a specific segment for your funnel card. If you do not choose a segment, the funnel analysis will look across all profiles within your chosen time frame and the funnel setup.

![Optional filter by segment dropdown shown open with segments to choose from list](https://klaviyo.zendesk.com/hc/article_attachments/28711702161051)

3. In the next step, you have the option to specify the maximum time window between the first and last step of the funnel you are creating. Open the ****Days**** dropdown and choose from options for ****Hours****, ****Days****, or ****Weeks****, and then input a whole number in the field to the left.

![Completion window dropdown open showing hours, days, weeks](https://klaviyo.zendesk.com/hc/article_attachments/28711731169947)

You will then come to the section to configure your funnel steps or events and see where customers are potentially dropping off in their journey.

It’s important that these steps are in the right logical order, starting with **Step 1** to ensure that you can accurately capture a customer moving through the funnel. For example, putting a conversion metric like **Started checkout** before a metric such as **Active on site** may produce inaccurate data as you may not be following the most logical action order. In addition, certain metrics (i.e., Klaviyo events and ecommerce events) together may also produce artificial drops in numbers and inaccurate results. Learn more in our FAQ’s section below.

4. Open the ****Metric**** dropdown and either choose your metric event from the alphabetized list or search in the **Filter** field. This list will contain all Klaviyo events and any events from your ecommerce integrations.

5. Click ****Add Step**** if you want to add more than the required 2 steps.

You are required to have at least 2 metric events to create a funnel, but no more than 5 metric events total. You can also delete metric steps by clicking on the trash can icon that appears to the upper right.

Underneath each step, you have the option to add a filter to further refine your customer subset. For example, If you are looking at a segment of repeat customers, you may add a filter by **Country** to review where these orders are primarily coming from.

6. To add a filter to a step, open the ****Select an additional filter**** dropdown and either choose your metric event from the alphabetized list or search in the **Filter** field.

If you choose to add filters, you will need to add a value. Values are related to your chosen metric and filter types. For example, if you choose a non-conversion metric such as **Active on site** and a filter as **Attributed Message**, you will see options to choose the specific attributed message from the value dropdown.

7. To add a value to a step and filter, open the ****Select a value**** dropdown and either choose your metric event from the alphabetized list or search in the **Filter** field.

8. Once you are satisfied with your funnel setup, click ****Create****.

### Troubleshooting potential card errors

If your funnel has been successfully created, you will see your new card appear at the top of the dashboard.

However, if you receive an error message noting that “Your funnel could not be saved,” refresh the page and try again. If you receive a message that “Something went wrong,” this means that the data is currently not available. You will need to refresh the page manually and see if your data will now load. Additionally, you may receive card errors noting that you are using an inactive segment or 1 or more of your metric events has since been deleted. For this message, either refresh the entire page or make adjustments to your funnel as necessary, and click ****Create**** to save these changes.

Occasionally, you may produce a card with certain metric events as steps, but the numbers may be artificially low or inaccurate. These issues may be related to certain metrics that are being used together (i.e., Klaviyo events and ecommerce events). Learn more these potential discrepancies in our [troubleshooting funnel analysis guide](https://help.klaviyo.com/hc/en-us/articles/17797984549659).

## Reviewing your results

Once your funnel card has been created, it will appear at the top of your dashboard. You can always adjust the order of your cards if needed. Below is an example of a funnel card with 5 steps.

![](https://klaviyo.zendesk.com/hc/article_attachments/38256052710299)

Depending on how many steps you added, each card will display a bar graph per step reflecting your step order from left to right.

The first bar on the left represents the aggregated total number of customers that qualify for that metric event within your report’s time frame (reflected in the top number and in the bar itself). Each subsequent bar represents the number of customers who qualify for that particular metric as a subset of the total from the first bar or step (reflected in the top number, percentage, and bar itself).

If we apply this to the example above, this means that of the 18,136 customers who used received an email, 14,336 customers opened the email. And of those 18,136 customers, 3,773 went on to click on the email. Then 1,154 profiles added an item to cart, and ultimately 662 profiles placed an order.

You can also review the overall completion percentage from the first step in your funnel by hovering over any of the bars in card.

## Editing your cards

1. To edit a card, find the particular funnel card or graph that you want to adjust and click ****Edit****.
   ![Edit button in upper right of the example funnel card created](https://klaviyo.zendesk.com/hc/article_attachments/28711702197915)
2. The settings menu will appear from the right. Make any edits or updates that you need to your funnel steps.
3. Once you are satisfied with your edits, click ****Save****.

If you have made edits and do not click ****Save****, it will prompt you to either discard your changes or cancel and return to editing and saving changes. Choose ****Discard**** changes if you do not wish to save your edits. Otherwise, choose ****Cancel**** to go back to the settings menu and save your changes.

## Cloning your funnels

You can also clone funnels so you can quickly iterate without having to recreate funnels from scratch. To clone an existing funnel, click the action menu (i.e., 3 dot menu) and select the ****Clone**** option.

![](https://klaviyo.zendesk.com/hc/article_attachments/35615563094043)

This will duplicate your funnel so you can make changes while preserving the original.

## Customizing the main dashboard view

In addition to customizing the setup of each individual card, you can also customize settings for the entire dashboard itself.

### Adjusting the dashboard time frame

By default, the funnel dashboard and all cards will use the last 7 days as the time frame.

However, you can adjust this to the following options:

- Last 7 days
- Last 30 Days
- Last 90 Days
- Last 365 Days
- Week-to-date
- Month-to-date
- Year-to-date
- Custom (choose your own start and end date)

To adjust the dashboard date:

1. Click on the time frame dropdown at the top of the report.

![The Timeframe dropdown at the top of the report showing 7 days](https://klaviyo.zendesk.com/hc/article_attachments/28711731167003)

2. Choose your desired time frame.

Whatever time frame you choose will update the entire dashboard. Note that only segments and profiles that fit the criteria of your first event step and fall within the time frame you choose will be reflected in the cards.

## Adjusting the order of the dashboard

To adjust the order of your cards, click and hold the ****dot icon**** at the top of a card. You can drag and drop each card to its desired location.