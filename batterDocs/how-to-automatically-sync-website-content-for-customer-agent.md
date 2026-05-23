<h1>How to automatically sync website content for Customer Agent</h1>

## You will learn

You will learn how to enable automatic reindexing (auto-sync) for your Customer Agent's connected websites. By automating this process, you ensure your Agent always answers questions using the latest information on your website about your products and policies, reducing the manual effort of refreshing your knowledge base and deflecting support tickets caused by outdated answers.

## Before you begin

- ****Prerequisites:**** You must have the ****Customer Agent**** feature enabled and at least one website source added to your Agent Content.
- ****Availability:**** This feature is available only to ****paying Customer Agent subscribers****. It is not available on trial or free plans.
- ****Roles:**** You must have ****Owner****, ****Admin****, or ****Manager**** permissions to manage Agent content.
- ****Time to complete:**** ~2 minutes.
- ****Important:**** Automatic syncing occurs on a periodic schedule (approximately daily). For immediate updates (e.g., a flash sale launching in 10 minutes), you should still perform a manual reindex.

## Overview

Customer Agent uses content you upload to answer customer inquiries accurately. Previously, if you added new products or changed your return policy, you had to manually trigger a "reindex" for the Agent to learn that information.

With ****automatic syncing****, Klaviyo periodically crawls your connected websites to detect changes. If new pages are found or existing content is updated, the Agent automatically ingests these changes. This "set and forget" capability is ideal for high-velocity stores that frequently add new inventory.

## Set it up

1. From the main navigation, select ****Service > Customer Agent****.
2. Click the ****Content**** tab.
3. Locate the ****Websites**** content types in the table.
4. Find the specific URL you want to keep updated (e.g., your storefront or FAQ page).
5. Check the ****Auto-sync**** setting to ****On****.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/45985082500251)
6. ****Expected result:**** The system will now queue this site for periodic crawling. A status indicator may appear showing that auto-sync is active.

****Tip:**** By default, your main storefront URL is likely already toggled ****On****. Review your settings to ensure all desired sub-pages are also enabled.

## Best practices

- ****Enable for high-traffic pages:**** Always turn on auto-sync for your primary storefront and "New Arrivals" pages to capture inventory changes.
- ****Monitor the "Last Updated" date:**** Use the ****Last updated**** column in your content table to verify when the crawler last refreshed your data.
- ****Combine with manual indexing:**** Auto-sync runs periodically. If you make a critical update to your shipping policy right before Black Friday, trigger a ****Manual Reindex**** for immediate effect.
- ****Exclude static archives:**** If you have archived blog pages that never change, you can leave auto-sync ****Off**** to prioritize crawling bandwidth for your active pages.

## Measure success

- ****Key metrics to watch:****
  - ****Last updated timestamp:**** Ensure this is recent (within the last 3-4 days).
  - ****Resolution rate:**** Monitor if the Agent is successfully answering questions about new products.
- ****If the Agent provides outdated answers:****

1. Check the ****Last updated**** column for the source URL.
2. If the date is older than your recent site change, click the ****Refresh**** button manually.

## Troubleshooting

****Symptom:**** The Agent doesn't know about a product I added this morning. ****Likely cause:**** The automatic sync schedule (approx. daily) hasn't run yet. ****Fix:**** Manually click ****Refresh**** next to the website URL for an immediate update.

****Symptom:**** I cannot toggle "Auto-sync" on (the toggle is grayed out). ****Likely cause:**** You are on a Trial plan. ****Fix:**** Upgrade to a paid Customer Agent subscription to unlock automatic reindexing.

****Symptom:**** The "Last updated" date changed, but the content didn't update. ****Likely cause:**** The crawler detected that the content on the page was identical to the previous version and skipped re-embedding to save processing time. ****Fix:**** Verify you published your changes on your website, then wait for the next cycle or reindex manually.

## FAQ

****Q:**** Does auto-sync crawl my entire website every time? ****A:**** No. The system uses your sitemap and "last crawled" data to identify only the pages that have changed or are new. This ensures efficient processing.

****Q:**** Can I turn auto-sync off for specific pages? ****A:**** Yes. The toggle is available on a per-website/per-page basis in your Content table.

****Q:**** Does this feature work for uploaded PDF files? ****A:**** No. Automatic reindexing currently applies only to ****Websites**** (`ENTIRE_SITE` and `SINGLE_PAGE`). Files and text snippets must be updated manually.

## Compliance & data handling

When you enable auto-sync, you authorize Klaviyo to periodically crawl the public-facing content of the provided URLs. Ensure your website's `robots.txt` file does not block Klaviyo's crawler, as this will prevent updates. ****This information is not legal advice. Consult your legal counsel for guidance on applicable laws.****

## Next steps

- ****Review non-website content:**** Check if your uploaded PDFs or text snippets need manual refreshing.
- ****Monitor conversations:**** Watch your ****Conversation Logs**** to see how the Agent handles questions about your newest products.
