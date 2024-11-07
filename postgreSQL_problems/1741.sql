-- ProblemSolving for LeetCode SQL
-- 1741. Find Total Time Spent by Each Employee

SELECT event_day as day, emp_id, (sum(out_time) - sum(in_time)) as total_time
FROM Employees
GROUP BY emp_id, event_day