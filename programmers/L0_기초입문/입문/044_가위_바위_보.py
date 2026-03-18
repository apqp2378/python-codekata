# 가위 바위 보
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120839
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 03. 18. 09:16:34

def solution(rsp):
    answer = ''
    for ch in rsp:
        if ch == '2':
            answer += '0'
        elif ch == '0':
            answer += '5'
        else:
            answer += '2'
    return answer