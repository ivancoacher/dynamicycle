---
id: 5306587861531
title: "How to indicate the country for an SMS import"
source_url: "https://klaviyo.zendesk.com/hc/en-us/articles/5306587861531-How-to-indicate-the-country-for-an-SMS-import"
section: "Import SMS contacts"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:55:03Z"
language: en
---

## You will learn

Learn how to indicate the country in a CSV file with SMS profiles.

In the instructions below, we use Google Sheets to indicate the country in an SMS list upload. This can be accomplished using other programs too, but the instructions may differ.

## Before you begin

You can only import SMS consent in countries [where Klaviyo SMS is available](https://klaviyo.zendesk.com/hc/en-us/articles/4402914866843).

Before adding in the country to a CSV, you should:

- Copy your CSV into a program such as Google Sheets.
- Make the first column in the CSV email (preferred, if available) or phone number.

## Options for indicating the country

In the table, we outline:

- Full names of the available countries
- The country code
- Accepted ways you can shorten the country names in your CSV (if you don’t have the full name)

|  |  |  |
| --- | --- | --- |
| ****Country name**** | ****Country code**** | ****Accepted shortened name(s)**** |
| Australia | +61 | AUS |
| Austria | +43 | AT |
| Belgium | +324 | BE |
| Canada | +1 | CAN |
| Denmark | +45 | DK |
| Finland | +358 | FI |
| France | +33 | FR |
| Germany | +49 | DE |
| Hungary | +36 | HU |
| Ireland | +353 | IE |
| Italy | +39 | IT |
| Luxembourg | +352 | LU |
| Netherlands | +31 | NL |
| New Zealand | +64 | NZ |
| Norway | +47 | NO |
| Poland | +48 | PL |
| Portugal | +351 | PT |
| Spain | +34 | ES |
| Sweden | +46 | SE |
| Switzerland | +41 | CH |
| United Kingdom | +44 | GBR |
| United States of America | +1 | US, USA, United States |

****What is a country code?****

A country code is a number at the beginountry codes are a specific number at the beginning of a phone number.

In the United States and Canada, the country code is the number 1 and phone numbers are 10 digits. So for the example number of 1 (234) 567-8910: 1 is the country code.

## Indicate the country for an SMS import

The best way to indicate the country in a CSV depends on where your contacts are located and what information your previous SMS provider exports.

Choose the first option that best describes your situation:

- [I have a country code at the beginning of every phone number](#h_01G0CXA7WMB4GY9QGBZTC2A4QD) (most common).
- I don’t have a country code and my contacts are from:
  - [A single country](#h_01G0CXAWXCFS6ZRAGTP9JGFWWQ).
  - [Only the US and Canada](#h_01G0CXB831W115FM27KMY5JKJC).

If none of these options apply to you, the only option is to search by phone number and apply the country that way. However, in most cases, the country code is already in the CSV.

## Country code is included

If you have the country code before your phone numbers, you only need to add a plus sign before the number, even if your contacts are from multiple, different countries.

Watch our video or scroll down for instructions.

![](https://fast.wistia.com/embed/medias/ld30gq77eh/swatch)

1. Highlight the phone number column.
   ![Highligting the phone number column in a CSV](https://klaviyo.zendesk.com/hc/article_attachments/28717879988635)
2. Click ****Insert > Columns****.
3. Select ****Insert 1 column left****.
   ![Option to insert 1 column to the left of the highlighted column](https://klaviyo.zendesk.com/hc/article_attachments/28717879990299)
4. Name the new column "Phone Number."
5. Add the following: ="'+"&C2

   - Note: replace C2 with the first cell that contains a phone number.![Inserting a formula to add an apostrophe and plus sign before the phone number](https://klaviyo.zendesk.com/hc/article_attachments/28717852535963)
6. Highlight the rest of the column.
7. Click ****Edit > Paste**** to format the rest of the phone numbers.
8. Highlight and then copy the new column.
9. Go to ****Edit > Paste Special****.
10. Select ****Values Only****.
    ![Paste special options when Values Only is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28717852529051)
11. Delete the original phone number column (the one without the plus signs).

    - Note that the apostrophe may disappear if you click into another cell.![Example of a spreadsheet that has the correct formatting](https://klaviyo.zendesk.com/hc/article_attachments/28717880007707)
12. Click ****File > Download > Comma Separated Values (.csv)****.

## Contacts are all from 1 country

If your list contains SMS profiles that are all from the same country, follow the steps below:

1. Click into an empty column in your spreadsheet.
2. Name that column “Country."
3. In the first cell under that title, write in the country (e.g., Canada or CAN).
   ![Adding the name of the country in a new column](https://klaviyo.zendesk.com/hc/article_attachments/28717879991963)
4. Copy the country’s name/abbreviation.
5. Highlight the rest of the cells in that column.
6. Click ****Edit > Paste****. All cells in that column should now show the country name.
   ![Option for pasting the country's name in highlighted cells](https://klaviyo.zendesk.com/hc/article_attachments/28717879997979)
7. Click ****File > Download****.
8. Choose ****Comma Separated Values (.csv)****.

## Contacts are only in the US and Canada

If your contacts are all from either the US or Canada, you can add the country code to the phone number, which is the same for both countries.

To do this, follow these steps:

1. Highlight the phone number column.
2. Click ****Insert > Columns****.
3. Select ****Insert 1 column left****.
   ![Inserting a column to the left of the phone number column](https://klaviyo.zendesk.com/hc/article_attachments/28717879988635)
4. Name the new column "Phone Number."
5. In the next cell, type the following: "'+1"&C2

   - Replace the 1 with the correct country code.
   - Replace C2 with the first cell that contains a phone number.![Adding in a formula to combine an apostrophe, plus sign, and the country code with the phone number](https://klaviyo.zendesk.com/hc/article_attachments/28717852540443)
6. Highlight the rest of the column.
7. Click ****Edit > Paste**** to format the rest of the phone numbers.
8. Highlight and then copy the new column.
9. Go to ****Edit > Paste Special****.
10. Select ****Values Only****.
    ![Paste special menu when Values Only is highlighted](https://klaviyo.zendesk.com/hc/article_attachments/28717852529051)
11. Delete the original phone number column (the one without the plus signs).
    ![Example of a CSV for an SMS import](https://klaviyo.zendesk.com/hc/article_attachments/28717880007707)
12. Click ****File > Download > Comma Separated Values (.csv)****.

## Outcome

You’ll now have either the name of the country or the country code for every phone number in your CSV. You can now upload the contacts as either subscribed or unsubscribed in Klaviyo.

Check out more how-tos for SMS CSVs: