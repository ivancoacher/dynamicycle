<h1>Guide to using customer agent on SMS</h1>

## Introduction

****What is Customer Agent on SMS?****

- A 24/7 AI assistant that responds to inbound SMS messages to answer questions, recommend products, and resolve common issues
- Supports revenue-driving and service use cases (product recommendations, WISMO, FAQs)

  ****Why use Customer Agent on SMS?****
- Drive incremental revenue from SMS replies
- Resolve repetitive support questions automatically
- Reduce ticket volume while improving response speed
- Provide 24/7 assistance

## Before you get started

### Requirements

- Active SMS plan
- Shopify recommended for full functionality (order tracking, recommendations)
- note: SHAFT brands cannot activate Customer Agent on SMS

### What messages does it handle?

Customer Agent will respond to inbound messages unless they:

- Match compliance keywords (STOP, HELP, etc)
- Trigger subscribe/unsubscribe logic (keywords, unsubscribe intent)
- Trigger an SMS keyword automation

### What happens if the Agent can’t resolve the issue?

- Follows handoff settings
- If you've chosen to escalate to a helpdesk, the agent receiving the ticket will receive a transcript of the customer agent conversation
- If you've chosen not to escalate to helpdesk, you will configure a closeout message to be sent when the agent cannot resolve the customer's need

### Built-in Guardrails to control SMS costs

- Messages that are spam or noise will be ignored. For example, auto-response messages like "I'm driving with focus turned on" will not trigger a customer agent conversation.
- Customer agent attempts to limit responses to a single SMS segment when possible
- When customer agent cannot resolve the customer's issue, it escalates instead of sending excessive messages

---

## Best practices for driving revenue with Customer Agent on SMS

### 1. Proactively invite replies in your campaigns and flows

Customer Agent only works if customers reply.

Encourage replies in:

- Abandoned cart messages (e.g., sizing, returns, styling questions)
- Welcome series (e.g., shade match, personalization inputs)

  Include:
- Clear invitation (“Reply with questions”)
- Context-specific prompts based on funnel friction

Save an agent conversation starter in Settings > Marketing. You can add this prompt to flows and campaigns with one click.

![](https://klaviyo.zendesk.com/hc/article_attachments/47313754403867)

### 2. Control which profiles can interact with customer agent

You have 3 choices:

- you can let all profiles interact with customer agent
- you can make customer agent exclusive to specific segments, or exclude certain segments
  - good for: operating customer agent as a VIP-only feature (ex. personal concierge)
- you can require certain keywords to initiate customer agent conversations, or exclude certain keywords
  - good for: guiding customer agent queries (ex. "reply style me for a personalized recommendation)
  - good for: ensuring certain queries go straight to your help desk

![](https://klaviyo.zendesk.com/hc/article_attachments/47313694679195)

### 3. Plan SMS + Agent usage together

Customer Agent consumes:

- AI conversations (priced per conversation)
- SMS segments (standard SMS billing applies)

  Best practices:
- Ensure SMS plan limit exceeds expected Agent usage
- Consider enabling Flex or AutoUpgrade to avoid throttling

### 4. Measure performance and identifying engaged customers

- Monitor SMS performance by going to the Performance page and filtering 'Key Metrics' by channel
- note: SMS revenue attribution follows the account’s SMS attribution model settings
- Identify and re-target profiles who interacted with customer agent by creating a segment
  - build a segment using "What someone has done"
  - choose from: Resolved Customer Agent Conversation, Escalated Customer Agent Conversation, Started Customer Agent Conversation

---

##
