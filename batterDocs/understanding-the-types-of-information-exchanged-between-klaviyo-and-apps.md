<h1>Understanding the types of information exchanged between Klaviyo and apps</h1>

## You will learn

Learn about what types of data are exchanged between Klaviyo and external apps, and where that data is found in your Klaviyo account. When you integrate a third-party application with Klaviyo, the two platforms exchange information. Most data exchange with Klaviyo is one-way; data is pulled into your Klaviyo account so you can leverage a broad scope of your customers' data within Klaviyo.

## Table of contents

1. Types of data
2. Where to view event data
3. Where to view profile data
4. Where to view catalog data

## Types of data

Klaviyo syncs several types of data with external applications:

1. ****Event Data****Events are populated along a customer's timeline each time they take a certain action. Each event - such as **Active on Site**, **Placed Order**, or **Fulfilled Order** - is known as a metric. There can be multiple instances of metric data for one contact, as long as they take the corresponding action more than once. For instance, when a customer places several orders on your website, they will have several **Placed Order** metrics listed on their timeline.
2. ****Profile Data****Profile data describes an aspect of a contact's identity, and is made up of both Klaviyo properties and custom properties. Klaviyo properties are natively tracked within Klaviyo and include attributes such as First Active, Last Active, Source, First Name, and Last Name. [Custom properties](https://help.klaviyo.com/hc/en-us/articles/115005074627) are additional profile data which you can create and are often specific to your business. Common custom properties include gender, birthday, or product preference. Custom properties can also be pulled in through third-party integrations, which allow you to import reviews, ratings, and other information not natively tracked in Klaviyo.
3. ****Catalog Data****Catalog data describes items found within your product catalog. This data is frequently modified on your ecommerce platform as you add or remove products from your store. Examples of catalog data include variants such as color and size. Within Klaviyo, catalog data is pulled in and used to populate product feeds, campaigns, and flow messages.

## Where to view event data

Event data can be viewed in the following places within Klaviyo:

- Profile event timeline
- Profile metrics snapshot
- View metadata
- Metrics tab (found under Analytics)

All event data associated with a customer can be found in their profile. Since you can use event data to build targeted segments and filter flows, you'll find event metrics listed as options within the segment and flow builders.

Use event data to filter and split your flow messaging and to create key segments of your customers to send to. This personalization will make your messaging more relevant to your subscribers, aligning your brand with their journey.

### Event timeline within a profile

You can view a timeline of events associated with a customer within their profile.

1. In your Klaviyo account, click the ****Audience**** dropdown and select ****Profiles****.
2. Select a customer profile.
3. By default, the events filter is set to **All Metrics**. To change this metric, select another option from the dropdown.
   ![Profile for George Costanza showing cancelled order and placed order metrics](https://klaviyo.zendesk.com/hc/article_attachments/28720668777243)

### Metrics snapshot within a profile

Each profile has a **METRICS** snapshot located on the right-hand side. This section quantifies activity both from the last 30 days as well as from all-time. To adjust the metrics shown within this section, click ****Edit**** and select the metrics you want to see. You can choose to display any and all events your customer has experienced in this section.

### Dive deeper into metric data

If a metric is more complex, it can have additional, related data associated with it. This is known as metadata. The information tracked in the metadata will vary according to the metric type. Simple metrics, such as **Received email**, have no associated metadata since there’s no additional data to track with the metric. A **Placed Order** metric, however, is considered to be a complex metric, since it can include the following details about the items in the order: price, style, quantity, discounts, etc.

Within a customer's event timeline, data associated with an event can be viewed in two places:

- ****Metric details****

  Click ****Details**** beneath the metric listing.

  ![WooCommerce Placed Order metric with Details in light gray and timestamp](https://klaviyo.zendesk.com/hc/article_attachments/28720657044507)

  Not every metric contains metadata, but when there is metadata associated with a metric, you’ll see it in **Details**.

  This **Placed Order** event includes metadata related to Item, SKU, Categories, etc.

  ![WooCommerce Placed Order metric with item details about a tee shirt, with collapse in light gray and timestamp](https://klaviyo.zendesk.com/hc/article_attachments/28720668781339)

  All metadata listed in this section can be used in both the segment builder and the flow builder.
- ****Metric timestamp****

  Click on the ****timestamp**** to the right of an event to open an **Activity Details** window.

  ![List with Cancelled Order and Placed Order metrics, both with timestamp ](https://klaviyo.zendesk.com/hc/article_attachments/28720657052059)

  **Activity Details** contains a list of all metadata associated with the metric. Top-level attributes such as **Collections**, **Discount Codes**, and **Items** can be collapsed and expanded to display even more detailed information.

  ![Activity details page showing extra section expanded, including Billing Address details](https://klaviyo.zendesk.com/hc/article_attachments/28720668784539)

  All data listed within **Activity Details** except for data listed in the **extra** section can be used in both the segment builder and flow builder. Data from the **extra** section can only be used in the flow builder, to populate flow email templates.

  For example, the **extra** section may contain images or prices of items. Use this data to populate your abandoned cart emails with images and prices of items your customers left behind.

### The Metrics tab

Click the ****Analytics**** dropdown and select the ****Metrics**** tab to see a list of all tracked metrics. Metrics include events tracked by Klaviyo, as well as events synced through third-party apps. Each metric has an associated icon that indicates where the metric is coming from: Klaviyo-originated metrics are associated with a Klaviyo icon, API-originated metrics are associated with a gear icon, and integrations-originated metrics are associated with their respective icons.

![Metrics tab in Klaviyo showing all metrics including those from Klaviyo, Mailchimp, and Shopify](https://klaviyo.zendesk.com/hc/article_attachments/28720668788507)

### Event options within targeted segments

Event data can be used to define a segment. As a part of the segment set up process, you can choose a definition based on a metric that describes what a customer has or has not done. You can then choose one metric from a list of all metrics available in your Klaviyo account. In the following example, we've chosen a Klaviyo metric.

![Klaviyo segment builder showing a segment named Received with condition has received email at least once over all time](https://klaviyo.zendesk.com/hc/article_attachments/28720668793883)

### Event options within a flow filter

Flows can be filtered based on an event. When you set up a flow filter, you can choose an event metric as part of the filter definition. For example, customers who enter an abandoned cart flow can be filtered out of the flow when they place an order.

Event metrics can also be referenced in a flow email by inserting template tags. Template tags pull event data into an email. For example, you can include an image and price of an item in an abandoned cart email. Check out our guide on [using template tags and variable syntax](https://klaviyo.zendesk.com/hc/en-us/articles/115005084927) for more information.

## Where to view profile data

Profile data and custom profile data can be viewed within your contacts' profile pages. You can also build segments and flows based on profile attributes.

### Profile data listed on a contact record

To find profile data in your Klaviyo account, navigate to the ****Profiles**** tab (under ****Audience****) and click on a contact. Both the **CONTACT** section and the **INFORMATION** section contain profile data, and the **INFORMATION** section contains specific Klaviyo properties and custom data.

![Contact, channels, and information sections of a Profile in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28720668801435)

Each piece of data listed in the **INFORMATION** section is known as a 'Klaviyo property', while each piece of data listed in the **Custom Properties** subsection under **INFORMATION** is referred to as a custom property.

You can add these custom properties to a contact's profile to track specific information about your customers.

### Profile data within segment definitions

You can use profile attributes to build targeted segments. For example, if you’re running a promotional event you’d like to target towards customers in La Jolla, CA, you can use the region attribute to build a segment of your contacts who live within 25 miles of that zipcode.

![Klaviyo segment builder showing segment called Spring LaJolla Event](https://klaviyo.zendesk.com/hc/article_attachments/28720657083547)

### Profile data in flow filters

You can pull profile data into flow filters to determine which customers should remain in a flow.

Flows can also be triggered by a date property. For example, Klaviyo's prebuilt birthday flow references a date field that occurs every year.

## Where to view catalog data

Catalog data includes information related to your product catalog such as photos, descriptions, and stock information. To view the items in your catalog, navigate to ****Content > Products****.

You can insert catalog data into your campaign and flow emails by embedding a product block in your email templates. There are several ways to insert catalog items into your product block. Static catalog items can be inserted into a product block, or you can embed a dynamic product feed instead.

Dynamic product feeds pull catalog items based on an algorithm, so you can choose to display trending items, best selling items, or a collection of items based on a customer's behavior.

### Catalog data in campaign emails

Products can be featured prominently in your campaign emails. For example, you can feature product images, product names, and product prices pulled from your product catalog in your new product launch campaign. Here, we've selected a static product block where you can select images manually from your product catalog.

![Klaviyo template builder with static contact block highlighted in a Memorial Day email](https://klaviyo.zendesk.com/hc/article_attachments/28720668805275)

### Product feeds in flow emails

Product feeds pull catalog data so they can be displayed dynamically in a customer email. Here, we've selected a dynamic product block in order to utilize a product feed. Your product feed could be configured to display trending items, for instance.

![Klaviyo template builder with dynamic contact block highlighted in a Memorial Day email](https://klaviyo.zendesk.com/hc/article_attachments/28720657089563)

## Additional resources

- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932)
- [Guide to creating segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)
- [Understanding how information Is exchanged between Klaviyo and apps](https://klaviyo.zendesk.com/hc/en-us/articles/360030265051)
- Need more help integrating with Klaviyo? Check out [Klaviyo's Agency Partners](https://connect.klaviyo.com/)
