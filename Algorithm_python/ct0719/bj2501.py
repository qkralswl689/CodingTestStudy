import sys

p,k = map(int,sys.stdin.readline().split())

tmp = []

for i in range(1,p+1) :
    if(p % i == 0) :
        tmp.append(i)

if(len(tmp) < k) :
    print(0)
elif(len(tmp) >= k) :
    print(tmp[k-1])