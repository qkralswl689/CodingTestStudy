import sys
A = []
B = []
for i in range(10) :
    A.append(int(sys.stdin.readline().strip()))
    B.append(int(A[i] % 42))
    
# set() : 집합타입으로 변환 -> 집합으로 변경시 중복 값 사라지고 하나만 남는다
answer = set(B)

print(len(answer))
