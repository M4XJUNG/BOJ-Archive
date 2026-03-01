-- 코드를 입력하세요
SELECT
    II.ITEM_ID,
    II.ITEM_NAME,
    II.RARITY
FROM
    ITEM_INFO AS II
WHERE
    II.ITEM_ID NOT IN (
        -- 업그레이드의 부모가 되는 모든 아이템 ID를 선택합니다.
        -- PARENT_ITEM_ID가 NULL인 경우는 루트 아이템이므로 제외합니다.
        SELECT PARENT_ITEM_ID
        FROM ITEM_TREE
        WHERE PARENT_ITEM_ID IS NOT NULL
    )
ORDER BY
    II.ITEM_ID DESC;