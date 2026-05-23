<h1>How to standardize country names and utilize standardized properties</h1>

## You will learn

Learn about the data transformation tool in Klaviyo, and how you can use it to make your data consistent and useful. With the standardization transformation method tool in Klaviyo, you can set rules to replace specific profile property values automatically, ensuring they all have the same value.

A common use case for this transformation is to standardize the country names on your account to make them easier to work with in segmentation and flows.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn how to purchase this plan.

## Standardize country names

You can either use Klaviyo’s pre-built country standardization transformation, or create a transformation from scratch.

### Standardize country names using a pre-built transformation

The data transformation tool has some pre-built transformations that you can easily enable, including 1 for standardizing country names.

To implement a pre-built transformation, navigate to ****Advanced KDP > Data management > Transformation****. If this is your first transformation, you’ll immediately see the pre-built transformations on the page. If you already have previous transformations, select ****Create****.![Create transformation button](https://klaviyo.zendesk.com/hc/article_attachments/28704479382555)

You’ll be brought to the transformation builder, where you can edit the pre-built standardization rules for country names to fit the needs of your brand.

![Pre-built transformation options](https://klaviyo.zendesk.com/hc/article_attachments/28704487426075)

By default, the pre-built transformation includes the following countries, along with different variations of each name:

- United States
- United Kingdom
- Canada
- Spain
- France
- Italy
- Germany
- Australia
- New Zealand
- Ireland

You can have up to 30 conditions within a standardization rule.

### Standardize country names from scratch

To create a standardization rule:

1. In the **If value** condition, select ****Contains**** or ****Equals****.

   The **Contains** operator requires the property value being replaced to contain the specified substring you enter for the **If value**. Note that the entire property value will be replaced, not just the substring matched. **Contains** only supports text values.

   The **Equals** operator requires an exact match between the value being replaced and the replacement value. The entire property value will be replaced by the replacement value.
2. Select the [data type](https://help.klaviyo.com/hc/en-us/articles/115005237648) for the **If value**.
3. Enter your desired values to be replaced in the **If value** condition. You'll see a drop-down showing up to 512 unique values that exist on your account of the property being transformed. You can include up to 30 values in one condition, or create a new value by selecting the **Enter new value** option in the drop-down.
   ![Different varations of the same property for USA](https://klaviyo.zendesk.com/hc/article_attachments/28704487428635)
4. In the **Replace with** condition, select ****Text**** as the [data type](https://help.klaviyo.com/hc/en-us/articles/115005237648) for the replacement value.
5. Enter your desired replacement value in the **Replace with** condition.

You can create up to 30 standardization rules, which are interpreted with “If else” logic. If the first condition doesn’t match, the next will be evaluated, and this will continue until a condition matches. Once a condition matches, the system stops evaluating the remaining conditions. If no condition matches, the transformed profile property will be set to the original value.

![Standardization modal in Klaviyo](https://klaviyo.zendesk.com/hc/article_attachments/28704487434267)

## Use cases for standardized country names

By standardizing country names with Klaviyo’s data transformation tool, it is much easier to utilize country data across Klaviyo. Below are common use cases for standardized country names in Klaviyo.

## Set up region-based flows

Standardizing country names allows you to more effectively personalize flows based on the region a customer is located in. Variations in country names can cause customers to go through conditional splits in a flow incorrectly, or require conditional splits with many conditions to account for each variation. By transforming country names, these variations can be standardized to a single format, making it easy to create splits based on a single value.

A conditional split in a flow creates 2 distinct paths, branching based on defined characteristics of your recipients. In this case, you can use the **Country\_tranformed** property in Klaviyo as the characteristic that will determine which branch a flow member will go down. This allows you to localize flow emails based on where a customer is located, and they will automatically receive the flow email that is most relevant to them. You can update content like product recommendations, include different privacy policies and terms and conditions, and otherwise personalize content to specific locales.

Learn how to add a [conditional split](https://help.klaviyo.com/hc/en-us/articles/115003872171) to a flow in Klaviyo.

In the example below, a conditional split sends customers entering a welcome flow down 2 different paths based on whether they are located in the United States. This allows you to better personalize the email subscribers receive based on location.

![Welcome series based on $country_transformed](https://klaviyo.zendesk.com/hc/article_attachments/28704479384347)

You can also combine multiple conditional splits based on the **Country\_transfomed** property to create a series of paths customers will go down until they reach the right split for their location. Flow members will travel down the **No** path for each split until they reach the split for their country, or eventually reach a default email if none of the splits are relevant to their location.

![Welcome series based on $country_transformed with multiple branches](https://klaviyo.zendesk.com/hc/article_attachments/28704479379867)

## Measure performance

Standardizing country names also allows you to more easily create custom reports to understand your performance by country. Variations in country names can make it more challenging to report on this data due to the large number of items for each country. With the transformation of country names in place, these variations will standardize to a single format, making it easy to create splits based on a single value.

To create reports in Klaviyo regarding performance by country, navigate to ****Custom reports**** > ****Analytics****.

![Custom reports in Klaviyo navigation](https://klaviyo.zendesk.com/hc/article_attachments/28704487436187)

Here, you can create reports to analyze your performance by country, or select a pre-built report from the **Reports Library**.

Learn more about [custom reports in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360047725651) and how to create them.

### Sales by country

In the **Reports Library**, you can find the **Sales by country** report that provides insight on the countries with the most sales for your brand. You can customize the events included in the report, as well as the timeframe you’d like to analyze.

To take advantage of your country name standardization, change the **Group or Filter** for the report to the **$country\_transfomed** property.

![Sales by $country_transformed repoirt](https://klaviyo.zendesk.com/hc/article_attachments/28704487427355)

### Email performance by country

In the **Reports Library**, you can find the **Engagement by country** report that provides insight on the countries with the most sales for your brand. You can customize the events included in the report, as well as the timeframe you’d like to analyze.

To take advantage of your country name standardization, change the **Group or Filter** for the report to the **$country\_transfomed** property.

![Engagement by $country_transformed report](https://klaviyo.zendesk.com/hc/article_attachments/28704487427739)

## Build regional segments

With the country name standardization, you can also easily create location-based segments. Since the values for country names are standardized, you don’t have to create multiple conditions to capture each variation of a country name.

To limit a segment to only include profiles in a specific country, use the following condition:

1. Properties about someone > $country\_transformed > equals > country
   ![Segment based on $country_transformed](https://klaviyo.zendesk.com/hc/article_attachments/28704479385371)
2. In the **Dimension value** field, enter the standardized name for the country you want to include in the segment.
3. Optional: To include multiple country conditions, combine them with an **OR** operator![Segment with multiple conditions using $country_transformed](https://klaviyo.zendesk.com/hc/article_attachments/28704487433627)

You can use these localized segments to personalize your marketing based on the country a profile is located in, targeting them with different content, like languages, deals, and product recommendations.

## Additional ways to use data transformation

The following common transformations can also help you clean and format data so it can be utilized more effectively in segmentation and personalization:

- Standardize U.S. state names
- Standardize city names
- Format first names
- Standardize genders
- Reformat custom profile properties like quiz results

## Additional resources

[Understand data transformation in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/17760400736539)

[How to add a conditional split to a flow](https://help.klaviyo.com/hc/en-us/articles/115003872171)

[Understanding branching best practices for flows](https://help.klaviyo.com/hc/en-us/articles/360051182592)
