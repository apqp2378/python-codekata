# 3월에 태어난 여성 회원 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131120
# 작성자: 최상원
# 작성일: 2026. 01. 16. 15:40:15

-- 코드를 입력하세요
SELECT
MEMBER_ID,
MEMBER_NAME,
GENDER,
DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d') as DATE_OF_BIRTH
FROM MEMBER_PROFILE
where DATE_FORMAT(DATE_OF_BIRTH,'%m') = 03 and TLNO is not null and GENDER = 'W'
order by MEMBER_ID asc