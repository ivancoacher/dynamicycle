<h1>Deliverability glossary</h1>

## You will learn

The glossary below defines common deliverability terms and acronyms used in Klaviyo offerings.

## A

****A Records****: A records is short for address records. They indicate the IP address connected to the web pages of a specific domain name. For ESPs, this is related to the local domain. The local domain forms the basis for the links that are visible in the emails that are sent out. Records are not set up in your email software. Instead, this is done via the DNS settings that you or your hosting provider manage.

****Allowlist****: A list of items, such as IP addresses, domain names, URLs, or usernames that are allowed access to a certain system protocol. This is also known as a whitelist.

## B

****Blocklist****: A blocklist is a list of items, such as IP addresses, domain names, URLs, or usernames that are denied access to a certain system protocol. Email blocklists are real-time databases that use criteria to determine if an IP is sending email it considers to be spam. There are blocklists for both IP addresses and domains that can severely impact their reputation and deliverability. This is also known as a blacklist.

****BIMI****: BIMI stands for Brand Indicators for Message Identification. This is a protocol that allows brands to authenticate the logo shown in inboxes based on sender’s DNS settings.

****Bots****: Robots created by malicious actors that subscribe to signup forms in high volumes all at once. Bots may look like real email addresses at first, but in reality, this practice is called list bombing and is a form of cybersecurity attack.

****Bounce****: When an email is unable to be delivered. There are two types of [bounces](https://help.klaviyo.com/hc/en-us/articles/115005250408-Bounced-Emails-in-Klaviyo): hard and soft. Hard and soft bounces occur for different reasons.

****Block****: A block occurs when an incoming email is blocked by the receiving inbox provider. This is typically due to a temporary reason, such as your IP being blocklisted or an issue with the content of the email.

****Branded sending domain****: [Branded sending domains](https://help.klaviyo.com/hc/en-us/articles/115000357752) (also known as dedicated sending domains) use the domain of a business instead of a shared domain supplied by Klaviyo. This process is also known as whitelabeling.

## C

****CAN-SPAM Act****: A US law intended to minimize the sending of unwanted emails, otherwise known as spam. CAN-SPAM “sets the rules for commercial email, establishes requirements for commercial messages, gives recipients the right to have you stop emailing them, and spells out tough penalties for violations.”

****CASL****: CASL stands for Canada’s anti-spam legislation and is similar to the CAN-SPAM Act in that it regulates the types of emails sent by commercial senders. CASL “protects consumers and businesses from the misuse of digital technology, including spam and other electronic threats. It also aims to help businesses stay competitive in a global, digital marketplace.”

****CCPA****: [CCPA](https://help.klaviyo.com/hc/en-us/articles/360035875272-Frequently-Asked-Questions-About-the-CCPA) stands for California Consumer Privacy Act. It's a law that will take effect on January 1, 2020 and will govern how businesses handle the personal information of California residents.

****Click tracking****: The URL used for analytics collection within an email. Recipients can see the tracking domain when hovering over a link or when clicking a link within the email.

****Clipping****: An email is “[clipped](https://help.klaviyo.com/hc/en-us/articles/115000591251-Why-is-my-email-being-clipped-)” by Gmail when it is over 102KB in size. When this happens, you may see a sharp decrease in open rates. This is because open events are calculated when a tracking pixel is loaded at the bottom of an email; if the email has been clipped, then this open event will not register, and thus open rates will be underreported. For more information on clipping and how to prevent it, check out our guide.

****CNAME****: [CNAME](https://help.klaviyo.com/hc/en-us/articles/360001550572-Setting-Up-Dedicated-Click-Tracking) is short for canonical name. This can be used to alias one name to another.
A common example is when you have both example.com and www.example.com pointing to the same application and hosted by the same server. In this case, to avoid maintaining two different records, it’s common to create:

- An A record for example.com pointing to the server IP address
- A CNAME record for www.example.com pointing to example.com

As a result, example.com points to the server IP address, and www.example.com points to the same address via example.com. Should the IP address change, you only need to update it in one place. If you edit the A record for example.com, www.example.com automatically inherits the changes.

## D

****DDoS attack****: DDoS stands for distributed denial of service. In a distributed denial-of-service attack (DDoS), the incoming traffic flooding the victim originates from many different sources. This effectively makes it impossible to stop the attack simply by blocking a single source.

A DoS or DDoS attack is analogous to a group of people crowding the entry door of a shop, making it hard for legitimate customers to enter, thus disrupting business.

****Dedicated IP address****: [A dedicated IP address](https://help.klaviyo.com/hc/en-us/articles/7675517826587) is an IP address that only one account uses (see also shared IP address).

****Dedicated click tracking****: [Dedicated click tracking](https://help.klaviyo.com/hc/en-us/articles/360001550572-Setting-Up-Dedicated-Click-Tracking) allows a customer to display their own domain on click tracking links as opposed to the default Klaviyo encoding.

****Deferred****: A deferred email means that the email was temporarily rejected by the inbox provider. Klaviyo will retry the message later, at which point it is generally accepted.

****Deliverability****: Email deliverability is defined as when an email successfully reaches the inbox (including tabbed inboxes, such as Google’s Promotions tab). An email is unsuccessfully delivered when it ends up in the spam folder or is blocked from reaching the inbox entirely.

****Delivery****: A delivery occurs when an email is delivered to the correct email address and was allowed by the recipient’s IP address. Even if your email was delivered to the spam folder, it still counts as a delivery.

****DKIM****: DKIM stands for domain keys identified mail. DKIM is a cryptographic technology created by Cisco and Yahoo that ensures that the message that arrives at the inbox provider is identical to the message that was sent. DKIM defends against malicious modification of messages in transit. Like an SPF record, DKIM is also a TXT record that’s added to a domain’s DNS. It’s also known as “email signing.” DKIM prevents the falsification of emails. If someone tampers with the content of an email, DKIM detects it.

****DMARC****: DMARC stands for domain-based message authentication, reporting, and conformance. DMARC is a protocol that uses SPF and DKIM to determine the authenticity of an email message. DMARC can tell a receiving server whether or not to accept an email from a particular sender. DMARC requires both SPF and DKIM to fail in order for it to act on a message. DMARC unifies DKIM and SPF and tells your server what to do if it receives a suspicious email. Also ensures that you receive information about forged email sent in your name.

****DNS****: DNS stands for domain name system. This system is essentially the "phone book of the Web". When you update your DNS records, you can consider this the equivalent of updating your address in the web's phonebook so that it's possible to verify who you are when you send an email. When we talk about a DNS provider, we’re talking about a service that hosts your domain name, like GoDaddy, or Cloudflare, HostGator, SquareSpace, etc.

****Domain****: A domain is the registered name that emails and images are sent from, like Klaviyo.com or boston.com. The domain name must be registered before you can use it. Every domain name is unique. No two websites can have the same domain name.

****Domain reputation****: A measure of how inbox providers view a sending domain’s trustworthiness, based on sending practices and infrastructure.

****DoS attack****: DoS stands for a denial of service. In computing, a DoS attack is a cyber-attack in which the perpetrator seeks to make a machine or network resource unavailable to its intended users by temporarily or indefinitely disrupting services of a host connected to the Internet. Denial of service is typically accomplished by flooding the targeted machine or resource with superfluous requests in an attempt to overload systems and prevent some or all legitimate requests from being fulfilled.

## E

****Email engagement****: Email engagement refers to recipients opening and/or clicking the emails you send them. Email engagement is used by inbox providers to determine whether or not your business is practicing good sending habits.

****ESP****: ESP stands for email service provider, or a system that you can use to send commercial and transactional emails to your customers. Klaviyo is considered an ESP.

## G

****GDPR****: [GDPR](https://help.klaviyo.com/hc/en-us/articles/360003211651-Frequently-Asked-Questions-About-GDPR) stands for the General Data Protection Regulation. It’s a law enacted by the European Commission in 2016 that went into effect on May 25, 2018. It’s designed to protect the privacy of all EU citizens, including when those citizens engage with businesses located outside the European Union, by imposing regulations around personal data.

## H

****Hard bounce****: A hard bounce occurs when an email cannot be delivered due to a permanent reason, such as an invalid email address. Klaviyo will automatically suppress any email addresses that have hard bounced.

****Header****: Also called the email header, this refers to identifying information about email such as the subject line, from address, recipient address, date, and more.

## I

****Inbox provider****: Also called a mailbox provider, this is a service used to manage email correspondence, for example, Outlook, Gmail, and more. These are companies that provide their customers with servers to send, receive, accept, and store email. Some inbox providers attract users because they are free and they advertise their services on every message.

****IP address****: An IP address is a number listed in the domain name system that sends mail on behalf of your domain name. Inbox providers check reputations of IP’s sending emails on behalf of domains.

****IP reputation****: A measure of how inbox providers view an IP address’ trustworthiness as a sender, based on sending practices and infrastructure.

****ISP****: ISP stands for Internet service provider. These are organizations that provide services for accessing or using the Internet. Some ISPs also provide email service but may lack some features that are typically offered by providers who focus primarily on email. This includes web-hosted inbox providers, like Verizon, Xfinity, and more.

## L

****List bombing****: [List bombing](https://help.klaviyo.com/hc/en-us/articles/9890182538011) refers to the practice of abusing and attacking email list signup pages by bombarding them with a large number of new email addresses at the same time. At first, it may look like a spike in signups. In reality, it’s a cyber attack.

****List cleaning****: [List cleaning](https://help.klaviyo.com/hc/en-us/articles/115005078347-List-Cleaning) is the process of removing invalid and/or unengaged contacts from your subscriber list. This ensures that you don’t inadvertently email any addresses that will negatively impact your sending reputation.

## M

****MBP****: MBP stands for mailbox provider, also called an inbox provider. This is a service used to manage email correspondence, for example, Outlook, Gmail, and more. These are companies that provide their customers with servers to send, receive, accept, and store email.

****MX record****: MX record stands for mailer exchange record. This specifies the mail server responsible for accepting email messages on behalf of a domain name. It is a resource record in the DNS.

MX records must be used in conjunction with A records. The A record will point to the mail server(s). When another mail server wants to communicate with your mail server, it will look for an MX record. That MX record must point to the A record which points to the mail server’s IP address.

## P

****Permission pass****: A one-time email sent to recipients to verify opt-in permission. It requires that you have already gained verifiable opt-in permission at some point, but perhaps you haven’t seen them engage with your messaging in a long time. Recipients who open and click a CTA within the email to confirm their subscription will remain subscribed, while recipients who don’t click are suppressed or removed from your email list. The latter category of recipients should be engaged through other marketing channels and driven back to your website, where they can resubmit an email signup form to receive future emails.

****Phishing****: A hacker attempts to fraudulently retrieve a users’ sensitive information by imitating electronic communication from a trusted organization in an automated manner.

****Pristine spam trap****: [A pristine spam trap](https://help.klaviyo.com/hc/en-us/articles/360003019251-What-is-a-Spam-Trap#pristine-spam-trap--pst-1) (PST) is created with the intention of finding people who are sending spam or not following best sending practices. These emails are never used in real-world instances and are brand new addresses, so hitting a PST is likely to cause your IP to be blocklisted or your emails to go to spam. In the eyes of mailbox providers, this means you either purchased a list or do not follow best practices since these addresses are not legitimate and do not open emails.

## R

****Ramping****: Ramping is a process that aids in the overall warming process to become a reputable sender, whether you are using a dedicated or shared IP. When ramping a dedicated IP, this will be part of your overall warming process as it relates to your new infrastructure. Ramping shared IP’s involves new customers needing to warm their reputation relative to their new relationship with Klaviyo IPs.

****Recycled spam trap****: [A recycled spam trap](https://help.klaviyo.com/hc/en-us/articles/360003019251-What-is-a-Spam-Trap#recycled-spam-trap--rst-2) (RST) is an address that was used as a real address at some point in the past. It’s common to see RSTs as domains provided by free services, such as @yahoo or @gmail. You may see domains of closed businesses repurchased with the intention of making them RSTs. An out-of-date email doesn’t always become an RST immediately. Some inbox providers may delete the address after no activity -- e.g. if the address stops receiving emails.

## S

****Sending domain****: The sending domain is the registered name on the internet (e.g., companyxyz.com). A domain reputation is the sending reputation for the domain name. This can be the subdomain or domain.

****Sender reputation****: A measure of how inbox providers view an email sender's overall trustworthiness, based on their sending practices and infrastructure. Sender reputation is a key consideration inbox providers use when determining where to place an email (e.g., spam, promotions, primary).

****Shared IP address****: An IP address that multiple senders use.

****Shared**** s****ending domain****: Shared sending domains contain a root domain shared among multiple Klaviyo accounts. Klaviyo automatically adds a unique element to sending domains to make it easier for more sophisticated inbox providers like Gmail and Hotmail to identify each sender as different.

****Soft bounce****: A soft bounce occurs due to a temporary reason, such as the inbox being full or the recipient’s email server being down momentarily. Klaviyo will automatically suppress email addresses that soft bounce more than seven consecutive times.

****Spam****: Spam is unsolicited bulk email.

****Spam complaint****: A spam complaint is recorded when an email recipient actively marks one of your emails as spam. This is tracked in Klaviyo in the analytics of a particular campaign or flow email. Spam complaints are not tracked when an email simply winds up in the spam folder, but only when someone takes action to mark your email as spam.

****Spam trap****: [A spam trap](https://help.klaviyo.com/hc/en-us/articles/360003019251-What-is-a-Spam-Trap#overview0) is an email address, or in some cases, an entire domain, used to capture, collect, and monitor email sent to it​. Spam traps are usually created and managed by ISPs & mailbox providers, mail administrators, and/or other similar groups. The main purpose of spam traps are an attempt to gain information on who is sending it in hopes of preventing future incidents

****SPF****: SPF stands for sender policy framework. An SPF record is like the return address placed on a letter indicating who sent it. If a recipient knows and trusts the person who sent them the letter, they’re more likely to open it. SPF records prevent someone from sending an email on behalf of your organization. SPF checks the sender of an email for authenticity.

****Spoofing****: Email spoofing means that a phisher has modified the email header of a message so that it appears as if it was sent from someone else. Hackers may use this technique to impersonate an employee of a company, for example, to obtain login credentials, personal data, or other confidential information. In this metaphor, the “recipient” is actually a receiving mail server, not a person. The SPF record is a short line of text that an administrator of that domain adds to their TXT record. The TXT record is stored in the DNS.

****Subdomain****: An extension of a main domain; specifically the prefix in a sending domain (e.g. sending domain is send.helloworld.com, the subdomain is send).

****Suppress****: A [suppressed](https://help.klaviyo.com/hc/en-us/articles/115005246108-Suppressed-Profiles-in-Klaviyo) contact is a contact that can no longer be contacted. A contact can become suppressed due to a variety of reasons, including:

- Unsubscribing
- Marking one of your emails as spam
- Hard bouncing
- Soft bouncing 7+ times in a row
- Being manually suppressed

## T

****TINS****: TINS stands for this is not spam. Emails that recipients recover from their spam folder by marking it as “this is not spam,” letting the inbox provider know that the user would like to receive these emails.

****TXT record****: TXT record stands for text record. These hold free form text of any type and are used to verify the authenticity of emails. Historically, they have also been used to contain human-readable information about a server, network, data center, and other accounting information.

A fully qualified domain name may have many TXT records. The most common uses for TXT records are SPF, DK, DKIM, and DMARC.

## W

****Warming****: [Warming](https://help.klaviyo.com/hc/en-us/articles/360025945671-Warming-Your-Sending-Infrastructure) refers to the process of establishing a good sending reputation when you first start sending emails with Klaviyo. The warming process is especially important if you are sending from a dedicated IP address and/or dedicated sending domain. The exact warming schedule will vary from case to case, but in essence, to warm your sending infrastructure, you will need to turn on high engagement flows, send your first campaigns to highly engaged recipients, closely monitor your engagement, and adjust accordingly.
