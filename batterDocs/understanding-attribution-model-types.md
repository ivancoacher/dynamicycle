<h1>Understanding attribution model types</h1>

## You will learn

Learn about how Klaviyo’s different attribution models work, including how to enable linear attribution on your account and how attribution is calculated.

## Before you begin

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) and [Marketing Analytics](https://help.klaviyo.com/hc/en-us/articles/33789259613595) are not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality.Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn about how to purchase these plans.

By default, Klaviyo uses a co-operative last touch attribution model and Advanced KDP and Marketing Analytics customers can update their attribution model type

## How to update your attribution model

To update your attribution model:

1. Navigate to ****Account**** > ****Settings**** > ****Attribution****.
2. In the **Attribution model** card, select **Last touch** or **Linear** from the dropdown menu.

![](https://klaviyo.zendesk.com/hc/article_attachments/36552316480027)

Once updated, the change will take up to 36 hours to be applied to your account

## Last-touch attribution model

A last touch attribution model gives credit to the final touchpoint before a conversion and will provide an understanding of which touchpoints were most effective at driving conversions.

### Last-touch model example

In the last-touch model below, a customer places an order with a $100 value after interacting with 2 emails and an SMS. Since the SMS message was their final touchpoint before the conversion, it will receive all the credit (i.e., $100 of attributed value) even though the emails may have played a role in the recipient’s decision to purchase.

![](https://klaviyo.zendesk.com/hc/article_attachments/36552316475547)

## Linear attribution models

A linear attribution model equally gives credit to each touchpoint leading to a conversion. Meanwhile, a **Last touch** model only applies the credit to the final touchpoint before a conversion.

In general, linear attribution models are more accurate because they consider the full customer journey leading up to a conversion, rather than just the final touchpoint.

Customers often have multiple touchpoints before a conversion, with each of them ultimately playing a role in the conversion. An attribution model that accounts for this can help you learn what touchpoints are more effective at different stages in the conversion cycle, and help to focus your marketing on the entire customer journey leading up to a conversion.

For a touchpoint to be considered in the linear attribution model:

- The message must be received within the configured lookback window for a channel.
- The interaction event must occur for that message within the configured lookback window.

Learn[how to configure your attribution settings](https://help.klaviyo.com/hc/en-us/articles/11118357030555).

### Linear model example

In the linear model below, a customer places an order with a $100 value after interacting with 2 emails and an SMS. Since the linear model attributes to all the touchpoints equally, they will each receive a third of the credit (i.e., about $33 of attributed value).

![](https://klaviyo.zendesk.com/hc/article_attachments/36552301544603)
