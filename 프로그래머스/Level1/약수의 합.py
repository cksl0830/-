def solution(n):
    answer = 0

    for i in range(1,n+1):
        if n%i==0:
            answer+=i

    return answer
    
// 다른 사람의 풀이 ( n / 2 의 수들만 검사하면 성능 약 2배 향상.. 기억! ) 

def solution(n):
   
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
