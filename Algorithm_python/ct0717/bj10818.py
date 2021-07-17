import sys

n = int(sys.stdin.readline().strip())

k = list(map(int,sys.stdin.readline().split()))

print(min(k), max(k))