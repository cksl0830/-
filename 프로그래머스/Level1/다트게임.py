def solution(dartResult):
    temp = ''
    score = []
    
    for i in dartResult:
        if i.isnumeric():
            temp += i   #처음에 temp=i로 했는데 10 이라는 숫자때문에 에러남  
        elif i == 'S':
            temp = int(temp)**1
            score.append(temp)
            temp = ''
        elif i == 'D':
            temp = int(temp)**2
            score.append(temp)
            temp = ''
        elif i == 'T':
            temp = int(temp)**3
            score.append(temp)
            temp = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1
        
    return sum(score)
            
  
// 다른 사람의 풀이 (진짜 효율적인 풀이인듯 ... 그래도 가독성은 내가 더 좋은듯..) 

def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)
    
