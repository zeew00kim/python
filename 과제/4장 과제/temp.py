# numArr = []
# strArr = []

# # 정수를 입력 후 연산한 결과를 출력
# for i in range(2):
#     num = int(input("enter the integer : "))
#     numArr.append(num)

# print(numArr[0] + numArr[1])

# # 문자열을 입력 후 원하는 자료형으로 변환하여 출력
# for i in range(2):
#     str = input("enter the string : ")
#     strArr.append(str)

# print(int(strArr[0]), float(strArr[1]))

# # 정수형 데이터를 문자열로 변환
# print(str(numArr[0]) + "1")

# # 파이썬은 아래와 같이 출력 시 boolean 타입으로 출력됨
# a, b = 100, 200
# print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# if(1234) : print("true")
# if(0) : print("false") # 출력 안됨

charA = ord('A') #0d65, 0x41, 0101
mask = 0x0F

print("%x & %x = %x" % (charA, mask, charA & mask))
print("%x | %x = %x" % (charA, mask, charA | mask))

mask = ord('a') - ord('A')

charB = charA ^ mask
print("%c ^ %d = %c" % (charA, mask, charB))

charA = charB ^ mask
print("%c ^ %d = %c" % (charB, mask, charA))