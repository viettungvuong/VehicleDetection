import cv2
import imutils
import os
import pytesseract

path = "license_plates/"

def getLicensePlate(image,i):
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
    # cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
    # cv2.imshow("img1",img1)
    # cv2.waitKey()

    valid_contours=[]
    # tim nhung contour phu hop, du rong
    for contour in contours:
       if (cv2.contourArea(contour)>=300):
          valid_contours.append(contour)

       # cv2.drawContours(img1,valid_contours,-1, (0,255,0), 3)
       # cv2.imshow('img1',img1)
       # cv2.waitKey(0)
       # cv2.destroyAllWindows()

       # tim countour nao ma la bien so xe
       for contour in valid_contours:
          perimeter = cv2.arcLength(contour, True) # chu vi contour

          # ham nay tra ve polygonal representation cua contour
          # ham nay con giup contour don gian hon nhung van giu duoc hinh dang
          approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)

          if len(approx)==4: # neu co 4 canh
             shape = approx # tim duoc bien so xe
             # luu contour chua bien so xe
              
             # lay phan bien so xe
             x, y, w, h = cv2.boundingRect(contour)
             processImg = image [y: y + h, x: x + w]
             cv2.imwrite(path+'plate'+str(i)+'.png',processImg)

             cv2.drawContours(image, [shape], -1, (255, 0, 0), 3)
             # cv2.imshow('License plate',image)
             # cv2.waitKey(1)
             # cv2.destroyAllWindows()

             break
       
def getLicenseNumber(license_plate):
    text = pytesseract.image_to_string(license_plate, lang='eng') 
    return text

imageNames = os.listdir(path)
i = 0

for name in imageNames:
   filePath = os.path.join(path,name)
   currentImg = cv2.imread(filePath)

   if currentImg is None:
      continue
   
   getLicensePlate(currentImg,i)

   plateImg = cv2.imread(path+'plate'+str(i)+'.png')
   print("i license number is " + getLicenseNumber(plateImg) + "\n")
   
   i+=1
   





