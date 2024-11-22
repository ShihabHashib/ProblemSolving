-- ProblemSolving for LeetCode SQL
-- 1667. Fix Names in a Table

SELECT 
    user_id, 
    CONCAT(upper(substring(name, 1, 1)), lower(substring(name, 2))) AS name
FROM 
    users
ORDER BY 
    user_id;