# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 03. 17. 10:03:17

def solution(hp):
    general = hp // 5
    hp %= 5

    soldier = hp // 3
    hp %= 3

    worker = hp

    return general + soldier + worker