def solution(n):

    word='수박'

    if n%2==0:
        return word*(n//2)

    if n%2!=0:
        return word*(n//2)+word[0]
        
        
// 다른 사람의 풀이 (생각했었는데 n의 숫자가 엄청 크면 s의 메모리 공간이 늘어나서 갠적으로 별로 ..)
 
def water_melon(n):
    
    s = "수박" * n
    return s[:n]
 
