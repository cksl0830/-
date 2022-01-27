def solution(s):

    if (len(s)==4 or len(s)==6) and s.isdigit():
        return bool(1)
    else:
        return bool(0)
      
      
 // 다른 사람의 풀이 (len in --> len이 4 또는 6 안에 포함인지 확인 ,, or이랑 같음!)

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)  
