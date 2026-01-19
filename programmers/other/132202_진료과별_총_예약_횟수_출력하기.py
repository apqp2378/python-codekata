# 진료과별 총 예약 횟수 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132202
# 작성자: 최상원
# 작성일: 2026. 01. 19. 09:10:48

-- 코드를 입력하세요
SELECT
MCDP_CD AS 진료과코드,
COUNT(1) AS 5월예약건수
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY 2,MCDP_CD