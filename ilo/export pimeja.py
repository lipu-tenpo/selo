# To be run from within Scribus.
import scribus

def general_settings(lipu):
	# Set document unit to millimetres. Just to be sure.
	scribus.setUnit(scribus.UNIT_MILLIMETERS)

	# Save linked text frames as PDF articles?
	lipu.article = True

	# Do not show objects outside the margins in the exported file?
	# No. It crops away too much.
	lipu.doClip = False

	# Embed fonts fully or as subset depending on 'fonts' attribute.
	lipu.fontEmbedding = 0

	# Mandatory string for PDF/X-3 or the PDF will fail PDF/X-3 conformance.
	# We recommend you use the title of the document.
	# lipu.info = 'lipu tenpo nanpa something'

	# Export PDF in grayscale?
	lipu.isGrayscale = False

	# Output destination: screen.
	lipu.outdst = 0

	# In the PDF viewer, show the document with facing pages,
	# starting with the first page displayed on the right.
	lipu.pageLayout = 3

	# Generate thumbnails?
	lipu.thumbnails = True

	# PDF version to use: PDF 1.4 (Acrobat 5)
	lipu.version = 14

def print_pimeja(lipu):
	# Save linked text frames as articles.

	# Export PDF in grayscale?
	lipu.isGrayscale = True

	# Output destination: printer.
	lipu.outdst = 1

	# Use document bleeds?
	lipu.useDocBleeds = False

	# Show crop marks?
	lipu.cropMarks = False

	# Name of file to save into.
	# FIXME cut off the last four letters (.sla)
	# and append .pdf extension
	nimi = scribus.getDocName()
	lipu.file = nimi[:-4] + '-pimeja.pdf'

	# Save selected pages to PDF file.
	lipu.save()

def print_ilo(lipu):
	# TODO Use document bleeds

	# Returns the name of the current file.
	# Appears to be with extension.
	# Unsure whether the path is also included.
	nimi = scribus.getDocName()

	# Use document bleeds?
	lipu.useDocBleeds = True

	# Show bleed marks?
	lipu.bleedMarks = False

	# Show crop marks?
	lipu.cropMarks = True

	# Indicate the distance offset between mark and page area.
	lipu.markOffset = 3

	# Indicate the length of crop and bleed marks.
	lipu.markLength = 3

	# Name of file to save into.
	# FIXME cut off the last four letters (.sla)
	# and append .pdf extension
	lipu.file = nimi[:-4] + '-ilo.pdf'

	# Save selected pages to PDF file.
	lipu.save()

if __name__ == '__main__':
	lipu = scribus.PDFfile()
	general_settings(lipu)
	# print_pimeja(lipu)
	print_ilo(lipu)
	scribus.messagebarText('Successfully exported.')
