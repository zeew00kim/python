# 딕셔너리의 key(음식)와 어울리는 value(음식)를 매칭하여 출력하는 프로그램

food = {
    "떡볶이":"어묵",
    "라면":"김치",
    "치킨":"맥주",
    "짜장면":"단무지"
}

while (True):
    select = input(str(list(food.keys())) + " 중 하나를 선택하세요 : ")
    if select in food:
        print("%s 음식과 어울리는 음식은 %s입니다." % (select, food.get(select)))
    elif select == "\n":
        print("반복문을 종료")
        break
    else:
        print("존재하지 않는 음식")
        continue