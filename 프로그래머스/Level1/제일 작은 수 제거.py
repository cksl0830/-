def solution(arr):

    answer=sorted(arr,reverse=True)
    arr.remove(answer[len(answer)-1])

    if len(arr)==0:
        arr.append(-1)

    return arr
  
// 다른 풀이  (공부삼아 일부러 min 함수 안쓰고 다르게 풀어보았다!)

def solution(arr):
    
    arr.remove(min(arr))
    
    if len(arr)==0:
        arr.append(-1)
        
    return arr
