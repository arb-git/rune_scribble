import cv2
import matplotlib.pyplot as plt
import random
import string

def Cv2ImgShow(img_array, scale_factor=1):
    window_name = ''.join([random.choice(string.ascii_lowercase) for _ in range(10)])
    cv2.namedWindow(window_name)
    if scale_factor != 1:
        img_array = cv2.resize(img_array, (img_array.shape[1]*scale_factor, img_array.shape[0]*scale_factor))
    cv2.imshow(window_name, img_array)
    cv2.waitKey(0)

def PltShowImage(image_list, window_name='whatever'): # for mark_boundaries output
    """Prints a scaled image with matplotlib"""
    fig = plt.figure(window_name)
    if len(image_list) > 10:
        # assume that one image is passed, but not packed in a list
        image_list = [image_list]
    for nr, image in enumerate(image_list):
        ax = fig.add_subplot(1, len(image_list), nr+1)
        ax.imshow(image)
        # ax.colorbar()
    _ = plt.plot()