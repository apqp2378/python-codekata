# 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/151137
# 작성자: 최상원
# 작성일: 2026. 01. 19. 09:23:26

-- 코드를 입력하세요
SELECT
CAR_TYPE,
COUNT(1) AS CARS
FROM CAR_RENTAL_COMPANY_CAR 
WHERE OPTIONS LIKE '%통풍시트%'
   OR OPTIONS LIKE '%열선시트%'
   OR OPTIONS LIKE '%가죽시트%'
GROUP BY 1
ORDER BY CAR_TYPE ASC
