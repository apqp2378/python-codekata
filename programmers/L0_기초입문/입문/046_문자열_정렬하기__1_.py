# 문자열 정렬하기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 04. 06. 09:40:22

def solution(my_string):
    answer = []

    for ch in my_string:
        if ch.isdigit():
            answer.append(int(ch))
    answer.sort()
    return answer