from skimage.filters import threshold_local
import numpy as np
from PIL import Image
import cv2
from django.core.files import File
from io import BytesIO


def preProcessImage(image,degree):
    # converting PIL image to cv2 format
    im = Image.open(image)
    im.rotate(degree)
    im.convert('RGB')

    # binarizing image
    open_cv_image = np.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    warped = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    T = threshold_local(warped, 11, offset=10, method="gaussian")
    warped = (warped > T).astype("uint8") * 255

    # converting image back to PIL format
    im = Image.fromarray(warped)

    # converting file into a django friendly format
    temp_io = BytesIO()
    im.save(temp_io, 'JPEG')
    final = File(temp_io, name=image.name)

    return final
