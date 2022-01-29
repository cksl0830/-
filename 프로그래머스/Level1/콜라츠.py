def solution(num):
    count = 0

    for i in range(500):
        if num%2==0:
            num=num/2
            count+=1

        elif num==1:
            return count
        else:
            num=num*3+1
            count+=1


    return -1
  
  
 // 다른 사람의 풀이 #그냥 for문 도는 i에 +1 ... 굳이 count쓴 나를 반성하려고 가져옴 
 
 def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
