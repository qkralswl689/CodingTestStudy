# A 와 B 의 값을 공백으로 구분하여 입력받는다
A, B = map(int,input().split())

if A > B :
    print('>')
elif A < B :
    print('<')
elif A == B :
    print('==')
