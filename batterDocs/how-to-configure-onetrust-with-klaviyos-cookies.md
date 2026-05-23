<h1>How to configure OneTrust with Klaviyo&#039;s cookies</h1>

## You Will Learn

Learn how to configure OneTrust cookie management tools (including their Auto-BlockingTM functionality and Cookie Pro product) tools to work with Klaviyo’s tracking and onsite functionality.

Klaviyo.js is Klaviyo's JavaScript snippet that enables Active on Site tracking and signup forms. You have the option to enable this tracking through your ecommerce integration or by pasting the code in your site's theme. Typically when Klaviyo’s JavaScript is enabled, the \_\_kla\_id cookie can track and identify site visitors. When not blocked, this cookie temporarily holds personally identifiable information, and once the visitor is identified (e.g., clicking a link through a Klaviyo-sent email), this cookied information is passed to Klaviyo. However, OneTrust requires additional setup steps to ensure this information is captured and then compliantly sent to Klaviyo.

In this article we will walk through the steps to ensure OneTrust is capturing visitor information appropriately and sending it to Klaviyo. Please note that you will need to complete all cookie setup steps in this guide and in the order outlined below.

## Prerequisites

We suggest visiting our [Guide to Klaviyo Web Tracking](https://help.klaviyo.com/hc/en-us/articles/115005076767) for more information on how our cookies capture known visitor information in different ways.

Additionally, it is important that you have already enabled Klaviyo.js, either directly through your [ecommerce integration](https://help.klaviyo.com/hc/en-us/categories/115000032731-Ecommerce-Integrations) or [manually](https://developers.klaviyo.com/en/docs/guide-to-integrating-a-platform-without-a-pre-built-klaviyo-integration#javascript-track-api-for-on-site-metrics).

## Configuring Klaviyo and OneTrust’s Tools

OneTrust’s tools will automatically block cookies unless visitors have already explicitly consented via OneTrust. These tools can block cookies but also cause Klaviyo forms to stop working altogether, even forms that do not require tracking.

In order to adhere to this compliance protocol and allow certain forms to function, Klaviyo needs to be configured with OneTrust in a way that does not track events without consent. Klaviyo’s tracking includes:

- if a visitor is active on site, the site referrer URL
- if a visitor views or adds to a product to their cart (if you’ve enabled this separately)

To make consent-based tracking compatible across OneTrust and Klaviyo, as well as some sign-up form functionality continue to work, you will need to follow the steps below inside OneTrust’s CookiePro tool.

## Add Your Website to CookiePro

If you haven’t already, you will need to add your website to your CookiePro account.

1. Log into your [CookiePro account](http://app.cookiepro.com/) and click the ****Cookie Compliance**** section under My Apps.

![View of the CookiePro dashboard with Cookie Compliance section highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28717390181531)

2. Click ****Add Website**** in the upper right-hand corner.

![The Add Website button in the upper right corner of the CookiePro dashboard page](https://klaviyo.zendesk.com/hc/article_attachments/28717390183579)

3. From here, you will see a section to set up and add your website and scanning details. Fill in your website URL and name of your organization in the first two fields.

![Scan Website modal with fields to fill website URL and Organization information](https://klaviyo.zendesk.com/hc/article_attachments/28717383884059)

Note that if you already have an organization associated with your CookiePro account, it will appear in the dropdown as an option.

4. Under the ****Advanced Options**** section, you can choose to adjust or add your scanning settings.

5. You can adjust the number of website pages that CookiePro will scan by changing the number in the **Limit scan** to field. By default, CookiePro will recommend scanning the first 1,000 pages.

![Inside Scanning Settings page, the ability to input scanned page numbers in field and toggle option on](https://klaviyo.zendesk.com/hc/article_attachments/28717390188315)

6. You can also limit the CookiePro scan to one area of your site. To do this, toggle on the option next to **Limit to this path****within site.** Make sure that your Website URL above reflects this URL path (e.g., retail.com/signups).

![Inside the Scanning Settings page, the toggle option to only scan pages within one area of your website](https://klaviyo.zendesk.com/hc/article_attachments/28717383946907)

7. Finally, if there are certain pages or types of pages that you want CookiePro to scan, you can add these in the next few fields. Add page IDs separated by commas to the **Scan Pages with Query****Parameters** field to scan pages by ID number.

You can also scan pages by URL by adding these URLs in the **Target Pages to Scan** field.

If you have a longer list of URLs or a sitemap, you can copy and paste those into the **Sitemap URLs** field. These URLs will be scanned first in the scan queue.

![In the Scanning Settings page, fields to add additional information on certain pages or areas of your website to scan ](https://klaviyo.zendesk.com/hc/article_attachments/28717383893403)

8. Once you have all settings completed, click ****Scan & Configure**** in the lower right corner.

## Configuring the Static-Tracking Cookie

In the section below we will walk through setting up your static-tracking cookie to ensure you are able to gather third-party cookies and pass these to Klaviyo.

1. Once your website has been added, navigate to ****Cookiepedia**** > ****Categorizations**** in the left hand navigation.

2. Look for the Klaviyo static-tracking \_\_kla\_id cookie either by searching for it in the field above or by scrolling through the list below. It should be the option labeled as “Persistent” with the **static-tracking.klaviyo.com** hostname.

3. Click the ****\_\_kla\_id**** cookie option.

![Inside the Categorizations page, a highlighted view of the __kla_id cookie in a list](https://klaviyo.zendesk.com/hc/article_attachments/28717390192411)

4. Once on the **Cookie Details** page, navigate to the ****Categorization**** tab.

5. If you have not run a scan with Klaviyo and OneTrust yet, make sure to choose ****Targeting Cookies**** from the **Select a category** dropdown. Make sure that **Third-Party Cookie** is already populated in the **Select a party** dropdown.

![On the Categorization tab, a modal showing dropdowns for selecting a cookie category and cookie party](https://klaviyo.zendesk.com/hc/article_attachments/28717390194715)

6. Once you have made these updates, click ****Save**** in the lower right corner.

7. In this same area, navigate to the ****Source**** tab. You should see your website URL appear in the list, as shown in the example below.

![Inside the Sources page, a view of your website URL displayed](https://klaviyo.zendesk.com/hc/article_attachments/28717383898267)

8. Click on your ****website URL****.

9. A dropdown will appear with a new URL; click on the pencil icon to the right.

![A highligted view of the pencil editing icon to the right of your website URL](https://klaviyo.zendesk.com/hc/article_attachments/28717383900315)

10. In the modal, remove your current URL and replace it with: **https://static-tracking.klaviyo.com**.

11. Click ****Confirm**** once you have updated the URL.

![A modal view of your Resource URL with a confirm butotn in the lower right](https://klaviyo.zendesk.com/hc/article_attachments/28717383943067)

12. To confirm that the Klaviyo cookie has been updated, navigate to ****Cookpedia********> Categorizations**** in the left-hand navigation. 1

3. Click on the ****Cookies**** tab.

14. From here, your \_\_kla\_id cookie should show a “1” listed under both the **Domain Category Overrides** and **Domains** columns.

![On the confirmation screen, a list view showing your __kla_id cookie with domain category overrides and domain as a numeric one](https://klaviyo.zendesk.com/hc/article_attachments/28717390203035)

## Configuring the Static.Klaviyo Cookie

In the section below, we will walk through setting up your static.Klaviyo cookie to ensure you are able to gather third-party cookies and pass these to Klaviyo.

1. Navigate to ****Cookiepedia > Categorizations**** in the left hand navigation.

2. Look for the static.Klaviyo \_\_kla\_id cookie either by searching for it in the field above or by scrolling through the list below. It should be the option labeled as “Persistent” with the **static.klaviyo.com** hostname.

3. Click this ****\_\_kla\_id**** cookie option.

![On the Categorizations page, the __kla_id cookie option highlighted in a list view](https://klaviyo.zendesk.com/hc/article_attachments/28717383910299)

4. Once on the **Cookie Details** page, navigate to the ****Categorization**** tab.

5. Choose ****Targeting Cookies**** from the **Select a Category** dropdown. Make sure that **Third-Party Cookie** is already populated in the **Select a party** dropdown.

![On the Categorization tab, a modal showing dropdowns for selecting a cookie category and cookie party](https://klaviyo.zendesk.com/hc/article_attachments/28717390194715)

6. Once you have made these updates, click ****Save**** in the lower right corner.

7. In this same area, navigate to the ****Source**** tab. You should see your website URL appear in the list below.

![A modal view of your website URL](https://klaviyo.zendesk.com/hc/article_attachments/28717383898267)

8. Click on your ****website URL****.

9. A dropdown will appear with a new URL; click on the pencil icon that appears to the right of this.

![A highligted view of the pencil editing icon to the right of your website URL](https://klaviyo.zendesk.com/hc/article_attachments/28717383900315)

10. In the modal remove your current URL and replace with: **https://static-tracking.klaviyo.com**[.](https://static-tracking.klaviyo.com.)

11. Click ****Confirm**** once you have updated the URL.

![A modal of your website URL with a confirm button in the lower right](https://klaviyo.zendesk.com/hc/article_attachments/28717383943067)

12. To confirm that the Klaviyo cookie has been updated, navigate to ****Cookiepedia > Categorizations**** in the left hand navigation.

13. From here, your \_\_kla\_id cookie should show a “1” listed under both the **Domain Category Overrides** and **Domains** columns.

![On the confirmation screen, a list view showing your __kla_id cookie with domain category overrides and domain as a numeric one](https://klaviyo.zendesk.com/hc/article_attachments/28717390203035)

## Configuring Your Website First-Party Cookie

In the section below we will walk through how to set up your websites or first-party cookies directly to capture the events on your ecommerce site.

1. Navigate to ****Cookiepedia > Categorizations**** in the left hand navigation.

2. Look for your website specific \_\_kla\_id cookie either by searching for it in the field above or by scrolling through the list below. It should be the option labeled as “Persistent” with your website URL as the hostname.

3. Click this ****\_\_kla\_id**** cookie option.

![On the Categorization page, your __kla_id cookie highlighted in a list view](https://klaviyo.zendesk.com/hc/article_attachments/28717383916315)

4. Once on the **Cookie Details** page, navigate to the ****Categorization**** tab.

5. Choose ****Targeting Cookies**** from the **Select a Category** dropdown. Make sure that **First-Party Cookie** is already populated in the **Select a party** dropdown.

![On the Categorization tab, a modal showing dropdowns for selecting a cookie category and cookie party](https://klaviyo.zendesk.com/hc/article_attachments/28717390209819)

6. Once you have made these updates, click ****Save**** in the lower right corner.

7. In this same area, navigate to the ****Source**** tab. You should see your website URL appear in the list below.

![A modal view of your website URL](https://klaviyo.zendesk.com/hc/article_attachments/28717383898267)

8. Click on your ****website URL****.

9. A dropdown will appear with a new URL; click on the pencil icon that appears to the right of this.

![A highligted view of the pencil editing icon to the right of your website URL](https://klaviyo.zendesk.com/hc/article_attachments/28717383900315)

10. In the modal remove your current URL and replace with: **https://static-tracking.klaviyo.com**.

11. Click ****Confirm**** once you have updated the URL.

![A modal showing your website URL with a Confirm button in the lower right corner](https://klaviyo.zendesk.com/hc/article_attachments/28717383943067)

## Previewing Your Updated Cookies

1. Navigate to ****Scripts**** in the left-hand navigation.

2. On the Scripts page, click on your ****website URL**** that appears below.

![On the Scripts page, your website URL will appear in the list below to click](https://klaviyo.zendesk.com/hc/article_attachments/28717383922971)

3. Then, click ****Publish Production**** in the upper right-hand corner.

![View of the Publish Production button to click in the upper right corner of the Scripts page](https://klaviyo.zendesk.com/hc/article_attachments/28717383924507)

4. In the right sidebar that appears, click ****Confirm****.

5. Once on the **Review** tab, scroll down and click ****Continue****.

6. Finally, on the **Confirm****and Publish** tab, click ****Publish Test & Preview****. Your preview may take a few seconds to load, but you will see a green check appear below once it’s ready.

![](https://fast.wistia.com/embed/medias/2b9o3tsibi/swatch)

7. Once this success message appears, click ****Confirm**** below.

## Publishing Your Updated Cookies

Before you publish your cookies, it’s important to note that production scripts can take up to four hours to take effect on your website. Once you follow the directions below, please wait up to four hours to see these updates.

1. Navigate to ****Websites**** in the left-hand navigation.

2. On the **Websites** page, click on your ****website URL**** from the list below.

![On the Websites page, your website URL will appear in the list below to click](https://klaviyo.zendesk.com/hc/article_attachments/28717390222491)

3. From here, click ****Publish**** in the upper right corner.

4. A sidebar modal will appear confirming your version to publish. Click ****Confirm**** in the lower right corner.

![A modal that will appear from the right sidebar to publish your website cookies with confirm button in lower right corner](https://klaviyo.zendesk.com/hc/article_attachments/28717390226715)

5. In this same modal, you will move onto the **Review and Publish** screen. Click the toggle on ****Enable Automatic Blocking of Cookies****.

You can read more about CookiePro’s Auto-Blocking feature in their [guide](https://community.cookiepro.com/s/article/UUID-5b03e81d-8b3b-5da8-eed5-b3b015730f3c?language=en_US).

![On the Review and Publish screen, a highlighted area to toggle on Automatic Blocking of Cookies](https://klaviyo.zendesk.com/hc/article_attachments/28717383934235)

6. Click ****Publish**** in the lower right corner.

7. A popup will appear with your Production Scripts. Click ****Copy Scripts****.

![A popup window showing your production scripts to copy and paste to your website](https://klaviyo.zendesk.com/hc/article_attachments/28717390232603)

8. Place these scripts within the html of your ecommerce website. Read more about placing these scripts into your ecommerce website in CookiePro’s step-by-step [guide](https://community.cookiepro.com/s/article/UUID-7478d3b4-18eb-3ac0-a6fd-fb7ebff9f8dc?language=en_US).

## Outcome

You have successfully set up your OneTrust cookie tracking software to ensure that your visitor information is captured and then compliantly sent to Klaviyo.
