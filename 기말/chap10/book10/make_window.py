from tkinter import *

window = Tk()
# window.title("윈도우 연습")
# window.geometry("400x100")
# window.resizable(width = FALSE, height = FALSE)

photo = PhotoImage(file = r"기말\chap10\task10\gif\cat.gif")
label1 = Label(window, image=photo)
label2 = Label(window, text = "우애옹쓰", font = ("궁서체", 30), fg = "blue")
# label3 = Label(window, text = "배경색", font = ("궁서체", 10), bg = "magenta", 
#                width = 20, height = 5, anchor = "center") # 앵커는 기준점 (SE = 오른쪽 아래)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)
# label3.pack()

window.mainloop()