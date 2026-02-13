# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 02. 13. 09:08:11

def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even,odd]