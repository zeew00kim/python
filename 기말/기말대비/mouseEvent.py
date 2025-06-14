from tkinter import *
from tkinter import messagebox

# 클릭한 마우스 버튼의 종류와 선택된 좌표를 알려줌
def clickEvent(event):
    if event.num == 1:
        show = "Left Button (" + str(event.x) + ", " + str(event.y)  + ")"
    elif event.num == 3:
        show = "Right Button (" + str(event.x) + ", " + str(event.y) + ")"
    label.configure(text=show)

# 마우스를 뗄 경우 어떤 종류의 버튼을 떼었는지
def releaseEvent(event):
    if event.num == 1:
        messagebox.showinfo("좌클릭 해제", "좌클릭 마우스 해제")
    elif event.num == 3:
        messagebox.showinfo("우클릭 해제", "우클릭 마우스 해제")

root = Tk()
root.title("마우스 드래그")
root.geometry("300x200")
root.resizable(width=FALSE, height=FALSE)

label = Label(root, text="마우스 버튼을 클릭", fg="red", font=("굴림", 10))
label.pack(side=TOP)

root.bind("<Button>", clickEvent)
root.bind("<ButtonRelease>", releaseEvent)

root.mainloop()