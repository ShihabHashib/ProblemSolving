-- ProblemSolving for LeetCode SQL
-- 184. Department Highest Salary

SELECT  d.name as Department,
        e.name as Employee, 
        e.salary as Salary
        
FROM Employee e
JOIN Department d on e.departmentId = d.id

WHERE (e.salary, e.departmentId) IN (
    SELECT  MAX(salary), departmentId
    FROM Employee
    GROUP BY departmentId
)