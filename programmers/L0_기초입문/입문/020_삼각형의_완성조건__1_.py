# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 01. 21. 09:01:51

def solution(sides):
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        return 1
    else:
        return 2