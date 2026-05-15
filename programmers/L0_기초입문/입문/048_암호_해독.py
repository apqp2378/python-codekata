# 암호 해독
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 05. 15. 09:15:43

def solution(cipher, code):
    answer = '' 
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i] 
    return answer