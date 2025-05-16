# 문자열을 단어 단위로 left|right shift 하는 프로그램

inStr, outStr = "", ""
strLen = 0

inStr = str(input("문자열을 입력 : "))

word = inStr.split() # 공백 기준 문자열 분리 후 리스트 저장
strLen = len(word)

while True:
    sel = str(input("LEFT or RIGHT 방향 선택 : "))
    if sel != "left" and sel != "right":
        print("조건에 맞도록 재입력!!!")
        continue
    break

if sel == "left":
    for i in range(strLen):
        shift = word[i+1:] + word[:i+1]
        outStr = " ".join(shift) # 문자열들을 공백으로 이어 붙임
        print("leftShift no.%d :" % (i+1), outStr)

elif sel == "right":
    for i in range(strLen):
        shift = [word[-1]] + word[:-1]  # 오른쪽 회전
        word = shift
        outStr = " ".join(shift)  # 문자열들을 공백으로 이어 붙임
        print("rightShift no.%d :" % (i+1), outStr)

push, pop = "", ""
cnt = 0 

push = str(input("문자열을 입력 : "))
cnt = len(push)

for i in range(cnt):
    pop += push[cnt - (i+1)]

print("거꾸로 출력 :", pop)

print("시작이 \'00\'이면 :", pop.startswith("00"))
print("종료가 \'z\'라면 :", pop.endswith("z"))