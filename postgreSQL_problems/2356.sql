-- ProblemSolving for LeetCode SQL
-- 2356. Number of Unique Subjects Taught by Each Teacher

SELECT teacher_id, COUNT(DISTINCT subject_id) as cnt 
FROM Teacher 
GROUP BY teacher_id 
