money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
money = int(input("교환할 금액 :  "))
# 4장 : 입력한 금액을 환전 후 남은 금액을 출력하는 프로그램

c500 = money // 500
money %= 500
print(f"500원 수량 : {c500}")

c100 = money // 100
money %= 100
print("100원 수량 : %d" % (c100))

c50 = money // 50
money %= 50
print("50원 수량 : {0:d}" .format(c50))

c10 = money // 10
money %= 10
print(f"10원 수량 : {c10}")

print(f"잔금 : {money}")