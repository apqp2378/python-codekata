# 루시와 엘라 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59046
# 작성자: 최상원
# 작성일: 2026. 01. 16. 15:12:09

-- 코드를 입력하세요
SELECT
ANIMAL_ID,
NAME,
SEX_UPON_INTAKE
FROM ANIMAL_INS 
WHERE NAME IN('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')