n = list(input())

cut = int(len(n)/2)

sum1, sum2 = 0, 0
for i in range(cut):
    sum1 += int(n[i])

for j in range(cut,len(n)):
    sum2 += int(n[j])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")
