<h1>How to import geofences using a CSV upload</h1>

## You will learn

Learn how to import multiple geofence locations into Klaviyo by uploading a CSV file.

## Table of contents

To import geofences using a CSV upload:

1. [Create your CSV file](https://docs.google.com/document/d/19AiD4EFBohtGGgMzmpLFNwwnY8CIIM2vp1azP2EfBww/edit#create-your-csv-file).
2. [Upload your CSV file](https://docs.google.com/document/d/19AiD4EFBohtGGgMzmpLFNwwnY8CIIM2vp1azP2EfBww/edit#upload-your-csv-file).
3. [Review your import history](https://docs.google.com/document/d/19AiD4EFBohtGGgMzmpLFNwwnY8CIIM2vp1azP2EfBww/edit#review-your-import-history).

## Create your CSV file

Before you upload, you need a properly formatted CSV file. Each row in the file represents one geofence location. Every location requires columns for:

- ****Name****
- ****Address**** OR ****Latitude**** and ****Longitude****

  You can also include any of the following optional columns:
- ****Radius**** — the size of the geofence area in meters
- ****Description****
- ****Status**** — **active** or **inactive**; whether the geofence is enabled for triggering events
- ****Enter**** — **true** or **false**; whether to trigger an event when a profile enters the geofence
- ****Exit**** — **true** or **false**; whether to trigger an event when a profile exits the geofence

![Table with columns Name, Address, and Radius. Row 1: My First Store, 123 Main St, Anytown, NY 12345, 500.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/61bee3e4148007b66b5aca09ac89d374163c32ce-848x100.png)

You can download a pre-formatted template directly from the import flow. Navigate to ****Audience**** > ****Geofences**** > ****Import locations**** and select ****Create your own template****. In the modal that appears, choose the columns that you want to include and then select ****Download****. Open the downloaded file in any spreadsheet tool, such as Excel or Google Sheets, and fill in your location data. Then save the file as a .csv, .text/csv, or.applications/csv.

![A dialog box for downloading a CSV template, offering column selections like Name and Latitude/Longitude, with a "Download" button.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/751fbf43bfa0ed6d9569eb5352ba7107a7f8c350-1448x880.png)

## Upload your CSV file

Once your file is ready:

1. Navigate to ****Audience**** > ****Geofences****.
2. Select ****Import locations****.
3. On the ****Upload locations to create geofences**** screen, drag and drop your file into the upload area, or click ****Select file**** to browse for it.
4. Once the file has been updated, select ****Next****.
5. Map your CSV columns to geofence fields in Klaviyo.
   ![Data import mapping screen showing CSV columns 'Name', 'Address', 'Radius' mapped to corresponding fields with sample data. 3/3 items selected for import.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/7d632d3b57d8d8717c092692002a2404c5e9c4d7-866x332.png)
6. When all mappings look correct, select ****Next****.
7. Select default values for any geofence properties that are not included in your CSV or that are blank in a given row.
   1. The map on the right side of the screen gives you a visual preview of the geofence radius. You can type a sample address into the search bar above the map to see approximately how large the geofence will appear in a real location.
      ![A settings panel titled "Apply defaults" for geofences, with "Enter event: True", "Exit event: False", "Status: Active", and "Radius: 500 meters" selected.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/68943d9928260257f3eccdaa2f0b6d59248be1de-982x1296.png)
8. When your defaults are set, select ****Import****.

## Review your import history

After you start an import, you can track its status in ****Import history****. Each entry shows the date and time of the import, how many locations were imported, and the result:

- ****Complete**** — all locations imported successfully
- ****Partial complete**** — some locations imported, but others failed; select ****Download failed rows**** to get a CSV of the rows that did not import, which you can correct and re-upload
- ****Failed**** — no locations imported

![Dashboard of 'Imports in the last 7 days', showing one complete (1/1 locations) and one partially complete (1/4 locations) import entry.](https://cdn.sanity.io/images/6ct6b26e/help-center-prod/c3e56fa5ce70ca6ddb7d97a57738f7b1e22e1a08-1224x584.png)

Your import may take anywhere from a few seconds to a few minutes, depending on the size of your file. You can navigate away from the page, and the import will continue in the background.

## Best practices

- Keep location names descriptive and consistent. Klaviyo uses the ****Name**** field as the primary identifier, so clear names make it easier to manage your geofences later.
- Use the ****Latitude/Longitude**** columns, instead of ****Address,**** when you need precise placement, such as for a specific entrance to a building or a location within a large complex.
- Start with a small test file of two or three locations before importing a large batch. This approach lets you confirm your column mapping and defaults are correct before committing to a full upload.
- Review the failed rows report after any partial import. Common issues include malformed addresses, unsupported values in the ****Status**** or ****Enter/Exit**** columns, or missing required fields.

## Outcome

After a successful import, your locations appear in the ****Locations**** section of Klaviyo with the status and settings you configured. You can use these geofences in flows and segments to trigger messages based on your profiles’ locations.
