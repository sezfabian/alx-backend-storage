-- script that aggregates number of fans by country
CREATE TEMPORARY TABLE countryfans AS
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- script that ranks country origins by number of (non-unique) fans
SELECT origin, nb_fans
FROM countryfans
ORDER BY nb_fans DESC;
