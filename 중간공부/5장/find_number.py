# 5장 : 0~9 숫자 중 리스트에 없는 값 찾기
import random

number = []
for num in range(0, 10):
    number.insert(num, random.randrange(1, 10))

print("number =", number)

for num in range(len(number)):
    if num not in number:
        print(f"정수 {num}은 리스트에 없음")
