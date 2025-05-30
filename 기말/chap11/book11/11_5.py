# 텍스 파일 검색 후 출력

inFp = None
fName, inList, inStr = "", [] , ""

fName = input("파일명을 입력 : ") # C:/Windows/Temp/data1.txt
inFp = open(fName, "r", encoding="UTF-8")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")

inFp.close()