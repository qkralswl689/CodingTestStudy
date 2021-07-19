import sys

n,k = map(int, sys.stdin.readline().split())

num = []

for i in range(1 ,k+1) :
    # [::-1] : 처음부터 끝까지 -1칸 간격으로 -> 역순으로
    num.append(int(str(n*i)[::-1]))

print(max(num))