# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 01. 19. 16:22:33

def solution(numbers):
    answer = 0
    for n in numbers:
        answer += n
    return answer / len(numbers)