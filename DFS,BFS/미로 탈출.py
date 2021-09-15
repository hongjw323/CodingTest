### BFS 문제 ###
from collections import deque

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input())))

#상,하,좌,우 이동방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#BFS 함수 정의
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()
        #상,하,좌,우 이동
        for i in range(4):
            #다음 칸으로 이동
            nx = x + dx[i]
            ny = y + dy[i]

            #밖으로 나가면
            if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                continue
            #괴물이 있으면
            if array[nx][ny] == 0:
                continue
            #괴물이 없으면(갈 수 있음)
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1 #거리 더하기
                queue.append((nx,ny))

    #가장 오른쪽 아래까지의 최단거리 반환
    return array[n-1][m-1]

#BFS 함수 호출
print(bfs(0,0))