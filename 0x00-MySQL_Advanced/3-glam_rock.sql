-- lists all bands with Glam rock as their main style, ordered by longevity
-- column names are band_name and lifespan

SELECT band_name,
    CASE
        WHEN split IS NULL OR split > 2020 THEN 2020
        ELSE split
    END - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;