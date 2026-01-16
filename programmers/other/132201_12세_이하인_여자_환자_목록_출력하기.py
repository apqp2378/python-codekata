# 12세 이하인 여자 환자 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132201
# 작성자: 최상원
# 작성일: 2026. 01. 16. 15:04:43

-- 코드를 입력하세요
SELECT
PT_NAME,
PT_NO,
GEND_CD,
AGE,
IFNULL(TLNO,'NONE') AS TLNO
from PATIENT 
where age <=12 and GEND_CD = 'W'
order by age desc, PT_NAME