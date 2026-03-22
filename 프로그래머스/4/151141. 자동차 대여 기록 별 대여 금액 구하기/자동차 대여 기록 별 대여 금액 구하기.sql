-- 코드를 입력하세요
-- 1. '트럭'의 대여 기록과 기간, 적용될 할인 유형을 미리 계산하는 CTE
WITH TRUCK_RENTALS AS (
    SELECT
        H.HISTORY_ID,
        C.DAILY_FEE,
        DATEDIFF(H.END_DATE, H.START_DATE) + 1 AS DURATION,
        -- 대여 기간에 따라 할인 유형을 매핑
        CASE
            WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 90 THEN '90일 이상'
            WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 30 THEN '30일 이상'
            WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 7 THEN '7일 이상'
            ELSE 'NONE' -- 할인 없는 경우를 위한 값
        END AS DURATION_TYPE
    FROM
        CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    JOIN
        CAR_RENTAL_COMPANY_CAR C ON H.CAR_ID = C.CAR_ID
    WHERE
        C.CAR_TYPE = '트럭'
)

-- 2. 위에서 계산된 정보와 할인 정책을 JOIN하여 최종 요금 계산
SELECT
    T.HISTORY_ID,
    -- 최종 요금 계산: 일일요금 * 기간 * (1 - 할인율/100), 소수점 버림
    FLOOR(T.DAILY_FEE * T.DURATION * (1 - IFNULL(P.DISCOUNT_RATE, 0) / 100)) AS FEE
FROM
    TRUCK_RENTALS T
-- 할인 정책 테이블과 LEFT JOIN (할인 없는 경우도 포함하기 위해)
LEFT JOIN
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
    ON T.DURATION_TYPE = P.DURATION_TYPE AND P.CAR_TYPE = '트럭'
-- 3. 결과 정렬
ORDER BY
    FEE DESC,
    T.HISTORY_ID DESC;