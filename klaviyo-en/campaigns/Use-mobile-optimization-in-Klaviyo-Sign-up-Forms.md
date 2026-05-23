---
id: 44513639011099
title: "Use mobile optimization in Klaviyo Sign-up Forms"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/44513639011099-Use-mobile-optimization-in-Klaviyo-Sign-up-Forms"
section: "Email campaigns"
category: "Campaigns"
category_slug: "campaigns"
klaviyo_updated: "2026-04-21T20:06:37Z"
language: en
---

Use mobile optimization in Klaviyo Sign-up Forms

Dec 17, 2025, 11:56:51 AM

## Overview

Tailor your Klaviyo forms for desktop and mobile without duplicating forms, helping you publish faster and improve the experience for mobile visitors.

Mobile optimization lets you design per-device experiences by editing mobile and desktop views side by side, and by choosing whether changes to blocks sync across devices or stay device-specific.

## Before you begin

- Some block types do not support unlinking between devices. Exceptions include: Disclosure, Spin to win, Image (handled separately), and Phone number (multi-step consent).

## How it works

### Dual device preview toggle

Preview your form in desktop and mobile side by side to see how edits adapt across devices in real time. This reduces back-and-forth toggling and speeds up mobile design quality.

![Image of the mobile/ desktop/ dual view toggle](https://klaviyo.zendesk.com/hc/article_attachments/44513671380507)

### Linked vs. unlinked blocks

By default, equivalent blocks in desktop and mobile are linked: changes in one view carry over to the other. You can choose to unlink blocks to make mobile- or desktop-only edits without duplicating your form.

![Image highlighting the location of the in-canvas linking and unlinking button](https://klaviyo.zendesk.com/hc/article_attachments/44513671385371)

You can unlink/relink a selected block by clicking the ****in-canvas unlink button****, or clicking the ****side-panel unlink button****.

When a block is unlinked:

- Edits apply only to the current device view; the other device’s block isn’t changed.
- Cloning an unlinked block creates the clone only in the current device view (cloning a linked block duplicates it to both devices).

Relinking blocks:

- Relinking creates a new paired block across devices again. If the counterpart block has been deleted, relinking creates it for the other device so both views have the block again (you can then delete any duplicates you don’t need).

### Teasers per device

You can unlink teasers via the side panel, so that desktop and mobile each have their own teaser styling. Relinking resets visibility back to all devices for the relinked teaser.

![Image showing the form teaser with different content between desktop and mobile view](https://klaviyo.zendesk.com/hc/article_attachments/44513671387035)

## Step-by-step

### Open dual preview

1. Open your form in the editor.
2. Switch to the preview via the ****toggle**** that shows both desktop and mobile side by side to assess layout and spacing at a glance.

![The image showing the Klaviyo forms editor with the device view toggles highlighted](https://klaviyo.zendesk.com/hc/article_attachments/44513671391387)

### Unlink a block for device-specific edits

1. Select the block you want to customize on mobile.
2. Choose ****Unlink**** so mobile edits won’t affect desktop.
3. Adjust your mobile layout (e.g., location, font sizes, spacing) for readability on smaller screens.
4. Repeat for other blocks as needed.

![The image showing the Klaviyo forms editor with the in-canvas, and side-panel unlink buttons highlighted](https://klaviyo.zendesk.com/hc/article_attachments/44513671393563)

### Relink when you want shared behavior again

1. Select the block and choose ****Relink****.
2. If the counterpart is missing on the other device, the editor creates it automatically.
3. Remove duplicated blocks.

![The image showing the Klaviyo forms editor with the in-canvas, and side-panel relink buttons highlighted](https://klaviyo.zendesk.com/hc/article_attachments/44513639004699)

![The image showing the Klaviyo forms editor showing the outcome of relinking a block from the desktop view](https://klaviyo.zendesk.com/hc/article_attachments/44513639005851)

### Set teasers by device (optional)

1. Open teaser settings and choose ****Unlink****.
2. Configure teaser content or visibility for desktop and mobile independently.
3. Relink later if you want one teaser to apply to both devices.

## Best practices for mobile forms

- Prioritize smaller screens: use bigger fonts, concise copy.

- Increase tap targets and vertical spacing so buttons and inputs are easy to use.

- Consider full-screen on mobile for focus and clarity, especially on smaller devices.

- Keep imagery purposeful. If a side image competes with content on small screens, hide it or simplify the layout.

## Limitations and behaviors to know

- A linked block is a single block with device visibility set to both desktop and mobile. Any edits you make in either view update that one shared block.

- When you unlink a block, the editor creates a second block under the hood and sets each block to a different device (one desktop-only, one mobile-only). From that point on, edits are not synced between them.

- Unlinking is not supported for some block types: Disclosure, Spin to win, Image (handled separately in side-image work), and Phone number (multi-step consent).

- Cloning behaves differently based on link state: clones of linked blocks appear on both devices; clones of unlinked blocks appear only on the current device view.

- When you relink, the selected block becomes the source of truth and is set to show on both devices. If a counterpart is missing, the editor creates it; if multiple versions exist, you may need to manually remove any extra blocks you don’t want to keep.

## Outcome

You should now be able to create a sign-up form that is optimized for mobile devices without creating two separate forms.

## Troubleshooting

- I don’t see unlink/relink on a block:
  The block type may not support unlinking (see exceptions).

- My mobile change affected desktop (or vice versa):
  Make sure the block is unlinked before editing the device-specific version.
- My relink created an extra block:
  That’s expected if the counterpart was missing. Delete the duplicate you don’t need after relinking.

## Next steps

- [Getting started with sign-up forms.](https://help.klaviyo.com/hc/en-us/articles/360026474752)

- [Basics: form form design.](https://help.klaviyo.com/hc/en-us/articles/15763867466395)

- [How to A/B test a sign-up form.](https://help.klaviyo.com/hc/en-us/articles/360045462071)