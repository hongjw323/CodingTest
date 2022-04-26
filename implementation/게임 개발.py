n, m = map(int, input().split())

x, y, z = map(int, input().split())

maps = []   # 0 : 육지, -1 : 바다
for i in range(n):
    maps.append(list(map(int, input().split())))

gone = [[0]*m for _ in range(n)]    # 0 : 안가본 곳
gone[x][y] = 1

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

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
    if maps[nx][ny] == 0 and gone[nx][ny] == 0:
        gone[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1
    if turn_cnt == 4:
        nx = x - dx[z]
        ny = y - dy[z]
        if maps[nx][ny] == 0:   # 육지라면 뒤로 이동
            x = nx
            y = ny
        else:
            break
        turn_cnt = 0

print(cnt)