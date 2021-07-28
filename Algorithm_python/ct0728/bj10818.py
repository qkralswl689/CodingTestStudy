import sys

n = int(sys.stdin.readline().strip())

for i in range(1) :
    tmp = list(map(int,sys.stdin.readline().split()))

print(min(tmp),max(tmp))