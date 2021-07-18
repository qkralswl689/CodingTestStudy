import sys

n = int(sys.stdin.readline().strip())

grade = list(map(int,sys.stdin.readline().split()))

m = max(grade)
sum = 0.0
dev = []
for i in range(n) :
    dev.append(float(grade[i]/ m * 100))
    sum += dev[i]

answer = sum / n

print(answer)