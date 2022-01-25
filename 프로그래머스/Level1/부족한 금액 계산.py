def solution(price, money, count):
    answer = 0

    for i in range(1,count+1):
        answer+=price*i

    if answer>money:
         return answer-money
    else:
        return 0
      
      
// 다른 사람의 풀이 (등차수열의 합을 이용 ,,) 

def solution(price, money, count):
    return max(0,price*(1+count)*count//2-money)
