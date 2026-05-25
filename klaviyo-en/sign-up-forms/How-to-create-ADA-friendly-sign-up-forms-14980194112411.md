---
id: "14980194112411"
title: "How to create ADA-friendly sign-up forms"
source_url: "https://help.klaviyo.com/hc/en-us/articles/14980194112411-How-to-create-ADA-friendly-sign-up-forms"
section: "Form best practices"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:28Z"
language: "en"
---
## You will learn

Learn how to use the accessibility assistant feature in the **Form Alerts** tab of the sign-up forms editor to avoid some of the most common web content accessibility guidelines (WCAG) compliance issues. Companies striving to make their websites ADA-friendly should reference and follow WCAG standards. The accessibility assistant guides you in creating sign-up forms that are accessible for all of your site visitors.

The WCAG standards aim to make web content more accessible to everyone, including people with disabilities. Website accessibility is a legal requirement in many countries, and implementing WCAG standards can help satisfy many of these accessibility needs. Please note that while the accessibility assistant is intended to help identify accessibility issues under the WCAG 2.0 AA standards as they apply to sign-up forms, it may not be able to identify every accessibility requirement due to known limitations of existing technology or other factors independent of technology. Use of the accessibility assistant can help with web accessibility requirements, but does not guarantee compliance with applicable laws. To confirm legal implications and requirements of web accessibility, it is recommended to seek the advice of a qualified lawyer.

## Before you begin

Below is a list of issues that the accessibility assistant will check for. Please note that the error types listed below are how Klaviyo's accessibility assistant identifies them, not specific input field names in the form builder. If an error is detected, an alert with a description and fix prompt will appear in the **Form alerts** tab.

|  |  |
| --- | --- |
| ****Error type**** | ****Description**** |
| Button-name | Ensures buttons have discernible text. |
| Image-alt | Ensures image elements have alternate text (alt text) or a html role of “none” or presentation. |
| Color-contrast | Ensures the contrast between foreground and background colors meets WCAG 2 AA contrast ratio thresholds. |
| Link-in-text-block | Ensure links are distinguishable from surrounding text in a way that does not rely on color. |
| Link-name | Ensures links have discernible text. |
| Label | Ensures every form element has a label. |

## Create a ADA-friendly sign-up form

Whether you’re building your first sign-up form or updating a form, the accessibility assistant helps you identify and fix accessibility issues.

To create a form in-line with the WCAG standards listed above:

1. Create a new sign-up form or open up the form editor for one of your existing sign-up forms.
2. Use the editor to [add content blocks](https://klaviyo.zendesk.com/hc/en-us/articles/4413550187035) and [style the form](https://klaviyo.zendesk.com/hc/en-us/articles/4413537049883) to fit your brand.

   The accessibility assistant will monitor for form elements that do not meet WCAG standards as you build your form and log them as **Active alerts**. An existing form will log all issues in the **Active alerts** section.
3. Click on the ****Form alerts**** in the bottom left to see the identified accessibility issues.

   Under **Active alerts,** you’ll see various cards describing the elements that don't meet WCAG standards that the accessibility assistant identified in your form, in addition to other content or design issues identified. Each card will include a description of the issue and a prompt to either fix or dismiss it. For example, if you add an image to your sign-up form, the accessibility assistant will alert you to add alt text to the image. Alt text provides a description of the image so that shoppers browsing your site with a screen reader can access the digital content.

   ![The Form Alerts tab highlighted in the lower left corner of the sign-up form editor and showing 2 active alerts.](https://klaviyo.zendesk.com/hc/article_attachments/28717384388123)
   ![The Form Alerts tab open and displaying 3 identified accessibility issues found in a sign-up form.](https://klaviyo.zendesk.com/hc/article_attachments/28717384404123)
4. To fix an issue, follow the suggestions on the card and either resolve or add the missing elements. Once you are satisfied with your changes, click ****Fix******.**
   ![An example accessibility issue in the Form alerts tab that has a prompt to Edit block in order to resolve the issue.](https://klaviyo.zendesk.com/hc/article_attachments/28717384405531)

   Some issues will prompt you to fix them in the respective block’s settings (i.e., a button block) or the styles section, rather than directly in the **Form alerts** tab. To resolve these issues, take note of the problem description on the alert card, then click ****Edit block**** (or ****Edit Styles****) to make the suggested changes. Navigate back to the ****Form alerts**** tab once you fix the issue.
5. If you wish to ignore one or more of the accessibility suggestions, click ****Dismiss****. Dismissing an issue will prompt a modal to appear, asking you to cancel or confirm your choice.

   Once you successfully fix or dismiss all identified issues, you will see a “No active alerts” message shown in the **Form alerts** tab.
   ![The Dismiss alert modal that populates when you dismiss an accessibility issue in the Gorm alerts tab.](https://klaviyo.zendesk.com/hc/article_attachments/28717390684827)
   ![The toggle in the Form alerts tab that allows you to switch between Active alerts and Dismissed alerts.](https://klaviyo.zendesk.com/hc/article_attachments/28717390691227)

   You can return to ignored issues at a later time by opening the assistant and viewing your previously dismissed alerts. It is recommended you fix all issues highlighted in the accessibility assistant. Non-compliance with WCAG standards may expose your company to legal risk.
6. Click ****Publish**** to set your sign-up form live on your site with your accessibility updates.

Note that when you click publish, you'll be prompted to fix any active form alerts. You can choose to resolve the errors in the **Form alerts** tab or publish anyways.

## JAWS accessibility reports

Please note that JAWS, a computer screen reader program for Microsoft Windows, may not be detecting sign-up forms on your website that were created in Klaviyo. To ensure that site visitors using JAWS can still interact with sign-up forms on your website, we suggest adding an extra snippet of code to your site that makes it more accessible to JAWS.

Copy the following code snippet and paste it into your site’s main theme file so that JAWS will detect and read your Klaviyo sign-up forms:

```
  const isAriaHiddenTrue = ($el) => {
    const ariaHiddenValue = $el ? $el.getAttribute("aria-hidden") : null;
    return ariaHiddenValue === "true";
  };

  const isHTMLElement = (node) => {
    return node.nodeType === Node.ELEMENT_NODE;
  };

  const isModal = (node) => {
    if (node.children.length !== 1) return false;
    const modalContainer = Array.from(node.children[0].classList).some((cls) =>
      cls.startsWith("kl-private-reset")
    );

    return modalContainer;
  };

  const getTopLevelDomElements = () => {
    const body = document.body;

    // Use the children property to get all top-level elements
    const topLevelNodes = Array.from(body.children).filter((node) => {
      if (isHTMLElement(node)) {
        const tagName = node.tagName.toLowerCase();

        console.log("isModal: ", isModal);

        // Filter out specific tags
        return (
          tagName !== "script" &&
          tagName !== "link" &&
          tagName !== "iframe" &&
          tagName !== "style" &&
          !isModal(node)
        );
      }
      return false;
    });

    return topLevelNodes;
  };

  const a11yHideTopLevelElements = () => {
    const $elements = getTopLevelDomElements();

    $elements.forEach(($el) => {
      if (!isAriaHiddenTrue($el)) {
        $el.setAttribute("kl-aria-hidden", "true");
        $el.setAttribute("aria-hidden", "true");
      }
    });
  };

  const a11yShowTopLevelElements = () => {
    const $elements = getTopLevelDomElements();

    $elements.forEach(($el) => {
      if ($el.hasAttribute("kl-aria-hidden")) {
        $el.removeAttribute("kl-aria-hidden");
        $el.removeAttribute("aria-hidden");
      }
    });
  };
```

## Next steps

It is important to maintain WCAG standards across all of your Klaviyo sign-up forms. Previously published sign-up forms may still contain accessibility issues for you to fix, but note that Klaviyo will not automatically fix any WCAG non-compliant issues.

Navigate to the **Form alerts** tab within the editor for each of your existing forms to resolve any accessibility issues to help with WCAG-compliance on your website.