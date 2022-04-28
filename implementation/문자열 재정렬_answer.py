data = input()

result = []
sum = 0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        sum += int(x)

result.sort()

if sum != 0:
    result.append(str(sum))

answer = ''.join(result)
print(answer)