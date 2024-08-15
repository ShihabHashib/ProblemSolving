-- ProblemSolving for LeetCode SQL
-- 176. Second Highest Salary

select (
    SELECT DISTINCT salary AS SecondHighestSalary 
    FROM Employee 
    ORDER by salary desc
    OFFSET 1 LIMIT 1
)


-- SELECT (array_agg(salary order by salary desc))[2] as SecondHighestSalary 
-- FROM Employee
