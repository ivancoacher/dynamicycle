<h1>How to create a spin-to-win sign-up form</h1>

Learn how to add a spin-to-win wheel to boost sign-up form engagement and increase submit rates. Spin-to-win wheels are interactive, and encourage site visitors to subscribe for a chance to win a discount or reward.

Spin to win is a sweepstakes promotion. Check for compliance with local laws governing sweepstakes and prize promotions, including GDPR and marketing consent requirements before releasing a spin to win form on your website.

## About spin-to-win forms

General requirements:

- Each spin-to-win form must have only 1 wheel and at least one email or SMS consent field.
- The form must be set to display on ****All devices**** (in the **Display** settings).
- The form must include appropriate disclosure language for each type of consent collected (e.g., email, promotional SMS, and transactional SMS).
- If collecting both email and SMS consent, only one of these input fields can be marked as required. If collecting only one type of consent, that field can be required.

  Functionality details:
- The spin-to-win wheel cannot be placed:
  - Alone on the first step of a form. It needs at least 1 consent collection field, such as email or SMS, to be included on the first step.
  - On a step that has both email and SMS fields (these consents need to be collected on different form steps).
  - On the form’s success step.
- Forms that use a tap-to-text method for SMS consent cannot use spin-to-win wheels.

****How spin-to-win forms work****

Spin-to-win sign-up forms work as follows:

1. Add the spin-to-win block to your sign-up form.You can customize its appearance, the reward for each section (“slice”) of the wheel, and the probability of a shopper landing on each slice.
2. Klaviyo automatically creates a success step for each slice that you add to the wheel. You can then customize each success step and configure the appropriate coupon for each possible reward.
3. Determine your preferred sequence for spinning the wheel and collecting visitor information. For example:

   - Consent first:
     Ask for consent and any other personal information before the form page with the wheel. Visitors must complete this step(s) to access the wheel on the next page. This ensures visitors provide information before spinning.
   - Collect and spin:
     Place the information collection fields and the spin-to-win wheel on the same form step. Visitors fill out the fields and submit the form to spin the wheel. This combines information collection and the spinning action into one step.
4. After visitors complete the necessary steps, the wheel spins (if it hasn’t already) and reveals the winning slice. This will occur regardless of whether the visitor has confirmed their subscription for lists that use double opt-in.
5. The success step for the winning slice will automatically display on the form, and the new subscriber will receive their reward.

![Video showing a site visitor entering their email and then submitting it to spin the wheel on a spin to win form.](https://klaviyo.zendesk.com/hc/article_attachments/34639250736411)

## Add a spin-to-win wheel to a form

1. In Klaviyo’s left-hand navigation, select ****Sign-up forms****.
2. Open an existing form in the form editor, or click ****Create form**** to start a new one.
3. Select the ****Add blocks**** tab.
4. Drag and drop a ****Spin-to-win**** block into your form.
   ![The Add blocks tab open in the Klaviyo form editor showing the Spin-to-win block highlighted.](https://klaviyo.zendesk.com/hc/article_attachments/34614841525659)

   The spin-to-win wheel can not be placed on a step that includes both email and phone number fields. You must collect these on different steps, and the phone number field cannot be required.
5. In the **Wheel logic** menu along the left, customize each slice’s:

   - ****Label****
     - Determine the number of slices on the wheel and label each with a potential reward (e.g., 10% off, free shipping). By default, the wheel has 6 slices, but you can adjust it to have between 2 and 6.
   - ****Probability**** (e.g., 20%).
     - Assign the likelihood of each slice being selected. The probability for each slice must be equal to or greater than 1%, meaning you cannot guarantee one outcome, and all slices must add up to 100%. Note that decimals are not permitted.![The Spin-to-win menu in the form editor showing example form's wheel logic settings, including example wheel slice label names and probability percentages for each.](https://klaviyo.zendesk.com/hc/article_attachments/34614856460315)

   As a best practice, ensure that every slice has an attainable prize associated with it, so that all participants win something and avoid encountering a “try again” or similar message.
6. Optional: select ****Duplicate all slices on the wheel**** to display slices twice, diagonally from one another.

   - Note that duplicating does not change slice probability.
7. Use the **Wheel style** and **Slice style** sections to customize the design to fit your brand (e.g., sizing, coloring, and label text).
8. Select ****Success**** from the menu bar. Klaviyo automatically creates a success step for each slice on your spin-to-win wheel.
   ![The Success step selected in the menu bar of the form editor and showing the success steps corresponding to each slice of the spin-to-win wheel in the form.](https://klaviyo.zendesk.com/hc/article_attachments/34614856462619)
9. Ensure that you customize and add the appropriate coupon on each success step (e.g., configure a 10% off coupon on the 10% off success step). For assistance creating coupons, head to our [Guide on adding coupon blocks in forms](https://help.klaviyo.com/hc/en-us/articles/6038674938523#h_01HA28D5B0W8N9E9B1AQSSCB2N).

   For SMS-only consent forms, only static coupons are permitted.
10. Use the **Styles** and **Targeting & behaviors** tabs to refine the rest of your form’s design and behavior.
11. Once you’re satisfied with the form’s configuration and design, click ****Publish****.

### Coupon management for spin-to-win forms

When creating sign-up forms and offering coupons on your website, note that our system caches coupon codes to prevent users from obtaining multiple unique codes for the same dynamic coupon. For example, if a regular form (non-spin-to-win) issues a dynamic coupon (type A) to a subscriber, that code is stored. If the same user later plays the spin-to-win game and encounters the same type of coupon (type A), they will receive the same stored code. This system ensures fair and secure distribution of coupons by preventing multiple unique codes for the same offer.

To avoid confusion, it's helpful to document this behavior in your help resources to inform users they may receive the same code in different interactions, ensuring clarity for both your team and customers.

## Sending out Flows based on spin-to-win outcome

You are able to send out dynamic flows based on the spin to win outcome by creating a segment based on the **"$success\_step\_name"** event property, nested under the "**Form completed by profile"** event. This is captured when a shopper completes the spin to win form.

![The success_step_name field is highlighted in the profile properties menu, nested under the Form completed by profile event](https://klaviyo.zendesk.com/hc/article_attachments/41006951150107)

The **"$success\_step\_name"** event property value is determined by the slice label name which is set when configuring the spin to win wheel.

![Klaviyo segment builder showing a rule for profiles who won “10% Off” in the last 30 days.](https://klaviyo.zendesk.com/hc/article_attachments/41006943289883)

![Klaviyo Spin-to-win setup with only “10% Off” at 100% probability; all other slices set to 0%.](https://klaviyo.zendesk.com/hc/article_attachments/41006943292059)

By creating a segment for each of your spin to win outcomes, you are able send out [segment-triggered flows](https://help.klaviyo.com/hc/en-us/articles/360003040052) automatically as each shopper receives their winning outcome.

## Next steps

After publishing your form, visit your website in an incognito browser to test its appearance and functionality. Fill out the form to make sure the success steps display correctly.

Tip: If you want to test the impact of the spin-to-win gamification element, you could [A/B test the spin-to-win form versus a standard consent collecting form](https://help.klaviyo.com/hc/en-us/articles/360045462071#h_01JBHKG8SGYSGHA4MXTXV1A3PF).
