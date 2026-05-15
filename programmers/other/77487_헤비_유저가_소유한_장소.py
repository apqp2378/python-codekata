# 헤비 유저가 소유한 장소
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77487
# 작성자: 최상원
# 작성일: 2026. 05. 15. 09:18:19

-- 코드를 입력하세요
SELECT
ID,
NAME,
HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT
    HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(*) >= 2
)
ORDER BY ID;