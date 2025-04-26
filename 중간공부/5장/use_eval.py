# 5장 : eval 함수를 사용한 프로그램

select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

select = int(input("1. 입력한 수식 계산, 2. 두 수 사이의 합계 : "))

if select == 1:
    numStr = input("수식을 입력 : ")
    answer = eval(numStr)
    print("\'%s\'의 결과는 %5.1f입니다." % (numStr, answer))

elif select == 2:
    num1 = int(input("첫 번째 정수 : "))
    num2 = int(input("두 번째 정수 : "))
    for i in range(num1, num2 + 1):
        answer += i
    print("%d + ... + %d = %d" % (num1, num2, answer))

else:
    print("1 또는 2만 입력...")