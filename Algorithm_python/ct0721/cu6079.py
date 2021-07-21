import sys

a = int(sys.stdin.readline().strip())

sum = 0

for i in range(1, a +1 ) :
    sum += i
    if sum >= a :
        print(i)
        break
