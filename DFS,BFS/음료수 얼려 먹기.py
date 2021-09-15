### DFS 문제 ###
n, m = map(int, input().split())    #n,m 입력

#얼음판 입력
array = []
for i in range(n):
    array.append(list(map(int,input())))

#DFS 함수 정의 : 연결된 모든 노드들 방문
def dfs(x,y):
    #얼음판 밖일 때 종료
    if x<0 or y<0 or x>n-1 or y>m-1:
        return False
    
    #구멍 찾기
    if array[x][y] == 0:
        array[x][y] = 1 #방문 처리
        #상, 하, 좌, 우 움직이기
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x, y-1)
        dfs(x, y+1)
        #다 움직이면 True
        return True
    #0이 없을 때
    return False

#DFS 함수 실행
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)