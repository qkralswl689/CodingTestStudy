import sys

answer = []
for i in range(2) :
    answer.append(sys.stdin.readline().strip())


for i in range(1,-1,-1) :
    print(answer[i])