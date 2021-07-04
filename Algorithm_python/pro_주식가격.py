prices = [1, 2, 3, 2, 3, 3, 1]

# prices 길이 만큼 0 채우기
answer = [0] * len(prices)

# for문의 범위 
for i in range(len(prices)) : 
    for j  in range(i+1,len(prices)) :

          if(prices[i] <= prices[j]):
                    answer[i] +=1
                
          if(prices[i] > prices[j]):
                    answer[i] +=1
                    break        
     
print(answer)
        

