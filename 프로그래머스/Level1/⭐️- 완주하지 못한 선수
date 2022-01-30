def solution(participant, completion):
    answer = dict()
    HashValue = 0
    
    for p in participant:
        answer[hash(p)] = p    #hash() 함수 숫자값으로 변환(주소)
        HashValue += hash(p)

    for c in completion:
        HashValue -= hash(c)

    return answer[HashValue]
    
    
// 다른 사람의 풀이 1

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
    
    
// 다른 사람의 풀이 2  (collections 사용)

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
