import re

n = input()
number = re.findall(r'\d',n)

sum = 0
for i in range(len(number)):
    sum += int(number[i])

n_list = list(n)
n_list.sort()

result = n_list[len(number):]
result.append(str(sum))

print(''.join(result))

# => 숫자를 입력하지 않은 경우, 0으로 붙어버림