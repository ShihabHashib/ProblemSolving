-- ProblemSolving for LeetCode SQL
-- 183. Customers Who Never Order

SELECT name AS Customers  
FROM Customers a LEFT OUTER JOIN Orders b
ON a.id = b.customerId 
WHERE customerId is null
