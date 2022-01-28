def solution(n):
    answer=list(map(int,str(n)))

    return answer[::-1]
    
// 다른 사람의 풀이 (함수 사용)

def solution(n):
    return list(map(int, reversed(str(n))))
