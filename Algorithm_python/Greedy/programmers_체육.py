

##for i in range(lost) :
  ##  if(i == lost[i]) :

##print(lost[0])

# result = n - len(lost)
# for i in range(1 ,n+1) :
#     for j in range(len(lost)):
#         if i == lost[j]:
#          for k in range(len(reserve)):
#                  if reserve[k] - lost[j] == 1 or  reserve[k] - lost[j] == -1:
#                     reserve[k] = -1
#                     result += 1
#                     break
# print(result)

## 65% 정답
# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     for i in range(1, n + 1):
#         for j in range(len(lost)):
#             if i == lost[j]:
#                 for k in range(len(reserve)):
#                     if reserve[k] - lost[j] == 1 or reserve[k] - lost[j] == -1:
#                         reserve[k] = -1
#                         answer += 1
#                         break
#     return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

## 90% 정답 -> java로 푼거 대입
## 도난당한 학생수 만큼 반복
def solution(n, lost, reserve):
    answer = n
    for i in range(len(lost)) :
        # 체육복 여분 여부 false로 설정
        j = 0
        yn = False
        #yn 이 false일 경우
        while yn == False :
            # 여벌의 체육복을 가진 학생 수 만큼 wile문이 돌면 break
           if j == len(reserve) :
               break
           if i+1 < len(lost) :
               if lost[i+1] == reserve[j] :
                   j += 1
                   continue
            # 도난당한 학생 번호와 여벌의 체육복이 있는 학생의 번호가 같으면
           if lost[i] == reserve[j] :
               # 여벌의 체육복이 있는 학생의 번호의 자리에 -1 대입 후
               reserve[j] = -1
               # 체육복 여분 여부를 true(여분있음)으로 변경
               yn = True
           # 도난당한 학생의 번호 - 여분의 체육복이 있는 학생의 번호의 값이 1인경우
           elif lost[i] - reserve[j] == 1 :
               # 여벌의 체육복이 있는 학생의 번호의 자리에 -1 대입 후
               reserve[j] = -1
               # 체육복 여분 여부를 true(여분있음)으로 변경
               yn = True
            # 도난당한 학생의 번호 - 여분의 체육복이 있는 학생의 번호의 값이 -1인경우
           elif lost[i] - reserve[j] == -1 :
               # 여벌의 체육복이 있는 학생의 번호의 자리에 -1 대입 후
               reserve[j] = -1
               # 체육복 여분 여부를 true(여분있음)으로 변경
               yn = True
           else :
               # 위의 경우가 아니면 j의 값을 1씩 더해준다
               j += 1

        # while문이 돌고난후 yn(체육복 여분 여부 체크 내용)이 false 라면
        if yn == False :
           # 수업을 들을 수 잇는 학생 수에서 1씩 감소시킨다
           answer -= 1


    return answer

