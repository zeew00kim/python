# 각 단수를 헤더에 표기하고 가로로 구구단 출력
for i in range(1, 10):
    if i == 1:
        for k in range(2, 10):
            print("[  %d단  ]\t" % k, end="")
            if k == 9:
                print("")
    for j in range(2, 10):    
        print("%d * %d = %d\t" % (j, i, i * j), end="")
        if j == 9:
            print("")