i, k, heartNum = 0, 0, 0
numStr, ch, heartStr = "", "", ""

if __name__ == "__main__" : 
    # 입력한 숫자를 각 하나의 문자열로 처리
    numStr = input("숫자를 여러개 입력 : ") 
    print("")
    i = 0
    ch = numStr[i]
    while True : # 파이썬은 bool 자료형이 대문자로 시작
        heartNum = int(ch)
        heartStr = ""
        for j in range(0, heartNum):
            heartStr += "\u2665"
            k += 1
        print(heartStr)

        i += 1
        if (i > len(numStr) - 1):
            break
        ch = numStr[i]