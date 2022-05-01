# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    english = ['zero','one','two','three','four','five','six','seven','eight','nine']
    num = 0
    for e in range(len(english)):
        if english[e] in s:
            s = s.replace(english[e],str(num))
        num += 1
        
    answer = int(s)
    return answer