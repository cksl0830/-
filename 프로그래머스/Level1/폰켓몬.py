def solution(nums):

    num=len(nums) #폰켓몬숫자
    answer=list(set(nums)) #중복제거

    if num/2 > len(answer):
        return len(answer)
    else:
        return num/2
      
      
 // 다른 사람의 풀이 (간결의 끝판왕 ,,)

def solution(nums):
    return min(len(set(nums)), len(nums)//2)  
