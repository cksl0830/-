def solution(absolutes, signs):
    answer=0

    for x in range(len(absolutes)):
        if signs[x]:
            answer+=absolutes[x]
        else:
            answer+=-absolutes[x]

    return answer
  
  
// 다른 사람의 풀이 
  
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
