import math

def convert(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

def isprime(x):
    if x==1:
        return False
    
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0:
            return False
    return True

def solution(n, k):
    
    cnt = 0
    s = convert(n,k)
    s = s.split('0')
    
    for num in s:
        if not num: 
            continue 
        if isprime(int(num)): 
            cnt += 1
    return cnt
