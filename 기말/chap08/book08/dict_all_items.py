# 딕셔너리의 키와 값들을 모두 출력하는 프로그램

std = {}

std["id"] = 2022
std["name"] = "zeew00"
std["major"] = "S/W"

for key in std.keys():
    print("%s : %s" % (key, std[key]), end=' ')

print()

for items in std.items():
    print(f"{items}", end=" ")

print()

for key, value in std.items():
    print(f"{key}:{value}", end=" ")