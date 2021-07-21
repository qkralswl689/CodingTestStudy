import sys

a,b = map(int,sys.stdin.readline().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format((a / b), ".2f"))