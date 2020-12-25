from fpdf import FPDF
import os
pdf = FPDF()
imagelist = os.listdir()
# imagelist is the list with all image filenames
for image in imagelist:
	print(image)
	if image.endswith(".png") or image.endswith(".PNG") or image.endswith(".jpg") or image.endswith(".JPG"):
		pdf.add_page()
		pdf.image(image,None,None,150)
print("OK")
pdf.output("yourfile.pdf", "F")