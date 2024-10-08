-- ProblemSolving for LeetCode SQL
-- 1587. Bank Account Summary II

SELECT u.name, SUM(t.amount) AS balance
FROM Transactions t
JOIN Users u ON t.account = u.account
GROUP BY u.name, t.account
HAVING SUM(t.amount) > 10000;
