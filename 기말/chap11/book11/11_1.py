inFp = None
inStr = ""

inFp = open("C:/Windows/Temp/data1.txt", "r", encoding="UTF-8")
# 인코딩 옵션을 지정하지 않을 시 디코딩 에러 발생

# 아래의 방식은 한 라인씩 일일히 읽어야 함 (readline)
inStr = inFp.readline()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end ="")

inStr = inFp.readline()
print(inStr, end ="")

# 반복문을 활용한 readline()
while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(inStr, end="")
print()

inList = ""

inFp = open("C:/Windows/Temp/data1.txt", "r", encoding="UTF-8")

inList = inFp.readlines()
print(inList)

inFp.close()