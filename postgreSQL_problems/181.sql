-- ProblemSolving for LeetCode SQL
-- 181. Employees Earning More Than Their Managers

SELECT e.name AS Employee
FROM Employee e
LEFT JOIN Employee m ON m.id = e.managerId

WHERE e.salary > m.salary
