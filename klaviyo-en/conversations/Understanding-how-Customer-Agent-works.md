---
id: 37659296009883
title: "Understanding how Customer Agent works"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/37659296009883-Understanding-how-Customer-Agent-works"
section: "Customer Agent"
category: "Conversations"
category_slug: "conversations"
klaviyo_updated: "2026-04-21T13:54:54Z"
language: en
---

Learn how Klaviyo's Customer Agent understands and answers shopper questions, including what information it uses and the types of questions it can help with.

## How does Customer Agent gather information?

Klaviyo’s Customer Agent synthesizes information from the following sources to deliver accurate, contextually relevant answers in real time:

- ****Your website****
  - When you enable Customer Agent, Klaviyo automatically syncs with the information in your website. Customer Agent then accesses your site’s public pages to its initial knowledge base foundation to answer questions. Klaviyo will sync a maximum of 10,000 pages from your site.
  - In the **Knowledge** tab in Klaviyo, you can see the URL and the number of pages ingested. You can also re-ingest at any time if you make major updates to your site.
    ![Knowledge tab showing a single live webpage data source for the AI Service Agent.](https://klaviyo.zendesk.com/hc/article_attachments/38190369091611)
- ****Additional knowledge sources****
  - You can optionally add more information or documentation on [the](https://www.klaviyo.com/kagent/knowledge) [**Knowledge**](https://www.klaviyo.com/kagent/knowledge) [tab in Klaviyo](https://www.klaviyo.com/kagent/knowledge) to supplement what Customer Agent knows from your site. Customer Agent immediately trains itself on any new knowledge you add.
- ****Additional profile-level context****
  - Web chat: When a shopper starts a conversation with Customer Agent, it can detect what page the shopper is currently viewing and scrape its contents. This helps Customer Agent contextualize specific shopper questions, so it can provide precise answers related to the product or topic displayed. For example, if a visitor asks "will it fit my laptop?", Customer Agent can identify that they're viewing a laptop case.
  - SMS: When a shopper starts a conversation with Customer Agent, it can detect messages exchanged between the brand and the shopper over the last 48 hours. This helps Customer Agent contextualize the shopper's question. For example, if a shopper received an abandoned cart flow SMS that read "You left the compression leggings behind! Any question, reply here" and then replied "are they machine-washable?", Customer Agent can identify that they are asking about the compression leggings.

Customer Agent is optimized to use these sources efficiently and find the most accurate answer it can based on the question asked.

## How does Customer Agent answer questions?

Customer Agent follows 4 main steps to generate a response:

- ****Query****
  - Customer Agent receives the shopper’s question through the chat interface on your site.
- ****Contextualization****
  - It analyzes the question to determine intent (e.g., product detail or recommendation, order status, general inquiry, etc.). It also considers:
    - Web chat: The current webpage the shopper is viewing.
    - SMS: message exchanged over the last 48 hours before the conversation started
    - Previous messages in the conversation for added context.
- ****Routing****
  - Based on the contextualized query, Customer Agent decides where to route the question to ensure it's handled best. This can be:
  - ****Retrieval for Service****
    - Customer Agent locates the best information to address a shopper's question or directs the query to the appropriate process for handling it. For example:
      - For general questions, it relies on your site content and any knowledge you’ve uploaded.
      - For product-related questions, it either extracts information from the current webpage or suggests related or complimentary items using your product catalog.
      - For order tracking questions, it prompts follow-up questions or authentication if needed and retrieves order details from Shopify.
  - ****Recommendations****
    - Customer Agent will route the conversation to its specialized recommendation skill to return products that match the user's specific query.
  - ****Tracking****
    - Customer Agent will review the user's orders within the last 90 days and retrieve tracking information for the specific order. If there are multiple orders, Customer Agent will automatically clarify with the user which order they're referring to.
- ****Generation****
  - It composes a clear and helpful response using the gathered information.
  - SMS: it tries to limit responses to ~320 characters if possible

If Customer Agent cannot find a suitable answer, it follows your [handoff settings](https://help.klaviyo.com/hc/en-us/articles/37659474656027) to escalate the conversation.

## What kind of questions can Customer Agent answer?

Customer Agent can assist with a wide range of shopper questions, including:

- ****Brand-related****:
  - Answers questions about shipping, returns, FAQ pages, or any information available on your site or in added resources.
- ****Product details****:
  - Provides information on product features, availability, sizing, and other specifics (e.g., What are the dimensions?).
- ****Product recommendations****:
  - Suggests complimentary items, alternatives, and makes comparisons with similar products (e.g., “What goes well with this?” or “Do you have something similar?”).
- ****Order status****:
  - Updates on order status, tracking, or order details (e.g., “Where is my order?”).
- ****Follow-ups:****
  - Understands references to earlier parts of the conversation for continuity and context (e.g., “Does it come in blue” after asking about a specific jacket).
- ****Small talk****:
  - Responds to friendly, conversational exchanges. Note that Customer Agent can handle a few instances of small talk; however, it won’t continually engage in random conversation.

Response accuracy depends on accessible information on your website and from added knowledge sources. You should [test your Customer Agent regularly](https://help.klaviyo.com/hc/en-us/articles/37659457059739) and keep your knowledge sources up to date to ensure the best answers for your shoppers.

## How does Customer Agent keep data secure?

Customer Agent only has access to information that you expressly provide, either directly in Klaviyo or through your publicly available website content; it does not reference external sources on the internet. Your data and conversations are never used to train large language models (LLMs), such as public models like OpenAI.

All customer data handled by Customer Agent is encrypted during transmission, and common types of personally identifiable information (PII) shared in conversations are automatically removed before being sent to an LLM.

## Additional resources

- [How to enable Customer Agent](https://help.klaviyo.com/hc/en-us/articles/37659268052635)
- [How to test and train your Customer Agent](https://help.klaviyo.com/hc/en-us/articles/37659457059739)
- [How to optimize your content for Customer Agent](https://help.klaviyo.com/hc/en-us/articles/40418535535387)