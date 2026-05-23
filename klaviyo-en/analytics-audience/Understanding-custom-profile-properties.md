---
id: 115000250912
title: "Understanding custom profile properties"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/115000250912-Understanding-custom-profile-properties"
section: "Understand profiles"
category: "Audience"
category_slug: "analytics-audience"
klaviyo_updated: "2026-04-21T13:54:11Z"
language: en
---

## You will learn

Learn about custom properties in Klaviyo that you can use to store information about the contacts in your account.
Here are several examples of how you might use custom properties:

- To collect additional information about your contacts, such as gender, size, coupon code, etc.
- To collect contacts' preferences, such as email frequency, type of content, etc.
- To collect contacts' responses to a questionnaire

You can collect virtually any type of information you'd like about a contact using custom properties, and then later use this information to tailor content, create segments, or filter flows. There is no limit to the number of custom properties that can be added to one profile.

## How to add a custom property to a profile

There are two main ways you can add a custom property to a contact's profile:

1. Add this information yourself (e.g. by manually adding it, or [uploading a CSV](https://klaviyo.zendesk.com/hc/en-us/articles/1260806293150))
2. Ask contacts to provide this information

### Add a custom property yourself

When uploading a list, any column after the "Email" column can be used to attach a custom property to a profile. For example, you could have a "Gender" column that corresponds with a contact's gender.

![Hair color custom property being added during upload](https://klaviyo.zendesk.com/hc/article_attachments/28720891154075)

If the property doesn’t yet exist on any Klaviyo profiles, you’ll need to create a new property during the upload. To do this, type the property name you’d like to use into the **Klaviyo Field** column of the new property’s row, then select ****Create option****.

Do not click ****Subscribe to Email Marketing**** in the **Import review** step, so that all profiles in the upload will retain their existing subscription status in Klaviyo.

![Create profile property option on a profile in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28720846056603)

You can also add custom properties directly to a contact's profile. First, navigate to the profile you would like to add a custom property to. Here, you will see an area labeled **Custom Properties**, with an option to **Add custom property**. Click this and add the custom property you would like.

![Add custom profile property button](https://klaviyo.zendesk.com/hc/article_attachments/28720846060059)

### Collect custom profile property data

You can collect custom properties straight from your subscribers when they sign up using a subscribe page, sign-up form, or [third-party list growth integration](https://connect.klaviyo.com/integrations). You can also collect custom properties from existing subscribers using a manage preferences page.

- [Collect custom properties with a sign-up form](https://help.klaviyo.com/hc/en-us/articles/4413550187035)
- [Collect custom properties with a subscribe or manage preferences page](https://help.klaviyo.com/hc/en-us/articles/115005251848-Edit-Opt-in-Related-Pages-for-a-List)

Any additional fields you add to a subscribe page or sign-up form will be collected as custom properties. You can even use these methods as a questionnaire if you would like to filter segments or flows by the responses you receive.

## Profile properties in sign-up forms

If you use a sign-up form to collect profile property information, and the custom property does not yet exist in any Klaviyo profiles, you may have to create the option for the profile property name and value.

First, enter a label title and value title for your property. Once values have been added, they will appear as options from then on. Each property label should be unique. For broader instruction, see [properties in sign-up forms](https://help.klaviyo.com/hc/en-us/articles/115005074627#h_01HA32RZBB2RB125E2K2RH7A55). All custom fields can be edited before or after publishing your form.

![](https://klaviyo.zendesk.com/hc/article_attachments/39652942794651)

Different form fields create properties with [different data types](https://help.klaviyo.com/hc/en-us/articles/115005237648). For example, the boolean data type can only represent two values: true or false. An example of boolean data is the property stored when someone has accepted marketing from you.

To view all submissions to your form together, [export the profiles as a CSV](https://help.klaviyo.com/hc/en-us/articles/115005078687-How-to-Export-a-List-or-Segment-to-a-CSV-File), along with the properties from your form. Note that only form submissions that are connected to a profile can be stored and exported.

Collecting the same profile property multiple times in a single form will set the property value associated with the last collection step. Additionally, if someone fills out the same form multiple times, only the most recent submission will be saved. If you need to track and store each form submission separately, we recommend using a survey tool like [Typeform](https://help.klaviyo.com/hc/en-us/articles/115000107112).

## How to use custom properties

You can use custom properties to segment your audience, filter flows, and include dynamic content within emails. Once you've created a custom property and it is present on at least 1 profile, it will populate in the segment builder when you select **Properties about someone**. Likewise, this will happen when you [add filters to a flow](https://help.klaviyo.com/hc/en-us/articles/115002779051-Flow-Triggers-and-Filters).

![Segmenting based on custom property called Hair Color](https://klaviyo.zendesk.com/hc/article_attachments/28720891157659)

You can also dynamically populate your emails with a custom property by using the "lookup" filter:

|  |  |
| --- | --- |
| Your hair color is:  {{ person|lookup:'Hair Color' }} | Your hair color is:  Blonde |

## Additional resources

- [Profiles and properties glossary](https://help.klaviyo.com/hc/en-us/articles/360053679071-Profiles-and-Properties-Glossary)
- [Profile properties reference](https://help.klaviyo.com/hc/en-us/articles/115005074627-Guide-to-Properties)