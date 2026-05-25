---
id: "18620644491035"
title: "Getting started with Code"
source_url: "https://help.klaviyo.com/hc/en-us/articles/18620644491035-Getting-started-with-Code"
section: "Code"
category: "Advanced KDP & Marketing Analytics"
category_slug: "advanced-kdp-marketing-analytics"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: "en"
---
## You will learn

Learn about Code, and how to create custom functions that are executed directly by Klaviyo.

Code requires custom development and Klaviyo’s support team is unable to offer hands-on assistance. If you don't have a developer on your team and are not comfortable writing code yourself, consider reaching out to a Klaviyo Partner for assistance.

## Before you begin

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn how to purchase this plan.

## What is Code?

Code enables you to execute custom functions in response to events captured in Klaviyo. You can write your own Javascript or Python functions in the Code editor, and they are then executed directly in the platform.

With Code, you can send data to your external systems without having to set up a public HTTP endpoint to receive webhooks, and build custom functionality that is triggered in response to an event’s occurrence. You can also access many popular prebuilt modules to facilitate creating custom solutions.

Learn [how to build custom functions using Code](https://academy.klaviyo.com/build-custom-functions-with-code).

## Topics

Code allows you to execute custom functions in response to any event that can be queried for via the [Get Events API](https://developers.klaviyo.com/en/reference/get_events).

These include:

- Email events (e.g., **Clicked email**, **Marked email as spam** )
- SMS events (e.g., **Sent SMS**, **Received SMS**)
- Push notification events (e.g., **Received push**, **Bounced push**)
- Events from integrations ( i.e., events from first-party integrations created by Klaviyo)
- API events (i.e., events synced through Klaviyo’s APIs)

Klaviyo Code does not support the following events as topics:

1. Email opened
2. Email received

## Code interface

To access Code, navigate to the **Code** tab under ****Advanced KDP********> Data Management > Code******.**

To create a custom function, select the **Create a function** button:

![Create a function button](https://klaviyo.zendesk.com/hc/article_attachments/28722598719003)

You will be brought to the **Recipes** page, where you can either select a prebuilt solution to execute, or a blank Python or Node.js function.

![image (9).jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722610653467)

If you select an existing recipe, you'll see the code editor with the code for the solution, along with a description of the functionality.

![image (10).jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598744219)

If you select a blank function so you can create your own custom solutions, the **Details** modal will appear where you can:

- ****Name your function****
  A name to identify your function.
- ****Select a topic for your function****
  The event that will trigger your code’s execution .
- ****Select a runtime****
  The runtime environment in which the code is executed (i.e., Python or Node.js).
  ![3.11.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722610665883)

  After making the required selections and selecting the **Create function** button, you will be brought to an interface with the following tabs:
- Editor
- Test output
- Logs

## Granting permissions

The first time you create a function through Code, you will be prompted to authenticate the Code OAuth application. This is required so that your Code functions are able to access data in your Klaviyo account.

Once you’ve granted access, you will be brought to the Code editor.

## Editor

On the **Editor** page in Code, you’ll the page split into 3 tabs:

- ****Code****
  The code tab has an editor where you can write Python or Javascript functions.
- ****Modules****
  Modules are 3rd party packages that add functionality to your functions.
- ****Environment Variables****
  Environment variables are the key-value pairs that your function accesses when it runs.

### Code

On the **Code** tab, you’ll see an editor you can use to write Python or Javascript functions that are executed in response to the selected topic.

![3.11(2).jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722610658843)

![js.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598751003)

### Handler function parameters

In order for Klaviyo to execute the code you write, it must be wrapped in a function named “handler” that accepts 2 parameters:

- ****Event****
  Consists of the event data associated with the triggering event in JSON:API format. If the trigger is non-event based (e.g., **Added to List**), then the value of this parameter will be **None** or **Null** depending on the language.
- ****Context****
  Contains additional metadata about the function execution, including the profile associated with the function invocation. You can access the profile object via **context.profile** in Javascript or **context["profile"]** in Python.

Below are examples of the event and context parameters that are passed to the handler function.

****Example event format****

```
{
    {
  "data": {
    "type": "event",
    "id": "7S2q9haejYG",
    "attributes": {
      "timestamp": 1694435729,
      "event_properties": {
        "MfaEnabled": false,
        "IpAddress": "000.00.0.0",
        "UserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "UserRole": "Owner",
        "SessionId": "34sh0a9nh8ngnk2nfacjxmt592yx40ib",
        "LoginType": "Username_password",
        "current_company_id": "XXXXX",
        "$event_id": "1694435729"
      },
      "datetime": "2023-09-11 12:35:29+00:00",
      "uuid": "b0b8fe80-509f-11ee-8001-278cc529fcd3"
    },
    "relationships": {
      "profile": {
        "data": {
          "type": "profile",
          "id": "123456"
        },
        "links": {
          "self": "https://a.klaviyo.com/api/events/7S2q9haejYG/relationships/profile/",
          "related": "https://a.klaviyo.com/api/events/7S2q9haejYG/profile/"
        }
      },
      "metric": {
        "data": {
          "type": "metric",
          "id": "4Tdup6"
        },
        "links": {
          "self": "https://a.klaviyo.com/api/events/7S2q9haejYG/relationships/metric/",
          "related": "https://a.klaviyo.com/api/events/7S2q9haejYG/metric/"
        }
      }
    },
    "links": {
      "self": "https://a.klaviyo.com/api/events/7S2q9haejYG/"
    }
  }
}
```

****Example context format****

```
{
    "company_id": "XXXXX",
    "trigger": {"type": "event", "uid": "123456"},
    "function_id": "123456",
}
```

### Modules

On the **Modules** tab, you can select from the most popular prebuilt modules (i.e., 3rd-party packages that add capabilities to your functions).

To add an external module to use in your code, select the ****Add module**** button:

![Add module button](https://klaviyo.zendesk.com/hc/article_attachments/28722610608411)

On the modal that appears, you can search and select the module you’d like to add:

![Add module modal](https://klaviyo.zendesk.com/hc/article_attachments/28722598684571)

Once added, you can use the module with the code you write in Klaviyo.

You should refer to the external module’s native documentation for information regarding how to use it.

![Added modules](https://klaviyo.zendesk.com/hc/article_attachments/28722598687771)

****The klaviyo module****

All Code functions come with a custom **klaviyo** package that is pre-installed into your Code environment. This module allows your functions to access the data in your Klaviyo account without needing to supply any credentials, such as an API key.

The API of the **klaviyo** module depends on whether your code is written in Python or Javascript.

### Python **klaviyo** module

The API of the pre-installed **klaviyo** module is the same as the [Klaviyo SDK](https://github.com/klaviyo/klaviyo-api-python) object you would normally instantiate with the **klaviyo-api** Python module. You can think of the **klaviyo** module as a pre-instantiated **klaviyo** SDK client.

For example, in a traditional workflow you would first instantiate a new Klaviyo SDK client by passing an API key to the constructor, and then use the resulting SDK object.

```
from klaviyo_api import KlaviyoAPIimport osdef handler(event, context):  klaviyo = KlaviyoAPI(api_key=os.getenv("KLAVIYO_API_KEY"))  print(klaviyo.Metrics.get_metrics())
```

With Code, you just need to import the klaviyo object and authentication is handled for you.

```
import klaviyodef handler(event, context):  print(klaviyo.Metrics.get_metrics())
```

View the [available Klaviyo objects and their methods](https://pypi.org/project/klaviyo-api).

### Javascript **klaviyo** module

When using the pre-installed **klaviyo** module in your Javascript functions, import the specific Klaviyo features you want to access using curly brace syntax from the **klaviyo** module. Then use them as you normally would an API object using the [**klaviyo-api**](https://www.npmjs.com/package/klaviyo-api) [Javascript module](https://www.npmjs.com/package/klaviyo-api).

```
import { Metrics } from 'klaviyo';export default async (event, context) => {  console.log(await Metrics.getMetrics())}
```

View the [available Klaviyo objects and their methods](https://www.npmjs.com/package/klaviyo-api).

### Environment variables

The **Environment variables** tab allows you to set key-value pairs that your code in Klaviyo can reference when it runs. These can be used to store information like credentials and secret keys so your functions can access them as they run.

To add an environment variable, select the ****Add a variable**** button:

![Add environment variables button](https://klaviyo.zendesk.com/hc/article_attachments/28722610624539)

On the modal that appears, you can set a key-value pair for your environment variable.

![Key-value pairs set for environment variable ](https://klaviyo.zendesk.com/hc/article_attachments/28722610627099)

Once created, the environment variables will be listed on the page and can be used in your code.

To access your environment variables in your code, use os.getenv("Key") for Python, or process.env.KEY for Node.js.

![Created environment variables](https://klaviyo.zendesk.com/hc/article_attachments/28722598707611)

To update the value for an existing environment variable, you must create a new variable with the same key you would like to update the value for.

## Test output

The **Test output** tab in Code allows you to test your code with recent events to confirm that the output is behaving as expected.

To test your function:

1. Select the ****Run test**** button:
   ![Run test button](https://klaviyo.zendesk.com/hc/article_attachments/28722598714907)
2. On the modal that appears, select an event to test with. You can select from the 10 most recent events captured in Klaviyo.
   ![Recent events to test with](https://klaviyo.zendesk.com/hc/article_attachments/28722610636315)
3. After selecting an event to test with, the test output will be shown:

![Test output](https://klaviyo.zendesk.com/hc/article_attachments/28722610618651)

## Logs

The **Logs** tab shows the health of your ongoing Code functions. You’ll see:

- ****Status****
  The progress of a function’s execution.
- ****Response time****
  The amount of time it takes for your code to execute in response to an event.
- ****Date****
  A timestamp for when the function was executed.

## Rate limits

Klaviyo code has the following rate limits:

- ****Function timeout****
  Functions in Code can execute for up to 15 seconds before they timeout.
- ****Function rate limit****
  Functions in Code allow for up to 25 concurrent executions per function.

## Deploying code

To deploy the code that you write in the editor, toggle the status dropdown to **Live**.

![Toggle to deploy code](https://klaviyo.zendesk.com/hc/article_attachments/28722610634139)

Once set to live, the code you write will execute each time the topic event is captured in Klaviyo.

When a function is set live, there may be up to a 15 minute delay before events begin to trigger the function.

## Example solution

Below is an example of a custom solution being implemented with Code.

In the example, event data is set as a profile property so it can be used in targeted emails and in segmentation. The **Booked shoot** custom event is captured in Klaviyo when customers book a shoot with the brand, and data about the booking city and associated URL is set as a profile property on the respective profile.

A property called **Recent bookings** is also created, which stores data from the 5 most recent **Booked shoot** events so it can be looped through and accessed in an email templates.

### Code

The Python code for this solution is written in the Code editor and is executed directly by Klaviyo.

![Code_updates.jpg](https://klaviyo.zendesk.com/hc/article_attachments/32517910641819)

### Example code

[“Booked](https://www.napkin.io/api/embed/236e23398bf14a27)

### Modules

In this example, the built-in **klaviyo** module is used. The **klaviyo** module relies on the **klaviyo-api** module being added to the function. Once added, the **klaviyo** module will handle authentication for you, so no API key is needed.

### Environment variables

Environment variables can be used to store information like credentials and secret keys so your functions can access them as they run. For this example, the following key-value pair is set:

- ****MAX\_PROPERTIES\_TO\_STORE****
  An environment variable used to define the maximum number of properties to store for the example function.

### Testing

While creating the function to set event data as profile properties, the **Test output** tab is used to verify the expected output.

![test_output.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722610647323)

### Logs

Once the function has been created and tested, the **Logs** tab shows the health status of the function as it is executed in response to **Booked shoot** events.

![Logs.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722598726043)

### Outcome

With this Code function in place, as customers sign up for shoots and trigger the custom **Booked shoot** event, the event data will be stored on the customer profile for use in segmentation and targeted campaigns.

## Implementing Recipes

Recipes in Code allow you to implement prebuilt solutions without the need for custom development.

To implement a Recipe in your Klaviyo account:

1. Select the **Create function** button on the Code page.
2. Choose the Recipe you’d like to implement in your account. You’ll be brought to the editor where you can see the code for the selected Recipe, along with a description of what the function does.
3. Click the **Select** button to continue.
   ![Currency converter recipe in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28722598756891)
4. Choose a name for the function and the trigger that will cause it to execute. The runtime is automatically set based on the code for the Recipe.
5. Select the **Create function** button.
6. Once the function has been created, set the relevant environment variables so the function has the data it needs to run.
7. The Recipe can now be tested and set to **Live**.

Recipes may require you to update certain fields to match your desired naming preferences and the data in your events. See the instructions for the Recipe to view which fields can be renamed and edited.