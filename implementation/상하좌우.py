n = int(input())
plans = input().split()

type = ['L', 'R', 'U', 'D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

x,y = 1,1
nx,ny = 0,0

for plan in plans:
    for i in range(len(type)):
        if plan == type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<1 or nx>n or ny<1 or ny>n :
                nx = x
                ny = y
        else :
            continue
        
        # print(nx,ny)
        x = nx
        y = ny

print(x,y)