score = [3.5, 4.0, 4.5]

top = 3.5 * 3
top += (4.0 * 2)
top += (4.5 * 1)

bottom = sum(score)

avg = top / bottom

print("평균 점수 : %.2f" % (avg))