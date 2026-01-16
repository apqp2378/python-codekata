# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 01. 16. 23:24:19

def solution(n, k):
    return 12000 * n + 2000 * k - 2000 * min(n//10, k)