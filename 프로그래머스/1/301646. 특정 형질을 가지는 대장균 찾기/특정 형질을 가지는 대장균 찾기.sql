-- 코드를 작성해주세요
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0   -- 2번 형질이 없음
  AND (GENOTYPE & 1 OR GENOTYPE & 4) = 1;  -- 1번이나 3번 형질을 가짐