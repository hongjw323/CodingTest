input_data = input()

row = int(input_data[1])    #행
column = int(ord(input_data[0]))-ord('a')+1     #열(a~h를 1~8로 변환)

#움직일 수 있는 경우의 수
steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

cnt = 0
for step in steps:
    cnt += 1
    
    #이동하고자 하는 위치
    next_row = row + step[0]
    next_col = column + step[1]

    if next_row < 1 or next_col < 1 or next_row > 8 or next_col > 8:
        cnt -= 1
        continue


print(cnt)