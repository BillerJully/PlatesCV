import cv2
import pytesseract
import re
import sys
from imutils import contours
from tkinter import *
from tkinter import filedialog
import messagebox

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
            checkpoint = False
            if len(result) > 7:
                for c in result:
                    if c.isdigit():
                        checkpoint = True
            if checkpoint:
                messagebox.showinfo(title="Найденный номер: ", message="Номер на машине: "+ result)





    #cv2.imshow("Test", image)

window = Tk()
window.title("Распознавание номеров")
window.geometry('600x400')
canvas = Canvas(window, height=600, width=400)
canvas.pack()
frame = Frame (window, height=600, width=400)

btn = Button(text="Загрузить фото автомобиля", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=Plates)
btn.place(relx=.5, rely=.5, anchor="c", height=30, width=270, bordermode=OUTSIDE)

window.mainloop()
