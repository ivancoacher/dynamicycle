<h1>Understanding MMS image and GIF best practices</h1>

## You will learn

Learn best practices for sending images and GIFs in text messages so that they display nicely to recipients.

### Why follow MMS best practices?

A variety of factors affect how an image or GIF looks on a recipient’s phone, including the wireless carrier, type of phone (iOS or Android), and the phone version.

By following MMS best practices, you can maximize your chances of the media looking good for all of your recipients.

## Before you begin

When you add an image or GIF to a text message, the message automatically turns from an SMS into an MMS.

Please note the following about MMS messages:

- You cannot change the position of the image in an MMS, and it may appear differently on iOS and Android devices.
- MMS is only available for certain countries and [sending number types.](https://help.klaviyo.com/hc/en-us/articles/4402914866843)
  - United States: toll-free numbers and short codes.
  - Canada: toll-free numbers.
  - Australia: long codes.

Always A/B test MMS against SMS messages for your audience.
On average, SMS tends to perform the same or better than MMS messages, but MMS costs more credits. Learn more about the [SMS and MMS credit system](https://help.klaviyo.com/hc/en-us/articles/13502982552347).

## Supported media types

Klaviyo supports the following media types for MMS messages:

- PNG
- JPEG
- GIF

Other file types (including MP4 and WebP) are not available for MMS. For instance, you will either not be able to attach this file to a message (like with MP4s) or mobile carriers may refuse to deliver your message (such as with WebP images). You can, however, upload a WebP file and opt to have Klaviyo convert it to an PNG file for you.

If you choose to upload an image, Klaviyo's [automatic image compression](https://help.klaviyo.com/hc/en-us/articles/115005253688#h_01JVN2QQXD9N2QT2MQ9D7PGX6S) tool optimizes clarity and ensure fast load times.

### PNG vs. JPEG

Both PNG and JPEGs have their own advantages and disadvantages:

- PNGs:
  - Are never blurry or distorted.
  - Keep all data in the image, so always appear the same no matter how many times it’s edited.
  - Can have transparent backgrounds (although this is not recommended for MMS images).
- JPEGs
  - Can be resized easily.
  - Lose data every time the image is made smaller, so can become blurry.

In short, use PNG when possible. If you have a larger-sized image that you need to make smaller, use a JPEG.

****Why are PNG and JPEG images different?****

The differences between PNG and JPEG are the result of how these images get compressed. Images use one of two types of compression processes: lossy or lossless.

- ****Lossy****
  Images permanently delete data as they’re resized.
- ****Lossless****
  Don’t lose any data when the image is edited, so they always look the same and don’t become blurry or distorted.

## File size limit

All images and GIFs must be under 600 KB.

If the file size is larger than 600 KB, the image or GIF may be compressed and distorted due to carrier constraints. Keeping your media under 600 KB ensures that recipients see the media the way you want it to appear in the highest quality possible.

Further, if a message has an image or GIF exceeding 600 KB, the message may not be delivered.

![SMS with image.jpg](https://klaviyo.zendesk.com/hc/article_attachments/28720847978779)

****Tips to reduce the file size****

Klaviyo has an [automatic image compression tool](https://help.klaviyo.com/hc/en-us/articles/115005253688#h_01JVN2QQXD9N2QT2MQ9D7PGX6S) built in to the upload process. When you upload an image, you'll see both the original and compressed versions with file sizes and percentage difference. Use the toggle to choose which version to upload. Klaviyo will recommend one, however you can override it if the compressed version loses clarity. Alternatively, you can export the file as a JPEG, and [use a program to reduce the file size](https://www.makeuseof.com/how-to-reduce-jpeg-file-size/).

If you need to make a GIF smaller:

- Use cuts (rather than fades), as cuts can decrease the size of a GIF by up to 50%.
- Decrease the number of frames per second.
- Add a color overlay, which decreases how many colors are in the GIF.

## Ratio

Your images and GIFs should not be overly wide or tall. Phones adjust multimedia to fit the width of the text message, so a ratio exceeding 9:16 (or 16:9) may look distorted.

Generally, images and GIFs can be in any of the following formats.

|  |  |  |
| --- | --- | --- |
|  | Ratio | Example sizes |
| Square | 1:1 | 480 x 480, 600 x 600 px |
| Portrait | 9:16 | 480 x 640, 1080 x 1920 px |
| Landscape | 16:9 | 500 x 375, 1920 x 1080 px |

As for which to choose, portrait tends to be the best option, followed by square. Portrait-sized media look good on most devices. This format is unlikely to be cut off or cropped because all media adjusts based on the width of the message.

## GIF length

While GIFs can be anywhere between 0 and 60 seconds, [GIPHY](https://support.giphy.com/hc/en-us/articles/360019914771-GIF-Creation-Best-Practices) recommends making your GIFs 6 seconds or less.

## Best practices

There are a few dos and don’ts for creating images and GIFs for MMS. If you don’t follow these best practices, your image can appear differently than you intend or look low quality.

### Dos

Check that your image or GIF has:

- ****High color contrast****
  Ensures the image on top and its background are distinct from each other, so the image doesn’t look blurry or as if it’s one solid color.
- ****High gradient contrast****
  If there’s a gradient, make sure the colors in the gradient are not too close to each other. Otherwise, it might appear like a solid-color image.

### Don’ts

Do not include any of the following in your images or GIFs:

- ****Transparent backgrounds****
  Within the message thread, the transparent background looks to be solid, with a random color selected as the background. Thus, recipients won’t see your image the way you intended, and it may look blurry or like a solid-color image.
- ****Borders****
  Some iOS devices cause borders to appear off-center from the image.
- ****Opacity transitions (GIFs)****There are 2 reasons for avoiding opacity transitions: they may show as random colors and can result in a larger file size.

## Additional resources

- Learn about the [differences between MMS and SMS](https://help.klaviyo.com/hc/en-us/articles/360041075091)
- Find out how to [create and send an SMS or MMS campaign](https://help.klaviyo.com/hc/en-us/articles/360040039971)
- Learn how to [add a dynamic image to an MMS](https://help.klaviyo.com/hc/en-us/articles/1260806102230)
