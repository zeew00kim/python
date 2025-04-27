# 6장 : 사용자가 입력한 단수를 출력

num = int(input("원하는 단수를 입력 : "))

print(f"[  {num}단  ]")
for i in range(2, 10):
    print("%d * %d = %d" % (num, i, num * i))
