def solution(m, n, board):
    answer = 0
    graph=[]
    # board 배열로 만들기
    for _ in range(m):               
        temp = board.pop(0)
        graph.append([x for x in temp])
    
    # 터질 블록이 없을 때까지 반복
    while True:                               
        remove = set()         
        for i in range(m - 1):                
            for j in range(n - 1):
                if graph[i][j] == "0":
                    continue
                # 연속으로 두 개가 동일한 블록이면, 밑에 두 개도 동일한지 확인
                if graph[i][j] == graph[i][j + 1]: 
                    if graph[i][j] == graph[i + 1][j] and graph[i][j + 1] == graph[i + 1][j+1]:
                        remove.add((i, j))
                        remove.add((i, j + 1))
                        remove.add((i + 1, j))
                        remove.add((i + 1, j + 1))    

        if len(remove) == 0:
            return answer 
        
        else:
            answer += len(remove) 
            for x,y in remove:
                graph[x][y] = '0'
            
            gravity(graph,remove)

            
# 밑으로 내리는 함수
def gravity(graph,remove):
    for x,y in reversed(list(remove)):  
                check = x - 1
                put = x

                while check >= 0:
                    if graph[put][y] == "0" and graph[check][y] != "0":
                        graph[put][y] = graph[check][y]
                        graph[check][y] = "0"
                        put -= 1
                    
                    check -= 1

        
# 밑으로 내리는 함수 2 (선호함) 
def gravity(graph,m,n):
    for x in range(m-2,-1,-1):
        for y in range(n):
            if graph[x][y]!='0':
                row=x
                while True:
                    if row+1 < m and graph[row+1][y]=='0':
                        graph[row+1][y]=graph[row][y]
                        graph[row][y]='0'
                        row+=1
                    else:
                        break
                        
    
