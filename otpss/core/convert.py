import pytesseract
from PIL import Image


# converting image file into text
def convert_img_to_txt(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    im = Image.open(image)
    # using psm 1 because for rotated images
    custom_config = r'--oem 3 --psm 1 '
    return pytesseract.image_to_string(im, config=custom_config) + " "
