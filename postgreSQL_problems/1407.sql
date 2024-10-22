-- ProblemSolving for LeetCode SQL
-- 1407. Top Travellers

SELECT 
    u.name, 
    coalesce(sum(r.distance), 0) as travelled_distance 
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY r.user_id, u.name
ORDER BY travelled_distance DESC, u.name
