# 카테고리 별 도서 판매량 집계하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144855
# 작성자: 최상원
# 작성일: 2026. 01. 19. 15:56:08

-- 코드를 입력하세요
SELECT
CATEGORY,
SUM(BS.SALES) as TOTAL_SALES
from BOOK B
join BOOK_SALES BS 
on B.BOOK_ID = BS.BOOK_ID
WHERE BS.SALES_DATE >= '2022-01-01' and BS.SALES_DATE < '2022-02-01'
GROUP BY CATEGORY
order by CATEGORY