# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 01. 20. 17:01:22

def solution(array, height):
    answer = 0
    for x in array:
        if x > height:
            answer += 1
    return answer


