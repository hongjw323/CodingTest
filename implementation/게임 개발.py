n, m = map(int, input().split()) #직사각형 크기 입력받기(nxm)
x, y, z = map(int, input().split()) #x,y : 현재위치 / z : 방향

#맵 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#갔다온 곳 체크 (초깃값 0)
went = [[0]*m for _ in range(n)]

#북(0), 동(1), 남(2), 서(3)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 돌기
def turn_left():
    global z
    z -= 1
    if z == -1:
        z = 3

#시뮬레이션 시작
turn_cnt = 0
result = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[z]
    ny = y + dy[z]

    #갔던 곳이 아니고, 육지면 이동
    if went[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        went[nx][ny] = 1
        result += 1
        turn_cnt = 0
        continue
    #다 갔던 곳 아니면 바다인 경우
    else:
        turn_cnt += 1
         #네 방향 모두 갈 수 없는 경우
        if turn_cnt == 4:
            nx = x - dx[z]
            ny = y - dy[z]

            if array[nx][ny] == 1:  #뒷 칸이 바다인 경우
                break
            else:   #뒤로 갈 수 있다면 이동
                x = nx
                y = ny
            turn_cnt = 0

print(result)