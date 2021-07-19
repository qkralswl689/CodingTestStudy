import sys

n = sys.stdin.readline().strip()

# 10진수 -> 16진수 소문자로 출력
# print('%x' % n)

# 10진수 -> 16진수 대문자로 출력
# print('%X' % n)

# 16진수 -> 8진수 출력
print('%o' % int(n,16))


