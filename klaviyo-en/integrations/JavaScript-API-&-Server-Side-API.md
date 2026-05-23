---
id: 360007119971
title: "JavaScript API & Server-Side API"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/360007119971-JavaScript-API-Server-Side-API"
section: "Custom integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:56:50Z"
language: en
---

## JavaScript API

The following guide will walk you through setting up and using the JavaScript API. If you are planning on a full ecommerce integration, please see [this guide](https://help.klaviyo.com/hc/en-us/articles/115005082927).

#### Note

To use the Klaviyo snippets provided below, you will need to update the placeholder for API\_KEY with [your public API key, which can be found here](https://www.klaviyo.com/account#api-keys-tab).

### Adding the Klaviyo snippet

To start tracking people, add the below snippet to the right in your website's main template so it will automatically be added to every page on your website. If you have a developer that will add this script to your website, you can send them a link to this guide.

```

```

****You need to make one change to the snippet****. If you're an eCommerce business, remove the four lines with the "identify" call. If you're a website or web app people log into, replace the `{{ email }}` placeholder email with the appropriate template variable that has the logged in user's email address.

We suggest putting the Klaviyo code at or near the bottom of your site template. If you use Google Analytics or other third party services, you can place the Klaviyo code directly above or below that.

You might be wondering, "How does using Klaviyo affect my site's performance?" The answer is Klaviyo doesn't affect your website's performance at all. Our code only loads once the rest of your website has finished loading. In addition, Klaviyo tells browsers to cache our JavaScript so your visitors often don't even need to download our JavaScript every time switch pages.

### Check Your Script

Once you've added the JavaScript to your website, you can check that it's set up properly by entering the URL of your website to the right.

Once the script is on your website, Klaviyo will start tracking visits and session on your website in real-time.

### API Basics

To make calls to the Klaviyo API and store information about people, you'll use the `_learnq` object that's automatically added by the Klaviyo script.

To make an API call, Klaviyo uses a special syntax that allows your API calls to work even when our script hasn't loaded on the page yet. You'll create an array where the first value is the name of the method you want to call and any subsequent values are arguments to pass to that method.

### Identifying People

The **identify** method allows you to identify and set properties on an individual. This method accepts a dictionary or hash of properties. When you identify someone, you must include either their email address, with the $email key, or a unique identifier such as their user ID, with the $id key.

Once you've included at least one of those identifiers, you're free to add any custom properties you want. Custom properties are useful for tracking facts about individuals. In Klaviyo, you can then create segments of people based on those properties. For instance, you might want to track an individual's plan type or sign up date. Klaviyo will also understand different data types you use, so feel free to use numbers, booleans and dates.

Klaviyo has a few special properties that are used to display information about people. These are: $first\_name, $last\_name, $phone\_number, $title and $organization.

In addition to properties you track, Klaviyo will automatically determine what website each person was first referred from for attribution tracking and a person's location based on where they access your website.

****Example Code:****

```

```

### Tracking Events and Actions

The **track** method allows you to record events and actions people take on your website. This method accepts a string which is the name you give to that event. This method also accepts an optional dictionary or hash of properties associated with that event.

For example, you could track when someone purchases an item and include information on the purchase price and what items they bought. If you have an application where people have profiles you could track when someone fills out their profile. If you are planning on a full ecommerce integration, please see this guide.

Klaviyo's event tracking and analytics are very flexible, so you can customize them to keep track of what's important to your business. Our track method also understands different data types, so you can use numbers, booleans and dates and we'll create intelligent charts and graphs based on the data you send.

****Example Code:****

```

```

## Server-Side API