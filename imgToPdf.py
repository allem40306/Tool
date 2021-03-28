from fpdf import FPDF
import os

pdf = FPDF()
imagelist = os.listdir()

# imagelist is the list with all image filenames
for image in imagelist:
	if image.endswith(".png") or image.endswith(".PNG") or image.endswith(".jpg") or image.endswith(".JPG"):
		try:
			pdf.add_page()
			pdf.image(image,None,None,150)
			print(image)
		except:
			print(image + "is GG")
			pass

print("OK")
pdf.output("picture.pdf", "F")