-- ProblemSolving for LeetCode SQL
-- 1517. Find Users With Valid E-Mails

SELECT *
FROM Users
WHERE mail ~ '^[a-zA-Z]+[a-zA-Z0-9_.-]*@leetcode\.com$'
