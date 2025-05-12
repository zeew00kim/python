# 4장 : 평점평균을 구하는 프로그램

score = [3.5, 4.0, 4.5]
credit = [3, 2, 1]
top, bottom = 0, 0

for i in range(len(score)):
    top += (score[i] * credit[i])
    bottom += credit[i]

avg = top / bottom

print("평균 점수 : %.2f" % (avg))