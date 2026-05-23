<h1>How to use the marketing agent</h1>

## Overview

The marketing agent is Klaviyo’s AI-powered tool to generate an on-brand marketing plan. Using only your website, the marketing agent gathers your brand assets, analyzes your brand voice, and builds a starter plan.

## Before you begin

- To access the marketing agent, your user role must be Owner, Admin, or Manager.
- The website used for setup must be a publicly accessible URL (not a password-protected or staging site).

## Set up the marketing agent

1. ****Access the marketing agent.****From within your Klaviyo account, navigate to the marketing agent via the button in the top right of the Klaviyo navigation bar.
   ![](https://klaviyo.zendesk.com/hc/article_attachments/41343672117531)
2. ****Review your brand settings.****The marketing agent will use your organization's website to gather information about your brand. It will collect images, copy, brand voice, and brand color information. This process typically takes 30-60 seconds to complete.Once the scraping process completes, you will be able to review your brand settings and adjust any inputs that have been pre-filled. This is also where you can set the language that will be used for generating content.Once complete, click the ****Yes, create**** button on the left side of the screen.

   There are multiple reasons why the information may not be pre-filled, most commonly due to a password-protected site or a restriction in the website’s robots.txt file. You can still manually input the brand settings to progress.
3. ****Finish setting up your account during the generation process (new accounts only).****The generation process often takes 5–10 minutes. You will receive an email when the generation process completes, so you can safely navigate away from this screen.

If you’re setting up a new account, we recommend that you use this time to complete your account setup by clicking the ****Set up account**** button on the left. This step involves verifying your email, your sender information, integrating your platform (if an integration exists), and uploading a list of existing subscribers.

## Review your marketing plan

Once the generation process is complete, you will see your marketing plan recommendations.

- All accounts will receive 4 campaigns. All campaigns will be scheduled to send to a segment of your subscriber list intended to ensure deliverability.
- You will receive a signup form and a welcome series flow if those are not yet set in your account.
- You will receive an abandoned cart flow and order confirmation flow if your account is detected to be integrated with: Shopify, BigCommerce, Magento 2, WooCommerce, Wix, PrestaShop, or Salesforce Commerce Cloud.
- You will receive an order confirmation flow if your account is detected to be integrated with: Olo, Thanx, or Toast.

This content is created by AI. Please review and make sure everything looks right before using it. You are ultimately responsible for the content of your messages.

When you click into a recommendation, you can review the generated content. You can see the desktop and mobile preview of the content as well as any recommended settings.

If you approve of the content, you can select the ****Launch**** button to launch the campaign, flow, or form. You will receive a warning if there are any prerequisite setup steps required to launch.

If you want to make edits to the content before launching, you can click the ****Edit**** button. This will create the content in your account. You can edit it just as any other campaign, form, or flow in Klaviyo. You can add your own image assets, edit text, and adjust all settings.

If you click the ****Delete**** button, this recommendation will be removed from your feed. Additionally, you can click the ****Provide feedback**** button to give Klaviyo more context about the recommendation. The marketing agent will use this information to guide future generations.

## Returning to the marketing agent

You can return to the marketing agent at any time and review the impact of the objects it generated. Every 7 days you will have the ability to run another marketing agent generation.

## Content generation guardrails

The marketing agent uses a number of built-in safeguards to help ensure generated content is accurate, safe, and on-brand. However, due to the nature of large language models, generated content may not always be 100% accurate. You're responsible for reviewing and approving all final messages.

#### Brand voice and quality control

The agent pulls in your brand voice automatically by analyzing your website or using any pre-filled [brand voice](https://help.klaviyo.com/hc/en-us/articles/35873068949147) that exists in your Klaviyo account. It uses this voice when generating subject lines, preview text, and message content. Our multi-agent approach ranks, refines, and regenerates ideas until the output meets quality thresholds.

#### Factuality and research depth

We prompt the agent to avoid hallucinations and rely on facts from your website and Klaviyo account. If more information is needed, the agent runs additional research to generate more detailed content.

#### Cohesion across content

All generated emails share a consistent context: your company information, audience, and brand style. Before finalizing the plan, the agent checks that subject lines, preview text, and email templates align and revises them if needed.

#### Product and promotion accuracy

The agent avoids referencing products or offers that don’t exist. We have additional guardrails to catch and regenerate any copy that includes unverified discounts or coupons.

#### Toxicity and compliance filters

To reduce the likelihood of generating harmful or inappropriate content, we use third-party moderation tools to scan outputs for issues. If any violations are detected, the agent regenerates the message.

#### CAN-SPAM compliance requirements

Our system has guardrails in place to include an unsubscribe link, organization name, and organization address in emails to help you effectively comply with CAN-SPAM regulations. Even with these guardrails, please ensure your messages comply with all local laws and regulations related to where you are sending. You are ultimately responsible for the content of your messages.

## FAQ

- ****How long does a generation take?****
  - The marketing agent generation often takes up to 10 minutes, but during periods of high demand it may take longer. You will receive an email when your recommendations are available.
- ****Which languages are supported?****
  - Currently, content can be generated in English, French, and German. To select the content‐generation language, go to the Marketing Agent [confirm assets page](https://www.klaviyo.com/account-setup/marketing-agent/confirm-assets) and select your marketing language from the drop down. Support for additional languages is coming soon.
- ****Can I edit the content before I send?****
  - Yes, you can click ****Edit**** on any recommendation to edit it in the Klaviyo builder.
- ****Is the marketing agent free to use?****
  - Yes, all Klaviyo accounts have access to the marketing agent.
- ****Can I regenerate sooner than 7 days?****
  - No, currently you can only generate new recommendations every 7 days.
- ****What image types can the marketing agent gather from my website?****
  - The marketing agent can currently gather .png, .jpg, .jpeg, and .gif image file types. Other image file types (such as .svg and .webp) will not be used in generating content.
