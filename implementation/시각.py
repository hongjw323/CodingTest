n = int(input())

cnt = 0
for h in range(n+1):    #시
    for m in range(60):     #분
        for s in range(60):     #초
            
            #3 들어가면 더하기
            if '3' in str(h)+str(m)+str(s):
                cnt += 1

print(cnt)