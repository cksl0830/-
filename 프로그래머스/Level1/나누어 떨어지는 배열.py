def solution(arr, divisor):
    answer = []

    for i in arr:
        if i%divisor==0:
            answer.append(i)

    if len(answer)==0:
        answer.append(-1)

    return sorted(answer)
    
 
// 다른 사람의 풀이 (정확히 똑같이 짰다가 가독성을 위해 위에처럼 다시 품)
 
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1] 
