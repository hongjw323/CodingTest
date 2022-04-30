# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    unit = len(s) // 2
    answer = len(s)
    for i in range(1,unit+1):
        cnt = 1
        compressed = ""
        part = s[0:i]
        for j in range(i,len(s),i):
            if part == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += str(cnt) + part
                else:
                    compressed += part
                cnt = 1
                part = s[j:j+i]
        if cnt > 1:
            compressed += str(cnt) + part
        else:
            compressed += part
        answer = min(answer,len(compressed))
        
    return answer