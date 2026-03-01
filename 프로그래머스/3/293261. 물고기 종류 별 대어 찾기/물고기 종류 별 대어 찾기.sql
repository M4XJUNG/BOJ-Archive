-- 코드를 작성해주세요
SELECT
    I.ID,
    N.FISH_NAME,
    I.LENGTH
FROM
    FISH_INFO AS I
JOIN
    FISH_NAME_INFO AS N ON I.FISH_TYPE = N.FISH_TYPE
WHERE
    (I.FISH_TYPE, I.LENGTH) IN (
        -- 각 물고기 종류별로 최대 길이를 구하는 서브쿼리
        SELECT
            FISH_TYPE,
            MAX(LENGTH)
        FROM
            FISH_INFO
        GROUP BY
            FISH_TYPE
    )
ORDER BY
    I.ID ASC;