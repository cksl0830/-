import itertools

def solution(nums):
    count = 0
    
    for i in itertools.combinations(nums, 3):
        answer=sum(i)
        k=0
        for j in range(2,answer):
            if answer%j == 0:
                k+=1
                break
        if k==0:
            count+=1

    return count
  
  
// 다른 사람의 풀이 (if-else 효율적으로 사용 ,,)
    
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:              #안에 for문 나와서 else 하기
            answer += 1
    return answer

  
