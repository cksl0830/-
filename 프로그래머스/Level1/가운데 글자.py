def solution(s):
    if len(s)%2==0:
        return s[len(s)//2-1]+s[len(s)//2]
    else:
        return s[len(s)//2]
      
      
// 다른 사람의 풀이 (슬라이싱 ,, 굿)

def solution(s):

    return s[(len(s)-1)//2:len(s)//2+1]

