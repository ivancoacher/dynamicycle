<h1>How to configure escalation rules</h1>

## You will learn

What escalation rules are, what they can and can’t do, and how to write triggers that hand off to a human at the right moments — without escalating too much or too little.

## Before you begin

You’ll need:

- An ****Owner****, ****Admin****, or ****Manager**** role
- Handoff settings configured — see **Managing Customer Agent settings**. When an escalation rule fires, the handoff follows whatever you’ve configured (helpdesk ticket, email forward, etc.).

## What escalation rules are

****Escalation rules**** are triggers that immediately hand off a conversation to a human. When a shopper’s message matches one of your rules, Customer Agent stops generating a response and starts the handoff.

Escalation rules are evaluated ****before**** Customer Agent generates a response. That means a matching message never gets a Customer Agent reply — it goes straight to a human.

You can create up to ****20 escalation rules****.

### What they’re NOT for

This is the most common confusion. Escalation rules can ****only trigger**** a handoff. They cannot:

- ****Teach Customer Agent how to behave.**** That’s a skill. Use a skill to tell Customer Agent how to respond to a topic.
- ****Prevent an escalation.**** Rules only add escalations; they don’t suppress them. If you want Customer Agent to handle something a skill is currently escalating, edit the skill’s behavior or add content.
- ****Route to different humans based on topic.**** Today, escalation rules use the same handoff destination for every triggered escalation.

## Set it up

1. Navigate to ****Customer Agent > Guidance > Escalation rules****.
2. Click ****Add rule****.
3. Write a ****Title**** — short and descriptive (e.g., “Defective product report”).
4. Write a ****Trigger description**** — natural-language description of when the rule should fire. Be specific.
5. Click ****Save****.
6. Test the rule in the playground.

## Writing good escalation rules

Good rules are:

- ****Topic- or situation-based**** — describe what the shopper is talking about, not the words they use
- ****Specific**** — broad triggers (“anything urgent”) fire too often and erode trust
- ****Mutually exclusive**** — avoid two rules that overlap; consolidate where possible

A rule fires when Customer Agent recognizes the shopper’s intent matches the trigger description. You don’t need to list every possible phrasing — describe the situation, not the keywords.

## Examples

Five escalation rules with reasoning:

- ****Defective product report**** — Customer reports an item arrived broken, malfunctioned, or stopped working. **Why escalate:** defective product claims often need warranty, replacement, or refund decisions a human should make.
- ****Legal threat or compliance issue**** — Customer mentions lawyers, lawsuits, regulatory complaints (FTC, BBB), or threatens legal action. **Why escalate:** legal language needs a human, immediately.
- ****Profanity or abusive language**** — Customer uses profanity directed at the brand or staff, or escalates to threats. **Why escalate:** a human can de-escalate or end the conversation appropriately.

## What happens when a rule fires

Customer Agent immediately:

1. Stops generating a response
2. Hands off the conversation according to your handoff settings
3. Logs the conversation as ****Escalated**** with the matched rule for reporting

The handoff destination (helpdesk ticket, email forward, custom message) is set in **Managing Customer Agent settings**.

## Troubleshooting

****Symptom:**** A rule isn’t firing when it should.
****Likely cause:**** Trigger description is too narrow or too specific to particular keywords.
****Fix:**** Rewrite the trigger to describe the situation in plain language. Test with multiple phrasings in the playground.

****Symptom:**** A rule is firing too often.
****Likely cause:**** Trigger description is too broad or overlaps with another rule.
****Fix:**** Narrow the description. Add explicit carve-outs (“does not include…”). Check for overlap with other escalation rules.

## FAQ

****How many escalation rules can I have?****
Up to 20.

****What if a shopper’s message matches two rules?****
Customer Agent will escalate on the first match. The conversation logs the rule that triggered the escalation.

****Can I disable a rule without deleting it?****
Yes. Toggle the rule off; you can re-enable it any time.

## Next steps

- ****Configure handoff settings**** so escalations go where you want them
- ****Test in the playground**** to see how rules fire on real messages
- ****Monitor the dashboard**** — review escalation rates and which rules fire most
