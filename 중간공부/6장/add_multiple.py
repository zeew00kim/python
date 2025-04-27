# 6장 : 7의 배수들의 합을 구하는 프로그램

sum = 0

for i in range(7, 100, 7):
    sum += i

print(f"7의 배수들의 합 : {sum}")