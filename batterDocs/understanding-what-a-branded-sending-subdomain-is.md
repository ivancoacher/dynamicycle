<h1>Understanding what a branded sending subdomain is</h1>

## You will learn

When setting up a [branded sending domain](https://klaviyo.zendesk.com/hc/en-us/articles/115000357752) (also known as a dedicated sending domain), you will need to choose an associated subdomain or prefix. In this article, you will learn more about how to choose a subdomain that is right for your business.

## Understanding sending domain prefixes

A sending domain is the domain that your emails are sent from and will appear in your email header. Each domain begins with a subdomain. For example, if your sending domain is **send.helloworld.com**, the subdomain is **send**.

You can choose any word as your subdomain, as long as it is not already being used within your DNS (domain name system). That said, you will want to choose a word that fits your brand and sending purpose. “Send” is the most common prefix for dedicated sending domains, and the one we recommend at Klaviyo, because it is typically unused by another service within a DNS. We will dive deeper into how to choose a sending subdomain that is right for you in the section below.

## Sending domain prefix best practices

When setting your dedicated sending domain in Klaviyo, you will need to add a subdomain under **Sending domain** during this process.

![branded1.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28722596814107)

As mentioned [above](#h_01EW0NPYD4BBR1EYE6VQS0E1W9), you can technically choose any word you want as your subdomain. Keep these best practices in mind when choosing a subdomain:

- ****There can be no duplicate subdomains in your DNS****
  When you create a sending domain, it becomes its own unique web address. For that reason, you can only use a subdomain once within your DNS, since you can’t have multiple pages with the same address. You can check within your DNS registry to see if a given subdomain is available.
  However, in Klaviyo, you can use the same subdomain for multiple accounts since it will all be attributed to that one domain in your DNS. For example, if you manage a US and UK account for a given brand, you can use the same sending domain for both. If you use one sending domain across multiple accounts, the [CNAME or NS records](https://help.klaviyo.com/hc/en-us/articles/360039295051-Deliverability-Glossary#c2) should be the same, but each account will have a different TXT value and each TXT value needs to be added into the DNS record.
- ****Your subdomain should suggest email sending****
  Though you can choose any word for your subdomain, we recommend that you choose a subdomain that implies email sending. Other users of your DNS can then easily identify your subdomain; this will reduce the chances of another user deleting or editing it by mistake. When you go through your DNS records at any point in the future, you will see this subdomain and easily know that it is for dedicated sending.

  You will want to easily determine which subdomain specifies your sending domain. For example, subdomains such as **send.helloworld.com**, **emails.helloworld.com**, or **newsletter.helloworld.com** can all work.

We recommend that you do not use **mail** as a subdomain as it is typically reserved for an inbox setup and already used in the DNS.

In a nutshell, you can choose any word as your subdomain, but it is a best practice to choose one that fits the purpose of your domain and is not already in use. For more information on creating a branded sending domain, head to [how to set up a branded sending domain](https://klaviyo.zendesk.com/hc/en-us/articles/115000357752).

## Additional resources

- [How to set up a branded sending domain](https://klaviyo.zendesk.com/hc/en-us/articles/115000357752)
- [How to set up dedicated click tracking](https://klaviyo.zendesk.com/hc/en-us/articles/360001550572)
- [Getting started with email deliverability](https://klaviyo.zendesk.com/hc/en-us/articles/115005247008)
