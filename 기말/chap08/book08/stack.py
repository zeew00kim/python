import random

# 파이썬으로 quickSort 및 stack 구조 구현

def init_stack():
    global top
    top = -1

def is_empty():
    if top == -1:
        return True
    else:
        return False

def is_full():
    if top == listLen - 1:
        return True
    else :
        return False
    
def error(errorStr):
    print(errorStr)
    exit(1)

def push(element):
    global top, data, listLen
    if is_full() == True:
        data += [0] * listLen
        listLen *= 2
        top += 1
        data[top] = element
        print("스택 크기 두배 증가")
    else:
        top += 1
        data[top] = element

def pop():
    if is_empty():
        error("stack underflow")
    else:
        global top
        temp = top
        top -= 1
        return data[temp]

def peek():
    if is_empty():
        error("stack underflow")
    else:
        return data[top]
    
def quickSort(data, left, right):
    if (left >= right):
        return
    
    pivot = data[(left + right) // 2]
    checkLeft = left
    checkRight = right
    temp = 0

    while checkLeft <= checkRight:
        while data[checkLeft] < pivot:
            checkLeft += 1
        while data[checkRight] > pivot:
            checkRight -= 1
        if checkLeft <= checkRight:
            temp = data[checkLeft]
            data[checkLeft] = data[checkRight]
            data[checkRight] = temp
            checkLeft += 1
            checkRight -= 1
    
    quickSort(data, left, checkRight)
    quickSort(data, checkLeft, right)

listLen = int(input("리스트의 길이를 입력 : "))
listInt = []

top = 0
data = [0] * listLen

init_stack()

for i in range(0, listLen):
    listInt.append(random.randint(1, 20))

quickSort(listInt, 0, listLen -1)

while(True):
    init_stack()
    for i in range(0, listLen):
        push(listInt[i])
    cycle = str(input("반복 여부 (yes/no) : "))
    if cycle == "no":
        break

popCnt = int(input("pop 횟수 입력 : "))

print("pop 연산 %d회 수행 결과 : " % popCnt, end="")
for i in range(0, popCnt):
    print(pop(), end=" ")

print("") 