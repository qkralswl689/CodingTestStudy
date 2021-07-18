import sys

n = int(sys.stdin.readline().strip())

for i in range(n) :
    ox = list(str(sys.stdin.readline()))

    # 값 출력 후 초기화
    sum = 0
    count = 0

    for j in range(len(ox)):
        if(ox[j].__eq__('O')):
            count += 1
            sum += count
        elif(ox[j].__eq__('X')) :
            count = 0
    print(sum)

