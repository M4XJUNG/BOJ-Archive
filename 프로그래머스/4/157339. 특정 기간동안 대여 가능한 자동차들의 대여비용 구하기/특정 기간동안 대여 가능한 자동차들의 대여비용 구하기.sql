-- 코드를 입력하세요
-- 1. 2022년 11월에 대여 기록이 있어 대여가 불가능한 자동차 ID 목록을 CTE로 정의
WITH UNAVAILABLE_CARS AS (
    SELECT DISTINCT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-11-30'
)

-- 2. 메인 쿼리에서 차량 정보와 할인 정보를 JOIN하고, 조건에 따라 필터링 및 계산
SELECT
    C.CAR_ID,
    C.CAR_TYPE,
    -- 30일간의 대여 금액을 할인율을 적용하여 계산 (소수점 버림)
    FLOOR(C.DAILY_FEE * 30 * (1 - P.DISCOUNT_RATE / 100)) AS FEE
FROM
    CAR_RENTAL_COMPANY_CAR C
JOIN
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN P ON C.CAR_TYPE = P.CAR_TYPE
WHERE
    C.CAR_TYPE IN ('세단', 'SUV')
    AND P.DURATION_TYPE = '30일 이상'
    -- 위에서 정의한 '대여 불가능한' 자동차를 제외
    AND C.CAR_ID NOT IN (SELECT CAR_ID FROM UNAVAILABLE_CARS)
-- 3. 계산된 FEE를 기준으로 최종 필터링
HAVING
    FEE >= 500000 AND FEE < 2000000
-- 4. 결과 정렬
ORDER BY
    FEE DESC,
    C.CAR_TYPE ASC,
    C.CAR_ID DESC;