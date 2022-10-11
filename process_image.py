"""
    This file is intended to test the image processing methods before
        adding them to the main app. This allows using PyCharm debugging
        features s.a. breakpoints efficiently.
    This script uses the scribble drawing from ./static/images/input.png
        as its input image.
"""

import cv2
from pathlib import Path

root = Path('.')

if __name__ == '__main__':
    image = cv2.imread(root/'static'/'images'/'image.png')
    pass