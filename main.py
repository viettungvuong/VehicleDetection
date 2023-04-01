import numpy as np
import os
import cv2
from os.path import isfile, join
import matplotlib.pyplot as plt
from PIL import Image
import glob
import video

# convert frames to grayscale
def grayScaleImage(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# image threshold of two grayscale pics
def imageThreshold(grayA, grayB):
    diff_image = cv2.absdiff(grayB, grayA)

    # perform image thresholding
    ret, thresh = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)

    return thresh

# image dilation from image threshold
def imageDilation(thresh):
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    return dilated


# count valid contours
def contours(thresh):
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    valid_cntrs = []

    for i, cntr in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cntr)
        # kiem tra contour co nam trong vung quy dinh hay kh (duoi y = 80) va dien tich phai du lon
        if (x <= 200) & (y >= 80) & (cv2.contourArea(cntr) >= 25):
            valid_cntrs.append(cntr)
    return valid_cntrs


 # ve contour tren hinh goc
def contourOriginal(frame,thresh,i,path):
    valid_countours = contours(thresh)

    dmy = frame.copy()
    cv2.drawContours(dmy, valid_countours, -1, (127, 200, 0), 2)
    cv2.line(dmy, (0, 80), (256, 80), (100, 255, 255))
    plt.imshow(dmy)
    plt.show()

    cv2.putText(dmy, "vehicles detected: " + str(len(valid_countours)), (55, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 180, 0), 2)
    cv2.line(dmy, (0, 80), (256, 80), (100, 255, 255))
    cv2.imwrite(path + str(i) + '.png', dmy)

kernel = np.ones((4,4),np.uint8)

#import frame
path = "frames/"

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

for i in range(0,len(frames)-1):
    # get grayscale images
    grayA=grayScaleImage(frames[i])
    grayB=grayScaleImage(frames[i+1])

    thresh=imageThreshold(grayA, grayB)

    dilated=imageDilation(thresh)

    contourOriginal(frames[i],thresh,i,path)

video.videoGenerate()

