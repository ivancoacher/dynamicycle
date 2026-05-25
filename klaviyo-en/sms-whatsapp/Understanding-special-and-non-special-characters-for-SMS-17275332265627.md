---
id: "17275332265627"
title: "Understanding special and non-special characters for SMS"
source_url: "https://help.klaviyo.com/hc/en-us/articles/17275332265627-Understanding-special-and-non-special-characters-for-SMS"
section: "Format your SMS messages"
category: "SMS"
category_slug: "sms-whatsapp"
klaviyo_updated: "2026-04-21T13:54:30Z"
language: "en"
---
## You will learn

Learn which characters are considered not special or special for SMS.

Special characters, which include emojis and certain types of text and symbols, shorten the message’s character limit from 160 to 70. They can also be difficult to tell apart from non-special characters.

****Why do special characters shorten the character limit?****

This is due to how SMS messages are encoded.

Before a message is sent, it encodes each character into bits of data that can be transmitted. Each character requires a certain number of bits to be encoded, and each SMS allows for a set number of bits.

SMS messages are encoded in either 7 or 16 bits via the following formats:

- ISO-8859-15 (7 bits)
  The default for all SMS messages. This format limits the number of characters to 160 and does not allow for special characters.
- UTF-8 (16 bits)
  Limited to 70 characters per message and allows for special characters and emojis.

****How many more characters do I get if I go over the first 70 characters?****

Technically, the second (and third and fourth) SMS segment can have 70 characters. Using a special character or emoji changes the way an SMS is encoded. Thus, the 70-character limit applies to every message segment for that SMS.

Note that when an SMS extends beyond 1 message, Klaviyo includes a header on the backend so that carriers know the 2 sends go together. This takes up a few characters, which is why you see that you are able to use 134 characters for 2 sends.

![](https://klaviyo.zendesk.com/hc/article_attachments/33627679862683)

## Non-special characters

Most non-special characters come from the GSM-7 character set (also called a “charset”), which includes:

- All Latin characters
- Numbers (0–9)
- Some Greek characters
- Some symbols and other characters

In some cases, capitalizing letters may affect whether they're counted as special or non-special characters. For instance, à, é, è, ì, ò, and ù are GSM-7 characters, but capitalizing them to À, É, È, Ì, Ò, and Ù makes them UCS-2 characters.

****I’m using all non-special characters, why did the character limit decrease?****

This is a common issue if you’re copying text and symbols from a third party. Sometimes a character will appear like a non-special character, but is actually from a special charset. The symbols look nearly identical, and it can be difficult to tell them apart.

|  |  |
| --- | --- |
| ****Special character**** | ****Non-special character**** |
| ‟ | " |
| ԁ | d |
| @ | @ |

Most of the time, lookalike special characters change to non-special characters before they’re delivered. However, this is not always the case, and it’s best to remove any accidental special characters.

Try re-typing your message directly in Klaviyo or using a text cleaner. If that doesn’t work, check that every symbol is actually considered non-special.

### Latin letters

Note that sometimes, only 1 version of a letter is accepted. If there’s no capitalized or lowercase version, the corresponding cell is blank.

|  |  |  |
| --- | --- | --- |
| ****Description**** | ****Capitalized**** | ****Lowercase**** |
| Latin letter a | A | a |
| Latin letter b | B | b |
| Latin letter c | C | c |
| Latin letter d | D | d |
| Latin letter e | E | e |
| Latin letter f | F | f |
| Latin letter g | G | g |
| Latin letter h | H | h |
| Latin letter i | I | i |
| Latin letter j | J | j |
| Latin letter k | K | k |
| Latin letter l | L | l |
| Latin letter m | M | m |
| Latin letter n | N | n |
| Latin letter o | O | o |
| Latin letter p | P | p |
| Latin letter q | Q | q |
| Latin letter r | R | r |
| Latin letter s | S | s |
| Latin letter t | T | t |
| Latin letter u | U | u |
| Latin letter v | V | v |
| Latin letter w | W | w |
| Latin letter x | X | x |
| Latin letter y | Y | y |
| Latin letter z | Z | z |
| Latin letter æ | Æ | æ |
| Latin letter sharp (German) | ß |  |
| Latin a with ring above | Å | å |
| Latin a with grave |  | à |
| Latin e with grave |  | è |
| Latin i with grave |  | ì |
| Latin o with grave |  | ò |
| Latin u with grave |  | ù |
| Latin e with acute |  | é |
| Latin o with stroke | Ø | ø |
| Latin a with diaeresis | Ä | ä |
| Latin o with diaeresis | ö | ö |
| Latin u with diaeresis | Ü | ü |
| Latin n with tilde | Ñ | ñ |
| Latin c with cedilla | Ç |  |

### Greek letters

The non-special Greek letters are listed below. Note that there is only 1 version of these characters.

|  |  |
| --- | --- |
| ****Description**** | ****Character**** |
| Greek gamma | Γ |
| Greek delta | Δ |
| Greek theta | Θ |
| Greek lambda | Λ |
| Greek xi | Ξ |
| Greek pi | Π |
| Greek sigma | Σ |
| Greek phi | Φ |
| Greek psi | Ψ |
| Greek omega | Ω |

### Numbers

|  |  |
| --- | --- |
| ****Description**** | ****Character**** |
| Zero | 0 |
| One | 1 |
| Two | 2 |
| Three | 3 |
| Four | 4 |
| Five | 5 |
| Six | 6 |
| Seven | 7 |
| Eight | 8 |
| Nine | 9 |

### Money signs

|  |  |
| --- | --- |
| ****Description**** | ****Character**** |
| Pound sign | £ |
| Dollar sign | $ |
| Yen sign | ¥ |
| \*Euro sign | € |
| Currency sign | ¤ |

\*Note that the Euro sign (€) counts as 2 characters.

### Symbols

|  |  |
| --- | --- |
| ****Description**** | ****Character**** |
| At symbol | @ |
| Low line | \_ |
| Ampersand | & |
| Asterisk | \* |
| Period (full stop) | . |
| Comma | , |
| Exclamation mark | ! |
| Inverted exclamation mark | ¡ |
| Question mark | ? |
| Inverted question mark | ¿ |
| Colon | : |
| Semi-colon | ; |
| Apostrophe | ' |
| Double quotation mark | " |
| Left parenthesis | ( |
| Right parenthesis | ) |
| Less than | < |
| Greater than | > |
| Equal sign | = |
| Plus sign | + |
| Hyphen or minus | - |
| Percent sign | % |
| Number sign (hashtag, pound) | # |
| Section sign | § |
| Forward slash | / |
| \*Backslash | \ |
| \*Left square bracket | [ |
| \*Right square bracket | ] |
| \*Left curly bracket | { |
| \*Right curly bracket | } |
| \*Vertical bar | | |
| \*Tilde | ~ |
| \*Caret or circumflex | ^ |

****\***** Any symbol marked by an asterisk counts as 2 characters in a text message.

## Special characters

Special characters are any other character or emoji that’s not listed in one of the tables above, including: À, á, â, ç, ê, É, È, Ì, î, í, Ò, ô, ó, Ù  and ú.

Any unicode character is considered special, even if it looks similar to a non-special character. Let’s use the example of double quotation marks.

- This is the non-special character: "
- These are special characters: «, “, ‟, ❝,〝, "

## How to check if your character is special or not

If you're not sure if your character is special or not, use [this message segment calculator](https://twiliodeved.github.io/message-segment-calculator/). Specifically, look at the **Encoding Used**:

- GSM-7 indicates there are no special characters.
- UCS-2 indicates there is at least 1 special character.
  ![Example of a special character in the message segment calculator](https://klaviyo.zendesk.com/hc/article_attachments/28713340971547)

## Additional resources

- [Understanding MMS image and GIF best practices](https://help.klaviyo.com/hc/en-us/articles/360041074911)
- [How to create and send an SMS campaign](https://help.klaviyo.com/hc/en-us/articles/360040039971)
- [How to use Klaviyo email and SMS together](https://help.klaviyo.com/hc/en-us/articles/360056849631)