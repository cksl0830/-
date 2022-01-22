def solution(id_list, report, k):
    answer = {x: 0 for x in id_list}  # 메일 받는 횟수를 value값으로
    recieve = {x: 0 for x in id_list}  # 신고 받은 횟수를 value값으로

    for s in set(report):
        recieve[s.split()[1]] += 1

    for i in set(report):
        if recieve[i.split()[1]] >= k:
            answer[i.split()[0]] += 1

    return list(answer.values())
  
  
  // 다른 사람 풀이
  
  -> 다 비슷하게 풀었다. 테케에 시간초과라는 조건이 있어서 효율성있게 짜는 것이 중요했던?
  나 역시 처음에 시간초과가 떴다.. 레벨1이지만 나중에 꼭 다시 풀어보자!
  
  

  
