<h1>How to create and target a segment of recent cart abandoners</h1>

## You will learn

Learn how to identify site visitors who have recently abandoned a cart in order to target them across marketing channels. For example, you can create a recent cart abandoners segment and sync it to Facebook Custom Audiences to drive them back to your site, or you can create an exit-intent popup targeting shoppers as they're about to leave your website. While it's not possible to dynamically display the specific items left in someone's cart as you would in an abandoned cart email, you can still remind them of items left behind with the language and CTA you use.

Want to send an email to someone when they abandon a cart? Check out our [guide to creating an abandoned cart flow.](https://help.klaviyo.com/hc/en-us/articles/115002779411-Guide-to-Creating-an-Abandoned-Cart-Flow) Emailing cart abandoners should be accomplished using a flow, rather than a campaign sent to a segment, in order to send timely reminders to shoppers with items that are still left in their carts.

## Create a segment of recent cart abandoners

1. Navigate to ****Audience > Lists & Segments**** from the Klaviyo navigation menu.
2. Click ****Create List/Segment****.
3. Choose ****Segment****.
4. Create a segment with the following definition:
   ****What someone has done (or not done) > Started Checkout > at least once in the last 1 week
   AND
   What someone has done (or not done) > Placed Order > zero times in the last 1 week
   ![A segment of site visitors who recently abandoned a cart](https://klaviyo.zendesk.com/hc/article_attachments/28705663512731)****

The time constraint within the segment (1 week, in this example) can be adjusted based on your marketing needs.

Due to [how segments with relative time conditions work](https://help.klaviyo.com/hc/en-us/articles/115005233488-How-Dynamic-Segments-Update), this segment will not update in real-time, but instead will update every 24 hours.

### Are you using Amazon Buy with Prime?

If you're using Buy with Prime to power payment and fulfillment for any of the products on your store, there's another condition you should add to your segment. First, make sure to do the following:

- [Integrate Buy with Prime with Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/14708088221467) to bring Buy with Prime data into your Klaviyo account.

Then:

- Add another AND, followed by the condition **Placed Order** (Buy with Prime) **zero times in the last 1 week** to the segment above.

## Target cart abandoners

### With an exit-intent form

Use the [sign-up form builder](https://help.klaviyo.com/hc/en-us/articles/360026474752) to design the form that you would like to display when someone is about to navigate away from your site but still has items in their cart. You will likely want to choose a popup, flyout, or full page form so that you can capture shoppers' attention.

In the ****Targeting & Behaviors**** tab, configure the following settings:

- On the ****Display**** tab:
  - Under **Timing**, configure the form to appear ****Based on rules > When visitor is exiting the page****.
  - Under **Frequency**, uncheck the **Don't show again if form was submitted or if go to URL button was clicked**. This ensures that someone will see the form more than once, in the event that they abandon a cart multiple times. Then, under **After a visitor closes this form, show again after** timeframe to ensure that shoppers aren't consistently seeing this form within the same browsing session. In our example, we've set a 30-day timeframe before a shopper will see the form again.
    ![The Display menu within the Targeting and behavior tab of the form builder showing an example form set to display when a visitor exits the page and set to show again after 30 days.](https://klaviyo.zendesk.com/hc/article_attachments/28706697860763)
- On the ****Targeting**** tab:
  - Under **Visitors**, select ****Show to specific profiles in a list or segment****, then configure the form to only display to visitors in your recent cart abandoners segment.
  - As a safeguard, under **URLs**, exclude it from displaying on the order confirmation page. Alternatively, only target the form to certain pages on your site, like your homepage.
    ![The Targeting menu within the Targeting and behaviors tab of the form builder showing an example form set to only show to visitors in the abandoned cart segment, and only display on the homepage URL.](https://klaviyo.zendesk.com/hc/article_attachments/28706697867291)

Additionally, configure a call-to-action (CTA) that either brings shoppers back to their cart or directly to the checkout page. Click on the main CTA button in the form preview, then select ****Go to URL**** as the button **Action**. Then, set your checkout or cart URL as the destination URL.

### On Facebook

You can target Facebook users in a similar way using Klaviyo's integration with Facebook. Before syncing a segment of recent cart abandoners to Custom Audiences, ensure that you [have the Facebook integration set up](https://help.klaviyo.com/hc/en-us/articles/115005082127-Integrate-Facebook-Advertising-with-Klaviyo).

Once you have the integration configured, you can sync any segment in Klaviyo to a Facebook Custom Audience. As mentioned above, you may want to extend the timeframe of the segment if you are planning to sync it to Facebook in order to reach a broader audience.

Follow the prompts to create a new Custom Audience. Next, in Facebook, build an ad to display to this audience of recent cart abandoners. Update the CTA link in the ad to direct shoppers back to their cart, the checkout page, or your general site. For more information on this process, head to our course on [integrating owned marketing with your Facebook ad strategy.](https://academy.klaviyo.com/integrate-owned-marketing-with-your-facebook-advertising-strategy)

## Additional resources

- [Advanced segmentation reference](https://klaviyo.zendesk.com/hc/en-us/articles/360035312491)
- [How to create an abandoned cart flow](https://klaviyo.zendesk.com/hc/en-us/articles/115002779411)
