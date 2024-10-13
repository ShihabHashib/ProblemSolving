-- ProblemSolving for LeetCode SQL
-- 586. Customer Placing the Largest Number of Orders

SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY count(customer_number) DESC
LIMIT 1