#반복되는 수열을 이용해 문제 풀이 - [가장 큰 수*k, 두번째 큰 수]의 반복

n, m, k = map(int, input().split()) #n, m, k 값 입력받기
data = list(map(int, input().split()))  #n개의 수 입력받기

data.sort() #입력받은 수 정렬
first = data[n-1]   #가장 큰 수
second = data[n-2]  #두번째로 큰 수

#가장 큰 수가 더해지는 횟수 계산
count = (m/(k+1)) * k
count += m % (k+1)

result = 0
result += count*first
result += (m-count) * second

print(result)
