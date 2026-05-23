<h1>SMS opt-in methods reference</h1>

Learn about the different methods for growing your SMS list with Klaviyo.

By collecting SMS consent from these interested customers, you can send personalized and timely messages, such as order updates, exclusive promotions, and loyalty rewards, which can help you build a loyal customer base.

## Best practices for collecting SMS consent

Remember that your entire audience is a potential SMS subscriber, from new site visitors to one-time customers, email subscribers, or social media followers. When collecting SMS consent, there are a few best practices to keep in mind to grow your audience and drive revenue:

- SMS must be optional and cannot appear to be required. To accomplish this, SMS consent should be collected separately from any other marketing channel.
  - As a general best practice, use a multi-step form if you’re asking for both email and phone numbers so that there’s a clear, separate opt-in button for SMS.
- Set up your SMS compliance basics to build trust with your customers and maintain confidence from a legal standpoint:
  - [Create a mobile terms of service](https://help.klaviyo.com/hc/en-us/articles/360049177511) (TOS) to link anywhere you collect SMS consent.
  - [Update your privacy policy](https://help.klaviyo.com/hc/en-us/articles/4404199571867) to include a description of your SMS marketing program, how you store phone numbers and location data, and the types of messages you’ll send via SMS.
  - [Create SMS disclosure language](https://help.klaviyo.com/hc/en-us/articles/11644128409371), which must be included anywhere you collect SMS consent. On sign-up forms, it’s best practice to place disclosure language above the submit button, so subscribers understand what they’re opting in to before they sign up.
- While there are multiple SMS opt-in methods in forms, [Smart Opt-in](https://help.klaviyo.com/hc/en-us/articles/24743883751451) is the optimized method for list growth and streamlining the SMS subscription experience.

## SMS opt-in methods

Klaviyo provides a number of different ways to collect SMS consent:

- [Sign-up forms](https://help.klaviyo.com/hc/en-us/articles/27902671291419#h_01J472TF8016NMR0QED2C51BZ9), with options to collect phone numbers via:
  - Smart Opt-in
  - Tap-to-text
  - Phone number input field
- [SMS subscribe links](https://help.klaviyo.com/hc/en-us/articles/27902671291419#h_01J472TF80CTZTZRFWB7X44CVM)
- [Subscribe keywords](https://help.klaviyo.com/hc/en-us/articles/27902671291419#h_01J472TF80JCW3QWS3Z03JCG6Q)
- [Consent at checkout](https://help.klaviyo.com/hc/en-us/articles/27902671291419#h_01J472TF81SWB8YFR5VAGFCAPJ), available for:
  - Shopify
  - Magento 2
  - BigCommerce
  - WooCommerce
  - Prestashop
- [API](https://help.klaviyo.com/hc/en-us/articles/27902671291419#h_01J472TF81450BCHPSQVX6G9V7)

If you’re using a form or subscribe link to collect phone numbers, you can link directly to these in an email or on an Instagram page.

### Forms

There are 3 ways to collect phone numbers from your site visitors within a sign-up form:

1. Smart Opt-in (best practice for list growth)
2. Tap-to-text
3. Phone number input field

#### Smart Opt-in

You must have a paid SMS plan to configure Smart Opt-in in sign-up forms.

How it works:

1. Site visitors who input their phone number into your sign-up form instantly receive a message containing a 1-time passcode.
2. The sign-up form shows another step asking for the 1-time code to confirm their subscription and join your list.
3. The 1-time code auto-populates on iOS and Android browsers, so site visitors can seamlessly double opt-in without needing to take action in their messaging app.

![A mobile device showing an internet browser with someone entering their phone number into an input field on a form, then clicking the auto-fill one-time code that populates, and confirming subscription.](https://fast.wistia.com/embed/medias/6n4a2zlbw6/swatch)

Benefits:

- Optimizes list growth
  - Smart Opt-in is best practice for increasing list growth because it keeps shoppers on your site during the opt-in process, reducing friction and leading to higher opt-in rates.
- Seamless opt-in experience for your shoppers
  - Site visitors don’t need to take any action in their messaging app with Smart Opt-in, which minimizes the chance of distraction and brings speed and ease to the SMS opt-in experience.
- Accessible for all devices and sending numbers
  - Smart Opt-in works on all devices (e.g., desktop and mobile devices) and sending number types (e.g., long code, short code, branded sender ID, etc.).
- Utilizes 2-step consent process, similar to double opt-in
  - Collecting SMS consent via Smart Opt-in is similar to the double opt-in process in that visitors take 2 steps to opt in: entering their phone number, and then inputting the one-time code that they receive. Double opt-in is strongly recommended when collecting SMS consent, and in the US it is required if you plan to add SMS to your abandoned cart flows.

For setup guidance with Smart Opt-in, see [how to use Smart Opt-in to collect SMS consent](https://help.klaviyo.com/hc/en-us/articles/24743883751451).

#### Tap-to-text

How it works:

1. Site visitors on mobile and desktop devices see a different option:
   1. On desktop: users input their number manually into an input field.
   2. On mobile:
      - Users click on a button in a form.
      - The user’s messaging app opens with a pre-populated message that contains a subscribe keyword.
      - The user sends the message.
2. The next step depends on whether the keyword in your subscribe message uses single or double opt-in:
   - Single opt-in: the user becomes a subscriber immediately.
   - Double opt-in: the user must confirm their subscription before they fully become an SMS subscriber.

![Video of a user successfully subscribing to text updates via Klaviyo's Tap to Text](https://klaviyo.zendesk.com/hc/article_attachments/43033458821531)

Tap-to-text requires you to set up multiple forms if you plan to send to multiple countries, and it also does not work with branded sender IDs. In general, we recommend using Smart Opt-in, which has all of the same advantages without these disadvantages.

![A flowchart with two methods for a user to subscribe to a service using tap-to-text on either a desktop or mobile device.](https://klaviyo.zendesk.com/hc/article_attachments/28716119302427)

Benefits:

- Simple process
  - Users only need to tap a button and send a pre-populated message, making the opt-in process quick and easy.
- Reduces user errors
  - Eliminates the need for users to manually enter their phone number or other details on mobile, which minimizes the risk of typos or incorrect numbers.
- Utilizes 2-step opt-in process
  - By default, users must take 2 steps to become an SMS subscriber: tapping a button and sending a text. Not only is this good for compliance (since it’s similar to double opt-in), it also leads to a cleaner, more accurate subscriber list as sending the text verifies that the number is active and owned by the subscriber.
- Mobile optimization
  - Tap-to-text is an efficient opt-in method for shoppers on mobile devices, as it leverages the native functionality of mobile phones. You can use dynamic blocks to create distinct views in 1 form so that mobile shoppers see a tap-to-text experience and desktop shoppers see a phone number input field.

For setup guidance with tap-to-text, see [how to collect SMS consent with a tap-to-text form](https://help.klaviyo.com/hc/en-us/articles/9351341171995).

#### Phone number input field

How it works:

1. Site visitors can click the input field in your sign-up form.
2. Users manually enter their phone number.
3. They click the button to submit the form and subscribe to SMS marketing.

![Clicking a phone number input field block within the sign-up form editor and dragging and dropping into an example form's preview SMS opt-in step.](https://fast.wistia.com/embed/medias/u2waz8b93t/swatch)

Benefits:

- Easy setup
  - A phone number input field can be dragged into any sign-up form from the **Add blocks** tab within the form editor, and there’s no additional actions to configure.
- Familiar process
  - A phone number input field in a sign-up form collects phone numbers in a simple, familiar manner that works on all device types.

The phone number field is standard, but is not as mobile-friendly or streamlined as either Smart Opt-in or tap-to-text. In general, display this field only on desktop devices.

For setup guidance on phone number input fields, see [understanding form blocks and fields.](https://help.klaviyo.com/hc/en-us/articles/4413550187035)

### SMS subscribe links

How it works:

1. You create an SMS subscribe link and design a subscribe page.
2. You share that link in emails or post it on social media stories.
3. Clicking on the link automatically redirects:
   - Mobile users to a tap-to-text experience
   - Desktop users to a subscribe page with a phone input field

SMS subscribe links can only be used by long codes, short codes, and toll-free sending numbers. They are not available for branded sender IDs, as they are unable to receive text messages.

![A process flow for a new user promotion, specifically for signing up for SMS alerts to receive a 15% discount, that shows an SMS subscribe link workflow on desktop and on a mobile device.](https://klaviyo.zendesk.com/hc/article_attachments/28716058536603)

Benefits:

- Facilitates SMS list growth
  - SMS subscribe links are dynamic in launching the optimal SMS opt-in experience per shopper’s device, which reduces friction and allows shoppers to quickly sign up.
- Cross-platform accessibility and scale
  - The ability to share an SMS subscribe link in a social media post or story allows viewers to subscribe from any platform, broadening your reach.

Keep in mind that subscribe links only work for 1 sending number. For instance, if you use a toll-free number for both the US and Canada, you can use a single subscribe link to collect SMS subscribers in both countries. However, say you use a short code in Canada. In that case, you need to create a separate subscribe link for each country. You then need to display one link only to the US and the other only to Canada.

For guidance on how to create and share an SMS subscribe link, see [how to create an SMS subscribe link](https://help.klaviyo.com/hc/en-us/articles/14104388043931).

### Subscribe keywords

How it works:

1. Create custom subscribe keywords (e.g., “JOIN,” “TEXT,” “SUBSCRIBE”) in your Klaviyo account.
2. Promote that keyword and your dedicated sending number across various channels such as on your website, in emails, and on social media.
3. People text that keyword to your sending number to opt in to SMS marketing.
4. Upon texting the keyword, what happens depends whether the keyword uses single or double opt-in:
   - Single opt-in: the subscriber receives an automated confirmation message acknowledging their subscription and often providing a welcome message or offer.
   - Double opt-in: the user must confirm their subscription before they fully become an SMS subscriber.

Subscribe keywords can only be used by long codes, short codes, and toll-free sending numbers. They are not available for branded sender IDs, as they are unable to receive text messages.

![A flowchart showing a user subscribing to SMS marketing by sending an SMS message containing a dedicated subscribe keyword.](https://klaviyo.zendesk.com/hc/article_attachments/28716119304987)

Benefits:

- Ease of use
  - Subscribing via a simple keyword is quick and easy for customers, reducing barriers to opt-in.
- Instant opt-in
  - The process is immediate, allowing customers to subscribe in real-time without needing to navigate through forms or pages.
- Versatile usage
  - Keywords can be used in various contexts (e.g., during events, sales, at point of sale, etc.) and can be promoted in multiple locations to capture a wide audience.

Note that if you have [flows that reply to inbound SMS messages](https://help.klaviyo.com/hc/en-us/articles/360049930372), the flow can respond to any word (including, but not limited to, subscribe keywords).

For guidance on how to use subscribe keywords, see [how to add custom keywords](https://help.klaviyo.com/hc/en-us/articles/360050384091).

### Collect SMS at checkout

How it works:

- If you use Shopify, Magento 2, BigCommerce, WooCommerce, or PrestaShop you can ask for SMS consent at checkout to target shoppers that are highly engaged with your brand.
- Customers filling out their personal information during checkout can also check a box if they’re interested in opting in to SMS marketing.
- Customers who provide their phone number can confirm this opt-in by clicking to continue to the shipping details page in the checkout process. When they confirm the order, they also confirm their consent for SMS marketing.

![A SMS consent checkbox on an example checkout page showing someone who selected to subscribe to SMS marketing and then entered their phone number in an input field.](https://klaviyo.zendesk.com/hc/article_attachments/28716058534811)

Benefits:

- Streamlined user experience
  - By requesting consent when the customer is already providing information, this approach seamlessly integrates into the user experience, minimizing friction and increasing the likelihood of obtaining consent.
- Target an engaged and interested audience
  - Obtaining consent at the checkout stage ensures you are targeting individuals who have a genuine interest in your offerings, resulting in higher-quality leads for future marketing efforts.

For more information on who can collect SMS consent at checkout and how to set it up, see our [guide on collecting SMS consent at checkout on your website](https://help.klaviyo.com/hc/en-us/articles/25220861016091#h_01HWDX24XA6VWQKE862ZN0SY8K).

### API

How it works:

- You can import SMS consent into Klaviyo from a third-party application or via API.

  With this method, we recommend having your developer or someone experienced with making API calls test that you’re properly importing SMS consent into Klaviyo.

Benefits:

- You can import SMS consent from any platform you can build on with this method.

For guidance on collecting and syncing consent, see [how to collect SMS consent via API](https://developers.klaviyo.com/en/docs/collect_email_and_sms_consent_via_api).

## Inspiration for using these opt-in methods

### Including a subscribe link or a link to a sign-up form in an email

Send an email that includes a subscribe link or a link to one of your sign-up forms to encourage existing email subscribers to opt in to SMS marketing. Email subscribers already have an established relationship with your brand, so they are more likely to trust you and feel comfortable sharing their phone number for SMS communication.

Using a subscribe link or sign-up form link in an email:

- [Share an SMS subscribe link in an email](https://klaviyo.zendesk.com/hc/en-us/articles/14104388043931)
  You can create an SMS subscribe link to share in your emails so that anyone who clicks on it can easily opt in to SMS marketing.
- [Link to a sign-up form in an email](https://help.klaviyo.com/hc/en-us/articles/8185730542235)
  You can embed an SMS sign-up form in a landing page on your website, then send a message (e.g., a flow or campaign) to your existing email subscribers, directing them to the landing page where they can opt in to SMS marketing.

### Targeting your Instagram audience

Share an SMS subscribe link in an Instagram story to encourage immediate action from viewers who are already engaged with your content. Instagram stories can have high visibility, so sharing an SMS subscribe link in a story can help you reach a larger audience quickly.

Using a subscribe link in an Instagram story:

- Create an SMS subscribe link to share in your social media channels, such as Instagram, so that anyone who clicks on it can easily opt in to SMS marketing.
  - SMS subscribe links are dynamic in that they automatically optimize the sign up experience for shoppers across all devices, redirecting mobile shoppers to a tap-to-text experience, and sending desktop shoppers to the Klaviyo list’s unsubscribe page.

For more guidance on collecting SMS consent on Instagram, see [how to collect SMS subscribers with a tap-to-text link](https://help.klaviyo.com/hc/en-us/articles/360059544911#01H8PG1DGTHWPXGZ26TBCSX0YE).

### Turn an SMS subscribe link into a QR code

You can turn an SMS subscribe link into a QR code, making it easy for customers to share their contact information without slowing down checkout. By placing a QR code in your brick-and-mortar store or on promotional materials, shoppers can quickly scan it to sign up. Directing visitors to a subscribe page through a QR code helps your grow your SMS subscriber list so you can send personalized messages and offers that encourage repeat purchases.

To create a QR code for your subscribe link:

1. In Klaviyo, navigate to ****Audience > Growth tools****.
2. Scroll to **Manage subscribe links**, and click ****Manage****. If you have not already created one, create your first SMS subscribe link. Note that, for compliance best practices, the subscribe page your link is tied to should only collect phone numbers.
3. Next to the subscribe link you want to use, click ****Copy****.
4. Use a third-party tool (e.g., Swapt) to generate a QR code, pasting the copied SMS subscribe link as the destination URL.
5. Generate the code and get creative; add it to posters, business cards, flyers, and more.

### Showing a keyword on your website

Enhance engagement on your website by featuring interactive elements such as contests, surveys, or quizzes. Encourage visitors to participate by texting a specific keyword to your sending number. Incorporating a keyword with a contest or giveaway is an innovative strategy to boost SMS opt-ins and drive interaction; however, make sure to include disclosure language wherever you put the keyword.

Note that subscribe keywords are not available for branded sender IDs as they are unable to receive text messages.

Using a keyword for a survey on your website:

1. Use a third-party tool to create a quiz.
2. [Create a custom subscribe keyword](https://help.klaviyo.com/hc/en-us/articles/360050384091) and promote it on your website with your sending number (e.g., Text “FLAVOR” to 555555 to cast your vote for the next cookie flavor”).
3. Site visitors can text that keyword to your sending number to opt in to SMS marketing and engage with the survey.

When using custom keywords, it is imperative to clearly explain the purpose of the sign up (via disclosure language) and strictly adhere to that purpose. For example, if consent is obtained for a one-time quiz, you are not permitted to send additional SMS messages beyond that scope. However, you can try targeting this group to encourage opt-in for general marketing messages separately.

For guidance on how to use subscribe keywords, see [how to add custom keywords](https://help.klaviyo.com/hc/en-us/articles/360050384091).

## Additional resources

- [How to get set up with SMS in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/4404274419355)
- [Understanding SMS consent collection](https://help.klaviyo.com/hc/en-us/articles/360035056972)
- [Basics: SMS compliance](https://help.klaviyo.com/hc/en-us/articles/7956171032091)
