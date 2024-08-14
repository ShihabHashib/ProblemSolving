--  ProblemSolving for LeetCode SQL
--  175. Combine Two Tables

SELECT firstName, lastName, city, state
FROM Person p LEFT OUTER JOIN Address a
ON p.personId = a.personId;