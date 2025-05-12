# 튜플 형식으로 인식
def func(*para):
    result = 0
    for num in para:
        result += num
    return result

hap = func(10, 20)
print("매개변수 2개 전달 결과 :", hap)
hap = func(10, 20, 30)
print("매개변수 3개 전달 결과 :", hap)

# 딕셔너리 형식으로 인식
def dic(**para):
    for i in para.keys():
        print("%s --> %d명입니다." % (i, para[i]))

dic(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)