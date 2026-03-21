-- 코드를 작성해주세요
-- 1. 서브쿼리를 사용하여 'Front End' 카테고리에 속하는 모든 스킬 코드의 합을 구합니다.
--    (CODE 값이 2의 제곱수이므로 SUM은 BIT_OR와 같은 역할을 합니다.)
-- 2. DEVELOPERS 테이블의 SKILL_CODE와 위에서 구한 합계를 비트 AND 연산합니다.
-- 3. 연산 결과가 0이 아니면, 해당 개발자는 Front End 스킬을 하나 이상 보유한 것입니다.
SELECT
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS
WHERE
    SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End')
ORDER BY
    ID ASC;