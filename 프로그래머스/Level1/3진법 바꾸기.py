def solution(n):

    answer = 0
    temp=''

    while n!=0 :  #3진법으로 변환
        temp+=str(n%3)
        n=n//3

    answer=int(temp,3) #3진수에서 10진수로

    return answer
    
