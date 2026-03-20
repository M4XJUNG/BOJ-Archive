-- 코드를 입력하세요
-- 1. RECURSIVE CTE를 사용하여 0부터 23까지의 시간 테이블을 생성
WITH RECURSIVE hours (h) AS (
    SELECT 0
    UNION ALL
    SELECT h + 1 FROM hours WHERE h < 23
)

-- 2. 생성된 시간 테이블에 실제 입양 데이터를 LEFT JOIN
SELECT
    h.h AS HOUR,
    IFNULL(COUNT(A.ANIMAL_ID), 0) AS COUNT
FROM
    hours h
LEFT JOIN
    ANIMAL_OUTS AS A ON h.h = HOUR(A.DATETIME)
GROUP BY
    h.h
ORDER BY
    HOUR ASC;