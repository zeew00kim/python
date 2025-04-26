import sys

numArr = []
size = 10
i = 0

while i < size:
    val = input("enter the integer number : ")
    try:
        numArr.append(int(val))
        i += 1
    except ValueError:
        print("please enter the integer...")


for i in range(size):
    print(f"arr[{i}] = {numArr[i]}")