-- ranks country origins of bands, ordered by the number of (non-unique) fans
-- column names are origin, nb_fans
-- origin is the country of origin of the band
-- nb_fans is the number of unique fans that the bands have in that country
SELECT origin, SUM(fans) AS fans
FROM metal_bands
GROUP BY origin
ORDER BY SUM(fans) DESC;
