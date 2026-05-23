<h1>Understand data transformation in Klaviyo</h1>

## You will learn

Learn about the data transformation tool in Klaviyo, and how you can use it to make your data more useful.

[Advanced KDP](https://help.klaviyo.com/hc/en-us/articles/17655007276059) is not included in Klaviyo’s standard marketing application, and a subscription is required to access the associated functionality. Head to our [billing guide](https://help.klaviyo.com/hc/en-us/articles/115000976672) to learn how to purchase this plan.

![](https://fast.wistia.com/embed/medias/r18x9gg89n/swatch)

## Transform data

To transform data in Klaviyo:

1. Navigate to the **Transformation** tab under ****Advanced KDP********>********Data management > Transformation****.
2. Choose a pre-built transformation, or select the ****Create**** button to define your own transformation rules from scratch.
3. If creating your own transformation, choose the profile property you’d like to transform, along with the transformation method. The transformed property and values will be saved under a new profile property called **Property\_transformed**; **Property** being the name of your original profile property with the **\_transformed** suffix appended.

Additional transformations can be not applied to the transformed version of a property (i.e., **Property\_transformed**).

![Transformation tab in CDP navigation](https://klaviyo.zendesk.com/hc/article_attachments/28716356228123)

Only the following roles can create, edit, and delete transformations:

- Owner
- Admin
- Manager

## Transformation methods

The data transformation tool in Klaviyo allows you to make the following transformations to your profile property values:

- ****Format****
  Reformat profile property values.
- ****Standardize****
  Set rules to automatically replace specific profile property values.
- ****Merge****
  Merge multiple custom profile properties into 1 property

Only a single **Format** and **Standardize** transformation can be applied per profile property

Transformations to profile property values apply to all existing profiles and will continue applying on an ongoing basis.

### Format

The Format transformation method has 5 formatting options:

1. ****Remove spaces****
   Deletes spaces at the beginning and end of values (e.g., “ ABC” to “ABC”).
2. ****Delete quotes****
   Deletes quotation marks at the beginning and end of values (e.g., “ABC” to ABC).
3. ****Delete special characters****
   Deletes all characters that are not numbers and letters (e.g., A,B,C to ABC).
4. ****Capitalize the first letter of every word****
   Capitalizes the first letter of each word (e.g., John doe to John Doe).
5. ****Revise date format****
   Revises date and time formats so they can be stored in a consistent format. You can format either dates only, or date and time. Dates are stored in the ISO 8601 format in our system (YYYY-MM-DD, and YYYY-MM-DD HH:MM:SS.SS), but how they appear in the app will depend on your locale.

You can select as many of the formatting options as you wish when transforming a property’s values.

![revise dates.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716356253723)

Multiple formatting rules are applied in the following order:

1. Remove spaces
2. Delete quotes
3. Delete special characters
4. Capitalize words
5. Revise dates

****Example Format transformation****

In this example, the **Format** transformation is being applied to the **Name** profile property in Klaviyo using the formatting rules:

- Remove spaces
- Remove special characters
- Capitalize the first letter of every word

If the original **Name** profile property has the value set to **“alex!”**, this transformation would result in the creation of a new profile property called **name\_transformed**, with the value set to **Alex.**

###

### Standardize

With the standardization transformation method, you can set rules to automatically replace specific profile property values.

![Standardize transformation rules](https://klaviyo.zendesk.com/hc/article_attachments/28716356234395)

To create a standardization rule:

1. In the **If value** condition, select **Contains** or **Equals.**

   The **Contains** operator requires the property value being replaced to contain the specified substring you enter for the **If value**. Note that the entire property value will be replaced, not just the substring matched. **Contains** only supports text values.

   The **Equals** operator requires an exact match between the value being replaced and the replacement value. The entire property value will be replaced by the replacement value.
2. Select the [data type](https://help.klaviyo.com/hc/en-us/articles/115005237648) for the **If value**.
3. Enter your desired values to be replaced in the **If value** condition. You'll see a drop-down showing up to 512 unique values that exist on your account for the property being transformed. You can include up to 30 values in one condition, or create a new value by selecting the **Enter new value** option in the drop-down.

   ![Multiple values set from drop down for standardize condition](https://klaviyo.zendesk.com/hc/article_attachments/28716333272091)

   Properties with a large number of unique values like **Email**, **Phone Number,****First Name,** and **Last Name** will not appear in drop-downs.
4. In the **Replace with** condition, select the [data type](https://help.klaviyo.com/hc/en-us/articles/115005237648) for the replacement value.
5. Enter your desired replacement value in the **Replace****with** condition.

For the list data type, values must be in square brackets with comma separated values within (e.g. [1,2,3] or [A,1,True])

You can create up to 10 standardization rules, which are interpreted with "If else” logic. If the first condition doesn’t match, the next will be evaluated, and this will continue until a condition matches. After there is a match, the remaining conditions are not evaluated. If no condition matches, the original value will be set for the transformed profile property.

****Example Standardize transformation****

In this example, the **Standardize** transformation is being applied to the **Country** profile property using the standardization rules:

- If value contains **America** Replace with **USA**
- If value equals **Can** Replace with **Canada**
- **If value equals “Canada” Replace with Canada**

If the **Country** profile property has the value set to **America**, this transformation would result in the creation of a new profile property called **country\_transformed** with the value set to **USA.** If the value for the **Country** property was originally set to “**Canada”**, this would create the **country\_transformed** property with the value set to **Canada**.

### Merge

The **Merge** transformation allows you to combine multiple custom profile properties into 1, allowing you to effectively use the data in segments in templates.

Transformations are applied in the following order:

1. Merge
2. Format
3. Standardize

   To create a merge rule:
4. Select up to 10 profile properties to merge. By default, the merge must include 2 properties, but more can be included with the **Add** button.

The order of the properties included in the transformation determines how the values are prioritized during the merge, with items at the top of the list having the most priority. In the example above, **Hair type** will be the primary property that gets set on profiles as part of this merge.

![marge_hair_type.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716356261659)

2. To change the priority of properties included in the merge, use the up and down arrows.

3. Select ****Save**** once your merge transformation is set up.

You can combine up to 10 properties with a single **Merge** transformation. Note that once you save the transformation, you can no longer change the topmost priority. Instead, you can delete the transformation and create a new one.

****Example Merge transformation****

In this example, the **Merge** transformation is being applied to the **Birthday** and **Birthdate** properties to combine into a single property called **Birthday\_transformed**.

![brithday:birthdate.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716356256027)

If a profile has the **Birthday** property set to 06/07/1998, and another has the **Birthdate** property set to 06/04/2001, the transformation will result in each of the unique properties to be updated to **Birthday\_transformed**, and keep their original values.

## Pre-built transformations

There are 4 pre-built transformations you can quickly enable with the **Transformation** tool.

1. ****Format first names****
   Capitalize the first name of profiles for consistency in your messaging (e.g., **alex** to **Alex**).
   ![Pre-built transformation to format first names with capital letters](https://klaviyo.zendesk.com/hc/article_attachments/28716333274139)
2. ****Standardize country names****
   Standardize common country names so they all have the same value, allowing for consistency across similar profiles and easier segmentation(e.g., **U.S.** or **USA** to **United States**).
   ![Pre-built transformation to standardize variations of country names](https://klaviyo.zendesk.com/hc/article_attachments/28716333281179)
3. ****Standardize U.S. state names****
   Standardize the values for all 50 states, allowing for consistency across similar profiles and easier segmentation (e.g., **NY** or **New york** to **New York**).
   ![Pre-built transformation to standardize variations of U.S. state names](https://klaviyo.zendesk.com/hc/article_attachments/28716356247195)
4. ****Format birthdays****
   Format birthday properties for consistency in segmentation and messaging.

![format dates prebuilt.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716333294363)

To implement a pre-built transformation, navigate to the **Transformation** tab under **Advanced KDP**. If this is your first transformation, you’ll immediately see the prebuilt transformations on the page. If you already have previous transformations, select ****Create****.

![prebuilt_transform .jpg](https://klaviyo.zendesk.com/hc/article_attachments/28716333296539)

When you select a pre-built transformation, you’ll be brought to the transformation builder with the rules already defined. You can add or edit any of these rules here based on the needs of your brand.

![Transformation bulder for standarize states pre-built transformation](https://klaviyo.zendesk.com/hc/article_attachments/28716333286043)

If you try to apply a pre-built transformation to a profile property which already has a transformation of that type (i.e., **Standardize** or **Format**) you will see an error message as only a single transformation of each kind to a property.

Once you are ready to apply a pre-built transformation, select ****Save**** in the transformation builder. The transformation will be activated and will be visible on your transformation list.

![Saved transformations](https://klaviyo.zendesk.com/hc/article_attachments/28716356251291)

## Managing transformations

Once you have a data transformation created in Klaviyo, you’ll see it listed on the **Transformations** page with the following details:

- ****Profile property****
  The name of the original profile property that is being transformed.
- ****New profile property name****
  The name of the transformed profile property.
- ****Transformation method****
  The transformation method used.
- ****Status****
  The status of the transformation (i.e., **Active**, **In progress**, **Inactive**).
- ****Last edited****
  The timestamp of the most recent profile property transformation.
  ![List view of active transformations on account](https://klaviyo.zendesk.com/hc/article_attachments/28716356224667)

  You can have up to 30 transformations active at once.

  When a new transformation is first created, its status is **In progress**. While in this status, the transformation is being applied in bulk to existing profiles. Once bulk transformation is complete, the status becomes **Active**. Any new profiles or updates to existing profiles will be transformed live.

  From the menu next to each transformation, you can:
- Edit existing transformations
- Delete transformations
- Enable inactive transformations

To update or retransform a property, you can use the **Edit** option.

![Edit option to make changes to existing transformation](https://klaviyo.zendesk.com/hc/article_attachments/28716333279643)

Note that deleting a transformation will not delete already transformed properties saved under **Property\_transformed**, but the transformation will no longer be applied to any new data.

If you lose access to the Data transformation feature because a trial ended or you are no longer using the Advanced KDP add-on:

- All transformations will be set to the **Inactive** state.
- Transformations will no longer apply to new data.
- Previously transformed data will continue to be available.

If you decide to use the Advanced KDP add-on again in the future, you can manually set any inactive transformations to **Active** again.
