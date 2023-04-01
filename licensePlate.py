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

# edge detection
edge = cv2.Canny(gray_image, 30, 200)
# tim contour
contours, new = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1 = image.copy()
# cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
# cv2.imshow("img1",img1)
# cv2.waitKey()

valid_contours=[]
# tim nhung contour phu hop, du rong
for contour in contours:
    if (cv2.contourArea(contour)>=400):
        valid_contours.append(contour)

cv2.drawContours(img1,valid_contours,-1, (0,255,0), 3)
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()