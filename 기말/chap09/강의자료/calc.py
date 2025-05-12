def calc(a, b, op):
    result = 0
    if op == '+':
        result = a + b
        print("%d + %d = %d" % (a, b, result))
    elif op == '-':
        result = a - b
        print("%d - %d = %d" % (a, b, result))
    elif op == '*':
        result = a * b
        print("%d * %d = %d" % (a, b, result))
    elif op == '/':
        result = a / b
        print("%d / %d = %d" % (a, b, result))
    elif op == '//':
        result = a // b
        print("%d // %d = %d" % (a, b, result))
    elif op == '%':
        result = a % b
        print("%d % %d = %d" % (a, b, result))
    elif op == '**':
        result = a ** b
        print("%d ** %d = %d" % (a, b, result))
    else :
        print("연산자 입력 오류")
        return -1
    return result

a = int(input("a 값을 입력 : "))
b = int(input("b 값을 입력 : "))
op = input("연산자를 입력 : ")

result = calc(a, b, op)