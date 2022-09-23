import cv2
import pytesseract
import re
import sys
from imutils import contours
from tkinter import *
from tkinter import filedialog


def Plates():
    pytesseract.pytesseract.tesseract_cmd = 'D:\\tesseract\\tesseract.exe'
    file = filedialog.askopenfilename()
    image = cv2.imread(file)
    height, weight, _ = image.shape

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]

    contour = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour, _ = contours.sort_contours(contour[0])
    for i in contour:
        area = cv2.contourArea(i)
        x, y, w, h = cv2.boundingRect(i)
        if area > 500:
            img = image[y:y + h, x:x + w]
            result = pytesseract.image_to_string(img, lang="eng+rus")
            list(result)
            if len(result) > 7:
                print(result)

    cv2.imshow("Test", image)

    cv2.waitKey(0);
window = Tk()
window.title("Распознавание номеров")
window.geometry('600x400')


btn = Button(window, text="Загрузить файл!", command=Plates)
btn.grid(column=1, row=0)
window.mainloop()
