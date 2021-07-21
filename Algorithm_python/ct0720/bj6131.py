import sys

n = int(sys.stdin.readline().strip())

count = 0

for a in range(1,501) :
    for b in range(1,501) :
        if( a * a > b * b and a * a == (b * b) + n ) :
            count += 1
print(count)