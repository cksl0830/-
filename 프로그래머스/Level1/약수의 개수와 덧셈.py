def solution(left, right):
    answer=0
    count=0

    for i in range(left,right+1):
        for k in range(1,i+1):
            if (i % k==0):
                count+=1

        if (count % 2==0):
            answer+=i
        else:
            answer-=i
        count=0


    return answer
    

// 다른 사람의 풀이 

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:    #제곱수의 약수 개수는 홀수개임을 이용
            answer -= i
        else:
            answer += i
    return answer
