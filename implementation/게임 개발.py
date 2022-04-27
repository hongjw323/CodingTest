n, m = map(int, input().split())

x, y, z = map(int, input().split())

# 맵 정보
maps = []   # 0 : 육지, -1 : 바다
for i in range(n):
    maps.append(list(map(int, input().split())))
# 왔던 곳 체크
gone = [[0]*m for _ in range(n)]    # 0 : 안가본 곳
gone[x][y] = 1

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽 방향
def turn_left():
    global z
    z -= 1
    if z == -1:
        z = 3

cnt = 1
turn_cnt = 0
while True:
    turn_left()
    nx = x + dx[z]
    ny = y + dy[z]
    # 육지 + 가보지 않은 곳 일 때, 이동
    if maps[nx][ny] == 0 and gone[nx][ny] == 0:
        gone[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_cnt = 0 # 이동했으니까 초기화
        continue
    else:
        turn_cnt += 1
    # 4방향 다 돌았을 때
    if turn_cnt == 4:
        nx = x - dx[z]
        ny = y - dy[z]
        if maps[nx][ny] == 0:   # 육지라면 뒤로 이동
            x = nx
            y = ny
        else:   # 바다 + 가본 곳일 때, 종료
            break
        turn_cnt = 0 # 4방향 다 돌아봤으니까 초기화

print(cnt)