while (True):
    sel = int(input("원하는 진수 값을 입력 (2/8/10/16) : "))
    num = input("10진수 정수를 입력 : ")

    if sel == 16:
        num10 = int(num, 16)
        print("16진수 -> ", hex(num10))
    elif sel == 10:
        num10 = int(num, 10)
        print("10진수 -> ", num10)
    elif sel == 8:
        num10 = int(num, 8)
        print("8진수 -> ", oct(num10))
    else:
        num10 = int(num, 2)
        print("2진수 -> ", bin(num10))

    choice = input("종료 여부를 선택 y/n : ")
    if choice == 'y':
        break