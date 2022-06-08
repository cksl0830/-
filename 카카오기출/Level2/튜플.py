def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    
    for i in s:
        temp = i.split(',')
        for j in temp:
            if not int(j) in answer:
                answer.append(int(j))
    return answer
    
    
// 다른 풀이 (시간복잡도 감소)

from collections import Counter

def solution(s):
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.split(',')
    s = list(map(int,s))
    
    s = dict(Counter(s))
    counter = sorted(s.items(), key=lambda x: -x[1])
    
    answer=[]
    for key,value in counter:
        answer.append(key)
    
    return answer
