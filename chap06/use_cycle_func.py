# 1부터 사용자가 입력한 정수 값 까지의 합
num = int(input("정수 값을 하나 입력 : "))
sum = 0

print("[ ", end="")
for i in range(1, num, 1):
    sum += i
    print("%d" % (i), end="")
    if i != num - 1 :
        print(", ", end="")
    elif i == num - 1 :
        print(" ]")

print(f"result of sum = {sum}")

# 0 ~ 100 사이에 있는 7의 배수들의 합
sum = 0

for i in range(0, 100):
    if i % 7 == 0 and i >= 7:
        sum += i

print(f"{sum}")

# 사용자가 입력한 정수의 구구단 가로로 출력하기
while True :
    n = int(input("1 ~ 9 사이의 정수 값을 입력 : "))
    if n >= 1 and n <= 9 :
        print("당신이 입력한 정수 : %d" % n)
        break
    else :
        print("범위 이내의 값으로 재입력...")
        continue

for _ in range(1):
    for j in range(1, 10, 1):
        print("%d * %d = %-3d" % (n, j, n * j), end="")
    print("")