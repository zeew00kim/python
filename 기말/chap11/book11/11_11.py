from tkinter import *

## 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE = 256, 256

## 메인 코드 부분 ##
window = Tk()
canvas = Canvas(window, height = XSIZE, width = YSIZE)

paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE / 2 , YSIZE / 2), image = paper, state = "normal")

canvas.pack()
window.mainloop()