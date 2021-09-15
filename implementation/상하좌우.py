n = int(input())    #n값 입력받기
plans = input().split() #상하좌우 입력받기

x, y = 1, 1 #초기값

#L, R, U, D 에 따른 이동방향
px = [0, 0, -1, 1]
py = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

#입력받은 만큼 움직임
for p in plans:
    #이동방향 탐색
    for m in range(len(move)):
        if p == move[m]:
            nx = x + px[m]
            ny = y + py[m]
            #밖으로 빠져나갔을 경우, 무시        
            if nx<1 or ny<1 or nx>n or ny>n:
                continue

            x = nx
            y = ny

print(x,y)
