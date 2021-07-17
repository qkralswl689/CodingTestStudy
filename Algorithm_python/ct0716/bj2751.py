# 다시 풀어야됨
import sys
n = int(input())

a = []
for i in range(n) :
    a.append(int(sys.stdin.readline()))

a.sort()

[print(i) for i in a]