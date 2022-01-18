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
  
  
  // 다른 사람의 풀이 (풀이가 비슷해서 생략)
  
