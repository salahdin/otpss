from skimage.filters import threshold_local
import numpy as np
import imutils
from PIL import Image
import cv2
from django.core.files import File
from io import BytesIO


def preProcessImage(image):
    # converting PIL image to cv2 format
    im = Image.open(image).convert('RGB')
    open_cv_image = np.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    warped = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped, 11, offset=10, method="gaussian")
    warped = (warped > T).astype("uint8") * 255

    # converting back to PIL
    im = Image.fromarray(warped)

    temp_io = BytesIO()
    im.save(temp_io, 'JPEG')

    final = File(temp_io, name=image.name)

    return final
