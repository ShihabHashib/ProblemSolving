-- ProblemSolving for LeetCode SQL
-- 1484. Group Sold Products By The Date

SELECT  sell_date,
COUNT(DISTINCT product) as num_sold,
STRING_AGG(DISTINCT product, ',') as products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date