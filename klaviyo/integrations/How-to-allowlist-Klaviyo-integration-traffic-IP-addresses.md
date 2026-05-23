---
id: 19143781289115
title: "How to allowlist Klaviyo integration traffic IP addresses"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/19143781289115-How-to-allowlist-Klaviyo-integration-traffic-IP-addresses"
section: "All integrations"
category: "Integrations"
category_slug: "integrations"
klaviyo_updated: "2026-04-21T13:54:32Z"
language: en
---

## You will learn

Learn how to allowlist IP addresses for outbound Klaviyo integration traffic to ensure that your firewall is not blocking Klaviyo’s requests. All outbound Klaviyo integration traffic is behind a set of predictable, static IP addresses so that you can have a high level of confidence that this traffic is coming from Klaviyo. This is especially applicable to customers using self-hosted ecommerce integrations such as Magento 2 and WooCommerce.

Please note that integration traffic does not include flow-triggered webhook traffic, which uses different IP addresses.

## What IP addresses does Klaviyo use for integration traffic?

The IP address range used by Klaviyo for integration traffic is 207.211.192.0 - 207.211.207.255. This is the range that you should allowlist. This range can be represented as the CIDR address `207.211.192.0/20`.

If you are restricted from allowlisting /20 ranges, our range can be represented as 16 /24 ranges. Thus, you would need to allowlist:

`207.211.192.0/24`

`207.211.193.0/24`

`207.211.194.0/24`

`207.211.195.0/24`

`207.211.196.0/24`

`207.211.197.0/24`

`207.211.198.0/24`

`207.211.199.0/24`

`207.211.200.0/24`

`207.211.201.0/24`

`207.211.202.0/24`

`207.211.203.0/24`

`207.211.204.0/24`

`207.211.205.0/24`

`207.211.206.0/24`

`207.211.207.0/24`

## How-to examples

### How to allowlist in Cloudflare

Cloudflare does not accept allowlisting /20 ranges, so you'll need to allowlist all 16 of the /24 ranges given above.

1. Log in to your [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account and domain.
2. Go to ****Security > WAF > Tools****.
3. Under **IP Access Rule**s, enter the following details:
   1. For **Value**, enter the first range: `207.211.192.0/24`.
   2. Select the ****Allow**** action.
   3. For **Zone**, select whether the rule applies to the current website only or to all websites in the account.
   4. Enter a note for the rule (optional).
4. Select ****Add****.
5. Repeat this process for each of the 16 /24 ranges given in the section above.

You can learn more about IP access rules in [Cloudflare’s documentation](https://developers.cloudflare.com/waf/tools/ip-access-rules/).

### How to allowlist in Akamai

1. In the [Console](https://console.janrain.com/#/login), from the Edit page, click ****Add New IP Address****.
2. In the **Whitelist an IP network** field, type `207.211.192.0/20`.
3. When you are finished, click the **Save changes** icon.

You can learn more about managing IP allowlists in [Akamai’s documentation](https://techdocs.akamai.com/identity-cloud/docs/manage-property-ip-allow-lists).

## Outcome

You’ve successfully allowlisted Klaviyo’s static IP addresses for outbound integration traffic. Your firewall or security provider will now safely let that traffic through, knowing that it originates from Klaviyo.