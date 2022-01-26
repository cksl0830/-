def solution(a, b):
    answer=0

    for i in range(min(a,b),max(a,b)+1):
        if a==b :
            return a
        else:
            answer+=i

    return answer
  
// 다른 사람의 풀이 (가우스공식 이용 .. 경이롭다!!! 복습하자!!)

def adder(a, b):
    return (abs(a-b)+1)*(a+b)//2  



# 가우스 공식

--> n(x+y)//2 ::: n은 두 수 사이의 갯수 , x랑 y는 두 수를 말한다!!! 
