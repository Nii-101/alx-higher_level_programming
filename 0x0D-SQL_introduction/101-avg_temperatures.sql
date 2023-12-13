-- Displays avg temperature of city
-- Ordered by descending temp. values

SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
