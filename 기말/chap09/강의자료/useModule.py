from module_logic import * # 모듈 전체 호출

print(greet("zeew00"))
print(add(3, 5))

# random 함수로 로또 숫자 추첨
import random

def getNum():
    return random.randint(1, 45)

def selectionSort(lotto, size):

    for i in range(size):
        swapCnt = 0
        for j in range(size - i - 1):
            if lotto[j] > lotto[j+1]:
                temp = lotto[j]
                lotto[j] = lotto[j+1]
                lotto[j+1] = temp
                swapCnt += 1
        if swapCnt == 0:
            break

lotto =[]

print("[ 로또 추첨 시작 ]")

while True:
    num = getNum()
    if lotto.count(num) == 0:
        lotto.append(num)

    
    if len(lotto) >= 6:
        break

size = len(lotto)
selectionSort(lotto, size)

print("추첨된 로또 번호 : ", end="")

for i in range(len(lotto)):
    print(f"{lotto[i]} ", end="")

print()