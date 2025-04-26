# 4장 : 비트 연산자 활용 예제

a = ord('A')
mask = 0x0F # 2진수 : 00001111 (15)

print("%x & %x = %x" % (a, mask, a & mask)) # %x : 정수를 16진수 소문자로 출력
print("%X | %X = %X" % (a, mask, a | mask)) #%X : 정수를 16짙수 대문자로 출력

mask = ord('a') - ord('A') # 32

# XOR 값이 서로 다를 경우 True
b = a ^ mask
print("%c ^ %d = %c" % (a, mask, b))
a = b ^ mask
print("%c ^ %d = %c" % (b, mask, a))