# 6장 : 홀수를 더해 출력하는 프로그램

sum = 0

for i in range(500, 1000):
    if i % 2 != 0:
        sum += i

print(f"홀수의 합계는 {sum}")