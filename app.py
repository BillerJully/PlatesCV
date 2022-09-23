from tkinter import *


window = Tk()
window.title("Распознавание номеров")
window.geometry('600x400')
btn = Button(window, text="Загрузить файл!")
btn.grid(column=1, row=0)
window.mainloop()