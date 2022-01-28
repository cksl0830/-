def solution(number):
    return (sum(list(map(int,str(number)))))
 
// 다른 사람의 풀이 (재귀 사용) # 아주 좋은 방법.. 생각을 더 많이 해보자!

def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 

// 다른 사람의 풀이2 ( 타입 변환 )
def sum_digit(number):
    return sum([int(i) for i in str(number)])
