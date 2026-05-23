<h1>How to set up iOS universal links and Android App Links</h1>

## ****About universal links and App Links****

Universal links (for iOS) and App Links (for Android) direct your customers to content within your mobile app or, if the app isn't installed, to the same content on your website. Using these links in email and text messages allows you to use consistent URLs across all your marketing channels while creating a seamless experience for your customer, no matter their device. It's similar to traditional deep linking, but with additional functionality.

Universal links and App Links in Klaviyo are fully compatible with click-tracking and UTM tracking.

## ****How it works****

After configuration, when a customer clicks a link in one of your messages from a mobile device, Klaviyo is able to correctly identify and route them to the correct location in your mobile app if it's installed on their device. If the app is not installed, the customer will be taken to your website as usual.

In platforms that don't support this functionality, click-tracking interferes with universal links and App Links. This is because click-tracking uses a redirect to capture the click event, which prevents the app from opening directly.

Your mobile app must be using at least version 5.1.0 of the iOS SDK, version 4.1.0 of the Android SDK, or version 2.1.0 of the React Native SDK to set up universal links in email and text messaging.

## ****Before you begin****

Before you can set up universal links and / or App Links in Klaviyo, you'll need to have the following in place:

- Your mobile app must be using at least version 5.1.0 of the iOS SDK, version 4.1.0 of the Android SDK, or version 2.1.0 of the React Native SDK to set up universal links in email and text messaging.
- For links in ****email****, a ****dedicated click-tracking domain****. For set up instructions, see our article on[how to set up a dedicated click-tracking domain](https://help.klaviyo.com/hc/en-us/articles/360001550572).
- For links in ****text messages****, a ****branded custom link****. For set up instructions, see our article on[how to create a branded shortened link for SMS](https://help.klaviyo.com/hc/en-us/articles/17649597637147).
- The ****Klaviyo SDK installed**** on your mobile app.
- An `apple-app-site-association` ****(AASA) file**** (for iOS) and/or an `assetlinks.json` ****file**** (for Android) hosted on your website domain. These files are required by Apple and Google, respectively, to associate your website with your mobile app.
- Your ****mobile app must be configured to support universal links and / or App Links****.
  - For more information on configuring for iOS and setting up your `apple-app-site-association` (AASA) file, please see [Apple's developer documentation on supporting associated domains](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content/).
  - For more information on configuring for Android and setting up your `assetlinks.json` file, please see [Android's developer documentation on adding app links](https://developer.android.com/training/app-links).

## ****How to set up universal links and App Links in Klaviyo****

1. Navigate to ****Settings**** in your Klaviyo account.
2. Click ****Push notifications****.
3. Select the ****Universal & app links**** tab.
4. In the card, click ****Set up****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/42123623612955)
5. Select a click-tracking domain for the channel you wish to enable (email and/or text messages).
6. Enter your target domain. This is your website domain that you plan to use in the body of your messages.
7. Upload your `apple-app-site-association` (AASA) file and/or your `assetlinks.json` file.

   - If you have both an iOS and an Android app, you will need to upload both files.
   - If you only have an iOS app, you only need to upload an AASA file.
   - If you only have an Android app, you will need to upload both files.
8. Click ****Save****.
9. Return to the settings page. Select the click tracking domain(s) that should open on your app and ****click Enable****

![](https://klaviyo.zendesk.com/hc/article_attachments/42123631357339)

## ****Universal override****

In some cases, you may want to designate a specific link to open in your app, even if it doesn't match the paths defined in your AASA or `assetlinks.json` file. You can do this by adding the `universal="true"` attribute to the link's HTML.

For example: <a href="trk.example.com" universal="true">Link to your app!</a>

Alternatively, you can do the inverse by adding the `universal="false"` attribute to the link's HTML.

Note: This functionality is only available for email.

## ****Testing your setup****

To test your universal links and App Links, create a new campaign or flow message and include a link to a page on your website that you've configured for deep linking. Send a message to a device with your app installed, and another to a device without your app installed.

- On the device with your app installed, the link should open directly in your app.
- On the device without your app installed, the link should open in the device's web browser.

Note: Preview messages do not use click-tracking, so links may not be reflected accurately. For proper testing, do not use preview messages.

## ****Viewing your Klaviyo-hosted universal links and App Links files****

Once you've completed the setup, Klaviyo will host versions of your configuration files. To view them, navigate to the following URLs in your browser, replacing `<YOUR_TRACKING_DOMAIN>` with your own domain:

- ****iOS:**** `https://<YOUR_TRACKING_DOMAIN>/.well-known/apple-app-site-association`
- ****Android:**** `https://<YOUR_TRACKING_DOMAIN>/.well-known/assetlinks.json`

## ****FAQ****

****Do I need to have a dedicated click-tracking domain?**** A dedicated click-tracking domain is required to use universal links and App Links for email. For SMS, you will need to set up a branded custom short link.

****What happens if I have multiple Klaviyo accounts that share a single tracking domain?**** If multiple accounts share a single tracking domain, changes to the domain configuration will affect all of those accounts.
