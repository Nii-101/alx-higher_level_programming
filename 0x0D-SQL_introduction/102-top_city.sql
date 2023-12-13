-- Displays the top 3 city temperatures during July and August
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
