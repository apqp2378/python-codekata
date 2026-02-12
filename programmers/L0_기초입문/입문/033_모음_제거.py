# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 최상원
# 작성일: 2026. 02. 12. 09:15:09

def solution(my_string):
    vowel = 'aeiou'
    answer = ''
    for i in my_string:
        if i not in vowel:
            answer += i        
    return answer