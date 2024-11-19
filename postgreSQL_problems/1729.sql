-- ProblemSolving for LeetCode SQL
-- 1729. Find Followers Count

SELECT user_id, COUNT(*) as followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id