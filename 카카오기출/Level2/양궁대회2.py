from collections import deque

def bfs(n, info):    
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0
    
    while q:
        focus, arrow = q.popleft()
        if n >= sum(arrow):
            
            if sum(arrow) == n:  # 종료조건 1) 화살 다 쏜 경우
                apeach, ryan = 0, 0
                for i in range(11):
                    if not (info[i] == 0 and arrow[i] == 0):
                        if info[i] >= arrow[i]:
                            apeach += 10 - i
                        else:
                            ryan += 10 - i
                            
                if apeach < ryan:  # 라이언이 이기면
                    gap = ryan - apeach
                    if maxGap > gap:
                        continue
                    maxGap = gap  # 최대점수차 갱신
                    res=arrow[:]  # 최대점수차를 내는 화살상황 저장
                    
            elif focus == 10:  # 종료조건 2) 화살 덜 쐈을때 마지막에 몰아주기
                tmp = arrow.copy()
                tmp[focus] = n - sum(tmp)
                q.append((focus+1, tmp))

            else:  # 화살 쏘기
                tmp = arrow.copy()
                tmp[focus] = info[focus]+1 
                q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
                tmp2 = arrow.copy()
                tmp2[focus] = 0
                q.append((focus+1, tmp2))  # 0발 쏘기
    return res

def solution(n, info):
    answer = bfs(n, info)
    
    if not answer:
        return [-1]
    else:
        return answer
