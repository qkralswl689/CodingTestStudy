import sys

coin = [25, 10, 5, 1]
n = int(sys.stdin.readline())
n_list = []
for i in range(n):
    n_list.append(int(sys.stdin.readline()))

for i in n_list :
    c = []
    for j in range(4) :
        c.append(i // coin[j])
        i = i % coin[j]

    print(c[0], c[1], c[2], c[3])
