from tkinter import *
window = Tk()

# bt1 = Button(window, text="버튼1")
# bt2 = Button(window, text="버튼2")
# bt3 = Button(window, text="버튼3")

# bt1.pack(side = BOTTOM)
# bt2.pack(side = BOTTOM)
# bt3.pack(side = BOTTOM)

btnList = [0] * 3

for i in range(len(btnList)):
    btnList[i] = Button(window, text="버튼" + str(i+1))

for btn in btnList:
    btn.pack(side = TOP, fill = X, padx = 10, pady = 10, ipadx = 10, ipady = 10)

window.mainloop()