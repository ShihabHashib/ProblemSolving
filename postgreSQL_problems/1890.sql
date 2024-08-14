-- ProblemSolving for LeetCode SQL
-- 1890. The Latest Login in 2020

SELECT user_id, MAX(time_stamp) last_stamp
from Logins 
where 
    DATE_PART('year', time_stamp) = 2020
GROUP BY 1