def solution(d, budget):

    answer = 0 
    count = 0
    d.sort()

    for i in d:
        if i <= (budget-answer):
            answer+=i
            count+=1
        else:
            break

    return count

  
// 다른 사람의 풀이  (시간 복잡도 상에서 sum()이 반복되어 그렇게 좋은 풀이는 아닌 것 같다) 

def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
