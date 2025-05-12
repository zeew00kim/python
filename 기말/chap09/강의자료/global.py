# 글로벌 예약어 사용 예제

def func1():
    print("func1's value a : %d" % a)
    # 전역변수 값을 그대로 출력

def func2():
    global a # global : 전역변수 지정 키워드
    a = 10
    print("func2's value a : %d" % a)
    # 전역변수 값을 10으로 변경 후 출력

a = 20

func1()
func2()