-- Displays the number of records with the same score in the table
-- The number of records for the score has the label 'number'
-- It is sorted in descending order
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
