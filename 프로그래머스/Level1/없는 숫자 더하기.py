def solution(numbers):
    answer=0
    list=[0,1,2,3,4,5,6,7,8,9]

    for x in list:
        if x not in numbers:
            answer+=x

    return answer
  
  
  // 다른 사람의 풀이 
  def solution(numbers):
    return 45 - sum(numbers)
