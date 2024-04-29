# how to design<br>an edition of *lipu tenpo*

Welcome to the *selo* repository. It contains all the files you need to make your own edition of *lipu tenpo*. This file has the instructions you need to make one.

This document is not yet complete. jan Kasape, the designer, is working on it. The instructions may also change over time.

## preparations

To make an edition of *lipu tenpo*, you need
1. Scribus (version 1.5.8)
1. a vector editor like [Inkscape](https://inkscape.org)
1. `git`

## working with Scribus

Scribus is the main tool that you will use. This section contains some tips for your workflow.

### the scrapbook

### panes

Properties, Item Properties, Align and Distribute, Scrapbook, TODO

TODO Show margins, boxes, text flow, rulers relative to page. Toggle these options all on or off using *F11*.

## preparing the files

Clone the *selo* repository onto your device. If you already have the edition, ensure it is up-to-date using `git pull`.

If you make a new edition, TODO.
If you make a different version of an edition, make its folder.
In the root of the directory, make a new folder for the edition. Its name must be the name of the edition. For instance, `/nanpa lipu`. In the folder of the edition, create three folders: `ijo`, `sitelen`, and `toki`.

In the

In addition, you must know the following:


1. the articles in plaintext form
1. the titles of the articles
1. the authors of the articles
1. the name of the category in which each article is
1. the images that the articles use
	1. a greyscale version
	1. a coloured version
		- *If the image uses colour; otherwise, use only a greyscale version.*
		- *The coloured version must have the same dimensions as the greyscale version, and the positioning must be identical.*

TODO use the files that you need for all editions, move them to `/ali`

If you use Inkscape, copy the file `/lipu-tenpo.gpl` to where Inkscape stores its palettes, which is `~/.config/inkscape/palettes`. Select it using TODO in Inkscape.
Copy the template file TODO into the folder of the edition.
The palette is: TODO table

## an article

### the text

import

### images

text wrap
positioning: integers. this is for the greyscale version.

### footnotes

Footnote in the text: regular letter (or superscript? TODO), and apply the style *nanpa lili sewi* TODO.

### title

### tilte background

Inkscape, use spine path TODO.

## the cover

Change the text in the textbox to the name of the edition. The textbox is positioned TODO.

### the image

The proportions of the front-cover image are preferably TODO.

The front-cover image is usually in SVG format, because jan Simo usually draws it.

## the second page

The second page of an edition has four parts.

### table of contents

### *jan pali*

The *jan pali* section contains the names of all people who contributed to the edition.

For each part, the names are sorted alphabetically, that is: `a e i j k l m n o p s t u w`,
and the pseudo-letter ‹end of word› goes before all of them, as usual.
But we use some extra rules, because, in Toki Pona, the structure of a name is *\[one or more nouns\] \[one or more proper names\]*, where a noun is lowercased and the first letter of a proper name is capitalised.

These are the rules:

- Sort by proper name, not noun.
	- jan Kasape < akesi Lipamanka < akesi kon Nalasuni
- If two people have the same proper name, but a different headnoun, break the tie using the noun.
	- jan Temi < mu Temi < mun Temi < jan Temili < mun Temili < pan Temili
- If a name contains multiple proper names, ignore the spaces between them.
	- jan Ke < waso Keli < jan Ke Tami < jan Kewi

- If different people with the same name contributed, include them both.

TODO add no-break spaces in the names and after `<`.

If a name does not follow the structure *\[one or more nouns\] \[one or more proper names\]*, then do what makes most sense.

If someone prefers their proper name to be spelt with a lowercase letter, then treat it as if it were capitalised.
- jan Nalu < soweli nata < palisa jelo Natan

If a name contains only a headnoun, treat it as a name.
- jan Lakuse < lipamanka < jan Lokan

But if a name consists of multiple words and no proper name, many orderings may make sense.
You might want to ignore particles like ‹pi›, and put ‹jan pi nimi ala› before TODO, such as in *nanpa TODO*.

jan Nalu ? jan pi nimi ala

Once the names are sorted, do the following:

- Separate the names with a `+`. It resembles the ‹en› of the *sitelen pona* writing system.
- Put a space before the `+`, and a no-break space after the `+`.
- Replace each space in a name with with a no-break space.

A no-break space is the symbol ` `.

- *Compose key + Space + Space*, or *Control + Shift + `u`, `A0`, Return*.
- *Alt + TODO*
- In Scribus, TODO

If you don’t want to type it, break the paragraph manually with soft breaks. These move to the next line without starting a new paragraph. In Scribus, and in many other places too, you can insert a soft break with *Shift + Return*.

- no-break spaces between ‹li alasa e pakala toki.› and so forth.

### introduction by jan Sonatan

Use an en dash (`–`).

- *Compose key + `-` + `-` + `.`*
- *Alt + TODO*
- In Scribus, TODO


### legal notice

Ensure that the year of publication is correct.

## checklist before publishing

- manual adjustment: arrows, pini, table of contents

- images: use integers for scaling and panning, because you have to remember them

- checks
1. order
	1. Are all the page numbers correct?
	1. Where there are multiple articles on one page, does the order of articles correspond to the order in the table of contents?
		- If not, move some titles to the foreground.
		- select the title
	1. Does the category name next to the page number correspond with the category name of the article on it?
		- If the category changes in the middle of a page, use that category.
		- If there are multiple categories.
	1. Does each non-poetry article start with an arrow and end with a ‹pini› symbol?
		1. If an article continues from an odd page to an even page, is there an arrow in the bottom right on the odd page?
		1. Are the first words of each non-poetry article in bold?
		1. Is the TODO
	1. Are the colours correct?
		1. For each category, is the background of the title images the same shade?
1. Is the PDF metadata correct?

## exporting

- Go to *File > Export as PDF* TODO.
- PDF version 1.5 TODO.

## the greyscale version

- SVG images, such as front cover: in *Properties*, set the right dimensions and position.
- images must have same dimensions and same positioning

- ungroup the front and back cover with *Control + Shift + `g`*.
- you can remove the objects that are not displayed on the page, but it’s not necessary. If you do, then the pre-flight verifier in Scribus will raise some errors like ‹Object is not on a Page TODO› before you export the document. You can ignore them.

Front cover: use your imagination; make front and back look good. Use only the colours ‹kiwen› and ‹kiwen walo›

### replacing the colours
