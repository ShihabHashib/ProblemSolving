-- ProblemSolving for LeetCode SQL
-- 1050. Actors and Directors Who Cooperated At Least Three Times

SELECT actor_id, director_id FROM ActorDirector 
GROUP BY actor_id, director_id
HAVING COUNT(timestamp) > 2;
