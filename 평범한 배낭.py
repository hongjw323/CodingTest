# 백준 12865번 https://www.acmicpc.net/problem/12865
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
        weight = prod[i][0] #현재 물품의 무게
        value = prod[i][1]  #현재 물품의 가치

        if weight > j:
            knap[i][j] = knap[i-1][j]   #i번째 물품을 챙기지 않았을 때 최댓값
        else:
            knap[i][j] = max(knap[i-1][j-weight]+value, knap[i-1][j])   #i번째 물품을 챙겼을 때 최댓값

print(knap[N][K])
