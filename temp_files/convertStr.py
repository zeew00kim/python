inputStr = ''

if __name__ == "__main__":
    inputStr = input("enter the string : ")
    strLen = len(inputStr)
    print("converted string : ", end="")
    for i in range(strLen -1, -1, -1):
        print(f"{inputStr[i]}", end="")