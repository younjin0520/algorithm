def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        count=0
        for j in range(i+1,len(prices)):
            count+=1
            if prices[j]<prices[i]:
                break
        answer.append(count)
    answer.append(0)
    return answer
