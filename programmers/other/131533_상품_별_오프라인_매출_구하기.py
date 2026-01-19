# 상품 별 오프라인 매출 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131533
# 작성자: 최상원
# 작성일: 2026. 01. 19. 16:10:26

-- 코드를 입력하세요
SELECT
PRODUCT_CODE,
SUM(p.PRICE * OS.SALES_AMOUNT) AS SALES
from PRODUCT AS P
JOIN OFFLINE_SALE AS OS
ON P.PRODUCT_ID = OS.PRODUCT_ID
group by PRODUCT_CODE
order by SALES DESC, PRODUCT_CODE