def solution(N):
    answer = 0
    N=list(map(int,str(N)))

    for i in range(len(N)):
        answer+=N[i]

    return answer

 
// 다른 사람의 풀이 (재귀 사용) # 아주 좋은 방법.. 생각을 더 많이 해보자!

def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 

// 다른 사람의 풀이2 # 간단하게 구현할 수 있음에도 좀 돌아갔던 나의 풀이.. 
def sum_digit(number):
    return sum([int(i) for i in str(number)])
