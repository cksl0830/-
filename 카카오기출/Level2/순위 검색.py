from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    
    # info 정보 저장 
    for s in info:
        s = s.split()
        key = s[:-1]
        value = int(s[-1])

        for i in range(5):
            comb = list(combinations(key, i))
            for c in comb:
                temp = ''.join(c)
                dic[temp].append(value)
                
    for key in dic.keys():
        dic[key].sort()

    # query 확인 
    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        key = q[:-1]
        value = int(q[-1])

        while '-' in key:
            key.remove('-')
            
        key = ''.join(key)
        
        if key in dic:
            scoreList = dic[key]
            left, right = 0, len(scoreList)
            while left < right:
                mid = (left + right) // 2
                if scoreList[mid] >= value:
                    right = mid
                else:
                    left = mid+1
            answer.append(len(scoreList)-left)

        else:  
            answer.append(0)

    return answer
