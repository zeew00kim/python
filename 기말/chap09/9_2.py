from time import *
from datetime import *
# 각 모듈의 모든 함수 및 상수를 현재 namespace로 가져온다는 뜻

# 두 날짜를 입력 받아 그 사이의 차이(일 수)를 반환
def cntDay(date1, date2):
    retDay = 0
    # 문자열 data를 '/' 기준으로 나누어 각 변수에 대입
    year, month, day = date1.split('/')
    sDay = date(int(year), int(month), int(day))
    year, month, day = date2.split('/')
    eDay = date(int(year), int(month), int(day))
    diffDay = eDay - sDay
    retDay = diffDay.days # 날짜만 추출
    return retDay

def getDay(t):
    week = ['월', '화', '수', '목', '금', '토','일']
    return week[t.tm_wday] # 한글 요일을 문자열로 반환

startDate, curDate, tm = "", "", None

if __name__ == "__main__" :
    startDate = input("시작날짜(연/월/일) : ")
    tm = localtime()
    curDate = str(tm.tm_year) + '/' + str(tm.tm_mon) + '/' + str(tm.tm_mday)

    print(startDate, "부터 오늘(", curDate, ")까지는", 
          cntDay(startDate, curDate), "일이 지났습니다.")
    print("그리고 오늘은", getDay(tm), "요일입니다.")