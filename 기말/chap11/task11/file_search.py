from tkinter import *
import os
import os.path

## 함수 선언 부분 ##
def clickListBox(evt):
    global currentDir, searchDirList
    if (dirListBox.curselection() == ()):  # 다른 리스트 박스를 클릭할 때는 무시
        return
    dirName = str(dirListBox.get(dirListBox.curselection()))  # 클릭한 폴더명
    if dirName == '상위폴더':
        if len(searchDirList) == 1:  # 상위 폴더를 클릭했는데, 현재 C:\면 무시
            return
        searchDirList.pop()  # 상위 폴더로 이동
    else:
        searchDirList.append(currentDir + dirName + '\\')  # 클릭한 폴더 추가
    fillListBox()


def fillListBox():
    global currentDir, searchDirList, dirLabel, dirListBox, fileListBox
    dirListBox.delete(0, END)     # 폴더 리스트 박스를 비움
    fileListBox.delete(0, END)    # 파일 리스트 박스를 비움

    dirListBox.insert(END, "상위폴더")
    currentDir = searchDirList[len(searchDirList) - 1]
    dirLabel.configure(text=currentDir)
    folderList = os.listdir(currentDir)

    for item in folderList:
        if os.path.isdir(currentDir + item):
            dirListBox.insert(END, item)
        elif os.path.isfile(currentDir + item):
            fileListBox.insert(END, item)


## 전역 변수 선언 부분 ##
window = None
searchDirList = ['C:\\']     # 검색할 폴더 목록의 스택
currentDir = 'C:\\'
dirLabel, dirListBox, fileListBox = None, None, None

## 메인 코드 부분 ##
window = Tk()
window.title("폴더 및 파일 목록 보기")
window.geometry('300x500')

dirLabel = Label(window, text=currentDir)
dirLabel.pack()

dirListBox = Listbox(window)
dirListBox.pack(side=LEFT, fill=BOTH, expand=1)
dirListBox.bind('<<ListboxSelect>>', clickListBox)

fileListBox = Listbox(window)
fileListBox.pack(side=RIGHT, fill=BOTH, expand=1)

fillListBox()  # 처음에는 C:\의 모든 폴더 목록 보기

window.mainloop()