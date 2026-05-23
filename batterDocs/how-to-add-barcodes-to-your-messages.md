<h1>How to add barcodes to your messages</h1>

## You will learn

Learn how to use the `{% barcode %}` tag to generate [Code 128](https://en.wikipedia.org/wiki/Code_128) barcodes in your email, MMS, RCS, and WhatsApp messages. The barcode value can be a static string, a profile property, an event variable, or a Klaviyo coupon code.

### Quick reference

| Channel | Mode | Where to add the tag |
| --- | --- | --- |
| Email | `html` or `url` | Text block, HTML block, or image block URL field |
| MMS | `url` (default) | Dynamic Image section |
| RCS | `rcs` | Dynamic Image section |
| WhatsApp | `url` (default) | Dynamic Image section |

## Before you begin

The `{% barcode %}` tag works by generating a URL. When that URL is loaded (in a preview, an inbox, or a mobile device), it renders a PNG image of the barcode. This means the barcode image isn't created until the URL is actually fetched.

The `{% barcode %}` tag is supported in:

- Email
- MMS
- RCS
- WhatsApp

If you're currently using `{% barcode_code %}` from the [Getting started with coupon codes](https://help.klaviyo.com/hc/en-us/articles/115005084727) article, the `{% barcode %}` tag is the recommended replacement. It supports all channels (not just email) and works with any value, not only Klaviyo coupon codes. The `{% barcode_code %}` tag still works for existing implementations, but new barcodes should use `{% barcode %}`.

## Basic usage

The simplest way to use the barcode tag is:

```
{% barcode 'MyCode' %}
```

This produces a URL that returns a PNG image of a barcode. When scanned, the barcode contains the value `MyCode`.

The barcode value is required. The tag must always include a value — either a static string in quotes or a variable. A tag with no value (or a variable that resolves to empty) will produce an invalid URL.

You can customize the barcode by passing arguments to the tag. For example:

```
{% barcode 'MyCode' width=200 height=100 %}
```

See the arguments reference section below for all available options.

## Using barcodes with different channels

### Email

For email, you have two options for how the barcode renders:

****Option 1: HTML mode (recommended for email)****

Set `mode=html` to have the tag output an HTML `<img>` element directly. This is the simplest approach for including a barcode in an email.

```
{% barcode 'MyCode' mode=html %}
```

Place this tag in a text block or HTML block in the email template editor.

****Option 2: URL mode****

Leave the mode unset (or set `mode=url`) to get a URL, then place that URL in an image block's image URL field. This gives you more control over the image styling.

```
{% barcode 'MyCode' %}
```

If the barcode doesn't appear in a text block, check whether the block has show/hide logic applied that may be hiding it.

### MMS

For MMS messages, add the barcode tag in the ****Dynamic Image**** section of the SMS/MMS editor, not in the text body.

1. Open your MMS message in the editor.
2. Click the ****Add image**** icon in the message box.
3. Go to the ****Dynamic Image**** tab.
4. Paste your barcode tag, for example:

   ```
   {% barcode person.LoyaltyId %}
   ```
5. Click ****Save****.

This follows the same process as adding any dynamic image to an MMS. For more details, see [How to add a dynamic image to a text message](https://help.klaviyo.com/hc/en-us/articles/1260806102230).

### RCS

For RCS messages, use `mode=rcs` to format the barcode for RCS image requirements. This mode automatically sets dimensions that display correctly on both Android and iOS.

```
{% barcode 'MyCode' mode=rcs %}
```

Add the barcode tag in the Dynamic Image section of the RCS message editor, the same way you would for MMS.

****RCS defaults:****

- Width: 600px
- Height: 300px
- Padded to: 1440x720px

These defaults follow Klaviyo's RCS image formatting recommendations. You can override them with custom `width`, `height`, `padded_width`, and `padded_height` values if needed.

If your custom barcode dimensions exceed 1440x720px, the default padding will not be applied because the image won't fit in the standard canvas. In this case, provide your own `padded_width` and `padded_height` values.

### WhatsApp

For WhatsApp messages, add the barcode tag in the Dynamic Image section of the message editor, the same way you would for MMS.

```
{% barcode person.MembershipId %}
```

No special configuration or mode is needed for WhatsApp. The default `mode=url` works correctly.

## Barcode tag arguments reference

| Argument | Usage | Values | Default |
| --- | --- | --- | --- |
| `width` | Sets the width of the barcode | A number (rendered size must not exceed 4096px; see Scaling and sizing) | 100 |
| `height` | Sets the height of the barcode | A number (rendered size must not exceed 4096px; see Scaling and sizing) | 50 |
| `mode` | Sets the output format | `url`, `html`, or `rcs` | `url` |
| `coupon` | Specifies that the value is a Klaviyo-managed coupon code | `True` or `False` | `False` |
| `padded_width` | Width of the padded image area in pixels. Must be provided with `padded_height`. Not scaled. | A number less than 4096 | None (1440 for `mode=rcs`) |
| `padded_height` | Height of the padded image area in pixels. Must be provided with `padded_width`. Not scaled. | A number less than 4096 | None (720 for `mode=rcs`) |

## Using barcodes with profile properties and event data

You can use profile properties or event variables as the barcode value, so each recipient gets a unique barcode.

****Profile property examples:****

```
{% barcode person.LoyaltyId %}
{% barcode person.email %}
{% barcode person.MembershipNumber %}
```

****Event variable examples (for metric-triggered flows):****

```
{% barcode event.Code %}
{% barcode event.OrderId %}
```

****Handling missing values:****

If a recipient doesn't have the property set, the barcode URL will be invalid and the image won't load. You have two options:

Option 1: Use a `default` ****filter**** to set a meaningful fallback value:

```
{% barcode person.BarcodeCode|default:'STORE-MEMBER' %}
```

Make sure the default is a value that makes sense if scanned. A generic placeholder like "fallback" would produce a scannable but useless barcode.

****Option 2: Use a conditional statement**** to hide the barcode entirely when the value is missing:

```
{% if person.BarcodeCode %}
  {% barcode person.BarcodeCode mode=html %}
{% endif %}
```

Always handle the missing-value case when the barcode value comes from a profile property or event variable. Without a default or conditional, recipients missing that property will see a broken image.

****Combined example for email:****

```
{% barcode person.LoyaltyId width=200 height=75 mode=html %}
```

## Using barcodes with Klaviyo coupon codes

If you use Klaviyo-managed coupon codes and want to render them as barcodes, set `coupon=True`. This tells the system to assign a coupon code to the recipient and use that code as the barcode value.

```
{% barcode 'ShopifyCoupon' coupon=True %}
```

This works across all channels. For example, to send a coupon barcode via RCS:

```
{% barcode 'ShopifyCoupon' coupon=True mode=rcs %}
```

Only set `coupon=True` when using Klaviyo-managed coupon codes. If you manage your own coupon codes and store them as a profile property, reference the property directly without `coupon=True`:

```
{% barcode person.CouponCode %}
```

## Scaling and sizing

By default, the barcode's width and height are scaled by a factor of ****3x****. This means:

- A `width` of 100 renders at ****300px**** actual width
- A `height` of 50 renders at ****150px**** actual height

  ****Exception:**** When `mode=rcs`, the scaling factor is ****1x****. This allows more precise control over the barcode dimensions to fit RCS image formatting requirements.

  ****Padding values are not scaled.**** The `padded_width` and `padded_height` arguments always represent actual pixel values. Because the inner barcode is scaled by 3x, your padding values must be larger than 3 times the width and height. For example:

  ```
  {% barcode 'Code' width=200 height=100 padded_width=700 padded_height=400 %}
  ```

  Here, the barcode renders at 600x300px (200×3, 100×3) within a 700x400px padded canvas.

  ****Maximum image size:**** The barcode service will not generate images larger than ****4096x4096 pixels****. This limit applies to the **rendered** size after scaling. For non-RCS barcodes (3x scaling), that means the maximum `width` argument is approximately 1365 (1365 × 3 = 4095px). For RCS barcodes (1x scaling), the maximum is 4096.

  ****Width guidelines for long codes:****
- For non-RCS barcodes: if your code exceeds ****15 characters****, increase the width beyond the default of 100 (which renders at 300px).
- For RCS barcodes: if your code exceeds ****30 characters****, increase the width beyond the default of 600px.

If the width is too narrow to encode the data, the barcode image will fail to generate.

## Troubleshooting

### Always preview before sending

Because the `{% barcode %}` tag produces a URL at render time and the image isn't generated until that URL is fetched, failures may not be apparent until you preview or send the message. Follow these steps to catch issues early:

1. ****Preview the message.**** If the barcode doesn't load in the preview, it won't load when sent.
2. ****Scan the barcode.**** Use a barcode scanning tool (such as [imagetotext.info/barcode-scanner](https://www.imagetotext.info/barcode-scanner)) to verify the barcode encodes the expected value.
3. ****Send a test message to yourself**** before sending to your audience.

### Common issues

****The barcode image doesn't load****

The most common cause is an empty barcode value. This happens when the tag references a profile property or event variable that the recipient doesn't have. For example:

```
{% barcode person.BarcodeCode %}
```

If the recipient has no `BarcodeCode` value, the generated URL will be missing the code, and the image won't render. To fix this, add a `default` filter:

```
{% barcode person.BarcodeCode|default:'defaultCode' %}
```

****The barcode image fails to generate but the URL looks correct****

The barcode width is likely too narrow to encode all the data in your code. Try increasing the `width` value. As a rule of thumb:

- Codes over 15 characters need a width larger than the default 100 (300px rendered).
- RCS codes over 30 characters need a width larger than the default 600px.

****The barcode doesn't appear in a text block (email)****

Check whether the text block has show/hide logic applied. If a condition is hiding the block, the barcode won't render even if the tag is correct. Open the block's settings to verify.

## Additional resources

- [Getting started with coupon codes in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005084727) — Learn how to create and manage coupon codes, including how to use the older `{% barcode_code %}` tag for coupon barcodes in email.
- [How to add a dynamic image to a text message](https://help.klaviyo.com/hc/en-us/articles/1260806102230) — Learn how to add dynamic images to MMS messages, including where to find the Dynamic Image section in the editor.
- [Message personalization reference](https://help.klaviyo.com/hc/en-us/articles/4408802648731) — Reference for all personalization tags available in Klaviyo, including profile properties, event variables, and filters.
- [Understanding MMS image and GIF best practices](https://help.klaviyo.com/hc/en-us/articles/360041074911) — Best practices for image sizing and formatting in MMS messages.
