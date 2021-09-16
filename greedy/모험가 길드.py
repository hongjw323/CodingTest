n = int(input())
danger = list(map(int, input().split()))

danger.sort(reverse=True)

cnt = 0
while True:
    big = danger[0]
    
    if big <= len(danger):
        danger = danger[big:]
        cnt += 1
        if len(danger) == 0:
            break
    else:
        break
    #print(danger)

print(cnt)