def solution(a,b):
    answer = 0
    for num1,num2 in zip(a,b):
        answer += num1 * num2

    return answer
  
  
  // 다른 사람의 풀이  (한 줄 ,,,)
  def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])
