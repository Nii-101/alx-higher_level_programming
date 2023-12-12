-- Lists all records of the table with the name value
-- The records are ordered in Descending score
-- Score first, then name
SELECT score, name FROM second_table WHERE name IS NOT NULL
GROUP by score, name
ORDER BY score DESC;
