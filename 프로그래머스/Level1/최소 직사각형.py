def solution(sizes):

    w=[] 
    h=[]

    for i in range(len(sizes)):
        w.append(min(sizes[i])) #둘 중 작은 것들의 list
        h.append(max(sizes[i])) #둘 중 큰 것들의 list


    return max(w)*max(h) #두 list중 젤 큰 것들 곱하기


// 다른 사람의 풀이

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
