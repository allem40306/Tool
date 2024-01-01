# https://newbedev.com/python-python-load-all-images-from-folder-code-example
import os, fitz
from PIL import Image
from tqdm import tqdm

def imageConvert(inputFolder, outputFolder):
    imageList = [".webp",".tif",".jpx"]
    for file in os.listdir(inputFolder):
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() in imageList:
            im = Image.open(f"{inputFolder}\{file}").convert("RGB")
            im.save(f"{outputFolder}\{filename}.jpg","jpeg")

def imageToPdf(inputFolder):
    imageList = [".png",".jpg"]
    def imgToPdf(folder, name):
        pdf = fitz.open()
        for path in tqdm(os.listdir(folder), desc=f'{name}', leave=False):
            filename, file_extension = os.path.splitext(path)
            if file_extension.lower() in imageList:
                file = f"{folder}/{path}"
                with Image.open(file) as img:
                    width, height = img.size
                page = pdf.new_page(width=width, height=height)
                rect = fitz.Rect(0, 0, width, height) 
                page.insert_image(rect=rect, filename=file)
        pdf.save(f"{inputFolder}/{name}.pdf")

    for path in tqdm(os.listdir(inputFolder)):
        fullPath = f"{inputFolder}/{path}"
        if os.path.isdir(fullPath):
            imgToPdf(fullPath, path)
