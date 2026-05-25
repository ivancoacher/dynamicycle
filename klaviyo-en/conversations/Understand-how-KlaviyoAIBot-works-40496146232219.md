---
id: "40496146232219"
title: "Understand how KlaviyoAIBot works"
source_url: "https://help.klaviyo.com/hc/en-us/articles/40496146232219-Understand-how-KlaviyoAIBot-works"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-21T13:56:56Z"
language: "en"
---
Learn about KlaviyoAIBot, including:

- What it is and what it crawls
- How to identify authentic requests
- How crawling respects site rules and how to control it

This article is for anyone who sees traffic from KlaviyoAIBot and wants to confirm if it is legitimate or adjust how it is allowed to crawl.

## What is KlaviyoAIBot?

KlaviyoAIBot is Klaviyo’s web crawler for its Kai Customer Agent feature. KlaviyoAIBot fetches publicly available pages from domains and URLs that you have explicitly connected to your account. By indexing this content, Klaviyo can tailor AI experiences both on your website and within the Klaviyo platform. This is useful for content generation, AI answers, and product recommendations.

You can add sources beyond your primary storefront, including help centers (such as Zendesk), blogs, and news articles. KlaviyoAIBot does not bypass authentication, paywalls, or access controls.

## How it works

- ****Consent and scope****
  Klaviyo crawls the domains and URLs that you have explicitly connected to your account. For instance, it will crawl any public Shopify pages that are integrated with your Klaviyo account but won’t search Wikipedia for related content.
- ****Respect for site rules****
  KlaviyoAIBot only crawls the content you want crawled, following the Robots Exclusion Protocol (REP) as defined in .
- ****Politeness****.
  If your site signals rate limiting, Klaviyo reduces its rate automatically. Klaviyo respects standard HTTP responses like or 503 along with a header.
- ****Revisits****
  Klaviyo periodically recrawls to keep content fresh. Frequency varies based on change signals and your configuration.

## How to identify KlaviyoAIBot

KlaviyoAIBot uses 2 complementary signals.

If you see requests that claim to be KlaviyoAIBot that don't pass signature verification (or aren't marked as verified bots by Cloudflare), treat them as untrusted.

###

KlaviyoAIBot/1.0 (+https://help.klaviyo.com/hc/en-us/articles/<article\_id>)

### HTTP message signatures (web bot auth)

Every request is signed using [HTTP Message Signatures RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) and Cloudflare’s [Web Bot Auth](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/web-bot-auth/). You can use this to verify that the request genuinely came from KlaviyoAIBot without relying on IP allowlists.

****Tip****: If your site is behind Cloudflare, Cloudflare will verify Klaviyo’s signatures for you and flag traffic as a Verified Bot (cf.bot\_management.verified\_bot = true). You can safely allow it in WAF rules with that field.

****I see traffic that says it is KlaviyoAIBot. How do I know it is real?****
If you use Cloudflare, confirm the request is marked as a verified bot. If you do not use Cloudflare, verify that the request includes HTTP Message Signature headers that validate according to RFC 9421 and Web Bot Auth.

## What KlaviyoAIBot crawls

- ****Your ecommerce store****
  The ecommerce domain connected to Klaviyo.
- ****Additional sources****
  Any other source connected to your website, such as help centers (e.g., Zendesk), documentation portals, knowledge bases, blogs, and news articles when the customer has connected them.
- ****Public content****
  KlaviyoAIBot respects robots rules in robots.txt and does not attempt to access gated resources.

### How to control or limit crawling

- R****obots.txt****
  Add or update robots rules for the KlaviyoAIBot user-agent to allow or disallow sections. Find out more about [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt) and [REP](https://datatracker.ietf.org/doc/html/rfc9309).
- ****Temporary slowdowns****
  Return standard rate limiting responses, like [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) or 503 with [Retry-After](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After), to reduce rate without changing robots rules.
- ****Choose what’s connected****
  You can add or remove the domains and URLs you want connected at any time.

****Can I block a specific section of my site?****
Yes. Use robots rules for KlaviyoAIBot in robots.txt to disallow those paths. If you don’t know how, contact

****Does the bot obey temporary slowdown signals?****
Yes. Standard rate limiting responses like 429 or 503 together with Retry-After are honored.

## Data use and privacy

KlaviyoAIBot retrieves content to power AI features, such as for content generation, AI answers, and product recommendations. Crawled content is tied to your account and follows your settings.

Klaviyo periodically updates the indexed content to keep it current as long as the source page remains publicly available.

When a page becomes restricted via robots.txt or is removed from the source site, Klaviyo deletes the corresponding indexed content within a few days.

When you disconnect a source from your account, Klaviyo removes the associated content immediately.

****Do you publish IP ranges?****

No. Verification is based on cryptographic signatures and Cloudflare’s Verified bots program rather than static IP allowlists.