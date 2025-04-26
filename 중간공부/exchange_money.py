money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

money = int(input("교환할 금액 :  "))

c500 = money // 500
money %= c500

c100 = money // 100
money != c100