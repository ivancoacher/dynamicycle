---
id: 17252552814875
title: "How to use age-gating with Klaviyo"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/17252552814875-How-to-use-age-gating-with-Klaviyo"
section: "SMS age-gating and prohibited content"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: en
---

## You will learn

Learn about age-gating in Klaviyo, which may allow brands to send otherwise prohibited content via SMS in [most countries where SMS is available](https://help.klaviyo.com/hc/en-us/articles/4402914866843).

This information is intended solely for educational and informational purposes and should ****not**** be construed as legal advice. The content provided is general in nature and may not reflect the most up-to-date information. Klaviyo strongly advises consulting with a qualified legal counsel to ensure your compliance with applicable laws and regulations in connection with your use of our services.

## What is allowed with Klaviyo age-gating

Brands falling under the following industries may be able to send SMS if they use age-gating (prohibited content rules apply to all industries):

- Alcohol
- Firearms
- Tobacco
- Sex

However, what's allowed depends on the country you're sending to, the sending number you're using, and the legal age of consent. Please open the dropdowns below to learn more.

****Alcohol****

Age-gating for alcohol is allowed in [most countries where SMS is available](https://help.klaviyo.com/hc/en-us/articles/4402914866843), except Canada, New Zealand, Denmark, Norway, Finland, Sweden, and Poland.

The age of consent in each country is:

- 21 in the United States.
- 18 in the United Kingdom, Germany, Ireland, Australia, France, Belgium, Austria, Spain, Italy, Portugal, Denmark, and Hungary.
- 16 in Switzerland.

Age-gating for alcohol is available for all sending numbers.

****Firearms****

Firearm related content may be allowed with SMS age-gating in the United States and United Kingdom.

|  |  |  |
| --- | --- | --- |
| ****Country**** | ****Age of consent**** | ****Sending number**** |
| United States | 21 | Short Code |

****Tobacco****

Tobacco related content may be allowed with SMS age-gating in the United States.

|  |  |  |
| --- | --- | --- |
| ****Country**** | ****Age of consent**** | ****Sending number**** |
| United States | 21 | Short Code |

****Sex****

Certain content in the category of sex may be allowed with SMS age-gating in the following countries:

|  |  |  |
| --- | --- | --- |
| ****Country**** | ****Age of consent**** | ****Sending number**** |
| United States | 18 | Short Code |
| United Kingdom | 18 | Branded Sender Id, Long Code, Short Code (Vanity) |
| Canada | 18 | Short Code (Vanity) |
| Australia | 18 | Branded Sender ID, Long Code |
| Netherlands | 18 | Branded Sender ID, Long Code |

## The opt-in process with age-gating

For proper age-gating with SMS, 2 things need to happen before someone can opt in:

1. Someone enters their age.
2. SMS consent is added if that age meets that country’s minimum age requirement.

Anyone who is under the legal age for a specific country or doesn’t enter their age cannot become an SMS subscriber. However, they can subscribe to email.

****Will an underage profile automatically become an SMS subscriber when they turn the legal age?****

No. A person can only consent after they are legally of-age. Signing up when they’re younger than that age (even if it’s only a day before) doesn’t count.

For instance, if someone in the UK is 17 and tries to subscribe to an alcohol brand, they won’t become an SMS subscriber at that time or automatically when they turn 18. The only way for that individual to subscribe to SMS is to opt in once they are already 18 or older.

****If someone fails the age gate, can they try again?****

If someone fails an age gate, they’ll receive an error message. However, they can resubmit it (e.g., to fix a typo).

## Who is eligible for age-gating with Klaviyo

Age-gating is not available for all industries and countries with Klaviyo:

- It is only allowed for alcohol and firearms brands, not any other type of [prohibited content](https://help.klaviyo.com/hc/en-us/articles/4401822831771).
- Age-gating is only available in specific countries and, in some cases, sending numbers.

  Check the list below to see which industries are prohibited and which require age-gating in the US.

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | ****Industry**** | | ****Allowed with age-gating?**** | ****Allowed in Klaviyo?**** | ****Number types**** |
  | Alcohol | | Yes  Age: 18 or 21+ (depending on country) | [Yes](https://help.klaviyo.com/hc/en-us/articles/17252552814875), in certain countries | Short code and toll-free numbers |
  | Firearms | | Yes  U.S. age: 21+  U.K. age: 18+ | Yes (U.S., U.K.) | U.S.: short code  U.K.: long code |
  | Sweepstakes (regional laws for sweepstakes may apply) | | Yes  Age: 18+ | No | Short code and toll-free numbers |
  | Adult | Sex toys and lingerie | Yes  Age: 18+ | Yes, in certain countries | Short Code, Branded Sender ID, Long Codes (Country Dependent) |
  | Sexually explicit content | No | No | N/A |
  | Tobacco | Tobacco, including vapes containing nicotine, and tobacco-related paraphernalia | Yes  U.S. age: 21+ | No | N/A |
  | Illegal Substances | CBD/Cannabis, including CBD/Cannabis vapes and CBD/Cannabis-related paraphernalia | No | No | N/A |
  | Gambling | Gaming apps, websites, betting apps, casinos | No | No | N/A |
  | Fireworks | | No | No | N/A |
  | Hate speech | | No | No | N/A |
  | Violence | | No | No | N/A |
  | Profanity | | No | No | N/A |
  | Illegal drugs | | No | No | N/A |

  Requirements for launching SHAFT programs:
- You must implement a robust [age gate](https://help.klaviyo.com/hc/en-us/articles/4408311712667#h_01HA4R92DZQCAHT4VMMDY19SGM) for any SHAFT-related content at SMS opt in. Asking if the subscriber is of legal age to view SHAFT-related content is not sufficient to meet carrier requirements for a robust age gate. Any age gate must collect the subscriber’s date of birth.
- Review all onsite content to verify it doesn’t contain illegal material or promote unlawful activity.
- Notice: Carriers have full discretion to approve or reject programs, including those that don’t meet their codes of conduct or content policies.

****What happens if I try to collect or import SMS consent in a country where age-gating isn’t available?****

In this case, the profile syncs to Klaviyo without SMS consent and shows the **Failed SMS Age Gate** metric.

For instance, if you import a CSV that contains both US and Canadian numbers, only the US numbers are imported as consented SMS subscribers. Canadian numbers are added as profiles in your account, but you can’t send SMS messages to these individuals, since age-gating is currently not available for any prohibited content in Canada.

The same is true for collecting consent, such as with sign-up forms. We recommend targeting your SMS opt-in methods to countries where age-gating is available.

## Use SMS age-gating in Klaviyo

You don't need to manually enable age-gating in Klaviyo; instead, when you set up SMS, Klaviyo will detect if your brand is tied to alcohol, firearms, and tobacco.

For you, this process appears as:

1. You start by going through the setup wizard.
2. When you select a country where SMS age-gating is available and Klaviyo detects that your brand requires age-gating, you are automatically submitted for approval.

   - If you select countries where age-gating isn't available, you will not be able to use SMS in those regions. Additionally, if those are the only countries you chose, you will not be able to set up SMS.
3. Add an age gate to a form to begin using SMS.

## Important note for age-gated accounts

Any brands using Klaviyo for SMS are responsible for making sure you have stored the date of birth for these profiles.

To check that all subscribers have a DOB if you weren't using age-gating, there are several segments you can use, depending on your setup.

****Example 1: Is consented to SMS but there's no DOB****

The following segment is useful if you want to add a birthday to a profile so that you have this info all in one place. For instance, you can target an age-gated form to this segment.

- **Is consented to SMS**
  AND
- **\*Does not have a DOB on their profile**

\*Note that for the second condition, you must change the **Type** to **Text.**

![Segment of profiles with SMS consent but not a birthday](https://klaviyo.zendesk.com/hc/article_attachments/37218576027163)

****Example 2: Is consented for SMS and is above the legal age in a country****

If you do have a DOB, you can create a segment of everyone who's above the legal age in a specific country. This way, you can then import profiles and add age-gated consent.

Note that you should change the date to the current date and subtract either 21, 18, or 16 years, depending on the legal age in a specific country.

![Segment of profiles with SMS consent and above the legal drinking age](https://klaviyo.zendesk.com/hc/article_attachments/37218576030747)

To make this into age-gated consent, you can:

- Export the segment.
- Change the date field column to **Age Gated Date of Birth**.
- Re-import this list.

## What you can and can’t do as an age-gated account

Once you’re approved by Klaviyo, you’ll be able to start growing your SMS list and importing subscribers. However, there are some differences in doing this as an account that requires age-gating versus one that doesn’t.

Note that age-gated accounts can only collect promotional consent, not transactional consent.

### Collecting SMS consent

Age-gating is not available with all SMS consent collection methods.

Having an age-gated form when a visitor arrives reduces the likelihood of your number from getting audited or shut off.

Check the table below to see how you can grow your SMS list as an age-gated account.

|  |  |
| --- | --- |
| ****Allowed (with age gate)**** | ****Never allowed**** |
| Forms (popups, embeds, etc.) | Subscribe keywords |
| Subscribe pages | Consent at checkout |
| Tap-to-text forms, pages, and buttons |
| API calls |

The steps to [creating SMS forms](https://help.klaviyo.com/hc/en-us/articles/9351341171995) or subscribe pages are almost the same as they are for non-age-gated accounts.

The only differences are that:

- You must include the age gate field in your form.
- You must target forms to specific countries.

Subscribers must fill out the age gate before consenting to SMS. Thus, you should use a muIti-step form, with the age gate on the first step and the option to subscribe to SMS as the second step.

![Age gate on a form](https://klaviyo.zendesk.com/hc/article_attachments/28716356147227)

The age-gate field can not be used to trigger [date property flows](https://help.klaviyo.com/hc/en-us/articles/360002732652).

****Why can’t I use keywords or consent at checkout?****

Unfortunately, Klaviyo does not support age-gating with these opt-in methods due to the way people provide consent. The only way Klaviyo can properly age-gate consent is through the age-gate field.

****Can I use the regular date field rather than the age-gate field when collecting SMS consent?****

No, you cannot use the normal date field as a replacement for the age gate field.

The normal date input field does not verify that individuals are the legal age. This is because the date for that field is not always a date of birth. While that’s the most common use case, the normal date field can be used for other dates as well, including wedding and due dates.

### Importing SMS consent

When [importing SMS consent](https://help.klaviyo.com/hc/en-us/articles/360035428731), we strongly recommend including the following columns:

- **Age Gated Date of Birth**
- **SMS Consent Timestamp**

While both fields are optional, they are critical for your compliance and records. For example, if you ever need to confirm to a carrier during an audit that someone was of-age when they became an SMS subscriber.

If you don’t include a valid date of birth when importing SMS consent, the profiles will be uploaded without consent in Klaviyo.

## Next steps

After you set up age-gating in your account and reviewed the dos and don'ts, you can begin using SMS. Note that some information in these resources may not apply to age-gated accounts.

- Check out our [getting started with SMS resource](https://academy.klaviyo.com/getting-started-with-sms)
- Learn about [creating popups to start building your SMS list](https://help.klaviyo.com/hc/en-us/articles/9351341171995).
- See how to [set up an SMS welcome flow](https://help.klaviyo.com/hc/en-us/articles/360036122291).