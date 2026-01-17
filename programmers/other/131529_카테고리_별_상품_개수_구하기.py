# 카테고리 별 상품 개수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131529
# 작성자: 최상원
# 작성일: 2026. 01. 17. 09:41:37

-- 코드를 입력하세요
SELECT
left(PRODUCT_CODE,2) as CATEGORY,
count(PRODUCT_CODE) as PRODUCTS
from PRODUCT 
group by left(PRODUCT_CODE,2)