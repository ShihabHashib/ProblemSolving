-- ProblemSolving for LeetCode SQL
-- 197. Rising Temperature

SELECT c.id FROM weather c
JOIN weather p
ON c.recordDate = p.recordDate + 1
WHERE c.temperature > p.temperature
