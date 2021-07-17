import sys

n = int(sys.stdin.readline().strip())

for i in range(1,n+1) :
    a,b = map(int,sys.stdin.readline().split())
    print("Case #%s: %s"%(i,a + b))