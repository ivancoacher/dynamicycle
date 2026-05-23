<h1>Understanding how segment conditions evaluate null or empty values</h1>

## You will learn

Learn about segmentation and properties that aren’t set or have no values in Klaviyo. These changes were implemented in April 2023.

In addition to the changes outlined below, all segmentation with dates now uses the UTC timezone. Learn about the changes to [segmenting with dates](https://help.klaviyo.com/hc/en-us/articles/4403222359451).

## Key terms

- ****Property not set****A property that doesn’t exist on a profile
- ****Property with no value****
  A property that is set on a profile, but doesn’t have an associated value

## Properties that aren’t set and booleans

In boolean conditions (i.e., true/false conditions), properties that don’t exist are no longer considered in the evaluation.

- ****Old system****Profiles where property does not exist used to be evaluated as False.
- ****New system****Profiles where property does not exist are now excluded from evaluation.

Consider the condition ****Properties about someone > VIP > is False****. A Klaviyo account contains the following profiles:

|  |  |  |
| --- | --- | --- |
| ****Profiles**** | ****Under the old system:**** | ****Under the new system:**** |
| 100 profiles where ****VIP = true**** | 🚫 Excluded from segment | 🚫 Excluded from segment |
| 50 profiles where ****VIP = false**** | ✅ Included in segment | ✅ Included in segment |
| 25 profiles where ****VIP property**** is not set | ✅ Included in segment | 🚫 Excluded from segment |

Before the change, this segment contained ****75 profiles****. After the change, it includes ****50 profiles****.

### Why this is better

The new system more accurately evaluates only True or False conditions, and you have the option to explicitly include profiles where that property is not set, if desired, by adding the condition ****OR Properties about someone > [profile property] > is not set****.

## Properties that aren’t set and text conditions

Historically, when evaluating profile properties that don’t exist for text conditions, these values have been treated as if they contain the text “None.” Now, these values are excluded from consideration in text conditions.

- ****Old system****Text conditions that searched for strings like “N,” “No,” and “None” included properties that aren’t set.
- ****New system****Properties that don’t exist on the profile are now excluded from evaluation.

Consider the condition ****Properties about someone > Do you eat tofu > contains “No”****. A Klaviyo account contains the following profiles:

|  |  |  |
| --- | --- | --- |
| ****Profiles**** | ****Under the old system:**** | ****Under the new system:**** |
| 50 profiles where ****Do you eat tofu = Yes**** | 🚫 Excluded from segment | 🚫 Excluded from segment |
| 25 profiles where ****Do you eat tofu = No**** | ✅ Included in segment | ✅ Included in segment |
| 15 profiles where the property ****Do you eat tofu**** is not set | ✅ Included in segment | 🚫 Excluded from segment |

Before the change, this segment contained ****40 profiles****. It would count the 25 who answered “No,” and the 15 profiles where that value was not set, because it was treating their empty values as “None.” After the change, it includes ****25 profiles****.

### Why this is better

The new system does not erroneously set the string “None” in profile properties that aren’t set. This means that any searches that include “N,” “No,” “Non,” and “None” will no longer include these properties.

## Properties that aren’t set and negative conditions

When a segment uses negative conditions (i.e., a profile property “is not” a specific value, or “does not contain” a specific string), the segment will no longer include properties that aren’t set.

- ****Old system****Properties that aren’t set used to be included in segments with negative conditions.
- ****New system****Properties that aren’t set are now excluded from evaluation.

Consider the condition ****Properties about someone > Favorite color > doesn’t equal > red****. A Klaviyo account contains the following profiles:

|  |  |  |
| --- | --- | --- |
| ****Profiles**** | ****Under the old system:**** | ****Under the new system:**** |
| 60 profiles where ****Favorite color = red**** | 🚫 Excluded from segment | 🚫 Excluded from segment |
| 45 profiles where ****Favorite color = blue**** | ✅ Included in segment | ✅ Included in segment |
| 100 profiles where the property ****Favorite color**** is not set | ✅ Included in segment | 🚫 Excluded from segment |

Before the change, this segment contained ****145 profiles****. After the change, it includes ****45 profiles****.

### Why this is better

The previous system was ambiguous, and it was unclear why certain profiles were being included when they did not have a profile property. There was also no straightforward way to exclude those profiles if desired.

The new system makes it explicit that only profiles where the property is set are included. If you want to include profiles which do not have the profile property set, you can do so by adding ****OR Properties about someone > [profile property] > is not set****.

## Countries that aren't set and the "Is or is not within the EU (GDPR)" criteria

When a segment criteria contains the definition “If someone is or is not within the EU (GDPR)” “Location is not within European Union/United States,” the segment will no longer include profiles where the Country property is not set.

- ****Old system****Profiles where property does not exist used to be included in this segment.
- ****New system****
  Profiles where property does not exist are now excluded from evaluation.

Consider the condition ****If someone is or is not within the EU (GDPR) > Location is not > within > European Union****. A Klaviyo account contains the following profiles:

|  |  |  |
| --- | --- | --- |
| ****Profiles**** | ****Under the old system:**** | ****Under the new system:**** |
| 50 profiles where ****Country**** = USA | ✅ Included in segment | ✅ Included in segment |
| 40 profiles where ****Country**** = Spain | 🚫 Excluded from segment | 🚫 Excluded from segment |
| 20 profiles where ****Country**** = France | 🚫 Excluded from segment | 🚫 Excluded from segment |
| 100 profiles where the property ****Country**** is not set | ✅ Included in segment | 🚫 Excluded from segment |

Before the change, this segment contained ****150 profiles****. After the change, it includes ****50 profiles****.

### Why this is better

The new system more accurately evaluates only profiles with a known country. You can the option to explicitly include profiles without a known country, if desired, by adding the condition ****OR Properties about someone > Country > is not set****.
