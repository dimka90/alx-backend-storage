-- Select the band name and calculate the lifespan of each band
SELECT band_name , COALESCE(split, 2022) - formed AS lifespan
-- From the table named 'metal_bands'
FROM metal_bands
-- Filter bands whose style contains the phrase 'Glam rock'
WHERE style Like '%Glam rock%'
-- Order the results by the calculated lifespan in descending order
ORDER BY  lifespan  DESC;