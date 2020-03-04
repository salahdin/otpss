import pytesseract
from PIL import Image


# converting image file into text
def convert_img_to_txt(str):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = Image.open(str)
    return pytesseract.image_to_string(im)
