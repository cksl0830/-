def solution(N):
    answer = 0
    N=list(map(int,str(N)))

    for i in range(len(N)):
        answer+=N[i]

    return answer

 
// 다른 사람의 풀이 (재귀 사용)

def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 
