# 5장 : 윤년 여부를 구해 해당 월의 일수를 구하는 로직

def get_days_in_month(year, month):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_year = True
    else: 
        leap_year = False
    
    if month == 2:
        if leap_year == True:
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

year = int(input("연도를 입력 : "))
month = int(input("월을 입력 : "))

if 1 <= month and month <= 12:
    days = get_days_in_month(year, month)
    print(f"{year}년 {month}월의 일수는 {days}일입니다.")
else:
    print("1~12 범위의 값으로 입력하세요...")