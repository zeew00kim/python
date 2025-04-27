# 7장 : 마지막 정수 3개만 출력하는 프로그램

list = []
num, i = 0, 0

while(num < 100):
    val = int(input("정수를 입력 : "))
    if val != -1:
        list.append(val)
        num += 1
    elif val == -1:
        print("마지막 3개의 값 :", list[-4:-1:1], end="")
        print("")
        break