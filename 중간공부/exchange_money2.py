money, c50000, c10000, c5000, c1000 = 0, 0, 0, 0, 0

money = int(input("금액을 입력 : "))

if money >= 50000:
    c50000 = money // 50000
    money %= 50000

    c10000 = money // 10000
    money %= 10000

    c5000 = money // 5000
    money %= 5000

    c1000 = money // 1000
    money %= 1000

print(f"5만 원 : {c50000}개\n1만 원 : {c10000}개\n5천 원 : {c5000}개\n1천 원 : {c1000}개")
print(f"잔여 금액 : {money}")