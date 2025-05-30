outFp = None
outStr = ""

outFp = open("C:\Windows\Temp\data2.txt", "w")

while True:
    outStr = input("문자열 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()