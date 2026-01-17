# 동명 동물 수 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59041
# 작성자: 최상원
# 작성일: 2026. 01. 17. 09:36:02

-- 코드를 입력하세요
SELECT
name,
count(name) as COUNT
from ANIMAL_INS 
group by name
HAVING count(name) >= 2
ORDER BY NAME