n, m, k = map(int, input().split()) #n,m,k 입력받기
data = list(map(int, input().split())) #숫자 입력받기

data.sort(reverse=True) #내림차순 정렬
first = data[0]
second = data[1]

sum = 0
while True:
    for i in range(k):  #가장 큰 수 더하기
        sum += first
        m -= 1
        if m == 0:
            break

    sum += second
    m -= 1
    if m == 0:
        break

print(sum)
