# 7장 : 2차원 배열 프로그램

list_2d = []
val = 0

for i in range(0, 4):
    row = []
    for j in range(0, 5):
        row.append(val)
        val += 3
    list_2d.append(row)

for i in range(0, 4):
    for j in range(0, 5):
        print("%d\t" % list_2d[i][j], end="")
    print("")