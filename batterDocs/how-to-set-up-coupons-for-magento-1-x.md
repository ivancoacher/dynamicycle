<h1>How to set up coupons (for Magento 1.x)</h1>

Klaviyo's Magento 1 integration is no longer accepting new installations and will reach full end-of-support in late 2027. Klaviyo Support is no longer able to assist with Magento 1–related requests.

## You will learn

Magento supports [Shopping Cart Price Rules](http://docs.magento.com/m1/ce/user_guide/marketing/price-rules-shopping-cart.html) that can be used to apply a discount to a customer's order. Coupon codes can be created for existing price rules, so that shoppers can easily leverage a given code to apply a discount during the checkout process.

Klaviyo's Coupons for Magento feature allows Magento 1.0 stores to do the following:

- Create new coupons in Klaviyo associated with pre-existing price rules in Magento.
- Include dynamic coupons within flow emails, so each recipient receives a unique code.

This guide will explain how to get setup with Magento coupons in Klaviyo.

Dynamic coupon codes are not currently available when sending campaign emails. Sending unique coupon codes in a campaign would require generating thousands of codes per second. Klaviyo cannot guarantee a specific Magento server's rate-limiting settings will not impact the generation of dynamic coupons at this volume and velocity. Due to this, dynamic coupons are only available when sending flow emails.

## Requirements

As a prerequisite, ensure that you've [enabled the Magento integration in Klaviyo and installed the Klaviyo extension in Magento](https://help.klaviyo.com/hc/en-us/articles/115005082187).

## Enable the REST API

Start by enabling the REST API by creating a new REST Role and giving it full access, then assigning the role to one of your admin users.

1. Click on ****System > Web Services > REST - Roles****.
2. Create a new Admin role. For the field **Role Name** enter a name, for example "Administrator".
3. Click on the ****Role API Resources**** tab on the left. Set **Resource Access** to ****All**** and click ****Save Role****.
4. Next, navigate to ****System > Web Services > REST - Attributes****.
5. Select ****Admin**** from the list of user types.
6. Set **Resource Access** to ****All**** and click ****Save.****
7. Next, navigate to ****System > Permissions > Users****.
8. Select an admin user from the list and click ****Edit user****.
9. Click the ****REST role**** tab on the left sidebar.
10. Click the radio button to assign the new REST admin role to your user.
    ![](https://klaviyo.zendesk.com/hc/article_attachments/28717985502747)
11. Click ****Save User****.

You've now enabled the REST API for your Magento store.

If you are unsure whether or not your REST API is configured properly, please review the steps outlined in our [resource on troubleshooting coupons for Magento 1x](#h_01GZ248ZJVNJTRVFYKMTKFXFEK).

## Generate REST Credentials in Magento

To enable Klaviyo's Magento Coupons feature, first generate REST API credentials from your Magento store using the REST admin account you just made, and then paste these into your Klaviyo account.

1. Log in as the REST admin user you created in the [Enable the REST API section above](https://help.klaviyo.com/hc/en-us/articles/115005246547#enable-the-rest-api2)
2. Click on ****System > Configuration**** and then click on ****Klaviyo**** under the **Customers** section.
3. Click ****Generate OAuth Tokens****.![763276](https://klaviyo.zendesk.com/hc/article_attachments/28717985489051)

The **Consumer Key, Consumer Secret, Authorization Token** and the **Authorization Secret** will populate. You will copy/paste these values into your Klaviyo account in the next step.

## Setup Magento Coupons in Klaviyo

1. From your Klaviyo account, [navigate to your Magento integration](https://www.klaviyo.com/integration/magento).
2. Click the ****Advanced Options**** arrow to expand the **Coupon Settings**.
3. Paste in the REST credentials you created above.

   Your Magento server must support HMAC-SHA1 signatures for OAuth authentication.

   ![](https://klaviyo.zendesk.com/hc/article_attachments/28717985495067)
4. Click ****Update Magento Settings.****

Klaviyo will validate your REST credentials and you will be able to start creating coupons with the Coupons tab of your account.

## Create a Magento Coupon in Klaviyo

When you first navigate to [the **Coupons** tab in your Klaviyo account](https://www.klaviyo.com/coupons) after providing your REST credentials, you will see the message, "You haven't added any coupons yet."

Before you create a new coupon, you will first need to define a Price Rule in Magento that will include all the specifications for the coupon. Price Rules cannot be created from within Klaviyo. A new coupon created in Klaviyo must reference a pre-existing Price Rule in Magento.

When creating a Price Rule in Magento, note that the option to associate a new Price Rule with a specific coupon should be left set to Specific Coupon and you must have the **Use Auto Generation** checkbox selected.

1. Click ****Add Coupon**** to create a new coupon.
2. Fill in the following information: **Coupon Name** and the **Magento Rule ID.**

- ****Coupon Name:**** The name you specify can consist of only letters, numbers and underscores and can be up to 32 characters long
- ****Magento Rule ID:**** Create a rule in Magento first, and paste the ID of that rule here to associate it with this coupon

![](https://klaviyo.zendesk.com/hc/article_attachments/28717985497243)

All created coupons will appear with the following overview details:

- ****Coupon Name:**** Name of the coupon
- ****Active Timeframe:**** There are the following options:
  - Active, No Expiration
  - Date A - No Expiration
  - Date A - Date B
  - Active, Expires Date B
- ****Created Date:**** Date the coupon was created
- ****Last Updated Date:**** Date the coupon was last updated

Coupons can be edited and deleted from this tab via the dropdown on the right-hand side.
![](https://klaviyo.zendesk.com/hc/article_attachments/28717985500315)

## Use a Magento Coupon in a Flow Email

Once a coupon is created, you can insert it into a flow email using the following placeholder variable. You can only add one coupon code per email. You can display the same coupon code in multiple places, but you cannot use multiple codes.

```
{% coupon_code 'CouponName' %}
```

Replace **CouponName** with the name of your coupon. For example:

![mceclip0__2_.png](https://klaviyo.zendesk.com/hc/article_attachments/28717991395995)

## Use Unique Coupons in SMS Flow Messages

Unique coupons are also available for your [SMS/MMS messages](https://help.klaviyo.com/hc/en-us/articles/360044863132-Using-Unique-Coupon-Codes-in-SMS-and-MMS-Messages) in flows. Generate the codes just like you would for email. Then, use the template tag below to add the coupon code to your SMS or MMS message:

`{% coupon_code 'CouponName' %}`.

In the snippet, change **CouponName** to the name of the coupon you want and add it into the message (either flow or campaign).

![2020-06-16_17-58-37.png](https://klaviyo.zendesk.com/hc/article_attachments/47772696564635)

Unlike in emails, you can only use one coupon code per SMS message. With email, you have access to [hidden blocks](https://help.klaviyo.com/hc/en-us/articles/115005258208-Show-or-Hide-Template-Blocks-Based-on-Dynamic-Variables) to send different coupons based on where someone lives or what they’ve done. If you try to add multiple coupons to an SMS message, you will see an error message.

![2020-06-17_09-51-08.png](https://klaviyo.zendesk.com/hc/article_attachments/28717991397787)

## Troubleshoot Errors

### Error Message: “Unable to connect to the REST API with the specified REST credentials. Please check that these credentials are valid in your Magento admin."

If you are seeing this error message in Klaviyo, there are two likely root causes:

1. Your Magento server is not set up to support HMAC-SHA1 signatures for OAuth authentication.
2. You may have not enabled full role access for the REST API.

To resolve this issue, enable HMAC-SHA1 signatures for OAuth authentication on your Magento server. Then complete the following steps to update your REST permissions:

1. Uncomment, or add, the rewrite rule in your .htaccess file. This is the line you’ll want to ensure is un-commented:
   `RewriteRule ^api/rest api.php?type=rest [QSA,L]`
2. Double check that your REST Role is setup correctly
   We cover the instructions for this in our [guide to setting up coupons for Magento in the section linked here](https://help.klaviyo.com/hc/en-us/articles/115005246547#enable-the-rest-api).
3. Another common cause is that various Apache modules can strip “Authorization: Basic base64 (user:password)” header.
   Check out [this post for more information](https://devhacksandgoodies.wordpress.com/2014/06/27/apache-pass-authorization-header-to-phps-_serverhttp_authorization/)

### Coupon codes populated into emails by Klaviyo are not unique -- all recipients appear to be receiving the same code.

When creating a Price Rule in Magento, the option to associate a new Price Rule with a specific coupon should be left set to Specific Coupon and you must have the “Use Auto Generation” checkbox selected.

Click on your Price Rule in Magento, and under **General Information**, scroll down to the line option "Coupon" and change this setting to "Specific Coupon". Next, check the box for auto generation here. This should fix the issue and allow us to generate a new unique coupon code for each email recipient.
