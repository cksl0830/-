def solution(record):
    answer = []
    dic = {}
    
    for s in record:
        temp = s.split()
        if len(temp) == 3:
            dic[temp[1]] = temp[2]
              
    for s in record:
        temp = s.split()
        if temp[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dic[temp[1]])
        elif temp[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dic[temp[1]])
            
    return answer
