<h1>How to use custom objects in segments</h1>

You must have access to [custom objects](https://help.klaviyo.com/hc/en-us/articles/35105337172123) to use this functionality.

## You will learn

Learn how to use custom objects in segments so you can create groups of customers based on object data.

Note that you must [create an object](https://help.klaviyo.com/hc/en-us/articles/35105337172123) first before you can use custom object data in segmentation.

## Build segments using object data

Just like profile properties, you can use object data to personalize your marketing through segmented groups of customers.

Learn [how to use segments in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908).

To access object data in the segment builder:

1. Navigate to ****Lists & Segments**** > ****Create segment****.
2. Select ****Properties about someone**** in the **Select a condition** dropdown.
3. Select the object you want to use in your segment condition from the **Object** group. All your available objects are listed here.
4. Set the object record count in the **Person** field.
5. Select an object property to filter on in the **Where** row.
6. Set the operator (i.e., **equals**, **doesn’t equal**, **is at least**, etc.).
7. Set a specific object property value in the **Dimension value field**.

You must type in your object property values exactly to see results in the **Dimension value** dropdown.

![](https://klaviyo.zendesk.com/hc/article_attachments/35158640997147)

### Filtering object conditions

You can filter object conditions to only allow profiles with records that meet your requirements to enter a segment. Object conditions in the segment builder can be filtered by:

1. The number of object records that a profile has.
2. The specific object property values for each object record.

You can apply up to 5 filters to an object condition.

****Object record count****

The object record count (i.e., the **Person** field in the segment builder) allows you to define how many qualifying object records a profile must have to enter the segment. For example, with something like a **Pets** object, this enables you to identify pet owners with multiple pets, each with their own object record.

The available record count filters are:

- ****Has at least one****Profile has at least one object record.
- ****Does not have any**** Profile does not have any object records.
- ****Has****Profile has an object record set.
- ****Does not have****Profile does not have an object record set.
- ****Has at least**** Profile has at least X object records.
- ****Has more than****Profile has more than X object records.
- ****Has fewer than**** Profile has less than X object records.
- ****Has at most**** Profile has no more than X object records.

## Example segments using object data

These object properties are just examples, and the filters available to you are based on the object data sent to Klaviyo.

### **Pet** object

Say you have a **Pet** object that contains data about customers’ pets. You may want to create segments like:

- Profiles that have at least 3 cats, to target with coupons for bulk products like litter and food.
- Profiles with dogs under the age of 1, to target with marketing specific for pet owners with puppies.
- Profiles with dogs of a specific breed, for targeted marketing campaigns featuring dogs similar to their own.

### **Appointment** object

Say you have an **Appointment** object that contains data about customers’ appointments. You may want to create segments like:

- Profiles that have an upcoming appointment, to send them reminders.
- Profiles that all have appointments with the same person, to send them updates when their availability unexpectedly changed.
- Profiles that had a good experience during their appointment, to target with review requests.

## Additional resources

[Getting started with custom objects](https://help.klaviyo.com/hc/en-us/articles/35105337172123)

[Getting started with segments](https://help.klaviyo.com/hc/en-us/articles/115005237908)
