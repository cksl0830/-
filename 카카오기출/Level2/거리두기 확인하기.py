from collections import deque
dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]  

def bfs(graph):
    p = []
    
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'P':
                p.append((i, j))
    
    visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
    distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
    q=deque()
    
    for x,y in p:
        q.append((x,y))
        visited[x][y] = 1
            
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 0:
                    if graph[nx][ny]=='X':
                        continue
                    if graph[nx][ny] == 'P' and distance[x][y] <=1:
                        return 0
                    if graph[nx][ny] == 'O':
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                        
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(bfs(place))
    
    return answer
