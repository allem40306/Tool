import io, os, glob, fitz
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image, ImageFile
from tqdm import tqdm

ImageFile.LOAD_TRUNCATED_IMAGES = True

# https://www.thepythoncode.com/code/extract-pdf-images-in-python
def pdfToImage(filepath):
    pdf_file = fitz.open(f"{filepath}.pdf")
    totalCnt = 1
    try:
        os.mkdir(f"{filepath}")
    except:
        pass
    for page_index in range(len(pdf_file)):
        page = pdf_file[page_index]
        image_list = page.get_images()
        for image_index, img in tqdm(enumerate(page.get_images(), start=1), desc=f'{pdf_file}', leave=False):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            image.save(open(f"{filepath}\image{totalCnt}.{image_ext}", "wb"))
            totalCnt = totalCnt + 1
        if len(image_list) > 5:
            break

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

for file in tqdm(glob.glob(f"D:\Tool\in\*.pdf", recursive=True)):
    pdfToImage(f"{file.replace('.pdf','')}")