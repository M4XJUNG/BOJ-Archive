-- 코드를 작성해주세요
WITH RankedEcoli AS (
    -- NTILE(4)를 사용하여 크기 내림차순으로 4개의 분위로 나눕니다.
    SELECT
        ID,
        NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS Quartile
    FROM
        ECOLI_DATA
)
SELECT
    R.ID,
    CASE
        WHEN R.Quartile = 1 THEN 'CRITICAL'
        WHEN R.Quartile = 2 THEN 'HIGH'
        WHEN R.Quartile = 3 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM
    RankedEcoli AS R
ORDER BY
    R.ID ASC;