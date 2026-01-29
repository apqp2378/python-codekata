# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 01. 29. 09:02:19

def solution(n):
    answer = 0
    for a in range(1,n+1):
        if n % a == 0:
            answer += 1
    return answer