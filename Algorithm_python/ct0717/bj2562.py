import sys

n = []

for i in range(9) :
    n.append(int(sys.stdin.readline().split()))

print(max(n))

print(n.index(max(n))+1)