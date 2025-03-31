year = 0

# __name__ : 다른 파일에선 실행 X
if __name__ == "__main__":
    year = int(input("enter the year : "))
    
    # 연산자 우선순위에 의해 and 부분 조건 만족 시 or는 비교안함
    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        print("{0:d} is leap year.\n" .format(year))
    else :
        print(f"{year} is not leap year.\n")