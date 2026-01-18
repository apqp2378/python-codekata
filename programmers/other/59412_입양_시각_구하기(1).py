# 입양 시각 구하기(1)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59412
# 작성자: 최상원
# 작성일: 2026. 01. 19. 08:58:22

-- 코드를 입력하세요
SELECT
HOUR(DATETIME) AS HOUR,
COUNT(1) AS COUNT
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY 1
ORDER BY HOUR(DATETIME) ASC
