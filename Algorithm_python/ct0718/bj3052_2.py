# 다시풀기
import sys
A = []
B = []
for i in range(10) :
    A.append(int(sys.stdin.readline().strip()))
    B.append(int(A[i] % 42))

answer = set(B)

print(len(answer))