import random

def getNum(strData):
    numStr = ""
    for ch in strData:
        # .isdigit() : 문자열이 숫자로만 되어있는지 확인
        if ch.isdigit(): 
            numStr += ch
    
    return int(numStr) # 문자열을 정수로 변환 후 리턴

data = [] 
i, k = 0, 0

if __name__ == "__main__" :
    for i in range(0, 10):
        temp = hex(random.randrange(0, 100000))
        temp = temp[2:] # 접두사 '0x' 제거
        data.append(temp) # 16진수 문자열 리스트에 추가
    
    print("정렬 전 데이터 : ", end="")
    for num in data:
        print(num, end=" ")
    
    print("")

    # getNum 함수에서 추출된 정수를 기준으로 리스트 정렬
    for i in range(0, len(data)-1):
        minIdx = i
        for j in range (i+1, len(data)):
            if getNum(data[minIdx]) > getNum(data[j]):
                minIdx = j
        temp = data[i]
        data[i] = data[minIdx]
        data[minIdx] = temp
    
    print("정렬 후 데이터 : ", end="")

    for num in data:
        print(num, end=" ")

    print("")