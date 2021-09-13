import sys

coin = [25,10,5,1]

t = int(sys.stdin.readline())
t_list = []
for i in range(t) :
    t_list.append(int(sys.stdin.readline()))

for i in t_list :
    c = []
    for j in range(len(coin)) :
        # // : 나누기 연산 후 소수점 이하의 수를 버리고, 정수 부분의 수만 구함
        c.append(i // coin[j])
        i = i % coin[j]

    print(c[0], c[1], c[2], c[3])
