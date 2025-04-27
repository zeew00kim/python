# 7장 : 리스트에서 최대값과 최소값을 찾아 반환하는 프로그램

list = []
num, min, max = 0, 0, 0

while(True):
    num = int(input("정수 하나를 입력 : "))
    if num > 999 or num < -999:
        print("~999 ~ 999 이내의 갑으로 재입력...")
        continue
    elif num == 0:
        print("입력을 종료합니다...")
        list.sort()
        max = list.pop()
        min = list[0]
        break
    else:
        print(f"push {num} into the stack")
        list.append(num)

print("sorted list =", list[0::])
print(f"최대값 : {max}, 최소값 : {min}")