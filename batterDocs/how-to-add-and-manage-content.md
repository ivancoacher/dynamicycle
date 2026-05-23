<h1>How to add and manage content</h1>

## You will learn

What content is in Customer Agent, why most of your knowledge base is already loaded, how to add more, and how to write content Customer Agent can actually use to answer shopper questions.

## Before you begin

You’ll need:

- An ****Owner****, ****Admin****, or ****Manager**** role

## You already have content

Customer Agent automatically scrapes your storefront on setup using the KlaviyoAIBot crawler. Most brands have hundreds of pages indexed — product pages, help articles, policy pages, FAQ — before they ever add anything manually.

Before you start adding more, ****review what’s already there.**** Open the Content tab and browse what Customer Agent has indexed. If you see gaps, add the missing sources. If you see outdated content, refresh or remove it.

For ongoing automatic indexing of your site, see **How to auto-sync website content**.

## Content vs. skills

It’s easy to confuse these two when you’re setting up Customer Agent:

- ****Content**** is what Customer Agent knows — facts, policies, product details. Static information you can write down.
- ****Skills**** are what Customer Agent does — handling specific types of requests, often involving tools or multi-step workflows.

A good test: if the answer is the same for every customer and you can write it as a fact, it belongs in content. If Customer Agent needs to do something — look up data, take an action, run a multi-step process — that’s a skill.

For example, your return policy is content. Actually starting a return for a shopper is the Returns & exchanges skill.

## Adding more content

Three ways to add to Customer Agent’s knowledge base:

### Upload a document

Use this for policies, FAQs, training materials — anything you have as a file but don’t have on your website.

1. Navigate to ****Customer Agent > Content****.
2. Click ****Add source > Upload file****.
3. Select the file (PDF, .docx, .txt, etc.).
4. Confirm and save.

### Add a webpage

Use this for URLs you want Customer Agent to index — a specific landing page, a help article, your help center, or your full storefront.

1. Navigate to ****Customer Agent > Content****.
2. Click ****Add source > Add webpage****.
3. Paste the URL.
4. Choose any of these options:

   - ****Set as my storefront URL**** — Connect this URL as your storefront. Customer Agent uses the storefront connection to pull richer ecommerce data alongside the page content.
   - ****Turn on auto syncing**** — Automatically re-sync the page when changes are detected. Leave off if you want a one-time import.
   - ****Which pages should the AI agent import?****
     - ****Import all pages from this URL**** — Pulls in this page and every child page underneath it. Use this for help centers, blogs, or section roots.
     - ****Import only this page**** — Just this one page. Use this for one-off URLs.
5. Click ****Save****.

### Add a snippet

Use this for short pieces of information that don’t justify a full document — a single FAQ answer, a quick policy clarification, a product spec.

1. Navigate to ****Customer Agent > Content****.
2. Click ****Add source > Add snippet****.
3. Write a clear question and a clear answer. Save.

For automatic, ongoing scraping of your full website, set up auto-sync — see **How to auto-sync website content**.

## Writing content Customer Agent can use well

Not every well-written page is good for Customer Agent. A few principles:

- ****Use clear, plain language.**** Avoid jargon and marketing copy. Customer Agent uses your wording, so anything you wouldn’t want a shopper to read shouldn’t be in your content.
- ****Use H1/H2/H3 structure.**** Headings help Customer Agent find the right passage to answer a specific question.
- ****Be factual, not promotional.**** Tone goes in Guidance, not in content. Content should answer questions, not sell.
- ****Restate the question in the answer.**** “Our return window is 30 days from delivery” beats “30 days.” The full sentence is easier to retrieve and read.
- ****Use bullet lists for processes.**** Step-by-step instructions are easier for Customer Agent to format into a clear response.
- ****Don’t bury the answer in walls of text.**** Lead with the answer; add detail after.
- ****Remove conflicts.**** If two pages contradict each other, Customer Agent can’t pick the right one. Audit and consolidate.
- ****Keep documents focused.**** A single, focused page on one topic beats a 20-page mega-doc covering everything.
- ****Image and video content needs text.**** Customer Agent can’t read images or transcribe video. Make sure key information is in text form.

### Examples

****Good — shipping policy:****

### Shipping eligibility

> We ship to all 50 US states. We do not ship to PO Boxes, APO/FPO addresses, or international destinations.

### Shipping costs

> Standard shipping is free on orders over $50. Orders under $50 are charged $7 flat-rate shipping.

****Good — return requirements:****

### What can be returned

> Items can be returned within 30 days of delivery if they are unused, in original packaging, and accompanied by the original receipt.

### What cannot be returned

> Final-sale items, customized products, and gift cards are not eligible for return.

Both examples use clear headings, short factual sentences, and explicit positive and negative information.

## Managing content

From the Content tab you can:

- ****Edit**** content directly — Customer Agent picks up the changes after a re-index.
- ****Delete**** content that’s outdated or no longer relevant.
- ****Re-sync**** a webpage to refresh it from the source.
- ****Inspect what got ingested**** — open a source to see exactly how Customer Agent has stored it.

For each source, the three-dot menu gives you these options.

## Troubleshooting

****Symptom:**** Customer Agent isn’t using a document I added.
****Likely cause:**** Document is too long, doesn’t have clear headings, or restates the same content as a higher-quality source.
****Fix:**** Break the document into smaller focused pages. Add clear headings. Test in the playground with the question the document should answer.

****Symptom:**** Auto-sync missed a page.
****Likely cause:**** The page is gated, behind a login, or not linked from your site’s main navigation.
****Fix:**** Add the page manually as a webpage source.

****Symptom:**** Customer Agent is using outdated content.
****Likely cause:**** Source hasn’t been re-synced since you updated it.
****Fix:**** Open the source, click the three-dot menu, and choose ****Re-sync****. Confirm in the playground that the new content is being used.

## FAQ

****What file types can I upload?****
PDF, DOCX, TXT, and Markdown. Customer Agent extracts text only — formatting and images are not preserved.

****How often does auto-sync run?****
Auto-sync runs on a regular cadence. See **How to auto-sync website content** for details.

****What about gated or login-protected pages?****
Auto-sync can’t access pages behind a login. Add those manually as documents or snippets.

## Next steps

- ****Set up auto-sync**** for ongoing site coverage
- ****Test in the playground**** to see how Customer Agent uses your content
- ****Configure Guidance**** to control how Customer Agent communicates this content
