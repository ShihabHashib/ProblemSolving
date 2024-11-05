-- ProblemSolving for LeetCode SQL
-- 1633. Percentage of Users Attended a Contest

SELECT 
    contest_id, 
    ROUND((COUNT(user_id)::numeric / (SELECT COUNT(user_id)::numeric FROM Users)) * 100, 2) AS percentage
FROM 
    Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id