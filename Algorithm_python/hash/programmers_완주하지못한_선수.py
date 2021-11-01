participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
answer = ''
for i in range(len(completion)) :
    for j in range(len(participant)) :
        if participant[j] == completion[i]:
            participant.remove(completion[i])
            if len(participant) == 1:
                answer = participant[0]
            break

# for i in range(len(participant)):
#     answer = participant[i]

print(answer)
# 제출용 -> 효율성 0.0 으로 실패
def solution(participant, completion):
    answer = ''
    for i in range(len(completion)):
        for j in range(len(participant)):
            if participant[j] == completion[i]:
                participant.remove(completion[i])
                if len(participant) == 1 :
                    answer = participant[0]
                break

    return answer