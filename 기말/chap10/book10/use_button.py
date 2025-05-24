from tkinter import *
from tkinter import messagebox

def myFunc():
    # messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠^^")
    if check.get() == 0:
        messagebox.showinfo("", "체크 버튼 해제")
    else :
        messagebox.showinfo("", "체크 버튼 활성")

window = Tk()

# photo = PhotoImage(file = r"기말\chap10\task10\gif\dog3.gif")
# button1 = Button(window, image=photo, command=myFunc)

# button1.pack()

check = IntVar()
checkBox1 = Checkbutton(window, text="클릭하세요.", variable = check, command = myFunc)

checkBox1.pack()

window.mainloop()