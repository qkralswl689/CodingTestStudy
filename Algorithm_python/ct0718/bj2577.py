import sys
B = 1
for i in range(3) :
    A = eval(sys.stdin.readline().strip())
    B *= A

answer = list(str(B))

for i in range(10) :
    # count 함수는 문자열 내부에서 특정 문자, 혹은 문자열이 포함 되어있는지 계산해서 반환 해준다
    print(answer.count(str(i)))


