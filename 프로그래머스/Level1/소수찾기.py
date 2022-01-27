def solution(n):
    count = 0
    for n in range(2, n+1):
        for i in range(2, n):
            if n%i == 0:
                break
        else:    
            count += 1
    return count
  
  
--> 이렇게 풀면 시간초과 발생! 고민하다가 구글링해서 답지를 봤다
  
// 다른 사람의 풀이
  
def solution(n):
    num = set(range(2,n+1))
    
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
 
    return len(num)  


--> "에라토스테네스의 체"를 이용!
n까지의 모든 소수를 구한다고 하면 2를 제외한 모든 2의 배수를 num에서 제거. 
3을 제외한 모든 3의 배수를 num에서 제거. 4는 아까 2에서 제거. 
5를 제외한 모든 5의 배수를 num에서 제거. 이렇게 반복해서 num에 남아 있는 수들이 소수이다. 
대량의 소수를 한꺼번에 판별하고자 할 때 사용한다.
