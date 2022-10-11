"""
    This file is intended to test the image processing methods before
        adding them to the main app. This allows using PyCharm debugging
        features s.a. breakpoints efficiently.
    This script uses the scribble drawing from ./static/images/input.png
        as its input image.
"""

import cv2
import numpy as np
from pathlib import Path
from utils import Cv2ImgShow, PltShowImage

root = Path('.')

if __name__ == '__main__':
    img_path = str(Path(root/'static'/'images'/'input.png').absolute())
    image = cv2.imread(img_path)

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    PltShowImage(grayscale_image)