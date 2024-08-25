-- ProblemSolving for LeetCode SQL
-- 595. Big Countries

SELECT name, population, area FROM World 
WHERE area > 3000000 AND population > 25000000
ORDER BY name desc
