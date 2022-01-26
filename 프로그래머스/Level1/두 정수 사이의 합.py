def solution(a, b):
    answer=0

    for i in range(min(a,b),max(a,b)+1):
        if a==b :
            return a
        else:
            answer+=i

    return answer
  
// 다른 사람의 풀이 (수열공식 이용 .. 경이롭다!!! 복습하자!!)

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2  
