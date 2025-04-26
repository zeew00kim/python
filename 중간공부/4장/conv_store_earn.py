import random

itemCnt = 6

Pprice = [random.randint(1000, 10000) for _ in range(itemCnt)]
Sprice = [price + 1000 for price in Pprice]

Ptotal = sum(Pprice)
Stotal = sum(Sprice)
profit = Stotal - Ptotal

print("[ 편의점의 하루 매출 계산 ]")
for i in range(itemCnt):
    print(f"물품 {i+1} 구매가격 {Pprice[i]}원, 판매가격 {Sprice[i]}원")

print(f"본사에 지불한 총 구매금액 : {Ptotal}원")
print(f"물품 판매 수익 : {Stotal}원")
print(f"총 판매 수익 : {profit}원")