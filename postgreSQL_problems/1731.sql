-- ProblemSolving for LeetCode SQL
-- 1731. The Number of Employees Which Report to Each Employee

SELECT a.employee_id, a.name, count(*) as reports_count, round(avg(b.age)) as average_age
FROM Employees a
JOIN Employees b on a.employee_id = b.reports_to
GROUP BY a.employee_id, a.name
ORDER BY a.employee_id
