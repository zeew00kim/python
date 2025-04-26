import random

num = []

for i in range(10) :
    num.append(random.randrange(1, 11))
    print("%d " %num[i], end="")

print("")

print("after making list : ", num)

for i in range(9) :
    minIdx = i
    for j in range(i + 1, 10) :
        if num[j] < num[minIdx] :
            minIdx = j
    temp = num[i]
    num[i] = num[minIdx]
    num[minIdx] = temp

print("after sortting list : ", num)

for n in range(10) :
    if n not in num :
        print("integer %d is not in list" %n)