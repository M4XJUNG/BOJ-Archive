-- 코드를 작성해주세요
-- 1. 재귀적 CTE(Recursive CTE)를 사용하여 각 개체의 세대를 결정합니다.
WITH RECURSIVE GENERATION_DATA AS (
    -- 기본 케이스(Anchor Member): 1세대 (부모 ID가 NULL인 개체)
    SELECT
        ID,
        PARENT_ID,
        1 AS GENERATION
    FROM
        ECOLI_DATA
    WHERE
        PARENT_ID IS NULL

    UNION ALL

    -- 재귀 케이스(Recursive Member): 이전 세대와 JOIN하여 다음 세대를 결정
    SELECT
        E.ID,
        E.PARENT_ID,
        G.GENERATION + 1
    FROM
        ECOLI_DATA E
    JOIN
        GENERATION_DATA G ON E.PARENT_ID = G.ID
)

-- 2. 위에서 구한 세대 정보와 자식이 없는 개체 정보를 결합하여 집계합니다.
SELECT
    -- 자식이 없는 개체의 수를 셉니다.
    COUNT(*) AS COUNT,
    -- 세대를 그룹화합니다.
    GENERATION
FROM
    GENERATION_DATA
WHERE
    -- 현재 개체의 ID가 다른 개체의 부모 ID 목록에 없는 경우 (자식이 없는 경우)
    ID NOT IN (SELECT DISTINCT PARENT_ID FROM ECOLI_DATA WHERE PARENT_ID IS NOT NULL)
GROUP BY
    GENERATION
ORDER BY
    GENERATION ASC;