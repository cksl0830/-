import math

def solution(n):
    num=math.sqrt(n)
    if num==int(math.sqrt(n)):
        return (num+1)**2
    else: 
        return -1

      


