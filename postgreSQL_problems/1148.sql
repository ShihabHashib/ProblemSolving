-- ProblemSolving for LeetCode SQL
-- 1148. Article Views I

SELECT distinct author_id as id
FROM Views
WHERE author_id = viewer_id 
ORDER BY author_id
