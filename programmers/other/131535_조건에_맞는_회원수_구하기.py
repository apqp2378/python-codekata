# 조건에 맞는 회원수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131535
# 작성자: 최상원
# 작성일: 2026. 01. 16. 14:56:13

-- 코드를 입력하세요
SELECT
count(user_id)
from USER_INFO 
where JOINED like '2021%' and age between 20 and 29
