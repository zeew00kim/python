from tkinter import *
from tkinter import messagebox

def myFunc():
    if var1.get() == 1:
        label.configure(text="쏘나타를 선택함", fg="Blue")
        messagebox.showinfo("쏘나타", "중형 세단")
    elif var2.get() == 2:
        label.configure(text="그랜저를 선택함", fg="Green")
        messagebox.showinfo("그랜저", "준대형 세단")
    else:
        label.configure(text="G80을 선택함", fg="Orange")
        messagebox.showinfo("G80", "대형 세단")

root = Tk()
root.title("차량 선택")
root.geometry("240x160")

label = Label(root, text="차량을 선택하세요", font=("궁서체", 8))
label.pack()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

rd1 = Checkbutton(root, text="쏘나타", variable=var1, onvalue=1, offvalue=0)
rd1.place(x=0, y=0)
chk2 = Checkbutton(root, text="그랜저", variable=var2, onvalue=2, offvalue=0)
chk2.pack()
chk3 = Checkbutton(root, text="G80", variable=var3, onvalue=3, offvalue=0)
chk3.pack()

btn = Button(root, text="클릭하세요", bg="Yellow", command=myFunc)
btn.pack(side=BOTTOM, fill=X, padx=50, pady=10,)

root.mainloop()