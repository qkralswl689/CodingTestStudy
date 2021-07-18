##### 코드 분석 할것
# https://blog.naver.com/nuang0530/221949503294
import sys

sum = 1

for i in range(3) :
    # eval() : 문자열 형태로 입력된 숫자를 수 형태로 변경해준다
    A = eval(sys.stdin.readline())
    sum *= A


sum_list = list(str(sum))

for i in range(10) :
    # count 함수는 문자열 내부에서 특정 문자, 혹은 문자열이 포함 되어있는지 계산해서 반환 해준다
    print(sum_list.count(str(i)))


