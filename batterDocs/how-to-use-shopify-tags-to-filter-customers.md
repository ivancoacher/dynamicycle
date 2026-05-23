<h1>How to use Shopify tags to filter customers</h1>

## You will learn

Learn about how to use Shopify tags to filter customers in Klaviyo.

## Before you begin

If you have not already, read our article on [Getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating, before continuing with this article.

## About Shopify tags in Klaviyo

Klaviyo's Shopify integration creates a single “Shopify Tags” property, which is stored as a list data type on the Klaviyo customer profile. This is because, when these tags are used, there are often several tags applied to the same customer.

The difference between lists and strings is that the string data type is used to collect a single word or single phrase, while the list data type is used to collect an array of words or phrases, where each item in the array can be identified individually. When using the Shopify Tags property in a segment or filter, you can include as many available tags as you'd like, using multiple conditions.

## Segment people associated with a single Shopify tag

To create a segment of customers associated with a single Shopify tag:

1. In Klaviyo, click the ****Audience**** dropdown and select ****Lists & Segments****
2. Click ****Create List/Segment**** and select ****Segment****
3. Name your segment
4. Under Definition, choose ****Properties about someone > Shopify Tags****.
5. The ****Type**** field will then automatically set to **List**.
6. Type the name of the tag you'd like to use in the box after 'contains'
7. Click ****Create Segment****

![Klaviyo segment builder showing a segment defined by Shopify tags contains newsletter](https://klaviyo.zendesk.com/hc/article_attachments/28713327903771)

## Segment people associated with multiple Shopify tags

To create a segment of customers associated with multiple Shopify tags:

1. In Klaviyo, click the ****Audience**** dropdown and select ****Lists & Segments****
2. Click ****Create List/Segment****, and select ****Segment****
3. Name your segment
4. Under Definition, choose ****Properties about someone > Shopify Tags****
5. The Type field will then automatically set to **List**.
6. Type the name of the first tag you'd like to use in the box after 'contains'
7. Click ****And****
8. Add another condition for each tag you would like to use, just like you did the first one
9. Click Create Segment.

![Klaviyo segment builder showing segment defined by Shopify tags contains tag1 and Shopify tags contains tag2](https://klaviyo.zendesk.com/hc/article_attachments/28713327901595)

## Segment people without any Shopify tags

You might want to create a segment of people who are not associated with any Shopify tags. To create this segment:

1. In Klaviyo, click the ****Audience**** dropdown and select ****Lists & Segments****
2. Click ****Create List/Segment**** and select ****Segment****
3. Name your segment
4. Under Definition, choose ****Properties about someone > Shopify Tags****
5. Update Type to **List**
6. Choose the option **is empty**
7. Click ****Create Segment****

![](https://klaviyo.zendesk.com/hc/article_attachments/28713333528347)

## Segment people without a specific Shopify tag

You might want to create a segment of people who are not associated with a specific Shopify tag. To create this segment:

1. In Klaviyo, click the ****Audience**** dropdown and select ****Lists & Segments****
2. Click ****Create List/Segment**** and select ****Segment****
3. Name your segment
4. Under Definition, choose ****Properties about someone > Shopify Tags****
5. Update Type to **List**
6. Select ****doesn't contain****, then select the tag you want to exclude
7. Click ****Create Segment****

****![](https://klaviyo.zendesk.com/hc/article_attachments/28713327919259)****

## Use Shopify tags in a profile filter

You can also use Shopify tags within a profile filter, just like you did when building a segment.

1. When editing the profile filter, select ****Properties about**** ****someone > Shopify Tags > contains****
2. Select the tag you wish to use as your filter
3. Make sure Type is set to **List**

![Klaviyo flows builder trigger setup showing profile filter Shopify tags contains newsletter](https://klaviyo.zendesk.com/hc/article_attachments/28713327909019)

## Additional resources

- [Understand properties](https://help.klaviyo.com/hc/en-us/articles/115005074627-Add-Custom-Properties-to-a-Contact-Profile#how-to-use-custom-properties)
- [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932-Getting-Started-with-Flows)
