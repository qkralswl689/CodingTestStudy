##### 코드 분석 할것
# https://blog.naver.com/nuang0530/221949503294
import sys

sum = 1

for i in range(3) :
    A = eval(sys.stdin.readline())
    sum *= A


sum_list = list(str(sum))

for i in range(10) :
    print(sum_list.count(str(i)))