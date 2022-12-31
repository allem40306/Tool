import io, glob, fitz
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image

# https://www.thepythoncode.com/code/extract-pdf-images-in-python
def pdfToImage(pdf_file):
    pdf_file = fitz.open(pdf_file)
    totalCnt = 1
    for page_index in range(len(pdf_file)):
        page = pdf_file[page_index]
        image_list = page.get_images()
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page {page_index}", )
        for image_index, img in enumerate(page.get_images(), start=1):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            image.save(open(f"image{totalCnt}.{image_ext}", "wb"))
            totalCnt = totalCnt + 1

def pdfMerge(inputFolder):
    paths = glob.glob(f"{inputFolder}/*.pdf")
    paths.sort()
    pdf_writer = PdfFileWriter()
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(f'{inputFolder}/out.pdf', 'wb') as fh:
        pdf_writer.write(fh)