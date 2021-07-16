import sys
sys.stdin = open("input.txt", 'r')

input = sys.stdin.readline

n = int(input().rstrip())-7
l = [float(input().rstrip()) for _ in range(7)]
l.sort()
i = 0
while i < n:
    l.append(float(input().rstrip()))
    l.sort()
    l.pop()
    i += 1
for n in l:
    print('{0:.3f}'.format(n))
