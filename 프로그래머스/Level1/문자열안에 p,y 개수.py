def solution(s):

    if s.count('p')+s.count('P') != s.count('y')+s.count('Y'):
        return bool(0)
    else:
        return bool(1)
        
        
// 다른 사람의 풀이 (소문자로 바꾸기 ...아하)

def numPY(s):
   
    return s.lower().count('p') == s.lower().count('y')
