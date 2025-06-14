from tkinter import *
from tkinter import messagebox

def myFunc():
    if myVar.get() == 1:
        messagebox.showinfo("벤츠", "당신의 선택은 벤츠")
    elif myVar.get() == 2:
        messagebox.showinfo("BMW", "당신의 선택은 BMW")
    else :
        messagebox.showinfo("아우디", "당신의 선택은 아우디")

root = Tk()
root.title("차량 선택")
root.geometry("200x150")
root.resizable(width=FALSE, height=FALSE) 

myVar = IntVar()

label = Label(root, text="하단의 브랜드 중 하나를 선택", font=("궁서체", 8), fg="blue", anchor=CENTER)
label.pack(side=TOP)

rd1 = Radiobutton(root, text="벤츠", variable=myVar, value=1)
rd1.pack(side=TOP)
rd2 = Radiobutton(root, text="BMW", variable=myVar, value=2)
rd2.pack(side=TOP)
rd3 = Radiobutton(root, text="아우디", variable=myVar, value=3)
rd3.pack(side=TOP)

btn = Button(root, text="클릭하세요", bg="Yellow", command=myFunc)
btn.pack(side=TOP)

root.mainloop()