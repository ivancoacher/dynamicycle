---
id: "360045726811"
title: "Getting started with Klaviyo APIs"
source_url: "https://help.klaviyo.com/hc/en-us/articles/360045726811-Getting-started-with-Klaviyo-APIs"
section: "Custom integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:48Z"
language: "en"
---
## You will learn

Get a foundational understanding of API calls and how the Klaviyo APIs can benefit your business.  In this guide, you will learn about REST APIs, HTTP methods, and developer tools to prepare you for testing Klaviyo's APIs. Your first API calls can be accomplished in as little as 10 minutes from start to finish. If you are already familiar with API calls and are ready to test our APIs, follow [our guide on how to use our Postman collections](https://developers.klaviyo.com/en/docs/use_klaviyos_postman_collections).

Throughout this guide, we will link out to a glossary when new technical terms are introduced. If you are uncertain about the meaning of a word at any point in the guide, check out the [technical terms glossary](https://klaviyo.zendesk.com/hc/en-us/articles/360045302732).

### What is a REST API?

[REST](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70N1JW33C63TB1Q7FJ1) [API](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70NQNX9BHEAWCGE4PFS) is a set of acronyms that stand for Representational State Transfer and Application Programming Interface. These terms can be more simply understood as structured requests that allow a piece of software to talk to another and pass information between them. When you make an API call, you are submitting a request to a server where information is stored, which then returns a response containing your requested data in JSON, or JavaScript Object Notation, format.

More simply, REST APIs allow you to request data stored in Klaviyo and have that data returned to you in a format that is readable by you and by computers.

![whatisanAPI_copy.png](https://klaviyo.zendesk.com/hc/article_attachments/28722557581467)

A standard API call happens in seconds. Behind the scenes, your call will:

1. Send a structured request for data over the internet to the API. Requests are sent via [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview), a basic network request type that the internet is largely built around.
2. The API will receive the request, process it, and obtain the requested information from Klaviyo's databases.
3. The API then responds to the client application using JSON structured format.
4. You will receive the JSON response from your client application.

Although this knowledge is helpful to understand how data transfer works, it isn't necessary to start making API calls and getting value out of what Klaviyo APIs have to offer. Everything you need to know to get started with your first API calls will be covered in the following sections.

### HTTP methods

HTTP methods are the “verbs” by which your requests are sent. There are 2 [HTTP methods](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70NYQ9F64XV2CCK9E0Q) we will address in this guide: GET and POST.

Although we will not use them here, it is worth noting that most REST APIs support additional HTTP methods such as PUT, PATCH, and DELETE.

#### GET

A GET request can be most easily understood as a “read” request. GET requests retrieve information from the API [endpoint](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70N6DTN4KXNP9RZ7VER) and return it to you in a JSON-formatted response. These requests only allow you to read data, making them the safest type of request because your data cannot be modified or overwritten with this method.

#### POST

A POST request can be simply understood as a “write” request. POST allows you to create or add new resources. For example, a POST request to the List API can be used to create a new list in your account, while a GET request can be used to retrieve all available lists. Note that, when posting data, responses will vary depending on when Klaviyo can complete your request.

### Necessary tools

APIs offer plenty of flexibility to your workflows and don't require you to use a specific client application or [language library](https://help.klaviyo.com/hc/en-us/articles/360045302732#l8) to achieve the desired results. Because API calls are made using HTTP requests, nearly every programming language has the ability to send this type of request natively or through a widely available language library. Additionally, depending on your machine and operating system, you can use native applications like Apple’s [Terminal](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/CommandLInePrimer/CommandLine.html) or Windows [Command Line](https://docs.microsoft.com/en-us/windows/terminal/) to make client-side API calls. However, these applications require prior knowledge of command line interfaces.

We use a free web and desktop application called [Postman](https://www.postman.com/). Postman has a variety of features that make it easier to set up and send an API request by inputting the endpoint, [parameters](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70NKFSQDB43945J0J18), and [authentication](https://help.klaviyo.com/hc/en-us/articles/360045302732#h_01HCJKN70NQNX9BHEAWCGE4PFS) into a helpful user interface.

## Test Klaviyo's APIs

Klaviyo's APIs are useful for sending data from other platforms or servers to Klaviyo accounts or querying information within a Klaviyo account. Now that you have an understanding of how APIs work, you can get started testing our APIs for your business's use cases. For a full list of Klaviyo's available APIs, check out our [API reference documentation](https://developers.klaviyo.com/en/reference/api_overview). Follow our [guide on how to use our Postman collections](https://developers.klaviyo.com/en/docs/use_klaviyos_postman_collections) to make your first Klaviyo API call.

## Additional resources

### Developer portal resources

Klaviyo's [developer portal](https://developers.klaviyo.com/en) contains API guides and reference documentation to help you make the most out of our APIs. Check out the resources below to get started:

- [Klaviyo API reference documentation](https://developers.klaviyo.com/en/reference/api_overview)
- [Getting started with the Javascript API](https://developers.klaviyo.com/en/docs/javascript_api)
- [Setting up API-based transactional events](https://developers.klaviyo.com/en/docs/guide_to_setting_up_api_based_transactional_events)

### Klaviyo developer courses

[Klaviyo Academy](https://academy.klaviyo.com/) provides developer courses to help you get started building with Klaviyo APIs. Check out the courses below:

- [API fundamentals for marketers](https://academy.klaviyo.com/en-us/collections/api-fundamentals-for-marketers)
- [Klaviyo developer certificate](https://academy.klaviyo.com/klaviyo-developer-certificate)
- [Define common API terms](https://academy.klaviyo.com/define-common-api-terms/1955790)