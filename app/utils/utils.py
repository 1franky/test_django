import base64
import contextlib
import io
import os

import cv2
import numpy as np
from PIL import Image


def format_time(inicio, fin):
    return "{:.4f} segundos".format(fin-inicio)

def from_base64_to_numpy(imgString):
    image_bytes = base64.b64decode(imgString)
    image = Image.open(io.BytesIO(image_bytes))
    im = image.convert("RGB")
    return np.array(im)


def from_file_to_numpy(file_bytes):
    file = io.BytesIO(file_bytes)
    image = Image.open(file)
    im = image.convert("RGB")
    return np.array(im)


def read_image_from_base64(string):
    nparr = np.fromstring(base64.b64decode(string), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

