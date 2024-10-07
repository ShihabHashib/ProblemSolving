-- ProblemSolving for LeetCode SQL
-- 1581. Customer Who Visited but Did Not Make Any Transactions

SELECT v.customer_id, count(*) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE transaction_id is null
GROUP BY customer_id