astro = "*"
num = 0

while (num > 9 or num < 1):
    num = int(input("정수를 입력 : "))
    if (num > 9 or num < 1):
        print("값이 범위를 벗어남")
        break
    else:
        for i in range(num):
            for j in range(num - i - 1):
                print(" ", end="")
            for k in range(i * 2 + 1):
                print(f"{astro}", end="")
            print("")
        
        for i in range(num -2, - 1, -1):
            for j in range(num - i - 1):
                print(" ", end="")
            for k in range(i * 2 + 1):
                print(f"{astro}", end="")
            print("")
    num = 0