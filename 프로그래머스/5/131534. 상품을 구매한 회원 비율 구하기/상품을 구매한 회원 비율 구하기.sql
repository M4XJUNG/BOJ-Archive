-- 코드를 입력하세요
-- 1. 2021년에 가입한 회원을 필터링하기 위해 USER_INFO와 ONLINE_SALE를 JOIN합니다.
-- 2. 판매일(SALES_DATE)을 기준으로 년/월별 그룹을 만듭니다.
-- 3. 각 그룹 내에서 고유한 구매 회원 수(COUNT DISTINCT)를 계산합니다.
-- 4. 비율 계산을 위해 서브쿼리로 2021년 전체 가입자 수를 구하고, 이를 분모로 사용합니다.
SELECT
    YEAR(O.SALES_DATE) AS YEAR,
    MONTH(O.SALES_DATE) AS MONTH,
    -- 년/월별로 구매한 고유 회원 수를 집계
    COUNT(DISTINCT U.USER_ID) AS PUCHASED_USERS,
    -- (월별 구매 회원 수 / 2021년 전체 가입 회원 수)를 계산하고 반올림
    ROUND(
        COUNT(DISTINCT U.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED) = 2021),
        1
    ) AS PUCHASED_RATIO
FROM
    USER_INFO U
JOIN
    ONLINE_SALE O ON U.USER_ID = O.USER_ID
WHERE
    YEAR(U.JOINED) = 2021 -- 2021년에 가입한 회원만 대상으로 필터링
GROUP BY
    YEAR, MONTH
ORDER BY
    YEAR ASC,
    MONTH ASC;