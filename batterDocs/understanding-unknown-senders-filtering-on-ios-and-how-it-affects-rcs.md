<h1>Understanding Unknown Senders filtering on iOS and how it affects RCS</h1>

When you send RCS messages, they are delivered from an RCS agent. If you've sent SMS messages previously, then your subscribers will be receiving your RSC messages from a new sender. Although these messages are sent from your branded and verified RCS agent, they may appear in the “Unknown Senders” inbox on some subscribers’ iOS devices.

## ****How the Unknown Senders inbox works****

On iOS, users can enable a setting called Filter Unknown Senders, which separates messages from numbers or senders not saved in their contacts and with whom they have not previously engaged.

- This setting is off by default, meaning most users will receive all messages in their primary inbox.
- When on, the first message from a new Sender ID (e.g. RCS agent) appears in both the primary and unknown senders inboxes, allowing the recipient to review it and mark the sender as known.
- If the recipient marks the sender as known, all future messages from the SID (e.g. RCS agent) will appear in the primary inbox.
- If they do not, any future messages from that Sender ID (e.g. RCS agent) will appear only in the unknown senders inbox.

## ****Contact Cards****

Unlike SMS senders, RCS agents cannot be saved as contacts on a user’s device. As a result, contact cards are not supported on RCS.

If any of your existing flows include contact cards, they will be automatically removed from the RCS version of the message to avoid delivery issues.

You should update these flows by either:

- Editing the RCS version of the message to remove references to saving the sender as a contact and instead ask users to mark the sender as known, or
- Using a conditional split to prevent the message from sending to RCS recipients altogether.

## ****Recommended best practices****

To maximise visibility and keep your RCS messages in the primary inbox, encourage recipients to mark the sender as known when making first contact on an RCS agent.

## ****Summary****

- RCS messages are sent from a new Sender ID (RCS agent).
- RCS agents cannot be saved as contacts, and contact cards are not supported on RCS.
- The Unknown Senders filter is off by default. When enabled, messages from unknown senders, including RCS agents, are moved to the Unknown Senders inbox.
- When someone receives a message from an RCS agent for the first time, they are prompted to mark the sender as known. Once marked as known, all future messages from that RCS agent will appear in the primary inbox.
