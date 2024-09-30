-- ProblemSolving for LeetCode SQL
-- 607. Sales Person

SELECT name
FROM SalesPerson
WHERE sales_id not in (
    SELECT sales_id
    FROM Orders as o
    JOIN Company as c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)
