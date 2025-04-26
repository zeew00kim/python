# sum, i = 0, 0
# num = int(input("enter the positive-integer : "))

# while i < num :
#     sum += i
#     i += 1

# print("result of sum i ~ num : {0:d}" .format(sum))

num = 0

while (num > 9 or num < 1) :
    num = int(input("정수를 입력 : "))
    if (num > 9 or num < 1) :
        print("범위를 벗어남...")
        break
    else :
        for i in range(num) :
            for j in range(num - 1 - i):
                print(" ", end="")
            for k in range(i * 2 + 1):
                print("\u2605")
            print("")

        for i in range(num - 2, -1, -1):
            for j in range(num - i - 1):
                print(" ", end="")
            for k in range(i * 2 + 1):
                print("\u2605")
            print("")
    num = 0