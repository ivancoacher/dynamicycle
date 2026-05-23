<h1>Troubleshooting custom CSS, JavaScript, and HTML in Klaviyo</h1>

## You will learn

Learn how to troubleshoot custom code when [importing a custom HTML template](https://help.klaviyo.com/hc/en-us/articles/115005254068-Import-a-Custom-HTML-Template-into-Klaviyo) or building your own custom coded template.

We only recommend using custom HTML for technically savvy marketers, or for anyone who has access to a developer. While our product does support custom HTML, our support team is unable to help you build out your custom templates beyond offering the general guidance covered in this documentation.

To maintain the security of your data, Klaviyo's support team is not able to open your HTML files.

## Custom HTML and CSS elements

If you're creating a custom HTML template, you cannot use product feeds within your email.

Certain HTML and CSS elements used to make emails interactive are not currently supported. For example, if you are looking to make your email interactive in Gmail by using certain CSS attribute selectors, your template may trigger an error in Klaviyo.

Klaviyo does not currently support certain operators (like ~) in email templates. This may limit the extent to which certain custom HTML and CSS can be used. If your template contains HTML or CSS that isn't fully supported, you will not be able to generate a preview of your email and will see an error message instead.

## Common HTML issues

If you're finding that your custom HTML email does not look correct, here are a few common places to check for problems.

### Single quotes in font

Wherever you're adding a font-family attribute in CSS, look for single quotes or unnecessary quotes. Remove all quotes when adding in your font.

|  |  |
| --- | --- |
| ****Problem**** | ****Fixed**** |
| font-family:'Helvetica Neue', Helvetica, Arial | font-family:Helvetica Neue, Helvetica, Arial |

### Media queries

If media queries are not in the standard format, they will not render properly. Follow the standard format for all media queries.

|  |
| --- |
| ****Standard media query format**** |
| @media only screen and (max-width: 460px) |

### Unnecessary center tags

If you have multiple HTML <center> tags throughout your email template, it may not render properly in Gmail. To fix this issue, remove all unnecessary <center> tags. Only one <center> tag is needed at the top of the email template near the <body> tag. All additional <center> tags are superfluous.

## Klaviyo does not support JavaScript emails

Most email clients (Gmail, Hotmail, Yahoo, etc.) view JavaScript in emails as a security threat. This is because scripts can hide malicious content. As a result, these major email clients block scripts in emails entirely. Given the inherent security threat associated with JavaScipt in emails and the lack of support for such scripts by most major email clients, any added scripts will automatically be removed.

## Klaviyo does not support embedded forms or videos

Klaviyo does not support embedded forms, widgets, or videos in templates. This is because our testing shows that these types of features do not reliably render across all major email clients. Similar to JavaScript snippets, most email clients view these elements as a security threat and strip them out of emails altogether.

If you're interested in learning workarounds for this, [check out this article on adding a video or GIF to an email](https://help.klaviyo.com/hc/en-us/articles/115005256968).

## Other unsupported tags and attributes

The HTML tags and attributes covered here are not an exhaustive list of what Klaviyo supports. In general, HTML elements that are [supported by major inbox providers](https://www.caniemail.com/) are also supported by Klaviyo.

If your template has unsupported HTML, Klaviyo will attempt to replace the unsupported elements with a supported alternative (i.e., a span tag). If there is no clear replacement, that portion of your HTML will be removed. If portions of your HTML seem to disappear after adding them, this means they are likely not supported; try an alternative HTML tag or attribute to achieve a similar effect.

## Additional resources

- [How to import a custom HTML template](https://klaviyo.zendesk.com/hc/en-us/articles/115005254068)
- [Troubleshooting email template error messages](https://klaviyo.zendesk.com/hc/en-us/articles/4402386684187)
