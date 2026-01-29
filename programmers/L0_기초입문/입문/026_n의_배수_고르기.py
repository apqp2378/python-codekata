# n의 배수 고르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120905
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 01. 29. 09:08:41

def solution(n, numlist):
    answer = []
    for x in numlist:
        if x % n == 0:
            answer.append(x)
    return answer