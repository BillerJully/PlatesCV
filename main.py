import cv2
import pytesseract
import sys
from imutils import contours
pytesseract.pytesseract.tesseract_cmd = 'D:\\tesseract\\tesseract.exe'
image = cv2.imread('./PlatesPic/3.jpg')
height, weight, _ = image.shape

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]


contour = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour, _ = contours.sort_contours(contour[0])
for i in contour:
    area = cv2.contourArea(i)
    x, y, w, h = cv2.boundingRect(i)
    if area > 500:
        img = image[y:y+h, x:x+w]
        result = pytesseract.image_to_string(img, lang="eng+rus")
        if len(result) > 7:
            print(result)




cv2.imshow("Test", thresh)



cv2.waitKey(0);