n = input()
length = len(n)
summary = 0

# 왼쪽 부분의 자릿수 합 구하기
for i in range(length//2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for j in range(length//2, length):
    summary -= int(n[j])

if summary == 0:
    print("LUCKY")
else:
    print("READY")