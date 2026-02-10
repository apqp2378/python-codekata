# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 02. 10. 09:10:57

def solution(n):
    answer = n ** 0.5
    if answer == int(answer):
        return 1
    else:
        return 2