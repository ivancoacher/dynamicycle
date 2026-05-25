---
id: "50223237602715"
title: "Use the Social Content Library"
source_url: "https://help.klaviyo.com/hc/en-us/articles/50223237602715-Use-the-Social-Content-Library"
section: "Social Events & Content"
category: "Social Marketing"
category_slug: "content"
klaviyo_updated: "2026-05-11T15:18:45Z"
language: "en"
---
****Premium feature.**** Available on the paid Klaviyo Social Marketing plan with Facebook Login.

The Social Content Library surfaces every Instagram Post, Story, and Reel where your brand is tagged. Unlike Engagement events, which capture the action and require a matching Klaviyo profile, the Social Content Library shows you all tagged content from any creator with a public Instagram account, organized for your review and analysis.

This article covers what's in the Social content library, how to navigate it, and how access works across authentication types.

## Plan and access

Every Klaviyo account can see the ****Social content**** tab in the left navigation, but the experience depends on your plan and how Instagram is connected.

- ****Paid Social Marketing plan with Facebook Login authentication method.**** Full access. The library populates with all tagged content and engagement metrics.
- ****Paid Social Marketing plan with Instagram Login authentication method.**** The Social content tab is visible but content does not flow in. Re-authenticate with Facebook Login to populate the library. See [Connect Instagram to Klaviyo](https://claude.ai/local_sessions/local_80abb3ff-dbd6-41d8-8476-669d3c3be7eb#).
- ****Free Auto-replies plan with either authentication method.**** The Social content tab is visible and shows a splash page describing the feature. Upgrade to the paid Social Marketing plan to unlock access.

To use the Social content library at full capability you need both the paid plan and a Facebook Login connection.

## Open the Social Content Library

In Klaviyo, open ****Social**** in the left navigation and select ****Social content****. If your Instagram account is connected with Facebook Login and you're on the paid plan, you'll see your tagged User-generated-content (UGC) in a grid. Klaviyo back-populates up to 200 previously tagged Posts and Reels.

If you haven't connected Instagram yet, you'll see a splash screen prompting you to do so.

## Top-level metrics

Above the content grid you'll see a row of metrics that summarize tagged activity for your selected date range.

- ****Unique creators.**** Distinct Instagram accounts that have tagged your brand.
- ****Total posts.**** All tagged posts, stories, and videos.
- ****Engagement rate.**** Average engagement across all tagged content. Calculated per post as (likes + comments) divided by the creator's follower count at the time of the mention, then averaged across posts.
- ****Likes & comments.**** Total likes and total comments across all tagged content.
- ****Potential reach.**** Sum of follower counts across unique creators.

The metrics update when you change the filters.

![A social media dashboard displaying posts of a small brown dog, with an Instagram story pop-up showing a close-up of the dog.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/84512cd43c9354a461bccf650411b2b2e93c8114-3024x1656.png)

## Browse, filter, and sort

The grid shows each tagged post as a tile with the creator's handle, the media, and basic engagement counts. Switch between ****grid**** and ****list**** views using the toggle on the right. List view exposes more quantitative detail; grid view emphasizes the content itself.

****Filters****

- ****Date range.**** Updates both the grid and the top-level metrics.
- ****Media type.**** Filter by Post, Story, or Video.
- ****Bookmarked.**** Show only content you've bookmarked.
- ****Creator name.**** Filter to a single creator.
- ****Show expired.**** Include or exclude expired stories.

  ****Search****

  Search by creator handle or by keywords in captions.

  ****Sort****
- Most recent
- Most liked
- Most commented
- Highest engagement rate

## Open the detail view

Click a tile to open the detail panel for that post. The detail panel shows:

- The full media, including caption
- The creator's handle and follower count at the time of the mention.
- Engagement metrics: engagement rate, likes, comments
- Posted date and last sync time
- A link to open the post directly in Instagram.

Stories and videos auto-play on hover in the grid. You can pause and resume manually.

## Bookmark content

Bookmark media items to come back to them later.

- ****Bookmark a post.**** Click the bookmark icon on the tile. Bookmarked posts can be filtered using the Bookmarked filter.

## Stories behavior

While a story is active, it appears in the library normally. Once a story expires (24 hours after posting), Klaviyo is no longer able to show the media but the history of the Story being published persists.

Use the ****Show expired**** filter to include or exclude expired stories from the view.

## How content stays current

Klaviyo refreshes the Social Content Library automatically.

- ****Mentions**** (when a creator tags your brand using the @ sign in their caption or in their Story) come in via a Meta webhook in real time.
- ****Tagged content**** (when a creator tags your brand in the Post or Reel content itself) come in via the Meta Tag API. It can take up to 30 minutes for new tagged content to display.
- ****Engagement metrics**** (likes, comments) refresh on a recurring schedule that varies based on how recently the content was published and how many other pieces of content you’ve been tagged in recently.

Each tile shows a "Last updated" timestamp.

## Connecting one Instagram to multiple Klaviyo accounts

If your Instagram is connected to multiple Klaviyo workspaces (a 1:Many setup), the Social Content Library behaves slightly differently on first entry:

1. The first time you open the library in a new workspace, Klaviyo shows a confirmation message explaining that this Instagram is connected to other workspaces and that UGC may also appear there.
2. Once you confirm, the library populates as normal.

Tagged content is visible across all connected workspaces. Bookmarks and other in-workspace actions are scoped to each workspace independently.

## Things to know

- The Social Content Library requires Facebook Login. Tagged content does not flow in on Instagram Login connections.
- User-generated content (UGC) cannot be downloaded or exported from Klaviyo today.