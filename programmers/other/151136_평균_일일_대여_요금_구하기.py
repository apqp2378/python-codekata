# 평균 일일 대여 요금 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/151136
# 작성자: 최상원
# 작성일: 2026. 01. 16. 15:33:43

-- 코드를 입력하세요
SELECT
ROUND(SUM(DAILY_FEE)/COUNT(DAILY_FEE),0) AS AVERAGE_FEE 
from CAR_RENTAL_COMPANY_CAR 
WHERE CAR_TYPE = 'SUV'
