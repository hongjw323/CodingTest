n = int(input())
danger = list(map(int, input().split()))

danger.sort()

group = 0   #현재 그룹의 모험가 수
cnt = 0     #만들어진 그룹 수

for i in danger:
    group += 1  #그룹 내 모험가 추가
    # 공포도보다 그룹 내 모험가가 더 많거나 같다면 그룹 생성 / 아니면 모험가 추가
    if group >= i:
        cnt += 1    #그룹 추가
        group = 0   #현재 그룹에 포함된 모험가 수 초기화

print(cnt)
