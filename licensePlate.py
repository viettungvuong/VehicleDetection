import cv2
import imutils
import pytesseract

path='license_plates/'
image = cv2.imread(path+'1.jpeg')
# chinh kich thuoc hinh xuong 500 px
image = imutils.resize(image, width=500)
# tao gray image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# giam noise cua anh
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)

