import sys

n = sys.stdin.readline().strip()

# ord() : 입력값을 아스키코드 값으로 변경
n2 = ord(n)+1

# chr() : 유니코드 문자 형태로 변경
s = chr(n2)

print(s)