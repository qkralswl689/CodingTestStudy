import sys

from string import ascii_uppercase

alpha_list = list(ascii_uppercase)

n =  sys.stdin.readline().strip()

n_list = list(n)

n_list.sort()
print(n_list)
count = 0
answer = 0
result = 0
for i in range(len(n_list)) :
    for j in range(len(alpha_list)):
        if n_list[i] in alpha_list[j] :
            count += alpha_list.index(n_list[i])+1
            break

print(count)

