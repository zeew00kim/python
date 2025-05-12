# 리스트를 이용해 여러 값을 리턴

def multi(a, b):
    retList = []
    res1 = a + b
    res2 = a - b
    retList.append(res1)
    retList.append(res2)
    return retList

myList = []
hap, sub = 0, 0

myList = multi(100, 200)
hap = myList[0]
sub = myList[1]

print("return result :", myList)