temp = "0123456789ABCDEF"

def convert(num, base):
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]
    
def solution(n, t, m, p):
    answer = ''
    tmp = ''
    
    for i in range(m*t):
        tmp += convert(i, n)
        
    while len(answer) != t:
        answer += tmp[p-1]
        p += m
        
    return answer
