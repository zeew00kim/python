# 8장 : countDic = {}, countList = [] 사용 예제

import operator # 정렬을 위한 itemgetter 사용

inStr = '''오늘은 5월 6일 화요일이다. 
나는 컴퓨터공학부 4학년 학생이다.'''
cntDic = {}
cntList = []

if __name__ == "__main__":
    for ch in inStr :
        # 유니코드의 한글만 범위만 필터링 ('힣'이 마지막 범위)
        if 'ㄱ' <= ch and ch <= '힣':
            if ch in cntDic: 
                cntDic[ch] += 1 # 이미 딕셔너리에 값이 있다면 +1
            else:
                cntDic[ch] = 1 # 없다면 새로 추가 후 1로 초기화
    
    # 딕셔너리의 (문자, 빈도수) 항목들을 빈도수 기준 내림차순 정렬
    cntList = sorted(cntDic.items(), 
                     key = operator.itemgetter(1), 
                     reverse = True)
    
    print("원문 :", inStr)
    print("--------------------")
    print("문자\t빈도수")
    print("--------------------")
    for i in range(0, len(cntList)):
        print(cntList[i][0], '\t', cntList[i][1])