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
a[2] = 7

# 사전 자료형