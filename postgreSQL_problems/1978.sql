-- ProblemSolving for LeetCode SQL
-- 619. Biggest Single Number

SELECT MAX(num) as num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS n
