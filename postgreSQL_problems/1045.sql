-- ProblemSolving for LeetCode SQL
-- 1045. Customers Who Bought All Products

SELECT customer_id 
FROM Customer 
GROUP BY customer_id
HAVING 
    COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM PRODUCT)
