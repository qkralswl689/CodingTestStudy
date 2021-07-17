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