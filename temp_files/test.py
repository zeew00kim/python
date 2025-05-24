def temp(*val):
    for i in range(len(val)):
        value = list(val)
        for i in range(len(value)):
            value[i] += 10
    return value

print("함수 실행 결과 :", list(map(lambda x: x**2, temp(10, 20, 30, 40))))