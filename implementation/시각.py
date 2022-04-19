n = int(input())
i_cnt, s_cnt, m_cnt = 0,0,0

for i in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(s):
                s_cnt += 1
        if '3' in str(m):
            m_cnt += 1
    if '3' in str(i):
        i_cnt += 1
        
print(i_cnt + s_cnt + m_cnt)