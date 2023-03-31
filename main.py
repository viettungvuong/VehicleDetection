import numpy as np
import os
import cv2
from os.path import isfile, join
import matplotlib.pyplot as plt
from PIL import Image
import glob

#import frame
path = "frames"

# read all image file names in the folder
image_names = os.listdir(path)

# create an empty list to store the images as arrays
image_arrays = []

# loop through each image file name and read the image as an array
for name in image_names:
    # join the path and file name to get the full file path
    file_path = os.path.join(path, name)

    # read the image as an array using OpenCV or PIL
    # if using OpenCV, use cv2.imread() function
    # if using PIL, use Image.open() function
    img_array = cv2.imread(file_path)

    # add the image array to the list
    image_arrays.append(img_array)

# convert the list of image arrays to a NumPy array
frames = np.array(image_arrays)

# convert frames to grayscale
def grayScaleImage(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# image threshold of two grayscale pics
def imageThreshold(grayA, grayB):
    diff_image = cv2.absdiff(grayB, grayA)

    # perform image thresholding
    ret, thresh = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)

    return thresh

# convert two consecutive frames to grayscale
for i in range(0,len(frames)-1):
   grayA = grayScaleImage(frames[i])
   grayB = grayScaleImage(frames[i+1])

# plot the image after frame differencing
plt.imshow(cv2.absdiff(grayB, grayA), cmap = 'gray')
plt.show()

# image threshold
thresh = imageThreshold(grayA, grayB)
plt.imshow(thresh, cmap = 'gray')
plt.show()

# image dilation from image threshold
def imageDilation(thresh):
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    return dilated

# apply image dilation
dilated = imageDilation(thresh)

# plot dilated image
plt.imshow(dilated, cmap = 'gray')
plt.show()
