import sys

num = sys.stdin.readline().strip()

answer = ''.join(filter(str.isalnum,num))
print(answer)