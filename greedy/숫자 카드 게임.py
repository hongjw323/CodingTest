n, m = map(int, input().split())    #nxm 입력받기

num = []
for i in range(n):
    data = list(map(int, input().split()))  #행 입력받기
    
    small = min(data)   #행에서 가장 작은 값
    num.append(small)

print(max(num))
