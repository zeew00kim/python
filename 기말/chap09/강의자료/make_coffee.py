def making_coffee(coffee):
    print("#1. 뜨거운 물을 준비")
    print("#2. 음료를 담을 컵을 준비")

    if coffee == 1:
        print("#3. 아이스 아메리카노 제조")
    elif coffee == 2:
        print("#3. 뜨거운 아메리카노 제조")
    elif coffee == 3:
        print("#3. 믹스커피 제조")
    else:
        print("#3. 아무거나 제조")

    print("#4. 물을 붓는다.")
    print("#5. 스푼으로 젓는다.")

coffee = int(input("원하는 커피 종류를 선택 (1. 아아 | 2. 뜨아 | 3. 믹스) : "))
result = making_coffee(coffee)
print("커피 제조 완료")