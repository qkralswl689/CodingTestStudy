import sys

n,x = map(int,sys.stdin.readline().split())

num = list(map(int,sys.stdin.readline().split()))

for i in range(len(num)) :
    if num[i] < x :
        print(num[i], end=" ")