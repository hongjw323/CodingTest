import sys

N, K = map(int, input().split())
knap = [[0 for _ in range(K+1)] for _ in range(N+1)]

#입력 받기
prod = [[0,0]]
for _ in range(N):
    prod.append(list(map(int, input().split())))

#문제 풀이
weight = 0
value = 0
for i in range(1,N+1):
    for j in range(1,K+1):
        weight = prod[i][0]
        value = prod[i][1]

        if weight > j:
            knap[i][j] = knap[i-1][j]
        else:
            knap[i][j] = max(knap[i-1][j-weight]+value, knap[i-1][j])

print(knap[N][K])
