<h1>How to create or clone a private API key</h1>

You must be an Owner or Admin to create, clone, or delete a private API key.

## You will learn

Learn how to create a private API key, which is a unique identifier used for API calls, as well as define a scope.

Both private API keys and scopes help you protect your and your customers’ data by limiting what third parties can access.

## About private API keys and scopes

When you make an API call, it allows one software to connect to another. This connection allows a software to request, edit, or add information to the other.

A private API key makes sure that this request has the right permissions (i.e., that it came from an authorized user, account, or program). Think of it like a house key: it lets you and your family in, but keeps out everyone else.

Including a scope for a private API key adds another layer of authorization, limiting what specific elements a third party can access. Scopes are similar to a hotel key, only giving you access to certain areas (like your room or the gym) and not the whole building.

### Types of scopes

When you create a private API key, you must select its scope. In other words, you must decide whether you want a third party to:

- Not have any access to an API endpoint.
- View all data for an API endpoint, but not be able to make changes (also called “read-only”).
- Create, delete, and make other changes to anything associated with that endpoint (also called “full access” or “write access”).

For example, say you want to [add subscribers to a Klaviyo list](https://developers.klaviyo.com/en/reference/create_list_relationships) from a third-party software. In that case, you must have full (write) access to the API endpoints for lists, profiles, and bulk subscribing profiles. However, the third party does not need access to any other endpoint.

You can learn about [Klaviyo’s APIs](https://developers.klaviyo.com/en/reference/api_overview) and see the[available scopes for each endpoint](https://developers.klaviyo.com/en/docs/authenticate_) on the Developer Portal.

## Before you begin

Please note the following:

- After you create a private API key, you cannot:
  - View the private API key again.
    - Tip: securely save private API keys and note down what you want to use them for, such as in a password manager.
  - Add or edit its scopes.
    - If you need to change scopes, the only option is to delete the original private API key and then create a new one with the correct scope.
- Private API keys have full access by default.

If you're not sure which API endpoints, scopes, or permissions you need, please contact a developer or reach out to a[Klaviyo partner](https://connect.klaviyo.com/) for help.

## Create a private API key

You will not be able view a private API key after creating it. Instead, you should treat private API keys like a password: only sharing these keys with parties you trust and saving them in a secure place, such as a vault or password manager.

1. Click your organization name in the bottom left.
2. Navigate to ****Settings****.
3. Click ****API keys****.
   ![API keys tab in account settings](https://klaviyo.zendesk.com/hc/article_attachments/28723522966299)
4. Click ****Create Private API Key****.
5. Name the API key.
6. Choose the scope you want to give the API key:

   - Read-only
   - Full
   - Custom![Page to create a private API key with a scope](https://klaviyo.zendesk.com/hc/article_attachments/28723522963355)
7. Select ****Create****.

Now, when you share a private API key, the third party will only have access to the information you defined in the scope.

## Using queries

Queries are used in advanced scenarios. If you are not already familiar with queries or how to use them, we recommend working with a developer.

#### Include

Note that if you try to use the `include` query, you will have to change the format from what’s listed above.

For example, the profiles endpoint is **/api/profiles**.

However, if you add the include query parameter (**/api/profiles?include=list**), you will also need **list:read** or **list:full access**, depending on what type of API call you’re making.

#### Scopes

Using the `scopes` parameter, you can create a URL parameter to autofill in what scope access you need for your private API key.

In the scopes query, include a comma-separated list of the scopes you want to pre-select.

An example URL is:
**https://www.klaviyo.com/create-private-api-key?scopes=campaigns:read,campaigns:write**

Navigate to our Developer Portal to see the [scopes you can use in this query](https://developers.klaviyo.com/en/docs/authenticate_).

## Clone a private API key

With private API keys, cloning allows you to create a new key that has the same scopes and permissions as the original key.

Note that:

- Cloning does not generate the same key as the original private API key.
- You cannot re-name a cloned API key; it has the same name as the original key.

To clone a private API key:

1. Navigate to the ****API keys**** tab.
2. Click the 3-dot menu next to the key you want to clone.
3. Select ****Clone > Clone****.
   ![Menu to clone or delete a private API key](https://klaviyo.zendesk.com/hc/article_attachments/28723544939931)
4. Copy or download the new private API key and store it in a secure place.
5. Make sure to delete your old key if it's no longer needed.
