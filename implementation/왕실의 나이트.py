from matplotlib.pyplot import step


place = input()
row = ord(place[0]) - 96
column = int(place[1])

steps = [(-2,-1),(-2,1),(-1,-2),(1,-2),(-1,2),(1,2),(2,-1),(2,1)]
# print(steps[1][0])

cnt = 0
for i in range(len(steps)):
    cnt += 1
    next_row = row + steps[i][0]
    next_col = column + steps[i][1]
    
    if next_row>8 or next_col>8 or next_row<1 or next_col<1 :
        cnt -= 1
    else :
        continue
 
print(cnt)