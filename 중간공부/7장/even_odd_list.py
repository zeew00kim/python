# 7장 : 홀수리스트, 짝수리스트를 각자 따로 출력하는 프로그램

import random

even, odd = [], []
num = 0

while(num <= 100):
    # num = int(input("정수를 입력 : "))
    num = random.randrange(0, 10)
    if num != 0:
        if num % 2 == 0:
            even.append(num)
            even.sort()
        else:
            odd.append(num)
            odd.sort()
        num += 1
    elif num == 0:
        print("반복을을 종료합니다...")
        break

print("짝수 리스트 =", even[0::])
print("홀수 리스트 =", odd[0::])