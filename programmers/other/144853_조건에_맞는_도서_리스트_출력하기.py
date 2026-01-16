# 조건에 맞는 도서 리스트 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144853
# 작성자: 최상원
# 작성일: 2026. 01. 16. 15:22:38

-- 코드를 입력하세요
SELECT
BOOK_ID,
DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE 
FROM BOOK 
WHERE PUBLISHED_DATE LIKE '2021%' and CATEGORY = '인문'
ORDER BY PUBLISHED_DATE ASC