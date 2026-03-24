-- 코드를 작성해주세요
-- 1. WITH 절(CTE)을 사용하여 필요한 스킬 코드들을 미리 정의합니다.
WITH SKILL_CODES AS (
    SELECT
        (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') AS PYTHON_CODE,
        (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') AS CSHARP_CODE,
        (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End') AS FRONT_END_CODE
),
-- 2. 각 개발자별로 등급을 부여하는 CTE를 만듭니다.
DEVELOPER_GRADES AS (
    SELECT
        -- CASE 문을 사용하여 우선순위(A -> B -> C)에 따라 등급을 부여합니다.
        CASE
            -- A 등급: Front End와 Python 스킬을 모두 보유
            WHEN D.SKILL_CODE & S.FRONT_END_CODE AND D.SKILL_CODE & S.PYTHON_CODE THEN 'A'
            -- B 등급: C# 스킬을 보유
            WHEN D.SKILL_CODE & S.CSHARP_CODE THEN 'B'
            -- C 등급: Front End 스킬을 보유
            WHEN D.SKILL_CODE & S.FRONT_END_CODE THEN 'C'
            ELSE NULL
        END AS GRADE,
        D.ID,
        D.EMAIL
    FROM
        DEVELOPERS D, SKILL_CODES S
)
-- 3. 등급이 부여된(NULL이 아닌) 개발자만 조회하고 정렬합니다.
SELECT
    GRADE,
    ID,
    EMAIL
FROM
    DEVELOPER_GRADES
WHERE
    GRADE IS NOT NULL
ORDER BY
    GRADE ASC,
    ID ASC;