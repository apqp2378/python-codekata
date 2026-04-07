# 최댓값 만들기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 04. 07. 09:43:52

def solution(numbers):
    numbers.sort()

    first = numbers[0] * numbers[1]
    last = numbers[-1] * numbers[-2]

    return max(first, last)