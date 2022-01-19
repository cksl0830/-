def solution(array, commands):
    answer = []
    
    for a,b,c in commands:
        sortlist=array[a-1:b]
        sortlist.sort()
        answer.append(sortlist[c-1])
            
    return answer
    
    
// 다른사람의 풀이 

def solution(array, commands):
  return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
