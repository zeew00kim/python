# 윈도우 복사 명령어 구현

inFp, outFp = None, None
inStr = ""

inFp = open("C:/Windows/win.ini", "r", encoding="UTF-8")
outFp = open("C:/Windows/Temp/data1.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
