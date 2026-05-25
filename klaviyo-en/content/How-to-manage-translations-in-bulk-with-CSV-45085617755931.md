---
id: "45085617755931"
title: "How to manage translations in bulk with CSV"
source_url: "https://help.klaviyo.com/hc/en-us/articles/45085617755931-How-to-manage-translations-in-bulk-with-CSV"
section: "Build and use templates"
category: "Content"
category_slug: "content"
klaviyo_updated: "2026-05-11T12:54:35Z"
language: "en"
---
You must have a paid Klaviyo account and Smart Translations enabled to use this feature.

Manage translations outside Klaviyo by exporting and editing a CSV file, then importing it back to update translations in bulk or collaborate with others.

## Export a CSV of your translations

Follow these steps to export the current translations for a single message:

1. Open the message you want to update (campaign email, flow email, SMS, WhatsApp message, etc.).
2. Click ****Translate**** to open the translation editor.
3. In the translation editor, open the actions menu and click ****Export CSV****.
   ![Translation editor with the Export CSV option highlighted in the actions menu](https://klaviyo.zendesk.com/hc/article_attachments/45177653196699)
4. In the export modal, you have the option to select between a ****Smarting CSV**** or a ****CSV****

![](https://klaviyo.zendesk.com/hc/article_attachments/45987097006619)

### Exporting Smartling CSV

1. Your browser downloads a CSV file that includes:
   1. The following default Smartling directives:****# smartling.first\_row\_header=TRUE****
      ****# smartling.paths=2****
      ****# smartling.source\_key\_paths=1****
      ****# smartling.translations\_in\_columns=TRUE****
   2. ****block\_id**** – the unique identifier for each translatable string in this message.
   3. ****Source language code**** (e.g., en) – the original source text for that string.
   ![Sample translation CSV in Google sheets showing smartling directives, block_id, source language column code, for one row.](https://klaviyo.zendesk.com/hc/article_attachments/45987074722971)

You can use this file as-is to import your strings to Smartling. Smartling automatically parses the CSV, extracts the strings, and lets you trigger translation jobs.

After the job finishes, download the resulting CSV and import it back using the ****import**** button.

### Exporting a Simple CS

1. Your browser downloads a CSV file that includes:
   1. ****block\_id**** – the unique identifier for each translatable string in this message.
   2. ****source**** – the original source text for that string.
   3. ****Language columns**** – one column per language, named with its language code (for example, en, fr, es-MX).
   ![Sample translation CSV in Google sheets showing block_id, source, and language column for multiple rows.](https://klaviyo.zendesk.com/hc/article_attachments/45177659814683)

You can now open this file in Excel, Google Sheets, or another spreadsheet editor.

## Update the CSV

When you edit the CSV, you only need to work in the language columns.

Do not edit, add, or delete any values in the block\_id column. If a row has an invalid or missing block\_id, that row is ignored during import and its translations are not updated.

### What you can safely change

In the CSV:

- Update existing translations by editing the appropriate language column.
- Add missing translations by filling in empty cells for a language column.
- Leave a language’s values unchanged if you do not want to update that language.
- Add one or more ****new language columns****:
  - Use a valid BCP‐47 language code (for example, fr-CA, de, ca).
  - On import, these languages are added to the translation editor for this message if they are supported.

### What you should not change

Avoid the following:

- ****Do not edit or delete block\_id values.****
- ****Do not add rows.**** Each row must continue to map to an existing translatable string in the message.
- ****Do not change the source values**** in the CSV:
  - To change the source content, edit the message directly in the Klaviyo editor, then export a new CSV.
- ****Do not rename the required columns**** (block\_id, source, and the language columns).
- ****Do not change the file format****:
  - Keep the file as a .csv file.
  - Save in ****UTF‐8**** encoding.

### Handling empty cells

If you clear out a translation cell in the CSV and leave it empty:

- The import treats that empty string as a value.
- The existing translation for that cell is overwritten with an empty value. This can effectively remove a translation.

If you want to ****avoid changing a translation****, leave its existing value in the CSV or remove that language column entirely before importing.

When you are done editing, save the file as a UTF‐8 encoded .csv.

## Import the CSV

After you have updated and saved your CSV:

1. Return to the translation editor for the same message.
2. Click ****Import CSV****.
3. In the import modal, either:
   ![Import CSV modal in the translation editor with Select file and drag-and-drop options.](https://klaviyo.zendesk.com/hc/article_attachments/45177653207835)

   - Click ****Select file**** and choose your CSV, or
   - Drag and drop your CSV into the upload area.
4. Klaviyo runs a ****validation “dry run”**** and shows:
   ![Import summary dialog showing counts of updated, unchanged, and ignored rows, with warnings listed above the Import button.](https://klaviyo.zendesk.com/hc/article_attachments/45177653210779)

   - A ****summary**** of how many rows will be updated, unchanged, or ignored
   - Any ****warnings or errors**** it detected
5. Review the summary and warnings carefully.
6. If everything looks correct, click ****Import**** to apply the changes.

During validation, Klaviyo also checks for:

- File size and row limits (for example, files larger than 10MB will be rejected).
- Required columns (such as block\_id, source, and at least one language column).
- Language codes that are not recognized or not supported by the channel.
- Empty translation values and other potential issues.

If validation fails, you see an error message and can select a new file without making any changes to your translations.

## Understand import results

After validation, the import summary shows what will happen if you proceed.

### Summary counts

The summary can include counts like:

- ****Updated**** – the number of rows where at least one translation value will change.
- ****Unchanged**** – rows that are present in the CSV but where all values match what is already stored.
- ****Ignored / skipped**** – rows that will not be imported (for example, because the block\_id does not exist in this message or required data is missing).

Counts are calculated per row, not per language. For example, if a CSV has two rows and two language columns:

- If one row updates in one language, the ****Updated**** count is 1.
- If one row updates in both languages, the ****Updated**** count is still 1.
- If both rows update in one or all languages, the ****Updated**** count is 2.

## Best practices

To keep your translation data accurate and easy to manage:

1. ****Start from the latest export.**** Avoid reusing older CSVs, especially after you change content or languages in the message.
2. ****Keep a backup of each export.**** Save a copy of the CSV before making changes so you can roll back if needed.
3. ****Coordinate with translators.**** Explain which columns they can edit (language columns only) and which columns they must not change (**block\_id**, **source**).
4. ****Work in smaller batches if needed.**** If your file is very large, consider splitting work across multiple messages or running several smaller imports.
5. ****Use supported language codes.**** When adding new language columns, use supported BCP-47 codes from the **Smart Translations** article to avoid “unprocessable” languages.

## Resolve validation warnings and import errors

If you see warnings or errors during import validation, review the sections below to understand what they mean and how to fix them.

****"Required columns are missing."****

****What it means:**** One or more required columns (**block\_id** or **source**) are missing or renamed.

****What to do:**** Make sure the CSV includes **block\_id** and **source** columns. If you copied data into a new sheet, confirm that the header row matches the original export.

****"You have empty translation values. Empty strings will be treated as values."****

****What it means:**** Your CSV has empty translation values, and empty strings will be treated as values.

****What to do:**** If you proceed, those empty cells overwrite any existing translations for that key and language. If you want to leave those translations unchanged, restore the previous values or remove that language column and re-import the file.

****"<count> key(s) does not exist in your project and will not be included in the import."****

****What it means:**** Some **block\_id** values in your CSV don’t exist for this template (for example, if **block\_id** values were edited manually).

****What to do:**** Those rows are ignored, and translations for those keys don’t change. To resolve this, remove those rows from the CSV or export a fresh file if needed.

****"Your file contains duplicate keys with conflicting values. The first value will be used."****

****What it means:**** Two or more rows in your CSV have the same **block\_id** values (for example, if rows were duplicated by mistake).

****What to do:**** The values of the first row are used and the remaining duplicate rows are ignored. To resolve this, remove the duplicate rows from the CSV or export a fresh file if needed.

****"Multiple columns resolve to the same language. Only the last column will be used and the others will be ignored."****

****What it means:**** Two or more columns in your CSV have the same language code or resolve to the same language (for example, if a language column was duplicated by mistake).

****What to do:**** The values of the last duplicate column are used and the remaining duplicate columns are ignored. To resolve this, remove the duplicate columns from the CSV or export a fresh file if needed.

****"Your file contains columns with language codes that are not supported by this channel: <invalid language code>. These will be ignored but valid locales will be imported."****

****What it means:**** A column header in your CSV uses a language code that isn’t supported or recognized.

****What to do:**** To add a new language, use one of the supported BCP-47 codes from the **Smart Translations** documentation. Columns with unsupported codes are ignored.

****"You have languages in your file that are not in your project. The following languages will be added to your translation editor: <language detected>."****

****What it means:**** Your CSV includes language columns that are not currently part of this template.

****What to do:****

- If you want to add those languages, review the list and click ****Import**** to add them to the translation editor.
- If you don’t want to add them, remove those columns and re-import the file.

****"No locale columns found."****

****What it means:**** The CSV includes **block\_id** and **source** columns but no other column header was detected.

****What to do:**** Add at least one supported language column and try again.

****"No valid locale columns found."****

****What it means:**** The CSV includes **block\_id** and **source** columns but no valid language columns.

****What to do:**** Add at least one supported language column and try again.

If you see only warnings and understand their impact, you can proceed with the import. If you see an error, you must correct the CSV and re-upload it before continuing. If you continue to see errors, export a fresh CSV from the translation editor, make minimal changes, and try another import to isolate the issue.

If you continue to see errors after checking these items, export a fresh CSV from the translation editor, make minimal changes, and try another import to isolate which change is causing the problem.