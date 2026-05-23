<h1>Profiles and properties glossary</h1>

## You will learn

The glossary below defines common terms regarding profiles and properties in Klaviyo.

## A

****Active profiles****: any profiles in Klaviyo that can be messaged and who are not suppressed.

****Activity feed****: a list of metrics that are associated with a profile to capture a timeline of their interactions with your business. While the default view is to include All Metrics, you can choose to only view activity around a specific metric from the associated dropdown instead.

****Address****: the primary address of a given profile.

****Address 2****: the second line of a profile’s address, if applicable.

## C

****Channels****: a section found on the right-hand side of a profile; it describes what channels (i.e., SMS, email, push notifications) the contact has opted in to receive from your brand. It will also provide opt-out information (if applicable) and the profile’s consent-status.

****Charts****: a section within a profile where you can more deeply analyze a contact's engagement around available metrics; it is located in the upper right-hand corner of a profile.

****City****: the city that a profile is located in.

[****Consent****](https://klaviyo.zendesk.com/hc/en-us/articles/360037101072): whether the profile has consented to receive your marketing channels.

****$consent\_form\_id****: the ID of the form that collected a profile's consent (if applicable).

****$consent\_form\_version****: the version of the form that collected a profile's consent. This only applies if you run A/B tests and have multiple variations for the specific form.

****$consent\_method****: the method through which a profile consented to receive marketing from your brand (e.g., via a form, at checkout, etc.).

****Contact****: a section found on the right-hand side of a profile; it is automatically populated by Klaviyo and includes the contact’s general contact, location, and social information.

****Country****: the country that a profile is located in.

****Coupons****: a section found on the right-hand side of a profile that contains information about coupons and coupon codes that a customer has received. This section won't appear if a customer has not received any coupons. Moreover, it will only include unique coupon codes created in Klaviyo, not static codes that you create in Shopify or another ecommerce platform.

****Custom properties****: properties that you generate yourself and are specific to your content, brand, and use case; they’re found under **Custom Properties** in the **Information** section of a profile. Properties added by integrations will also appear as custom properties.

## D

****Date Added****: an option found in the **Property** column when exporting a list or segment. This reflects the date the profile was added to the list or segment being exported.

## E

****Email****: the profile’s email address.

## F

[****First Active****](https://klaviyo.zendesk.com/hc/en-us/articles/115005247028): the first time that a profile engaged with your account. The date recorded represents the first time the contact was active (e.g., opened or clicked an email, visited your website, made a purchase, etc.)

****First Name****: the profile’s first name.

## I

****$id****: the external ID that can be used as a primary identifier on the profile — typically used in place of an email address. Note that using the $id property for identifying profiles is often not a best practice. It should only be used if you plan to use $id instead of email to identify profiles; otherwise there's a risk of duplicate profiles existing in your account. If you choose to do this, please refer to our [API documentation](https://developers.klaviyo.com/en/reference/api_overview) to learn how to use it for template sends, personal messages, and targeted exports. As of April 2022, the external id ($id) property has a limit of 64 characters.

[****Information****](https://klaviyo.zendesk.com/hc/en-us/articles/115005247028): a section found on the right-hand side of a profile that contains the Klaviyo-assigned **First Active** and **Last Active** dates, how the contact found you, their custom property values, and the date and time the profile was created and updated.

## K

[****Klaviyo ID****](https://klaviyo.zendesk.com/hc/en-us/articles/115005247088): a unique ID that you can find by navigating to a profile and looking for the 26-character ID (or 6-character ID in some cases) in the URL.

****Klaviyo properties****: default properties in your Klaviyo account. You will find them in various spots within a profile; when exported in a CSV file, many are identified by a dollar sign ($) prefix.

## L

****Last Active****: the date of the most recent recorded activity that the profile has taken.

****Last Click****: the date of this profile’s most recent recorded click.

****Last Name****: the profile’s last name.

****Last Open****: the date of this profile’s most recent recorded open.

****Latitude****: the latitude associated with the profile’s location.

****Lists & Segments****: a section found on the right-hand side of a profile that shows all of the lists and segments someone is a member of, the date they were added, and the ability to remove them from each list or segment.

****$locale:**** the locale of the profile stored in [IETF BCP 47 language tag format](https://www.rfc-editor.org/info/bcp47). Shopify's locale field syncs automatically to $locale in Klaviyo.

****$locale\_language:**** the [ISO 639-1/2](https://www.iso.org/iso-639-language-code) language sub-tag derived from the $locale property.

****$locale\_country:**** the [ISO 3166 alpha-2](https://www.iso.org/iso-3166-country-codes.html) country sub-tag derived from $locale property.

****Longitude****: the longitude associated with the profile’s location.

## M

****Messages****: the profile’s personal inbox in Klaviyo, located in the upper right-hand corner of a profile. Here, you can review scheduled, sent, and skipped emails and also message them directly. While flows and personal messages are visible from the scheduled tab, campaigns are excluded.

****Metrics****: a section found on the right-hand side of a profile where you can adjust which metrics you see on the profile. This section will quantify metric activity from the last 30 days as well as all-time.

## O

****Organization****: the organization (i.e. place of business) where this profile works.

## P

****Phone Number****: the profile’s phone number.

[****Predictive Analytics****](https://klaviyo.zendesk.com/hc/en-us/articles/360020919731): a section found on the right-hand side of a profile that displays the contact's customer lifetime value (including historic, predicted, and total CLV), churn risk prediction, average time between purchases, and order timeline. You will only see this section if you have at least 500 customers who placed an order, an ecommerce integration (e.g., Shopify, BigCommerce, etc.) or use our API to send placed orders, at least 180 days of order history, placed orders within the last 30 days, and at least some customers who have placed 3 or more orders.

****Profile****: a contact stored in your Klaviyo account.

****Profile Created On****: the date that the profile was created in your Klaviyo account.

****Profile property****: a characteristic associated with a contact’s profile that you can use to create robust segments, trigger flows, craft targeted messaging, and more.

## S

****SMS Consent Timestamp****: a timestamp that appears on a profile when they subscribe to SMS marketing from your brand.

****SMS promotional consent****: consent for SMS marketing messages, which includes SMS campaigns and all flows. With promotional consent, you can also send transactional messages.

****SMS transactional consent****: consent for SMS transactional messages, including SMS conversations, order updates, and other post-purchase flow messages.

****Source****: the source through which your profile came into your account. By default, all new signups have this property as a hidden field to identify the form that they used to sign up. It is found on all profiles regardless of their consent status and will align with the name of the form used. Source will be captured as a custom property under the Information section of the profile and it's captured as **$source**.

****State / Region****: the state or region where a profile is located.

[****Suppressed profiles****](https://klaviyo.zendesk.com/hc/en-us/articles/115005246108): profiles in Klaviyo who can no longer be emailed. A person can become suppressed because they unsubscribed or marked an email as spam, an email sent to them hard bounced or soft bounced more than seven times, they were suppressed in a previous email service provider, or you manually suppressed them

## T

****Timezone****: the time zone associated with the profile’s location.

****Title****: the title (e.g., position) this profile holds at their company.

## Z

****Zip Code****: the zip code (i.e. postal code) associated with the profile’s location.
