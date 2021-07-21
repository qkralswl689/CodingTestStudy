import sys

a,b,c = map(int,sys.stdin.readline().split())

d = a+b+c
print(d,format((d/3),".2f"))