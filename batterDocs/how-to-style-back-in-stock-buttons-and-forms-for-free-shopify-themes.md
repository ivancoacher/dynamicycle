<h1>How to style Back in Stock buttons and forms for free Shopify themes</h1>

## You will learn

Learn what key changes to make for each free Shopify theme to quickly ensure your Back in Stock button and form match your theme's styling. The Klaviyo "Notify Me When Available" button and form are highly configurable. You are able to change the colors, fonts, text, and other elements according to your design preferences.

Installation of back in stock is only supported for certain free Shopify themes, and not for Shopify stores using custom themes. At this time, Klaviyo support cannot assist with implementing back in stock for stores using custom themes. To check which Shopify theme your store is using, you can use a [Shopify theme detector](https://pagefly.io/blogs/shopify/shopify-theme-detector).

## Before you begin

If you have not already, read our guide on [getting started with Shopify](https://help.klaviyo.com/hc/en-us/articles/115005080407-How-to-Integrate-with-Shopify) for step-by-step instructions on integrating, before continuing with this article.

To learn about more generally about the Back in Stock feature and how to enable it, read our guide on [install back in stock for Shopify.](https://klaviyo.zendesk.com/hc/en-us/articles/360001895651)

## How to style your button and form

1. When you're [installing your snippet](https://help.klaviyo.com/hc/en-us/articles/360001895651-How-to-Install-Back-in-Stock-for-Shopify#install-the-snippet5), find the styling snippet for your free theme in this article.
2. The default snippet is shown below. Update (or add) line items within the `trigger: {}` and `modal: {}` sections of the default snippet according to what's shown in the styling snippet
   1. For example, if you have the Crave theme, you only need to add the the following line within the modal section:  `font_family: '"Archivo", serif;'`
3. Make any other desired styling updates to the line items as you see fit.

```
<script src="https://a.klaviyo.com/media/js/onsite/onsite.js"></script>
<script>
    var klaviyo = klaviyo || [];
    klaviyo.init({
      account: "PUBLIC_API_KEY",
      platform: "shopify"
    });
    klaviyo.enable("backinstock",{
    trigger: {
      product_page_text: "Notify Me When Available",
      product_page_class: "button",
      product_page_text_align: "center",
      product_page_margin: "0px",
      replace_anchor: false
    },
    modal: {
     headline: "{product_name}",
     body_content: "Register to receive a notification when this item comes back in stock.",
     email_field_label: "Email",
     button_label: "Notify me when available",
     subscription_success_label: "You're in! We'll let you know when it's back.",
     footer_content: '',
     additional_styles: "@import url('https://fonts.googleapis.com/css2?family=Roboto+wght@400;700&display=swap');",
     drop_background_color: "#000",
     background_color: "#fff",
     text_color: "#222",
     button_text_color: "#fff",
     button_background_color: "#439fdb",
     close_button_color: "#ccc",
     error_background_color: "#fcd6d7",
     error_text_color: "#C72E2F",
     success_background_color: "#d3efcd",
     success_text_color: "#1B9500"
    }
  });
</script>
```

## Crave

```
trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Archivo", serif;'
}
```

## Dawn

```
trigger: {
 product_page_class: 'button'
},
modal: {
font_family: '"Assistant", sans-serif;'
}
```

## Studio

```
trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Electra", serif;'
}
```

## Colorblock

```
trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Futura", sans-serif;' }
```

## Sense

```
trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Harmonia Sans", sans-serif;'
}
```

## Taste

```
trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Anonymous Pro", sans-serif;'
}
```

## Craft

```
trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Quattrocento Sans", sans-serif;'
}
```

## Ride

```
trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Avenir Next", sans-serif;'
}
```

## Refresh

```
trigger: {
 product_page_class: 'button'
},
modal: {
 font_family: '"Questrial", sans-serif;'
}
```

## Simple

### Beauty

```
modal: {
 font_family: '"PT Serif",serif;'
}
```

## Pop

### Bone

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Raleway');",
 font_family: '"Raleway","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Toy

```
trigger: {
 product_page_class: 'btn btn--large btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Open+Sans');",
 font_family: '"Open Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Black & White

```
trigger: {
 product_page_class: 'btn btn--large btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Open+Sans');",
 font_family: '"Open Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Vibrant

```
trigger: {
 product_page_class: 'btn btn--large btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Open+Sans');",
 font_family: '"Open Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

## Venture

### Snowboards

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Karla');",
 font_family: '"Karla","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Outdoors

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Roboto');",
 font_family: '"Roboto","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Boxing

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Source+Sans+Pro');",
 font_family: '"Source Sans Pro","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

## Debut

### Default

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Work+Sans');",
 font_family: '"Work Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Light

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Muli');",
 font_family: '"Muli","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

## Supply

### Light

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Roboto');",
 font_family: '"Roboto","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Blue

```
trigger: {
 product_page_class: 'btn btn--large btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Montserrat');",
 font_family: '"Montserrat","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

## Narrative

### Warm

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Avenir');",
 font_family: '"Avenir","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Light

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Open+Sans');",
 font_family: '"Open Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Cold

```
trigger: {
 product_page_class: 'btn btn--full'
},
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Lato');",
 font_family: '"Lato","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

## Brooklyn

### Classic

```
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=Arapey');",
 font_family: '"Arapey",serif;'
}
```

## Minimal

### Modern

```
modal: {
 font_family: '"PT Serif",serif;'
}
```

### Vintage

```
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=PT+Sans');",
 font_family: '"PT Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

### Fashion

```
modal: {
 additional_styles: "@import url('https://fonts.googleapis.com/css?family=PT+Sans');",
 font_family: '"PT Sans","HelveticaNeue","Helvetica Neue",sans-serif;'
}
```

## Outcome

You've now updated the styling of your Back in Stock button and form on your Shopify store.
