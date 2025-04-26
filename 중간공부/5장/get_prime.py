# 5장 : 사용자가 입력한 정수가 소수인지 판단하는 로직

while (True):
    num = int(input("정수를 입력 : "))
    primeCnt = 0
    list = []

    for i in range(1, num + 1):
        if num % i == 0:
            list.append(i)
            primeCnt += 1
    
    if num > 1 and primeCnt == 2:
        print(f"정수 {num}의 약수들 =", list)
        print(f"{num} is Prime")
    else :
        print(f"정수 {num}의 약수들 =", list)
        print(f"{num} is not Prime")

    choice = str(input("추가 진행 여부 (yes/no) : "))
    if choice == "no":
        print("프로그램 종료...")
        break