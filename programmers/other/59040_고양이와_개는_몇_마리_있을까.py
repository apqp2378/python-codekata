# 고양이와 개는 몇 마리 있을까
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59040
# 작성자: 최상원
# 작성일: 2026. 01. 17. 09:52:50

-- 코드를 입력하세요
SELECT
ANIMAL_TYPE,
COUNT(1) as count
FROM ANIMAL_INS 
group by 1
order by ANIMAL_TYPE