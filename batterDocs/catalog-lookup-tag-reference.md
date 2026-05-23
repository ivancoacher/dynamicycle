<h1>Catalog lookup tag reference</h1>

## You will learn

Learn how to use the catalog tag, which allows you to reference specific product information from your catalog within your emails, SMS, and push messages. This is useful when you want to create custom product recommendations, or cross-reference product information. For example, if you're using your own recommendation engine, you can pass your own product recommendations as event or profile data to Klaviyo, and then utilize that data in templates.

Please note that this guide is designed for tech-savvy marketers or customers who have access to a developer.

## The {% catalog %} tag

The `{% catalog %}` tag uses the following syntax:

```
{% catalog itemID unpublished="cancel" %}
...
{% endcatalog %}
```

Replace **itemID** with the Product ID of the product you are referencing. This is the Product ID as synced from your own product catalog. Note, this lookup is specifically for the Product ID and not the SKU.

Including **unpublished="cancel"** will ensure that you don't send your message in the event that the item referenced is unpublished. This argument is optional.

- If any item referenced in your message is unpublished in your catalog at the time of lookup, the entire message will be skipped.
- For a given flow message, you can navigate to ****Analytics > Recipient Activity > Other**** and see a list labeled **Skipped: Catalog Item Unavailable**. This list includes all profiles that were skipped because an item featured in the message was out-of-stock or otherwise unavailable.

When using this feature, between the opening and closing catalog tags, you can reference specific data from the item associated with the **itemID** in your Klaviyo product catalog.

The following data is available to reference inside of a `{% catalog %}` block.

| ****Template tag**** | ****Name**** | ****Description**** |
| --- | --- | --- |
| `{{ catalog_item.description }}` | Description | The description of the item. |
| `{{ catalog_item.url }}` | URL | The url for accessing the item in your store. |
| `{{ catalog_item.title }}` | Title | The title of the item. |
| `{% currency_format catalog_item.metadata|lookup:"price" %}` | Price | The price of an item. This tag formats the item price with the correct currency prefix. |
| `{{ catalog_item.currency_symbol }}` | Currency Symbol | The graphic symbol used to denote a currency unit |
| `{{ catalog_item.currency_code }}` | Currency Code | The alphabetic code used to denote currency |
| `{{ catalog_item.featured_image.full.src }}` | Full image | The url for the full image of the item. Use this inside of an image block, or an <img> tag. |
| `{{ catalog_item.featured_image.thumbnail.src }}` | Thumbnail | The url for the full image of the item. Use this in an <img> tag in custom HTML, or use it as a dynamic image placeholder URL surrounded by the opening and closing {% catalog %} tags |
| `{{ catalog_item.id }}` | Id | The Product ID of the item. |
| `{{ catalog_id }}` | Catalog ID | The ID of the catalog so you can specify which catalog to pull from if you have multiple. |

There may be additional data fields available that are considered metadata. To reference one of these additional item properties, you can use the variable syntax: {{ catalog\_item.metadata.color }}. In this case, the variable will pull in the "color" value associated with the item stored in the item's metadata.

To access a preview of all available details stored on an item — including all metadata — add the following snippet to a text block in a test template, and update **itemID** with the Product ID of one of the current products in your catalog.

```
{% catalog itemID %}
{{ catalog_item }}
{% endcatalog %}
```

Then, preview the message. This preview provides a raw version of all the data available for your products.

## Filtering by catalog ID

If you have multiple catalogs you can specify which catalog you want to pull from using the `{{catalog id}}` tag. For example, you might have a catalog synced through a Klaviyo integration such as Shopify, catalog synced via API, or a custom catalog feed. Tag details may vary based on your integration. In the following example, multiple catalogs are synced to the same Klaviyo account and we want to pull a product description from a specific product contained in an API catalog.

First, find the catalog ID:

1. In Klaviyo, navigate to ****Content > Products****.
2. Select the catalog you want to use from the **All catalogs** dropdown.
   ![Screenshot 2025-05-13 at 12.08.19 PM.png](https://klaviyo.zendesk.com/hc/article_attachments/36947752771483)
3. Copy the catalog ID from the URL.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36947760688539)

Then, find the item ID:

1. After selecting the catalog, select the product you want to use from the catalog.
2. On the product details page, you'll see the Item ID.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/36947760692891)

For the example above, the code would look like:

```
{% catalog "SAMPLE-DATA-ITEM-15" integration="api" catalog_id="1060935"%} {{ catalog_item.description }}{% endcatalog %}
```

## Filtering by locale

Locale aware catalogs like the Shopify catalog in Klaviyo can be searched for by locale. Locale language and region can be referenced with two letter country and language code using ISO 3166 and 639 standards. If a localized product can not be found the default product information will be used.

```
{% catalog "SAMPLE-DATA-ITEM-15" integration="api" catalog_id="1060935" language='fr' region='CA' %} {{ catalog_item.description }}{% endcatalog %}
```

## Look up an item ID passed with an event

Using a catalog lookup with an event is mostly used in the following scenarios:

- If you're using a custom integration where product recommendations are passed along with an event to show in the message. For example, a browse abandonment message where unique recommendations are generated based on viewed items. Instead of populating the single item a customer viewed in the message, you can generate and populate a set of recommended items based on that item viewed. A set of Product IDs needs to be sent to Klaviyo along with the event.
- If you're using a custom integration and you prefer not to send all product details that need to go in an message. For example, with an abandoned cart message, only send the Product IDs of all abandoned items and Klaviyo can look up each one to pull in all relevant details. There's no need for every event to contain product name, price, image, etc. since all of this can be populated by only passing the Product ID to Klaviyo, then looking up the information in your Klaviyo product catalog.

When using a `{% catalog %}` tag with an event, the lookup is based on the Item ID of the catalog item (this will either be Product ID or SKU depending on the integration).

For an event where the identifying value passed is Item ID, the lookup tags will appear like this:

```
{% catalog event.ItemID %}
…
{% endcatalog %}
```

Within this `{% catalog %}` block, add template variables for the data you would like to populate regarding each item (i.e. title, image, etc.)

For example, using the sample catalog item data below, we can build out a `{% catalog %}` block that references key product information:

****Catalog item data:****

```
{
  "description": "Standard issue for all Klaviyos. This t-shirt has the Klaviyo logo on the front and mark diagram on the back.",
  "url": "https://klaviyogear.myshopify.com/collections/klaviyo-classics/products/short-sleeve-t-shirt-1",
  "title": "Classic Klaviyo T-Shirt",
  "featured_image": {
    "full": {
      "src": "https://www.klaviyo.com/media/images/examples/products/klaviyo-tshirt-full.png"
    },
    "thumbnail": {
      "src": "https://www.klaviyo.com/media/images/examples/products/klaviyo-tshirt-thumbnail.png"
    }
  },
  "id": "KLAVIYO-TSHIRT",
  "metadata": {
    "Color": "Grey",
    "Design": "Standard"
  }
}
```

****Template block syntax:****

The syntax for the following `{% catalog %}` block would pull in the item image, item title, and item description from your catalog, for each item in the event:

```
{% for item in event.Items %}
	{% catalog item.SKU %}
 		<img src="{{ catalog_item.featured_image.full.src }}"/>
 		{{ catalog_item.title }}
 		{{ catalog_item.description }}
 	{% endcatalog %}
{% endfor %}
```

If the lookup can’t find the item it’s looking for, the message is skipped and does not send.

## Look up an item ID as a custom property

If you're using your own recommendation engine, you can pass recommended item IDs to profiles in Klaviyo as a [custom profile property](https://klaviyo.zendesk.com/hc/en-us/articles/115000250912). Using a `{% catalog %}` tag, you can reference information from any of these products when messaging this customer.

If the lookup can’t find the item it’s looking for, the message is skipped and does not send.

### Syntax for multiple item IDs stored in a single property

```
{% for item in person|lookup:'Recommended Products' %}{% catalog item %}

<img src="{{ catalog_item.featured_image.thumbnail.src }}" style="display: inline-block; border: none" width="150px" />

<p>{{ catalog_item.title }} {% endcatalog %}</p>

{% endfor %}
```

### Syntax for a single item ID in a profile property

```
{% catalog person|lookup:"Recommended Products" %}

<img style="display: inline-block; border: none;" src="{{ catalog_item.featured_image.thumbnail.src }}" width="150px"/>

  <p>{{ catalog_item.title }} {% endcatalog %}</p>
```

## About the has\_category tag

Use the **has\_category** tag to determine whether an item in your catalog is part of a particular category. It must be used within a catalog lookup tag for a particular item.

Use the sample code below to use this tag, replacing **itemID** with a product ID from your catalog and **category\_name** with all or part of a category name.

```
{% catalog itemID %}
{{ catalog_item.title }}
{% has_category catalog_item "category_name" as in_category %}
{% if in_category %}
I am on sale!
{% else %}
{% endif %}
{% endcatalog %}
```

This example displays the product title, then checks whether the product is in a category, **category\_name**. If this evaluates as **true**, the message “I am on sale!” will appear following the product title.

The **has\_category** tag searches for full and partial matches to the category name you set. For example, if you use “sale” as the category name and a product has a tag “on-sale”, the **has\_category** tag will evaluate as **true** for that product.

## Additional resources

- [How to use product feeds and recommendations](https://klaviyo.zendesk.com/hc/en-us/articles/115005082787)
- [Overview of the email template editor](https://klaviyo.zendesk.com/hc/en-us/articles/115005082447)
