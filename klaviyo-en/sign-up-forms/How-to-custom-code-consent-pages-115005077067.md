---
id: "115005077067"
title: "How to custom code consent pages"
source_url: "https://help.klaviyo.com/hc/en-us/articles/115005077067-How-to-custom-code-consent-pages"
section: "Getting started with consent pages"
category: "Sign-up forms"
category_slug: "sign-up-forms"
klaviyo_updated: "2026-04-21T13:54:18Z"
language: "en"
---
## You will learn

Learn how to enable and use Klaviyo's hosted pages feature, which allows you custom code your own preference pages, subscribe pages, and unsubscribe pages.

This article is for developers; Klaviyo does not currently offer services to help build out custom code, nor do we provide support for custom code troubleshooting. To learn about our built-in app consent pages, head to our [article on getting started with consent pages](https://help.klaviyo.com/hc/en-us/articles/115005251848).

## Before you begin

Before configuring a hosted page, enable this feature:

1. Navigate to ****Settings > Other****.
2. Choose ****Consent pages**** from the dropdown.
3. Under **Custom hosted pages**, toggle on the switch to **Use custom dedicated domain for hosted pages**.
   ![The Custom Hosted Pages section on the Consent Pages tab in Klaviyo showing the switch to enable hosted pages.](https://klaviyo.zendesk.com/hc/article_attachments/33232831304219)

Note that only accounts with a paid plan who have passed [account verification](https://help.klaviyo.com/hc/en-us/articles/115000628331) have access to this setting.

## Create a custom consent page

1. Head to ****Settings > Other****.
2. Click ****Hosted pages****.
3. Next to **Pages**, click the ****+**** symbol to add a new page.
4. Name this page (e.g., unsubscribe.tmpl); you will be able to use this for any of your consent pages, but you can create more than 1 page if you'd like.

   Hosted page names cannot contain spaces as it will lead to an error. Avoid spaces or use underscores  to break up titles.
5. Design an HTML page that includes the fields and features of your choice. Example fields that can be inserted for a custom consent page include:
   - Choices for email frequency:
     - An option to unsubscribe
     - An option to receive all emails
     - Frequency options for daily, weekly, monthly, etc. newsletters
   - Information that can be used to target and segment:
     - A checkbox for whether or not the user wants sale announcements
     - A checkbox for whether or not the user wants product announcements
     - A checkbox for whether or not the user wants blog updates
     - Other lists the user may want to join

****Example of HTML code for a consent page****

You can use this code in your unsubscribe.tmpl to get a fully functional consent pages with email type and frequency preferences:

```
<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <!-- Latest compiled and minified CSS -->
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
      <style type="text/css">
        /* Space out content a bit */
        body {
            padding-top: 20px;
            padding-bottom: 20px;
        }

        form {
            margin-bottom: 18px;
        }

        /* Custom page header */
        .header {
            border-bottom: 1px solid #e5e5e5;
            margin-bottom: 10px;
        }

        .header h1 {
            margin: 10px 0;
        }

        .required-fields {
            text-align: right;
        }

        .required-fields span {
            color: #a94442;
            font-weight: bold;
        }

        .list-group-item label {
            font-weight: normal;
            margin-top: 17px;
        }

        .list-group-item label input[type="checkbox"] {
            margin-right: 4px;
        }

        .form-group span.required {
            position: absolute;
            top: 0;
            right: 0;
            font-size: 20px;
            color: #a94442;
            font-weight: bold;
            user-select: none;
        }

        label.error {
            color: #a94442;
            font-weight: bold;
            margin-top: 4px;
        }

        .form-actions {
            margin: 25px 0;
        }

        .form-control+.form-control {
            margin-top: 6px;
        }

        .panel-group .panel-title .closed-icon,
        .panel-group .panel-title .open-icon {
            margin-right: 0.5em;
            top: 2px;
        }

        .panel-group .panel-title a:hover,
        .panel-group .panel-title a:active {
            text-decoration: none;
        }

        .panel-group .panel-title a:hover .text,
        .panel-group .panel-title a:active .text {
            text-decoration: underline;
        }

        .panel-group .panel-title .closed-icon {
            display: none;
        }

        .panel-group.closed .panel-title .open-icon {
            display: none;
        }

        .panel-group.closed .panel-title .closed-icon {
            display: inline;
        }

        /* Custom page footer */
        .footer {
            padding-top: 18px;
            border-top: 1px solid #e5e5e5;
        }

        /* Customize container */
        @media (min-width: 768px) {
            .container {
                max-width: 730px;
            }
        }
    </style>
      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
      <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->
   </head>
   <body>
      <div class="container">
         <div class="header">
            <img src="http://via.placeholder.com/300x75" />
            <h1>Email Preferences</h1>
         </div>
         <form action="" id="preferences_form" method="POST" role="form" class="form-horizontal">
            {% if form.non_field_errors %}
            <div class="alert alert-danger">
               {% for error in form.non_field_errors %}
               {{ error }}{% if not forloop.last %}<br />{% endif %}
               {% endfor %}
            </div>
            {% endif %}
            <input type="hidden" name="$fields" value="EmailInterests,EmailFrequency" />
            <input type="hidden" name="$list_fields" value="EmailInterests" />
            <!-- <input type="hidden" name="$unsubscribed_url" value="/p/preferences_updated" /> -->
            <!-- <input type="hidden" name="$updated_profile_url" value="/p/preferences_updated" /> -->
            <!--<p class="required-fields">
               <span>*</span> Required Information
               </p>-->
            <div class="form-group{% if form.errors|lookup:'$email' %} has-error{% endif %}">
               <label for="email" class="col-sm-3 control-label">Email Address<span class="required">*</span></label>
               <div class="col-sm-9">
                  <input type="email" class="form-control" id="email" name="$email" value="{% if request.POST|lookup:'$email' %}{{ request.POST|lookup:'$email' }}{% else %}{{ person.email|default:'' }}{% endif %}" />
                  {% if form.errors|lookup:'$email' %}
                  <p class="help-block">{% for error in form.errors|lookup:'$email' %}{{ error }}{% endfor %}</p>
                  {% endif %}
               </div>
            </div>
            <div class="form-group">
               <label for="first_name" class="col-sm-3 control-label">First Name</label>
               <div class="col-sm-9">
                  <input type="text" class="form-control" id="first_name" name="$first_name" value="{% if request.POST|lookup:'$email' %}{{ request.POST|lookup:'$first_name' }}{% else %}{{ person.first_name|default:'' }}{% endif %}" />
               </div>
            </div>
            <div class="form-group">
               <label for="last_name" class="col-sm-3 control-label">Last Name</label>
               <div class="col-sm-9">
                  <input type="text" class="form-control" id="last_name" name="$last_name" value="{% if request.POST|lookup:'$email' %}{{ request.POST|lookup:'$last_name' }}{% else %}{{ person.last_name|default:'' }}{% endif %}" />
               </div>
            </div>
            <div class="form-group">
               <label for="interests" class="col-sm-3 control-label">Interests</label>
               <div class="col-sm-9">
                  <div class="checkbox">
                     <label>
                     <input type="checkbox" name="EmailInterests" value="New Releases" {% if 'New Releases' in person.EmailInterests or 'New Releases' in request.POST.EmailInterests %}checked="checked"{% elif not person.EmailInterests and not request.POST.EmailInterests %}{% endif %} />
                     New Product Releases
                     </label>
                  </div>
                  <div class="checkbox">
                     <label>
                     <input type="checkbox" name="EmailInterests" value="Promotions" {% if 'Promotions' in person.EmailInterests or 'Promotions' in request.POST.EmailInterests %}checked="checked"{% elif not person.EmailInterests and not request.POST.EmailInterests %}{% endif %} />
                     Promotions & Sales
                     </label>
                  </div>
                  <div class="checkbox">
                     <label>
                     <input type="checkbox" name="EmailInterests" value="Blog" {% if 'Blog' in person.EmailInterests or 'Blog' in request.POST.EmailInterests %}{% elif not person.EmailInterests and not request.POST.EmailInterests %}{% endif %} />
                     Latest from the Blog
                     </label>
                  </div>
                  <div class="checkbox">
                     <label>
                     <input type="checkbox" name="EmailInterests" value="Events" {% if 'Events' in person.EmailInterests or 'Events' in request.POST.EmailInterests %}{% elif not person.EmailInterests and not request.POST.EmailInterests %}{% endif %} />
                     Events
                     </label>
                  </div>
               </div>
            </div>
            <div class="form-group">
               <label for="interests" class="col-sm-3 control-label">How often would you like to hear from us?</label>
               <div class="col-sm-9">
                  <div class="radio">
                     <label>
                        <!-- Default value. -->
                        <input type="radio" name="EmailFrequency" id="email_frequency_0" value="All" {% if person.EmailFrequency == 'All' or request.POST.EmailFrequency == 'All' %}checked="checked"{% elif not person.EmailFrequency and not request.POST.EmailFrequency %}checked="checked"{% endif %} />
                        Twice per Week
                     </label>
                  </div>
                  <div class="radio">
                     <label>
                     <input type="radio" name="EmailFrequency" id="email_frequency_1" value="Weekly" {% if person.EmailFrequency == 'Weekly' or request.POST.EmailFrequency == 'Weekly' %}checked="checked"{% endif %} />
                     Once per Week
                     </label>
                  </div>
                  <div class="radio">
                     <label>
                     <input type="radio" name="EmailFrequency" id="email_frequency_2" value="Monthly" {% if person.EmailFrequency == 'Monthly' or request.POST.EmailFrequency == 'Monthly' %}checked="checked"{% endif %} />
                     Once per Month
                     </label>
                  </div>
               </div>
            </div>
            <div class="checkbox">
               <label>
               <input type="checkbox" name="$unsubscribe" value="true" />
               <span class="text">Unsubscribe me from all emails.</span>
               </label>
            </div>
            <div class="clearfix form-actions">
               <div class="pull-right">
                  <button type="submit" class="btn btn-default btn-primary">Update Preferences</button>
               </div>
            </div>
         </form>
         <footer class="footer">
            <p>
               © 2017 Company Name — <a href="https://www.klaviyo.com" target="_blank">Privacy Policy</a>
            </p>
         </footer>
      </div>
      <!-- /container -->
      <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
      <!-- Latest compiled and minified JavaScript -->
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
      <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.13.1/jquery.validate.min.js"></script>
      <script>
        $(function() {
            $('#preferences_form').validate({
                rules: {
                    $email: {
                        required: true
                    }
                },
                messages: {
                    $email: 'Please enter your email address.',
                    $first_name: 'Please enter your first name.',
                    $last_name: 'Please enter your last name.'
                }
            });
            // Toggle validation based on selection.
            $('input[name="$unsubscribe"]').on('change', function() {
                $('form .form-actions button[type="submit"]').toggleClass('cancel', $(this).is(':checked'));
            });
        });
        $('input[name="$unsubscribe"]').on('change', function(){
          $('input[type=checkbox]').not(this).prop('checked', false);
        });
        $('input[type=checkbox]').not('input[name="$unsubscribe"]').on('change', function(){
          $('input[name="$unsubscribe"]').prop('checked', false);
        });
    </script>
   </body>
</html>
```

### Set a hosted page's redirect after submission (Optional)

By default, after a hosted page (e.g., hosted preferences page) is submitted successfully, the user will be redirected to 1 of 2 places:

- If they've requested to unsubscribe, they'll be sent to your account's default unsubscribe confirmation page.
- If they've updated their profile (or done anything that's not an unsubscribe request), the user will be sent to your account's default preferences confirmation (success) page.

If you used the sample HTML above, this is reflected in the <body> as:

```
<!-- <input type="hidden"
name="$unsubscribed_url" value="/p/preferences_updated" /> -->
<!-- <input type="hidden"
name="$updated_profile_url" value="/p/preferences_updated" /> -->
```

To customize where someone is redirected to after submitting your hosted page, adjust the value="..." lines to your preferred URL(s) within the HTML.

### Add custom assets to hosted pages (Optional)

If you want to use your own CSS file, JS file, or images on your hosted page, upload them by clicking the ****+**** symbol next to **Assets** and reference them in the source code of the page.

Use the following tag to reference an asset you've uploaded to your Klaviyo account: `{% asset_url 'style.css' %}`

![source code of your consent page showing uploaded custom asset tag](https://klaviyo.zendesk.com/hc/article_attachments/30388426692507)

## Using the custom consent pages

You can replace each of your account's default consent pages with custom-coded pages so that all emails use these custom pages by default. Alternatively, you can configure a only 1 particular list to use custom-coded pages, so that only emails sent to that list would use the custom pages.

- If you have customized consent pages for a specific list, any emails sent to that list will use those unique consent pages.
- Any lists that you have not customized unique consent pages for will use your account's default consent pages. In addition, any email that is NOT sent to a specific list, including metric-triggered flow emails, campaigns sent to a segment, or [personal emails](https://help.klaviyo.com/hc/en-us/articles/115005246328-Email-a-Single-Person-using-Klaviyo), will also use your default consent pages.

### Change default consent pages to hosted pages

If you would like to replace 1 or more of your account's default consent pages (e.g., preference page, subscribe page, or email unsubscribe page) with custom-coded pages, follow these steps:

1. Click your company name in the bottom left corner of Klaviyo.
2. Select ****Settings****.
   ![Account tab in the bottom left corner with settings selected from the navigation menu](https://klaviyo.zendesk.com/hc/article_attachments/28723623382427)
3. Select ****Other**** from the top.
4. Click the 3 dots dropdown menu on the consent page you plan to replace, and select ****Use Hosted Page****.
   ![The Consent Pages tab in Klaviyo showing an the additional options menu open on an example preference page.](https://klaviyo.zendesk.com/hc/article_attachments/33232831319067)
5. In the dialog window that appears, select your custom page file and click ****Save****.

If you would like to use a custom page for flow emails or campaigns sent to a segment, you will have to switch your account's default consent pages to use your custom pages. Follow the same process as above to replace your default consent pages with custom-coded pages.

### Use custom consent pages for a list

You'll have to configure each individual list that you'd like to use a custom page for instead of the default consent pages.

1. Navigate to the list that you'd like to connect to a custom page.
2. Click the ****Subscribe & Preference Pages**** tab to see all of the editable consent pages for that list.
3. Under the consent page that you want to replace with a custom page, click the 3 dots dropdown menu and select ****Use Hosted Page****.
   ![The Subscribe & preferences pages tab for an example list in Klaviyo showing the additional actions menu open on the preferences page.](https://klaviyo.zendesk.com/hc/article_attachments/33232831322779)

   Note that you can choose to use a hosted page for all of the consent pages if you wish.
4. In the dialog window that appears, select your custom page file and click ****Save****.

In your emails, you should still use the standard Klaviyo unsubscribe and manage preferences tags (i.e., {% unsubscribe %} and {% manage\_preferences %}). These tags will populate as links in your live emails and will automatically bring recipients to your custom pages.

## Hosted pages FAQ

****Do I need to add any JavaScript to my page for this form to submit properly?****
Since your custom forms will be contained inside of a hosted page, you don't have to add any extra JavaScript or an action URL to the <form> to make it submit properly. As long as a hosted page is visited from an email sent via Klaviyo, it will automatically tie back to the correct contact.

****Does this page have to be in HTML?****
This page must be in HTML. You can include additional images, stylesheets, etc., either by linking to them or by adding a folder of included files.

****Can Klaviyo help me build a custom page?****
Klaviyo does not currently offer services to help build out custom code, nor do we provide support for custom code troubleshooting. The ****Hosted Pages**** feature is meant to provide a blank slate for [developers or code-savvy marketers](https://connect.klaviyo.com/).

Learn more about the customization capabilities with Klaviyo's built-in consent pages in [getting started with consent pages](https://help.klaviyo.com/hc/en-us/articles/115005251848-Getting-started-with-opt-in-related-pages-for-a-list).

## Additional resources

- [How to customize a list's unsubscribe page](https://klaviyo.zendesk.com/hc/en-us/articles/115005079627)
- [Understanding list growth tools in Klaviyo](https://klaviyo.zendesk.com/hc/en-us/articles/115005080327)
- [Understand custom hosted pages in Klaviyo](https://help.klaviyo.com/hc/en-us/articles/360057676272-Understand-custom-hosted-pages-in-Klaviyo)