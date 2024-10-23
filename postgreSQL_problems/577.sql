-- ProblemSolving for LeetCode SQL
-- 577. Employee Bonus

SELECT name, bonus
FROM Employee 
FULL JOIN Bonus using (empId)
WHERE bonus < 1000 OR bonus is null
