# https://programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict

def solution(id_list, report, k):
    reporting = defaultdict(set)
    reported = defaultdict(set)
    
    for r in report:
        a, b = r.split(' ')
        reporting[a].add(b)
        reported[b].add(a)
    
    answer = []
    for id in id_list:
        cnt = 0
        for i in reporting[id]:
            if len(reported[i]) >= k:
                cnt += 1
            else:
                continue
        answer.append(cnt)
    
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/92334/solution_groups?language=python3

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}   
    
    #id별 신고당한 횟수
    for r in set(report):
        reports[r.split()[1]] += 1
    
    #id별 메일받는 횟수
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer