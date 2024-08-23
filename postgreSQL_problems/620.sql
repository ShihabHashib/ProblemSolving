-- ProblemSolving for LeetCode SQL
-- 620. Not Boring Movies

SELECT * FROM Cinema
WHERE id % 2 != 0 AND description != 'boring'
ORDER by rating desc