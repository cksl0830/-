def solution(msg):
    
    alp=[0]
    for i in range(26):
        alp.append(chr(65+i))
    
    answer = []
    s,e=0,1
    while True:
        if e==len(msg):
            answer.append(alp.index(msg[s:e]))
            break
            
        if not msg[s:e+1] in alp:
            answer.append(alp.index(msg[s:e]))
            alp.append(msg[s:e+1])
            s=e
            
        e+=1
            
    return answer
