charAstro ='*'
num = 0

while (num > 9 or num < 1) :
    num = int(input("enter the integer number : "))
    if (num > 9 or num < 1):
        print("number is out of bounds...")
        break
    else:
        for i in range(num):
            for j in range(num - i - 1):
                print(" ", end="")
            for k in range(i * 2 + 1):
                print(f"{charAstro}", end="")
            print("")

        for i in range(num - 2, -1, -1):
            for j in range(num - i - 1):
                print(" ", end="")
            for k in range(i * 2 + 1):
                print(f"{charAstro}", end="")
            print("")
    num = 0