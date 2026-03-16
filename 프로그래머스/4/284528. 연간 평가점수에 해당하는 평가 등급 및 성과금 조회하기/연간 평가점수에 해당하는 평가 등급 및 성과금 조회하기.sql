-- 코드를 작성해주세요
-- 1. 사원별 평균 점수를 계산하는 CTE(Common Table Expression) 정의
WITH AVG_GRADE AS (
    SELECT
        EMP_NO,
        AVG(SCORE) AS SCORE_AVG
    FROM
        HR_GRADE
    GROUP BY
        EMP_NO
)

-- 2. 사원 정보와 평균 점수를 조인하여 등급 및 성과금 계산
SELECT
    E.EMP_NO,
    E.EMP_NAME,
    -- 평균 점수에 따라 GRADE 부여
    CASE
        WHEN G.SCORE_AVG >= 96 THEN 'S'
        WHEN G.SCORE_AVG >= 90 THEN 'A'
        WHEN G.SCORE_AVG >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    -- 평균 점수에 따라 BONUS 계산
    CASE
        WHEN G.SCORE_AVG >= 96 THEN E.SAL * 0.20
        WHEN G.SCORE_AVG >= 90 THEN E.SAL * 0.15
        WHEN G.SCORE_AVG >= 80 THEN E.SAL * 0.10
        ELSE 0
    END AS BONUS
FROM
    HR_EMPLOYEES AS E
JOIN
    AVG_GRADE AS G ON E.EMP_NO = G.EMP_NO
ORDER BY
    E.EMP_NO ASC;