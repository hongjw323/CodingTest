import sys

#N, K 입력받기
N, K = map(int, input().split())
cnt = 0

while N > 1:
    if N % K == 0:
        N = N/K
        cnt = cnt+1
    else:
        N = N-1
        cnt = cnt+1

print(cnt)