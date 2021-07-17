import sys

n = int(sys.stdin.readline().strip())

# for i in range(1,n+1) :
#     for j in range(i) :
#         print("*" , end="")
#     print()

for i in range(1,n+1) :
    print("*" * i ,end="")
    print()
