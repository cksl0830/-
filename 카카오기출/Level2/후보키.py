from itertools import combinations

def solution(relation):
    n = len(relation)
    m = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, m+1):
        combi.extend(combinations(range(m), i))
        
    #유일성
    unique = []
    for c in combi:
        tmp=set()
        for item in relation:
            tmp.add(tuple([item[key] for key in c]))

        if len(tmp) == n:    # 유일성
            flag = True
            
            for x in unique:
                if set(x).issubset(set(c)):  # 최소성
                    flag = False
                    break
                    
            if flag: 
                unique.append(c)
    
    return len(unique)
