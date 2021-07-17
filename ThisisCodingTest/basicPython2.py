# 문자열 자료형
# 문자열 변수 초기화 -> '' OR "" 사용
data = 'Hello World'
print(data)

# 문자열 내부에 "" OR '' 사용해야할때 -> " "안에는 '' , '' 안에는 "" , \(백슬래시) 사용시 "",'' 를 문자열에 원하는 만큼 포함시킬 수 있다
data = "Dont't ypu know \"Python\"?"
print(data)

# 문자열 연산
a = 'Hello'
b = 'World'
print(a + " " + b)

a = 'String'
print(a * 3)

# 문자열은 내부적으로 리스트와 같이 처리된다 -> 리스트와 같이 인덱싱과 슬라이싱 이용할 수 있다
a = "ABCDEF"
print(a[2 : 4])

# 튜플 자료형 -> 소괄호() 를 이용, 한번 선언된 값을 변경할 수 없다
a = (1,2,3,4)
print(a)
# a[2] = 7

# 사전 자료형 -> key,value의 쌍을 데이터로 가지는 자료형 => 내부적으로 해시테이블을 이용하므로 데이터의 검색 및 수정에 있어 O(1)의 시간에 처리할 수 있다
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

# 사전 자료형에 특정한 원소가 있는지 검사할 때 -> '원소 in 사전' 형태를 사용 => 리스트나 튜플에서도 사용할 수 있는 문법 
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

if '사과' in data : 
    print("'사과'를 키로 가지는 데이터가 존재합니다")

# 사전 자료형 관련 함수
# keys() -> 키 데이터만 뽑아 리스트로 이용
# values() -> 값 데이터만 뽑아서 리스트로 이용
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()

# 값 데이터만 담은 리스트
values_list = data.values()

print(key_list)
print(values_list)

# 각 키에 따른 값을 하나 씩 출력
for key in key_list : 
    print(data[key])

# 집합 자료형 -> 리스트 혹은 문자열을 이용해 만들수 있다 => 중복 허용하지 않는다, 순서가 없다
# - 키가 존재하지 않고 값 데이터만 담게 된다
# - 특정한 데이터가 이미 등장한 적이 있는지 여부를 체크할 때 매우 효과적이다
# 초기화 -> set() 함수 이용 OR 중괄호 안에 각 원소를 콤마 기준으로 구분해서 넣는다 ({,})

# 초기화 방법 1) set() 함수 이용
data = set([1,1,2,3,4,4,5])
print(data)

# 초기화 방법 2) 중괄호 사용
data = {1,1,2,3,4,4,5}
print(data)

# 집합 자료형의 연산 -> 합집합 : | , 교집합 : & , 차집합 : -
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

# 합집합
print( a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)

# 집합 자료형 관련 함수 -> add(), update(), remove()
data = set([1,2,3])
print(data)

# add() : 새로운 원소 추가
data.add(4)
print(data)

# update() : 새로운 원소 여러 개 추가
data.update([5,6])
print(data)

# remove() : 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

# 조건문
# if 조건문 1 :
#       조건문 1이 True일 때 실행되는 코드
# elif 조건문 2 :
#       조건문 1에 해당하지 않고 , 조건문 2가 True 일 때 실행되는 코드
# else :
#       위의 모든 조건문이 모두 True 값이 아닐 때 실행되는 코드
grade = 90
if grade >= 90 :
    print("A")
elif grade >= 80 :
    print("B")
elif grade >= 70 :
    print("C")
else :
    print("F")

# in , not in 연산자
# X in 리스트 -> 리스트 안에 X가 들어 있을 때 True
# X not in  문자열 -> 문자열 안에 X가 들어가 있지 않을 때 True

# pass -> 조건문의 값이 True라고 해도 아무것도 처리하고 싶지 않을 때 사용
score = 85
if score >= 80 :
    pass
else :
    print("성적이 80점 미만입니다")

print("프로그램을 종료합니다")

# 반복문 
# while , for
# while -> 조건이 참일 때에 한해서 반복적으로 코드 수행
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9 :
    result += i
    i += 1

print(result)

# for 
# for 변수 in 리스트 :
#       실행할 소스코드

result = 0
# i는 1부터 9까지의 모든 값을 순회
for i in range(1,10) : 
    result += i

print(result)

# range() 의 값으로 하나의 값만 넣으면 자동으로 시작 값은 0이 된다
scores = [90,85,77,65,97]

for i in range(5) :
    if scores[i] >= 80 :
        print(i + 1, "번 학생은 합격입니다.")

# 2중 for문 - 구구단
for i in range(2,10) :
    for j in range(1,10) :
        print(i,"X",j,"=",i*j)
    print()

# 함수
# def 함수명(매개변수) :
#       실행할 소스코드
#       return 변환 값

# 더하기 기능 함수
def add(a,b) :
    return a + b

print(add(3,7))

# 함수의 배개변수의 변수를 직접 지정
print(add(b = 3 , a = 7))

# global 키워드 -> 해당 함수는 지역변수를 만들지 않고 함수 바깥에 선언된 변수를 바로 참조하게 된다
a = 0

def func() :
    global a
    a += 1

for i in range(10) :
    func()

print(a)

# 입 출력
# 입력을 위한 코드

# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int,input().split()))

data.sort(reverse=True)
print(data)

# n, m ,k를 공백으로 구분하여 입력
n, m, k = map(int,input().split())

print(n,m,k)

# sys 라이브러리 사용 -> 빠른 입력을 위해 java 의 버퍼드리더 라고 생각
import sys
# readline() 함수 호출 후 꼭 rstrip() 함수 사용해야 한다 -> readline() 으로 입력하면 입력후 엔터가 줄바꿈 기호로 입력 => 이 공백 문자를 제거하기위해 rstrip() 함수 사용
sys.stdin.readline().rstrip()

# 변수를 문자열로 바꾸어 출력 -> str()
answer = 7

print("정답은" + str(answer) + "입니다")
# 각 변수를 콤마로 구분해도 된다
print("정답은", str(answer), "입니다")
