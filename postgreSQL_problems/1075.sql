-- ProblemSolving for LeetCode SQL
-- 1075. Project Employees I

SELECT project_id, ROUND(AVG(experience_years)::numeric, 2) as average_years
FROM Project p
LEFT JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY project_id