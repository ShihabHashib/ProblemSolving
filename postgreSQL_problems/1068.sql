-- ProblemSolving for LeetCode SQL
-- 1068. Product Sales Analysis I

SELECT product_name, year, price 
FROM Sales as s
JOIN Product as p ON s.product_id = p.product_id