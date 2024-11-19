-- ProblemSolving for LeetCode SQL
-- 626. Exchange Seats

SELECT(
    CASE
        WHEN id % 2 = 1 and id = (SELECT MAX(id) from Seat) THEN id
        WHEN id % 2 = 1 THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
    END 
) as id, student
FROM Seat
ORDER BY id