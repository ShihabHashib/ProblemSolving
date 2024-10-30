-- ProblemSolving for LeetCode SQL
-- 1327. List the Products Ordered in a Period

SELECT product_name, sum(unit) as unit
FROM Orders
JOIN Products p using (product_id)
WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY product_id, product_name
Having sum(unit) > 99